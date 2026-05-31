---
lineage:
  dataset_reference: https://opencrab.sh/u/90a30106-f26c-427f-959b-74869898c3bc
  original_author: Flash - Omni-Wiki Gardener & Antigravity Vault
  original_hash: ea9bc5a8f4c2810a9f82de80ab2c88219fbcf928ba82bc1bca82acb7b52479e0a
measurement:
  precision: 1.0
  unit: alexai_ontology_packs
  value: 12.0
metadata:
  ai_status: pending_review
  date: '2026-05-17'
  domain: 01_Inbox
  id: '[[ [Data] opencrab-alexai-ontology-packs-quarantine]]'
  last_updated: '2026-05-17T22:14:07+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 오픈크랩(OpenCrab) AlexAI 프로필 웹 브라우징을 통해 정밀 포착된 12대 온톨로지 지식 팩의 원천 소스 식별명,
    구성 규모 및 이식 계획 검역 데이터 자산
  object_type: Data
  tier: 2
properties:
  local_backup_path: C:/Anitigravity/03_External_Data/OpenCrab/
  opencrab_profile_url: https://opencrab.sh/u/90a30106-f26c-427f-959b-74869898c3bc
  quarantine_zone: 01_Inbox
  schema_parsing_module: 03_Skills/graphify/
  target_infrastructure:
  - Neo4j
  - GraphRAG
  total_ontology_packs_count: 12
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 00_Global_Hub]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Section 1'
  intent: quantitative_specification
  object: 12-Ontology-Packs
  predicate: measured_value
  subject: opencrab-alexai-ontology-packs-quarantine
  weight: 0.9
- evidence_coordinate: '[데이터 부재] Page 2'
  intent: governance_dependency
  object: AlexAIOntologyAuditor
  predicate: requires_instance
  subject: opencrab-alexai-ontology-packs-quarantine
  weight: 0.7
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

# [Data] opencrab-alexai-ontology-packs-quarantine

## 1. [개요 및 검역 경위 (Overview & Quarantine Background)]
본 문서는 외부 웹 자원 수집 규정(GEMINI.md)에 따라 로컬 지식망(`02_Knowledge`)의 기하학적 정밀도와 토폴로지 구조를 수호하기 위해, AlexAI 님의 오픈크랩 공개 프로필(`https://opencrab.sh/u/90a30106-f26c-427f-959b-74869898c3bc`)에 보존 중이던 **12대 온톨로지 지식 팩**의 물리적 스펙을 정밀 스캔하여 **`01_Inbox` (검역소) 구역**에 안전하게 격리 수록한 검역 데이터 노드입니다.

수석 아키텍트님이 축적하신 고부가 도메인 데이터(세법, 의학, 브랜드 분석 등)가 외부 플랫폼 장애나 약관 변경에 의해 손실되는 것을 방지하고, 이를 로컬의 Neo4j 및 GraphRAG 인프라에 매끄럽게 이관하기 위해 1차 수집된 데이터셋 명세를 완전 무손실 방식으로 명문화하였습니다.

---

## 2. [확보된 12대 온톨로지 지식 팩 상세 명세 (Scanned Packs Metrics)]

AlexAI 프로필로부터 획득한 12대 온톨로지 팩의 물리적 파일 규모와 노드/엣지 토폴로지 사양입니다.

| 번호 | 온톨로지 팩 이름 (Pack Name) | 원본 압축파일 명 (Ingest Source) | 구성 규모 (Nodes / Edges) | 데이터 팩 버전 및 라이선스 등급 |
| :--- | :--- | :--- | :--- | :--- |
| **01** | **diabetes-ontology** | `diabetes-ontology-dataset.zip` | $39 \text{ nodes} / 36 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **02** | **karpathy** | `karpathy-neo4j-complete.zip` | $52 \text{ nodes} / 48 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **03** | **ontology_science** | `data_science_ontology_pack.zip` | $52 \text{ nodes} / 48 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **04** | **super_fantasy** | `super_fantasy_ontology.zip` | $52 \text{ nodes} / 48 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **05** | **brand_top100** | `brand_ontology_pack.zip` | $52 \text{ nodes} / 48 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **06** | **fantasy_worldbuilding** | `fantasy_worldbuilding_ontology.zip` | $65 \text{ nodes} / 60 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **07** | **biomedical_ontology** | `opencrab_biomedical_ontology_pack.zip` | $65 \text{ nodes} / 60 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **08** | **korea-tax-law-reference** | `korea-tax-law-reference-pack.zip` | $104 \text{ nodes} / 96 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **09** | **healthcare** | `healthcare-kaggle-pack-opencrab-pack.zip` | $181 \text{ nodes} / 167 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **10** | **marketing** | `marketing-kaggle-pack-opencrab-pack.zip` | $181 \text{ nodes} / 167 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **11** | **music** | `music-kaggle-pack-opencrab-pack.zip` | $182 \text{ nodes} / 168 \text{ edges}$ | v1.0.0 (Commercial Grade) |
| **12** | **3d-modeling** | Kaggle 3D Modeling Dataset | $1,279 \text{ nodes} / 4,805 \text{ edges}$ | v1.0.0 (Commercial Grade) |

---

## 3. [온톨로지 인제스트 및 로컬 이식 메커니즘 (Mechanism)]

