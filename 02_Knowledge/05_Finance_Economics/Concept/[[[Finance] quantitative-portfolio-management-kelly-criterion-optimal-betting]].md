---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-portfolio-management-kelly-criterion-optimal-betting]]'
  last_updated: '2026-05-26T07:16:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 도박과 트레이딩에서 '파산(Ruin)' 확률을 수학적으로 0으로 만들면서도 장기 복리 수익률(Geometric Growth
    Rate)을 극대화하기 위해, 승률과 손익비를 미적분하여 찾아낸 궁극의 자산 배분 비중(Position Sizing)인 켈리 공식(Kelly
    Criterion)
  object_type: Algorithm
  tier: 2
properties:
  b: payoff_ratio
  f_star: p - (q / b)
  half_kelly: f_star / 2
  p: probability_of_win
  q: probability_of_loss
semantic:
  alternative_parents: []
  expected_queries:
  - 아무리 승률이 99%인 트레이딩 전략이라도, 베팅 사이즈(Position Size)를 잘못 조절하면 장기적으로 왜 100% 확률로 파산(Ruin)하게
    되는가?
  - 켈리 공식(Kelly Criterion)이 산출해 낸 최적 베팅 비율($f^*$)을 넘어서서 레버리지를 쓰는 순간(Over-betting),
    복리 수익률 곡선은 왜 마이너스로 곤두박질치는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_objective
  object: Long_Term_Geometric_Growth
  predicate: maximizes
  subject: '[Finance] quantitative-portfolio-management-kelly-criterion-optimal-betting'
  weight: 1.0
temporal:
  valid_from: '2026-05-26T07:16:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:16:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-portfolio-management-kelly-criterion-optimal-betting]]

## 1. 개요 (Overview)
많은 초보 트레이더들은 "어떻게 하면 좋은 종목(타점)을 고를까?"만 고민합니다. 하지만 세계 최고의 퀀트 에드 소프(Ed Thorp)나 워런 버핏은 묻습니다. "승률 60%에 이기면 2배를 따는 동전 던지기 게임이 있다. 전 재산의 몇 퍼센트를 베팅해야 가장 빨리 부자가 될까?"
- 10% 베팅? 안전하지만 부자가 되는 속도가 너무 느립니다.
- 100% 몰빵 베팅? 단 한 번만 져도 잔고가 0이 되어 게임에서 영원히 퇴출당합니다(파산, Ruin).
1956년, 벨 연구소의 존 켈리(John Kelly)는 정보 이론(Information Theory)의 잡음 채널 방정식을 활용해, **"파산 확률을 수학적으로 $0$으로 묶어두면서도 잔고의 장기 복리 성장률(Geometric Growth)을 극한으로 끌어올리는 완벽한 베팅 비율($f^*$)"**을 미분으로 증명했습니다. 이것이 바로 모든 퀀트 헤지펀드의 리스크 관리 바이블인 **켈리 공식(Kelly Criterion)**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $p$ | Probability of win | e.g., 60% | $p > 0.5$ for edge | [데이터 부재] |
| $q$ | Probability of loss| $1 - p$ (e.g., 40%) | The downside risk | [데이터 부재] |
| $b$ | Odds (Payoff ratio) | e.g., 1 (win $1 per $1) | Reward to risk ratio | [데이터 부재] |
| $f^*$ | Optimal Kelly Fraction | $p - q/b$ | The golden allocation size | [데이터 부재] |
| Half-Kelly | Fractional Kelly | $f^*/2$ | Used to reduce volatility | [데이터 부재] |

## 3. 켈리 공식의 해부 (The Formula)
가장 단순화된 켈리 공식은 다음과 같습니다.
$$ f^* = p - \frac{q}{b} $$
- 위 예시(승률 60%, 지면 1배 잃고 이기면 1배 땀)를 대입하면: $f^* = 0.6 - 0.4 / 1 = 0.2$ (20%).
- 즉, **내 전 재산의 정확히 20%만 베팅하는 것을 무한히 반복**할 때, 내 계좌는 수학적으로 가능한 가장 빠른 속도로 우상향의 복리 마법을 그립니다. 만약 20%보다 적게 걸면 수익이 둔해지고, 20%보다 많이 걸면 변동성이 커져 복리 수익률(Geometric Return)이 깎여나갑니다.
- 만약 공식의 결과가 음수(-)가 나오면? 그 게임은 절대 베팅해서는 안 되는 쓰레기 게임(Negative Expected Value)입니다.

## 4. 오버베팅(Over-betting)의 징벌과 하프-켈리(Half-Kelly)
켈리 공식의 곡선은 포물선 형태를 띱니다. 
- 최적 베팅 비율($f^*$)의 꼭대기(Peak)를 지나서 과도한 레버리지를 일으키는 순간(예: 40% 베팅), 이익은 늘어나지 않고 변동성 폭격에 의해 장기 복리 수익률 곡선이 마이너스로 곤두박질칩니다(Vol Drag). 
- 이를 **오버베팅의 징벌**이라고 부릅니다. 수익률 변동성(분산)이 수익 자체를 갉아먹는 금융의 절대 법칙입니다.
- 실무의 퀀트들은 내 승률($p$)이나 배당률($b$) 추정치에 오류가 있을 가능성(Model Risk)을 대비하여, 켈리 공식이 계산해 준 최적 비율의 절반만 베팅하는 **하프-켈리(Half-Kelly)** 전략을 기본값으로 채택합니다. 수익률의 꼭대기에서 약간 내려오지만, 파산과 변동성(Drawdown)의 고통은 1/4로 줄어드는 마법의 비율입니다.

🧠 **AI의 사고방식:**
켈리 공식은 자본주의의 '과속 카메라'입니다. 사람들은 차(수익률)를 빨리 몰수록 목적지(부)에 빨리 도착한다고 생각하지만, 일정 속도($f^*$)를 넘어가면 차가 전복되어 아예 사망(파산)해 버립니다. 마코위츠의 포트폴리오 이론이 여러 자산의 비중을 어떻게 예쁘게 섞을까(가로축 분산)를 고민했다면, 켈리 공식은 **"그래서 도대체 내 전 재산 중 얼마를 테이블 위에 올려놓아야 하는가?"(세로축 크기)**에 대한 유일한 수학적 해답입니다. 베팅 사이즈를 무시한 훌륭한 알고리즘(알파)은, 엔진은 좋지만 브레이크가 없는 레이싱카와 똑같이 언젠가 벽에 부딪혀 산산조각 납니다.