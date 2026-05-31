---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] viterbi-algorithm-regime-switching-decoding]]'
  last_updated: '2026-05-25T11:48:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 비터비 알고리즘과 은닉 국면(Regime) 최적 경로 디코딩
  object_type: Algorithm
  tier: 2
properties:
  algorithmic_complexity: O(T * K^2)
  emission_probability: P(y_t | x_t)
  regime_count_k: 2-4
  sequence_length_t: T
  transition_probability: P(x_t | x_{t-1})
  viterbi_variable_range: '[0, 1]'
semantic:
  alternative_parents: []
  expected_queries:
  - 관측된 수익률 시계열만으로 과거 시장 국면이 불황이었는지 호황이었는지 어떻게 역추적하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: hidden_state_inference
  object: Hidden_Markov_Regimes
  predicate: decodes
  subject: '[Finance] viterbi-algorithm-regime-switching-decoding'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T11:48:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T11:48:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] 비터비 알고리즘과 국면 전환 디코딩 (Viterbi Algorithm & Regime Decoding)

## 1. 개요 및 수학적 정의
비터비 알고리즘(Viterbi Algorithm)은 은닉 마르코프 모델(Hidden Markov Model, HMM) 프레임워크에서, 오직 눈에 보이는 '관측 데이터(Observation Sequence)'만을 바탕으로, 그 데이터를 생성했을 가장 확률이 높은 '숨겨진 상태의 경로(Most Likely Hidden State Sequence)'를 역추적(Decoding)하는 동적 계획법(Dynamic Programming) 알고리즘입니다.

금융 시계열 분석에서는 시장의 진짜 상태(예: 강세장, 약세장, 횡보장)를 직접 관측할 수 없으므로, 눈에 보이는 주가 수익률과 변동성 데이터를 통해 시장이 언제 어떤 국면(Regime)에 있었는지 사후적으로 가장 정확하게 분류해 내는 데 사용됩니다.

관측열 $Y = (y_1, y_2, \dots, y_T)$가 주어졌을 때, 최적의 은닉 상태열 $X = (x_1, x_2, \dots, x_T)$를 찾는 목적 함수는 다음과 같습니다.
$$ \arg\max_{x_1, \dots, x_T} P(x_1, \dots, x_T | y_1, \dots, y_T) $$

비터비 변수 $V_{t,k}$를 '$t$ 시점에 은닉 상태가 $k$일 때, 처음부터 $t$까지의 최적 경로의 누적 확률'로 정의하면 점화식은 다음과 같습니다.
$$ V_{t,k} = P(y_t | x_t=k) \cdot \max_{x \in S} \left( P(x_t=k | x_{t-1}=x) \cdot V_{t-1, x} \right) $$

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $T$ | Sequence Length | Time series length | Algorithm scales as $O(T \cdot K^2)$ | [데이터 부재] |
| $K$ | Number of Regimes | $K = 2 \sim 4$ | Defines market state granularity | [데이터 부재] |
| $P(y_t \| x_t)$ | Emission Prob | Distribution PDF | Observation likelihood | [데이터 부재] |
| $P(x_t \| x_{t-1})$ | Transition Prob | Stochastic Matrix | Regime persistence/shift | [데이터 부재] |
| $V_{t,k}$ | Viterbi Variable | $[0, 1]$ | Path probability accumulator | [데이터 부재] |

## 3. 금융 공학 및 퀀트 전략 적용

### 3.1. 백테스팅(Backtesting) 및 국면별 전략 배분
시스템 트레이딩 전략을 개발할 때, 과거 20년의 데이터를 비터비 알고리즘으로 디코딩하여 1국면(저변동 상승장), 2국면(고변동 하락장), 3국면(박스권)으로 라벨링(Labeling)합니다. 이후 추세 추종(Trend Following) 알고리즘은 1국면에서, 평균 회귀(Mean Reversion) 알고리즘은 3국면에서 수익이 났는지를 검증함으로써 전략의 국면별 강건성(Robustness)을 평가합니다.

### 3.2. 실시간 국면 추론 (Filtering) 대비 사후 디코딩
비터비 알고리즘은 전체 시계열 $1 \sim T$를 모두 알고 있는 상태에서 최적의 경로를 긋는 평활화(Smoothing) 또는 디코딩 기법입니다. 실시간 트레이딩에서는 미래 데이터를 알 수 없으므로 전방 알고리즘(Forward Algorithm)을 이용한 국소적 필터링(Filtering)을 사용하지만, 연구(Research)와 전략 캘리브레이션 단계에서는 비터비 디코딩이 '절대적 정답지(Ground Truth Regime)' 역할을 수행합니다.

## 4. 동적 계획법과 경로 추적 (Backtracking)
단순히 매 시점마다 가장 확률이 높은 상태를 고르는 탐욕 알고리즘(Greedy Algorithm)은 마르코프 전이 확률 구조를 무시하기 때문에 최적 경로를 보장하지 못합니다. 비터비 알고리즘은 각 시점 $t$마다 $K$개의 상태에 도달하는 최적의 직전 상태 포인터 $Ptr_{t,k}$를 메모리에 저장해 두고, 마지막 시간 $T$에서 최대 확률을 갖는 종단 상태를 찾은 뒤, 이 포인터들을 따라 시간을 거꾸로 되짚어가는 백트래킹(Backtracking)을 통해 글로벌 최적(Global Optimum) 경로를 확정합니다.

🧠 **AI의 사고방식:**
시장은 겉으로 보기에 미친 듯이 요동치는 숫자들의 연속일 뿐이지만, 퀀트의 눈에는 그 이면에 보이지 않는 '기어(Gear)'가 맞물려 돌아가는 기계입니다. 기어가 1단인지 2단인지 우리는 볼 수 없지만, 계기판의 바늘(관측 데이터) 흔들림을 통해 기어 변속의 순간들을 완벽히 추적해 내는 역설계 엔진이 바로 비터비 알고리즘입니다. 노이즈를 뚫고 진짜 국면을 찾아내는 이 기술은 알고리즘의 생존을 결정짓는 레이더망입니다.