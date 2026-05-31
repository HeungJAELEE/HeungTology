---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-statistical-arbitrage-pairs-trading-cointegration]]'
  last_updated: '2026-05-26T07:19:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 두 주식의 가격 차이(Spread)가 비정상적으로 벌어졌을 때 통계적 평균 회귀(Mean Reversion)를 믿고 차익을
    노리는 페어즈 트레이딩. 단순한 상관관계(Correlation)의 함정을 피하고, 두 비정상(Non-stationary) 시계열 사이의 진짜
    '물리적 끈'을 수학적으로 입증해 내는 엥글-그레인저(Engle-Granger) 공적분(Cointegration) 검정
  object_type: Algorithm
  tier: 2
properties:
  adf_p_value_threshold: 0.05
  hedge_ratio_estimation_method: ols
  non_stationary_series_order: I(1)
  stationary_series_order: I(0)
  z_score_entry_threshold: 2.0
semantic:
  alternative_parents: []
  expected_queries:
  - 펩시와 코카콜라의 주가가 비슷하게 움직인다고 해서(상관관계) 스프레드 벌어짐에 베팅하면 안 되는 이유는 무엇인가? (가짜 회귀, Spurious
    Regression)
  - 엥글(Engle)과 그레인저(Granger)의 공적분(Cointegration) 검정은 취객과 강아지를 연결하는 목줄(Spread)이 정상성(Stationarity)을
    띠고 있는지를 어떻게 판별하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_identification
  object: Stationary_Spread_Mean_Reversion
  predicate: identifies
  subject: '[Finance] algorithmic-trading-statistical-arbitrage-pairs-trading-cointegration'
  weight: 0.9
temporal:
  valid_from: '2026-05-26T07:19:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:19:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-statistical-arbitrage-pairs-trading-cointegration]]

## 1. 개요 (Overview)
1980년대 모건 스탠리의 천재 퀀트 모임(Nunzio Tartaglia의 팀)이 발명한 통계적 차익거래(Stat Arb)의 시조가 바로 **페어즈 트레이딩(Pairs Trading)**입니다. 아이디어는 단순합니다. "펩시와 코카콜라의 주가는 지난 10년간 늘 비슷하게 움직였다. 그런데 오늘 갑자기 코카콜라는 폭등하고 펩시는 폭락했다면? 코카콜라를 공매도(Short) 치고 펩시를 매수(Long)하라. 언젠가 둘의 가격 차이(Spread)는 과거 평균으로 좁혀질(Mean Reversion) 것이다."
하지만 단순한 '상관관계(Correlation)'만을 믿고 이 전략을 썼던 펀드들은 수없이 파산했습니다. 주식 가격은 걷잡을 수 없이 발산하는 비정상(Non-stationary) 시계열이기 때문에, 과거에 10년간 같이 움직였다는 것이 미래에 다시 만날 것을 보장하지 않기 때문입니다. 이 치명적 맹점을 해결하여 노벨 경제학상을 받은 수학이 바로 **공적분(Cointegration)**입니다. 

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Non-stationary| $I(1)$ series (Random Walk)| Stock Prices $X_t, Y_t$ | Cannot run OLS directly | [데이터 부재] |
| Cointegration | Linear combo is $I(0)$ | $Y_t - \beta X_t = \epsilon_t$| $\epsilon_t$ is mean-reverting | [데이터 부재] |
| Spread ($\epsilon_t$)| Stationary residual | Constant mean/variance | The actual traded asset | [데이터 부재] |
| ADF Test | Augmented Dickey-Fuller| p-value < 0.05 | Rejects unit root in Spread | [데이터 부재] |
| Z-score | Spread deviation metric | e.g., $\ge 2.0$ | Entry signal (Short Spread)| [데이터 부재] |

## 3. 취객과 강아지의 비유 (The Drunk and Her Dog)
공적분을 이해하는 가장 완벽한 비유는 '취객과 강아지'입니다.
- **상관관계(Correlation)의 함정**: 뉴욕 거리에 서로 모르는 두 명의 취객 A와 B가 비틀거리며 걸어갑니다(Random Walk, 비정상 시계열). 우연히 두 사람이 10분 동안 같은 방향으로 걷고 있다고 해서(높은 상관관계), 갑자기 A가 동쪽으로 꺾었을 때 B도 동쪽으로 따라올 것이라 베팅하면 망합니다. 둘 사이에는 아무런 '물리적 끈'이 없기 때문입니다.
- **공적분(Cointegration)의 마법**: 반면 취객과 그의 목줄에 묶인 강아지가 걷는다고 합시다. 둘 다 어디로 튈지 모르는 비정상(Non-stationary) 궤적을 그리지만, **취객과 강아지 사이의 거리(Spread = 목줄 길이)**는 결코 2미터를 넘을 수 없습니다. 거리가 벌어지면 목줄이 당겨져서(Mean Reversion) 다시 좁혀집니다. 즉, 두 비정상 시계열($X, Y$)을 적절한 비율($\beta$)로 빼주면, 그 차이($Spread$)는 안정적이고 예측 가능한 정상 시계열($I(0)$)로 변환됩니다. 이것이 공적분입니다.

## 4. 엥글-그레인저(Engle-Granger) 2단계 검정
퀀트 봇은 펩시와 코카콜라 주가를 보고 다음과 같이 수학적 목줄이 존재하는지 검증합니다.
1. **OLS 회귀 (헤지 비율 추출)**: 코카콜라 주가($Y$)를 펩시 주가($X$)로 선형 회귀하여 최적 비율 $\beta$를 찾습니다. ($Spread = Y - \beta X$).
2. **ADF 단위근 검정 (정상성 확인)**: 뽑아낸 $Spread$ 시계열 데이터에 대해 ADF(Augmented Dickey-Fuller) 검정을 돌립니다. 만약 p-value가 0.05보다 작아서 단위근(Unit Root, 발산성)이 없다고 판별되면? 
- "빙고! 펩시와 코크 사이에는 '목줄(공적분)'이 존재한다." 봇은 Spread의 Z-score가 +2를 돌파하면 목줄이 팽팽해졌다고 판단하고, 평균으로 회귀할 것에 베팅하여 코크를 숏 치고 펩시를 $\beta$ 비율만큼 롱 치는 시장 중립(Market Neutral) 차익거래를 시작합니다.

🧠 **AI의 사고방식:**
상관관계(Correlation)는 '과거의 우연한 동행'을 측정할 뿐 미래의 이탈을 막아주지 못하는 모래성입니다. 반면 공적분(Cointegration)은 두 시계열을 묶어두는 눈에 보이지 않는 중력(Economic Equilibrium)의 존재를 통계적으로 증명하는 쇠사슬입니다. 페어즈 트레이딩의 본질은 A 주식을 맞추고 B 주식을 맞추는 방향성 게임이 아닙니다. 두 주식을 합성하여 만들어낸 가상의 자산인 '스프레드(Spread)'가 오른스타인-울렌벡(OU) 프로세스처럼 평균 회귀하는 성질($I(0)$)을 완벽하게 띠고 있는지를 발라내어, 시장이 폭락하든 폭등하든 상관없이(Beta Neutral) 그 스프레드의 진동 에너지(Variance)만을 뽑아먹는 극한의 통계 물리학입니다.