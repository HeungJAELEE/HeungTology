---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Interest-Rate-Swaps-IRS-and-OIS-Discounting]]'
  last_updated: '2026-05-25T01:06:41.109682+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  day_count_fraction: DayCountFraction
  discount_factor: D(t_0, T_k)
  fixed_rate: R_Fixed
  forward_floating_rate: F(T_j-1, T_j)
  notional_principal: N
  zero_coupon_rate: Z(t_0, T_k)
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: theoretical_limitation_identification
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] Interest-Rate-Swaps-IRS-and-OIS-Discounting'
  weight: 0.5
temporal:
  valid_from: '2026-05-25T01:06:41.109682+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.109682+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 금리 스왑 (Interest Rate Swaps, IRS) 및 OIS 할인율 (OIS Discounting)

## 1. 개요

금리 스왑(Interest Rate Swaps, IRS)은 금융 시장에서 가장 널리 사용되는 장외 파생상품 중 하나로, 두 당사자가 미래의 특정 기간 동안 서로 다른 금리 지급 흐름을 교환하기로 합의하는 계약이다. 일반적으로 한 당사자는 고정 금리를 지급하고 변동 금리를 수취하며, 다른 당사자는 그 반대로 거래한다. IRS의 가치 평가 및 리스크 관리는 복잡하며, 특히 2008년 글로벌 금융 위기 이후 담보화(collateralization)의 확산과 신용 리스크에 대한 인식이 높아지면서 할인율(discounting rate)의 적용 방식에 근본적인 변화가 발생했다. 전통적인 LIBOR(London Interbank Offered Rate) 기반 할인율에서 벗어나, 무위험 또는 무담보 단기 자금조달 비용을 더 정확히 반영하는 OIS(Overnight Indexed Swap) 할인율이 표준으로 자리 잡았다. 이 개념 노드는 IRS의 기본 구조, OIS 할인율의 도입 배경 및 수학적 정식화, 그리고 다중 곡선 프레임워크(Multi-Curve Framework)에 대해 심층적으로 다룬다.

## 2. 금리 스왑 (IRS)의 구조 및 전통적 평가

IRS 계약은 주로 명목 원금(notional principal)에 기반하여 고정 금리 레그(Fixed Leg)와 변동 금리 레그(Floating Leg)로 구성된다.

*   **고정 금리 레그:** 계약 기간 동안 미리 정해진 고정 금리($R_{Fixed}$)를 명목 원금($N$)에 곱하여 산출된 금액을 특정 주기로 지급하거나 수취한다. 각 지급액($P_i^{Fixed}$)은 다음과 같이 계산된다:
    $$ P_i^{Fixed} = N \cdot R_{Fixed} \cdot \text{DayCountFraction}(T_{i-1}, T_i) $$
    여기서 $\text{DayCountFraction}(T_{i-1}, T_i)$는 $T_{i-1}$부터 $T_i$까지의 기간에 대한 일수 계산 관례(예: Act/360, 30/360)에 따른 비례값이다.

*   **변동 금리 레그:** 특정 기준 금리(예: SOFR, EURIBOR)에 연동되어 계약 기간 동안 변동하는 금리를 명목 원금($N$)에 곱하여 산출된 금액을 지급하거나 수취한다. 각 지급액($P_j^{Floating}$)은 다음과 같이 계산된다:
    $$ P_j^{Floating} = N \cdot F(T_{j-1}, T_j) \cdot \text{DayCountFraction}(T_{j-1}, T_j) $$
    여기서 $F(T_{j-1}, T_j)$는 $T_{j-1}$ 시점에 $T_j$까지의 기간에 대해 결정되는 선도 변동 금리(forward floating rate)이다.

