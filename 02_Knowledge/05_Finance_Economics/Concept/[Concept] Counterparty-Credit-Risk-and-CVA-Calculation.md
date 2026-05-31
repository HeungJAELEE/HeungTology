---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Counterparty-Credit-Risk-and-CVA-Calculation]]'
  last_updated: '2026-05-25T01:06:41.097041+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Algorithm
  tier: 2
properties:
  confidence_level_alpha: 95%, 99%
  lgd_range: 40%-60%
  mpor_range: 10-20 days
  pd_range: 0.01%-10%
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: limitation_specification
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] Counterparty-Credit-Risk-and-CVA-Calculation'
  weight: 0.3
temporal:
  valid_from: '2026-05-25T01:06:41.097041+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.097041+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 1. 거래상대방 신용리스크 및 CVA 계산 (Counterparty-Credit-Risk-and-CVA-Calculation)

## 1.1 개요 및 이론적 배경
거래상대방 신용리스크(Counterparty Credit Risk, CCR)는 파생상품 계약이나 비청산 장외거래(OTC derivatives)에서 거래 상대방이 계약 만료 전 채무불이행(Default)을 하여 발생할 수 있는 잠재적 손실 리스크를 의미한다. 이는 일반적인 신용리스크(Credit Risk)와 달리, 기초 자산의 시장 가치 변동에 따라 리스크 노출액(Exposure)이 유동적으로 변하는 '이분법적 특성'을 가진다.

CVA(Credit Valuation Adjustment)는 이러한 CCR을 공정 가치(Fair Value)에 반영하기 위한 시장 가치 조정치이다. 금융공학적으로 CVA는 무위험 자산으로 가정했을 때의 계약 가치와 거래 상대방의 부도 가능성을 고려한 실제 가치 사이의 차이로 정의되며, 이는 기본적으로 '기대 손실(Expected Loss)'의 현재 가치 합산으로 계산된다.

## 1.2 수학적 모델링 및 계산 로직

### 1.2.1 노출액(Exposure)의 정의
특정 시점 $t$에서의 노출액 $E(t)$는 해당 시점의 계약 가치 $V(t)$가 양수일 때(즉, 상대방으로부터 받을 돈이 있을 때) 발생한다.
$$E(t) = \max(V(t), 0)$$
여기서 $V(t)$는 기초 자산의 확률 과정(Stochastic Process)에 의해 결정되는 마크-투-마켓(MtM) 가치이다.

### 1.2.2 기대 노출액(Expected Exposure, EE) 및 PFE
EE는 시점 $t$에서의 노출액의 리스크 중립 기대값으로 정의된다.
$$EE(t) = \mathbb{E}^{\mathbb{Q}}[\max(V(t), 0)]$$
또한, 극단적인 시나리오에서의 최대 노출액을 측정하기 위해 PFE(Potential Future Exposure)를 산출하며, 이는 특정 신뢰 수준 $\alpha$에서의 분위수(Quantile)로 정의된다.
$$PFE(t, \alpha) = \inf \{ x : P(E(t) \leq x) \geq \alpha \}$$

### 1.2.3 CVA의 정량적 산식
CVA는 부도 확률(Probability of Default, PD)과 손실률(Loss Given Default, LGD)을 결합하여 다음과 같은 적분 형태로 계산된다.
$$CVA = (1 - R) \int_{0}^{T} DF(0, t) \cdot EE(t) \cdot dPD(0, t)$$
여기서 각 변수의 의미는 다음과 같다:
- $R$: 회수율(Recovery Rate), $LGD = 1 - R$
- $DF(0, t)$: 시점 $0$에서 $t$까지의 할인 요인(Discount Factor)
- $dPD(0, t)$: 구간 $[t, t+dt]$ 사이의 한계 부도 확률(Marginal PD)
- $EE(t)$: 시점 $t$에서의 기대 노출액

