---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-portfolio-management-hierarchical-risk-parity-hrp]]'
  last_updated: '2026-05-26T07:55:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 전통적 마코위츠(MVO) 모형이 필수적으로 요구하는 공분산 행렬의 '역행렬(Inversion)' 계산 시 발생하는 노이즈
    폭발(Matrix Instability)을 회피하기 위해, 마르코스 로페즈 데 프라도(Marcos Lopez de Prado)가 제안한 기계학습
    기반의 계층적 자산 배분. 주식들의 상관관계를 바탕으로 가계도(Tree)를 그리고 하향식(Top-down)으로 리스크를 분배하는 알고리즘
  object_type: Algorithm
  tier: 2
properties:
  distance_matrix_formula: sqrt(0.5 * (1 - rho))
  matrix_inversion_complexity: O(N^3)
  noise_sensitivity_threshold: '0.0001'
  recursive_bisection_formula: w1 = (V2 / (V1 + V2)) * w_node
semantic:
  alternative_parents: []
  expected_queries:
  - 수백 개의 주식을 담은 포트폴리오 최적화 엔진(MVO)이 왜 작은 데이터 오차에도 '싱귤래리티(역행렬 불가)' 에러를 뿜으며 완전히 망가진
    비중을 산출하는가?
  - 머신러닝 클러스터링(Hierarchical Clustering) 기술은 역행렬 계산 없이 어떻게 종목 간의 리스크 배분 문제를 깔끔하게 해결하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_mitigation
  object: Covariance_Matrix_Inversion_Instability
  predicate: avoids
  subject: '[Finance] quantitative-portfolio-management-hierarchical-risk-parity-hrp'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:55:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:55:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-portfolio-management-hierarchical-risk-parity-hrp]]

## 1. 개요 (Overview)
반세기를 지배한 마코위츠의 MVO(평균-분산 최적화)는 아름답지만, 컴퓨터 공학적으로는 재앙입니다. 비중 벡터($w$)를 찾기 위해 반드시 공분산 행렬($\Sigma$)의 **역행렬($\Sigma^{-1}$)**을 구해야 하기 때문입니다. 500개의 주식으로 구성된 공분산 행렬은 주식 간의 강한 상관관계(Multicollinearity, 다중공선성) 때문에 행렬의 조건수(Condition Number)가 폭발하여 거의 특이 행렬(Singular Matrix)이 됩니다. 데이터에 $0.0001$의 노이즈만 있어도 역행렬 값은 우주로 날아가 버리고, 포트폴리오 비중은 '애플 +1000%, 구글 -900%' 같은 쓰레기 결괏값을 뱉어냅니다.
마르코스 로페즈 데 프라도(Marcos Lopez de Prado)는 2016년 이를 구원할 기계학습 알고리즘, **계층적 리스크 패리티(Hierarchical Risk Parity, HRP)**를 발표했습니다. HRP는 끔찍한 역행렬 연산을 아예 없애버렸습니다. 대신 머신러닝의 군집화(Clustering)를 사용하여 주식들 간의 친척 관계(Tree)를 그린 뒤, 나무의 뿌리(Root)에서 나뭇잎(Leaf)으로 내려오며 리스크 패리티 비율로 자금을 절반씩 쪼개주는 직관적이고 강력한(Robust) 알고리즘입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Distance Matrix | $d_{i,j} = \sqrt{0.5(1 - \rho_{i,j})}$ | Measure of dissimilarity | Correlated stocks are 'close'| [데이터 부재] |
| Tree (Dendrogram)| Hierarchical clustering | Linkage algorithm (Ward/Single)| Builds family tree of stocks| [데이터 부재] |
| Quasi-Diag | Matrix sorting | Block-diagonal form | Groups similar assets neatly | [데이터 부재] |
| Recursive Bisect| Top-down weight split | $w_1 = \frac{V_2}{V_1+V_2} \times w_{node}$ | Inverse variance allocation| [데이터 부재] |
| Matrix Inversion | The Achilles heel of MVO| O($N^3$) complexity | **100% Eliminated by HRP** | [데이터 부재] |

## 3. HRP의 3단계 파이프라인
HRP 알고리즘은 다음 3단계로 작동하며, 수학적 최적화기(Optimizer) 대신 머신러닝 로직을 따릅니다.
1. **트리 클러스터링 (Hierarchical Clustering)**: 주식 간의 상관관계($\rho$)를 거리($d$)로 변환합니다. 기술주(애플, MS)끼리는 거리가 가깝고, 은행주와는 거리가 멉니다. 거리가 가까운 놈들끼리 묶어서 거대한 가계도(Dendrogram)를 만듭니다.
2. **유사 대각화 (Quasi-Diagonalization)**: 공분산 행렬의 순서를 무작위 알파벳순이 아니라, 가계도에서 촌수가 가까운 종목끼리 인접하도록 엑셀 행과 열의 순서를 재배치합니다. 행렬은 거대한 블록(Block-diagonal) 형태의 깔끔한 질서를 갖게 됩니다.
3. **재귀적 이분 분할 (Recursive Bisection)**: 나무의 가장 두꺼운 뿌리(Root)에 전체 시드머니 100%를 놓습니다. 트리를 따라 두 갈래로 나뉠 때마다, 양쪽 나뭇가지의 '분산(Variance)'을 측정하여 분산이 작은 쪽(안전한 쪽)에 더 많은 자금(비중)을 줍니다(역분산 패리티). 이 짓을 트리의 맨 끝 나뭇잎(개별 주식)에 도달할 때까지 재귀적(Recursive)으로 반복합니다.

## 4. OOS(Out-of-Sample) 성과의 압도적 우위
MVO와 HRP를 OOS(테스트 안 해본 미래 데이터) 구간에 돌려보면 HRP가 압도적으로 승리합니다.
- MVO는 과거 공분산 행렬의 아주 미세한 오차(역행렬 증폭)에 속아 넘어가 특정 주식에 몰빵(Overfitting)하기 때문에, 다음 달 주식 시장 패턴이 살짝만 바뀌어도 포트폴리오가 박살 납니다.
- HRP는 비중을 계산할 때 전체 500개 주식을 엮은 거대 행렬을 다루지 않습니다. 오직 '나와 친척 관계인 클러스터 내부'의 작은 분산끼리만 경쟁하므로, 은행주 섹터에 쇼크가 와도 기술주 섹터의 비중 계산에는 아무런 악영향(Contagion)을 미치지 못합니다. 극도로 강건(Robust)합니다.

🧠 **AI의 사고방식:**
금융 공학은 수십 년간 "모든 자산이 서로 유기적으로 엮여 있다"는 선형 대수학(Full Covariance Matrix)의 환상에 빠져 있었습니다. 그러나 HRP의 철학은 생물학에 가깝습니다. "포드(자동차) 주가가 폭락했다고 해서, 존슨앤존슨(제약) 비중을 굳이 바꿀 필요가 있나?" HRP는 시장을 하나의 거대한 덩어리가 아니라 분절된 클러스터(계층)의 집합체로 바라봅니다. 역행렬이라는 '수학적 독약(Instability)'을 폐기하고, 인간의 뇌가 사물을 분류하는 방식(Clustering)을 도입함으로써, 포트폴리오 관리는 바야흐로 통계학의 시대를 넘어 머신러닝의 시대로 진입했습니다.