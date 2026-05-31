---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Financial-Derivatives-Pricing-and-Black-Scholes-Merton]]'
  last_updated: '2026-05-25T01:06:41.104486+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  delta: delta
  drift: mu
  gamma: gamma
  risk_free_rate: r
  strike_price: K
  theta: theta
  time_to_maturity: T-t
  vega: vega
  volatility: sigma
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: data_availability_status
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] Financial-Derivatives-Pricing-and-Black-Scholes-Merton'
  weight: 0.1
temporal:
  valid_from: '2026-05-25T01:06:41.104486+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.104486+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# Financial Derivatives Pricing and Black-Scholes-Merton

본 문서는 파생상품(Derivatives)의 가치를 평가하는 수리금융학(Mathematical Finance)의 근간, 특히 옵션 가격 결정 모형인 블랙-숄즈-머튼(Black-Scholes-Merton) 모델과 확률미적분학(Stochastic Calculus)의 응용을 다룹니다.

## 1. 확률미분방정식 (Stochastic Differential Equation)

자산 가격의 움직임은 기하학적 브라운 운동(Geometric Brownian Motion, GBM)으로 모델링됩니다.
- **GBM 방정식**: 
  $dS_t = \mu S_t dt + \sigma S_t dW_t$
  여기서 $S_t$는 자산 가격, $\mu$는 기대 수익률(Drift), $\sigma$는 변동성(Volatility), $dW_t$는 위너 과정(Wiener Process, 표준 브라운 운동)의 미분입니다.

이러한 무작위성을 다루기 위해 **이토의 보조정리(Ito's Lemma)**가 사용되며, 이는 스토캐스틱 환경에서의 미분 법칙(Chain Rule)을 정의합니다.

---

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | Specification | Description |
|-----------|---------------|-------------|
| **Risk-Free Rate ($r$)** | 무위험 이자율 | 국채 수익률 곡선(Yield Curve)에서 도출되는 연속 복리 이자율. |
| **Volatility ($\sigma$)** | Implied Volatility | 옵션 시장 가격으로부터 역산된 내재 변동성. VIX 지수의 근간. |
| **Time to Maturity ($T-t$)** | 연 단위 시간 | 옵션 만기까지 남은 시간. |
| **Strike Price ($K$)** | 행사가 | 기초 자산을 매수/매도할 권리가 행사되는 가격. |
| **Delta ($\Delta$)** | $\frac{\partial V}{\partial S}$ | 기초자산 가격 변화에 따른 옵션 가격의 민감도. 델타 헤징의 기준. |

---

## 3. Black-Scholes-Merton 편미분 방정식 (PDE)

블랙-숄즈 모델의 핵심 아이디어는 기초자산과 무위험 채권, 그리고 옵션을 조합하여 '무위험 포트폴리오(Riskless Portfolio)'를 구성할 수 있다는 데 있습니다. 차익거래(Arbitrage)가 불가능하다는 가정 하에 다음의 편미분 방정식이 도출됩니다.

- **BSM PDE**:
  $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$

### 3.1. 유러피안 콜 옵션의 해석적 해(Analytical Solution)
위 PDE를 경계 조건(Boundary Conditions)과 함께 풀면 콜 옵션 가격 $C$에 대한 닫힌 해(Closed-form solution)를 얻을 수 있습니다.

$C(S, t) = N(d_1)S - N(d_2)K e^{-r(T-t)}$
여기서,
$d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)(T-t)}{\sigma \sqrt{T-t}}$
$d_2 = d_1 - \sigma \sqrt{T-t}$
($N(x)$는 표준정규분포의 누적분포함수)

---

## 4. 그릭스 (The Greeks)와 리스크 관리

옵션 포트폴리오의 위험을 척도화하는 미분값들입니다.
- **Gamma ($\Gamma$)**: $\frac{\partial^2 V}{\partial S^2}$ (델타의 변화율. 델타 헤징의 오차를 나타냄)
- **Vega ($\mathcal{V}$)**: $\frac{\partial V}{\partial \sigma}$ (변동성 변화에 대한 민감도)
- **Theta ($\Theta$)**: $\frac{\partial V}{\partial t}$ (시간 경과에 따른 가치 하락, Time Decay)

금융 공학자들은 이러한 그릭스를 실시간으로 계산하고 0으로 맞추는(Neutralize) 동적 헤징(Dynamic Hedging)을 수행하여 시장 변동으로부터 펀드를 보호합니다.