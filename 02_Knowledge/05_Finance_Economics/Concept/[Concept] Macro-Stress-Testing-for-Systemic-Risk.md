---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Macro-Stress-Testing-for-Systemic-Risk]]'
  last_updated: '2026-05-25T01:06:41.114978+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  confidence_level_alpha: 99.0%-99.9%
  fire_sale_haircut_delta_threshold: 0.15
  leverage_ratio_lambda_threshold: 12.0
  network_density_rho_threshold: 0.3
  time_horizon_t_range: 1-8 quarters
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
  subject: '[Concept] Macro-Stress-Testing-for-Systemic-Risk'
  weight: 0.4
temporal:
  valid_from: '2026-05-25T01:06:41.114978+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.114978+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# Macro-Stress-Testing-for-Systemic-Risk (시스템적 리스크를 위한 거시 스트레스 테스트)

## 1. 개념적 정의 및 이론적 프레임워크 (Theoretical Framework)

거시 스트레스 테스트(Macro Stress Testing)는 개별 금융기관의 건전성 평가(Micro-prudential)를 넘어, 금융 시스템 전체의 상호연결성(Interconnectedness)과 피드백 루프(Feedback Loops)로 인해 발생하는 시스템적 리스크(Systemic Risk)를 정량적으로 분석하는 공학적 시뮬레이션 체계이다. 본 개념의 핵심은 특정 거시경제적 충격(Macro-shock)이 금융 네트워크 내에서 어떻게 전파(Propagation)되며, 이것이 어떻게 내생적 증폭 기제(Endogenous Amplification)를 통해 시스템 전체의 붕괴(Systemic Collapse)로 이어지는지를 모델링하는 데 있다.

시스템적 리스크는 단순한 개별 리스크의 합산이 아니며, 비선형적 전이 특성을 갖는다. 이를 해석하기 위해 통계물리학의 상전이(Phase Transition) 이론과 그래프 이론(Graph Theory)의 인접 행렬(Adjacency Matrix) 개념을 도입한다. 시스템 내 임계점(Critical Point)을 넘어서는 충격이 가해졌을 때, 개별 노드(금융기관)의 디폴트가 타 노드의 자산 가치 하락과 유동성 경색을 유발하는 연쇄 반응(Cascading Failure)을 분석하는 것이 본 테스트의 본질적 목적이다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 파라미터 (Parameter) | 기호 (Symbol) | 단위/범위 | 설명 (Technical Description) | 임계치/기준 (Threshold/Base) |
| :--- | :---: | :---: | :--- | :--- |
| Confidence Level | $\alpha$ | $\%$ | 충격 시나리오의 발생 확률 및 신뢰 수준 | $99.0\% \sim 99.9\%$ |
| Network Density | $\rho$ | $0 \le \rho \le 1$ | 금융기관 간 상호 노출액의 연결 밀도 | $\rho > 0.3$ (High Risk) |
| Fire-Sale Haircut | $\delta$ | $\%$ | 자산 급매 시 발생하는 가격 할인율 | $\delta \ge 15\%$ (Stress) |
| Time Horizon | $T$ | $\text{Quarter}$ | 스트레스 시나리오 적용 및 전파 주기 | $1 \sim 8 \text{ Quarters}$ |
| Leverage Ratio | $\lambda$ | $\text{Ratio}$ | 자기자본 대비 총자산 배수 | $\lambda > 12\text{x}$ (Fragile) |

## 3. 수학적 모델링 및 메커니즘 (Mathematical Modeling)

### 3.1. 충격 벡터 및 전이 함수 (Shock Vector & Transmission)
거시경제 충격은 벡터 $\mathbf{S}_t$로 정의되며, 이는 GDP 성장률, 금리, 부동산 가격 지수 등의 외생 변수로 구성된다.
$$\mathbf{S}_t = [s_{GDP}, s_{rate}, s_{asset}, \dots]^T$$

