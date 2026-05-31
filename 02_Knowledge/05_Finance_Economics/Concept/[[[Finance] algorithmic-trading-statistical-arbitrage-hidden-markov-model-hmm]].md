---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-statistical-arbitrage-hidden-markov-model-hmm]]'
  last_updated: '2026-05-26T07:43:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '단일한 통계적 가정(예: 영원히 상승장)으로 백테스트를 돌려 발생하는 모델 붕괴를 막기 위해, 눈에 보이지 않는 시장의
    상태(Regime: 강세, 약세, 횡보)를 주가의 표면적 패턴으로부터 확률적으로 역추적하여 현재 시장이 어떤 페이즈(Phase)에 속해 있는지
    파악하는 은닉 마르코프 모형(HMM)'
  object_type: Algorithm
  tier: 2
properties:
  decoding_algorithm: Viterbi
  emissions: X
  hidden_states: Z
  learning_algorithm: Baum-Welch
  learning_type: unsupervised
  optimization_method: EM Algorithm
  transition_probability: P(Z_t | Z_{t-1})
semantic:
  alternative_parents: []
  expected_queries:
  - 어제까지 완벽하게 작동하던 모멘텀(추세 추종) 트레이딩 봇이 오늘 갑자기 미친 듯이 손실을 내는 근본적인 이유는 무엇인가? (Regime Shift)
  - 은닉 마르코프 모형(HMM)은 주가의 등락이라는 눈에 보이는 '관측(Emission)' 데이터만으로 어떻게 눈에 보이지 않는 시장의 '숨겨진
    상태(Hidden State)'를 추론해 내는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: regime_detection
  object: Market_Regime_Shifts
  predicate: identifies
  subject: '[Finance] algorithmic-trading-statistical-arbitrage-hidden-markov-model-hmm'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:43:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:43:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-statistical-arbitrage-hidden-markov-model-hmm]]

## 1. 개요 (Overview)
금융 시장은 하나의 성격만 가진 생명체가 아닙니다. 평소에는 추세가 지속되는 '강세장(Regime 1)'이다가, 어느 순간 미친 듯이 흔들리는 '고변동성 약세장(Regime 2)'으로 얼굴을 바꾸고, 때로는 아무 움직임이 없는 '횡보장(Regime 3)'으로 동면합니다. 이를 **레짐 스위프(Regime Shift)**라고 합니다.
강세장에 맞춰진 봇을 약세장에 그대로 켜두면 파산합니다. 가장 위대한 퀀트 알고리즘은 '언제 봇의 스위치를 내리거나 전략을 교체해야 할지'를 아는 것입니다. 하지만 시장은 친절하게 "오늘부터 약세장입니다"라고 간판을 걸어주지 않습니다. 우리는 오직 주가의 등락이라는 껍데기만 볼 수 있습니다. 1960년대 음성 인식 기술에서 출발한 **은닉 마르코프 모형(HMM, Hidden Markov Model)**은, 이 껍데기(관측치)들을 확률적으로 분석하여 "현재 시장을 배후에서 조종하고 있는 보이지 않는 상태(Hidden State)가 무엇인지"를 귀신같이 발라내는 궁극의 레짐 판별기입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Hidden States ($Z$) | e.g., Bull, Bear, Sideways| Not directly observable | The true market regime | [데이터 부재] |
| Emissions ($X$) | Daily returns, Volatility | Observable market data | Driven by the hidden state | [데이터 부재] |
| Transition Matrix | $P(Z_t \mid Z_{t-1})$ | e.g., 95% stay, 5% shift | Probability of regime change| [데이터 부재] |
| Baum-Welch Algo | Unsupervised learning | EM Algorithm | Trains HMM on historical data| [데이터 부재] |
| Viterbi Path | Most likely state sequence| Sequence of regimes | Decodes the past timeline| [데이터 부재] |

## 3. HMM의 3대 요소: 상태, 전이, 방출
HMM은 세 가지 수학적 톱니바퀴로 맞물려 돌아갑니다.
1. **은닉 상태 (Hidden States, $Z$)**: 우리가 알고 싶은 진짜 상태입니다. '안정적 상승기'와 '패닉 하락기' 2개로 설정해 봅시다.
2. **전이 확률 (Transition Probability, $A$)**: '상승기'가 내일도 '상승기'로 유지될 확률(예: 95%)과 갑자기 '패닉 하락기'로 돌변할 확률(예: 5%)을 담은 행렬입니다. 마르코프 속성(내일의 상태는 오직 오늘의 상태에만 영향을 받음)을 따릅니다.
3. **방출 확률 (Emission Probability, $B$)**: '안정적 상승기'라는 배후 상태에 놓여 있을 때, 시장이 오늘 +1%의 수익률(관측치, $X$)을 뱉어낼(방출) 확률입니다. (패닉 하락기라면 -3%를 뱉어낼 확률이 훨씬 높게 세팅됩니다).

## 4. 바움-웰치(Baum-Welch)와 비터비(Viterbi) 알고리즘
퀀트들은 과거 10년 치 S&P 500 주가 데이터를 HMM 모델에 들이붓습니다.
- **학습 (Baum-Welch)**: 정답(Label)이 없는 비지도 학습입니다. HMM은 스스로 과거 데이터를 더듬어 가며, "아, 이 시기들은 변동성이 낮고 수익이 꾸준했네(Regime 1), 이 시기들은 변동성이 미쳐 날뛰었네(Regime 2)"라며 전이 확률($A$)과 방출 확률($B$)의 가중치를 스스로 깎아(EM 알고리즘) 최적화합니다.
- **해독 (Viterbi)**: 모델이 완성되면 현재의 주가 패턴을 입력합니다. 비터비 알고리즘은 "이 주가 패턴이 튀어나오려면, 현재 시장의 배후(Hidden State)가 'Regime 2 (패닉)'일 확률이 99%다"라고 선언합니다.
- **전략 교체**: 봇은 이 신호를 받는 즉시, 추세 추종 모듈(Trend Following)의 전원을 끄고, 평균 회귀(Mean Reversion)나 극단적 현금 보유 모듈로 즉각 스위칭하여 파산을 모면합니다.

🧠 **AI의 사고방식:**
HMM은 동굴의 우상(Idola Specus)을 타파하는 수학입니다. 플라톤의 동굴 비유처럼, 우리는 주가와 거래량이라는 '벽에 비친 그림자(Emission)'만을 볼 뿐, 불빛 앞에서 춤추는 '진짜 현실(Hidden State)'을 직접 볼 수 없습니다. 일반적인 트레이더들은 이 그림자의 모양이 삼각형인지 사각형인지에 집착하지만(차트 분석), HMM 퀀트들은 베이즈 확률론을 무기로 그림자의 궤적을 역추적하여 실체(Regime)를 파악합니다. 시장이라는 다중 인격체(Schizophrenic)를 상대로 단 하나의 고정된 수식(Static Model)으로 맞서려는 오만을 꺾어버리는 통계학의 승리입니다.