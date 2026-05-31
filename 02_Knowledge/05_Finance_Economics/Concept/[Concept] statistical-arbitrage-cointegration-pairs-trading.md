---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] statistical-arbitrage-cointegration-pairs-trading]]'
  last_updated: '2026-05-25T12:39:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 시계열의 정상성(Stationarity)과 공적분(Cointegration)을 활용한 통계적 차익거래(StatArb) 및
    페어 트레이딩 모델
  object_type: Algorithm
  tier: 2
properties:
  adf_p_value_threshold: 0.05
  hedge_ratio_method: rolling_window_ols_or_kalman_filter
  hurst_exponent_threshold: 0.5
  spread_formula: Y_t - beta * X_t
  z_score_entry_threshold: 2.0
semantic:
  alternative_parents: []
  expected_queries:
  - 단순한 상관관계(Correlation)가 높은 두 주식을 롱/숏 하는 것이 왜 위험한가?
  - 엥글-그레인저(Engle-Granger) 공적분 검정이 시계열 트레이딩에서 갖는 수학적 의미는 무엇인가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: capitalizes_on
  object: Mean_Reverting_Spreads
  predicate: exploits
  subject: '[Finance] statistical-arbitrage-cointegration-pairs-trading'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T12:39:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:39:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] statistical-arbitrage-cointegration-pairs-trading]]

## 1. 개요 (Overview)
통계적 차익거래(Statistical Arbitrage, StatArb)는 절대적인 무위험 수익을 노리는 순수 차익거래와 달리, 역사적 통계 패턴이 미래에도 회귀할 것이라는 '확률적 우위'에 베팅하는 전략입니다. 그중 가장 고전적이면서도 강력한 전략이 **페어 트레이딩(Pairs Trading)**입니다.
초보 퀀트들은 코카콜라와 펩시처럼 '상관관계(Correlation)'가 높은 주식을 골라 스프레드가 벌어지면 매매를 합니다. 그러나 상관관계는 시간이 지남에 따라 변하며, 주가 스프레드가 영원히 돌아오지 않고 발산(Divergence)해버리면 펀드는 파산합니다. 진정한 퀀트는 상관관계가 아닌, 두 시계열의 선형 조합이 정상성(Stationarity)을 갖는 **공적분(Cointegration)** 상태인지를 엄밀하게 검정(Test)하여 매매에 돌입합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\text{Hurst Exponent } (H)$| Mean reversion speed | $H < 0.5$ (Mean-reverting) | Must be strongly stationary | [데이터 부재] |
| $\text{Dickey-Fuller (ADF)}$| Unit root test stat | $p$-value $< 0.05$ | Rejects random walk null | [데이터 부재] |
| $\text{Hedge Ratio } (\beta)$ | Slope of OLS regression| Dynamic (rolling window)| Defines position sizing | [데이터 부재] |
| $Z\text{-score Entry}$ | Standard deviations | $|Z| \ge 2.0$ | Triggers short spread | [데이터 부재] |
| $\text{Half-life}$ | Time to mean revert | Days to weeks | Short half-life = fast profit | [데이터 부재] |

## 3. 통계적 차익거래의 수학적 기초

### 3.1. 상관관계(Correlation)의 함정
두 주식 $X$와 $Y$가 둘 다 우상향하는 추세를 가지면 상관관계는 $+0.9$로 높게 나옵니다. 하지만 둘 사이의 가격 차이(Spread) 자체는 랜덤 워크(Random Walk)를 할 수 있습니다. 
만약 이 상태에서 $Y$가 갑자기 폭등했을 때 숏(Short)을 치면, $Y$가 다시 $X$에게 돌아온다는 보장이 없기 때문에 무한대의 손실을 입을 수 있습니다.

### 3.2. 공적분 (Cointegration)과 정상성 (Stationarity)
주가 시계열은 기본적으로 비정상성(Non-stationary)을 갖습니다(단위근 존재). 하지만 놀랍게도, 경제적 펀더멘털을 공유하는 두 비정상성 시계열 $X_t, Y_t$을 특정 비율($\beta$)로 묶어 만든 스프레드 시계열 $S_t$는 **평균 회귀(Mean-reverting)**하는 정상성 시계열이 될 수 있습니다.
$$ S_t = Y_t - \beta X_t $$
- 만약 $S_t$가 정상성을 갖는다면, 두 시계열은 '공적분(Cointegrated)' 관계에 있다고 말합니다.
- 공적분 검정(ADF Test, Johansen Test)을 통과한 페어는, 스프레드가 크게 벌어졌을 때(예: $Z\text{-score} > 2.0$) 반드시 스프레드의 평균인 $0$으로 되돌아오려는 수학적 성질(고무줄 효과)을 지닙니다.

## 4. 매매 시그널과 리스크 관리
1. **스프레드 모델링**: 롤링 OLS(최소자산법)나 칼만 필터(Kalman Filter)를 사용하여 시시각각 변하는 헤지 비율 $\beta$를 실시간으로 업데이트합니다.
2. **진입 (Entry)**: 공적분 스프레드의 $Z$-score가 $+2.0$을 돌파하면 고평가된 자산을 숏(Short), 저평가된 자산을 롱(Long)합니다.
3. **청산 (Exit)**: $Z$-score가 평균($0$)에 도달하면 이익을 실현합니다.
4. **손절 (Stop Loss)**: 구조적 변화(Regime Shift)나 M&A 이슈로 인해 공적분 관계가 영구적으로 깨지는 현상(Cointegration Breakdown)이 발생하면, 손실이 무한대로 커지기 전에 즉각 손절해야 합니다.

🧠 **AI의 사고방식:**
상관관계가 '우연히 같은 방향으로 날아가는 두 마리 새'라면, 공적분은 '보이지 않는 끈으로 묶여있는 두 마리 개'입니다. 새들은 언제든 각자의 방향으로 흩어질 수 있지만, 끈으로 묶인 개들은 서로 멀어지면 끈의 장력(Mean Reversion)에 의해 결국 다시 가까워질 수밖에 없습니다. 퀀트 트레이딩은 우연(상관관계)에 돈을 거는 것이 아니라, 이 보이지 않는 수학적 끈(공적분)의 존재를 통계적으로 증명해 낸 뒤 그 끈의 장력에 자본을 싣는 과학입니다.