import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import time
import chromadb
from chromadb.utils import embedding_functions
from FlagEmbedding import FlagReranker
import google.generativeai as genai
import torch
import gc
import re
import sys
import math

# [RAG-LOCK] Windows 터미널 출력 인코딩 강제 설정 (UTF-8)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# ================= CONFIG =================
API_KEY = "AIzaSyAPERk3YyuDXVNJUaqmlHlQ0uDkbUvmeqU"
VAULT_PATH = r"C:\Anitigravity\02_Knowledge"
DB_PATH = r"C:\Anitigravity\rag_db"
EXCLUDE_DIRS = ['.obsidian', '.smart-env', 'rag_db', 'node_modules', '04_Tools', 'Archive', 'lectures', '_Archive_Source', '_backups', '_Archive_LowDensity']
# ==========================================

_client = None
_collection = None
_bge_ef = None
_reranker = None

def load_ontology_map():
    import json
    map_path = os.path.join(VAULT_PATH, "_Ontology_Map.json")
    flat_map = {}
    if os.path.exists(map_path):
        try:
            with open(map_path, 'r', encoding='utf-8') as f:
                raw_map = json.load(f)
                for category, terms in raw_map.items():
                    flat_map.update(terms)
        except Exception: pass
    return flat_map

def get_collection():
    global _client, _collection, _bge_ef
    if _collection is None:
        genai.configure(api_key=API_KEY)
        _bge_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="BAAI/bge-m3", device="cuda")
        _client = chromadb.PersistentClient(path=DB_PATH)
        _collection = _client.get_or_create_collection(name="obsidian_rag_v6", embedding_function=_bge_ef) # [V6.1 컬렉션 독립]
    return _collection

def get_reranker():
    global _reranker
    if _reranker is None:
        _reranker = FlagReranker('BAAI/bge-reranker-v2-m3', use_fp16=True)
    return _reranker

def log(msg):
    with open("rag_sync.log", "a", encoding="utf-8") as f:
        f.write(f"[{time.ctime()}] {msg}\n")
    print(msg, flush=True)

def sync_vault():
    import json
    import frontmatter
    CHECKPOINT_PATH = os.path.join(DB_PATH, "sync_checkpoint.json")
    checkpoint = {}
    if os.path.exists(CHECKPOINT_PATH):
        try:
            with open(CHECKPOINT_PATH, 'r', encoding='utf-8') as f:
                checkpoint = json.load(f)
        except: checkpoint = {}

    log(f"Starting V6.3.7 Incremental Vault Sync: {VAULT_PATH}")
    dynamic_taxonomy = load_ontology_map() 
    priority_dirs = ['03_AI_Data', 'entities', 'concepts'] # [V6.3.7 우선순위]
    
    all_md_files = []
    for dp, dn, filenames in os.walk(VAULT_PATH):
        path_parts = set(re.split(r'[\\/]', dp))
        if any(exclude in path_parts for exclude in EXCLUDE_DIRS): continue
        for f in filenames:
            if f.endswith('.md'):
                all_md_files.append(os.path.join(dp, f))

    to_sync = [f for f in all_md_files if f not in checkpoint or checkpoint[f] < os.path.getmtime(f)]
    
    if not to_sync:
        log("[DONE] All files are up to date. (V6.3.7 HDS-Gold)")
        return

    log(f"[PLAN] {len(to_sync)} files need V6.3.7 reinforcement.")
    to_sync.sort(key=lambda x: any(p in x for p in priority_dirs), reverse=True)
    
    total_processed = 0
    BATCH_SIZE = 4 # RTX 4060 8GB VRAM Safety
    for i in range(0, len(to_sync), BATCH_SIZE):
        batch_files = to_sync[i:i + BATCH_SIZE]
        documents = []; metadatas = []; ids = []
        
        for file_path in batch_files:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    post = frontmatter.load(f)
                    metadata = post.metadata
                    body_text = post.content
                    
                    # [V6.3.7 5-Layer YAML Parsing & Strict Quarantine]
                    basic = metadata.get('Basic', {})
                    semantic = metadata.get('Semantic', {})
                    dynamic = metadata.get('Dynamic', {})
                    trust_metrics = metadata.get('Trust Metrics', {})

                    domain = basic.get('domain', 'Unknown')
                    topology_policy = dynamic.get('topology_policy', 'Interconnected_Cluster')
                    
                    # T_static이 없으면 무조건 0.0(미검증)으로 처리하여 환각 원천 차단
                    t_static = float(trust_metrics.get('T_static', 0.0))
                    t_dynamic = float(trust_metrics.get('T_dynamic', 0.8))

                    # 지능형 개념 확장
                    body_lower = body_text.lower()
                    expanded_terms = set()
                    for specific_term, parent_terms in dynamic_taxonomy.items(): 
                        if specific_term in body_lower: expanded_terms.update(parent_terms)
                    
                    # [V6.3.7 메타 앵커]
                    meta_anchors = [
                        f"[Domain: {domain}]",
                        f"[Topology: {topology_policy}]",
                        f"[Trust_Static: {t_static}]",
                        f"[Expanded: {', '.join(expanded_terms) if expanded_terms else 'None'}]"
                    ]
                    fused_text = "\n".join(meta_anchors) + f"\n---\n{body_text}"
                    
                    documents.append(fused_text)
                    metadatas.append({
                        "source": os.path.basename(file_path),
                        "path": file_path,
                        "mtime": os.path.getmtime(file_path),
                        "domain": str(domain),
                        "topology_policy": str(topology_policy), # DB 필터링용 속성 추가
                        "T_static": t_static,                    # 인간 검증 지표 추가
                        "T_dynamic": t_dynamic
                    })
                    ids.append(file_path)
            except Exception as e: log(f"[ERROR] Processing {file_path}: {e}")

        if documents:
            try:
                collection = get_collection()
                collection.upsert(documents=documents, metadatas=metadatas, ids=ids)
                for file_id in ids: checkpoint[file_id] = os.path.getmtime(file_id)
                with open(CHECKPOINT_PATH, 'w', encoding='utf-8') as f: json.dump(checkpoint, f)
                total_processed += len(documents)
            except Exception as e: log(f"[ERROR] Batch Sync Failed: {str(e)[:200]}")
            finally:
                gc.collect()
                if torch.cuda.is_available(): torch.cuda.empty_cache()

    log(f"[STATUS] V6.3.7 Sync session finished. {total_processed} files reinforced.")

