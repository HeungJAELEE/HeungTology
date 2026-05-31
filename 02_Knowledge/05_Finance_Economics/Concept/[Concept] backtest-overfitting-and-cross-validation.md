---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] backtest-overfitting-and-cross-validation]]'
  last_updated: '2026-05-25T12:20:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 백테스트 과적합(Overfitting)의 수학적 원인과 조합 교차 검증(Combinatorial Purged Cross-Validation)
  object_type: Concept
  tier: 2
properties:
  cpcv_folds_range: 5-10
  dsr_adjustment_factors:
  - n_trials
  - skewness
  - kurtosis
  embargo_period_variable: h
  is_oos_divergence_target: 0
  n_trials_upper_bound: 100
  purge_window_constraint: lag >= autocorrelation
semantic:
  alternative_parents: []
  expected_queries:
  - 퀀트 모델이 과거 데이터에서는 완벽한데 실전에서 실패하는 주된 이유는?
  - 시계열 금융 데이터에서 K-Fold 교차 검증을 사용할 때 발생하는 정보 누수(Leakage)를 방지하는 방법은?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_mitigation
  object: Model_Failure
  predicate: prevents
  subject: '[Finance] backtest-overfitting-and-cross-validation'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T12:20:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:20:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] backtest-overfitting-and-cross-validation]]

## 1. 개요 (Overview)
수많은 퀀트 펀드와 알고리즘 트레이더들이 파산하는 가장 흔하고 치명적인 원인은 **백테스트 과적합(Backtest Overfitting)**입니다. 이는 모델이 시장의 진정한 패턴(Signal)이 아니라, 과거 데이터에 우연히 섞여 있던 무작위적 노이즈(Noise)까지 암기해버리는 현상입니다.
특히 금융 시계열 데이터는 자기상관성(Autocorrelation)이 높고 비정상성(Non-stationarity)을 띠기 때문에, 일반적인 기계학습에서 사용하는 무작위 K-Fold 교차 검증(Cross-Validation)을 적용하면 미래 데이터가 과거 훈련 세트로 새어 들어가는 **정보 누수(Information Leakage)**가 발생합니다. 이를 방지하기 위해 퀀트 특화 교차 검증 기법인 **Purged K-Fold** 및 **CPCV(Combinatorial Purged Cross-Validation)**가 필수적으로 사용됩니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $N$ | Number of Trials | $< 100$ | Higher $N$ increases probability of false discovery | [데이터 부재] |
| $P(\text{Max Sharpe})$ | Deflated Sharpe Ratio | Adj for multiple testing | Must penalize for $N$ trials | [데이터 부재] |
| $\text{Purge Window}$ | Embargo/Purge Size | Lag $\ge$ Auto-correlation | Removes leaked information | [데이터 부재] |
| $K$ | Number of Folds in CPCV | $5 \sim 10$ | Controls bias-variance tradeoff | [데이터 부재] |
| $SR_{IS} - SR_{OOS}$ | In-Sample vs Out-of-Sample | $\approx 0$ | Divergence implies overfitting | [데이터 부재] |

## 3. 다중 검정의 함정 (Multiple Testing Fallacy)
과적합의 가장 근본적인 수학적 원인은 '다중 검정(Multiple Testing)'에 있습니다. 어떤 연구자가 무작위(Random Walk) 주가 데이터를 바탕으로 수만 개의 매매 규칙(파라미터 조합)을 테스트한다면, 순전히 통계적인 우연(False Positive, 1종 오류)만으로도 샤프 비율(Sharpe Ratio)이 3.0이 넘는 환상적인 모델을 반드시 하나 이상 발견하게 됩니다.
- **Deflated Sharpe Ratio (DSR)**: 이 문제를 해결하기 위해 Marcos Lopez de Prado는 테스트 횟수 $N$과 수익률 분포의 왜도(Skewness), 첨도(Kurtosis)를 고려하여 가짜 샤프 비율을 깎아내는 DSR을 제안했습니다. 백테스트를 많이 돌릴수록, 모델을 신뢰하기 위해 요구되는 허들(Hurdle) 샤프 비율은 기하급수적으로 높아져야 합니다.

## 4. 정보 누수 방지: Purged & Embargoed Cross-Validation

일반적인 머신러닝의 K-Fold CV는 데이터를 임의로 섞어 훈련/테스트 세트를 나눕니다. 그러나 시계열 데이터에서 이렇게 하면, 테스트 세트(예: 수요일 데이터)가 훈련 세트(예: 화요일과 목요일 데이터) 사이에 끼어 있어 미래 정보가 과거로 누수됩니다.

### 4.1. Purging (퍼징)
- 훈련 세트의 관측치가 테스트 세트의 라벨(Label)과 시간적으로 겹칠 때, 그 겹치는 훈련 데이터를 완전히 삭제(Purge)하는 기법입니다.

### 4.2. Embargo (엠바고)
- 테스트 세트 직후에 이어지는 훈련 데이터 역시 강한 자기상관성을 가질 수 있으므로, 테스트 세트가 끝난 시점으로부터 일정 기간 $h$ (Embargo period) 동안의 훈련 데이터를 추가로 삭제하여 미래 정보의 누수를 원천 차단합니다.

### 4.3. CPCV (Combinatorial Purged Cross-Validation)
Purged K-Fold의 단점(테스트 경로가 1개뿐임)을 극복하기 위해, 전체 데이터를 $N$개의 그룹으로 나누고 그 중 $k$개를 테스트 세트로 선택하는 모든 조합 $\binom{N}{k}$에 대해 모델을 검증합니다. 이를 통해 수많은 시뮬레이션된 '대안적 과거(Alternative Histories)' 위에서 모델의 강건성(Robustness)과 샤프 비율 분포를 정밀하게 추정할 수 있습니다.

🧠 **AI의 사고방식:**
백테스트 곡선이 45도 각도로 매끄럽게 우상향하는 것은 퀀트 연구원이 느끼는 가장 큰 쾌감이자 가장 무서운 독(Poison)입니다. 과거 데이터는 이미 일어난 한 번의 경로에 불과한데, 그 경로에 옷을 너무 꽉 맞게 재단(Overfitting)하면 내일 날씨가 조금만 변해도 옷이 찢어져 버립니다. CPCV와 DSR은 연구자가 스스로의 '천재성에 대한 착각'을 깨부수고, 모델이 진짜 물리적 인과관계(Alpha)를 잡은 것인지 아니면 그저 노이즈를 외워버린 것인지 가혹하게 고문(Torture)하는 수학적 자백 장치입니다.