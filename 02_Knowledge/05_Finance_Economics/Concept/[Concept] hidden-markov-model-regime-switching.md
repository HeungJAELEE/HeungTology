---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] hidden-markov-model-regime-switching]]'
  last_updated: '2026-05-25T11:08:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Hidden Markov Models for market regime switching detection
  object_type: Algorithm
  tier: 2
properties:
  covariance_parameter: sigma_k
  emission_probability: B
  hidden_state: Z_t
  kelly_fraction: position_sizing_parameter
  mean_parameter: mu_k
  observed_asset_returns: X_t
  transition_matrix: A
semantic:
  alternative_parents: []
  expected_queries:
  - 은닉 마르코프 모델을 사용하여 시장의 상승/하락 국면을 어떻게 추정하는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: regime_detection
  object: Market_Regime
  predicate: detects
  subject: '[Finance] hidden-markov-model-regime-switching'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:08:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:08:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🔄 [Concept] 은닉 마르코프 모델(HMM) 기반 국면 전환

## 1. 다중 국면(Regime) 시계열의 한계 돌파
금융 시계열은 거시 경제 사이클이나 충격에 따라 상승장(Bull), 하락장(Bear), 횡보장(Sideways) 등 근본적인 구조(Regime)가 전환됩니다. 은닉 마르코프 모델(HMM, Hidden Markov Model)은 우리가 관측할 수 없는 '숨겨진 시장 상태(Hidden State, $Z_t$)'가 존재하며, 관측되는 자산 수익률 $X_t$는 이 숨겨진 상태에 종속되어 발생(Emission)한다고 가정합니다.

## 2. HMM의 수학적 구성 요소
1. **전이 확률 행렬 (Transition Matrix, $A$)**: 상태 $i$에서 상태 $j$로 전환될 확률. 마르코프 성질(미래 상태는 오직 현재 상태에만 의존)을 따릅니다.
   $$ a_{ij} = P(Z_{t+1} = j | Z_t = i) $$
2. **방출 확률 분포 (Emission Probability, $B$)**: 현재 시장 국면이 $k$일 때, 관측된 자산 수익률 $X_t$가 발생할 조건부 확률 밀도. 일반적으로 정규 분포를 가정합니다.
   $$ P(X_t | Z_t = k) \sim \mathcal{N}(\mu_k, \Sigma_k) $$

## 3. 알고리즘 트레이딩으로의 응용
퀀트 시스템은 **바움-웰치 알고리즘(Baum-Welch Algorithm)**과 같은 기댓값 최대화(EM) 기법을 사용하여, 관측된 과거 데이터로부터 전이 행렬 $A$와 각 국면의 $\mu_k, \Sigma_k$ 파라미터를 역추정(Calibration)합니다. 

이후 새로운 가격 데이터가 들어오면 **비터비 알고리즘(Viterbi Algorithm)**을 통해 "현재 시장이 폭락 국면(High Volatility Regime)에 진입했을 확률"을 실시간 연산하고, 확률이 임계치를 초과하면 시스템의 포지션 사이즈(Kelly Fraction)를 기계적으로 $0$으로 강제 청산(De-risking)합니다.