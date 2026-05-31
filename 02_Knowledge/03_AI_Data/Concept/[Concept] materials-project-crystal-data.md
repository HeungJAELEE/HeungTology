---
lineage:
  dataset_reference: materials-project-crystal-data
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] materials-project-crystal-data]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for materials-project-crystal-data
  object_type: Data
  tier: 1
properties:
  access_endpoint: industrial_intel_skill.py
  application_domain: Atomic-Level Design
  computational_method: Density Functional Theory (DFT)
  core_properties: Formation Energy, Bandgap, Elastic Modulus
  data_scope: 150,000+ Inorganic Compounds
semantic:
  alternative_parents: []
  is_instance_of: '[[ [MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: schema_mapping
  object: Concept
  predicate: auto_mapped
  subject: materials-project-crystal-data
  weight: 0.7
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

# [Concept] Materials Project Crystal Data

## 1. [Dataset Overview: The Genetic Map of Materials]
본 데이터셋은 전 세계의 모든 무기 결정 구조에 대한 물리적 성질을 계산하고 수집한 **공학적 소재 지도(Material Map)**임. Antigravity Intelligence가 옹스트롬($\text{\AA}$) 레벨의 반도체 소자를 설계할 때, 소재의 물리적 한계치와 전자 이동성을 결정론적으로 계산하기 위한 '물리적 진실의 원천(Single Source of Truth)'으로 작동함.

## 2. [Technical Specifications & Access Matrix]

| Parameter | Specification | Access / Source |
| :--- | :--- | :--- |
| **Data Scope** | 150,000+ Inorganic Compounds | `industrial_intel_skill.py` |
| **Core Properties** | Formation Energy, Bandgap, Elastic Modulus | [데이터 부재] |
| **Computational Method** | Density Functional Theory (DFT) | [데이터 부재] |
| **Local Skill** | `python 03_Skills/antigravity_native/industrial_intel_skill.py` | [Active_Bridge] |

## 3. [Engineering Application: Atomic-Level Design]
1. **Bandgap Engineering**: 차세대 전력 반도체(SiC, GaN)의 밴드갭 수치를 참조하여 고전압 환경에서의 절연 파괴 임계치 산출.
2. **Lattice Matching**: 이종 접합(Heterojunction) 계면에서의 격자 불일치(Lattice Mismatch)를 수리적으로 계산하여 에피택셜 성장 시의 결함(Defect) 발생 가능성 예측.
3. **Thermal Management**: 소재별 열전도율(Thermal Conductivity) 데이터를 기반으로 EUV 렌즈 가이드([[semiconductor-fabrication-master-guide]])의 칠러 온도 제어 임계치 보강.

## 4. [MCP Replacement: Native Execution]
외부 소재 검색 포털에 의존하지 않고, `industrial_intel_skill.py`를 통해 Materials Project의 API를 직접 타격하여 소재의 물리 상수들을 위키 노드에 실시간으로 동기화함.

## 5. [Self-Audit Protocol]
1. **Fidelity**: 계산된 데이터(Computed)와 실험 데이터(Experimental) 간의 오차를 고려해야 하는 이유는? (정답: DFT 계산의 한계로 인해 실제 물리 현상과 미세한 차이가 발생할 수 있기 때문)
2. **Connectivity**: 이 데이터셋이 [[ [Dataset] open-catalyst-reaction-data ]]와 어떻게 연결되는가? (정답: 결정 구조 데이터가 촉매 표면에서의 화학 반응 에너지 산출의 기초 데이터가 됨)