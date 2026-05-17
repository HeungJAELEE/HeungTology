---
metadata:
  id: "[[[SOP] v6-3-7-decoupled-rag-and-wiki-entropy-management]]"
  domain: "00_System"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[SOP] v6-3-7-decoupled-rag-and-wiki-entropy-management에 관한 고밀도 지능 노드"
semantic:
  tags: ["#00_System", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [SOP] v6-3-7-decoupled-rag-and-wiki-entropy-management

## 1. 개요 (Context)
RAG 엔진의 API 병목(Error 429 [Ref: API_Standard]) 대응을 위한 Decoupled RAG 운영 체계 및 파일명-본문 불일치(Wiki Entropy) 정화 프로토콜을 정의함.

## 2. API 429 Quota Exceeded 대응 전략
API 호출 한도 초과로 인한 RAG Synthesis 중단 시, Decoupled 모드로 즉각 전환하여 가용성을 확보함.

| 운영 모드 | 핵심 메커니즘 | 기술적 사양 |
| :--- | :--- | :--- |
| **Backend (Radar Mode)** | 로컬 GPU 기반 지식 노드 좌표 추출 | `--retrieve-only` 플래그 [Ref: Section_2] |
| **Frontend (Direct Hit Mode)** | `read_file` 기반 에이전트 직접 로드 | 독자 논리 엔진 보고서 생성 [Ref: Section_2] |

## 3. 에이전트 권한 및 데이터 격리 (Sandbox)
데이터 무결성 사수를 위해 에이전트 쓰기 권한을 엄격히 통제함.
* **Read-Only Zone:** `02_Knowledge` 내 모든 자산의 수정/교체(Write/Replace) 금지 [Ref: Section_3].
* **Output Isolation:** 생성 분석물은 `06_Output` 또는 `01_Inbox`로 격리 [Ref: Section_3].
* **Tagging Requirement:** 문단별 출처 태깅 강제 [Ref: Section_3].
    * `[🟢 Local RAG]`: 로컬 검증 팩트 [Ref: Section_3].
    * `[🌐 Web Search]`: 외부 검색 데이터 [Ref: Section_3].

## 4. Wiki Entropy 정화 프로토콜 [Critical]
파일명(Metadata)과 H1/본문(Content) 불일치인 '돌연변이 노드'를 탐지 및 정화함.

### 4.1. 정밀 골격 대조 (Skeleton Comparison)
기호(하이픈, 공백 등)에 의한 오탐 방지를 위해 다음 정규식 기반 골격 대조를 수행함 [Ref: Section_4.1].
`re.sub(r'[^\w\s가-힣]', '', title).replace(' ', '').lower()`

### 4.2. 돌연변이 유형별 Triage (수술 가이드)
| 위험 등급 | 유형 (Type) | 증상 (Symptom) | 조치 (Action) |
| :--- | :--- | :--- | :--- |
| **Medium** | Literary Subtitles | 파일명-골격 동일, H1 부연 설명 포함 | `Auto-Heal` (자동 절제) [Ref: Section_4.2] |
| **High** | Identity Swap | 도메인-내용 완전 불일치 | `Manual Override` (수동 재배치) [Ref: Section_4.2] |
| **High** | Legacy Squatting | H1 제목 구 규격(v4.2) 고착 | `Manual Update` (HDS-Gold 적용) [Ref: Section_4.2] |

## 5. 성능 비교 분석 (Theoretical vs Verified)

| 평가 지표 | 이론치 (Theoretical) | 검증치 (Verified) | 비고 |
| :--- | :--- | :--- | :--- |
| **API 429 회복력** | Synthesis 중단 및 작업 실패 | Decoupled 모드 전환을 통한 지속 수행 [Ref: Section_2] | 가용성 확보 |
| **엔티티 일치 정밀도** | 단순 문자열 매칭 (String Match) | 정규식 기반 골격 대조 (Regex-Skeleton) [Ref: Section_4.1] | 오탐율 감소 |
| **데이터 동기화 속도** | 수동 탐색 및 수정 | `rag_cli_v2.py --sync` 자동 동기화 [Ref: Section_5] | 운영 효율 증대 |

## 6. 정화 도구 레퍼런스 (Surgical Tools)
* `v62_triple_sync_healer.py`: 안전 구역 자동 절제 및 고위험군 리포트 [Ref: Section_6].
* `v622_atomic_splitter_live.py`: `---Slide---` 패턴 기반 엔티티 분화 [Ref: Section_6].
* `v623_global_sync_healer.py`: H1 제목-파일명 전수 강제 동기화 [Ref: Section_6].
* `v624_gauge_cleaner.py`: 문서 하단 잔류 게이지 로그 소거 [Ref: Section_6].
