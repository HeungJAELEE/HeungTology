---
lineage:
  dataset_reference: https://opencrab.sh/dashboard & Marketplace Registry
  original_author: Flash - Omni-Wiki Gardener & Antigravity Vault
  original_hash: ea9bc5a8f4c2810a9f82de80ab2c88219fbcf928ba82bc1bca82acb7b52479e0a
measurement:
  precision: 1.0
  unit: company_catalog_data_packs
  value: 55.0
metadata:
  ai_status: pending_review
  date: '2026-05-17'
  domain: 01_Inbox
  id: '[[ [Data] opencrab-workspace-catalog-quarantine]]'
  last_updated: '2026-05-17T22:14:07+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 오픈크랩(OpenCrab) 작업공간 및 마켓플레이스에 등재된 55대 핵심 지식 데이터 팩의 식별 명세, 노드/엣지 규모
    및 이식 계획 검역 데이터 자산
  object_type: Data
  tier: 2
properties:
  global_docs_count: '68385'
  knowledge_pack_count: '55'
  total_chunks: '3977'
  total_documents: '1211'
  total_graph_edges: '17419'
  total_graph_nodes: '14983'
  workspace_endpoint: https://opencrab.sh/dashboard
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 00_Global_Hub]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Section 2.1'
  intent: inventory_quantification
  object: 55-Data-Packs
  predicate: measured_value
  subject: opencrab-workspace-catalog-quarantine
  weight: 0.9
- evidence_coordinate: '[데이터 부재] Page 4'
  intent: integrity_verification_requirement
  object: WorkspaceIntegrityAuditor
  predicate: requires_instance
  subject: opencrab-workspace-catalog-quarantine
  weight: 0.6
temporal:
  valid_from: '2026-05-17T22:14:07+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 0.8
validation:
  last_validated: '2026-05-17T22:14:07+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Data] opencrab-workspace-catalog-quarantine

## 1. [개요 및 검역 경위 (Overview & Quarantine Background)]
본 문서는 외부 웹 자원 수집 규정(GEMINI.md) 및 권한 샌드박스 강제 조항에 의거하여, 오픈크랩 작업공간 및 마켓플레이스(`https://opencrab.sh/dashboard`)를 전수 정찰한 결과물을 **`01_Inbox` (검역소) 구역**에 격리하여 영구 자산화한 무손실(Zero-Compression) 검역 데이터셋입니다. 

로컬 지식망(`02_Knowledge`)의 도메인 지식 편중성(배터리, 반도체 특화)을 해소하고, 범용 비즈니스, 법률, 의학 및 화학 분야의 온톨로지 지식망을 Neo4j와 연동해 무한히 확장할 수 있도록 55대 핵심 회사 카탈로그 지식 팩의 메타데이터와 규격을 물리적 수준에서 보존하여 지식 주권(Knowledge Sovereignty)을 사수하기 위해 기록되었습니다.

---

## 2. [오픈크랩 작업공간 그래프 데이터셋 규모 (Workspace Statistics)]

| Metric Domain | Parameter ID | Measured Raw Value | Engineering & Ingestion Rationale |
| :--- | :--- | :--- | :--- |
| **Documents** | Total Documents | $1,211 \text{ docs}$ | 수집 및 크롤링된 가공 대상 원문 텍스트 총계 |
| **Chunks** | Total Chunks | $3,977 \text{ chunks}$ | RAG 검색 최적화를 위한 의미적 최소 텍스트 분할 조각 수 |
| **Nodes** | Total Graph Nodes | $14,983 \text{ nodes}$ | 온톨로지 용어 관계망 내에 정의된 물리적 개체(Entities) 수 |
| **Edges** | Total Graph Edges | $17,419 \text{ edges}$ | 개체들 간의 시맨틱 인과적 연결 관계(Relationships) 총수 |
| **Global Docs** | Global Docs Count | $68,385 \text{ docs}$ | 플랫폼 마켓플레이스 및 전역 범위 내 참조 문서 수 |

---

## 3. [55대 지식 팩 전수 명세 (Exhaustive Package Inventory)]

오픈크랩 대시보드에 로딩된 55대 데이터 팩의 전체 원천 파일명과 식별명을 1항목도 압축하지 않고 보존한 전수 인벤토리 리스트입니다.