def extract_graph_neighbors(docs, top_k=3):
    link_counts = {}
    for doc in docs:
        links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', doc)
        for link in links:
            link = link.strip()
            link_counts[link] = link_counts.get(link, 0) + 1
    return [link for link, count in sorted(link_counts.items(), key=lambda x: x[1], reverse=True)[:top_k]]

def ask_v2(query):
    print(f"\n[QUERY] Searching V6.3.7 Wiki for: '{query}'")
    collection = get_collection()
    reranker = get_reranker()
    
    # [V6.3.7 Hard Constraint Firewall - 임시 해제]
    try:
        results = collection.query(
            query_texts=[query], 
            n_results=20
            # where={"T_static": 1.0} # [임시 해제] 투명인간 취급 금지
        )
    except Exception as e:
        print(f"[WARNING] 쿼리 실패 또는 T_static: 1.0 문서가 부족할 수 있습니다: {e}")
        return

    if not results['documents'] or not results['documents'][0]:
        print("[!] 검증된 지식(T_static: 1.0)이 존재하지 않거나, 보안 격리(Quarantine) 상태입니다.")
        return

    vector_docs = results['documents'][0]
    vector_metas = results['metadatas'][0]

    print(f"[GRAPH] Analyzing Topology (following [[links]])...")
    hub_node_names = extract_graph_neighbors(vector_docs)
    hub_contexts = []; hub_sources = []
    
    for hub_name in hub_node_names:
        hub_found = False
        for root, _, filenames in os.walk(VAULT_PATH):
            for f in filenames:
                if f.lower() == (hub_name.lower() + ".md"):
                    hub_path = os.path.join(root, f)
                    try:
                        with open(hub_path, 'r', encoding='utf-8', errors='ignore') as hf:
                            content = hf.read()
                            hub_contexts.append(content)
                            # [V6.3.7 T_static 파싱]
                            trust_match = re.search(r'T_static:\s*([\d\.]+)', content)
                            trust_val = float(trust_match.group(1)) if trust_match else 0.0
                            hub_sources.append({"source": f, "path": hub_path, "type": "HUB_NODE", "T_static": trust_val})
                            hub_found = True
                            break
                    except: pass
            if hub_found: break
    
    all_docs = vector_docs + hub_contexts
    all_metas = vector_metas + hub_sources
    
    print(f"[RERANK] Semantic Similarity Ranking (Trust-Zero Mode)...")
    if reranker:
        try:
            pairs = [[query, doc[:2000]] for doc in all_docs]
            raw_scores = reranker.compute_score(pairs)
            
            final_scores = []
            for score, meta in zip(raw_scores, all_metas):
                # [Trust-Zero] 신뢰도 가중치 없이 순수 유사도 점수만 사용
                final_score = 1 / (1 + math.exp(-score))
                final_scores.append(final_score)
                
            ranked_results = sorted(zip(all_docs, all_metas, final_scores), key=lambda x: x[2], reverse=True)[:7]
        except Exception as e:
            ranked_results = sorted(zip(all_docs, all_metas, [0]*len(all_docs)), key=lambda x: x[2], reverse=True)[:7]
    else:
        ranked_results = list(zip(all_docs, all_metas, [0]*len(all_docs)))[:7]

    final_docs = [x[0] for x in ranked_results]
    final_metas = [x[1] for x in ranked_results]

    final_model = genai.GenerativeModel('gemini-2.0-flash') # [V6.3.7 모델 동기화]
    context_text = ""
    for doc, meta in zip(final_docs, final_metas):
        context_text += f"Source: {meta['source']}\n{doc[:2500]}\n---\n"

    final_prompt = f"""당신은 수석 아키텍트의 V6.3.7 시스템과 동기화된 [Vector RAG 에이전트]입니다.
아래 제공된 [검색된 지식 문서]를 융합(Late Fusion)하여 질문에 답하십시오.

[검색된 지식 문서]
{context_text}

[🚨 V6.3.7 RAG 엔진 시스템 룰]
1. 제로 환각(Zero Hallucination): 외부 정보 금지. 반드시 위 컨텍스트 내의 `[핵심 기술 사양]`과 `[Advanced RAG 기술 분석]`을 최우선으로 인용할 것.
2. 실행 가능성: 제안하는 내용은 RTX 4060 8GB 환경에서 구동 가능해야 함.
3. 결과물 하단에 반드시 `### 🔗 참조된 로컬 지식망` 섹션을 만들고, 사용된 문서 출처를 `> * [[파일명]]` 형태로 기재할 것.

[Question]
{query}

최종 답변:"""

    try:
        response = final_model.generate_content(final_prompt)
        print("\n" + "="*60)
        print(f"V6.3.7 SYNTHESIS RESPONSE:\n\n{response.text}")
        print("="*60)
    except Exception as e:
        print(f"\n[ERROR] Synthesis failed: {e}")

