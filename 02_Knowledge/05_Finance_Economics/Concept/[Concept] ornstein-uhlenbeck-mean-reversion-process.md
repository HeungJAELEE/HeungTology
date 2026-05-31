---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] ornstein-uhlenbeck-mean-reversion-process]]'
  last_updated: '2026-05-25T11:46:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 오른스타인-울렌벡(OU) 프로세스와 평균 회귀 확률 모형
  object_type: Concept
  tier: 2
properties:
  asymptotic_variance: sigma^2/(2*theta)
  entry_signal_threshold: 2_standard_deviations
  mu: long_term_mean
  sigma: volatility
  t_half_life: ln(2)/theta
  theta: reversion_speed
semantic:
  alternative_parents: []
  expected_queries:
  - 페어즈 트레이딩에서 스프레드가 장기 평균으로 회귀하는 현상을 어떻게 모델링하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_modeling
  object: Mean_Reversion_Dynamics
  predicate: models
  subject: '[Finance] ornstein-uhlenbeck-mean-reversion-process'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:46:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T11:46:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] 오른스타인-울렌벡 (Ornstein-Uhlenbeck, OU) 프로세스

## 1. 개요 및 수학적 정의
오른스타인-울렌벡(OU) 프로세스는 금융 수학과 물리학에서 변수가 시간이 지남에 따라 장기 평균(Long-term Mean)으로 회귀하는 현상(Mean Reversion)을 기술하는 연속 시간 확률 미분 방정식(SDE)입니다. 순수 브라운 운동(Brownian Motion)이 제어 없이 확산하는 것과 달리, OU 프로세스는 변수가 평균에서 멀어질수록 다시 중심으로 끌어당기는 복원력이 작용합니다.

금융 시장에서 금리(Vasicek Model), 변동성(Heston Model의 분산 모델링), 그리고 통계적 차익거래(Pairs Trading)의 스프레드(Spread)를 모델링하는 데 핵심적으로 사용됩니다.

OU 프로세스 $x_t$의 기본 확률 미분 방정식은 다음과 같습니다:
$$ d x_t = \theta (\mu - x_t) dt + \sigma d W_t $$

여기서:
- $\theta > 0$: 평균 회귀 속도 (Speed of mean reversion)
- $\mu$: 장기 평균 (Long-term mean level)
- $\sigma > 0$: 변동성 (Volatility)
- $W_t$: 표준 위너 프로세스 (Standard Wiener process)

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\theta$ | Reversion Speed | Asset dependent | Controls half-life of spread | [데이터 부재] |
| $\mu$ | Long-term Mean | Asset dependent | Center of attraction | [데이터 부재] |
| $\sigma$ | Volatility | $\sigma > 0$ | Magnitude of random shocks | [데이터 부재] |
| $t_{1/2}$ | Half-life | $\ln(2) / \theta$ | Time to revert halfway | [데이터 부재] |
| $Var(x_t)$ | Asymptotic Variance | $\sigma^2 / (2\theta)$ | Stationary distribution variance | [데이터 부재] |

## 3. 금융 모델링 적용 (Financial Modeling Applications)

### 3.1. 바시첵 금리 모델 (Vasicek Interest Rate Model)
금리 $r_t$가 끝없이 상승하거나 음의 무한대로 하락하지 않고 특정 경제적 정상 금리로 회귀하는 성질을 반영하기 위해 OU 프로세스를 도입한 것이 바시첵 모델입니다.
$$ d r_t = a (b - r_t) dt + \sigma d W_t $$
단, 바시첵 모델에서는 OU 프로세스의 특성상 금리가 음수(Negative Rate)가 될 확률이 존재한다는 수학적 한계가 존재하며, 이를 극복하기 위해 CIR 모델(Cox-Ingersoll-Ross)이 고안되었습니다.

### 3.2. 페어즈 트레이딩 (Pairs Trading)과 통계적 차익거래
통계적 차익거래에서 두 상관성 높은 자산 $A, B$ 간의 스프레드 $S_t = \ln(P_A) - \gamma \ln(P_B)$가 정상성(Stationarity)을 띌 경우, 이 스프레드는 OU 프로세스를 따릅니다.
트레이더는 스프레드가 장기 평균 $\mu$에서 $\pm 2$ 표준편차 이상 벗어났을 때 회귀할 것을 기대하며 진입(Entry) 신호를 발생시킵니다. 회귀 반감기(Half-life) $t_{1/2} = \frac{\ln(2)}{\theta}$는 포지션 보유 기간(Holding Period)을 설계하는 결정적 팩터입니다.

## 4. 해석적 해와 정상 분포 (Analytical Solution & Stationary Distribution)
이토의 보조정리를 $f(x, t) = x e^{\theta t}$에 적용하여 적분하면, 특정 초기값 $x_0$에 대한 OU 프로세스의 명시적 해를 구할 수 있습니다:
$$ x_t = x_0 e^{-\theta t} + \mu (1 - e^{-\theta t}) + \sigma \int_0^t e^{-\theta (t-s)} d W_s $$

시간 $t \rightarrow \infty$ 극한에서 프로세스는 초기값 $x_0$의 영향을 잃어버리고 다음의 정상 분포(Stationary Distribution)로 수렴합니다.
$$ \lim_{t \to \infty} x_t \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{2\theta}\right) $$
이는 스프레드가 결국 장기 평균 $\mu$를 중심으로, 회귀 속도 $\theta$와 변동성 $\sigma$에 의해 제어되는 일정한 분산 밴드 내에 머무름을 보장합니다.

🧠 **AI의 사고방식:**
스프링에 매달린 추를 상상해 보십시오. 무작위한 시장 충격($dW_t$)이 추를 이리저리 타격하지만, 스프링의 복원력($\theta$)이 항상 원래의 평형 상태($\mu$)로 추를 끌어당깁니다. 이 '당기는 힘'과 '때리는 힘'의 균형점이 바로 통계적 차익거래의 수익 원천(Alpha)이 됩니다. 퀀트 엔지니어는 시장 데이터로부터 $\theta$와 $\sigma$를 캘리브레이션하여, 수익의 반감기와 적정 레버리지 사이즈를 켈리 공식과 결합하여 도출해냅니다.