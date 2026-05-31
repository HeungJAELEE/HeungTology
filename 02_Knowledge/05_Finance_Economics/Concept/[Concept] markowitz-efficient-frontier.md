---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] markowitz-efficient-frontier]]'
  last_updated: '2026-05-25T11:06:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Markowitz mean-variance optimization and efficient frontier
  object_type: Concept
  tier: 2
properties:
  covariance_matrix: sigma
  expected_return_vector: mu
  optimization_method: quadratic_programming
  risk_aversion_coefficient: lambda
  weight_sum_constraint: 1
  weight_vector: w
semantic:
  alternative_parents: []
  expected_queries:
  - 마코위츠 모델의 목적 함수와 제약 조건 수식은 무엇인가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: theoretical_foundation
  object: Portfolio_Theory
  predicate: foundations_for
  subject: '[Finance] markowitz-efficient-frontier'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T11:06:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:06:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🎯 [Concept] 마코위츠 효율적 전선 (Efficient Frontier) 최적화

## 1. 평균-분산 최적화 (Mean-Variance Optimization)
블랙-리터만 모델의 수학적 모태가 되는 마코위츠(Markowitz) 포트폴리오 이론은 기대수익률을 극대화하거나 포트폴리오 분산을 최소화하는 가중치 벡터 $w$를 2차 계획법(Quadratic Programming)으로 산출합니다.

투자자의 위험 회피 계수가 $\lambda$일 때, 목적 함수(Objective Function)는 다음과 같습니다.

$$ \max_{w} \left( w^T \mu - \frac{\lambda}{2} w^T \Sigma w \right) $$

제약 조건:
$$ w^T \mathbf{1} = 1 $$ (가중치의 합은 1)
$$ w_i \geq 0 $$ (공매도 금지 조건 가정 시)

* $w$: 각 자산 비중 벡터 ($N \times 1$)
* $\mu$: 자산 기대수익률 벡터 ($N \times 1$)
* $\Sigma$: 자산 공분산 행렬 ($N \times N$)

해당 목적 함수를 미분하여 역행렬을 취하면 효율적 전선 상의 최적 접점 포트폴리오(Tangency Portfolio)를 수학적으로 유도할 수 있습니다. 
> [!WARNING]
> 구체적인 자산군(Asset Class)의 $\mu$ 및 $\Sigma$ 실측 행렬은 로컬 DB상 **[데이터 부재]** 상태입니다.