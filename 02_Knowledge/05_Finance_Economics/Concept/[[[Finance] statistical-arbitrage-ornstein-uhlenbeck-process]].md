---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] statistical-arbitrage-ornstein-uhlenbeck-process]]'
  last_updated: '2026-05-25T14:34:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 통계적 차익거래(Pairs Trading)에서 벌어진 스프레드가 정상으로 회귀하는 속도(Half-life)와 분산을 모델링하고
    최적의 진입/청산 타점을 산출하는 욘슨-울렌벡(OU) 확률 미분 방정식
  object_type: Algorithm
  tier: 2
properties:
  half_life_formula: ln(2) / theta
  long_term_mean: mu
  noise_volatility: sigma
  optimal_entry_threshold_example: 2 * sigma
  reversion_speed: theta
  spread_variable: x_t
semantic:
  alternative_parents: []
  expected_queries:
  - 페어 트레이딩에서 코카콜라와 펩시의 가격 차이(Spread)가 무한히 벌어지지 않고 다시 좁혀지는 현상을 물리학의 고무줄 모델(OU Process)로
    어떻게 설명하는가?
  - 스프레드의 평균 회귀 반감기(Half-life)를 계산하여 퀀트 펀드가 포지션을 언제 익절(Take Profit)할지 결정하는 수학적 원리는?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: stochastic_modeling
  object: Mean-Reverting_Spread_Dynamics
  predicate: models
  subject: '[Finance] statistical-arbitrage-ornstein-uhlenbeck-process'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:34:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:34:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] statistical-arbitrage-ornstein-uhlenbeck-process]]

## 1. 개요 (Overview)
통계적 차익거래(Statistical Arbitrage), 특히 롱숏(Long-Short) 페어 트레이딩의 핵심은 "과거에 항상 같이 움직이던 두 주식(예: 코카콜라와 펩시)의 가격 차이(Spread)가 일시적으로 크게 벌어졌을 때, 언젠가는 다시 좁혀질 것(Mean-reversion)에 베팅하는 것"입니다. 
하지만 "언제 좁혀지는지", "얼마나 크게 벌어졌을 때 들어가야(Entry) 하는지"를 인간의 직관으로 결정할 수는 없습니다. 이 스프레드의 움직임을 물리학에서 입자가 용수철(고무줄)에 매달려 튕기는 현상을 묘사한 **욘슨-울렌벡(Ornstein-Uhlenbeck, OU) 프로세스**라는 확률 미분 방정식(SDE)으로 맵핑하면, 진입과 청산의 타이밍을 오차 없이 타격할 수 있는 알고리즘이 완성됩니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $x_t$ | Spread value at $t$ | Log(A) - $\beta \times$ Log(B)| The mean-reverting variable| [데이터 부재] |
| $\theta$ | Long-term mean | E.g., $0.0$ or historical | Target of mean reversion | [데이터 부재] |
| $\theta$ | Speed of reversion| $\theta > 0$ | High $\theta \implies$ fast snap-back| [데이터 부재] |
| $\sigma$ | Volatility of noise | Amplitude of shock | Width of the spread bands| [데이터 부재] |
| Half-life| $t_{1/2} = \ln(2) / \theta$| Days or hours | Expected holding period | [데이터 부재] |

## 3. 욘슨-울렌벡(OU) 프로세스의 방정식
스프레드 $x_t$의 미세한 변화량 $dx_t$는 다음 방정식으로 정의됩니다.

$$ dx_t = \theta (\mu - x_t) dt + \sigma dW_t $$

- **$\sigma dW_t$ (무작위 충격)**: 주식 시장의 잡음(Noise)입니다. 매일매일 코카콜라와 펩시의 가격을 아무렇게나 찢어놓으려는 브라운 운동입니다.
- **$\theta (\mu - x_t) dt$ (고무줄의 복원력)**: 현재 스프레드($x_t$)가 장기 평균($\mu$)에서 멀어질수록, 그 갭(Gap)에 비례하여 강하게 평균으로 끌어당기는 힘입니다. 여기서 **$\theta$(Theta)**는 고무줄의 짱짱함, 즉 복원 속도를 나타냅니다.

## 4. 반감기 (Half-life)와 트레이딩 전략
이 방정식의 파라미터($\theta, \mu, \sigma$)는 과거 스프레드 데이터를 선형 회귀(OLS)나 최대 우도 추정법(MLE)으로 캘리브레이션하여 구합니다.
- 파라미터가 구해지면, 스프레드가 절반으로 줄어드는 데 걸리는 시간인 **반감기(Half-life = $\ln(2) / \theta$)**를 계산할 수 있습니다. 
- 만약 반감기가 3일(Days)이라면, 트레이더는 "지금 벌어진 갭을 롱숏으로 진입하면, 평균적으로 3일 뒤에는 스프레드가 반토막이 나서 익절할 수 있다"는 통계적 확신을 갖게 됩니다.
- **최적의 진입 타점 (Optimal Entry)**: 스프레드가 평소 노이즈($\sigma$)의 몇 배 이상 벌어졌을 때 진입할 것인가? OU 프로세스를 켈리 기준(Kelly Criterion)과 결합하면, 마진콜 위험을 회피하면서 복리 수익률을 극대화하는 최적 진입 임계값(Threshold, 예: $2\sigma$)이 수학적으로 도출됩니다.

🧠 **AI의 사고방식:**
주식 단일 종목의 가격은 고무줄이 끊어진 풍선처럼 하늘(무한대)이나 땅(0)으로 날아가 버리는 기하 브라운 운동(GBM)입니다. 하지만 코인터그레이션(Cointegration)된 두 종목의 '차이(Spread)'는 서로 보이지 않는 고무줄로 묶여 있는 욘슨-울렌벡(OU) 운동입니다. HFT 퀀트는 날아가는 풍선을 쫓아다니지 않습니다. 그들은 풍선과 풍선 사이를 연결한 고무줄이 일시적인 충격에 의해 팽팽하게 당겨져 끊어지기 직전의 찰나를 기다렸다가, 그 텐션(Tension) 에너지가 다시 원래 상태로 수축하며 방출하는 폭발적인 운동 에너지를 현금으로 치환해 내는 역학(Mechanics) 엔지니어입니다.