---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] poisson-process-and-jumps]]'
  last_updated: '2026-05-25T11:06:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Poisson processes and stochastic jump dynamics
  object_type: Concept
  tier: 2
properties:
  k: number_of_market_orders
  lambda: average_order_arrival_rate
  mu: drift_coefficient
  sigma: volatility_coefficient
  t: time_interval
  y_minus_one: jump_size_percentage_change
semantic:
  alternative_parents: []
  expected_queries:
  - 시장 미시구조에서 독립적인 주문 도착은 어떤 확률 분포를 따르는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_foundation
  object: Point_Process_Modeling
  predicate: foundations_for
  subject: '[Finance] poisson-process-and-jumps'
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

# 🕒 [Concept] 푸아송 프로세스와 점프 역학 (Poisson Process)

## 1. HFT 주문 도착의 기저 모델
호크스 프로세스의 자기 여기(Self-exciting) 현상을 제거한, 완전히 독립적이고 일정한 강도(Intensity, $\lambda$)로 발생하는 시장 주문 도착을 포착하는 기저 모델이 푸아송 프로세스(Poisson Process)입니다. 

단위 시간 $t$ 동안 시장가 주문(Market Order)이 정확히 $k$번 발생할 확률은 다음과 같이 정의됩니다.

$$ P(N(t) = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!} $$

* $N(t)$: 시점 $0$에서 $t$까지 도착한 주문의 총 횟수
* $\lambda$: 단위 시간당 평균 주문 도착률

## 2. 점프 확산 (Jump-Diffusion) 결합
자산 가격이 브라운 운동만으로 설명 불가능한 급격한 갭(Gap)을 보일 때, 연속적인 브라운 운동 $dW_t$에 불연속적 푸아송 점프 프로세스 $dN_t$를 결합합니다. (예: 머튼의 점프 확산 모델)

$$ \frac{dS_t}{S_t} = \mu dt + \sigma dW_t + (Y - 1) dN_t $$

* $dN_t$: 강도 $\lambda$를 갖는 푸아송 과정 ($dt$ 동안 1일 확률 $\lambda dt$, 0일 확률 $1-\lambda dt$)
* $Y-1$: 점프 발생 시 수익률의 백분율 변화 폭