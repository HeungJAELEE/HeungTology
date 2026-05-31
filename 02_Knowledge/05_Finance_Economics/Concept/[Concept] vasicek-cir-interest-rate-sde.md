---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] vasicek-cir-interest-rate-sde]]'
  last_updated: '2026-05-25T11:12:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Vasicek and CIR stochastic term structure models for interest rates
  object_type: Concept
  tier: 2
properties:
  feller_condition: 2ab > sigma^2
  interest_rate_volatility: sigma
  long_term_mean_level: b
  speed_of_reversion: a
semantic:
  alternative_parents: []
  expected_queries:
  - 바시첵 모델과 CIR 모델의 수학적 차이점과 이자율 기간 구조 모델링 방법은 무엇인가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_modeling
  object: Term_Structure_of_Interest_Rates
  predicate: models
  subject: '[Finance] vasicek-cir-interest-rate-sde'
  weight: 1.0
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

# 📉 [Concept] 바시첵(Vasicek) 및 CIR 이자율 SDE 모델링

단기 무위험 이자율 $r_t$는 주식과 달리 무한히 상승하지 않고 특정 거시 경제의 장기 균형으로 회귀(Mean Reversion)하는 성질을 지닙니다. 채권 퀀트 데스크는 이자율 기간구조(Term Structure)를 모델링하기 위해 다음의 SDE를 사용합니다.

## 1. 바시첵 (Vasicek) 모델
가장 고전적인 이자율 모델로, 이자율이 오른스타인-울렌벡(O-U) 프로세스를 따른다고 가정합니다.
$$ dr_t = a(b - r_t)dt + \sigma dW_t $$
* $a$: 평균 회귀 속도 (Speed of reversion)
* $b$: 장기 평균 이자율 (Long-term mean level)
* $\sigma$: 이자율 변동성

바시첵 모델은 해를 구하기 쉽고 정규 분포를 따른다는 장점이 있으나, 변동성 $\sigma$가 이자율 수준과 무관하여 **이자율이 음수(-)로 떨어질 수 있는** 수학적 한계를 지닙니다.

## 2. CIR (Cox-Ingersoll-Ross) 모델
바시첵 모델의 음수 이자율 문제를 해결하기 위해, 이자율이 낮아질수록 변동성도 감소하도록 브라운 운동 항에 $\sqrt{r_t}$를 곱한 모델입니다.
$$ dr_t = a(b - r_t)dt + \sigma \sqrt{r_t} dW_t $$

펠러 조건(Feller Condition, $2ab > \sigma^2$)을 만족할 경우 이자율 $r_t$는 0에 닿을 수는 있으나 결코 음수로 떨어지지 않는 절대 양수(Strictly Positive) 특성을 가지며, 카이제곱(Chi-squared) 분포를 통해 무이표채(Zero-coupon bond)의 만기 $T$ 가격 $P(t,T)$를 다음과 같이 결정론적으로 도출해냅니다.
$$ P(t,T) = A(t,T)e^{-B(t,T)r_t} $$
(구체적인 거시 금리 $a, b, \sigma$ 실측 파라미터는 **[데이터 부재]**)