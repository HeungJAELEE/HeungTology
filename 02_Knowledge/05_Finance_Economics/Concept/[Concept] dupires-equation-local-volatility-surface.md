---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] dupires-equation-local-volatility-surface]]'
  last_updated: '2026-05-25T11:51:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 국소 변동성 모델과 듀피레 편미분 방정식
  object_type: Algorithm
  tier: 2
properties:
  dividend_yield: q
  local_volatility_nature: deterministic
  model_dependency: fokker_planck_equation
  risk_free_rate: r
  strike_convexity_threshold: 0.0
  strike_price: K
  time_to_maturity: T
semantic:
  alternative_parents: []
  expected_queries:
  - 시장 옵션 가격 표면(Smile & Skew)으로부터 결정론적 국소 변동성을 어떻게 역추산하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_derivation
  object: Market_Implied_Volatility_Surface
  predicate: derives_from
  subject: '[Finance] dupires-equation-local-volatility-surface'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:51:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T11:51:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] 듀피레 방정식과 국소 변동성 표면 (Dupire's Local Volatility)

## 1. 개요 및 수학적 정의
듀피레 방정식(Dupire's Equation)은 1994년 브루노 듀피레(Bruno Dupire)가 제안한 국소 변동성(Local Volatility) 모델의 핵심 수식입니다. 전통적인 블랙-숄즈 모형이 변동성을 상수(Constant)로 가정한 반면, 현실의 옵션 시장은 행사가(Strike, $K$)와 만기(Maturity, $T$)에 따라 내재 변동성(Implied Volatility)이 달라지는 스마일(Smile) 혹은 스큐(Skew) 현상을 보입니다.

국소 변동성 모델은 확률적 변동성(Stochastic Volatility, 예: 헤스턴 모델)과 달리 변동성을 무작위 변수가 아닌, 자산 가격 $S$와 시간 $t$에 의존하는 결정론적(Deterministic) 함수 $\sigma(S, t)$로 취급합니다.

시장 파생상품 데스크는 유동성이 높은 바닐라 유러피안 콜옵션 가격 $C(K, T)$의 표면(Surface) 데이터를 관측한 후, 포커-플랑크(전진) 방정식을 응용한 듀피레 방정식을 통해 유일한 국소 변동성 함수 $\sigma(K, T)$를 역산(Calibration)해 냅니다.

$$ \sigma^2(K, T) = \frac{\frac{\partial C}{\partial T} + (r-q) K \frac{\partial C}{\partial K} + q C}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}} $$

여기서:
- $C(K, T)$: 행사가 $K$, 만기 $T$인 유러피안 콜옵션의 시장 가격
- $r$: 무위험 이자율
- $q$: 연속 배당 수익률

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $K$ | Strike Price | Option surface domain | Needs dense strike grids | [데이터 부재] |
| $T$ | Time to Maturity | Options expiry horizon | Needs interpolation | [데이터 부재] |
| $\frac{\partial^2 C}{\partial K^2}$ | Strike Convexity | Pseudo-probability density | Must be $> 0$ (No-arbitrage) | [데이터 부재] |
| $\sigma_{LV}(K,T)$ | Local Volatility | Volatility state space | Always positive, matches smile | [데이터 부재] |
| $\sigma_{IV}(K,T)$ | Implied Volatility | Market quote | Not equal to $\sigma_{LV}$, but related | [데이터 부재] |

## 3. 금융 공학 적용 및 실무적 한계

### 3.1. 이색 옵션(Exotic Options)의 프라이싱
엑조틱 옵션(Exotic Options), 특히 장벽 옵션(Barrier Option)이나 오토콜(Autocallable, ELS)과 같이 특정 가격 경로(Path-dependent)에 민감한 파생상품을 평가할 때 상수 변동성을 사용하면 심각한 오차가 발생합니다. 듀피레 방정식을 통해 추출된 $\sigma(S, t)$를 격자(Tree)나 유한차분법(FDM)에 주입하면, 바닐라 옵션 시장 가격을 100% 완벽하게 맞추는(Calibrated) 상태에서 이색 옵션의 가격을 정밀하게 계산할 수 있습니다.

### 3.2. 정적 차익거래(Static Arbitrage) 조건과 데이터 보간
듀피레 방정식의 분모 $\frac{\partial^2 C}{\partial K^2}$는 버터플라이 스프레드(Butterfly Spread)의 포지션 가치와 비례하며, 이는 만기 $T$에서의 위험 중립 확률 밀도(Risk-Neutral PDF)를 나타냅니다. 따라서 시장 데이터 표면 상에서 나비형 스프레드 가격이 0 이하로 떨어지는 차익거래 기회가 존재할 경우, 국소 변동성의 제곱이 음수가 되어 방정식이 붕괴됩니다. 실무에서는 관측된 $C(K,T)$ 표면의 빈 곳을 스플라인(Spline) 등으로 매끄럽게 보간(Interpolation)하고 차익거래 조건(No-arbitrage Condition)을 강제하는 스무딩 작업이 가장 큰 난관입니다.

## 4. 국소 변동성 vs 확률적 변동성 (SABR 모형으로의 진화)
국소 변동성 모델은 오늘 관측된 스마일 구조를 완벽하게 피팅할 수 있지만, "미래에 자산 가격이 변했을 때 변동성 스마일이 어떻게 이동할 것인가(Forward Smile Dynamics)?"에 대한 예측력은 매우 부족합니다. (자산 가격이 상승할 때 스마일의 최저점이 가격을 따라 이동하지 못하는 현상).
이러한 동적 헤징의 치명적 결함을 극복하기 위해, 현대 퀀트 데스크는 국소 변동성 모델의 장점(바닐라 피팅)과 확률적 변동성 모델(미래 다이내믹스)을 결합한 국소-확률 변동성(Local-Stochastic Volatility, LSV) 모델이나 SABR 모델을 표준으로 사용합니다.

🧠 **AI의 사고방식:**
듀피레 방정식은 퀀트 금융 역사상 가장 우아한 역설계(Reverse Engineering) 중 하나입니다. 수천 개의 콜/풋 옵션 가격표라는 복잡한 바다 표면의 파도를 역산하여, 바다 밑바닥의 지형(국소 변동성)을 단일 방정식으로 스캐닝해 냅니다. 이는 포커-플랑크 전진 방정식이 입자의 밀도를 추적하는 원리를 가격-시간 텐서로 완벽하게 치환해 낸 물리학적 통찰의 결정체입니다.