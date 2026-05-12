# 🪴 Antigravity V6.3.7: The Sovereign Industrial Intelligence Engine

> **"지능은 소유하는 것이 아니라, 무결한 구조로 배양하는 것이다."**

Antigravity는 현대 산업의 복잡성을 결정론적으로 지배하기 위해 설계된 **고밀도 지식 배양 및 RAG(Retrieval-Augmented Generation) 엔진**입니다. V6.3.7 하드코어 보안 패치와 Trust-Zero 개방형 지능망을 기반으로, 파편화된 데이터를 'HDS-Gold' 규격의 산업적 자산으로 변환합니다.

---

## 📂 System Topology: File Structure

Antigravity는 지식의 위계와 격리를 보장하기 위해 다음과 같은 엄격한 트리 구조를 유지합니다.

```text
C:\Anitigravity
├── 00_Plan/                # [Master Control] 프로젝트 기획 및 인수인계서
├── 01_Inbox/               # [Quarantine] 외부망 유입 데이터 및 미검증 초안
├── 02_Knowledge/           # [SSOT Vault] HDS-Gold 규격의 핵심 지식 저장소
│   ├── 00_Companies/       # 글로벌 기업 분석 및 공급망 데이터
│   ├── 00_System/          # 시스템 운영 SOP 및 거버넌스 노드
│   ├── 01_Semiconductor/   # 전공정/후공정 반도체 지능
│   ├── 02_Battery/         # 배터리 소재 및 셀 매뉴팩처링
│   ├── 03_AI_Data/         # 인공지능 모델 및 데이터 사이언스
│   ├── 04_Strategy_Mgmt/   # 경영 전략 및 품질 관리(ISO/IATF)
│   ├── 07_Display_Comm/    # 디스플레이 및 차세대 통신 기술
│   ├── 08_Robotics_Auto/   # 로보틱스 및 공정 자동화
│   ├── 25_Infrastructure/  # 스마트시티 및 에너지 그리드
│   └── _index/             # [Topology] Neo4j 및 RAG 벡터 인덱스 캐시
├── 03_Skills/              # [AI Skillset] 도메인별 파이썬 연산 및 TDD 스크립트
├── 04_Tools/               # [Utilities] 시스템 관리 및 동기화 유틸리티
├── 05_System_Modes/        # [Protocols] 세션 모드별 행동 강령(Rule)
├── 06_Output/              # [Production] 최종 발행된 기술 백서 및 보고서
├── rag_cli_v2.py           # [Core Engine] V6.3.7 RAG & 융합 엔진
└── README.md               # [Documentation] 본 시스템 기술 백서
```

---

## 🚀 Core Pillar: HDS-Gold V6.3.7 Standard

모든 지식 노드는 **HDS-Gold (High-Density, Deterministic, Scalable)** 규격을 준수하며, 5-Layer YAML 거버넌스를 통해 관리됩니다.

1.  **Basic Layer**: 고유 식별자(UID) 및 도메인 위계 정의.
2.  **Object Layer**: Concept, SOP, Manual, Data 등 지식의 성격 분류.
3.  **Semantic Layer**: 시맨틱 태그 및 Topology Policy를 통한 관계망 정의.
4.  **Dynamic Layer**: FidelityEngine 진단 상태 및 지식 엔트로피 제어.
5.  **Trust Metrics**: T_static(인간 검증) 및 T_dynamic(AI 추론) 신뢰도 지표.

---

## 🧠 Advanced Architecture: Dual-Core Search Protocol

Antigravity는 단편적인 벡터 검색의 한계를 넘어, **의미망(Semantic)**과 **위상망(Topological)**을 실시간으로 융합합니다.

### 1. Phase 1: Semantic Targeting (Vector RAG)
- **Engine**: ChromaDB + BGE-Reranker (Trust-Zero Mode)
- **Logic**: 질문의 의도를 분석하여 수천 개의 노드 중 가장 유사도가 높은 핵심 엔티티를 0.1초 내에 타격합니다.

### 2. Phase 2: Topological Expansion (GraphRAG)
- **Engine**: Obsidian-style `[[Link]]` Analysis + Neo4j Graph
- **Logic**: 타격된 핵심 노드에서 파생된 연관 노드들을 그래프 경로를 따라 추적하여, 질문의 맥락을 입체적으로 확장합니다.

### 3. Phase 3: Late Fusion Synthesis
- **Engine**: Gemini 2.0 Flash (Optimized for Industrial Reasoning)
- **Logic**: 수집된 파편들을 '결정론적 인과관계'에 따라 재구성하여, 환각 없는 최적의 산업적 해답을 도출합니다.

---

## 📂 Vault Hierarchy: The Command Center