전통적으로 IRS의 가치 평가는 하나의 금리 곡선을 사용하여 모든 미래 현금 흐름을 예측하고 할인하는 단일 곡선 프레임워크(Single-Curve Framework)를 따랐다. LIBOR는 이 프레임워크에서 선도 금리 예측과 할인율 모두에 사용되는 기준이었다. 특정 시점 $t_0$에서의 IRS 가치($Value_{IRS}$)는 고정 레그와 변동 레그의 미래 현금 흐름 현재 가치(Present Value, PV)의 차이로 계산된다:
$$ Value_{IRS} = PV_{Floating} - PV_{Fixed} $$
각 레그의 현재 가치는 해당 현금 흐름을 할인 인자(Discount Factor, $D(t_0, T_k)$)로 할인하여 산출된다.
$$ PV_{Fixed} = \sum_{i=1}^{M} P_i^{Fixed} \cdot D(t_0, T_i) $$
$$ PV_{Floating} = \sum_{j=1}^{K} P_j^{Floating} \cdot D(t_0, T_j) $$
여기서 $D(t_0, T_k)$는 $t_0$부터 $T_k$까지의 할인 인자를 나타낸다. 전통적으로 이 할인 인자는 LIBOR 시장에서 파생된 금리 곡선으로 구축되었다. 예를 들어, 제로 쿠폰 금리 $Z(t_0, T_k)$를 사용하면 $D(t_0, T_k) = \exp(-Z(t_0, T_k) \cdot (T_k - t_0))$ 이다.

## 3. OIS (Overnight Indexed Swap) 및 OIS 할인율의 등장

### 3.1. OIS의 정의 및 메커니즘

OIS는 변동 금리 레그가 특정 기간 동안의 일별(overnight) 금리(예: SOFR, EONIA)의 복리(compounding)로 결정되는 스왑 계약이다. 한 당사자는 고정 금리를 지급하고, 다른 당사자는 해당 기간의 일별 금리 복리 값을 지급한다. OIS는 주로 중앙은행의 기준 금리 경로에 대한 시장의 기대를 반영하며, 상대적으로 신용 리스크가 낮은 것으로 간주된다.

### 3.2. LIBOR 할인율의 한계와 OIS 할인율의 필요성

2008년 금융 위기 이후, 금융 기관 간의 신용 리스크가 부각되고 담보화(collateralization)가 일반화되면서 전통적인 LIBOR 기반 할인율의 한계가 명확해졌다.
1.  **신용 스프레드 포함:** LIBOR는 무위험(risk-free) 금리가 아니라 은행 간 신용 스프레드를 포함하고 있었다. 따라서 LIBOR를 할인율로 사용하는 것은 잠재적인 신용 리스크를 가정하는 것이며, 이는 담보화된 거래의 평가에 부적합하다.
2.  **담보화의 확산:** 대부분의 장외 파생상품 거래는 이제 신용 지원 부록(Credit Support Annex, CSA)을 통해 담보화된다. 이 경우 거래 당사자들은 일일 정산(daily margining)을 통해 담보를 교환하며, 이 담보는 대개 현금이다. 담보로 받은 현금은 일반적으로 일별 금리(예: 중앙은행 기준 금리)로 재투자되거나, 담보가 부족할 때 일별 금리로 조달된다. 따라서 담보화된 현금 흐름을 할인하는 데는 담보가치의 기회비용 또는 조달 비용을 반영하는 일별 금리가 더 적절하다.
3.  **무담보 자금 조달 비용의 차이:** 다양한 통화 및 만기별 LIBOR 금리들은 금융기관의 무담보 자금 조달 비용을 반영하므로, 서로 다른 만기의 LIBOR 금리가 무담보 금리 시장에서 완벽하게 균일한 리스크 프리미엄을 갖지 않거나, 심지어 동일한 만기라도 거래 상대방에 따라 다른 금리를 적용할 수 있다.

이러한 이유로 시장은 LIBOR 기반 할인율에서 OIS 기반 할인율로 전환되었다. OIS 금리는 담보화된 거래에서 담보를 운용하는 일별 금리(예: Fed Funds Effective Rate, EONIA, SOFR)를 가장 잘 대표하는 것으로 간주된다. 즉, OIS 할인율은 거의 무위험에 가까운 무담보 일별 자금 조달 비용을 반영하므로, 담보화된 파생상품 계약의 현금 흐름을 평가하는 데 이상적이다.

## 4. 다중 곡선 프레임워크 (Multi-Curve Framework)