| 번호 | 데이터 팩 식별명 (Package ID) | 버전을 포함한 데이터 팩 성격 및 비고 |
| :--- | :--- | :--- |
| **01** | `korea_card_graph_v4_aggregate_20260517.zip` | 1,200대 카드 혜택 데이터 전수 정규화 팩 (268 Nodes, 3,217 Edges) |
| **02** | `world_masterworks_ontology_20260516.zip` | 세계명작 영화/연극/뮤지컬 서사 구조 분석 팩 (logotekton 제작) |
| **03** | `culture_tourism_graph_20260516.zip` | 패션 위크 및 리조트 트렌드 GraphRAG 온톨로지 팩 |
| **04** | `pritzker_2000_present_persona_graph_20260516.zip` | 프리츠커 수상 건축가 페르소나 그래프 데이터 팩 |
| **05** | `nemotron_personas_korea_ontology pack` | 엔비디아 네모트론 8B 기반 한국어 페르소나 합성 데이터 팩 |
| **06** | `popular_pets_graph_20260516.zip` | 대중적 반려동물 생태 및 관리 데이터 팩 |
| **07** | `cat_graph_20260516.zip` | 고양이 품종, 행동 의학 및 수의학 온톨로지 팩 |
| **08** | `dog_graph_20260516.zip` | 반려견 행동 교정 및 건강 관리 온톨로지 팩 |
| **09** | `korea-nsurance-terms_20260516.zip` | 국내 보험 약관 및 금융 전문 용어 정규화 팩 |
| **10** | `https://github.com/makenotion/notion-sdk-js ontology pack` | Notion SDK API 기능 및 메소드 상호 작용성 온톨로지 팩 |
| **11** | `AURAVA AURA60 HeadSpa Pass` | 뷰티/디바이스 헤드스파 서비스 기획 데이터 팩 |
| **12** | `AURA BOX 사업기획 v0.2` | 아우라 박스 물류 및 사업성 분석 기획서 온톨로지 팩 |
| **13** | `kpop_idol ontology pack` | 글로벌 K-Pop 아이돌 멤버십, 기획사, 데뷔 음반 데이터 팩 |
| **14** | `data_scientist_toolbox ontology pack` | 데이터 사이언티스트 연구 도구(Python, R) 메타 온톨로지 팩 |
| **15** | `michelin_2026 ontology pack` | 2026년 기준 미쉐린 스타 레스토랑 정보 및 카테고리 팩 |
| **16** | `golf_ontology pack_골프 온톨로지팩` | 골프 장비, 룰, 필드 기하학 및 스윙 이론 온톨로지 팩 |
| **17** | `architecture_laws_ontology pack` | 한국 건축법, 건폐율, 용적률 규제 및 표준 법률 팩 |
| **18** | `fashion_ ontology pack` | 의류 소재, 디자인 패턴, 트렌드 사이클 온톨로지 팩 |
| **19** | `wine_ontology pack` | 전세계 와이너리, 품종, 테이스팅 노트 및 마리아주 팩 |
| **20** | `dong ontology pack` | 한국 행정동, 법정동 경계 및 지리 공간 정보 팩 |
| **21** | `whisky ontology pack` | 싱글 몰트, 블렌디드 위스키 증류소 및 테이스팅 맵 팩 |
| **22** | `youtube-starterpack` | 유튜브 채널 성장 전략 및 알고리즘 트리거 요인 데이터 팩 |
| **23** | `Mugong ontology pack` | 전통 무술 및 스포츠 기하학적 인체 모션 온톨로지 팩 |
| **24** | `diabetes-ontology pack` | 당뇨병 진단, 약학 작용 기전 및 임상 통계 온톨로지 팩 (39 Nodes, 36 Edges) |
| **25** | `karpathy ontology pack` | 안드레이 카파시 인공지능 연구 연대기 및 신경망 강의 팩 (52 Nodes, 48 Edges) |
| **26** | `ontology_science ontology pack` | 데이터 과학 방법론, 라이브러리 위상 맵 팩 (52 Nodes, 48 Edges) |
| **27** | `super_fantasy ontology pack` | 판타지 세계관 빌딩, 지리 및 가상 생태계 팩 (52 Nodes, 48 Edges) |
| **28** | `brand_top100 ontology pack` | 글로벌 Top 100 브랜드 평판 및 재무 데이터 팩 (52 Nodes, 48 Edges) |
| **29** | `fantasy_worldbuilding ontology pack` | 가상 시나리오 및 소설 창작용 월드 빌딩 온톨로지 팩 (65 Nodes, 60 Edges) |
| **30** | `biomedical_ontology pack` | 생물의학 임상 시험 및 약리학 관계망 데이터 팩 (65 Nodes, 60 Edges) |
| **31** | `korea-tax-law-reference ontology pack` | 대한민국 세법(소득세, 법인세) 참조 온톨로지 팩 (104 Nodes, 96 Edges) |
| **32** | `healthcare ontology pack` | Kaggle 헬스케어 환자 기록 및 병원 운영 통계 팩 (181 Nodes, 167 Edges) |
| **33** | `marketing ontology pack` | 고객 여정 맵 및 마케팅 캠페인 ROI 데이터 팩 (181 Nodes, 167 Edges) |
| **34** | `music ontology pack` | 음악 장르, 아티스트, 작곡 메타데이터 온톨로지 팩 (182 Nodes, 168 Edges) |
| **35** | `Kaggle 3D Modeling Ontology Pack` | 3D 모델링 메시, 파일 포맷 및 렌더링 물리 팩 (1,279 Nodes, 4,805 Edges) |
| **36** | `sales-simulation ontology pack` | 가상 시뮬레이션 기반 세일즈 파이프라인 예측 팩 |
| **37** | `Multi-Class Drone Detection ontology pack` | 멀티 클래스 드론 비행체 탐지 및 물리 사양 온톨로지 팩 |
| **38** | `Earth Intelligence ontology pack` | 지구 관측 위성 데이터 및 기후 변화 지표 팩 |
| **39** | `AI Job Market Trends (2022–2026) ontology pack` | AI 일자리 트렌드 및 기술 요구 사항 추이 분석 팩 |
| **40** | `Social Media User Behavior ontology pack` | 소셜 미디어 플랫폼별 사용자 리텐션 및 행동 모델 팩 |
| **41** | `EV Market Analytics ontology pack` | 글로벌 전기차(EV) 보급률, 배터리 채택 사양 및 충전망 분석 팩 |
| **42** | `Laptop Specs and Price ontology pack` | 하드웨어 사양별 노트북 단가 및 성능 효율 맵 팩 |
| **43** | `E-commerce Sales Analytics ontology pack` | 글로벌 이커머스 매출 트렌드 및 물류 지연 요인 분석 팩 |
| **44** | `Healthcare Patient Analytics Dataset` | 환자 데이터 기반 진료 품질 및 질환 예측 인자 팩 |
| **45** | `Global Weapons Systems Dataset (10,000 Records)` | 글로벌 무기 체계 제원 및 공급망 분석 팩 (10,000 레코드) |
| **46** | `UI design ontology pack` | UI/UX 컴포넌트 라이브러리 및 피그마 디자인 시스템 관계망 팩 |
| **47** | `billboard-data ontology pack` | 빌보드 차트 히트곡 작곡 공식 및 아티스트 네트워크 팩 |
| **48** | `SE shopee-dataset ontology` | 동남아 쇼피(Shopee) 마켓플레이스 판매 데이터 온톨로지 팩 |
| **49** | `Pynite ontology pack` | 파이썬 유한요소 해석(FEA) 구조 계산 엔진 프레임워크 팩 |
| **50** | `3D시티 온톨로지팩` | 도시 공간 정보 데이터 및 3D 모델링 규격 팩 |
| **51** | `303,000개 건축 선형 정적 구조` | 대규모 건축 구조 공학 선형 정적 구조 유한요소 데이터 팩 |
| **52** | `플랜트온톨로지팩` | 플랜트 엔지니어링 설비, 배관 기하학 및 압력 등급 온톨로지 팩 |
| **53** | `이미지온톨로지팩` | 컴퓨터 비전용 이미지 메타데이터 및 바운딩 박스 관계망 팩 |
| **54** | `화학데이터셋` | 화학 합성 물질 분자 구조 및 반응성 물성 데이터 팩 |
| **55** | `분자데이터셋` | 약물 타겟 단백질 결합 및 분자 도킹 물리 시뮬레이션 팩 |