개별 금융기관 $i$의 손실 함수 $\mathcal{L}_i$는 외생적 충격과 타 기관으로부터 전이된 내생적 충격의 합으로 표현된다.
$$\mathcal{L}_{i, t+1} = \Phi(\mathbf{S}_t, K_{i,t}) + \sum_{j=1}^{N} A_{ij} \cdot \text{Loss}_{j,t}$$
여기서 $\Phi$는 충격 전달 함수, $K_{i,t}$는 기관 $i$의 리스크 노출액, $A_{ij}$는 기관 $i$가 기관 $j$에 대해 가지는 익스포저(Exposure)를 나타내는 가중 인접 행렬(Weighted Adjacency Matrix)이다.

### 3.2. 상호연결성에 의한 연쇄 디폴트 (Cascading Defaults)
Eisenberg-Noe 알고리즘을 확장하여, 금융 시스템의 청산 벡터(Clearing Vector) $\mathbf{p}^*$를 산출한다. 각 기관의 지급 가능 금액 $p_i$는 다음과 같은 고정점 방정식(Fixed-point Equation)을 만족해야 한다.
$$p_i = \min \left[ L_i, \max \left( 0, \sum_{j=1}^N \Pi_{ji} p_j + e_i \right) \right]$$
- $L_i$: 기관 $i$의 총 부채
- $\Pi_{ji}$: 기관 $j$의 부채 중 기관 $i$가 보유한 비율
- $e_i$: 외부로부터의 유입 자금

### 3.3. 자산 급매 및 피드백 루프 (Fire-Sale Spiral)
유동성 위기에 직면한 기관이 자산을 강제 매각할 때, 시장 가격 $P$는 매각 물량 $Q$에 반비례하여 하락하며, 이는 다시 타 기관의 평가 손실(Mark-to-Market loss)로 이어진다.
$$\Delta P = -\gamma \cdot \sum_{i=1}^N Q_{i, \text{sale}}$$
이때, 자산 가치 하락으로 인한 자본 감소 $\Delta C_i$는 다시 추가 매각을 유발하는 양의 피드백 루프(Positive Feedback Loop)를 형성한다.
$$\Delta C_i = \beta_i \cdot \Delta P \cdot H_i$$
($\beta_i$: 자산 민감도, $H_i$: 해당 자산의 보유량)

### 3.4. 시스템적 중요도 측정 (CoVaR & SRISK)
개별 기관 $i$가 시스템 전체의 리스크에 기여하는 정도를 측정하기 위해 조건부 가치리스크(CoVaR)를 사용한다.
$$\text{CoVaR}_q^{sys|i} = \text{VaR}_q (\text{Loss}_{sys} | \text{Loss}_i = \text{VaR}_q(\text{Loss}_i))$$
시스템적 리스크 기여도 $\Delta \text{CoVaR}_i$는 다음과 같다.
$$\Delta \text{CoVaR}_i = \text{CoVaR}_q^{sys|i} - \text{CoVaR}_q^{sys|median}$$

## 4. 실행 알고리즘 및 연산 프로세스 (Operational Process)

1.  **Scenario Generation**: 몬테카를로 시뮬레이션(Monte Carlo Simulation)을 통해 최악의 거시경제 경로(Worst-case Path) $\mathbf{S}_{1:T}$를 생성한다.
2.  **Initial Shock Mapping**: $\mathbf{S}_t$를 개별 금융기관의 재무제표 항목(부실채권 비율, 순이자마진 등)으로 매핑하여 1차 손실 $\mathcal{L}_{i,0}$를 계산한다.
3.  **Network Propagation**: 인접 행렬 $A$를 이용하여 기관 간 연쇄 부도 가능성을 반복 계산(Iterative Calculation)한다.
4.  **Endogenous Amplification**: 자산 급매(Fire-sale) 모델을 적용하여 시장 가격 하락 $\Delta P$와 자본 잠식의 상호작용을 시뮬레이션한다.
5.  **Systemic Aggregation**: 최종적으로 시스템 전체의 자본 감소분 $\sum \Delta C_i$와 디폴트 기관 수 $N_{def}$를 산출하여 시스템 건전성 지표를 도출한다.

본 공학적 접근법은 금융 시스템을 하나의 거대한 동적 네트워크(Dynamic Network)로 간주하며, 선형적 분석으로는 포착할 수 없는 '꼬리 리스크(Tail Risk)'와 '비선형적 전이'를 정밀하게 예측하는 것을 목표로 한다.