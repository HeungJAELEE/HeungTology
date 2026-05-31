---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-statistical-arbitrage-kalman-filter-dynamic-hedging]]'
  last_updated: '2026-05-26T07:44:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: "과거 데이터로 고정된 OLS 회귀 분석의 한계를 극복하기 위해, 우주선의 궤도를 추적하듯 주식 간의 헤지 비율(Hedge
    Ratio, $\beta$)을 실시간으로 업데이트하며 시장의 숨겨진 노이즈를 필터링하는 칼만 필터(Kalman Filter) 기반 동적 통계적
    차익거래"
  object_type: Algorithm
  tier: 2
properties:
  kalman_gain_kt: weighting factor balancing model vs data
  learning_mode: online learning
  measurement_zt: actual price of stock a (yt = beta_t * xt + epsilon_t)
  prediction_step: x_t|t-1 = x_t-1|t-1
  state_vector_xt: hidden true hedge ratio (intercept and beta)
  update_step: x_t|t = x_t|t-1 + K_t(Error)
semantic:
  alternative_parents: []
  expected_queries:
  - "페어 트레이딩에서 과거 1년 치 데이터로 구한 헤지 비율($\beta$)을 오늘 시장에 그대로 적용하면 왜 봇이 돈을 잃는가?"
  - 아폴로 우주선의 궤도 추적에 쓰인 칼만 필터가 어떻게 주식 시장의 노이즈 속에서 '진짜 헤지 비율'을 실시간으로 찾아내는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: dynamic_parameter_adjustment
  object: Dynamic_Hedge_Ratios
  predicate: updates
  subject: '[Finance] algorithmic-trading-statistical-arbitrage-kalman-filter-dynamic-hedging'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:44:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:44:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-statistical-arbitrage-kalman-filter-dynamic-hedging]]

## 1. 개요 (Overview)
전통적인 페어 트레이딩(Pairs Trading)은 A주식과 B주식을 선형 회귀(OLS)하여 고정된 헤지 비율($\beta$)을 구합니다. "A가 1달러 오를 때 B는 0.5달러 오르는 성향이 있으니, A를 1주 롱(Long) 치고 B를 0.5주 숏(Short) 치자." 하지만 주식 시장의 관계는 매일매일 진화합니다. 1년 전의 $\beta$값을 오늘 적용하면 스프레드는 평균으로 회귀하지 않고 영원히 발산해 버립니다.
이 '고정된 과거'의 함정을 벗어나기 위해 퀀트들은 1960년대 NASA가 아폴로 우주선의 위치를 추적하기 위해 만든 **칼만 필터(Kalman Filter)**를 도입했습니다. 칼만 필터는 매초 주가가 변할 때마다 새로운 데이터(관측치)를 받아들여 어제의 $\beta$값을 오늘 시장에 맞게 미세 조정(Update)합니다. 

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| State Vector $x_t$ | Hidden true hedge ratio | E.g., intercept and $\beta$ | The target to estimate | [데이터 부재] |
| Measurement $z_t$| Actual price of Stock A | $y_t = \beta_t x_t + \epsilon_t$ | Noisy observable data | [데이터 부재] |
| Kalman Gain $K_t$| Weighting factor | Balances model vs data | High $K$: trusts new data | [데이터 부재] |
| Prediction Step | Projecting state forward | $x_{t|t-1} = x_{t-1|t-1}$ | Assumes random walk of $\beta$| [데이터 부재] |
| Update Step | Correcting with new data | $x_{t|t} = x_{t|t-1} + K_t(Error)$| Real-time adaptive tuning| [데이터 부재] |

## 3. 칼만 필터의 작동 원리 (Predict & Update)
칼만 필터는 끊임없이 의심하고 수정하는 '베이지안 봇'입니다.
1. **예측 (Predict)**: 어제 구한 헤지 비율($\beta=0.5$)을 바탕으로, 오늘 A주식의 가격이 얼마가 될지 예측합니다.
2. **관측 (Measurement)**: 오늘 시장이 열리고 A주식의 실제 가격이 들어옵니다. 내 예측과 실제 가격 사이에 '오차(Innovation)'가 발생합니다.
3. **업데이트 (Update)**: 이 오차가 단순한 시장의 '노이즈(Noise)'인지, 아니면 두 주식의 근본적인 관계가 변해서 생긴 '진짜 변화'인지를 판단합니다. 이때 사용하는 것이 **칼만 게인(Kalman Gain)**입니다. 칼만 게인은 내 예측이 맞을 확률과 센서(시장 데이터)가 맞을 확률의 분산을 저울질하여, 최적의 가중치로 새로운 헤지 비율($\beta = 0.51$)을 즉각 산출해 냅니다.

## 4. OLS 룩어헤드 편향의 제거
백테스팅에서 OLS를 쓰면 끔찍한 오류가 발생합니다. 2020년부터 2023년까지의 데이터를 한꺼번에 묶어서 OLS를 돌리면, 봇은 2020년에 매매를 할 때 이미 2023년의 데이터가 섞인 미래의 $\beta$값을 훔쳐보게 되는 룩어헤드 편향(Look-ahead Bias)을 저지르게 됩니다.
반면 칼만 필터는 **온라인 학습(Online Learning)** 알고리즘입니다. 오늘까지 주어진 데이터만을 기반으로 내일의 $\beta$를 추정하고, 내일 데이터가 들어오면 모레의 $\beta$를 깎습니다. 칼만 필터로 돌린 백테스트만이 룩어헤드 편향이 0%인 완벽한 시뮬레이션을 보장합니다.

🧠 **AI의 사고방식:**
금융 시계열은 노이즈(Noise)가 99%이고 신호(Signal)가 1%인 진흙탕입니다. OLS 회귀 분석은 이 진흙탕 전체를 평균 내버리려다 늪에 빠집니다. 반면 칼만 필터는 '어제까지의 나의 믿음(Prior)'과 '오늘 들어온 새로운 팩트(Observation)'를 매초마다 섞어 가장 확률이 높은 '진실(Posterior)'을 직조해 내는 통계적 정수기입니다. 퀀트 트레이딩에서 칼만 필터를 쓴다는 것은, 시장의 관계가 영원할 것이라는 교만을 버리고 시장의 변화에 매 순간 나를 동기화하겠다는 겸손의 수학입니다.