- **`00_Plan/`**: 마스터플랜 및 시스템 운영 지휘소.
- **`01_Inbox/`**: 미검증 외부 데이터 및 리서치 초안 검역소.
- **`02_Knowledge/`**: **Single Source of Truth.** 고밀도 엔지니어링 노드 저장소.
- **`03_Skills/`**: 데이터 분석, TDD, 브라우저 제어 등 모델의 행동 스킬셋.
- **`06_Output/`**: 최종 발행된 백서 및 기술 보고서.

---

## 🏛️ Deep-Dive: The Antigravity Ontology & Architecture

### 1. File System Philosophy: The Knowledge Factory
Antigravity의 폴더 구조는 **지식의 생애주기(Lifecycle)**와 **보안 격리(Quarantine)**를 기반으로 설계되었습니다.

- **`00_Plan/` (지휘소)**: 시스템의 뇌입니다. 마스터플랜과 인수인계서가 위치하며, 모든 분석의 '목적성'을 규정합니다.
- **`01_Inbox/` (검역소)**: 외부망에서 유입된 미검증 데이터(`Draft`)가 머무는 곳입니다. 이곳의 데이터는 `T_static: 0.0`으로 취급되어 지식망을 오염시키지 못하도록 철저히 격리됩니다.
- **`02_Knowledge/` (결정소)**: **Single Source of Truth.** 검증된 팩트만이 이곳에 입성합니다. 산업 표준, 물리 법칙, 확정된 기술 SOP가 고밀도로 저장됩니다.
- **`03_Skills/` (도구소)**: 에이전트가 실행할 수 있는 '근육'입니다. RAG 연산, 데이터 분석, TDD 등 모든 논리적 행동 지침이 스크립트 형태로 존재합니다.
- **`06_Output/` (산출소)**: 지식의 결정체입니다. 위키 노드들이 융합되어 최종적으로 발행되는 백서와 보고서가 위치합니다.

### 2. The 5-Layer YAML Rationale: Why So Complex?
V6.3.7의 YAML 구조는 LLM의 모호성을 제거하고 **'기계가 읽을 수 있는 지식(Machine-Readable Knowledge)'**을 만들기 위한 규격입니다.

| Layer | Engineering Purpose | RAG Interaction |
| :--- | :--- | :--- |
| **Basic** | **정체성 확립** | UID를 통해 문서 간의 유일성을 보장하고 도메인 위계를 설정합니다. |
| **Object** | **지식의 성격 규정** | `Concept`은 이해를, `SOP`는 실행을 목적으로 검색 가중치를 다르게 적용합니다. |
| **Semantic** | **위상망 구축** | `[[Link]]`와 태그를 통해 단순 검색을 넘어선 **Topological Search**를 가능케 합니다. |
| **Dynamic** | **엔트로피 제어** | 지식의 신선도와 진단 상태를 추적하여 스스로 진화하는 지식망을 구현합니다. |
| **Trust** | **정밀도 통제** | `T_static`과 `T_dynamic`을 분리하여, 인간의 지혜와 AI의 추론을 명확히 구분합니다. |

### 3. Why HDS-Gold? (The War on Hallucination)
산업 현장에서 AI의 환각은 치명적입니다. 우리는 이를 **'고밀도 결정론(High-Density Determinism)'**으로 해결합니다.
- **고밀도(High-Density)**: 문서를 80~120라인으로 강제하여 정보의 밀도를 높입니다. 이는 LLM이 답변 생성 시 참조할 '팩트 밀도'를 극대화하여 뇌피셜이 끼어들 틈을 주지 않습니다.
- **결정론(Deterministic)**: `FidelityEngine`과 LaTeX 수식을 본문에 강제 삽입합니다. 언어 모델의 모호한 서술을 수학적/논리적 확정성으로 대체하여 '항상 동일하고 정확한' 기술 답변을 보장합니다.

---

## 🛠️ Operational Commands

시스템 가동을 위한 핵심 인터페이스입니다.

```powershell
# 1. 지식망 전수 동기화 (Vector & Graph Sync)
.\.venv_cuda\Scripts\python.exe rag_cli_v2.py --sync

# 2. 고해상도 지능 검색 (Retrieve Only)
.\.venv_cuda\Scripts\python.exe rag_cli_v2.py --retrieve-only "질문 내용"

# 3. 에이전트 융합 답변 가동
.\.venv_cuda\Scripts\python.exe rag_cli_v2.py "질문 내용"
```

---

## 💻 Hardware Grounding (The Forge)

Antigravity는 아래의 물리적 환경에서 최적화된 성능을 발휘하도록 하드웨어 레벨에서 설계되었습니다.

- **Machine**: Lenovo Legion 5 (RTX 4060 8GB VRAM / 32GB RAM)
- **AI Backend**: CUDA 12.5.1 / PyTorch v2.10.0 / OpenVINO v2025.4.0
- **Environment**: Ubuntu 24.04 LTS & Windows 10 Cross-Hybrid

---

**[V6.3.7_STRICT_MODE_ACTIVE]**
**[MODERATOR: FLASH - THE CHIEF KNOWLEDGE ARCHITECT]**
