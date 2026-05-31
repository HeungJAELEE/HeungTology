---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] stationarity-and-unit-root-test]]'
  last_updated: '2026-05-25T11:06:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Stationarity, random walks, and Augmented Dickey-Fuller tests
  object_type: Algorithm
  tier: 2
properties:
  alternative_hypothesis_gamma: less_than_zero
  autocovariance_lag_dependency: k
  mean_stability: constant
  null_hypothesis_gamma: 0
  unit_root_phi: 1
  variance_stability: finite_and_constant
semantic:
  alternative_parents: []
  expected_queries:
  - 시계열의 정상성이란 무엇이며 AR(1) 모델로 어떻게 검정하는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: statistical_validation
  object: Time_Series_Integrity
  predicate: validates
  subject: '[Finance] stationarity-and-unit-root-test'
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

# 📊 [Concept] 시계열 정상성과 단위근 검정 (Unit Root Test)

## 1. 정상성(Stationarity)의 수학적 조건
퀀트 모델링(특히 공적분 및 ARIMA)을 적용하기 위해 시계열 $Y_t$는 약한 정상성(Weak Stationarity)을 만족해야 합니다.
1. $E[Y_t] = \mu$ (평균이 시간에 따라 일정)
2. $Var(Y_t) = \sigma^2 < \infty$ (분산이 일정)
3. $Cov(Y_t, Y_{t-k}) = \gamma_k$ (자기공분산이 시점 $t$가 아닌 시차 $k$에만 의존)

## 2. 단위근 검정 메커니즘
주가 시계열은 대체로 비정상 랜덤 워크(Random Walk)를 따르며, 이는 자기회귀 AR(1) 모델에서 계수가 1인 단위근(Unit Root)을 가짐을 의미합니다.

$$ Y_t = \phi Y_{t-1} + \epsilon_t $$
양변에서 $Y_{t-1}$을 빼면 차분 방정식이 도출됩니다.
$$ \Delta Y_t = (\phi - 1) Y_{t-1} + \epsilon_t = \gamma Y_{t-1} + \epsilon_t $$

여기서 귀무가설 $H_0 : \gamma = 0$ (즉 $\phi = 1$, 단위근 존재, 비정상성)을 기각하고 대립가설 $H_1 : \gamma < 0$을 채택해야만 통계적 차익거래 모델 진입이 수학적으로 허가됩니다.