---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] macro-quant-regime-switching-hidden-markov-models]]'
  last_updated: '2026-05-25T14:58:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 현재 금융 시장이 강세장(Bull), 약세장(Bear), 혹은 횡보장인지 인간의 자의적 판단이 아닌, 데이터에 숨겨진 잠재
    상태(Latent State)를 확률적으로 추론하여 포트폴리오를 다이나믹하게 스위칭하는 은닉 마르코프 모델(HMM) 기반 국면 전환 프레임워크
  object_type: Algorithm
  tier: 2
properties:
  baum_welch_algorithm_use: parameter_estimation
  emission_probability_b: n(mu_i, sigma_i^2)
  state_1_mu: 0.1
  state_1_sigma: 0.15
  state_2_mu: -0.2
  state_2_sigma: 0.4
  transition_matrix_a: p(z_t+1=j|z_t=i)
  viterbi_algorithm_use: state_decoding
  x_t_observed_data:
  - returns
  - vix
  - spreads
  z_t_hidden_state: latent
semantic:
  alternative_parents: []
  expected_queries:
  - 경제 지표나 주가 데이터만을 보고, 현재 시장이 '평온한 상태'에서 '위기 상태(Crisis)'로 넘어갔다는 것을 HMM 알고리즘은 어떻게
    찾아내는가?
  - 마르코프 국면 전환(Regime Switching) 모형에서 추출된 전이 확률 행렬(Transition Matrix)은 퀀트 포트폴리오 배분에
    어떻게 활용되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: regime_identification
  object: Latent_Market_Regimes
  predicate: identifies
  subject: '[Finance] macro-quant-regime-switching-hidden-markov-models'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:58:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:58:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] macro-quant-regime-switching-hidden-markov-models]]

## 1. 개요 (Overview)
금융 시장은 영원히 똑같은 성질을 유지하지 않습니다. 어느 해에는 주가가 조금씩 꾸준히 오르는 평온한 상승장(Low Volatility Bull Market)이다가, 갑자기 모기지 사태가 터지면 주가가 미친 듯이 요동치며 폭락하는 발작장(High Volatility Bear Market)으로 성질이 완전히 돌변합니다. 이를 **국면(Regime)**이라고 부릅니다.
초보 투자자는 "어제 많이 떨어졌으니 오늘이 바닥이겠지"라며 상승장의 논리로 폭락장에 물타기를 하다가 파산합니다. 거시 퀀트(Macro Quant)들은 인간의 편향된 감각을 배제하고, 현재 시장이 어느 국면에 속해 있는지를 오직 수학적 확률로만 판별하기 위해 머신러닝의 **은닉 마르코프 모델(Hidden Markov Model, HMM)**을 도입하여 실시간으로 펀드의 전략 모드를 스위칭(Regime-switching)합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $Z_t$ | Hidden Regime State | E.g., State 1 or 2 | Unobservable (Latent) | [데이터 부재] |
| $X_t$ | Observed Market Data | Returns, VIX, Spreads | Emitted from $Z_t$ | [데이터 부재] |
| $A$ | Transition Matrix | $P(Z_{t+1}=j \| Z_t=i)$ | Stays in state $i$ typically| [데이터 부재] |
| $B$ | Emission Probability | $N(\mu_i, \sigma_i^2)$ | Depends on hidden state | [데이터 부재] |
| Viterbi Alg | State decoding | Sequence of states | Most likely path of $Z_t$| [데이터 부재] |

## 3. 은닉 마르코프 모델(HMM)의 아키텍처
HMM은 다음과 같은 두 가지 계층으로 이루어져 있습니다.
1. **숨겨진 상태 (Latent States, $Z_t$)**: 시장의 진짜 '기분'입니다(예: 평온 1, 발작 2). 우리는 이 기분을 직접 눈으로 볼 수 없습니다.
2. **관측 가능한 데이터 (Observations, $X_t$)**: 우리가 매일 HTS에서 보는 S&P 500 수익률, VIX 지수, 하이일드 스프레드 등입니다. 이 데이터들은 시장의 '기분'이 기침처럼 겉으로 뱉어낸(Emission) 결과물일 뿐입니다.

### 3.1. 가우시안 혼합 (Gaussian Emission)
- **상태 1 (평온 국면)**: 컴퓨터가 데이터를 뜯어보니, 평균($\mu_1$)이 +10%이고 변동성($\sigma_1$)이 15%인 정규분포를 따릅니다.
- **상태 2 (발작 국면)**: 평균($\mu_2$)이 -20%이고 변동성($\sigma_2$)이 40%로 폭발하는 정규분포를 따릅니다.
- HMM 알고리즘(바움-웰치 알고리즘)은 과거 20년 치 데이터를 통째로 삼킨 뒤, 이 두 개의 숨겨진 정규분포를 찾아내고, 상태 1에서 2로 넘어갈 전이 확률(Transition Matrix)을 찾아냅니다.

## 4. 실시간 확률 추론과 포트폴리오 스위칭
가장 중요한 것은 실시간 트레이딩 적용입니다. 오늘 S&P 500이 -3% 폭락했습니다.
- 인간: "그냥 일시적 조정장이야."
- HMM(전향 알고리즘 연산): "오늘의 폭락 데이터($X_t$)가 들어왔을 때, 현재 시장이 '발작 국면(상태 2)'일 사후 확률(Posterior Probability)이 어제 5%에서 오늘 85%로 치솟았습니다."
- 이 확률이 임계치를 넘는 순간, 퀀트 알고리즘은 즉시 국면 전환(Regime Switch)을 선언합니다. 주식 비중을 강제로 축소하고 모멘텀 전략을 가동 정지시키며, 변동성 롱(Long Vol) 포지션이나 채권 비중을 극대화하는 '방어 모드'로 시스템을 완전히 재부팅(Re-weighting)합니다.

🧠 **AI의 사고방식:**
HMM은 벽 너머에 있는 괴물(시장)의 정체를 파악하는 프로파일링 수학입니다. 괴물이 벽을 부수고 나타날 때까지 기다리면(사후 확인) 이미 우리는 죽어 있습니다. 우리는 벽 너머에서 들려오는 발소리의 간격이나 숨소리의 거친 정도(관측 데이터 $X_t$)만을 듣고, 베이즈 정리(Bayes' Theorem)를 통해 괴물이 지금 자고 있는지, 아니면 사냥을 준비하며 몸을 일으켰는지(숨겨진 상태 $Z_t$)를 통계적으로 프로파일링해야 합니다. HMM은 개미들의 막연한 공포를 냉정한 0~1 사이의 확률값으로 변환하여, 포트폴리오의 안전핀을 가장 완벽한 타이밍에 뽑아버리는 거시 경제의 조기 경보 레이더입니다.