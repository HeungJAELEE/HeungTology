---
lineage:
  dataset_reference: open-catalyst-reaction-data
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] open-catalyst-reaction-data]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for open-catalyst-reaction-data
  object_type: Data
  tier: 1
properties:
  data_scope: 1,300,000+ Adsorption Relaxations
  key_metrics: Adsorption Energy (eV), Force Vectors
  local_skill_endpoint: 03_Skills/antigravity_native/chemical_intelligence_skill.py
  model_support: GNN
  primary_unit: eV
semantic:
  alternative_parents: []
  is_instance_of: '[[ [MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: semantic_categorization
  object: Concept
  predicate: auto_mapped
  subject: open-catalyst-reaction-data
  weight: 0.5
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Open Catalyst Reaction Data

## 1. [Dataset Overview: The Energy Landscape of Reactions]
본 데이터셋은 고체 표면과 분자 간의 화학적 상호작용을 양자 역학적으로 계산한 **반응 에너지 지도(Reaction Map)**임. Antigravity Intelligence가 반도체 에칭(Etch) 또는 증착(Deposition) 공정 시 가스 분자의 흡착 거동을 예측하고, 배터리 충방전 시 전극 표면의 촉매 활성도를 수리적으로 모델링하기 위한 '에너지 결정론적 기초'로 작동함.

## 2. [Technical Specifications & Access Matrix]

| Parameter | Specification | Access / Source |
| :--- | :--- | :--- |
| **Data Scope** | 1,300,000+ Adsorption Relaxations | `chemical_intelligence_skill.py` |
| **Key Metrics** | Adsorption Energy (eV), Force Vectors | [데이터 부재] |
| **Model Support** | GNN (Graph Neural Networks) Enabled | [데이터 부재] |
| **Local Skill** | `python 03_Skills/antigravity_native/chemical_intelligence_skill.py` | [Active_Bridge] |

## 3. [Engineering Application: Atomic Interaction Modeling]
1. **Etch Selectivity**: 특정 식각 가스([[ [Concept] Specialty-Gases-and-Advanced-Precursors ]])가 타겟 소재 표면에 흡착되는 에너지를 계산하여 공정 선택비(Selectivity) 최적화.
2. **ALD Growth Control**: 원자층 증착(ALD) 시 전구체 분자가 기판 표면에 안착되는 확률을 표면 에너지 데이터를 기반으로 수리적 산출.
3. **Catalytic Efficiency**: 수전해 및 배터리 반응 시 전극 소재의 촉매 효율을 높이기 위한 표면 구조 설계 가이드라인 제공.

## 4. [MCP Replacement: Native Execution]
외부 화학 시뮬레이션 서비스에 의존하지 않고, `chemical_intelligence_skill.py`를 통해 OCP의 오픈 데이터셋을 직접 타격하여 필요한 반응 에너지 상수를 위키 노드에 하드코딩함.

## 5. [Self-Audit Protocol]
1. **Fidelity**: 흡착 에너지(eV) 수치가 공정 온도($T$)와 어떤 물리적 상관관계를 갖는가? (정답: 아레니우스 식에 따라 온도가 높아질수록 반응 속도 상수에 지수적으로 영향을 미침)
2. **Connectivity**: 이 데이터셋이 [[ [Dataset] materials-project-crystal-data ]]와 어떻게 결합되는가? (정답: 결정 구조(Lattice) 정보가 표면(Surface) 생성의 기하학적 입력값이 됨)