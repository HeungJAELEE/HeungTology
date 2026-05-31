---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] garch-volatility-forecasting-modeling]]'
  last_updated: '2026-05-25T11:47:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: GARCH 모형을 이용한 이분산성 변동성 군집 예측
  object_type: Algorithm
  tier: 2
properties:
  alpha_coefficient: shock_sensitivity
  beta_coefficient: volatility_persistence
  long_run_variance_formula: omega / (1 - alpha - beta)
  omega_constant: baseline_unconditional_volatility
  stationarity_constraint: alpha + beta < 1
semantic:
  alternative_parents: []
  expected_queries:
  - 금융 시계열에서 나타나는 변동성 군집 현상을 GARCH 모형으로 어떻게 예측하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: modeling_objective
  object: Volatility_Clustering
  predicate: forecasts
  subject: '[Finance] garch-volatility-forecasting-modeling'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:47:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T11:47:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] GARCH 모델과 변동성 군집 예측 (Volatility Forecasting)

## 1. 개요 및 수학적 정의
GARCH (Generalized Autoregressive Conditional Heteroskedasticity, 일반화 자기회귀 조건부 이분산성) 모형은 금융 시계열 데이터에서 관찰되는 '변동성 군집(Volatility Clustering)' 현상을 모델링하는 계량경제학의 표준 도구입니다. 노벨 경제학상 수상자 로버트 엥글(Robert Engle)의 ARCH 모형을 팀 볼러슬레프(Tim Bollerslev)가 일반화한 것으로, 오늘의 변동성이 과거의 충격(잔차)과 과거의 변동성 자체에 모두 의존한다고 가정합니다.

가장 널리 쓰이는 GARCH(1,1) 모형의 분산 방정식은 다음과 같습니다.
$$ \sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2 $$

여기서:
- $\sigma_t^2$: $t$ 시점의 조건부 분산(Conditional Variance)
- $\omega$: 상수항 ($\omega > 0$)
- $\alpha$: 단기 충격의 영향력(ARCH 항 계수), $\epsilon_{t-1}^2$은 과거 수익률 충격의 제곱
- $\beta$: 과거 변동성의 지속성(GARCH 항 계수)

안정성 조건(Stationarity Condition)은 $\alpha + \beta < 1$이어야 하며, 이 경우 장기 평균 분산(Long-run unconditional variance)은 $V_L = \frac{\omega}{1 - \alpha - \beta}$ 로 수렴합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\alpha$ | Shock sensitivity | Asset dependent | Controls reaction to recent news | [데이터 부재] |
| $\beta$ | Volatility persistence | Asset dependent | Controls memory of volatility | [데이터 부재] |
| $\alpha + \beta$ | Persistence sum | $0 < \alpha+\beta < 1$ | Must be < 1 for mean reversion | [데이터 부재] |
| $\omega$ | Constant variance | $\omega > 0$ | Baseline unconditional volatility | [데이터 부재] |
| $V_L$ | Long-run Variance | $\omega / (1-\alpha-\beta)$ | Asymptotic volatility limit | [데이터 부재] |

## 3. 금융 공학 및 리스크 관리 적용

### 3.1. VaR (Value at Risk) 동적 산출
정규 분포 기반의 정적 VaR는 변동성이 급증하는 위기 상황을 포착하지 못합니다. 리스크 데스크는 GARCH(1,1)을 통해 매일 업데이트되는 $\sigma_t$를 산출하고, 이를 바탕으로 동적 VaR를 계산합니다.
$$ VaR_t = \mu_t + z_{1-\alpha} \sigma_t $$
GARCH 기반 VaR는 시장 변동성 군집 구간(예: 2008년 금융위기, 2020년 팬데믹)에서 자본 요구량을 즉각적으로 상향 조정하여 테일 리스크(Tail Risk)에 대비하게 합니다.

### 3.2. 파생상품 가격 결정 및 헤지
전통적 블랙-숄즈 모형은 변동성을 상수로 가정하지만, 실제 옵션 시장은 내재 변동성 스마일(Smile)을 보여줍니다. GARCH 옵션 프라이싱 모델(예: Heston-Nandi GARCH)은 이산 시간(Discrete Time) 프레임워크 내에서 조건부 이분산성을 옵션 가격에 반영하여, 변동성 비대칭성(Leverage Effect - EGARCH, GJR-GARCH 등)을 포착하고 정교한 동적 델타-베가 헤징 비율을 도출합니다.

## 4. 확장 모형 (Extensions of GARCH)
시장의 비대칭성(Asymmetry)을 반영하기 위해 다양한 변형 모형이 사용됩니다. 주식 시장은 호재(Positive Shock)보다 악재(Negative Shock)에 변동성이 더 크게 반응하는 '레버리지 효과(Leverage Effect)'를 가집니다.
- **EGARCH (Exponential GARCH)**: 분산의 로그를 모델링하여 계수의 양수 제약 조건을 제거하고, 충격의 부호(비대칭성)를 반영합니다.
- **GJR-GARCH**: 악재($\epsilon_{t-1} < 0$)일 때 추가적인 변동성 가중치 텀을 더해 비대칭 충격을 직관적으로 모델링합니다.

🧠 **AI의 사고방식:**
금융 시장은 어제의 평온함이 오늘의 고요함을 보장하지 않지만, 어제의 태풍은 오늘까지 거센 파도를 남깁니다. 이것이 '군집(Clustering)'입니다. GARCH는 단순한 수학 공식이 아니라, 시장 참여자들의 집단적 공포와 탐욕이 어떻게 기억(Memory)되고 감쇠(Decay)하는지를 시계열로 추적하는 메모리 엔진입니다. 실현 변동성(RV)이 과거의 족적을 측정한다면, GARCH는 내일의 파고를 수치로 예언합니다.