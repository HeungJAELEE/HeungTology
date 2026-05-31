---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-portfolio-management-kelly-criterion-optimal-bet-sizing]]'
  last_updated: '2026-05-26T07:54:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 확률적으로 유리한 게임(승률>50%)이라도 베팅 규모(Size)를 잘못 조절하면 장기적으로 계좌가 0으로 수렴하는 기하평균의
    저주를 극복하기 위해, 복리 성장률(CAGR)을 극대화함과 동시에 파산 확률을 0으로 묶어버리는 정보이론 기반의 절대 베팅 공식 켈리 기준(Kelly
    Criterion)
  object_type: Algorithm
  tier: 2
properties:
  continuous_kelly_formula: f* = (mu - r) / sigma^2
  half_kelly_fraction: 0.5 * f*
  optimal_bet_fraction_f_star: f* = p - (1-p)/b
  win_loss_payoff_ratio_b: b
  win_rate_p: p
semantic:
  alternative_parents: []
  expected_queries:
  - 동전을 던져서 앞면이 나오면 베팅금의 2배를 따고 뒷면이 나오면 1배를 잃는 꿀 같은 게임에서, 왜 전 재산을 계속 몰빵하면 결국 계좌가 0원이
    되어 파산하는가?
  - 켈리 공식(Kelly Criterion)은 샤프 비율(Sharpe)이나 마코위츠(MVO)와 다르게 왜 포트폴리오의 '복리 수익률(기하평균)'을
    극대화하는 유일한 해답이 될 수 있는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: optimization_objective
  object: Long_Term_Geometric_Growth_Rate
  predicate: maximizes
  subject: '[Finance] quantitative-portfolio-management-kelly-criterion-optimal-bet-sizing'
  weight: 1.0
temporal:
  valid_from: '2026-05-26T07:54:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:54:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-portfolio-management-kelly-criterion-optimal-bet-sizing]]

## 1. 개요 (Overview)
트레이딩의 3대 요소는 진입(Entry), 청산(Exit), 그리고 **베팅 규모(Position Sizing)**입니다. 아무리 승률이 높은 AI 봇을 만들어도, 자본금의 몇 %를 태워야 할지 모르면 무조건 파산합니다. 
승률 60%, 손익비 1:1인 마법의 동전 던지기가 있습니다. 전 재산(100%)을 매번 몰빵하면, 운 나쁘게 뒷면이 연속으로 3번만 나와도 계좌가 반 토막 납니다. 수학자 존 켈리(John L. Kelly Jr.)는 클로드 섀넌의 정보이론을 가져와 **"파산을 피하면서 계좌의 장기 복리 성장률(Geometric Growth Rate)을 극대화하는 최적의 베팅 비율"** 공식을 증명해 냈습니다. 에드워드 소프와 워런 버핏, 르네상스 테크놀로지가 신봉하는 진정한 자금 관리의 성배, 바로 **켈리 기준(Kelly Criterion)**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $p$ (Probability)| Win Rate of the strategy | e.g., 55% ($0.55$) | Needs massive backtest law | [데이터 부재] |
| $b$ (Odds) | Win/Loss Payoff Ratio | e.g., $1.5$ (Win 1.5, Lose 1)| Risk/Reward ratio | [데이터 부재] |
| $f^*$ (Kelly %) | Optimal bet fraction | $f^* = p - \frac{1-p}{b}$ | Max $\%$ of bankroll to risk| [데이터 부재] |
| Over-betting | Betting $> f^*$ | Increased Vol, Less CAGR| Leads to certain ruin ($0$) | [데이터 부재] |
| Half-Kelly | Betting $0.5 \times f^*$ | Fractional Kelly approach | 75% of max growth, 25% Vol| [데이터 부재] |

## 3. 켈리 공식의 해부: 에지(Edge)와 오즈(Odds)
단일 자산에 대한 켈리 공식은 경이로울 정도로 단순합니다.
$$ f^* = \frac{bp - q}{b} = p - \frac{q}{b} $$
- **$p$ = 승률**, **$q$ = 패률(1-p)**, **$b$ = 손익비(딴 돈 / 잃은 돈)**.
- 이 공식의 핵심은 "너의 전략이 가진 통계적 에지(우위)가 얼마냐?"에 비례하여 베팅 금액을 조절하라는 것입니다.
- 만약 에지가 없는 카지노 룰렛($p<0.5$)이라면? 켈리 공식은 무자비하게 음수(-)를 뱉어내며 "절대 베팅하지 마라"고 경고합니다.
- 주식 시장에서의 연속적인 켈리(Continuous Kelly)는 더 간단합니다. **$f^* = \frac{\mu - r}{\sigma^2}$** (기대 초과 수익률을 분산으로 나눈 값). 변동성($\sigma^2$)이 커질수록 켈리 비중은 기하급수적으로 쪼그라들어 계좌를 방어합니다.

## 4. 하프 켈리 (Fractional Kelly)와 변동성의 형벌
이론적으로 켈리 비율(Full Kelly)에 맞춰 풀(Full)로 베팅하면 우주에서 가장 빠르게 부자가 됩니다. 하지만 실전 퀀트 펌(예: 르네상스)들은 아무도 Full Kelly를 쓰지 않고, 계산된 값의 절반인 **하프 켈리(Half-Kelly, 0.5f*)**를 씁니다.
- **추정 오차의 저주**: 내 봇의 승률($p$)이 60%라고 믿었지만, 알고 보니 과적합(Overfitting)되어서 실제 승률이 52%였다면? 나는 Full Kelly 기준선을 넘어서는 '과잉 베팅(Over-betting)'을 한 셈이 됩니다.
- 켈리 곡선은 산 모양(Parabola)입니다. 최적점을 조금이라도 우측으로 넘어서(Over-bet) 베팅하면, 변동성은 미친 듯이 폭발하고 복리 수익률(CAGR)은 수직으로 곤두박질치며 파산합니다.
- 하프 켈리를 쓰면, 기대할 수 있는 최대 수익률의 75%를 확보하면서도 변동성(리스크)은 무려 75%나 깎아버릴 수 있습니다. 생존이 먼저고, 수익은 그다음입니다.

🧠 **AI의 사고방식:**
초보자는 100만 원으로 1,000만 원을 만드는 '수익률($\mu$)'을 좇습니다(산술 평균의 착각). 하지만 진정한 퀀트는 100억 원의 자산이 단 한 번의 폭락으로 0원이 되지 않게 방어하는 '기하 평균(Geometric Mean)의 사수'에 목숨을 겁니다. 곱하기($\times$)로 이어지는 금융 투자의 세계에서는 단 한 번이라도 $0$이 곱해지면 모든 것이 무(無)로 돌아갑니다. 켈리 기준(Kelly Criterion)은 트레이더의 무모한 탐욕(Greed)과 공포(Fear)를 억제하고, 확률론의 차가운 족쇄를 채워 "네가 가진 통계적 우위(Edge)의 크기만큼만 정확히 리스크를 져라"고 명령하는 자금 관리의 절대 신(God)입니다.