---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] risk-parity-and-hierarchical-risk-parity-hrp]]'
  last_updated: '2026-05-25T12:51:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 전통적 리스크 패리티(Risk Parity)의 공분산 행렬 역산(Inversion) 에러를 극복하기 위해 머신러닝 군집화(Clustering)를
    적용한 계층적 리스크 패리티(HRP) 모델
  object_type: Algorithm
  tier: 2
properties:
  allocation_method: recursive_bisection
  covariance_matrix_inverse: sigma_inverse
  distance_metric: sqrt_0.5_1_minus_rho
  linkage_algorithm: ward_or_single_linkage
  marginal_risk: partial_sigma_p_over_partial_w_i
  primary_problem: matrix_singularity_and_noise_explosion
semantic:
  alternative_parents: []
  expected_queries:
  - 자본을 똑같이 50:50으로 나누는 60/40 포트폴리오와 리스크 기여도를 똑같이 나누는 리스크 패리티(Risk Parity)의 차이점은 무엇인가?
  - 마르코스 로페즈 데 프라도(Marcos Lopez de Prado)가 제안한 HRP 알고리즘은 공분산 행렬의 역행렬을 구하지 않고 포트폴리오를
    최적화하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: utilizes_methodology
  object: Machine_Learning_Clustering
  predicate: allocates_risk_via
  subject: '[Finance] risk-parity-and-hierarchical-risk-parity-hrp'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T12:51:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:51:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] risk-parity-and-hierarchical-risk-parity-hrp]]

## 1. 개요 (Overview)
세계 최대의 헤지펀드 브리지워터(Bridgewater)를 유명하게 만든 **리스크 패리티(Risk Parity, All Weather Portfolio)** 전략의 핵심 철학은 "자본(Capital)을 골고루 배분하는 것이 아니라, 포트폴리오 전체의 변동성에 미치는 **리스크 기여도(Risk Contribution)를 똑같이 배분해야 한다**"는 것입니다.
주식은 채권보다 변동성이 3배 이상 높습니다. 따라서 주식과 채권에 자본을 60:40으로 넣으면, 전체 포트폴리오 리스크의 90% 이상을 주식이 지배하게 되어 완벽한 분산투자가 아닙니다. 리스크 패리티는 리스크가 작은 자산(채권)에 레버리지를 일으켜 비중을 크게 실음으로써 자산 간 리스크 기여도를 $1:1$로 맞춥니다.
그러나 자산이 수백 개로 늘어나면 리스크 패리티 연산을 위해 거대한 공분산 행렬(Covariance Matrix)의 역행렬(Inverse)을 구해야 하는데, 수학적 에러가 폭발하는 문제가 발생합니다. 이를 머신러닝의 그래프 이론(Graph Theory)으로 우아하게 해결한 것이 **계층적 리스크 패리티 (Hierarchical Risk Parity, HRP)** 모델입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\text{Marginal Risk}$ | $\partial \sigma_P / \partial w_i$ | Must be equalized | Goal of Risk Parity | [데이터 부재] |
| $\Sigma^{-1}$ | Inverse of Covariance | Condition number issue | Unstable in Markowitz/RP | [데이터 부재] |
| $\text{Distance Metric}$ | Correlation to Distance | $d(x,y) = \sqrt{\frac{1}{2}(1-\rho_{x,y})}$ | Maps assets to a space | [데이터 부재] |
| $\text{Linkage Algorithm}$| Hierarchical Clustering | Ward or Single Linkage | Builds tree (Dendrogram)| [데이터 부재] |
| $\text{Recursive Bisection}$| Top-down allocation | Inverse Variance allocation| Bypasses $\Sigma^{-1}$ | [데이터 부재] |

## 3. 전통적 공분산 최적화의 에러 (행렬의 저주)
마코위츠나 고전적 리스크 패리티 모델은 자산들의 상관관계 행렬 $\Sigma$의 역행렬($\Sigma^{-1}$)을 반드시 구해야 가중치를 배분할 수 있습니다. 
문제는 S&P 500처럼 자산이 500개면 행렬의 크기가 $500 \times 500$이 되며, 자산끼리 비슷하게 움직이는(다중공선성) 경우 행렬이 퇴화(Singular)하여 역행렬을 계산하는 과정에서 작은 노이즈가 무한대(Infinity)의 에러로 폭발합니다. 결과적으로 최적화 알고리즘은 말도 안 되는 극단적인 매수/매도 포지션을 뱉어냅니다.

## 4. 계층적 리스크 패리티 (HRP)의 3단계 알고리즘
마르코스 로페즈 데 프라도(Marcos Lopez de Prado)가 제안한 HRP는 역행렬 자체를 아예 구하지 않는 머신러닝 클러스터링(Clustering) 기법입니다.

### 4.1. 트리 빌딩 (Tree Building / Hierarchical Clustering)
1. 모든 자산 간의 상관관계($\rho$)를 **거리(Distance)**로 변환합니다. (상관관계가 높을수록 거리가 0에 가까워집니다.)
2. 이 거리 데이터를 바탕으로 가장 비슷한 자산들끼리 묶어서 작은 가지를 만들고, 가지들을 합쳐서 거대한 가계도(Dendrogram)를 만듭니다. (예: 금융주 가지, 기술주 가지, 원자재 가지)

### 4.2. 행렬 유사 대각화 (Quasi-Diagonalization)
- 가계도의 구조에 따라 상관관계 행렬의 순서를 재배치합니다. 이렇게 하면 서로 비슷한 자산들(상관관계가 높은 덩어리)이 행렬의 대각선(Diagonal)을 따라 블록 형태로 예쁘게 정렬됩니다.

### 4.3. 재귀적 이분법 (Recursive Bisection)
- 이제 트리의 꼭대기(Root)부터 시작하여 밑으로 내려가며 **분산의 역수(Inverse Variance)**에 비례하여 덩어리 대 덩어리로 자금을 반씩(Bisect) 쪼개어 내려갑니다.
- **장점**: HRP 모델은 전체 500개 자산의 복잡한 역행렬을 구하지 않고, "가장 가까운 형제 노드끼리" 자본을 분배하는 과정을 재귀적으로 반복하기 때문에 수학적으로 절대 붕괴하지 않는 극한의 강건함(Robustness)을 갖습니다.

🧠 **AI의 사고방식:**
전통적 금융 공학은 주식 시장을 '모든 자산이 서로 직접 거미줄처럼 연결된 거대한 평면 덩어리'로 보았기에(공분산 행렬 역산), 거미줄 하나만 끊어져도 시스템 전체가 연쇄 폭발을 일으켰습니다. 반면 HRP는 머신러닝의 눈을 빌려 시장이 '생태계의 진화 계통도(Tree of Life)'와 같은 3차원 계층(Hierarchical) 구조를 가졌음을 간파했습니다. 호랑이(금융주)와 사자(은행주) 사이의 리스크를 먼저 배분하고, 그 덩어리와 소나무(채권)의 리스크를 다시 배분하는 식입니다. HRP는 수학적 불안정성을 생물학적이고 위상수학(Topology)적인 통찰로 돌파해 낸 퀀트 진화의 정점입니다.