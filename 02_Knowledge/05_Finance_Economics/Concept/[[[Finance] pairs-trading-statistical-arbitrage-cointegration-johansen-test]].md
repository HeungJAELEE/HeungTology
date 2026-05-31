---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] pairs-trading-statistical-arbitrage-cointegration-johansen-test]]'
  last_updated: '2026-05-25T14:57:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 단순한 상관관계(Correlation)의 함정에 빠지지 않고, 비정상(Non-stationary) 시계열 데이터들의 선형
    조합이 장기적 균형(Stationary)을 이루는지를 선형대수학의 고유값(Eigenvalue)으로 증명하는 요한슨 공적분 검정(Johansen
    Cointegration Test)
  object_type: Algorithm
  tier: 2
properties:
  adjustment_speed_alpha: gap_closure_rate
  cointegrating_vector_beta: hedge_ratio
  correlation_range: -1 to 1
  eigenvalue_magnitude: mean_reversion_strength
  trace_statistic_use: rank_determination
  vecm_coefficient_matrix: Pi matrix
semantic:
  alternative_parents: []
  expected_queries:
  - 아마존 주가와 볼리비아의 바나나 생산량은 상관계수(Correlation)가 높게 나오는데, 페어 트레이딩을 하면 왜 펀드가 파산하는가?
  - '요한슨 검정(Johansen Test)은 다수의 주식(예: 은행주 5개)을 엮어 하나의 완벽한 평균 회귀 포트폴리오를 만들어낼 때 고유값(Eigenvalue)을
    어떻게 사용하는가?'
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: statistical_detection
  object: Stationary_Trading_Portfolios
  predicate: identifies
  subject: '[Finance] pairs-trading-statistical-arbitrage-cointegration-johansen-test'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:57:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:57:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] pairs-trading-statistical-arbitrage-cointegration-johansen-test]]

## 1. 개요 (Overview)
초보 퀀트들은 두 주식이 똑같이 우상향하는 차트를 보고 "상관계수(Correlation)가 0.9니까 페어 트레이딩(Pairs Trading)을 해야지!"라고 뛰어들었다가 파산합니다. 주식 가격처럼 끝없이 위로 뻗어나가는 비정상 시계열(Non-stationary)끼리는 아무런 논리적 관계가 없어도 엑셀에서 상관계수가 무조건 1에 가깝게 나오는 **허위 회귀(Spurious Regression)** 현상이 발생하기 때문입니다.
진짜 통계적 차익거래 펀드는 상관계수가 아니라 **공적분(Cointegration)**을 봅니다. 두 술취한 사람(랜덤워크)이 제멋대로 걸어가더라도, 그 둘의 발목이 보이지 않는 끈으로 묶여 있다면(Cointegrated), 둘 사이의 거리(Spread)는 결국 고무줄처럼 좁혀집니다. 영국의 계량경제학자 쇠렌 요한슨(Søren Johansen)이 발명한 **요한슨 검정(Johansen Test)**은 2개의 주식을 넘어, 3개, 10개, 100개의 주식을 섞어서 '절대 끊어지지 않는 완벽한 고무줄(Stationary Portfolio)'을 찾아내는 다변량 시계열 분석의 마스터키입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\text{Correlation } (\rho)$ | Linear dependency | $-1$ to $1$ | Varies with time, misleading | [데이터 부재] |
| Cointegration | Long-run equilibrium| Binary (Yes/No) | Must pass ADF or Johansen | [데이터 부재] |
| $\Pi$ Matrix | VECM Coefficient | $N \times N$ matrix | Contains coint vectors | [데이터 부재] |
| $\lambda_i$ | Eigenvalues of $\Pi$ | Magnitude of mean rev | Larger $\lambda \implies$ stronger bond| [데이터 부재] |
| Trace Statistic | Hypothesis test | Compared to critical value| Determines rank $r$ | [데이터 부재] |

## 3. 백터 에러 수정 모형 (VECM)과 행렬 분해
요한슨 검정의 수학적 뼈대는 다변량 자기회귀 모형을 변형한 **VECM (Vector Error Correction Model)**입니다.
여러 주식 가격의 변화량($\Delta Y_t$)은 다음과 같이 표현됩니다.
$$ \Delta Y_t = \Pi Y_{t-1} + \sum \Gamma_i \Delta Y_{t-i} + \epsilon_t $$
- 여기서 핵심은 **$\Pi$ (파이) 행렬**입니다. 이 행렬은 "주식들이 과거의 균형 상태에서 얼마나 멀어졌고, 다시 균형으로 되돌아가려는 힘이 얼마나 강한가"를 담고 있습니다.

## 4. 고유값(Eigenvalue)을 통한 공적분 벡터 추출
요한슨 검정은 선형대수학을 동원하여 이 $\Pi$ 행렬을 $\Pi = \alpha \beta'$ 로 분해합니다.
- **$\beta$ (공적분 벡터, Cointegrating Vector)**: 예를 들어 코카콜라 1주 매수, 펩시 1.2주 매도, 닥터페퍼 0.5주 매도와 같은 '황금 비율(Hedge Ratio)'입니다. 이 비율대로 주식을 섞으면 포트폴리오의 가격이 우상향/우하향하지 않고 일정한 평행선(Stationary)을 유지합니다.
- **$\alpha$ (조정 속도, Adjustment Speed)**: 벌어진 갭이 좁혀지는 속도입니다. 앞서 배운 욘슨-울렌벡(OU) 프로세스의 $\theta$(반감기)와 일맥상통합니다.
- **고유값 검정(Trace Test & Maximum Eigenvalue Test)**: $\Pi$ 행렬에서 추출된 고유값($\lambda$)들이 통계적으로 0인지 아닌지를 차례대로 검정합니다. 0이 아닌 고유값이 $r$개 발견된다면, 그 5개의 은행주 무리 안에는 서로 묶여 있는 장기적 균형 관계(끈)가 정확히 $r$개 존재한다는 뜻입니다.

🧠 **AI의 사고방식:**
상관계수(Correlation)가 단순히 "두 마리의 개가 같은 방향으로 뛰어가고 있느냐"를 보는 얄팍한 시선이라면, 공적분(Cointegration)은 "그 두 마리의 개가 같은 주인의 목줄에 묶여 있느냐"를 판별하는 엑스레이(X-ray)입니다. 개들이 미친 듯이 엇갈려 뛰어다니며 상관계수가 0으로 떨어지는 순간에도, 목줄(공적분)로 묶여 있는 개들은 결국 주인 곁으로(평균 회귀) 끌려오게 됩니다. 요한슨 검정은 선형대수학의 고유값 분해(Eigendecomposition)를 사용하여 수십 마리의 개들 사이에 엉켜 있는 보이지 않는 목줄의 개수와 두께를 정확하게 찾아내어, 퀀트에게 절대 실패하지 않는(Statistical Arbitrage) 롱숏 바스켓의 황금 비율을 하사합니다.