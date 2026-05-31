---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Overcollateralized-Lending-Protocols-Aave-Compound]]'
  last_updated: '2026-05-25T01:06:41.121317+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  health_factor_threshold: 1.0
  liquidation_bonus_range: 5%~15%
  liquidation_threshold_range: 80%~90%
  ltv_range: 50%~80%
  oracle_latency_threshold: < 1 minute
  utilization_kink_range: 80%~90%
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: systemic_constraint_specification
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] Overcollateralized-Lending-Protocols-Aave-Compound'
  weight: 0.85
temporal:
  valid_from: '2026-05-25T01:06:41.121317+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.121317+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 과담보 대출 프로토콜 (Overcollateralized Lending Protocols: Aave, Compound)

## 1. 기술적 개요 및 시스템 아키텍처 (Technical Overview & Architecture)

과담보 대출 프로토콜은 신뢰 기반의 신용 평가 시스템 없이 스마트 계약(Smart Contract)의 결정론적 로직(Deterministic Logic)만을 이용하여 자산의 유동성을 공급하고 차입하는 탈중앙화 금융(DeFi)의 핵심 인프라이다. 본 시스템의 핵심 설계 철학은 '무신뢰성(Trustlessness)'과 '시스템적 솔벤시(Systemic Solvency)'의 유지에 있으며, 이를 위해 차입자는 반드시 차입하고자 하는 자산의 가치보다 높은 가치의 담보 자산을 프로토콜에 예치해야 한다.

### 1.1 유동성 풀 모델 (Liquidity Pool Model)
전통적인 P2P 대출과 달리 Aave와 Compound는 P2P(Peer-to-Peer)가 아닌 P2P(Peer-to-Pool) 모델을 채택한다. 모든 공급자는 자산을 단일 유동성 풀에 예치하며, 이에 대한 증표로 yield-bearing 토큰(예: aToken, cToken)을 발행받는다.

이 시스템의 총 유동성 $L$은 다음과 같이 정의된다:
$$L_{total} = \sum_{i=1}^{n} D_i$$
여기서 $D_i$는 $i$번째 공급자가 예치한 자산의 양을 의미한다. 차입자는 풀의 가용 유동성 범위 내에서 자신의 담보 가치에 비례하여 자산을 인출할 수 있다.

### 1.2 동적 이자율 결정 알고리즘 (Dynamic Interest Rate Model)
이자율은 시장의 수요와 공급, 즉 유동성 이용률(Utilization Rate, $U$)에 의해 실시간으로 결정된다. 이용률 $U$의 정의는 다음과 같다:
$$U = \frac{\text{Total Borrows}}{\text{Total Liquidity}} = \frac{B}{C}$$

이자율 곡선은 일반적으로 'Kink'라고 불리는 굴절점을 포함한 선형 함수 모델을 따른다. 이는 이용률이 특정 임계값($U_{kink}$)을 넘어서면 유동성 부족 리스크를 방지하기 위해 이자율을 급격히 상승시켜 차입을 억제하고 상환을 유도하는 메커니즘이다.

- **$U \le U_{kink}$ 일 때:** $R_t = R_0 + \frac{U}{U_{kink}} \cdot R_{slope1}$
- **$U > U_{kink}$ 일 때:** $R_t = R_0 + R_{slope1} + \frac{U - U_{kink}}{1 - U_{kink}} \cdot R_{slope2}$

여기서 $R_t$는 현재 이자율, $R_0$는 기본 이자율, $R_{slope1}$과 $R_{slope2}$는 각각 굴절점 이전과 이후의 기울기를 의미한다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 파라미터 (Parameter) | 기술적 정의 (Technical Definition) | 일반적 범위/값 (Typical Range) | 영향도 (Impact) | 단위 (Unit) |
| :--- | :--- | :--- | :--- | :--- |
| **LTV (Loan-to-Value)** | 최대 담보 인정 비율 (Max Loan Ratio) | 50% $\sim$ 80% | 초기 차입 가능 한도 결정 | Percentage (%) |
| **Liquidation Threshold** | 청산 임계값 (Threshold for Liquidation) | 80% $\sim$ 90% | 청산 실행 시점 결정 | Percentage (%) |
| **Liquidation Bonus** | 청산인 인센티브 (Liquidator Incentive) | 5% $\sim$ 15% | 청산 속도 및 효율성 결정 | Percentage (%) |
| **Utilization Kink** | 이자율 급증 임계점 (Interest Rate Kink) | 80% $\sim$ 90% | 유동성 고갈 방지 지점 | Percentage (%) |
| **Oracle Latency** | 가격 피드 업데이트 지연 시간 | $< 1$ minute | 청산 갭 및 가격 조작 리스크 | Seconds (s) |

