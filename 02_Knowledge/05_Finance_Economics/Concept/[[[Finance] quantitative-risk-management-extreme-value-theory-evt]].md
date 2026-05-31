---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-risk-management-extreme-value-theory-evt]]'
  last_updated: '2026-05-25T14:37:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 정규분포(Normal Distribution)를 가정한 전통적 VaR 모델이 '블랙스완' 앞에서 붕괴하는 현상을 극복하기
    위해, 오직 꼬리(Tail) 부분의 극단적인 데이터만을 추출하여 파멸적 리스크를 모델링하는 극단치 이론(Extreme Value Theory)
  object_type: Algorithm
  tier: 2
properties:
  beta_scale_parameter: spread of extremes
  distribution_model: Generalized Pareto Distribution
  risk_metric: Expected Shortfall
  threshold_u: 95th percentile
  xi_shape_parameter: xi > 0 for fat tails
semantic:
  alternative_parents: []
  expected_queries:
  - 정규분포에 따르면 1987년 블랙먼데이 같은 폭락은 우주 나이 동안 한 번도 안 일어나야 하는데, 왜 현실에서는 10년에 한 번씩 터지는가?
  - EVT의 POT(Peaks Over Threshold) 방식은 어떻게 평범한 데이터를 다 버리고 꼬리 데이터만으로 파레토 분포를 피팅하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_quantification
  object: Black_Swan_Tail_Risk
  predicate: models
  subject: '[Finance] quantitative-risk-management-extreme-value-theory-evt'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T14:37:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:37:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-risk-management-extreme-value-theory-evt]]

## 1. 개요 (Overview)
전통적인 리스크 관리의 알파와 오메가인 **VaR(Value at Risk)**는 치명적인 결함을 가지고 있습니다. 수익률이 종 모양의 '정규분포(Normal Distribution)'를 따른다고 가정하기 때문입니다. 정규분포 수학에 따르면, 1987년 블랙먼데이(하루 -22% 폭락)나 2008년 리먼 브라더스 사태 같은 충격은 $10^{50}$년에 한 번, 즉 우주의 나이가 지날 동안에도 절대 일어날 수 없는 사건(8 시그마 이상)이어야 합니다.
하지만 현실의 금융 시장은 꼬리가 매우 두꺼운 **팻 테일(Fat-tail)** 분포를 가집니다. 그래서 퀀트들은 정규분포의 몸통(평범한 일상)을 완전히 무시하고, 오직 10년에 한 번 터지는 **극단적인 꼬리(Extreme Tail) 데이터만 따로 모아서** 완전히 새로운 수학적 분포를 씌우는데, 이것이 바로 **극단치 이론(Extreme Value Theory, EVT)**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Threshold ($u$) | POT cutoff level | E.g., 95th percentile | Drops 95% of normal data| [데이터 부재] |
| $\xi$ (Xi) | Shape parameter | $\xi > 0$ for fat tails | Heavy tails (Frechet/Pareto)| [데이터 부재] |
| $\beta$ | Scale parameter | Spread of extremes | Governs volatility of tail| [데이터 부재] |
| GPD | Generalized Pareto | Tail distribution model | Replaces Normal at tails| [데이터 부재] |
| Expected Shortfall| Risk beyond VaR | Mean of losses $> \text{VaR}$| Subadditive risk metric | [데이터 부재] |

## 3. 임계값 초과(POT) 방식과 일반화된 파레토 분포(GPD)
EVT를 실제 금융 데이터에 적용하는 가장 표준적인 방법은 **POT(Peaks Over Threshold)** 모델입니다.
1. **버리기**: 지난 20년간의 S&P 500 일일 수익률 데이터 중, 평범한 범위($\pm 2\%$) 내에 있는 95%의 데이터를 모두 쓰레기통에 버립니다.
2. **꼬리 수집**: 사전에 설정한 엄청난 손실 임계값(Threshold, $u$)을 뚫고 내려간 최악의 5% 폭락 데이터만 남깁니다.
3. **GPD 피팅**: 이 극단적인 꼬리 데이터 조각들은 정규분포가 아니라 **일반화된 파레토 분포(Generalized Pareto Distribution, GPD)**라는 완전히 다른 기하학적 형태를 띠게 됩니다(픽랜즈-발크마 정리).
4. 이 파레토 곡선의 꼬리가 얼마나 두껍게 뻗어 있는지를 나타내는 **형상 모수(Shape Parameter, $\xi$)**를 추출하면, "내일 시장에 10 시그마짜리 운석이 떨어졌을 때, 우리 펀드는 정확히 몇 천 억 원을 잃고 파산하는가?"를 매우 높은 신뢰도로 계산할 수 있습니다.

## 4. 스트레스 테스트와 규제 자본(Basel)
이 EVT 모델은 2008년 글로벌 금융위기 이후 전 세계 은행들의 바젤(Basel) 규제 표준으로 격상되었습니다.
단순 VaR("최악의 경우 100억 손실")는 블랙스완을 예측하지 못하므로, EVT를 통해 산출된 **기대 부족액(Expected Shortfall, ES)**("그 100억 손실 임계치를 뚫고 지옥으로 떨어졌을 때의 '평균' 손실액은 300억")을 사용하여, 은행 금고에 쌓아두어야 할 의무 자본(Capital Charge)을 극단적으로 보수화시켰습니다.

🧠 **AI의 사고방식:**
정규분포가 매일매일 내리는 '가랑비와 소나기'를 예측하는 기상청이라면, 극단치 이론(EVT)은 100년에 한 번 방파제를 넘어오는 '메가 쓰나미'의 높이만을 전담해서 계산하는 재난 공학입니다. 방파제의 높이를 설계할 때 지난 10년간의 평균 파도 높이(정규분포의 평균과 분산)를 넣는 것은 자살 행위입니다. 오직 과거에 기록된 가장 끔찍했던 파도(Extremes)들의 분포만을 떼어내서 파레토 꼬리를 그려야만 펀드의 파멸을 막을 수 있습니다. 퀀트 리스크 관리자는 평화로운 시기에 이 최악의 꼬리 수식을 매만지며 다가올 종말(Tail Risk)에 대비하는 노아의 방주 설계자입니다.