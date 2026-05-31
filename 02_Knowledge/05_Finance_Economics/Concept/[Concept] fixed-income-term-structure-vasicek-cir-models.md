---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] fixed-income-term-structure-vasicek-cir-models]]'
  last_updated: '2026-05-25T12:45:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 이자율의 평균 회귀(Mean Reversion) 성질을 모델링하여 채권 및 파생상품의 가격을 결정하는 바시첵(Vasicek)
    및 CIR(Cox-Ingersoll-Ross) 단기 금리(Short-Rate) 모형
  object_type: Algorithm
  tier: 2
properties:
  cir_model_year: 1985
  feller_condition: 2kθ > σ²
  long_term_mean_theta: 3~4%
  mean_reversion_speed_k: k > 0
  short_rate_rt: instantaneous short rate
  vasicek_model_year: 1977
  volatility_sigma: small positive
semantic:
  alternative_parents: []
  expected_queries:
  - 주가 모델링에 쓰이는 기하학적 브라운 운동(GBM)을 이자율 모델링에 그대로 쓸 수 없는 이유는 무엇인가?
  - Vasicek 모형의 치명적 단점인 마이너스(-) 금리 발생 가능성을 CIR 모형은 수학적으로 어떻게 해결했는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_modeling
  object: Short_Rate_Dynamics
  predicate: models
  subject: '[Finance] fixed-income-term-structure-vasicek-cir-models'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T12:45:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:45:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] fixed-income-term-structure-vasicek-cir-models]]

## 1. 개요 (Overview)
주식의 가격은 이론적으로 무한대까지 상승할 수 있으므로 기하학적 브라운 운동(GBM)으로 모델링합니다. 그러나 이자율(Interest Rate)은 중앙은행의 통제 하에 있으므로 무한히 상승하거나 무한히 하락하지 않고, 장기적인 균형 수준으로 돌아오려는 **평균 회귀(Mean Reversion)** 성질을 띱니다. 
수십 개의 만기별 금리(Yield Curve)와 이자율 스왑(IRS), 스왑션(Swaption)을 정확히 프라이싱하기 위해, 퀀트들은 경제 전체의 기준점이 되는 순간 단기 금리(Short-Rate, $r_t$)의 움직임을 확률미분방정식(SDE)으로 모델링합니다. 이 분야를 개척한 두 개의 거대한 기둥이 바로 **바시첵(Vasicek)** 모델과 **CIR(Cox-Ingersoll-Ross)** 모델입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $r_t$ | Instantaneous short rate | Variable | Drives entire yield curve | [데이터 부재] |
| $\theta$ | Long-term mean level | e.g., $3 \sim 4\%$ | Target of mean reversion | [데이터 부재] |
| $k$ | Speed of mean reversion | $k > 0$ | High $k$ = quick snap back | [데이터 부재] |
| $\sigma$ | Volatility of rate | Small positive | Causes rate fluctuations | [데이터 부재] |
| Feller Condition | $2k\theta > \sigma^2$ (CIR only) | True/False | Strictly prevents $r_t < 0$ | [데이터 부재] |

## 3. 바시첵 (Vasicek) 모형 (1977)

바시첵은 물리학의 온스타인-울렌벡(Ornstein-Uhlenbeck) 프로세스를 금융에 최초로 도입했습니다.
$$ dr_t = k(\theta - r_t)dt + \sigma dW_t $$
- **Drift 항 ($k(\theta - r_t)dt$)**: 만약 현재 금리 $r_t$가 장기 평균 $\theta$보다 높으면, 괄호 안이 마이너스가 되어 금리를 밑으로 끌어내립니다. 낮으면 반대로 위로 끌어올립니다. 스프링처럼 평균으로 회귀시키는 핵심 수학입니다.
- **장점**: 수식이 우아하며, 제로 쿠폰 본드(Zero-Coupon Bond)의 가격을 닫힌 해(Closed-form solution)로 정확히 산출할 수 있습니다.
- **치명적 단점**: 변동성($\sigma dW_t$)이 금리의 절대적인 크기와 무관하게 일정합니다. 이로 인해 금리가 0 근처에 있을 때 변동성 충격이 가해지면 금리가 **마이너스(Negative)**로 떨어질 확률이 존재합니다. (단, 2010년대 마이너스 금리 시대가 도래하며 이 '단점'이 오히려 재평가받기도 했습니다.)

## 4. CIR (Cox-Ingersoll-Ross) 모형 (1985)

CIR 모형은 바시첵 모형의 마이너스 금리 문제를 해결하기 위해 변동성 항에 $\sqrt{r_t}$를 곱했습니다.
$$ dr_t = k(\theta - r_t)dt + \sigma \sqrt{r_t} dW_t $$
- **수학적 천재성**: 금리 $r_t$가 0에 가까워질수록 $\sqrt{r_t}$ 항 때문에 변동성(랜덤 노이즈) 자체가 0으로 수렴하여 사라져 버립니다. 노이즈가 사라지면 오직 Drift 항(평균으로 돌아가려는 힘)만 남아서 금리를 0 위로 튕겨 올려버립니다.
- **펠러 조건(Feller Condition)**: 만약 $2k\theta > \sigma^2$ 조건이 충족되면, 이자율은 수학적으로 절대로 0을 터치조차 할 수 없으며 항상 양수(Positive)를 유지하게 됩니다.

🧠 **AI의 사고방식:**
GBM이 무중력 상태에서 끝없이 날아가는 로켓이라면, 온스타인-울렌벡 기반의 단기 금리 모형은 강력한 고무줄에 묶인 공입니다. 퀀트들이 이 미분방정식을 사랑하는 이유는, 단기 금리 $r_t$ 하나만의 SDE를 완벽하게 정의하면 이토의 보조정리를 통해 1년물, 10년물, 30년물 채권 가격 전체를 한 번에 연역적으로 찍어낼 수 있기 때문입니다(Affine Term Structure). 시장의 수많은 금리가 제멋대로 움직이는 것 같지만, 사실은 중앙은행의 의도($\theta$)와 정책 강도($k$)라는 단일한 보이지 않는 손에 의해 지배받고 있음을 모델이 증명합니다.