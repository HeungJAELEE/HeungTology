---
metadata:
  date: "2026-05-17"
  id: "[[[Battery] W13_correlation-vs-causality-physics]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "02_Battery"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "industrial-causal-inference-framework-v2026"
  original_author: "Antigravity Vault / Decision-Science-Group"
  original_hash: "050614752c2c37f9281755717763774e161ca7cd318182695888a4459f09385c"
object:
  object_type: "Concept"
  tier: 1
  description: '산업 공정의 허위 상관(Spurious Correlation)을 소거하고 실제 제어 레버를 식별하기 위한 인과 추론 메커니즘 및 SCM(Structural Causal Model) 가이드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 02_Battery]]"
  alternative_parents: []
spo_graph:
  - subject: "Causal Impact"
    predicate: "calculated_via"
    object: "P(Y | do(X))"
    evidence_coordinate: "[Ref: Pearl_SCM] Section 3.2"
    evidence_hash: "050614752c2c"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
  - subject: "Control Precision Gain"
    predicate: "measured_value"
    object: "Delta sigma > 0.15"
    evidence_coordinate: "[Ref: Fidelity_Comparison] Table 3"
    evidence_hash: "050614752c2c"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---



# [Battery] W13_correlation-vs-causality-physics

## 1. 운영상 필요성 (Operational Necessity)
상관관계(Correlation)는 변수 간의 동시 발생을 나타내는 통계적 지표인 반면, 인과관계(Causality)는 독립 변수의 변화가 종속 변수의 물리적 상태를 변환시키는 기전(Mechanism)을 의미합니다. 산업 공정에서 상관관계에 의존한 제어는 허위 상관을 유발하여 공정 최적화 실패의 원인이 됩니다. 인과 추론은 실제 제어 레버(Lever)를 식별하기 위한 필수 절차입니다.

## 2. 추론 명세 매트릭스 (Inference Matrix)

| 구분 | 상관관계 (Correlation) | 인과관계 (Causality) | 공학적 당위성 |
|:---|:---:|:---:|:---|
| **수학적 기초** | $P(Y \mid X)$ | **$P(Y \mid do(X))$** | 관찰 vs 개입의 차이 |
| **시간적 순서** | 무관 | **$X \prec Y$** | 원인의 물리적 선행성 필수 |
| **교란 통제** | 허용됨 | **의무적 (Mandatory)** | 제3 변수에 의한 왜곡 제거 |
| **의사결정 로직** | 단순 예측/힌트 | **제어/최적화** | 실제 제어 루프 반영 가능성 |

## 3. 핵심 프레임워크 (SCM & Do-calculus)
- **Backdoor Adjustment**: 변수 $X$와 $Y$ 사이의 허위 상관을 유발하는 교란 변수 $Z$의 영향을 수학적으로 격리하여 순수 인과 효과를 산출합니다.
- **Bradford Hill 기준**: 통계적 연관성을 물리적 인과성으로 격상하기 위해 일관성, 물리적 개연성, 시간적 선후성을 전수 검증합니다.

## 4. [Skill] Causal Root Cause Analyzer
DoWhy 라이브러리 기반의 인과 모델을 정의하고, Backdoor Adjustment를 통해 공정 변수의 실제 기여도를 추정하여 'VALID_LEVER' 여부를 판정하는 로직을 가동합니다.

## 5. 자가 검증 프로토콜 (Self-Audit)
1. **개입 실험**: 점도와 두께 간 상관관계를 인과관계로 확정하기 위한 개입 실험 데이터의 확보 여부.
2. **역인과성 탐지**: 시계열 데이터의 선후성을 검증하여 결과가 원인으로 오인되는 상황 방지.
3. **용량-반응 관계**: 독립 변수의 변화량에 따른 종속 변수의 비례적 반응(Dose-Response) 검증.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] agentic-workflows-2026-specification]]
- [[[Data] industrial-causal-inference-framework-v2026]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**
