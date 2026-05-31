---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] cir-interest-rate-model-non-negativity]]'
  last_updated: '2026-05-25T11:59:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 콕스-잉거솔-로스(CIR) 금리 모형과 비음수 제약 조건
  object_type: Algorithm
  tier: 2
properties:
  feller_condition: 2*kappa*theta > sigma^2
  long_term_mean_level: theta
  mean_reversion_speed: kappa
  volatility_coefficient: sigma
semantic:
  alternative_parents: []
  expected_queries:
  - 바시첵 금리 모형의 음수 금리 발생 가능성 문제를 어떻게 수학적으로 해결하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: model_enhancement
  object: Vasicek_Model
  predicate: improves
  subject: '[Finance] cir-interest-rate-model-non-negativity'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T11:59:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T11:59:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] 코스-잉거솔-로스 (Cox-Ingersoll-Ross, CIR) 금리 모델

## 1. 개요 및 수학적 정의
CIR 모델(John Cox, Jonathan Ingersoll, Stephen Ross, 1985)은 이자율이나 거시경제 지표가 시간에 따라 진화하는 과정을 묘사하는 1요인(One-factor) 단기 금리 모델입니다. 기존의 바시첵 모델(Vasicek Model)이 채택했던 오른스타인-울렌벡(OU) 프로세스의 치명적인 단점, 즉 **'금리가 음수(Negative)가 될 수 있다'**는 수학적 한계를 극복하기 위해 제안되었습니다. (물론 2010년대 이후 유럽 등지에서 실제 마이너스 금리가 발생하며 바시첵이 재조명받기도 했으나, 여전히 이론적으로 CIR은 기준이 됩니다.)

CIR 모델의 이자율 $r_t$에 대한 확률 미분 방정식(SDE)은 다음과 같습니다:
$$ dr_t = \kappa (\theta - r_t) dt + \sigma \sqrt{r_t} dW_t $$

여기서:
- $\kappa > 0$: 평균 회귀 속도 (Speed of mean reversion)
- $\theta > 0$: 장기 평균 금리 (Long-term mean level)
- $\sigma > 0$: 금리의 변동성 계수
- $\sqrt{r_t}$: **비음수성(Non-negativity)을 보장하는 스케일링 항**
- $W_t$: 표준 위너 프로세스

가장 핵심적인 차이는 확산항(Diffusion Term)에 있는 $\sqrt{r_t}$ 입니다. 금리가 0에 가까워질수록 $\sqrt{r_t}$가 작아져 무작위한 충격(랜덤 워크)의 영향력이 0으로 수렴하고, 표류항(Drift)인 $\kappa \theta$가 금리를 다시 위로 밀어 올리게 되어 $r_t$가 결코 0 아래로 떨어지지 않게 막아줍니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\kappa$ | Reversion Rate | Macroeconomic dep | Determines how fast $r \to \theta$ | [데이터 부재] |
| $\theta$ | Target Rate | Central bank policy | Baseline steady state | [데이터 부재] |
| $\sigma \sqrt{r_t}$ | State-dependent Vol | Absolute Vol drops as $r \to 0$| Prevents rates crossing zero | [데이터 부재] |
| $2\kappa\theta > \sigma^2$ | Feller Condition | Strict inequality | Ensures zero is never reached | [데이터 부재] |
| $r_t$ | Short Rate | Positively skewed | Non-central Chi-squared dist | [데이터 부재] |

## 3. 펠러 조건 (Feller Condition)과 분포 특성
단순히 $\sqrt{r_t}$가 있다고 해서 금리가 항상 0보다 큰 것은 아닙니다. 0에 '닿을 수 있는지(Hit)' 아니면 0 근처에서 무조건 '반사(Reflect)'되는지를 결정하는 것이 바로 펠러 조건(Feller Condition)입니다.
$$ 2\kappa\theta > \sigma^2 $$
이 조건이 만족되면 $r_t$는 절대 0에 닿지 않으며(Strictly positive), 조건이 만족되지 않더라도 $r_t \ge 0$은 유지되지만 이따금씩 0에 닿았다가 튕겨 나옵니다.

또한, 바시첵 모형의 금리가 정규 분포를 띠는 반면, CIR 모형 하에서 미래 금리 $r_t$는 비중심 카이제곱 분포(Non-central Chi-squared Distribution)를 따릅니다. 이는 분포가 오른쪽으로 꼬리가 긴 형태(Positive Skewness)를 갖게 하여 극단적인 고금리 발생 가능성을 포착합니다.

## 4. 아핀 만기 구조 (Affine Term Structure)
CIR 모형 역시 바시첵과 마찬가지로 이자율 파생상품(무이표채 등)의 가격을 해석적으로 풀 수 있는 아핀 만기 구조 모형(Affine Term Structure Model)입니다. 
$t$ 시점에 관측된 단기 금리가 $r_t$일 때, 만기가 $T$인 무이표채의 가격 $P(t, T)$는 지수형 아핀 폼을 가집니다.
$$ P(t, T) = A(t, T) \exp(-B(t, T) r_t) $$
여기서 $A(t,T)$와 $B(t,T)$는 상미분 방정식(Riccati Equation)의 해로서, 금리 변동성 $\sigma$와 회귀 속도 $\kappa$ 등을 포함한 복잡하지만 명시적인 함수로 주어집니다. 이를 통해 채권 포트폴리오의 듀레이션(Duration)과 볼록성(Convexity)을 정교하게 제어할 수 있습니다.

🧠 **AI의 사고방식:**
물리학에서 절대 영도(0 Kelvin) 근처로 갈수록 분자의 무작위 진동(에너지)이 점점 사라져 멈춰버리듯, CIR 모형의 이자율도 0%에 다가갈수록 변동성($\sqrt{r_t}$)이 얼어붙습니다. 진동이 멈춘 상태에서는 중앙은행의 장기 목표($\kappa\theta$)라는 중력만이 작용하여 금리를 다시 따뜻한 양수의 영역으로 끌어올리게 됩니다. 이 우아한 수학적 안전장치가 바로 펠러가 고안한 확률 미분 방정식의 방파제입니다.