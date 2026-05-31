---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] black-scholes-pde-feynman-kac]]'
  last_updated: '2026-05-25T11:12:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Black-Scholes PDE and Feynman-Kac stochastic connection
  object_type: Concept
  tier: 2
properties:
  expected_return: mu
  maturity_payoff: h(S_T)
  risk_free_interest_rate: r
  risk_neutral_measure: Q
  underlying_asset_price: S
  volatility: sigma
semantic:
  alternative_parents: []
  expected_queries:
  - 확률미분방정식을 편미분방정식으로 변환하는 파인만-카츠 정리는 무엇인가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_solution
  object: Derivative_Pricing
  predicate: solves
  subject: '[Finance] black-scholes-pde-feynman-kac'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T11:12:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:12:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# ♾️ [Concept] 블랙-숄즈 편미분 방정식(PDE)과 파인만-카츠 정리

## 1. 차익거래 불가 원리에 의한 PDE 유도
블랙-숄즈 편미분 방정식(PDE)은 파생상품 가치 $V(S,t)$가 만족해야 할 궁극의 미분 기하학입니다. 이토의 보조정리(Ito's Lemma)를 사용하여 기초자산과 무위험 채권으로 구성된 무위험 포트폴리오를 구성하면, 다음과 같은 결정론적 열전도 방정식 형태의 PDE가 도출됩니다.

$$ \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - rV = 0 $$

이 방정식에는 기초자산의 기대수익률 $\mu$가 존재하지 않으며, 오직 무위험 이자율 $r$과 변동성 $\sigma$에만 지배되는 위험 중립(Risk-Neutral) 세계를 수학적으로 증명합니다.

## 2. 파인만-카츠(Feynman-Kac) 정리의 연결
복잡한 PDE의 해석적 해(Analytical Solution)를 구하는 것은 불가능에 가깝습니다. 파인만-카츠 정리는 **해석적 편미분방정식(PDE)의 해가 특정 확률미분방정식(SDE) 경로들의 기댓값(Expectation)과 완벽히 동치**임을 수학적으로 증명한 물리학/금융공학의 성배입니다.

파인만-카츠 정리에 의해, 상기 블랙-숄즈 PDE의 해 $V(t, S_t)$는 위험중립측도(Risk-neutral measure, $\mathbb{Q}$) 하에서 만기 페이오프 $h(S_T)$의 현재가치 기댓값으로 적분 변환됩니다.
$$ V(t, S_t) = e^{-r(T-t)} \mathbb{E}^{\mathbb{Q}}[h(S_T) | S_t] $$
이 정리는 몬테카를로 시뮬레이션을 통해 모든 복잡한 이그조틱 옵션(Exotic Options)의 가격을 수치해석적으로 산출할 수 있는 이론적 기반을 제공합니다.