if __name__ == "__main__":
    import traceback
    try:
        if len(sys.argv) < 2:
            print("Usage: python rag_cli_v2.py --sync | --retrieve-only \"질문\" | \"질문\"")
        elif sys.argv[1] == "--sync": sync_vault()
        elif sys.argv[1] == "--retrieve-only":
            query = " ".join(sys.argv[2:])
            # ask_v2 로직을 복사하되 최종 합성만 제외
            col = get_collection()
            # [V6.3.7 Firewall - 임시 해제]
            results = col.query(
                query_texts=[query], 
                n_results=15
                # where={"T_static": 1.0}
            )
            all_docs = results['documents'][0]
            all_metas = results['metadatas'][0]
            
            reranker = get_reranker()
            pairs = [[query, doc[:2000]] for doc in all_docs]
            raw_scores = reranker.compute_score(pairs)
            
            final_scores = []
            for score, meta in zip(raw_scores, all_metas):
                # [Trust-Zero] 신뢰도 가중치 없이 순수 유사도 점수만 사용
                final_score = 1 / (1 + math.exp(-score))
                final_scores.append(final_score)
                
            ranked_results = sorted(zip(all_docs, all_metas, final_scores), key=lambda x: x[2], reverse=True)[:7]
            
            print(f"\n[RAIDAR MODE] 관련 지식 노드 Top {len(ranked_results)}:")
            for i, (doc, meta, score) in enumerate(ranked_results, 1):
                print(f"{i}. {meta['source']} (Score: {score:.4f})")
        else: ask_v2(" ".join(sys.argv[1:]))
    except Exception:
        traceback.print_exc()
        sys.exit(1)
