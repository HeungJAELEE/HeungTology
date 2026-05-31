---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] realized-volatility-microstructure-noise]]'
  last_updated: '2026-05-25T11:12:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: High-frequency realized volatility and microstructure noise modeling
  object_type: Concept
  tier: 2
properties:
  integrated_variance_iv: integral_0^t sigma_s^2 ds
  noise_term_epsilon: epsilon
  observed_price_p_obs: P_true + epsilon
  realized_volatility_rv_t: sum_{i=1}^M r_{t,i}^2
  sampling_frequency_m: M
semantic:
  alternative_parents: []
  expected_queries:
  - 초고빈도 데이터에서 실현 변동성을 측정할 때 마이크로스트럭처 노이즈가 미치는 영향은 무엇인가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: noise_mitigation
  object: Market_Microstructure_Noise
  predicate: filters
  subject: '[Finance] realized-volatility-microstructure-noise'
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

# 🔊 [Concept] 고주파 실현 변동성(Realized Volatility)과 미시구조 노이즈

## 1. 적분 분산(Integrated Variance)과 실현 변동성
자산 가격의 실시간 내재 분산을 측정하기 위해 퀀트 모델은 1일 단위가 아닌 마이크로초 단위의 수익률 제곱합인 실현 변동성(Realized Volatility, RV)을 계산합니다.
$$ RV_t = \sum_{i=1}^M r_{t,i}^2 $$
이론적으로 샘플링 빈도 $M \rightarrow \infty$ 일 때, $RV_t$는 연속 시간 내재 변동성의 적분인 적분 분산(Integrated Variance, $IV = \int_0^t \sigma_s^2 ds$)으로 완벽히 수렴해야 합니다.

## 2. 마이크로스트럭처 노이즈 (Microstructure Noise)의 발산
그러나 초고빈도(HFT) 영역에서는 틱(Tick) 단위의 띄엄띄엄한 호가 단위(Discreteness)와, 매수/매도 호가를 오가며 체결되는 호가창 바운스(Bid-Ask Bounce) 현상으로 인해 순수 가격에 노이즈 $\epsilon$이 개입합니다.

관측된 로그 가격: $P_{obs} = P_{true} + \epsilon$

이로 인해 초고주파 샘플링을 진행할수록 $RV_t$는 $IV$로 수렴하지 않고 노이즈 분산에 의해 무한대로 발산(Divergence)하는 역설이 발생합니다.
퀀트 시스템은 이를 제거하기 위해 하위 샘플링(Sub-sampling) 기법이나 **실현 커널(Realized Kernel)** 모델을 사용하여 자가상관된 노이즈 오차 항을 상쇄한 뒤 순수한 진성 변동성($IV$)만을 추출하여 알고리즘 입력값으로 라우팅합니다.