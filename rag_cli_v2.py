import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["HF_HUB_OFFLINE"] = "1"
import time
import chromadb
from chromadb.utils import embedding_functions
from FlagEmbedding import FlagReranker
import torch
import gc
import re
import sys
import math
import json
import frontmatter
import hashlib
from datetime import datetime

# Windows 터미널 출력 인코딩 강제 설정 (UTF-8)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# ================= CONFIG (V7.7 Enterprise Edition) =================
SEARCH_PATHS = [r"C:\Anitigravity\02_Knowledge", r"C:\Anitigravity\03_External_Data"]
DB_PATH = r"C:\Anitigravity\rag_db"
EXCLUDE_DIRS = ['.obsidian', '.smart-env', 'rag_db', 'node_modules', '04_Tools', 'Archive', 'lectures', '_Archive_Source', '_backups', '_Archive_LowDensity']
COLLECTION_NAME = "antigravity_fabric_v77_enterprise" 
# ======================================================================

_client = None
_collection = None
_bge_ef = None
_reranker = None

def get_collection():
    global _client, _collection, _bge_ef
    if _collection is None:
        log(f"[INIT] Loading BGE-M3 Embedding Model on CUDA...")
        _bge_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-m3", device="cuda")
        _client = chromadb.PersistentClient(path=DB_PATH)
        _collection = _client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=_bge_ef)
    return _collection

def get_reranker():
    global _reranker
    if _reranker is None:
        log(f"[INIT] Loading BGE-Reranker-V2-M3...")
        _reranker = FlagReranker('BAAI/bge-reranker-v2-m3', use_fp16=True)
    return _reranker

def log(msg):
    with open("rag_sync_v7.log", "a", encoding="utf-8") as f:
        f.write(f"[{time.ctime()}] {msg}\n")
    print(msg, flush=True)