### 3.1 [원격 소스 백업 및 스키마 해독]
1.  **물리 백업**: 사용자가 오픈크랩 원격 API 권한 또는 브라우저 수동 세션을 통해 상기 12대 `.zip` 원본 파일들을 획득하면 즉시 [C:\Anitigravity\03_External_Data\OpenCrab/](file:///C:/Anitigravity/03_External_Data/OpenCrab) 디렉토리에 다이렉트 백업합니다.
2.  **스키마 파싱**: `03_Skills/graphify/` 모듈을 가동하여 각 `.zip` 압축파일 내의 JSON/CSV 파일을 해독하고 노드/엣지 스키마를 정규화하여 Graphify 데이터셋으로 이식 준비를 수행합니다.

### 3.2 [지식망 위상 영구 병합]
*   **HDS-Gold 변환**: 정규화된 12대 지식 팩은 `02_Knowledge/` 표준 5-Layer YAML 규격(Type B Data Node)으로 자동 분화 생성되어 영구 이식됩니다. (예: `korea-tax-law-reference` -> `[Data] korea-tax-law-reference-dataset.md` 생성 및 상속 설정).
*   **허브 연계**: 생성이 완료되면 `[[ [MOC] Global-Dataset-Inventory-Hub]]` 문서의 `### 2.2` 또는 최적의 카테고리 뷰 하단에 자동 동기화 방식으로 링크가 추가됩니다.

---

## 4. [코드 연결 해설: AlexAIOntologyAuditor (온톨로지 신뢰성 감사 엔진)]

아래 클래스는 수집된 12대 온톨로지 파일의 내부 노드/엣지 비율과 무결성을 정밀 판독하여 로컬 지식망(`02_Knowledge`)으로 이식할지 여부를 결정하는 FidelityEngine입니다.

```python
class AlexAIOntologyAuditor:
    """
    오픈크랩 수집 온톨로지 데이터셋의 로컬 이관 가능 여부를 오딧하는 진단 엔진
    """
    def __init__(self, target_ratio=0.85):
        self.TARGET_RATIO = target_ratio

    def audit_ontology_pack(self, nodes, edges, pack_name):
        """
        Transitional Bridge: 고농축 지식의 핵심은 관계망의 밀도입니다. 
        노드만 존재하고 엣지가 끊겨 있는 데이터는 고사한 신경망과 같습니다. 
        이 진단 엔진은 수집된 온톨로지 팩의 엣지/노드 비율을 분석하여 정합성을 보증합니다.
        """
        if nodes == 0:
            return {
                "Pack_Name": pack_name,
                "Status": "INVALID_EMPTY_NODE",
                "Action": "HALT_IMPORT: Node count is zero."
            }
            
        ratio = edges / nodes
        status = "ONTOLOGY_STABLE_READY"
        action = "PROCEED_TO_GRAPHIFY_MAPPING"
        
        # 임계 비율 감사
        if ratio < self.TARGET_RATIO:
            status = "CRITICAL_SPARSE_GRAPH_WARNING"
            action = "INVESTIGATE_RELATIONSHIPS: Check for missing edges in raw JSON data before import."
        elif nodes > 1000:
            status = "MEGA_SCALE_ONTOLOGY_DETECTED"
            action = "PARTITION_INTO_TRIBUTARIES: Split into multiple smaller HDS-Gold instances to avoid token blowup."
            
        return {
            "Grounded_Pack_Name": pack_name,
            "Total_Nodes": nodes,
            "Total_Edges": edges,
            "Edge_to_Node_Ratio": round(ratio, 4),
            "Ontology_Audit_Status": status,
            "Governance_Instruction": action
        }
```

---

## 5. [지식 보강 요청서 (Ingestion Request)]
*   **Data Gap**: `korea-tax-law-reference` 및 `biomedical_ontology` 등 12대 핵심 팩의 로컬 이관을 위한 세부 JSON 노드 속성 레코드 및 압축 소스 파일 누락 상태.
*   **Action**: 본 격리 Data 노드를 영구 보존하고, 플랫폼 서비스 차단에 대비하여 사용자가 다운로드 받은 즉시 로컬 `03_External_Data`로 연동 적재하기 위한 인프라 감사를 지속 건의합니다.

---

## 6. [스스로 체크 (Self-Audit)]
1. 대한민국 세법 온톨로지(`korea-tax-law-reference`)가 $104 \text{ Nodes}$ 및 $96 \text{ Edges}$로 규정되어 있을 때, **AlexAIOntologyAuditor**가 진단한 엣지/노드 비율($0.923$)이 로컬 이관에 적합한 공학적 근거는 무엇인가?
2. **3D 모델링 온톨로지(`3d-modeling`)** 데이터셋의 규모가 $1,279 \text{ Nodes}$ 및 $4,805 \text{ Edges}$로 감지되었을 때, 이 대규모 구조망을 단일 마크다운 파일로 HDS-Gold화 하지 않고 **구역 분할(Partition)**을 통해 이식해야 하는 토큰 및 파싱 병목 해결 사유는 무엇인가?
3. MES 데이터와 마찬가지로 외부 온톨로지 팩의 메타 스키마를 로컬 **`01_Inbox` (검역소)**에 보관하고 standard B형 Data 노드로 버저닝 관리해야 하는 IATF 16949 데이터 거버넌스적 장점은 무엇인가?

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[ [AI] mcp-opencrab-functional-blueprint-and-dataset-list]]` : 오픈크랩 기능 복제 청사진
- `[[ [MOC] Global-Dataset-Inventory-Hub]]` : 전역 데이터셋 및 스킬 마스터 그리드
- `[[ [Data] opencrab-workspace-catalog-quarantine]]` : 오픈크랩 작업공간 55대 지식 팩 검역 데이터 노드

---
**[SPO_Graph: AlexAI_Ontology -> data_quarantined (Evidence: [데이터 부재] Section 1)]**
**[HEUNGTOLOGY_INTEGRITY: MAXIMUM_SEALED]**