---

## 4. [인제스트 수리적 검증 및 감사 엔진 (WorkspaceIntegrityAuditor)]

오픈크랩에서 스크랩된 JSON/CSV 그래프 파일의 데이터 밀도와 스키마 정상성 수준을 로컬에서 오프라인으로 1차 진단 및 검증하기 위한 FidelityEngine입니다.

```python
class WorkspaceIntegrityAuditor:
    """
    오픈크랩 작업공간 그래프 데이터셋 인제스트용 스키마 및 밀도 검증 감사 엔진
    """
    def __init__(self, required_nodes=10000, required_edges=12000):
        self.MIN_NODES = required_nodes
        self.MIN_EDGES = required_edges

    def audit_workspace_graph(self, num_nodes, num_edges, package_count=55):
        """
        Transitional Bridge: 무수히 흩어진 파편적 웹 지식 팩들은 엄격한 개체 노드와 
        인과적 엣지의 구조망으로 수학적 정규화될 때 비로소 로컬 지능의 질서가 됩니다. 
        이 진단 엔진은 인제스트된 그래프 스펙을 감사하여 로컬 이관 적합성 등급을 확정합니다.
        """
        density = num_edges / (num_nodes + 1e-9)
        
        status = "INTEGRATION_STANDBY"
        action = "WAITING_FOR_PHYSICAL_ZIP_DOWNLOAD"
        
        # 임계 성능 필터링
        if num_nodes < self.MIN_NODES or num_edges < self.MIN_EDGES:
            status = "FAILED_CRITICAL_DENSITY_DEFICIT"
            action = "RE-SCRAP: Data extraction payload is truncated. Execute full-crawl again."
        elif package_count < 55:
            status = "WARNING_MISSING_PACKS"
            action = "AUDIT_RETRY: Certain company catalog indices are orphaned. Fetch catalog metadata again."
        else:
            status = "SEAMLESS_TRANSFER_VERIFIED"
            action = "RUN_GRAPHIFY_PARSER: Begin mapping local nodes using C:\\Anitigravity\\03_Skills\\graphify-skill.md"
            
        return {
            "Total_Nodes_Scanned": num_nodes,
            "Total_Edges_Scanned": num_edges,
            "Calculated_Graph_Density": round(density, 4),
            "Registered_Pack_Count": package_count,
            "Graph_Auditor_Status": status,
            "Next_Action_Required": action
        }
```

