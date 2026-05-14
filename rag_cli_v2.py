import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import time
import chromadb
from chromadb.utils import embedding_functions
from FlagEmbedding import FlagReranker
import torch
import gc
import re
import sys
import math
from datetime import datetime

# [RAG-LOCK] Windows 터미널 출력 인코딩 강제 설정 (UTF-8)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# ================= CONFIG =================
SEARCH_PATHS = [r"C:\Anitigravity\02_Knowledge", r"C:\Anitigravity\03_External_Data"]
DB_PATH = r"C:\Anitigravity\rag_db"
EXCLUDE_DIRS = ['.obsidian', '.smart-env', 'rag_db', 'node_modules', '04_Tools', 'Archive', 'lectures', '_Archive_Source', '_backups', '_Archive_LowDensity']
# ==========================================

_client = None
_collection = None
_bge_ef = None
_reranker = None

def load_ontology_map():
    import json
    map_path = os.path.join(r"C:\Anitigravity\02_Knowledge", "_Ontology_Map.json")
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

    log(f"Starting V6.3.7 Incremental Sync across: {SEARCH_PATHS}")
    dynamic_taxonomy = load_ontology_map() 
    priority_dirs = ['03_AI_Data', 'entities', 'concepts', 'Chemistry_Datasets'] # [V6.3.7 우선순위]
    
    all_md_files = []
    for base_path in SEARCH_PATHS:
        for dp, dn, filenames in os.walk(base_path):
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
                    raw_content = f.read()
                    # [V6.4 Auto-Healing YAML] Fix invalid YAML list syntax on same line (Preserve Indentation)
                    raw_content = re.sub(r'^(\s*)(tags|is_part_of|related_to):\s*-\s*([^\r\n]+)', r"\1\2: [\3]", raw_content, flags=re.MULTILINE)
                    raw_content = raw_content.replace('[]]', '[]')
                    
                    post = frontmatter.loads(raw_content)
                    metadata = post.metadata
                    body_text = post.content
                    
                    # [V6.4 7-Layer YAML Parsing (Palantir AIP)]
                    basic = metadata.get('Basic', {})
                    semantic = metadata.get('Semantic', {})
                    dynamic = metadata.get('Dynamic', {})
                    trust_metrics = metadata.get('Trust Metrics', {})
                    lineage = metadata.get('Lineage', {})
                    exec_action = metadata.get('Executable_Action', {})

                    domain = basic.get('domain', 'Unknown')
                    topology_policy = dynamic.get('topology_policy', 'Interconnected_Cluster')
                    
                    t_static = float(trust_metrics.get('T_static', 0.0))
                    t_dynamic = float(trust_metrics.get('T_dynamic', 0.8))

                    # AIP Actionable 파싱
                    has_action = exec_action.get('has_action', False)
                    action_type = exec_action.get('action_type', 'None')
                    target_script = exec_action.get('target_script', 'None')
                    params_str = str(exec_action.get('params', '{}'))
                    logic_prov = lineage.get('logic_provenance', 'Unknown')

                    # [V7.5 Trust & Decay]
                    doc_date_str = basic.get('date', datetime.now().strftime("%Y-%m-%d"))
                    decay_rate = float(dynamic.get('decay_rate', 0.1))

                    # 지능형 개념 확장
                    body_lower = body_text.lower()
                    expanded_terms = set()
                    for specific_term, parent_terms in dynamic_taxonomy.items(): 
                        if specific_term in body_lower: expanded_terms.update(parent_terms)
                    
                    # [V6.7.5] 가상 질문(Expected Queries) 레이어 추출
                    expected_queries = semantic.get('expected_queries', [])
                    queries_text = "\n".join(expected_queries) if expected_queries else ""
                    
                    # [V6.4 AIP 메타 앵커]
                    meta_anchors = [
                        f"[Domain: {domain}]",
                        f"[Topology: {topology_policy}]",
                        f"[Logic_Provenance: {logic_prov}]",
                        f"[Has_Action: {has_action}]",
                        f"[Target_Script: {target_script}]",
                        f"[Expanded: {', '.join(expanded_terms) if expanded_terms else 'None'}]"
                    ]
                    # 메타데이터 + 가상 질문 + 본문을 통합 임베딩
                    fused_text = "\n".join(meta_anchors) + f"\n[Expected Queries]\n{queries_text}\n---\n{body_text}"
                    
                    documents.append(fused_text)
                    metadatas.append({
                        "source": os.path.basename(file_path),
                        "path": file_path,
                        "mtime": os.path.getmtime(file_path),
                        "domain": str(domain),
                        "topology_policy": str(topology_policy),
                        "T_static": t_static,
                        "T_dynamic": t_dynamic,
                        "has_action": bool(has_action),
                        "action_type": str(action_type),
                        "target_script": str(target_script),
                        "params": params_str,
                        "doc_date": doc_date_str,
                        "decay_rate": decay_rate
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
                log(f"  [PROGRESS] {i + len(batch_files)} / {len(to_sync)} files processed...")
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

def calculate_dynamic_trust(t_static, doc_date_str, decay_rate):
    from datetime import datetime
    try:
        doc_date = datetime.strptime(doc_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        months_passed = (current_date.year - doc_date.year) * 12 + current_date.month - doc_date.month
        t_dynamic = t_static - (months_passed * decay_rate)
        return max(t_dynamic, 0.1)
    except:
        return t_static

def ask_v2(query):
    print(f"\n[QUERY] Searching V6.3.7 Wiki for: '{query}'")
    collection = get_collection()
    reranker = get_reranker()
    
    # [V6.4 AIP Dual-Pipeline Retrieval]
    # Pipeline 1: Actionable Deterministic Scan (has_action: True 필터링)
    try:
        action_results = collection.query(
            query_texts=[query],
            n_results=10,
            where={"has_action": True}
        )
    except: 
        action_results = {'documents': [[]], 'metadatas': [[]], 'ids': [[]]}

    # Pipeline 2: Standard Semantic Scan
    try:
        results = collection.query(
            query_texts=[query], 
            n_results=30
        )
    except Exception as e:
        print(f"[WARNING] 쿼리 실패: {e}")
        return {
            "top_knowledge": None,
            "proposed_action": None,
            "score_board": []
        }

    # Merge results
    vector_docs = (action_results.get('documents', [[]])[0] or []) + (results.get('documents', [[]])[0] or [])
    vector_metas = (action_results.get('metadatas', [[]])[0] or []) + (results.get('metadatas', [[]])[0] or [])

    print(f"[GRAPH] Analyzing Topology (following [[links]])...")
    hub_node_names = extract_graph_neighbors(vector_docs)
    hub_contexts = []; hub_sources = []
    
    for hub_name in hub_node_names:
        hub_found = False
        for base_path in SEARCH_PATHS:
            for root, _, filenames in os.walk(base_path):
                for f in filenames:
                    if f.lower() == (hub_name.lower() + ".md"):
                        hub_path = os.path.join(root, f)
                        try:
                            with open(hub_path, 'r', encoding='utf-8', errors='ignore') as hf:
                                content = hf.read()
                                hub_contexts.append(content)
                                trust_match = re.search(r'T_static:\s*([\d\.]+)', content)
                                trust_val = float(trust_match.group(1)) if trust_match else 0.0
                                hub_sources.append({"source": f, "path": hub_path, "type": "HUB_NODE", "T_static": trust_val})
                                hub_found = True
                                break
                        except: pass
                if hub_found: break
            if hub_found: break
    
    all_docs = vector_docs + hub_contexts
    all_metas = vector_metas + hub_sources
    
    print(f"[RERANK] Semantic Similarity Ranking (Trust-Zero Mode)...")
    final_scores = [0] * len(all_docs)
    if reranker:
        try:
            import re
            pairs = []
            for doc in all_docs:
                # 🚀 [V6.4.8 Precision Patch] OS 환경(\r\n vs \n) 관계없이 YAML 블록 제거
                # --- [yaml] --- [body] 구조에서 두 번째 --- 이후의 텍스트만 추출
                clean_body = re.sub(r'^---.*?---\s*', '', doc, flags=re.DOTALL)
                
                # 본문 3000자 확보 (메타데이터 노이즈 완전 제거)
                pairs.append([query, clean_body[:3000].strip()])
                
            raw_scores = reranker.compute_score(pairs)
            final_scores = [1 / (1 + math.exp(-s)) for s in raw_scores]
        except Exception as e:
            print(f"[WARNING] 리랭킹 실패: {e}")

    # [V6.5.13 Precision Targeting] 질문의 의도 분석 (실무/팁 요구 여부)
    practical_keywords = ["팁", "방법", "가이드", "조치", "메뉴얼", "매뉴얼", "how to", "step", "관리", "분석", "팁"]
    is_practical_query = any(k in query.lower() for k in practical_keywords)

    combined_results = list(zip(all_docs, all_metas, final_scores))
    adjusted_results = []
    
    for doc, meta, score in combined_results:
        source_name = meta.get('source', '').lower()
        h_action = meta.get('has_action')
        is_actionable = False
        if isinstance(h_action, bool): is_actionable = h_action
        elif isinstance(h_action, str): is_actionable = h_action.lower() == 'true'
        
        # 기본 가중치: 액션 가능 노드 가산점
        final_score = score + 0.05 if is_actionable else score
        
        # 🚀 [V6.5.13] 실무 지식 타격 가중치
        if is_practical_query:
            if "[moc]" in source_name or "hub" in source_name:
                final_score -= 0.15
            elif "[entity]" in source_name or "[sop]" in source_name or "[data]" in source_name:
                final_score += 0.1
        
        # 🚀 [V6.5.19] 기술 핵심어 하드 매칭 (배터리 화학 도메인 확장)
        technical_map = {
            "ultrasonic": ["초음파", "혼", "horn", "진폭", "amplitude", "접합", "ultrasonic"],
            "laser": ["레이저", "laser", "keyhole", "용입", "penetration", "광학"],
            "robot": ["로봇", "robot", "팔", "arm", "토크", "force", "튜닝"],
            "resistance": ["저항", "spot", "점용접", "electrode", "전극"],
            "sodium": ["나트륨", "sodium", "sib", "하드 카본", "hard carbon", "hard-carbon"],
            "lithium": ["리튬", "lithium", "lib", "흑연", "graphite", "lfp", "ncm"]
        }
        
        for domain, keywords in technical_map.items():
            query_hit = any(k in query.lower() for k in keywords)
            doc_hit = any(k in (source_name + doc.lower()) for k in keywords)
            
            if query_hit:
                # 1. 도메인 일치 시 폭발적 보너스
                if domain in source_name or any(k in source_name for k in keywords):
                    final_score += 0.5
                
                # 2. 이종 배터리 도메인 간섭 차단
                if domain == "sodium" and ("lithium" in source_name or "graphite" in source_name or "graphene" in source_name):
                    final_score -= 1.0 # 나트륨 물었는데 리튬/그래핀 나오면 즉시 배제
                elif domain == "lithium" and ("sodium" in source_name or "hard carbon" in source_name):
                    final_score -= 1.0

                # 3. 초음파/레이저 등 공법 도메인 차단 (기존 유지)
                if domain == "ultrasonic" and ("resistance" in source_name or "laser" in source_name):
                    final_score -= 1.0

        # 🚀 [V7.5] Dynamic Trust Decay 적용
        t_stat = float(meta.get('T_static', 0.5))
        doc_date = meta.get('doc_date', datetime.now().strftime("%Y-%m-%d"))
        decay_r = float(meta.get('decay_rate', 0.1))
        t_dyn = calculate_dynamic_trust(t_stat, doc_date, decay_r)
        
        final_score = final_score * t_dyn
        
        adjusted_results.append((doc, meta, final_score))
    
    # 보정된 최종 점수로 정렬
    adjusted_results.sort(key=lambda x: x[2], reverse=True)
    
    # 🚀 [V6.5.15] MOC 1위 강제 배제 (실무 질문 시)
    if is_practical_query and len(adjusted_results) > 1:
        first_source = adjusted_results[0][1].get('source', '').lower()
        if "[moc]" in first_source or "hub" in first_source:
            for i in range(1, min(len(adjusted_results), 10)):
                target_source = adjusted_results[i][1].get('source', '').lower()
                if "[entity]" in target_source or "[sop]" in target_source:
                    adjusted_results[0], adjusted_results[i] = adjusted_results[i], adjusted_results[0]
                    break

    final_results_pool = adjusted_results[:15]
    
    # [V6.5.18] Deterministic Scoreboard
    print("\n" + "="*70)
    print("V6.5.18 Palantir AIP FINAL SCOREBOARD (Trust-Zero Mode):")
    for i, (doc, meta, score) in enumerate(final_results_pool, 1):
        icon = "🏛️" if "[moc]" in meta['source'].lower() else "📖"
        print(f"{i:2d}. {icon} {meta['source']:70s} | Score: {score:.4f}")
    print("="*70)
    
    final_docs = [x[0] for x in final_results_pool]
    final_metas = [x[1] for x in final_results_pool]

    # 결과를 저장할 데이터 객체 초기화 (V6.5.16 입체적 보고 구조)
    aip_report = {
        "top_hub": None,
        "top_entity": None,
        "proposed_action": None,
        "score_board": []
    }

    # ... (가중치 계산 및 정렬 로직 동일) ...
    # 🚀 [V6.5.16] 입체적 지식 포획 (Hub와 Entity를 각각 베스트로 추출)
    hub_candidates = [x for x in adjusted_results if "[moc]" in x[1].get('source', '').lower() or "hub" in x[1].get('source', '').lower()]
    entity_candidates = [x for x in adjusted_results if "[entity]" in x[1].get('source', '').lower() or "[sop]" in x[1].get('source', '').lower() or "[data]" in x[1].get('source', '').lower()]

    if hub_candidates:
        h_doc, h_meta, h_score = hub_candidates[0]
        h_body = re.sub(r'^---.*?---\s*', '', h_doc, flags=re.DOTALL).strip()
        aip_report["top_hub"] = {"source": h_meta['source'], "body": h_body}

    if entity_candidates:
        e_doc, e_meta, e_score = entity_candidates[0]
        e_body = re.sub(r'^---.*?---\s*', '', e_doc, flags=re.DOTALL).strip()
        aip_report["top_entity"] = {"source": e_meta['source'], "body": e_body}

    final_results_pool = adjusted_results[:15]

    # 🚀 [V6.4.1 Palantir AIP Handoff Logic - Hardened Security Mode]
    action_candidates = [m for m in final_metas if m.get('has_action') is True]
    
    if action_candidates:
        top_action = action_candidates[0] # 가장 점수가 높은 액션 추출
        
        # 🚀 [V6.4.2 AIP CONTEXT BRIEFING] 결재를 요구하기 전, 수석님께 맥락(이유)을 먼저 보고합니다.
        try:
            action_idx = final_metas.index(top_action)
            # 문서 본문에서 메타데이터 앵커들을 제외한 순수 텍스트 추출 시도
            raw_text = re.sub(r'^---.*?---\s*', '', final_docs[action_idx], flags=re.DOTALL)
            # 줄바꿈 제거 및 300자 요약
            snippet = raw_text[:300].replace('\n', ' ') + "..."
        except:
            snippet = "본문 컨텍스트 추출 불가"

        logic_provenance = top_action.get('logic_provenance', '미기재 (Lineage 불분명)')
        source_file = top_action.get('source', 'Unknown')
        
        aip_report["proposed_action"] = {
            "source": source_file,
            "logic": logic_provenance,
            "snippet": snippet,
            "script": top_action.get('target_script'),
            "type": top_action.get('action_type'),
            "params": top_action.get('params', '{}')
        }
        
        print("\n" + "💡 "*30)
        print("[AIP CONTEXT BRIEFING - 왜 이 액션이 제안되었는가?]")
        print(f"👉 출처 지식: {source_file}")
        print(f"👉 논리적 근거(Lineage): {logic_provenance}")
        print(f"👉 본문 핵심 요약: {snippet}")
        print("💡 "*30)

        # [Inferential Evidence] DB에 저장된 문자열 파라미터를 dict로 복원 시도
        import json
        import re
        import sys
        
        action_type = top_action.get('action_type', 'Unknown')
        script = top_action.get('target_script')
        
        # [V6.4.1] metadata에 저장된 params는 이미 str 형태이므로 파싱 시도
        raw_params = top_action.get('params', '{}')
        try:
            # 싱글 쿼테이션을 더블 쿼테이션으로 변환하여 json 로딩 (dict str 대응)
            params = json.loads(raw_params.replace("'", '"'))
        except:
            params = {}
        
        print("\n" + "⚠️ "*30)
        print("[AIP HANDOFF PROTOCOL ACTIVATED]")
        print(f"> 타겟 스크립트: {script} (Action: {action_type})")
        print(f"> 원본 파라미터: {params}")
        
        # 🛡️ [SECURITY FIREWALL] 파라미터 무결성 스키마 검증 (Sanitization)
        is_safe = True
        violation_reason = ""
        
        if action_type == "write_plc_register":
            # 1. IP 주소 정규식 검증 (사설망 대역 확인)
            if not re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", str(params.get("target_ip", ""))):
                is_safe, violation_reason = False, "유효하지 않은 PLC IP 주소 형식입니다."
            # 2. 레지스터 주소 검증 (알파벳 1자 + 숫자 조합 강제)
            elif not re.match(r"^[A-Z][0-9]+$", str(params.get("register", ""))):
                is_safe, violation_reason = False, "레지스터 주소 형식이 올바르지 않습니다 (예: D1000)."
            # 3. 입력 값 타입 검증 (순수 숫자형 문자열)
            elif not str(params.get("value", "")).isdigit():
                is_safe, violation_reason = False, "입력값(Value)은 순수 숫자여야 합니다."
                
        elif action_type == "execute_trading_logic" or action_type == "run_dummy_script":
            if action_type == "execute_trading_logic":
                if not re.match(r"^[A-Z0-9]+$", str(params.get("ticker", ""))):
                    is_safe, violation_reason = False, "티커 심볼은 영문 대문자 및 숫자만 허용됩니다."
                elif str(params.get("signal")).upper() not in ["BUY", "SELL", "HOLD"]:
                    is_safe, violation_reason = False, "허용되지 않은 매매 시그널입니다 (BUY/SELL/HOLD만 허용)."
                elif float(params.get("risk_ratio", 0.01)) > 0.05:
                    is_safe, violation_reason = False, "리스크 비율(risk_ratio)이 시스템 안전 한도(5%)를 초과했습니다."
            else: # run_dummy_script
                print("[INFO] 테스트용 액션 타입입니다. 기본 검증 통과.")
        else:
            # 등록되지 않은 액션 타입은 기본적으로 차단 (Default-Deny)
            is_safe, violation_reason = False, f"등록되지 않은 액션 타입입니다: {action_type}"

        # 방화벽 통과 실패 시 강제 종료 (Hard-Abort)
        if not is_safe:
            print("\n[🛑 SECURITY ALERT] 파라미터 무결성 검증 실패 (Sanitization Failed)")
            print(f"> 사유: {violation_reason}")
            print("[ABORT] 시스템 보호를 위해 해당 액션의 Handoff를 영구 차단합니다.")
            print("⚠️ "*30)
            return aip_report
            
        print("\n[✅ SECURITY CLEAR] 파라미터 무결성 스키마 검증 통과")
        print("⚠️ "*30)
        
        # 🚀 [V6.5.8 Headless Patch] API로 호출 시 Y/N 무시하고 데이터(aip_report) 리턴
        if not sys.stdin.isatty() or __name__ != "__main__":
            return aip_report
            
        # 방화벽을 통과한 안전한 파라미터에 대해서만 결재(Y/N) 요청
        user_input = input("\n위 액션을 승인하고 시스템에 전송하시겠습니까? (Y/N): ")
        
        if user_input.strip().upper() == 'Y':
            print("\n[🟢 AIP_EXECUTION] 실행 중: " + str(script))
            import subprocess
            try:
                # [V6.4.1 Hardened] 파라미터를 CLI 아규먼트 형태로 직렬화하여 실행
                args_list = []
                for k, v in params.items():
                    args_list.extend([f"--{k}", str(v)])
                
                cmd = [sys.executable, script] + args_list
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                for line in process.stdout:
                    print(line, end="")
                process.wait()
                print(f"\n[SUCCESS] 액션 완료 (Exit Code: {process.returncode})")
            except Exception as ex:
                print(f"\n[ERROR] 실행 중 치명적 오류: {ex}")
        else:
            print("\n[🛑 ABORT] 수석님에 의해 액션 실행이 거부(Reject)되었습니다.")
    else:
        print("\n[INFO] 검색된 노드 중 즉시 실행 가능한 액션(Actionable)이 없습니다.")
        
    return aip_report

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
