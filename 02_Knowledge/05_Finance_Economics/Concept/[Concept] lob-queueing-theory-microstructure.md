---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] lob-queueing-theory-microstructure]]'
  last_updated: '2026-05-25T11:09:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Queueing theory (M/M/1) applied to Limit Order Book dynamics
  object_type: Concept
  tier: 2
properties:
  arrival_rate: lambda
  average_queue_length: L
  average_waiting_time: W
  orders_in_front: N_front
  service_rate: mu
  time_horizon: tau
  utilization_factor: rho
semantic:
  alternative_parents: []
  expected_queries:
  - 대기 행렬 이론을 활용하여 지정가 주문의 체결 확률을 어떻게 모델링하는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_modeling
  object: Order_Execution_Probability
  predicate: models
  subject: '[Finance] lob-queueing-theory-microstructure'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T11:09:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:09:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# ⏳ [Concept] 지정가 주문장(LOB)의 대기 행렬 이론 (Queueing Theory)

## 1. M/M/1 대기 행렬 기반 LOB 모델링
고빈도 매매(HFT)의 마켓 메이킹 알고리즘에서 가장 중요한 변수는 자신이 호가창(Order Book)에 깔아놓은 지정가 주문이 "언제 체결될 것인가(Time to Execution)"입니다. 이를 수학적으로 풀기 위해 통신공학의 **대기 행렬 이론(Queueing Theory)**이 차용됩니다.

호가창의 특정 가격대 $P$를 하나의 서버(Server)로 간주하는 $M/M/1$ 대기 행렬에서:
* **도착률 (Arrival Rate, $\lambda$)**: 해당 가격대로 밀려 들어오는 타인의 신규 지정가 주문 속도 (푸아송 분포 가정).
* **서비스율 (Service Rate, $\mu$)**: 시장가 주문(Market Order)에 의해 기존 대기 주문이 체결되거나 캔슬되어 사라지는 속도.

## 2. 리틀의 법칙 (Little's Law)과 체결 확률
시스템이 안정 상태($\rho = \lambda / \mu < 1$)일 때, 주문장에 쌓여 있는 평균 호가 잔량 $L$과 주문 체결까지의 평균 대기 시간 $W$는 다음의 법칙을 따릅니다.

$$ L = \lambda W $$

HFT 알고리즘은 자신이 주문을 넣었을 때 앞에 대기 중인 주문량 $N_{front}$를 파악하고, 조건부 대기 시간 확률분포 $f_W(t)$를 적분하여 주어진 시간 $\tau$ 내에 주문이 체결될 확률을 실시간으로 추산합니다.

$$ P(\text{Execution before } \tau) = \int_{0}^{\tau} \frac{\mu^{N_{front}} t^{N_{front}-1}}{(N_{front}-1)!} e^{-\mu t} dt $$

체결 확률이 극도로 낮아지거나 $\lambda$가 $\mu$를 역전하는 호가 불균형(OIB 폭증)이 감지되면 알고리즘은 대기열을 취소(Cancel)하고 상위 호가로 도망(Flee)칩니다. (초단타 데스크의 $\lambda, \mu$ 임계치 실측 데이터는 **[데이터 부재]**)