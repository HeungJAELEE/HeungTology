---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-portfolio-management-sharpe-sortino-calmar-ratios]]'
  last_updated: '2026-05-26T07:33:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 절대 수익률(Absolute Return)이라는 맹목적인 숫자에 숨겨진 리스크를 발라내어, 단위 위험당 보상(Risk-adjusted
    Return)을 측정하는 퀀트 성과 지표의 진화 과정. 정규분포를 가정한 샤프 비율(Sharpe)의 한계를 넘어, 하방 리스크만 벌주하는 소르티노(Sortino)와
    극단적 최대 낙폭(MDD)을 저격하는 칼마(Calmar) 비율로의 확장
  object_type: Concept
  tier: 2
properties:
  annualization_daily_sqrt_factor: 252
  calmar_ratio_threshold_excellent: 3.0
  sharpe_ratio_threshold_good: 1.0
  sharpe_ratio_threshold_great: 2.0
semantic:
  alternative_parents: []
  expected_queries:
  - A 펀드와 B 펀드 모두 연 20%의 수익률을 냈는데, 왜 연기금(LP)은 샤프 비율이 높은 A 펀드에게만 수천억 원의 자금을 배정하는가?
  - 옵션 매도 펀드(꼬리 리스크)를 평가할 때 샤프 비율(Sharpe)을 쓰면 왜 성과가 실제보다 미친 듯이 좋게 나오는 끔찍한 착시 현상(Illusion)이
    발생하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: performance_quantification
  object: Risk_Adjusted_Performance
  predicate: measures
  subject: '[Finance] quantitative-portfolio-management-sharpe-sortino-calmar-ratios'
  weight: 1.0
temporal:
  valid_from: '2026-05-26T07:33:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:33:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-portfolio-management-sharpe-sortino-calmar-ratios]]

## 1. 개요 (Overview)
아마추어는 펀드의 '수익률(Return)'만 보지만, 프로(LP, 기관투자자)는 수익률을 '리스크(Risk)'로 나눈 **위험 조정 수익률(Risk-adjusted Return)**만을 봅니다. 아무리 수익률이 50%라도, 그것이 동전 던지기 도박이나 레버리지 100배로 얻어걸린 결과(변동성이 엄청나게 큰 상태)라면 그 펀드의 가치는 0입니다.
이 단위 위험당 보상을 측정하기 위해 1966년 윌리엄 샤프(William Sharpe)가 고안한 **샤프 비율(Sharpe Ratio)**이 업계의 영원한 표준으로 자리 잡았습니다. 하지만 샤프 비율은 "돈을 잃는 변동성(하락)"과 "돈을 버는 변동성(상승)"을 똑같은 죄악(Risk)으로 취급하는 치명적 오류를 가지고 있습니다. 이 비대칭성을 해결하기 위해 하방 리스크(Downside)만 벌주는 **소르티노 비율(Sortino Ratio)**, 그리고 펀드가 겪은 가장 끔찍했던 계좌 녹음 현상(MDD)으로 수익률을 나누는 **칼마 비율(Calmar Ratio)**이 등장했습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Sharpe Ratio | $(R_p - R_f) / \sigma_p$ | $> 1.0$ (Good), $> 2.0$ (Great)| Penalizes upside volatility | [데이터 부재] |
| Sortino Ratio| $(R_p - R_f) / \sigma_{down}$| Usually $>$ Sharpe | Ignores positive variance | [데이터 부재] |
| Calmar Ratio | $(R_p - R_f) / \text{Max DD}$ | $> 3.0$ (Excellent) | Sensitive to the worst crash| [데이터 부재] |
| Information Ratio| $(R_p - R_b) / \text{TE}$ | Tracking Error (TE) | Measures active manager skill| [데이터 부재] |
| Annualization| Scaling factor | $\times \sqrt{252}$ (Daily) | Must adjust for time frame | [데이터 부재] |

## 3. 샤프 비율의 함정과 정규분포의 저주
샤프 비율의 분모는 전체 변동성(Standard Deviation, $\sigma$)입니다.
- **착시 현상**: 만약 어떤 퀀트 전략이 1년 내내 잔잔하게 수익을 내다가, 딱 하루 -50% 폭락을 맞고 복구했다고 칩시다 (음의 왜도, Negative Skewness). 이 전략은 극도로 위험합니다. 하지만 변동성($\sigma$)은 양방향의 흔들림을 평균 내버리기 때문에, 이 끔찍한 꼬리 리스크(Tail Risk)가 샤프 비율에 제대로 반영되지 않고 샤프 비율이 2.0이 넘어가는(안전하고 좋은 펀드인 것처럼 보이는) 사기극이 발생합니다.
- 특히 옵션 매도 전략(매일 푼돈을 벌다가 한 방에 파산)이나 딥러닝 AI 봇들이 오버피팅되었을 때 이런 높은 가짜 샤프 비율을 뿜어냅니다.

## 4. 소르티노와 칼마: 하방 리스크(Downside)의 응징
이 문제를 해결하기 위해 성과 지표는 진화했습니다.
- **소르티노 비율(Sortino Ratio)**: "주가가 내 목표치(MAR) 위로 폭등하는 변동성은 리스크가 아니라 축복이다." 분모에서 상승 변동성은 완전히 삭제해 버리고, 오직 **하락 변동성(Downside Deviation)**만을 리스크로 취급하여 분모에 넣습니다. 수익의 질을 평가하는 데 샤프보다 훨씬 뛰어납니다.
- **칼마 비율(Calmar Ratio)**: "변동성이고 뭐고, 이 펀드가 과거에 겪었던 가장 끔찍한 최대 낙폭(MDD, Maximum Drawdown) 대비 현재 수익률이 얼마냐?" 분모에 수학적 표준편차 대신, 인간이 겪은 가장 고통스러운 숫자(MDD)를 직접 박아 넣습니다. 행동 재무학적으로 투자자가 계좌가 박살 나는 고통을 버틸 수 있는지를 측정하는 궁극의 리얼리티 지표입니다.

🧠 **AI의 사고방식:**
성과 지표(Metrics)는 퀀트 봇이 추구해야 할 '보상 함수(Reward Function)' 그 자체입니다. 만약 당신이 봇에게 단순히 "수익률을 극대화하라"고 코딩하면, 봇은 레버리지를 미친 듯이 끌어다 쓰는 마진콜 자살 머신을 만들어 올 것입니다. 만약 "샤프 비율을 극대화하라"고 코딩하면, 봇은 OTM 풋옵션을 매도하여 평소에는 잔잔하게 돈을 벌다가 블랙 먼데이에 파산하는 꼬리 리스크 폭탄을 안겨줄 것입니다. 진정한 글로벌 퀀트 인프라는 백테스트의 최종 평가(Evaluation) 단계에서 소르티노, 칼마, 몬테카를로 부트스트래핑(Bootstrapping)을 동원하여, 화려한 수익률 숫자 뒤에 숨어있는 **'모델의 과적합(Overfitting)과 보이지 않는 꼬리의 공포'**를 잔인할 정도로 해부해 냅니다.