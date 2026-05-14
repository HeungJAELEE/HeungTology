---
Basic:
  id: "SOP-EXTERNAL-DATA-ETL-PIPELINE-v6"
  date: 2026-05-14
  domain: 00_System_Governance
  project: "System_Normalization"
Dynamic:
  status: "Ratified (V6.8.0 Active)"
Object:
  uuid: "SOP-EXTERNAL-DATA-ETL-PIPELINE-v6"
  type: "SOP"
Semantic:
  tags: '["#SOP", "#ETL_Pipeline", "#Data_Ingestion", "#Vector_Sync", "#AIP_Architecture"]'
  expected_queries:
    - "외부 데이터셋을 시스템에 안전하게 이식하는 방법은?"
    - "V6.8.0 ETL 파이프라인의 4단계 공정 설명"
    - "벡터 공간 오염 방지를 위한 데이터 격리 정책"
  is_part_of: '["[[[MOC] 00_master-plan-and-system-governance-hub]]]"]'
Trust Metrics:
  T_init: 1.0
  T_static: 1.0
  note: "수석 아키텍트 승인 하에 확정된 외부 데이터 인제스트 공식 프로토콜."
Executable_Action:
  has_action: false
  action_type: "None"
  target_script: "None"
aliases: '["외부 데이터 이식 가이드", "AIP ETL 파이프라인", "데이터 격리 및 동기화 SOP"]'
citation_count: 1
current_trust_level: 1.0
provenance: '["Ratified by Chief Architect on 2026-05-14"]'
related_to: '["[[SOP] v6-3-7-decoupled-rag-and-wiki-entropy-management]"]'
trust_base: 1.0
trust_lambda: 0.0
type: SOP
---

# [SOP] Antigravity V6 외부 데이터셋 이식 워크플로우 (ETL Pipeline)

## 1. 개요 (Purpose)
본 문서는 외부 지식(GitHub, 논문, 데이터셋 등)을 Antigravity 시스템의 코어 지식망(`02_Knowledge`)을 오염시키지 않으면서 고성능 RAG 검색의 일부로 편입시키기 위한 **표준 ETL(Extract, Transform, Load) 파이프라인**을 정의한다.

## 2. 4단계 표준 공정 (Standard Processes)

### 🛠️ Step 1. 추출 및 분할 (Extraction & Chunking)
- **작업**: 원본 데이터(README.md 등)를 그대로 가져오지 않고, `github_ingestor.py` 스크립트를 사용하여 `##` (소제목) 단위로 텍스트를 정밀하게 분할한다.
- **이유**: 양자 화학(QM), 머신러닝 데이터셋 등 카테고리별로 덩어리(Chunk)를 나누어야 나중에 검색 엔진이 정확한 조준점(Targeting)을 잡을 수 있다.

### 🏭 Step 2. 포맷팅 및 HyDE 태그 주입 (Transformation)
- **작업**: 쪼개진 텍스트 덩어리를 Gemini 에이전트가 **7-Layer YAML** 규격으로 재작성한다. 불필요한 코드를 제거하고 정제된 마크다운을 생성한다.
- **방화벽 제어 (핵심)**:
  - `domain: 99_External_Dataset`: 현장 문서와 섞이지 않도록 도메인을 격리한다.
  - `T_static: 0.2`: 신뢰도 계급을 낮춰, 현장 SOP 검색 시 이 데이터가 1순위로 튀어나오는 것을 방지한다.
  - `expected_queries`: AI가 스스로 이 데이터가 쓰일 법한 현장 질문(가상 질문)을 창작하여 삽입함으로써 임베딩 성능을 향상시킨다.
  - `has_action: false`: 외부 데이터 기반의 무분별한 액션 제안을 차단한다.

### 📁 Step 3. 물리적 볼트 격리 (Loading & Isolation)
- **작업**: 변환된 마크다운 파일들을 `C:\Antigravity\03_External_Data\Chemistry_Datasets` 폴더에 물리적으로 분리하여 저장한다.
- **이유**: 벡터 공간(Vector Space) 오염을 막고, 옵시디언 그래프 뷰에서 외부 지식이 수석님의 코어 지식을 침범하지 않도록 경계를 긋는다.

### 🧠 Step 4. 벡터 공간 동기화 (Vector Sync)
- **작업**: 모든 파일이 저장된 후, 파이썬 터미널에서 `python rag_cli_v2.py --sync` 명령어를 실행한다.
- **결과**: `sync_checkpoint.json`이 신규 문서를 감지하고, 로컬 엔진(BGE-M3)이 본문과 HyDE 가상 질문을 뭉쳐 벡터(좌표)로 변환한 뒤 ChromaDB에 안착시킨다.

## 3. 예외 처리 및 유지보수
- API Rate Limit 발생 시 스크립트 내 `time.sleep` 간격을 조정한다.
- 데이터셋의 출처가 변경될 경우 `provenance` 필드를 즉시 업데이트한다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[SOP] v6-3-7-decoupled-rag-and-wiki-entropy-management]
- [[[MOC] chemistry-informatics-hub]]
- [[github_ingestor.py]]
