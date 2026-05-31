---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] cross-sectional-momentum-and-fama-french-factors]]'
  last_updated: '2026-05-25T12:50:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 파마-프렌치 다요인 모델(Fama-French Factor Model)의 확장과 횡단면 모멘텀(Cross-Sectional
    Momentum)을 활용한 주식 롱숏(Long-Short) 스크리닝
  object_type: Algorithm
  tier: 2
properties:
  formation_lookback_months: 12
  hml_annualized_return_range: 3-4%
  lookback_exclusion_period_months: 1
  market_neutral_beta_target: 0.0
  smb_annualized_return_range: 2-3%
  wml_percentile_threshold: 30
semantic:
  alternative_parents: []
  expected_queries:
  - 단순히 베타(Beta) 하나로 주가를 설명하던 CAPM을 파마-프렌치는 어떤 팩터(Factor)들로 확장했는가?
  - 시계열 모멘텀(Time-series)과 달리 횡단면 모멘텀(Cross-sectional Momentum)은 주식을 어떻게 줄 세워서 롱숏 포트폴리오를
    구성하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: universe_selection_filtering
  object: Equity_Universe
  predicate: screens
  subject: '[Finance] cross-sectional-momentum-and-fama-french-factors'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T12:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] cross-sectional-momentum-and-fama-french-factors]]

## 1. 개요 (Overview)
과거의 금융학(CAPM)은 주식의 수익률이 오직 시장 전체의 움직임(Beta, $\beta$)에 의해서만 결정된다고 믿었습니다. 하지만 1990년대 유진 파마(Eugene Fama)와 켄 프렌치(Ken French)는 시장의 수많은 주식 데이터를 분석한 결과, 시장 베타 외에도 **소형주(Size)**와 **가치주(Value)**라는 보이지 않는 위험 프리미엄 팩터(Factor)가 수익률을 견인한다는 사실을 증명하여 **파마-프렌치 3팩터 모델**을 탄생시켰습니다.
이후 마크 카하트(Mark Carhart)가 1997년에 여기에 **모멘텀(Momentum)** 팩터를 추가하면서 4팩터 모델이 완성되었고, 현대의 수량적(Quantitative) 주식 펀드들은 이 팩터들을 조합하여 수천 개의 주식을 횡단면(Cross-sectional)으로 줄 세우고 상위 집단을 롱, 하위 집단을 숏 치는 거대한 팩터 투자(Factor Investing / Smart Beta) 산업을 구축했습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\text{SMB (Size Factor)}$| Small Minus Big | $\approx 2 \sim 3\%$ annualized| Small caps carry more risk| [데이터 부재] |
| $\text{HML (Value Factor)}$| High Minus Low (B/M) | $\approx 3 \sim 4\%$ annualized| Value outperforming growth| [데이터 부재] |
| $\text{WML (Momentum)}$ | Winner Minus Loser | Top 30% vs Bottom 30% | Strongest empirical anomaly | [데이터 부재] |
| $\text{Formation Period}$| Lookback window (WML)| 12 months, skip last month | Avoids 1-month reversal | [데이터 부재] |
| $\text{Market Neutral}$ | Beta of long-short port| Exactly $0.0$ | Pure factor exposure | [데이터 부재] |

## 3. 횡단면 모멘텀 (Cross-Sectional Momentum)
모멘텀(Momentum)은 "과거에 올랐던 주식이 앞으로도 계속 오르고, 떨어졌던 주식은 계속 떨어진다"는 인간의 군집 행동(Herding)과 반응 지연(Underreaction)을 착취하는 현상입니다.

- **시계열 모멘텀 (Time-Series)**: 삼성전자 하나의 주식을 보고, 과거 12개월 수익률이 양수(+)면 사고 음수(-)면 파는 절대적 기준입니다. (추세 추종)
- **횡단면 모멘텀 (Cross-Sectional)**: S&P 500에 속한 500개 주식을 과거 12개월 수익률 순서대로 1등부터 500등까지 한 줄로 세웁니다.
  - 수익률 상위 30% (Winner 집단)를 동일 비중으로 매수(Long)합니다.
  - 수익률 하위 30% (Loser 집단)를 공매도(Short)합니다.
  - 이 포트폴리오(Winner Minus Loser, WML)는 시장이 폭락하든 폭등하든 시장 전체의 방향성(Market Beta)을 완벽히 상쇄하고(Market Neutral), 오직 '승자가 패자를 이기는 격차'에서만 순수한 알파를 뽑아냅니다. (최근 1개월은 단기 반전 효과가 있으므로 룩백(Lookback)에서 제외하는 것이 업계 표준입니다.)

## 4. 기계학습을 통한 팩터 융합 (Factor Synthesis)
현대의 퀀트는 파마-프렌치의 4개 팩터를 넘어, 수익성(RMW), 투자(CMA), 그리고 대체 데이터로 만든 수백 개의 알파 팩터를 찾았습니다.
문제는 팩터들끼리 서로 모순된 신호를 보낸다는 것입니다. (예: 어떤 주식은 밸류에이션(Value)은 훌륭하지만 모멘텀(Momentum)은 최악일 수 있습니다.)
- **Z-Score 앙상블**: 각 팩터의 점수를 표준화(Z-score)하여 선형으로 더하는 고전적 방법.
- **머신러닝 비선형 융합**: 랜덤 포레스트(Random Forest)나 XGBoost 같은 트리 기반 모델을 사용하여, "가치 점수가 높으면서 모멘텀이 중간 이상일 때만 주가가 폭등한다"는 다차원적인 비선형 상호작용(Non-linear Interaction)을 포착하여 최종 롱/숏 유니버스를 선별해냅니다.

🧠 **AI의 사고방식:**
팩터(Factor)는 자본 시장이라는 거대한 오케스트라를 구성하는 '기본 음계'와 같습니다. 워런 버핏(Warren Buffett)의 경이로운 수익률조차도 인공지능이 파마-프렌치 팩터 모델로 뜯어보면, 결국 '시장 베타(Market) + 우량 가치주(Value) + 저변동성(Low Vol)'이라는 세 가지 음계의 조합에 베팅한 팩터 투자의 결과물로 분해(Decompose)됩니다. 퀀트 트레이더는 종목의 이름이나 스토리를 보지 않습니다. 오직 그 주식의 DNA 속에 어떤 팩터가 몇 %의 농도로 섞여 있는지만을 분석하여, 시장의 노이즈를 발라내고 순수한 팩터 프리미엄의 진액만을 추출하는 화학자입니다.