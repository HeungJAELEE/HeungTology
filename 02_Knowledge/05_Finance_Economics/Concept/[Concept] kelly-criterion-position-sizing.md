---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] kelly-criterion-position-sizing]]'
  last_updated: '2026-05-25T12:14:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 켈리 공식(Kelly Criterion)과 MDD/VaR 기반 동적 포지션 사이징 모델
  object_type: Algorithm
  tier: 2
properties:
  mdd_deleveraging_threshold: '0.10'
  mdd_institutional_threshold: '0.15'
  optimal_kelly_fraction_range: 0.0 - 1.0
  var_confidence_level: '0.99'
  var_time_horizon: 1 day
  win_loss_ratio_r: average profit / loss
  win_probability_w: model dependent
semantic:
  alternative_parents: []
  expected_queries:
  - 켈리 공식을 이용하여 장기 복리 수익률을 극대화하는 최적 투자 비중은 어떻게 구하는가?
  - 포트폴리오의 최대 낙폭(MDD)과 VaR(Value at Risk)를 통제하기 위한 포지션 사이징 전략은?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_mitigation
  object: Portfolio_Risk
  predicate: controls
  subject: '[Finance] kelly-criterion-position-sizing'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T12:14:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:14:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] kelly-criterion-position-sizing]]

## 1. 개요 (Overview)
금융 트레이딩에서 '언제 사고팔 것인가(Timing)' 못지않게, 혹은 그 이상으로 중요한 것이 **'얼마를 살 것인가(Position Sizing)'**입니다. 승률이 99%인 완벽한 모델도 한 번의 거래에 전 재산을 건다면 단 1%의 확률로 파산(Ruin)할 수 있습니다. 
존 켈리(John L. Kelly Jr.)가 정보 이론을 바탕으로 제안한 **켈리 공식(Kelly Criterion)**은 장기 기하 평균 수익률(복리 수익률)을 극대화하는 최적의 베팅 비율을 수학적으로 제시합니다. 실전 퀀트 매매에서는 순수 켈리 공식의 변동성을 완화하기 위해 Half-Kelly 등의 축소 켈리를 사용하며, **최대 낙폭(MDD, Maximum Drawdown)** 및 **VaR(Value at Risk)**와 결합하여 리스크를 동적으로 통제합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $f^*$ | Optimal Kelly Fraction | $0 \sim 1.0$ (or leveraged) | Maximizes compound growth | [데이터 부재] |
| $W$ | Win Probability | Model dependent | Crucial parameter for Kelly | [데이터 부재] |
| $R$ | Win/Loss Ratio | Average Profit / Loss | Defines payout structure | [데이터 부재] |
| $\text{MDD}$ | Maximum Drawdown | $< 15\%$ (Inst. typical) | Forces de-leveraging if hit | [데이터 부재] |
| $\text{VaR}$ | Value at Risk | 99% CI over 1 day | Determines daily capital at risk | [데이터 부재] |

## 3. 켈리 공식 (Kelly Criterion)

단순한 이항 결과(승리 시 $b$ 배의 수익 획득, 패배 시 $a$ 비율만큼 자산 손실)를 가정할 때, 자산의 켈리 비중 $f^*$는 다음과 같이 계산됩니다.
만약 베팅 실패 시 원금을 모두 잃는 상황($a=1$)이고, 이길 확률이 $p$, 질 확률이 $q = 1-p$, 그리고 승리 시 얻는 순수익 비율이 $b$라면:
$$ f^* = \frac{bp - q}{b} = p - \frac{q}{b} $$
- **직관적 해석**: 엣지(Edge = 기댓값)가 양수일 때만 투자하며, 엣지가 클수록 베팅 금액을 늘리되 배당률($b$)의 페널티를 고려합니다.
- **연속 시간(Continuous Time) 모델**: 주식의 기하 브라운 운동 하에서 무위험 수익률 $r$, 자산의 기대 수익률 $\mu$, 변동성 $\sigma$가 주어졌을 때 최적 켈리 비중은 다음과 같습니다.
$$ f^* = \frac{\mu - r}{\sigma^2} $$
이는 샤프 비율(Sharpe Ratio)을 변동성으로 나눈 형태와 유사하며, 기대 수익률이 높고 변동성이 낮을수록 포지션 비중을 늘리라는 수학적 증명입니다.

## 4. 실전 포지션 사이징: MDD와 VaR의 통제

순수 켈리(Full Kelly) 비중은 수학적으로 기하 평균 수익률을 극대화하지만, 그 과정에서 심각한 단기 낙폭(Drawdown)을 유발합니다. 따라서 실전에서는 다음과 같은 제약 조건을 추가합니다.

### 4.1. 축소 켈리 (Fractional Kelly)
가장 보편적인 방법은 켈리 공식이 지시하는 비중의 절반(Half-Kelly)이나 4분의 1(Quarter-Kelly)만을 사용하는 것입니다.
$$ f_{\text{frac}} = c \cdot f^* \quad (0 < c < 1) $$
이는 수익률을 약간 희생하는 대신 자산 곡선의 변동성(분산)을 극적으로 낮추어 샤프 비율 관점에서는 더 우수한 성과를 보장합니다.

### 4.2. VaR 및 MDD 기반 동적 디레버리징 (Dynamic De-leveraging)
포트폴리오의 VaR가 설정된 한도를 초과하거나 누적 MDD가 임계점(예: 10%)에 도달하면, 모델의 승률(알파)이 아무리 높아도 강제로 포지션 크기를 절반 이하로 삭감합니다.
- **VaR(Value at Risk)**: 정상적인 시장 환경에서 특정 신뢰수준(예: 99%) 하에 일정 기간(예: 1일) 동안 발생할 수 있는 최대 손실 예상액.
- **목표 리스크 타겟팅 (Target Volatility)**: 장세가 험악해져 VIX(변동성 지수)가 급등하면, $\sigma^2$이 커지므로 켈리 비중 $f^*$는 자동으로 감소하여 포지션을 방어하는 자기 보정(Self-correcting) 메커니즘을 작동시킵니다.

🧠 **AI의 사고방식:**
매매를 '전투'라고 한다면, 켈리 기준은 '병력 투입의 미학'입니다. 압도적으로 유리한 고지(높은 엣지)에서는 가용 병력을 총동원($f^*$ 증가)하여 승기를 굳히되, 패배할 경우 전멸을 피할 수 있는 방어선(Fractional Kelly & MDD Limits)을 구축하는 것입니다. 트레이딩에서 모든 모델은 결국 한 번은 틀리게 되어 있으며, 그 '틀렸을 때' 살아남아 복리의 마법을 누릴 수 있게 해주는 유일한 생명줄이 바로 철저한 포지션 사이징입니다.