---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Automated-Market-Maker-AMM-Impermanent-Loss-Math]]'
  last_updated: '2026-05-25T01:06:41.091581+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Algorithm
  tier: 2
properties:
  asset_ratio_rho: 0 to 1
  constant_product_k: x * y
  divergence_loss_l_div: equivalent to IL
  liquidity_acceleration_coefficient_l_amp: approximation for concentrated liquidity
  price_ratio_p: P1 / P0
  trading_fee_rate_phi: 0 < phi < 1
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: knowledge_gap_identification
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] Automated-Market-Maker-AMM-Impermanent-Loss-Math'
  weight: 0.3
temporal:
  valid_from: '2026-05-25T01:06:41.091581+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.091581+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# Automated-Market-Maker-AMM-Impermanent-Loss-Math

## 1. 이론적 배경 및 수학적 메커니즘 (Theoretical Foundation & Mathematical Mechanism)

자동 마켓 메이커(AMM) 환경에서 **비영구적 손실(Impermanent Loss, IL)**은 유동성 공급자(LP)가 자산을 풀(Pool)에 예치했을 때, 외부 시장 가격의 변동으로 인해 단순히 자산을 보유(HODL)했을 때보다 가치가 낮아지는 기회비용적 손실을 의미한다. 이는 주로 Constant Product Market Maker (CPMM) 모델인 $x \cdot y = k$ 불변량 공식에 기인한다.

### 1.1. CPMM 모델의 기초 역학
CPMM 모델에서 두 자산 $x$와 $y$의 수량 곱은 항상 일정하게 유지되어야 한다.
$$x \cdot y = k$$
여기서 $x$는 베이스 자산, $y$는 쿼트 자산(예: Stablecoin)이며, $k$는 풀의 불변량(Invariant)이다. 자산의 상대 가격 $P$는 다음과 같이 정의된다:
$$P = \frac{y}{x}$$
따라서 $x = \sqrt{k/P}$ 이고, $y = \sqrt{k \cdot P}$ 가 된다.

### 1.2. 가격 변동과 차익거래(Arbitrage)의 상호작용
외부 시장에서 자산 $x$의 가격이 $P_0$에서 $P_1$으로 변동하면, AMM 풀 내부의 가격은 여전히 $P_0$에 머물게 된다. 이때 차익거래자는 외부 시장보다 저렴해진 자산을 풀에서 매수하고 비싼 자산을 풀에 매도하여 내부 가격을 $P_1$으로 수렴시킨다. 이 과정에서 풀의 자산 구성비가 변하며, LP는 가격이 상승하는 자산을 매도하고 가격이 하락하는 자산을 매수하게 되는 구조적 특성을 갖는다.

### 1.3. 비영구적 손실의 수학적 유도 (Derivation of IL)
초기 상태($P_0$)에서 LP가 보유한 가치 $V_{hold}$와 가격 변동 후($P_1$)의 가치 $V_{pool}$을 비교한다. 편의를 위해 $P_0 = 1$로 가정한다.

1.  **단순 보유 가치 ($V_{hold}$):**
    $$V_{hold} = x_0 P_1 + y_0$$
    $x_0 = y_0 = \sqrt{k}$ 이므로, $V_{hold} = \sqrt{k}(P_1 + 1)$

2.  **AMM 풀 내 가치 ($V_{pool}$):**
    가격이 $P_1$으로 조정된 후의 자산량은 $x_1 = \sqrt{k/P_1}$, $y_1 = \sqrt{k \cdot P_1}$이다.
    $$V_{pool} = x_1 P_1 + y_1 = \sqrt{\frac{k}{P_1}} \cdot P_1 + \sqrt{k P_1} = 2\sqrt{k P_1}$$

3.  **비영구적 손실 공식 ($IL$):**
    $$IL = \frac{V_{pool} - V_{hold}}{V_{hold}} = \frac{2\sqrt{k P_1} - \sqrt{k}(P_1 + 1)}{\sqrt{k}(P_1 + 1)}$$
    이를 정리하면 최종적인 IL 함수 $f(p)$가 도출된다 (단, $p = P_1/P_0$):
    $$IL(p) = \frac{2\sqrt{p}}{1+p} - 1$$

