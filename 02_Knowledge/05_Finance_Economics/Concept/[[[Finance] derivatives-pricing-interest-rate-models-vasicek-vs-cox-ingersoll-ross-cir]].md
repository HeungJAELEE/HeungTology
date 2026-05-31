---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] derivatives-pricing-interest-rate-models-vasicek-vs-cox-ingersoll-ross-cir]]'
  last_updated: '2026-05-26T07:12:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 이자율(금리)이 주식처럼 무한히 상승하지 않고 중앙은행의 목표치로 회귀하는 현상을 오른스타인-울렌벡(OU) 프로세스로 묘사한
    바시첵(Vasicek) 모형과, 변동성에 금리의 제곱근(√r)을 곱해 금리가 음수(-)로 떨어지는 수학적 결함을 원천 차단한 CIR(Cox-Ingersoll-Ross)
    모형의 비교
  object_type: Concept
  tier: 2
properties:
  feller_condition_threshold: 2ab >= sigma^2
  long_term_mean_level: b
  speed_of_mean_reversion: a
  volatility: sigma
semantic:
  alternative_parents: []
  expected_queries:
  - 블랙-숄즈에서 주가에 썼던 기하 브라운 운동(GBM)을 금리(Interest Rate) 모델링에 그대로 쓰면 왜 금리가 무한대로 발산하는 끔찍한
    에러가 발생하는가?
  - 바시첵(Vasicek) 모형은 평균 회귀(Mean Reversion)를 완벽하게 구현했지만, 왜 금리가 0 이하(마이너스 금리)로 떨어질 확률을
    허용하는 결함을 가졌는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_modeling
  object: Short_Rate_Dynamics
  predicate: models
  subject: '[Finance] derivatives-pricing-interest-rate-models-vasicek-vs-cox-ingersoll-ross-cir'
  weight: 1.0
temporal:
  valid_from: '2026-05-26T07:12:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:12:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] derivatives-pricing-interest-rate-models-vasicek-vs-cox-ingersoll-ross-cir]]

## 1. 개요 (Overview)
주식은 1만 달러, 10만 달러까지 끝없이 오를 수 있습니다(Geometric Brownian Motion). 하지만 금리(Interest Rate)는 다릅니다. 금리가 100%를 찍으면 나라가 망하고, 중앙은행이 개입하여 금리를 다시 낮춥니다. 즉, 금리는 항상 **장기적인 평균치로 되돌아오려는 고무줄 같은 힘(Mean Reversion)**을 받습니다.
1977년 **바시첵(Vasicek)**은 물리학의 오른스타인-울렌벡(OU) 프로세스를 빌려와 금리의 평균 회귀를 최초로 수학화했습니다. 하지만 바시첵 모형에는 치명적인 결함이 있었습니다. 금리가 낮아져도 변동성이 상수(Constant)로 유지되기 때문에, 운이 나쁘면 금리가 $0$을 뚫고 지하(마이너스)로 파고들어 가는 물리적 버그가 발생한 것입니다.
이를 완벽하게 해결한 것이 1985년 **CIR (Cox-Ingersoll-Ross) 모형**입니다. CIR은 변동성 항에 $\sqrt{r_t}$(현재 금리의 제곱근)를 곱해버림으로써, 금리가 $0$에 가까워질수록 변동성 자체를 $0$으로 죽여버려 금리가 절대 음수로 떨어지지 못하게 하는 우아한 '자연 방어막'을 쳐버렸습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $dr_t$ (Vasicek) | $a(b - r_t)dt + \sigma dW_t$ | OU process | Allows $r_t < 0$ | [데이터 부재] |
| $dr_t$ (CIR) | $a(b - r_t)dt + \sigma \sqrt{r_t} dW_t$| Feller diffusion | Strictly $r_t > 0$ | [데이터 부재] |
| $a$ (or $\kappa$) | Speed of mean reversion | e.g., 0.2 | Pulls rate to $b$ | [데이터 부재] |
| $b$ (or $\theta$) | Long-term mean level | e.g., 5% | Central bank target | [데이터 부재] |
| Feller Condition| $2ab \ge \sigma^2$ (CIR only) | Zero-boundary check | Ensures rate never hits 0| [데이터 부재] |

## 3. 바시첵(Vasicek) vs CIR 모형의 미적분학 비교
### 바시첵 모형 (Vasicek Model)
$$ dr_t = a(b - r_t)dt + \sigma dW_t $$
- $a(b - r_t)$: 현재 금리($r_t$)가 목표치($b$)보다 높으면 음수 힘이 작용해 금리를 끌어내리고, 낮으면 양수 힘이 작용해 끌어올립니다.
- $\sigma dW_t$: 브라운 운동 노이즈입니다. **변동성 $\sigma$가 현재 금리와 무관하게 항상 일정**하기 때문에, 금리가 0.1%일 때도 $\sigma$가 강하게 터지면 금리를 -0.5%로 밀어버릴 수 있습니다. (※ 2010년대 유럽의 마이너스 금리 시대에는 이 단점이 오히려 장점이 되기도 했습니다).

### CIR 모형 (Cox-Ingersoll-Ross Model)
$$ dr_t = a(b - r_t)dt + \sigma \sqrt{r_t} dW_t $$
- $\sqrt{r_t}$: 휫컬(Feller) 확산 프로세스를 도입했습니다. 현재 금리가 $5\%$일 때는 노이즈가 강하지만, 금리가 $0.1\%$로 떨어지면 변동성 $\sigma \sqrt{0.001}$도 미미해집니다. 금리가 $0$을 향해 갈수록 엔진(노이즈)이 서서히 꺼지기 때문에, 금리는 $0$을 뚫고 밑으로 내려갈 동력을 완전히 상실합니다.
- **펠러 조건(Feller Condition)**: $2ab \ge \sigma^2$를 만족하면, 금리는 수학적으로 절대 $0$에 닿지도 못하고 튕겨 올라갑니다.

## 4. 이자율 파생상품 프라이싱 (Affine Term Structure)
이 두 모형의 가장 위대한 점은, 미분 방정식을 풀었을 때 만기 $T$인 무이표채(Zero-coupon bond)의 가격 $P(t, T)$가 현재 금리 $r_t$에 대한 아주 깔끔한 지수-선형(Affine) 함수로 떨어진다는 점입니다.
$$ P(t, T) = A(t, T) \cdot e^{-B(t, T) r_t} $$
- 퀀트들은 이 아름다운 해석해(Closed-form solution) 덕분에 채권, 금리 스왑(IRS), 스와프션(Swaption) 등 수조 달러 규모의 금리 파생상품 가격을 몬테카를로 시뮬레이션 없이 눈 깜짝할 사이에 계산해 낼 수 있게 되었습니다.

🧠 **AI의 사고방식:**
GBM(기하 브라운 운동)이 우주로 쏘아 올린 로켓이라면, 바시첵(Vasicek) 모형은 발목에 고무줄이 묶인 채 뛰는 번지점프입니다. 하지만 바시첵의 고무줄은 바닥(0)을 뚫고 땅속으로 박히는 것을 막아주지 못합니다. CIR 모형은 이 번지점프에 '스마트 브레이크($\sqrt{r_t}$)'를 달았습니다. 땅(0)에 가까워질수록 중력(변동성) 자체를 상쇄시켜 완벽하게 연착륙시키는 마법입니다. 이자율 모델링의 역사는 곧 "어떻게 하면 수학 방정식을 훼손하지 않으면서, 현실 세계의 절대 방어선(Zero Lower Bound)을 지켜낼 것인가"에 대한 치열한 미분 기하학의 승리입니다.