## 3. 리스크 관리 및 솔벤시 메커니즘 (Risk Management & Solvency)

### 3.1 건강 지수 (Health Factor, HF)
프로토콜은 각 차입 계정의 건전성을 평가하기 위해 '건강 지수(Health Factor)'를 실시간으로 계산한다. HF는 차입자의 담보 가치가 청산 임계값 대비 얼마나 여유가 있는지를 나타내는 지표이다.

$$HF = \frac{\sum_{i=1}^{n} (\text{Collateral}_i \times \text{Liquidation Threshold}_i)}{\text{Total Borrowed Value in Base Currency}}$$

- $HF > 1$: 계정은 안전한 상태이며 정상적인 운영이 가능하다.
- $HF < 1$: 계정은 'Undercollateralized' 상태가 되며, 외부 청산인(Liquidator)에 의해 즉각적인 청산 대상이 된다.

### 3.2 청산 프로세스 및 인센티브 구조 (Liquidation Logic)
HF가 1 미만으로 떨어지면, 프로토콜은 스마트 계약을 통해 청산인의 개입을 허용한다. 청산인은 차입자의 부채 일부 또는 전부를 대신 상환하고, 그 대가로 차입자의 담보 자산을 시장가보다 할인된 가격(Liquidation Bonus 적용)으로 획득한다.

청산인이 획득하는 담보 가치 $V_{coll}$은 다음과 같이 계산된다:
$$V_{coll} = \text{Repaid Amount} \times (1 + \text{Liquidation Bonus})$$

이 메커니즘은 프로토콜의 부실 채권 발생 가능성을 최소화하고, 시장 변동성 상황에서도 시스템 전체의 자산 건전성을 유지하는 자동화된 안전장치 역할을 한다.

## 4. 수치적 무결성 및 오라클 의존성 (Numerical Integrity & Oracle Dependency)

과담보 대출 시스템의 가장 취약한 지점은 자산 가치 평가를 위한 외부 가격 피드(Oracle)의 정확성이다. $HF$ 계산에 사용되는 $\text{Collateral}_i$의 가치는 실시간 시장 가격 $P_i$에 의존한다.

$$\text{Collateral Value} = \sum (\text{Asset Amount}_i \times P_i)$$

만약 오라클에 의한 가격 조작(Price Manipulation)이나 지연(Latency)이 발생할 경우, 실제 가치는 충분함에도 불구하고 $HF < 1$이 되어 부당한 청산이 발생하거나, 반대로 가치가 하락했음에도 청산이 이루어지지 않아 프로토콜에 배드 뎁트(Bad Debt)가 누적될 수 있다. 이를 방지하기 위해 Aave와 Compound는 Chainlink와 같은 분산형 오라클 네트워크(DON)를 사용하여 다중 소스의 가격 평균값을 채택하고, 급격한 가격 변동 시 필터링 메커니즘을 적용한다.

## 5. 결론 및 공학적 시사점

과담보 대출 프로토콜은 수학적으로 정의된 LTV와 HF를 통해 신용 리스크를 완전히 제거하고, 유동성 이용률 기반의 이자율 곡선을 통해 시장 효율성을 극대화한 금융 공학적 시스템이다. 본 시스템의 안정성은 $\text{LTV} < \text{Liquidation Threshold} < 100\%$ 라는 엄격한 부등식의 유지와, 오라클의 실시간 정확도 및 청산인의 즉각적인 차익거래 활동이라는 세 가지 축에 의해 지탱된다.