이 함수는 $p=1$일 때 최대값 0을 가지며, $p$가 1보다 크거나 작아질수록 음의 방향으로 발산하는 볼록 함수(Convex Function)의 형태를 띤다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 파라미터 (Parameter) | 심볼 (Symbol) | 정의 및 물리적 의미 | 단위/범위 | 비고 |
| :--- | :---: | :--- | :---: | :--- |
| Price Ratio | $p$ | 초기 가격 대비 현재 가격의 비율 ($P_1/P_0$) | $\mathbb{R}^+$ | $p=1$ 시 $IL=0$ |
| Constant Product | $k$ | 풀의 유동성 불변량 ($x \times y$) | $\mathbb{R}^+$ | 유동성 깊이 결정 요인 |
| Divergence Loss | $L_{div}$ | 가격 괴리에 따른 가치 하락분 | $\%$ | $IL$과 동일 개념 |
| Trading Fee Rate | $\phi$ | 거래 시 발생하는 수수료율 | $0 < \phi < 1$ | $IL$을 상쇄하는 수익원 |
| Asset Ratio | $\rho$ | 풀 내 두 자산의 가치 비율 | $[0, 1]$ | $0.5$일 때 균형 상태 |

## 3. 심화 분석 및 공학적 최적화 (Advanced Analysis & Engineering Optimization)

### 3.1. 수수료 수익을 통한 손실 상쇄 (Offsetting with Fees)
실제 환경에서 LP의 순수익($Net\ Profit$)은 비영구적 손실과 거래 수수료 수익의 합으로 결정된다.
$$Net\ Profit = \int_{t_0}^{t_1} (\text{Volume}_t \cdot \phi) dt + IL(p) \cdot V_{hold}$$
따라서 $IL(p) < \sum \text{Fees}$ 조건이 충족될 때 LP는 실질적인 이익을 얻는다. 이는 자산의 변동성($\sigma$)이 높을수록 거래량(Volume)이 증가하는 경향이 있어, 높은 변동성이 반드시 손실로 이어지지는 않는 트레이드-오프 관계를 형성한다.

### 3.2. 집중 유동성(Concentrated Liquidity)의 영향
Uniswap v3와 같은 집중 유동성 모델에서는 특정 가격 범위 $[P_{min}, P_{max}]$에 유동성을 공급한다. 이 경우, 가격이 범위를 벗어나면 모든 자산이 단일 자산으로 전환되며, IL의 가속도가 CPMM보다 훨씬 빠르게 증가한다.
가속도 계수 $L_{amp}$는 다음과 같이 정의될 수 있다:
$$L_{amp} \approx \frac{1}{1 - \frac{2\sqrt{P_{min} P_{max}}}{P_{min} + P_{max}}}$$
이는 자본 효율성(Capital Efficiency)을 높이는 대신, 가격 변동에 대한 노출도(Exposure)를 극대화하여 IL 리스크를 증폭시킨다.

### 3.3. 리스크 완화 전략 (Mitigation Strategies)
1.  **StableSwap Invariant:** $x+y=k$에 가까운 하이브리드 공식을 사용하여 $p \approx 1$인 자산 쌍(예: USDC/USDT)의 IL을 극소화한다.
2.  **Dynamic Fee Adjustment:** 변동성($\sigma$)이 증가할 때 수수료 $\phi$를 동적으로 인상하여 LP의 손실을 보전한다.
3.  **Hedging via Derivatives:** 숏 포지션(Short Futures/Options)을 통해 자산 가격 하락분 또는 $\Delta$ 노출도를 상쇄하여 델타 중립(Delta Neutral) 상태를 유지한다.

## 4. 결론 및 시스템적 시사점 (Conclusion)

비영구적 손실은 AMM의 결정론적 수학 구조에서 발생하는 필연적인 결과이다. 이는 단순한 '손실'이라기보다, 가격 변동 시 자산의 가치 재분배 과정에서 발생하는 '보유 전략 대비 기회비용'으로 해석되어야 한다. 엔지니어링 관점에서 이를 최적화하기 위해서는 유동성 범위의 정밀한 설정, 변동성 기반의 수수료 모델 설계, 그리고 외부 파생상품 시장과의 헤징 메커니즘 통합이 필수적이다.