OIS 할인율의 도입은 파생상품 평가에 '다중 곡선 프레임워크'를 정착시켰다. 이 프레임워크는 현금 흐름의 '예측(forecasting)'과 '할인(discounting)'을 별도의 곡선을 사용하여 수행한다.

*   **예측 곡선 (Forecasting Curve):** 파생상품의 변동 레그에서 지급될 미래의 선도 금리(forward rate)를 예측하는 데 사용된다. 이 곡선은 여전히 LIBOR 후속 지표 금리(예: SOFR, SARON, TONA) 또는 EURIBOR와 같은 은행 간 대출 금리 시장에서 파생된다. 각 통화 및 만기별로 고유한 예측 곡선이 존재한다. 예를 들어, 3개월 USD SOFR IRS의 변동 레그를 예측하기 위해 SOFR 선물 및 SOFR 스왑 데이터를 사용하여 SOFR 예측 곡선을 구축한다.
*   **할인 곡선 (Discounting Curve):** 모든 현금 흐름을 현재 가치로 할인하는 데 사용된다. 이 곡선은 통화별 OIS 시장 데이터(예: USD SOFR OIS, EUR EONIA OIS)를 사용하여 구축된다. OIS 곡선은 담보화된 거래의 평가에서 거의 무위험 할인율로 간주된다.

따라서, 다중 곡선 프레임워크에서는 IRS의 고정 레그와 변동 레그 현금 흐름 모두 OIS 할인 곡선을 사용하여 할인되지만, 변동 레그의 미래 선도 금리 예측은 해당 기준 금리에 맞는 예측 곡선을 통해 이루어진다.

## 5. 수학적 정식화 및 평가 모델

### 5.1. OIS 할인 인자 ($D_{OIS}$)

OIS 할인 곡선은 시장에서 관측되는 OIS 스왑 금리를 부트스트랩(bootstrapping)하여 생성된다. 특정 만기 $T$에 대한 OIS 할인 인자 $D_{OIS}(t_0, T)$는 해당 기간의 OIS 금리 $R_{OIS}(t_0, T)$를 사용하여 다음과 같이 유도될 수 있다 (단순화된 예):
$$ D_{OIS}(t_0, T) = \frac{1}{1 + R_{OIS}(t_0, T) \cdot (T - t_0)} $$
더 정확하게는, 일별 금리 $r_{ON}(t, t+1)$의 복리를 이용하여 다음과 같이 계산될 수 있다:
$$ D_{OIS}(t_0, T_k) = \prod_{j=t_0}^{T_k-1} \frac{1}{1 + r_{ON}(j, j+1) \cdot \text{DayCountFraction}(j, j+1)} $$
여기서 $r_{ON}(j, j+1)$은 $j$일에 시작하여 $j+1$일에 만기되는 일별 선도 금리이다. 연속 복리 기준으로 $D_{OIS}(t_0, T) = \exp(-\int_{t_0}^T f_{ON}(u) du)$ 이며, $f_{ON}(u)$는 순간 일별 선도 금리이다.

### 5.2. 선도 변동 금리 ($F(T_{j-1}, T_j)$)

다중 곡선 프레임워크에서 선도 변동 금리는 해당 예측 곡선을 통해 결정된다. $T_{j-1}$에서 $T_j$까지의 선도 금리 $F(T_{j-1}, T_j)$는 예측 곡선에 해당하는 할인 인자 $D_{Forecasting}$를 사용하여 다음과 같이 계산된다:
$$ F(T_{j-1}, T_j) = \frac{1}{\text{DayCountFraction}(T_{j-1}, T_j)} \left( \frac{D_{Forecasting}(t_0, T_{j-1})}{D_{Forecasting}(t_0, T_j)} - 1 \right) $$
여기서 $D_{Forecasting}(t_0, T_k)$는 특정 기준 금리(예: SOFR, EURIBOR)에 대한 예측 곡선에서 파생된 $t_0$부터 $T_k$까지의 할인 인자이다.

### 5.3. IRS의 가치 (Value of IRS) - OIS 할인율 적용