def calculate_dynamic_trust(t_static, doc_date_str, decay_rate):
    try:
        # doc_date_str가 date 객체 형태 등 문자열에 상관없이 안전 변환
        doc_date_str = str(doc_date_str).split(" ")[0].strip()
        doc_date = datetime.strptime(doc_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        days_passed = (current_date - doc_date).days
        # V7.7 JIT 감쇄 연산 공식: 30일(1개월) 단위 비례 감쇄
        t_dynamic = t_static - (decay_rate * (days_passed / 30.0))
        return max(t_dynamic, 0.1)
    except Exception:
        return t_static

def sync_vault():
    CHECKPOINT_PATH = os.path.join(DB_PATH, "sync_checkpoint_v77.json")
    checkpoint = {}
    if not os.path.exists(DB_PATH):
        os.makedirs(DB_PATH)
    if os.path.exists(CHECKPOINT_PATH):
        try:
            with open(CHECKPOINT_PATH, 'r', encoding='utf-8') as f:
                checkpoint = json.load(f)
        except Exception: pass

    log(f"🚀 Starting Antigravity V7.7 Enterprise Unified Intelligence Global Sync")
    
    all_md_files = []
    for base_path in SEARCH_PATHS:
        if not os.path.exists(base_path): continue
        for dp, dn, filenames in os.walk(base_path):
            path_parts = set(re.split(r'[\\/]', dp))
            if any(exclude in path_parts for exclude in EXCLUDE_DIRS): continue
            for f in filenames:
                if f.endswith('.md'):
                    all_md_files.append(os.path.join(dp, f))

    to_sync = [f for f in all_md_files if f not in checkpoint or checkpoint[f] < os.path.getmtime(f)]
    
    if not to_sync:
        log("✅ [DONE] All nodes are synchronized with V7.7 Enterprise Fabric.")
        return

    log(f"🎯 [PLAN] {len(to_sync)} nodes identified for V7.7 Enterprise Hybrid Integration.")
    
    BATCH_SIZE = 4 # RTX 4060 8GB Safety Buffer
    for i in range(0, len(to_sync), BATCH_SIZE):
        batch_files = to_sync[i:i + BATCH_SIZE]
        documents = []; metadatas = []; ids = []
        
        for file_path in batch_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    raw_content = f.read()
                    post = frontmatter.loads(raw_content)
                    meta_raw = post.metadata
                    body_text = post.content
                    
                    # [V7.6.2 하이브리드 대소문자 방어선]
                    metadata = meta_raw.get('metadata', meta_raw.get('Basic', {}))
                    object_data = meta_raw.get('object', meta_raw.get('Object', {}))
                    semantic = meta_raw.get('semantic', meta_raw.get('Semantic', {}))
                    lineage = meta_raw.get('lineage', meta_raw.get('Lineage', {}))
                    spo_graph = meta_raw.get('spo_graph', meta_raw.get('SPO_Graph', []))
                    dynamic = meta_raw.get('dynamic', meta_raw.get('Dynamic', {}))
                    trust_metrics = meta_raw.get('trust_metrics', meta_raw.get('Trust Metrics', {}))

                    domain = metadata.get('domain', 'Unknown')
                    version = metadata.get('version', 'Legacy')
                    tier = int(object_data.get('tier', 1))
                    object_type = object_data.get('object_type', 'Concept')
                    
                    # T_static 및 decay_rate 대소문자/구조 예외 안전장치 (V7.7)
                    t_static_raw = trust_metrics.get('T_static', 1.0)
                    if isinstance(t_static_raw, dict):
                        t_static = float(next(iter(t_static_raw.values()), 1.0))
                    else:
                        t_static = float(t_static_raw)
                        
                    # decay_rate를 trust_metrics 블록에서 우선 탐색 (V7.7), 없을 시 dynamic 블록 탐색 (V7.6.2)
                    decay_rate = float(trust_metrics.get('decay_rate', dynamic.get('decay_rate', 0.0)))
                    
                    # [V7.7 핫픽스] date 객체 직결 에러 방어: 문자열 변환 강제
                    doc_date_raw = metadata.get('date', datetime.now().strftime("%Y-%m-%d"))
                    doc_date = str(doc_date_raw).split(" ")[0].strip()

                    # [V7.7 단일 상속 DAG 강제] List 다중 상속 폐기 및 단일 문자열 압축
                    is_instance_raw = semantic.get('is_instance_of', '')
                    if isinstance(is_instance_raw, list):
                        is_instance_str = str(is_instance_raw[0]) if is_instance_raw else ""
                        log(f"  [⚠️ DAG WARNING] Multiple inheritance detected in {os.path.basename(file_path)}! Bounded strictly to '{is_instance_str}' for single inheritance.")
                    else:
                        is_instance_str = str(is_instance_raw)
                    
                    expected_queries = semantic.get('expected_queries', [])
                    queries_text = "\n".join(expected_queries) if expected_queries else ""
                    
                    graph_text = ""
                    if isinstance(spo_graph, list):
                        for triple in spo_graph:
                            if isinstance(triple, dict):
                                s = triple.get('subject', '')
                                p = triple.get('predicate', '')
                                o = triple.get('object', '')
                                graph_text += f"({s} --{p}--> {o})\n"

                    # 융합 문서 생성
                    fused_text = f"[Domain: {domain}]\n[Type: {object_type}]\n[Parent: {is_instance_str}]\n[Graph]\n{graph_text}\n[Queries]\n{queries_text}\n---\n{body_text}"
                    
                    documents.append(fused_text)
                    metadatas.append({
                        "source": os.path.basename(file_path),
                        "path": file_path,
                        "domain": str(domain),
                        "object_type": str(object_type),
                        "is_instance_of": is_instance_str, # 단일 상속 좌표 보존
                        "tier": tier,
                        "T_static": t_static,
                        "doc_date": doc_date,
                        "decay_rate": decay_rate
                    })
                    ids.append(file_path)
            except Exception as e: 
                log(f"[ERROR] Node Parsing Failure {file_path}: {e}")
 
        if documents:
            try:
                col = get_collection()
                col.upsert(documents=documents, metadatas=metadatas, ids=ids)
                for file_id in ids: checkpoint[file_id] = os.path.getmtime(file_id)
                with open(CHECKPOINT_PATH, 'w', encoding='utf-8') as f: json.dump(checkpoint, f)
                log(f"  [V7.7_PROGRESS] {i + len(batch_files)} / {len(to_sync)} nodes integrated...")
            except Exception as e: 
                log(f"[ERROR] Batch Integration Failed: {str(e)[:200]}")
            finally:
                gc.collect()
                if torch.cuda.is_available(): torch.cuda.empty_cache()
 
    log(f"🏆 [SUCCESS] V7.7 Enterprise Intelligence Fabric Sealed.")

def ask_v7(query):
    log(f"\n🔍 [V7.7_QUERY] Searching Antigravity Fabric: '{query}'")
    col = get_collection()
    reranker = get_reranker()
    
    try:
        # Tier 0 및 일반 데이터 하이브리드 쿼리
        tier0_results = col.query(query_texts=[query], n_results=5, where={"tier": 0})
        std_results = col.query(query_texts=[query], n_results=20)
    except Exception as e:
        log(f"[ERROR] Retrieval Failure: {e}"); return

    all_docs = (tier0_results.get('documents', [[]])[0] or []) + (std_results.get('documents', [[]])[0] or [])
    all_metas = (tier0_results.get('metadatas', [[]])[0] or []) + (std_results.get('metadatas', [[]])[0] or [])
    
    if not all_docs:
        log("[WARN] No relevant nodes found."); return

    # 중복 노드 제거 로직
    seen_paths = set(); unique_results = []
    for doc, meta in zip(all_docs, all_metas):
        if meta['path'] not in seen_paths:
            seen_paths.add(meta['path'])
            unique_results.append((doc, meta))

    # 리랭킹 및 상속 가중치 계산
    pairs = [[query, re.sub(r'^---.*?---\s*', '', res[0], flags=re.DOTALL)[:3000]] for res in unique_results]
    raw_scores = reranker.compute_score(pairs)
    
    scored_results = []
    for (doc, meta), r_score in zip(unique_results, raw_scores):
        prob_score = 1 / (1 + math.exp(-r_score))
        t_dyn = calculate_dynamic_trust(meta['T_static'], meta['doc_date'], meta['decay_rate'])
        
        # [V7.7 Enterprise] SHA-256 감사 무결성 실시간 측정 검증
        integrity_status = "PASS"
        stored_hash = None
        current_hash = None
        try:
            with open(meta['path'], 'r', encoding='utf-8', errors='ignore') as f:
                post = frontmatter.load(f)
            # 바디 텍스트의 SHA-256 계산
            body_content = post.content.strip()
            current_hash = hashlib.sha256(body_content.encode('utf-8')).hexdigest()
            
            spo_graph = post.metadata.get('spo_graph', [])
            if isinstance(spo_graph, list):
                for triple in spo_graph:
                    if isinstance(triple, dict) and 'evidence_hash' in triple:
                        stored_hash = triple['evidence_hash']
                        break
            
            if stored_hash and current_hash != stored_hash:
                integrity_status = "FAIL"
        except Exception:
            pass

        final_score = prob_score * t_dyn
        if meta['tier'] == 0: 
            final_score += 0.1
            
        # 위변조 감지 시 신뢰 가중치 패널티 부과 (10%로 신뢰도 삭감)
        if integrity_status == "FAIL":
            final_score = final_score * 0.1
        
        scored_results.append((doc, meta, final_score, integrity_status))
    
    scored_results.sort(key=lambda x: x[2], reverse=True)
    
    # 상속 추적(Reasoning Bridge) 활성화: 최고 점수 노드가 Data 노드인 경우 부모 Concept 동시 표기
    log("\n" + "═"*80)
    log("   ANTIGRAVITY V7.7 ENTERPRISE INTEGRITY SCOREBOARD")
    log("═"*80)
    for i, (doc, meta, score, integrity) in enumerate(scored_results[:10], 1):
        type_icon = "🏛️ [Concept]" if meta['object_type'] == "Concept" else "📊 [Data]"
        parent_info = f" -> Parent: {meta['is_instance_of']}" if meta['is_instance_of'] else ""
        integrity_flag = " [🚨 위변조 감지]" if integrity == "FAIL" else ""
        log(f" [{i:2d}] {score:.4f} | {type_icon} {meta['source']}{parent_info}{integrity_flag}")
    log("═"*80)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rag_cli_v2.py --sync | \"질문\"")
    elif sys.argv[1] == "--sync":
        sync_vault()
    else:
        ask_v7(" ".join(sys.argv[1:]))
