---
aliases: '["V6.3.7 프론트엔드 에이전트 운영 가이드", "분리형 RAG 아키텍처", "위키 오염 복구", "Triple-Sync 정화"]'
type: SOP
Basic:
  domain: 00_System_Governance
  date: 2026-05-09
Object:
  uuid: v6-3-7-decoupled-rag-and-wiki-entropy-management-sop
Semantic:
  tags: '["#SOP", "#System_Governance", "#RAG_Architecture", "#Troubleshooting", "#HDS_Gold_v6_1"]'
  is_part_of: '["MOC 00_master-plan-and-system-governance-hub"]'
  caused_by: '["API_429_Quota_Exceeded_during_RAG_Synthesis", "Legacy_Folder_Merge_causing_Filename_Content_Mismatch"]'
  controls: '["RAG_Fallback_Strategy", "Agent_Write_Permission_Sandbox", "Trust_Source_Tagging", "Mutant_Node_Triage_Protocol", "Vector_DB_Sync_Trigger"]'
Dynamic:
  status: "Ratified (V6.3.7.4 Final)"
Trust Metrics:
  T_init: 1.0
  T_static: 1.0
  note: "수석 아키텍트 직접 승인 SOP. 시스템 헌법급 문서."
provenance: '["Project V6.3.7 지식망 정화 및 아키텍처 업그레이드"]'
related_to: '["MOC 00_master-plan-and-system-governance-hub"]'

# [RLHF Trust Metrics: 점근적 신뢰도 평가 모델]
trust_base: 0.40          # (정적) 파생 문서의 최초 신뢰도 시작점
trust_lambda: 0.3         # (정적) 학습률 (가중치 상승 속도 제어 상수)
citation_count: 0         # (동적) 터미널에서 Y를 누를 때마다 +1씩 누적되는 정수
current_trust_level: 0.40 # (동적) 파이썬 API가 공식을 계산하여 덮어쓰는 최종 결과값
---

# [SOP] v6-3-7-decoupled-rag-and-wiki-entropy-management

## 1. 개요 (Context)
본 문서는 Antigravity V6.3.7 시스템에서 발생하는 RAG 엔진의 API 병목(429 Error) 현상을 해결하기 위한 **분리형 RAG(Decoupled RAG)** 운영법과, 파일명과 본문이 불일치하는 **'위키 오염(Wiki Entropy)'** 사태를 진단하고 복구하는 물리적 정화 프로토콜을 정의한다.

## 2. API 한도 초과 (429 Quota Exceeded) 트러블슈팅
API 호출 한도로 인해 RAG 엔진의 답변 생성(Synthesis)이 멈출 경우, 즉각 '분리형 지식 융합' 프로세스로 전환한다.
* **백엔드 (Radar Mode):** 로컬 GPU를 활용해 관련 지식 노드의 물리적 파일 **경로(좌표)만 도출**한다. (`--retrieve-only` 기능 활용)
* **프론트엔드 (Direct Hit Mode):** 에이전트가 도출된 파일 경로를 `read_file`로 직접 읽어 들인 후, 독자적인 논리 엔진으로 보고서를 직접 생성한다. (이중 요약 및 토큰 낭비 원천 차단)

## 3. 프론트엔드 에이전트 통제 및 권한 샌드박스
* **Read-Only 구역:** 에이전트는 `02_Knowledge` 내의 모든 파일에 대해 절대 수정(Write/Replace)을 금지하며, 오직 읽기만 수행한다.
* **결과물 격리:** 생성된 분석 보고서 및 초안은 반드시 `06_Output` 또는 `01_Inbox`에 저장한다.
* **출처 태깅 강제:** 로컬 검증 팩트는 `[🟢 Local RAG]`, 외부 웹 검색 초안은 `[🌐 Web Search]`로 문단별 출처를 엄격히 분리하여 신뢰도 세척(Trust-Washing)을 방지한다.

## 4. 위키 오염(Wiki Entropy) 진단 및 복구 프로토콜 [핵심]
과거 폴더 통합 및 수동 작업의 잔재로 인해, 파일명(껍데기)과 H1 제목/본문(알맹이)이 따로 노는 '돌연변이 노드'가 발생할 수 있다. 이를 주기적으로 검열하고 정화한다.

### 4.1. 오탐 방지 진단 로직 (초정밀 골격 대조)
진단 스크립트(`v62_triple_sync_healer.py`) 가동 시, 하이픈, 언더바, 공백 등의 단순 기호 차이로 인한 가짜 불일치를 막기 위해 아래의 정규식을 사용해 뼈대만 대조한다.
* **적용 코드:** `re.sub(r'[^\w\s가-힣]', '', title).replace(" ", "").lower()`

### 4.2. 돌연변이 유형별 수술 가이드 (Triage)
대조 결과 불일치 판정이 난 노드들은 위험도에 따라 분리하여 타격한다.
* **[Medium Risk] 문학적 부제목 (Literary Subtitles):**
  - 증상: 파일명과 뼈대는 같으나 H1에 부연 설명이 붙은 경우 (예: `... (The Guardian of Life)`)
  - 조치: 스크립트를 통한 100% 자동 절제 및 파일명 덮어쓰기 (Auto-Heal) 단행.
* **[High Risk] 정체성 교환 (Identity Swap):**
  - 증상: 파일명은 `Battery`이나 내용은 `AI 머신비전`인 등 도메인과 내용이 완전 뒤바뀐 악성 노드.
  - 조치: 절대 스크립트 자동화 금지. 원문을 읽고 내용(알맹이)에 맞춰 파일명과 도메인 폴더를 수동으로 재배치(Manual Override)한다.
* **[High Risk] 레거시 포맷 점유 (Legacy Squatting):**
  - 증상: H1 제목이 과거 버전 규격(예: `[v4.2 RLHF...]`)으로 방치되어 본문을 덮어버린 경우.
  - 조치: 관리자가 본문 내용을 스캔하여 최신 HDS-Gold 규격의 H1 제목으로 수동 갱신한다.

## 5. 온톨로지 비동기 대응
에이전트가 탐색 중 `FileNotFound` 에러에 직면할 경우 무작위 탐색을 중단하고, 관리자에게 즉각 `rag_cli_v2.py --sync`를 통한 벡터 DB 동기화를 요청해야 한다.

## 6. 정화 도구 매뉴얼 (Surgical Tools Reference)

| 도구 | 용도 | 가동 조건 |
|:---|:---|:---|
| `v62_triple_sync_healer.py` | 안전 구역(부제목) 자동 절제 + 고위험군 격리 리포트 생성 | 주기적 / 대규모 노드 이동 후 |
| `v622_atomic_splitter_live.py` | `---Slide---` 벌크 파일을 개별 엔티티로 분화 | `intelligence-batch` 패턴 탐지 시 |
| `v623_global_sync_healer.py` | 리포트 기반 H1 제목-파일명 전수 강제 동기화 | `HIGH_RISK_MUTANT_REPORT.md` 갱신 후 |
| `v624_gauge_cleaner.py` | 문서 하단 잔류 게이지 로그 전수 소거 | 대규모 세션 종료 후 |

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 00_master-plan-and-system-governance-hub : 시스템 거버넌스 최상위 허브
- SOP cross-domain-industrial-ontology-mapping-and-data-fusion-protocol : 온톨로지 매핑 프로토콜

*Ratified by Chief Architect — 2026-05-09*