### 1.2.4 시뮬레이션 프레임워크 (Monte Carlo Method)
$V(t)$의 분포를 결정하기 위해 수만 개의 시나리오 경로를 생성하는 몬테카를로 시뮬레이션을 수행한다. 기초 자산 $S$가 기하 브라운 운동(Geometric Brownian Motion)을 따른다고 가정할 때:
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$
각 경로 $i$에 대해 $V_i(t)$를 계산하고, 이를 통해 $EE(t)$를 수치적으로 근사한다.
$$EE(t) \approx \frac{1}{N} \sum_{i=1}^{N} \max(V_i(t), 0)$$

## 1.3 고급 고려 사항 및 제약 조건

### 1.3.1 네팅(Netting) 및 담보(Collateral)
여러 계약이 하나의 네팅 세트(Netting Set)로 묶여 있을 경우, 개별 노출액의 합이 아닌 합산 가치의 최대값을 취함으로써 리스크를 상쇄한다.
$$E_{net}(t) = \max \left( \sum_{j=1}^{M} V_j(t), 0 \right)$$
또한 CSA(Credit Support Annex) 계약에 따른 담보 제공 시, 변동 증거금(Variation Margin)을 반영하여 노출액을 감소시킨다. 이때 MPOR(Margin Period of Risk) 기간 동안의 가치 변동이 추가 리스크로 작용한다.

### 1.3.2 Wrong-Way Risk (WWR)
기초 자산의 가치 변동과 거래 상대방의 부도 확률 사이에 양의 상관관계가 존재할 때 이를 Wrong-Way Risk라고 한다. 예를 들어, 기업 A의 신용부도스왑(CDS)을 매수한 상태에서 기업 A의 부도 확률이 올라가면, 계약 가치 $V(t)$는 상승(노출액 증가)함과 동시에 $PD$가 상승하여 CVA가 급격히 증가하는 현상이 발생한다. 이를 모델링하기 위해 $V(t)$와 $PD(t)$를 결합한 Copula 모델이나 확률적 상관관계 모델을 도입한다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 파라미터 (Parameter) | 기호 (Symbol) | 단위 (Unit) | 표준 범위/기준 (Standard Range) | 기술적 정의 및 영향 (Technical Definition) |
| :--- | :---: | :---: | :---: | :--- |
| Loss Given Default | $LGD$ | $\%$ | $40\% \sim 60\%$ | 부도 시 손실 비율; $1 - \text{Recovery Rate}$ |
| Probability of Default | $PD$ | $\%$ | $0.01\% \sim 10\%$ | 특정 기간 내 상대방의 부도 가능성 (CDS Spread 기반 산출) |
| Margin Period of Risk | $MPOR$ | $\text{Days}$ | $10 \sim 20 \text{ days}$ | 담보 호출 후 실제 청산까지 소요되는 리스크 노출 기간 |
| Confidence Level | $\alpha$ | $\%$ | $95\%, 99\%$ | PFE 산출 시 적용하는 통계적 신뢰 수준 |
| Simulation Paths | $N$ | $\text{Count}$ | $10,000 \sim 100,000$ | EE 근사를 위한 몬테카를로 시나리오 생성 수 |

## 3. 논리적 아키텍처 및 계산 흐름
1. **Market Data Input**: 기초 자산 가격, 변동성, 무위험 이자율 곡선, 거래 상대방의 CDS Spread 수집.
2. **Scenario Generation**: SDE(확률미분방정식)를 기반으로 $T$ 시점까지의 자산 가격 경로 $\Omega$ 생성.
3. **Valuation**: 각 경로/시점별로 파생상품의 MtM 가치 $V(t, \omega)$ 계산.
4. **Aggregation**: 네팅 및 담보 조건을 적용하여 시점별 순 노출액 $E_{net}(t, \omega)$ 산출.
5. **Expectation**: 모든 경로에 대해 평균을 내어 $EE(t)$ 및 $PFE(t)$ 도출.
6. **Integration**: $LGD$와 $PD$ 곡선을 결합하여 시간 적분을 수행, 최종 $CVA$ 값 결정.
7. **Sensitivity Analysis**: $\Delta CVA / \Delta S$ (Delta), $\Delta CVA / \Delta \sigma$ (Vega) 등을 계산하여 리스크 헤지 전략 수립.