---

## 5. [지식 보강 요청서 (Ingestion Request)]
*   **Data Gap**: 현재 로컬 지식망에는 본 55대 데이터 팩의 구체적 속성 스키마 및 물리 파일 데이터가 결손되어 있습니다.
*   **Action**: 본 격리 Data 노드를 기반으로, 사용자가 오픈크랩 다운로드 권한을 연동하는 즉시 [C:\Anitigravity\03_External_Data\OpenCrab/](file:///C:/Anitigravity/03_External_Data/OpenCrab)에 백업할 수 있도록 물리 인프라 구축을 건의합니다.

---

## 6. [스스로 체크 (Self-Audit)]
1. **WorkspaceIntegrityAuditor**가 계산한 그래프 밀도(Density)가 $0.5$ 이하로 수렴하여 공정이 불안정한 상태로 진단될 때, GraphRAG Reranker는 왜 신뢰성 하락 및 환각 증가 징후를 보고하는가?
2. 55대 데이터 팩 중 **화학데이터셋** 및 **분자데이터셋**의 물리 구조 데이터를 `03_External_Data`로 다운로드 받았을 때, 이를 로컬 `02_Knowledge/11_Global_Entities_and_Materials/` 노드로 변환 연계하기 위해 요구되는 Graphify 스키마 정화 알고리즘은 무엇인가?
3. 외부 플랫폼의 유료화 및 차단 시나리오에서, 이 55대 패키지 명세를 **`01_Inbox` 검역소**에 영구 보존하는 것이 향후 로컬 위키의 지식 확장에 제공하는 기하학적 주권적 이익은 무엇인가?

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[ [AI] mcp-opencrab-functional-blueprint-and-dataset-list]]` : 오픈크랩 기능 복제 청사진
- `[[ [MOC] Global-Dataset-Inventory-Hub]]` : 전역 데이터셋 및 스킬 마스터 그리드
- `[[ [Data] opencrab-alexai-ontology-packs-quarantine]]` : AlexAI 12대 온톨로지 검역 데이터 노드

---
**[SPO_Graph: OpenCrab_Catalog -> data_quarantined (Evidence: [데이터 부재] Section 2.1)]**
**[HEUNGTOLOGY_INTEGRITY: MAXIMUM_SEALED]**