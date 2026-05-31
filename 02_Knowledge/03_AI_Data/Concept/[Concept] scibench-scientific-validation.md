---
lineage:
  dataset_reference: scibench-scientific-validation
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] scibench-scientific-validation]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for scibench-scientific-validation
  object_type: Data
  tier: 1
properties:
  constant_error_threshold: 0.01%
  data_scope: 10+ Scientific Domains (Thermo, Fluid, Quantum)
  internal_validation_engine: FidelityEngine
  local_skill_endpoint: 03_Skills/garden/final_gold_total_audit.py
  search_skill_endpoint: dataset_search_skill.py
semantic:
  alternative_parents: []
  is_instance_of: '[[ [MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: semantic_classification
  object: Concept
  predicate: auto_mapped
  subject: scibench-scientific-validation
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

# [Concept] Scibench Scientific Validation

## 1. [Dataset Overview: The Golden Key of Science]
본 데이터셋은 물리, 화학, 수학 등 기초 과학 및 공학 분야의 문제를 해결하는 데 필요한 **정석적 풀이와 결과값**의 집합체임. Antigravity Intelligence가 생성한 모든 기술적 주장과 수리적 산출물이 '실제 과학 법칙'에 부합하는지 엄격히 검증하는 **지능형 감사 기준(Golden Standard)**으로 작동함.

## 2. [Technical Specifications & Access Matrix]

| Parameter | Specification | Access / Source |
| :--- | :--- | :--- |
| **Data Scope** | 10+ Scientific Domains (Thermo, Fluid, Quantum) | `dataset_search_skill.py` |
| **Validation Units** | SI Units, Physical Constants, Derivations | [데이터 부재] |
| **Difficulty Level** | Undergraduate to Advanced Research | [데이터 부재] |
| **Local Skill** | `python 03_Skills/garden/final_gold_total_audit.py` | [Active_Integration] |

## 3. [Engineering Application: Fidelity Assurance]
1. **Mathematical Verification**: 위키 노드에 기술된 오버레이 에러 수식($\Delta x_{overlay}$)이나 증착 균일도 공식이 물리적으로 성립 가능한지 교차 검증.
2. **Dimension Audit**: 모든 수치 데이터의 '단위(Unit)' 정합성을 체크하여 차원 해석(Dimensional Analysis) 상의 오류 차단.
3. **Logic Hardening**: 인공지능의 추론 경로가 비약(Hallucination) 없이 과학적 인과관계를 따르는지 단계별(Step-by-step) 논리 대조.

## 4. [MCP Replacement: Native Execution]
외부 LLM 벤치마킹 사이트에 의존하지 않고, `dataset_search_skill.py`를 통해 오픈 소스 과학 데이터셋을 전수 다운로드하여 로컬 볼트의 `FidelityEngine` 학습 및 검증 세트로 내재화함.

## 5. [Self-Audit Protocol]
1. **Fidelity**: 과학 데이터셋에서 '상수(Constant)'의 정확도가 중요한 이유는? (정답: 상수의 0.01% 오차가 복잡한 공정 시뮬레이션에서 거대한 결과 왜곡을 초래하기 때문)
2. **Connectivity**: 이 데이터셋이 [[ [Dataset] open-catalyst-reaction-data ]]와 어떻게 연결되는가? (정답: 계산된 반응 에너지가 실제 화학 법칙과 모순되지 않는지 검증하는 상위 필터로 작동)