이제 OIS 할인율과 다중 곡선 프레임워크를 적용한 IRS의 가치 평가를 제시한다. 고정 금리를 지급하고 변동 금리를 수취하는 IRS를 가정할 때, 가치($Value_{IRS}$)는 다음과 같다:
$$ PV_{Fixed} = N \sum_{i=1}^{M} (R_{Fixed} \cdot \text{DayCountFraction}(T_{i-1}, T_i)) \cdot D_{OIS}(t_0, T_i) $$
$$ PV_{Floating} = N \sum_{j=1}^{K} (F(T_{j-1}, T_j) \cdot \text{DayCountFraction}(T_{j-1}, T_j)) \cdot D_{OIS}(t_0, T_j) $$
$$ Value_{IRS} = PV_{Floating} - PV_{Fixed} $$
여기서 $D_{OIS}(t_0, T_k)$는 OIS 할인 곡선에서 파생된 할인 인자이며, $F(T_{j-1}, T_j)$는 해당 예측 곡선에서 파생된 선도 변동 금리이다.

## 6. 실무적 함의 및 리스크 관리

OIS 할인율의 도입은 금융 시장에 여러 가지 중요한 함의를 가져왔다.
*   **가격 일관성:** 담보화된 파생상품 간의 가격 일관성이 향상되었다. 모든 거래가 동일한 무위험(OIS) 할인율을 사용하므로, 아비트라지(arbitrage) 기회가 줄어들고 시장 효율성이 증대되었다.
*   **리스크 관리:** 신용 리스크와 금리 리스크를 보다 명확하게 분리하여 관리할 수 있게 되었다. OIS 할인율은 금리 리스크에 초점을 맞추고, 신용 리스크는 CVA(Credit Value Adjustment), DVA(Debt Value Adjustment), FVA(Funding Value Adjustment)와 같은 별도의 평가 조정(XVA)을 통해 관리된다.
*   **시스템 요구사항:** 다중 곡선 프레임워크를 지원하기 위해 기존의 파생상품 평가 및 리스크 관리 시스템은 상당한 업그레이드가 필요했다. 여러 통화 및 기준 금리에 대한 다양한 예측 곡선과 OIS 할인 곡선을 동시에 관리하고 부트스트랩하는 기능이 필수적이다.
*   **ISDA 프로토콜:** 산업 표준화 기구인 ISDA(International Swaps and Derivatives Association)는 OIS 할인율로의 전환을 용이하게 하기 위해 여러 프로토콜을 발표했으며, 이는 시장 참여자들의 전환을 가속화했다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter (사양)           | Description (설명)                                     | Value (값)                       | Unit (단위)      | Notes (비고)                                  |
|:---------------------------|:-------------------------------------------------------|:---------------------------------|:-------------------|:----------------------------------------------|
| **Discounting Curve Basis** | Standard basis for discount factors in major currencies | OIS (e.g., SOFR OIS, EONIA OIS)  | N/A                | Post-2008 financial crisis standard          |
| **Forecasting Curve Basis** | Reference rates for floating leg projections          | SOFR, EURIBOR, SARON, TONA       | N/A                | Depends on currency and contract type        |
| **Yield Curve Bootstrapping Method** | Algorithm for constructing yield curves from market data | Nelson-Siegel, Svensson, or Cubic Spline Interpolation | N/A | Commonly used numerical methods            |
| **Typical IRS Tenor Range** | Standard range of maturities for IRS contracts       | 1 year to 50 years               | Years              | Most liquid tenors are 2Y, 5Y, 10Y, 30Y      |
| **Collateralization Threshold** | Minimum uncollateralized exposure before margin call | 0 to 100,000                     | USD equivalent     | [데이터 수집 대기 중] |
| **Day Count Convention**   | Standard for calculating interest accrual days       | Actual/360, 30/360, Actual/365   | N/A                | Specified in contract terms (e.g., ISDA)     |
| **Basis Spread Definition** | Spread between forecasting and discounting curves    | Basis points (bp)                | bp                 | Explicitly quoted in basis swap markets      |
| **Numerical Precision for PV** | Required accuracy for Present Value calculations    | 1.0E-06                          | Currency unit      | Industry standard for pricing convergence   |