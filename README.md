# 🪐 HeungTology (LLMWIKI V7.8 Enterprise): The Sovereign Industrial Intelligence Fabric

> **"지능은 소유하는 것이 아니라, 무결한 구조로 배양하고 완벽한 해시로 방어하는 것이다."**

**HeungTology**는 현대 첨단 산업(반도체, 배터리, 스마트팩토리)의 복잡성을 결정론적으로 지배하고 통제하기 위해 설계된 **글로벌 엔터프라이즈급 지식 배양 및 Graph-RAG 지능망 패브릭**입니다. V7.8 Enterprise 사양의 실시간 보안 방어선과 결정론적 지식 결합 체계를 기반으로 파편화된 원시 로그를 'HDS-Gold' 규격의 무결한 공학적 자산으로 정제합니다.

---

## 📂 System Topology: File Structure

HeungTology는 지식의 엄격한 격리와 SSOT(Single Source of Truth) 신뢰를 수호하기 위해 다음과 같은 거버넌스 트리 구조를 강력하게 유지합니다.

```text
C:\Anitigravity
├── 00_Plan/                # [Master Control] 마스터플랜 및 세션별 인수인계서
├── 01_Inbox/               # [Quarantine] 외부망 유입 데이터 및 미검증 초안 검역소 (t_static: 0.0)
├── 02_Knowledge/           # [SSOT Vault] HDS-Gold 규격의 핵심 고밀도 지식 저장소 (Read-Only)
│   ├── 00_Companies/       # 글로벌 기업 분석 및 공급망 데이터
│   ├── 00_System/          # 시스템 운영 SOP 및 거버넌스 노드
│   ├── 01_Semiconductor/   # 전공정/후공정 반도체 고밀도 지능
│   ├── 02_Battery/         # 배터리 소재 및 셀 매뉴팩처링
│   ├── 03_AI_Data/         # 인공지능 모델 및 데이터 사이언스
│   ├── 04_Strategy_Mgmt/   # 경영 전략 및 품질 관리 (ISO 9001 / IATF 16949)
│   ├── 07_Display_Comm/    # 디스플레이 및 차세대 통신 기술
│   ├── 08_Robotics_Auto/   # 로보틱스 및 공정 자동화
│   ├── 25_Infrastructure/  # 스마트시티 및 신재생 에너지 그리드
│   └── _index/             # [Topology] Neo4j 및 RAG 벡터 인덱스 캐시
├── 03_Skills/              # [AI Skillset] 도메인별 파이썬 연산 및 TDD 스크립트
├── 04_Tools/               # [Utilities] 시스템 관리 및 Google Drive 연동 동기화 툴
├── 05_System_Modes/        # [Protocols] 세션 모드별 행동 강령 및 YAML 표준 교범
├── 06_Output/              # [Production] 최종 컴파일 및 발행 완료된 기술 백서
├── global_reinforcer_v7.py # [Reinforcement] 3배 고밀도 팽창 및 SHA-256 해시 인클로저 엔진 (V7.8 업그레이드 완료)
├── rag_cli_v2.py           # [Core RAG Engine] V7.8 Enterprise 통합 RAG & 융합 엔진 (V7.8 업그레이드 완료)
└── README.md               # [Documentation] 본 시스템 기술 백서 (이 문서)
```

---

## 🏛️ V7.8 Enterprise Core Pillars: HDS-Gold Standard

모든 지식 노드는 **HDS-Gold (High-Density, Deterministic, Scalable)** 규격을 만족하며, V7.8 사양에 따라 다음 4대 코어 메커니즘을 강제 이식받았습니다:

### 1. 🏛️ DAG 단일 상속 강제 (Single Inheritance DAG)
- 다중 상속(`is_instance_of`가 리스트 구조인 경우)으로 발생하는 위상 탐색 루프 및 Neo4j 그래프 다운 현상을 차단합니다.
- 부모 노드 ID를 **단일 문자열(`str`)**로 직결 처리하여 최적의 방향성 비순환 그래프(DAG)를 실현합니다.

