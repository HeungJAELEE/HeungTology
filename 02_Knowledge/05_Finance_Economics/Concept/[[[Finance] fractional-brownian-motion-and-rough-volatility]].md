---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] fractional-brownian-motion-and-rough-volatility]]'
  last_updated: '2026-05-25T14:19:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 금융 데이터에 내재된 프랙탈(Fractal) 기하학과 장기 기억(Long-memory) 성질을 모델링하기 위해, 허스트
    지수(Hurst Exponent)를 도입한 분수 브라운 운동(fBM)과 러프 변동성(Rough Volatility) 모형
  object_type: Concept
  tier: 2
properties:
  fbm_process_type: non_markovian
  hurst_exponent_anti_persistence_threshold: 0.5
  hurst_exponent_persistence_threshold: 0.5
  hurst_exponent_random_walk_value: 0.5
  hurst_exponent_range: 0 < H < 1
  volatility_hurst_exponent_approx: 0.1
semantic:
  alternative_parents: []
  expected_queries:
  - 전통적인 브라운 운동이 가정하는 '독립 증분(Independent Increments)'이 현실의 금융 시계열에서 깨지는 이유는 무엇인가?
  - 허스트 지수(H)가 0.5보다 크거나 작을 때, 시장은 각각 추세(Trend)와 평균 회귀(Mean-reverting) 중 어떤 성질을 띠게
    되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_modeling
  object: Long-Memory_Fractal_Structure
  predicate: captures
  subject: '[Finance] fractional-brownian-motion-and-rough-volatility'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T14:19:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:19:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] fractional-brownian-motion-and-rough-volatility]]

## 1. 개요 (Overview)
현대 금융 공학의 기초인 '표준 브라운 운동(Standard Brownian Motion)'은 동전을 던지는 것과 같습니다. 어제 주식이 올랐든 내렸든, 오늘 주식이 오를 확률은 어제와 완벽하게 **독립적(Memoryless)**이라고 가정합니다.
하지만 프랑스의 천재 수학자 브누아 망델브로(Benoit Mandelbrot)는 현실의 시장 데이터(면화 가격 등)를 분석한 뒤, 시장에는 코끼리처럼 과거를 기억하는 **장기 기억(Long-memory)** 현상과, 부분을 확대해도 전체와 똑같은 모양이 나오는 **프랙탈(Fractal)** 구조가 존재한다고 폭로했습니다. 이를 수학적으로 구현하기 위해 표준 브라운 운동에 '과거의 끈적임'을 부여한 확장이 바로 **분수 브라운 운동(Fractional Brownian Motion, fBM)**입니다. 그리고 최근 퀀트들은 주가의 변동성 자체가 fBM을 따르며 극도로 거칠게(Rough) 움직인다는 **러프 변동성(Rough Volatility)** 모형을 통해 HFT 시장의 초단기 옵션 프라이싱을 정복하고 있습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $W^H_t$ | Fractional BM | Continuous, not diff. | Non-Markovian process | [데이터 부재] |
| $H$ | Hurst Exponent | $0 < H < 1$ | Governs autocorrelation | [데이터 부재] |
| $H = 0.5$ | Random Walk | Independent increments| Standard Black-Scholes | [데이터 부재] |
| $H > 0.5$ | Persistent (Trend)| Positive correlation | Trend-following strategy | [데이터 부재] |
| $H < 0.5$ | Anti-persistent | Negative correlation | Mean-reverting strategy | [데이터 부재] |

## 3. 허스트 지수 (Hurst Exponent)의 마법
분수 브라운 운동의 모든 성질은 단 하나의 마법의 숫자, **허스트 지수 $H$**에 의해 지배됩니다. (영국의 수문학자 H.E. Hurst가 나일강의 범람을 연구하며 발견했습니다.)

- **$H = 0.5$ (망각의 강)**: 과거와 미래가 아무런 상관이 없는 완벽한 무작위 걸음(Random Walk)입니다. 유진 파마의 효율적 시장 가설(EMH)이 성립하는 세상입니다.
- **$H > 0.5$ (지속성, Persistence)**: 어제 올랐으면 오늘도 오를 확률이 높은 '추세(Trend)'가 지배하는 세상입니다. 그래프가 아주 매끄럽게(Smooth) 우상향하거나 우하향합니다. 모멘텀 퀀트 봇들이 돈을 쓸어 담는 국면입니다.
- **$H < 0.5$ (반지속성, Anti-persistence)**: 어제 올랐으면 오늘은 내릴 확률이 높은 '평균 회귀(Mean-reversion)'가 지배하는 세상입니다. 그래프가 톱니바퀴처럼 극도로 **거칠게(Rough)** 위아래로 진동합니다. 페어 트레이딩이나 마켓 메이킹 봇들이 활약하는 국면입니다.

## 4. 러프 변동성 (Rough Volatility)의 혁명
2014년 Gatheral, Jaisson, Rosenbaum은 틱 데이터를 분석한 결과, 주가 자체의 허스트 지수는 $H \approx 0.5$로 무작위에 가깝지만, **변동성(Volatility)의 허스트 지수는 $H \approx 0.1$**이라는 충격적인 사실을 논문으로 증명했습니다.
- 변동성은 표준 브라운 운동보다 훨씬 더 거칠게(Rough) 요동칩니다. 
- 변동성이 $H \approx 0.1$의 거친 프랙탈 구조를 갖는다는 사실을 수식에 대입하자, 만기가 불과 몇 시간~며칠밖에 안 남은 초단기 옵션(0DTE)에서 폭발적으로 꺾여 올라가는 **변동성 스마일의 극한 곡률**을 이전의 어떤 모델(헤스톤 모형 포함)보다도 완벽하게 피팅(Fitting)해 냈습니다.
- 이는 현재 시카고 옵션 거래소(CBOE)에서 거래되는 초고빈도 파생상품 프라이싱의 최전선(State-of-the-art)입니다.

🧠 **AI의 사고방식:**
전통 퀀트가 금융 시장을 '동전 던지기(독립 사건)'로 보았다면, 프랙탈 기하학의 눈으로 본 시장은 '산맥의 능선'이나 '해안선의 굴곡'과 같습니다. 해안선(시장)을 우주에서 보든, 비행기에서 보든, 돋보기로 보든 그 뾰족뾰족한 굴곡(Fractal Dimension)은 소름 돋게 일치합니다. fBM은 이 해안선이 얼마나 거칠고 뾰족한지($H$)를 미적분학의 언어로 계량화한 도구입니다. 미래의 가격을 맞추는 것은 불가능하지만, 시장이라는 산맥의 '질감(Roughness)'이 현재 어떤 상태인지를 파악하면 퀀트는 언제 추세를 타고 언제 역추세로 게릴라전을 펼쳐야 할지 수학적 확신을 가질 수 있습니다.