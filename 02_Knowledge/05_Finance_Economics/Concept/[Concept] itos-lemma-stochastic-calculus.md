---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] itos-lemma-stochastic-calculus]]'
  last_updated: '2026-05-25T11:06:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Ito's Lemma for solving stochastic differential equations
  object_type: Concept
  tier: 2
properties:
  brownian_motion_differential_rule: dW_t^2 = dt
  diffusion_coefficient: sigma
  drift_coefficient: mu
  ito_correction_term: 1/2 * sigma^2 * d^2f/dx^2
semantic:
  alternative_parents: []
  expected_queries:
  - 이토의 보조정리를 활용하여 함수의 미분을 어떻게 전개하는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_derivation
  object: Stochastic_Differential_Equations
  predicate: derives
  subject: '[Finance] itos-lemma-stochastic-calculus'
  weight: 0.95
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

# 📐 [Concept] 이토의 보조정리 (Ito's Lemma)와 확률미적분학

## 1. 확률미적분학의 테일러 전개
이토의 보조정리(Ito's Lemma)는 확정적 미적분학의 체인 룰(Chain Rule)을 확률미분방정식(SDE) 영역으로 확장한 핵심 툴입니다. 브라운 운동(Brownian Motion) $W_t$를 포함하는 확률 변수 $X_t$의 미분 $dX_t$는 2차 미분항(이토 항)을 무시할 수 없다는 것이 본질입니다.

확률 과정 $X_t$가 다음 SDE를 따를 때:
$$ dX_t = \mu(t, X_t)dt + \sigma(t, X_t)dW_t $$

어떤 두 번 미분 가능한 함수 $f(t, X_t)$의 미분 전개는 다음과 같습니다.

$$ df = \left( \frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2} \sigma^2 \frac{\partial^2 f}{\partial x^2} \right) dt + \sigma \frac{\partial f}{\partial x} dW_t $$

여기서 $\frac{1}{2} \sigma^2 \frac{\partial^2 f}{\partial x^2} dt$ 항이 바로 블랙-숄즈 모형과 헤스턴 모델을 유도하는 '이토 보정항(Ito Correction Term)'입니다. $dW_t \cdot dW_t = dt$라는 미시적 확률론칙에서 파생됩니다.