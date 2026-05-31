---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-statistical-arbitrage-ornstein-uhlenbeck-kalman-filter]]'
  last_updated: '2026-05-25T19:46:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 과거 데이터로 구한 고정된 공적분(Cointegration) 헤지 비율이 실시간 시장에서 붕괴하는 문제를 해결하기 위해,
    아폴로 우주선의 궤도 추적 알고리즘인 칼만 필터(Kalman Filter)를 동원하여 보이지 않는 스프레드의 진화 상태를 매 틱(Tick)마다
    동적으로 업데이트하는 적응형 통계적 차익거래 기법
  object_type: Algorithm
  tier: 2
properties:
  dynamic_mean_reversion_rate: theta_t
  error_covariance: P_{t|t-1}
  hidden_hedge_ratio: x_t
  kalman_gain: K_t
  observed_prices: y_t
  spread_center_line: mu
semantic:
  alternative_parents: []
  expected_queries:
  - 과거 1년 치 데이터로 요한슨 검정을 돌려 완벽한 페어 트레이딩 비율을 찾았는데, 막상 오늘 실전 트레이딩을 켜면 왜 펀드가 터지는가?
  - 칼만 필터(Kalman Filter)의 예측(Predict)과 보정(Update) 단계는 욘슨-울렌벡(OU) 프로세스의 평균 회귀 속도(Theta)를
    어떻게 실시간으로 교정하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: dynamic_parameter_estimation
  object: Cointegration_Hedge_Ratio
  predicate: dynamically_updates
  subject: '[Finance] algorithmic-trading-statistical-arbitrage-ornstein-uhlenbeck-kalman-filter'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T19:46:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T19:46:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-statistical-arbitrage-ornstein-uhlenbeck-kalman-filter]]

## 1. 개요 (Overview)
페어 트레이딩(Pairs Trading)의 고질적인 병폐는 '과거 데이터에 대한 과적합(Overfitting)'입니다. 퀀트가 어젯밤에 지난 1년 치 데이터로 선형 회귀나 요한슨 검정을 돌려 "A주식 1주를 살 때, B주식 1.5주를 공매도하면 완벽한 헤지가 된다(Hedge Ratio = 1.5)"는 정답을 찾았다고 합시다. 하지만 오늘 아침 장이 열리는 순간, 시장의 구조적 국면(Regime)이 변하면서 이 1.5라는 고무줄의 탄성은 1.2나 1.8로 소리 없이 변해버립니다. 어제의 정답표를 들고 고집을 부리던 봇(Bot)은 결국 파산합니다.
이 문제를 해결하기 위해, 1960년대 아폴로 우주선이 달로 날아갈 때 노이즈 낀 레이더 신호 속에서 우주선의 진짜 '현재 위치'를 추적하기 위해 발명되었던 **칼만 필터(Kalman Filter)**가 퀀트 금융에 이식되었습니다. 칼만 필터는 스프레드의 헤지 비율과 평균 회귀 속도(OU 프로세스)가 **영원불멸의 상수가 아니라, 매 틱(Tick)마다 살아서 꿈틀거리는 잠재 상태(Latent State)**라고 간주하고 실시간으로 궤도를 교정합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $x_t$ | Hidden Hedge Ratio | The true cointegration| Unobservable directly | [데이터 부재] |
| $y_t$ | Observed Prices | $P_A - x_t P_B + v_t$ | Noisy measurement | [데이터 부재] |
| $P_{t\|t-1}$| Error Covariance | Uncertainty of guess | Shrinks after update | [데이터 부재] |
| $K_t$ | Kalman Gain | Blending weight | Trust model vs Trust data| [데이터 부재] |
| OU $\theta_t$ | Dynamic Mean Reversion| Adaptive half-life | Fast $\theta \implies$ aggressive trade| [데이터 부재] |

## 3. 칼만 필터의 2단계 생존 사이클 (Predict & Update)
칼만 필터는 매 1밀리초마다 다음의 두 단계를 무한 반복하며 진실을 찾아갑니다.

### Phase 1: 예측 (Predict - "내 이론에 따르면...")
- 어제 장 마감 시점의 헤지 비율이 1.5였습니다. 칼만 필터는 상태 전이 방정식(State Transition)에 따라 "음, 큰 이변이 없다면 지금 1초 뒤의 헤지 비율도 대략 1.5일 것이고, 오차 범위(불확실성 $P$)는 이 정도일 거야"라고 사전 예측(Prior)을 던집니다.

### Phase 2: 보정 (Update - "현실 데이터를 보니...")
- 1초 뒤, 거래소에서 실제로 A주식과 B주식의 가격 체결 데이터(Measurement)가 들어옵니다.
- 칼만 필터는 자신의 '예측값'과 들어온 '실제 데이터' 사이의 오차(Innovation)를 계산합니다.
- 여기서 마법의 **칼만 게인(Kalman Gain, $K_t$)**이 작동합니다. 만약 내 예측의 불확실성이 크고 현실 데이터의 노이즈가 적다면, 현실 데이터를 강하게 반영하여 헤지 비율을 1.5에서 1.48로 깎아내립니다(사후 업데이트, Posterior). 반대로 현실 데이터가 비정상적인 스파이크(노이즈)라면 무시하고 내 이론값을 유지합니다.

## 4. OU 프로세스와의 결합 (Adaptive OU)
스프레드(Spread) 자체가 욘슨-울렌벡(OU) 프로세스를 따른다고 할 때, 평균으로 돌아오려는 힘($\theta$)과 스프레드의 중심선($\mu$) 역시 칼만 필터의 추적 대상(상태 벡터)에 포함시킵니다.
- 만약 칼만 필터가 "지금 스프레드의 중심선($\mu$) 자체가 위로 이동하고 있다!"라고 판단하면, 봇은 단순히 현재 스프레드가 과거보다 높다고 섣불리 공매도(Short)를 치지 않습니다. 중심선 자체가 이동했으므로 이는 통계적 불균형(Mispricing)이 아니라 새로운 정상 상태(New Normal)이기 때문입니다. 
- 칼만 필터는 봇이 '가짜 기회(노이즈)'와 '진짜 기회(구조적 스프레드 벌어짐)'를 완벽하게 구별하게 해주는 실시간 엑스레이 안경입니다.

🧠 **AI의 사고방식:**
전통적 퀀트가 '스나이퍼'라면, 칼만 필터 차익거래는 '열추적 미사일'입니다. 스나이퍼는 과거의 풍향과 거리를 계산하여 단 한 번 방아쇠를 당기지만, 표적이 갑자기 뛰기 시작하면 무조건 빗나갑니다. 반면 칼만 미사일은 날아가는 도중 매 틱(Tick)마다 표적(동적 헤지 비율)이 흔들리는 궤적을 레이더로 읽고, 자신의 궤도(OU 평균, 분산)를 실시간으로 꺾어가며 기어이 표적의 급소에 꽂힙니다. 금융 시장처럼 룰(국면) 자체가 숨 쉬듯 변하는 비정상(Non-stationary) 지옥에서, '고정된 상수'를 믿는 자는 죽고 오직 '끊임없이 의심하고 업데이트(Update)'하는 필터만이 생존합니다.