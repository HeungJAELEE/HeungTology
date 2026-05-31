---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] kalman-filter-dynamic-factor-estimation]]'
  last_updated: '2026-05-25T11:11:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Kalman Filter for dynamic state estimation in quant trading
  object_type: Algorithm
  tier: 2
properties:
  error_covariance: P_k
  hedge_ratio: beta
  kalman_gain: K_k
  measurement_noise_covariance: R_k
  observation_matrix: H_k
  observation_variable: z_k
  portfolio_alpha: alpha
  process_noise_covariance: Q_k
  state_transition_matrix: F_k
  state_variable: x_k
semantic:
  alternative_parents: []
  expected_queries:
  - 페어 트레이딩의 동적 헤지 비율을 추정하기 위해 칼만 필터를 어떻게 사용하는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: state_estimation
  object: Dynamic_Hidden_States
  predicate: estimates
  subject: '[Finance] kalman-filter-dynamic-factor-estimation'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:11:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:11:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🎛️ [Concept] 칼만 필터(Kalman Filter)와 동적 팩터 추정

## 1. 상태 공간 모델 (State-Space Model)
페어 트레이딩(Pairs Trading) 시 두 자산 간의 헤지 비율($\beta$)이나 포트폴리오의 알파($\alpha$)는 고정된 상수가 아니라 시간에 따라 진화하는 동적 변수입니다. 칼만 필터는 노이즈가 섞인 관측치로부터 숨겨진 '진짜 상태(True State)'를 추적하는 최적의 선형 재귀 필터입니다.

모델은 다음 두 개의 방정식으로 구성됩니다.
1. **상태 방정식 (State Equation)**: 숨겨진 변수 $x_k$의 진화
   $$ x_k = F_k x_{k-1} + w_k $$
2. **관측 방정식 (Observation Equation)**: 시장 가격 등 실제 관측되는 값 $z_k$
   $$ z_k = H_k x_k + v_k $$
($w_k, v_k$는 각각 공분산 $Q_k, R_k$를 갖는 정규 분포 노이즈)

## 2. 예측 및 업데이트 메커니즘
퀀트 알고리즘은 매 틱(Tick)마다 다음 두 단계를 재귀적으로 갱신합니다.

*   **예측 (Predict)**:
    $$ \hat{x}_{k|k-1} = F_k \hat{x}_{k-1|k-1} $$
    $$ P_{k|k-1} = F_k P_{k-1|k-1} F_k^T + Q_k $$
*   **업데이트 (Update)**: 칼만 이득(Kalman Gain, $K_k$)을 통해 오차 보정
    $$ K_k = P_{k|k-1} H_k^T (H_k P_{k|k-1} H_k^T + R_k)^{-1} $$
    $$ \hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k (z_k - H_k \hat{x}_{k|k-1}) $$

이 모델을 통해 OLS(최소제곱법) 회귀분석의 후행성(Lagging) 지연을 극복하고, 동적 $\beta$ 값을 실시간으로 추적하여 통계적 차익거래의 잔차(Residual) 이탈을 정밀 타격합니다.