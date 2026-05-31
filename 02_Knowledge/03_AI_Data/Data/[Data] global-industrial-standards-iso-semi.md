---
lineage:
  dataset_reference: global-industrial-standards-iso-semi
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
measurement:
  confidence_interval:
  - 0.0
  - 0.0
  instrument: Heuristic_Regex_Parser
  precision: '0.0'
  unit: ', S8, E47.1, ISO 9001, 14001 |'
  value: 1
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Data] global-industrial-standards-iso-semi]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for global-industrial-standards-iso-semi
  object_type: Data
  tier: 1
properties:
  core_standards: SEMI S2, S8, E47.1, ISO 9001, 14001
  data_scope: SEMI, ISO, IATF
  measurement_unit: Angstrom
  skill_endpoint: python 03_Skills/antigravity_native/industrial_intel_skill.py
semantic:
  alternative_parents: []
  is_instance_of: '[[ [03_AI_Data] [Concept] global-industrial-standards-iso-semi]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: automated_classification
  object: Data
  predicate: auto_mapped
  subject: global-industrial-standards-iso-semi
  weight: 0.7
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.05
  t_static: 0.8
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Data] Global Industrial Standards Iso Semi

## 1. [Dataset Overview: The Rulebook of Manufacturing]
본 데이터셋은 글로벌 제조 및 공학 시스템의 상호 운용성과 품질을 보장하는 **기술 표준(Technical Standards)** 데이터의 집합체임. Antigravity Intelligence가 옹스트롬($\text{\AA}$) 레벨의 공정을 설계할 때, 물리적 한계치와 안전 규격을 결정론적으로 참조하는 '절대 지휘 지침'으로 작동함.

## 2. [Technical Specifications & Access Matrix]

| Parameter | Specification | Access / Source |
| :--- | :--- | :--- |
| **Data Scope** | SEMI (Semi), ISO (General), IATF (Auto) | `industrial_intel_skill.py` |
| **Core Standards** | SEMI S2, S8, E47.1, ISO 9001, 14001 | [데이터 부재] |
| **Parameters** | Material Purity, Tolerance, Safety Thresholds | [데이터 부재] |
| **Local Skill** | `python 03_Skills/antigravity_native/industrial_intel_skill.py` | [Active_Bridge] |

## 3. [Engineering Application: Standardized Orchestration]
1. **Interface Design**: EUV 칠러와 리소그래피 장비 간의 물리적 인터페이스 표준(SEMI E-Series)을 참조하여 하드웨어 정합성 검증.
2. **Quality Audit**: 공정 산출물이 IATF 16949 등 자동차향 반도체 품질 기준을 충족하는지 수리적으로 판정.
3. **Safety Protocol**: Scrubber 및 가스 캐비닛의 안전 이격 거리와 배기 효율 임계치를 법적 표준에 맞춰 자동 산출.

## 4. [MCP Replacement: Native Execution]
외부 표준 구매 사이트에 의존하기 전, `industrial_intel_skill.py`를 통해 공개된 표준의 초안(Draft) 및 기술 요약본을 전수 크롤링하여 위키에 내재화함. 이를 통해 유료화 장벽을 우회하는 지식 주권을 확보함.

## 5. [Self-Audit Protocol]
1. **Fidelity**: 표준 데이터의 '버전 관리'가 중요한 이유는 무엇인가? (정답: 구형 표준(Legacy)과 신규 표준(Next-gen) 간의 하드웨어 호환성 충돌을 방지하기 위함)
2. **Connectivity**: 이 데이터셋이 [[ [Dataset] korean-legal-precedents-corpus ]]와 어떻게 연결되는가? (정답: 기술 표준 미준수가 법적 과실 판결에 미치는 영향 분석)