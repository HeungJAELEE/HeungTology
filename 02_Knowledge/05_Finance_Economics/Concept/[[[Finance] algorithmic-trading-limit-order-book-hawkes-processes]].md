---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-limit-order-book-hawkes-processes]]'
  last_updated: '2026-05-25T19:50:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 호가창에서 누군가 매수 주문을 터뜨렸을 때, 이 '단 하나의 사건'이 어떻게 수천 개의 다른 HFT 봇들을 자극하여 군집
    현상(Clustering)과 연쇄 폭발을 일으키는지를 미시적으로 모델링하는 자기-흥분(Self-exciting) 점프 방정식인 호크스 프로세스(Hawkes
    Process)
  object_type: Algorithm
  tier: 2
properties:
  alpha: excitation_jump_size
  beta: decay_rate
  lambda_t: conditional_intensity
  memory_kernel: sum_of_past_shocks
  mu: baseline_intensity
semantic:
  alternative_parents: []
  expected_queries:
  - 주문이 단순히 랜덤하게(Poisson) 들어오지 않고, 왜 시장가 매수가 하나 터지면 1밀리초 뒤에 미친 듯이 수백 개의 매수/매도 주문이
    연쇄 폭발(Clustering)하는가?
  - 호크스 프로세스(Hawkes Process)의 수학적 구조에서 베이스라인 강도(Base Intensity)와 여진(Excitation) 함수는
    어떻게 호가창의 메모리 효과(Memory Effect)를 구현하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: phenomenon_modeling
  object: Order_Flow_Clustering
  predicate: captures
  subject: '[Finance] algorithmic-trading-limit-order-book-hawkes-processes'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T19:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T19:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-limit-order-book-hawkes-processes]]

## 1. 개요 (Overview)
기존의 퀀트 이론들은 금융 시장의 사건(주문 체결, 파산 등)이 포아송 분포(Poisson Process)를 따른다고 가정했습니다. 포아송 분포의 핵심은 '독립성(Memoryless)'입니다. 동전을 던져서 앞면이 나왔다고 다음 판에 앞면이 나올 확률이 변하지 않는 것처럼, 앞사람이 매수 주문을 날렸다고 뒷사람의 행동에 영향을 주지 않는다는 가정입니다.
하지만 실제 HFT 호가창(Limit Order Book)은 절대 포아송이 아닙니다. 누군가 1호가 매도 잔량을 다 갉아먹는 거대한 시장가 매수(Market Buy)를 날리면, 그 순간 잠들어 있던 수천 개의 알고리즘 봇들이 이 시그널에 놀라(Excitation) 미친 듯이 매수 주문을 따라 넣거나 취소(Cancel)를 갈깁니다. **"하나의 사건이 다음 사건을 폭발적으로 유발한다"**는 이 군집 현상(Clustering)을 완벽하게 맵핑한 것이 지진학(Seismology)에서 건너온 **호크스 프로세스(Hawkes Process)**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\lambda(t)$ | Conditional Intensity | Probability of order at $t$| Changes every microsecond| [데이터 부재] |
| $\mu$ | Baseline Intensity | Background noise rate | Constant arrival rate | [데이터 부재] |
| $\alpha$ | Excitation Jump Size | Magnitude of shock | How much intensity rises | [데이터 부재] |
| $\beta$ | Decay Rate | Speed of forgetting | Pulls intensity back to $\mu$| [데이터 부재] |
| $\int_0^t \dots$ | Memory Kernel | Sum of past shocks | Captures event history | [데이터 부재] |

## 3. 자기-흥분 방정식 (Self-Exciting Equation)
호크스 프로세스의 수학적 핵심은 "사건의 발생 강도($\lambda(t)$) 자체가 과거에 발생한 사건들의 역사에 종속된다"는 것입니다.
$$ \lambda(t) = \mu + \sum_{t_i < t} \alpha e^{-\beta (t - t_i)} $$

1. **베이스라인 강도 ($\mu$)**: 아무 일도 일어나지 않는 평화로운 시장에서 개미들이 산발적으로 던지는 배경 노이즈(포아송 강도)입니다.
2. **흥분 점프 ($\alpha$)**: 시각 $t_i$에 누군가 거대한 지정가 주문을 취소(Cancel)하는 충격적인 사건이 터졌습니다. 이 순간, 시장의 주문 발생 강도 $\lambda$는 즉시 $\alpha$만큼 팍! 튀어 오릅니다(여진의 시작).
3. **망각 곡선 ($e^{-\beta (t - t_i)}$)**: 시간이 지남에 따라 사람들은 방금 전의 충격을 서서히 잊어버립니다. $\beta$는 이 기억이 소멸하는 속도(지수 감소)입니다. 

## 4. HFT 마이크로 프라이스 (Micro-price) 혁명
전통적인 중간 가격(Mid-price)은 매수 1호가와 매도 1호가의 단순 평균일 뿐입니다. 하지만 HFT 퀀트들은 호크스 프로세스를 이용해 호가창 양쪽에 쏟아지는 매수와 매도의 **진짜 발생 강도 차이($\lambda_{\text{buy}} - \lambda_{\text{sell}}$)**를 실시간으로 스캔합니다.
- 매수 쪽 호크스 강도($\lambda_{\text{buy}}$)가 자기-흥분을 일으켜 수식적으로 미친 듯이 팽창하고 있다면, 비록 현재 1호가 가격이 그대로일지라도 **1밀리초 뒤에는 100% 확률로 가격이 위로 폭발**합니다.
- 호크스 기반 알고리즘은 인간이 차트를 보고 "거래량이 터졌네"라고 생각하기도 전인 여진(Excitation)의 극초기 단계(지진파 P파 도달 시점)에서 이미 지정가 주문을 밀어 넣고 체결을 확정 짓는 극단적인 마이크로 알파(Micro Alpha)를 창출합니다.

🧠 **AI의 사고방식:**
금융 시장은 동전 던지기(포아송)가 아니라, **전염병(Epidemic)**과 같습니다. 첫 번째 기침 환자(시장가 매수)가 발생하면, 그 환자가 주변 사람들을 감염시키고($\alpha$), 감염된 사람들이 또 다른 사람들을 감염시키며 주문 폭발(Clustering)을 일으킵니다. 호크스 프로세스는 이 전염병의 '기초 감염 재생산 지수'를 계산하여, 방금 전 터진 주문 한 개가 단순한 감기인지, 아니면 앞으로 1초 동안 호가창 전체를 초토화시킬 좀비 바이러스의 시작인지를 미분방정식으로 식별해 내는 호가창의 질병관리본부(CDC)입니다.