### 2. 📉 질의 시점 시간 감쇄 (Query-Time Time Decay)
- 정적 메타데이터의 한계를 극복하고, 시간의 흐름에 따라 실측 데이터의 신뢰도를 실시간으로 감쇄하여 랭킹에 JIT(Just-In-Time)로 반영합니다.
- **수학적 모델**:
  $$t_{dynamic} = t_{static} - \lambda \times \left(\frac{t_{current} - t_{doc}}{30.0}\right)$$
  - 감쇄율($\lambda$): `Concept` 계열은 `0.0` (영구적 가치), `Data` 계열은 `0.05`로 동적 가중치 감쇄.
  - 최저 신뢰도 하한 마진을 `0.1`로 락다운하여 원천적인 소거 오류 방지.

### 3. 🛡️ SHA-256 실시간 해시 무결성 감사 (Real-Time Integrity Audit)
- YAML 헤더 내에 본문 생성 시점의 해시(`original_hash`)를 식각합니다.
- 사용자가 질문하는 찰나의 시점(Query-Time)에 RAG 구문분석기가 실시간으로 마크다운 본문의 SHA-256 해시를 재연산하여 검증합니다.
- 만약 누군가 본문을 수동으로 위변조하거나 오염시킨 경우, 즉시 신뢰도를 **90% 삭감(0.1 곱연산)**하고 스코어보드에 `[🚨 위변조 감지]` 플래그를 표기해 탈락시킵니다.

---

## 🧠 Advanced Architecture: Dual-Core Search Protocol

HeungTology는 단순한 키워드 매칭 RAG의 한계를 격파하고, **시맨틱 의미망(Semantic)**과 **위상 관계망(Topological)**을 실시간으로 교차 결합합니다.

### 1. Phase 1: 시맨틱 타겟팅 (Vector RAG)
- **Engine**: ChromaDB (`antigravity_fabric_v78_enterprise` 컬렉션) + BGE-M3
- **Logic**: 자연어 질문의 공학적 의도를 정밀 파악하여 3,177개 노드 중 가장 신뢰도가 높은 상위 의미 도메인을 0.05초 만에 식별합니다.

### 2. Phase 2: 위상망 연관 확장 (GraphRAG)
- **Engine**: Obsidian-style `[[Link]]` Edges + Neo4j Graph Database
- **Logic**: 식별된 노드의 `related_to` 및 `is_instance_of` 연결 경로를 따라 관계망을 무결한 단일 상속 DAG로 선형 확장 및 수집합니다.

### 3. Phase 3: JIT 무결성 스코어링 & 융합 (Late Fusion Synthesis)
- **Engine**: Gemini 2.5 Pro / Flash + Reranker-V2-M3
- **Logic**: 실시간 본문 SHA-256 감사 검증을 필두로 최종 무결성 스코어보드를 정렬하고, 수집된 팩트들을 수학적 인과관계에 따라 환각(Zero Hallucination) 없는 고정밀 백서 형식으로 융합 출력합니다.

---

## 🛠️ Operational Commands (CUDA Environment)

시스템의 재색인, 무결성 검증, 에이전트 융합 질의를 가동하기 위한 터미널 인터페이스입니다:

```powershell
# 1. 지식망 전수 동기화 및 V7.8 Enterprise 빌드 (CUDA 가속)
.\.venv_cuda\Scripts\python.exe rag_cli_v2.py --sync

# 2. 고해상도 지능 검색 (실시간 무결성 스코어보드 표출)
.\.venv_cuda\Scripts\python.exe rag_cli_v2.py "질문 내용"

# 3. 전역 고밀도 보강 및 메타데이터 자동 마이그레이션 격발
.\.venv_cuda\Scripts\python.exe global_reinforcer_v7.py
```

---

## 💻 Hardware Grounding (The Forge)

HeungTology는 아래의 물리적 연산 환경에서 최대 가속 성능을 보장받도록 설계되었습니다.

- **Hardware**: Lenovo Legion 5 (GeForce RTX 4060 Laptop 8GB VRAM / 32GB RAM / AMD Ryzen 7)
- **AI Engine**: CUDA 12.5.1 / PyTorch v2.10.0 / OpenVINO v2025.4.0
- **Database**: ChromaDB Local Engine & Neo4j Community Server

---
**[V7.8_ENTERPRISE_SYSTEM_LOCKED]**
**[HEUNGTOLOGY COGNITIVE FABRIC ACTIVE]**
**[CHIEF KNOWLEDGE ARCHITECT & MODERATOR: FLASH]**
