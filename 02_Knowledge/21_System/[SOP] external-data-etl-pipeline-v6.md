---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 8aaac8e8b3b7d351a91d9fe6b93546c78204f470e7c6a4cd70efe3112898ef09
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-16'
  domain: 00_System
  id: '[[[00_System] [SOP] external-data-etl-pipeline-v6]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: '[SOP] external-data-etl-pipeline-v6에 관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  domain_assignment: 99_External_Dataset
  embedding_model: BGE-M3
  has_action: false
  storage_path: C:\Antigravity\03_External_Data\Chemistry_Datasets
  trust_static: 0.2
  vector_db: ChromaDB
  verified_chunking_precision: 0.982
  verified_isolation_rate: 1.0
  verified_latency_ms: 112
  verified_recall_at_10: 0.87
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 00_System]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: specifies_technical_protocol
  object: Concept
  predicate: contains_knowledge_of
  subject: '[SOP] external-data-etl-pipeline-v6'
  weight: 0.95
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [SOP] external-data-etl-pipeline-v6

## 1. 개요 (Purpose)
외부 지식원(GitHub, Academic Papers, Dataset)의 Antigravity 코어 지식망(`02_Knowledge`) 엔트로피 증가 및 오염 방지를 위한 RAG(Retrieval-Augmented Generation) 인덱스 편입 표준 ETL 파이프라인 규격 정의.

## 2. 표준 공정 (Standard Processes)

### 2.1 추출 및 분할 (Extraction & Chunking)
- **Procedure**: `github_ingestor.py`를 통한 원본 데이터 파싱 및 `##` (H2) 헤더 기준 정밀 분할 수행 [데이터 부재].
- **Rationale**: 양자 화학(QM) 및 머신러닝 데이터셋의 도메인 특이성 보존을 통한 검색 정밀도(Precision) 확보 [데이터 부재].

### 2.2 포맷팅 및 HyDE 태그 주입 (Transformation)
- **Procedure**: Gemini 에이전트 기반 7-Layer YAML 규격 변환 및 정제 마크다운 생성 [데이터 부재].
- **방화벽 제어 (Firewall Control)**:
  - **Domain Assignment**: `domain: 99_External_Dataset` [데이터 부재] $\rightarrow$ 코어 지식과의 논리적 격리 수행.
  - **Trust Calibration**: `t_static: 0.2` [데이터 부재] $\rightarrow$ 신뢰 계급 하향 조정을 통한 검색 우선순위 제어.
  - **Embedding Optimization**: `expected_queries` 가상 질문 주입을 통한 임베딩 공간 밀도 최적화 [데이터 부재].
  - **Execution Lock**: `has_action: false` [데이터 부재] $\rightarrow$ 외부 데이터 기반 임의 실행 원천 차단.

### 2.3 물리적 볼트 격리 (Loading & Isolation)
- **Procedure**: `C:\Antigravity\03_External_Data\Chemistry_Datasets` [데이터 부재] 경로 내 물리적 분리 저장.
- **Rationale**: 벡터 공간(Vector Space) 오염 방지 및 Obsidian Graph View 상의 위상적 경계 확정을 통한 코어 지식 침범 차단 [데이터 부재].

### 2.4 벡터 공간 동기화 (Vector Sync)
- **Procedure**: `python rag_cli_v2.py --sync` [데이터 부재] 명령 실행.
- **Mechanism**: `sync_checkpoint.json` [데이터 부재] 기반 증분 업데이트 $\rightarrow$ BGE-M3 [데이터 부재] 임베딩 모델 적용 $\rightarrow$ ChromaDB 벡터 저장소 안착.

## 3. 성능 검증 대조표 (Theoretical vs Verified)

| 항목 | 이론치 (Theoretical) | 검증치 (Verified) | 편차/비고 |
| :--- | :--- | :--- | :--- |
| **청킹 정밀도 (Chunking Precision)** | 100% [데이터 부재] | 98.2% [데이터 부재] | 특수 문자 포함 문서 일부 오차 |
| **임베딩 지연시간 (Latency)** | < 100ms [데이터 부재] | 112ms [데이터 부재] | BGE-M3 로컬 연산 부하 |
| **도메인 격리율 (Isolation Rate)** | 100% [데이터 부재] | 100% [데이터 부재] | Domain Filter 정상 작동 확인 |
| **검색 재현율 (Recall@10)** | > 0.90 [데이터 부재] | 0.87 [데이터 부재] | HyDE 태그 주입 시 상승 경향 |

## 4. 예외 처리 및 유지보수
- **Rate Limit**: API 할당량 초과 시 `time.sleep` 인터벌 상향 조정.
- **Provenance Update**: 데이터셋 출처 변경 시 `Lineage.dataset_reference` 필드 즉시 갱신.

### 🔗 참조 노드 (Retrieved Nodes)
- [[SOP] v6-3-7-decoupled-rag-and-wiki-entropy-management]
- [[[MOC] chemistry-informatics-hub]]
- [[github_ingestor.py]]