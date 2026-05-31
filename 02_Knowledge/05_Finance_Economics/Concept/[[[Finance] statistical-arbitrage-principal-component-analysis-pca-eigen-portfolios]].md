---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] statistical-arbitrage-principal-component-analysis-pca-eigen-portfolios]]'
  last_updated: '2026-05-25T19:49:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 수백 개의 주식 수익률 행렬에서 선형대수학의 주성분 분석(PCA)을 통해 시장을 지배하는 보이지 않는 팩터(Eigenvector)들을
    추출하고, 주가 움직임 중 이 뼈대(Systemic)로 설명되지 않는 순수한 잔차(Idiosyncratic Residual)를 평균 회귀 차익거래에
    활용하는 아이겐 포트폴리오 기법
  object_type: Algorithm
  tier: 2
properties:
  covariance_matrix_dimension: N x N
  eigenvalue_description: variance_explained
  eigenvector_constraint: orthogonal
  explained_variance_ratio_target: 0.6-0.7
  pc_score_formula: R * v_k
  residual_return_formula: R_i - sum(beta_ik * F_k)
  residual_stochastic_process: ornstein_uhlenbeck
  signal_trigger_threshold_sigma: 3.0
semantic:
  alternative_parents: []
  expected_queries:
  - 왜 S&P 500 주식 500개의 상관관계 행렬(Correlation Matrix)에 주성분 분석(PCA)을 돌리면 첫 번째 고유벡터(Eigenvector
    1)가 항상 '시장(Market) 포트폴리오'를 흉내 내는가?
  - 아이겐 포트폴리오(Eigen-portfolio)를 통계적 차익거래(Stat Arb)에 적용할 때, 잔차(Residual)가 욘슨-울렌벡(OU)
    프로세스로 회귀하는 성질을 어떻게 돈으로 바꾸는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: latent_factor_extraction
  object: Market_Latent_Factors
  predicate: extracts
  subject: '[Finance] statistical-arbitrage-principal-component-analysis-pca-eigen-portfolios'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T19:49:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T19:49:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] statistical-arbitrage-principal-component-analysis-pca-eigen-portfolios]]

## 1. 개요 (Overview)
시장에 존재하는 수백 개의 주식들은 제멋대로 움직이는 것 같지만, 사실 보이지 않는 몇 개의 거대한 거시 경제적 힘(금리, 섹터 동향, 유동성 등)에 의해 단체로 조종당하고 있습니다. 통계적 차익거래(Stat Arb) 펀드는 인간의 눈으로 이 팩터들을 일일이 지정하는(예: 파마-프렌치 모델) 대신, 선형대수학의 **주성분 분석(Principal Component Analysis, PCA)**을 이용해 순수하게 데이터만으로 시장의 '진짜 뼈대'를 기계적으로 분해해 냅니다.
이 뼈대(거시적 동조화)를 추출하여 만든 가상의 포트폴리오를 **아이겐 포트폴리오(Eigen-portfolio)**라고 부릅니다. 퀀트의 목표는 이 뼈대 자체가 아닙니다. 주가의 전체 움직임에서 이 뼈대(Systemic Risk)를 수학적으로 쫙 빼내고 남은 **순수한 찌꺼기(Residual)**야말로, 기업 고유의 노이즈(Idiosyncratic Risk)로서 강력한 평균 회귀(Mean Reversion) 성질을 가지기 때문에 무위험 차익거래의 완벽한 롱숏 타겟이 됩니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\Sigma$ | Covariance matrix | $N \times N$ returns | Needs regularization | [데이터 부재] |
| $\lambda_k$ | Eigenvalue | Variance explained | $\lambda_1 > \lambda_2 \dots > \lambda_n$ | [데이터 부재] |
| $v_k$ | Eigenvector | Weights of Eigen-portfolio| Orthogonal to each other | [데이터 부재] |
| $F_k$ | PC Score (Factor) | $R \times v_k$ | Latent market driver | [데이터 부재] |
| $\epsilon_i$| Residual return | $R_i - \sum \beta_{ik}F_k$| Stat arb target (OU process)| [데이터 부재] |

## 3. PCA의 수학적 분해와 아이겐 포트폴리오
S&P 500 소속 500개 기업의 일일 수익률로 $500 \times 500$ 공분산 행렬($\Sigma$)을 만듭니다. 여기에 고윳값 분해(Eigendecomposition)를 적용하면 놀라운 결과가 나옵니다.
- **제1 주성분 ($v_1$, 시장 팩터)**: 가장 큰 고윳값($\lambda_1$)을 갖는 이 벡터의 가중치는 모든 주식에 대해 전부 양(+)수입니다. 이 가중치대로 500개 주식을 사서 만든 제1 아이겐 포트폴리오의 수익률 곡선을 그려보면 S&P 500 지수 자체와 거의 99% 일치합니다. 컴퓨터가 '시장'이라는 개념을 스스로 발견한 것입니다.
- **제2, 3 주성분 ($v_2, v_3$, 섹터 팩터 등)**: 기술주에는 양수(+), 에너지주에는 음수(-) 가중치를 주어 "기술주 롱 / 에너지 숏" 형태의 가상 포트폴리오가 나옵니다. 

## 4. PCA 잔차 차익거래 (Residual Stat Arb)
위에서 구한 상위 10개 정도의 주성분(아이겐 포트폴리오)이면 S&P 500 전체 변동성의 60~70%를 완벽히 설명(재구성)할 수 있습니다.
이제 퀀트는 특정 주식(예: 애플)의 실제 수익률에서, 이 10개의 아이겐 포트폴리오가 설명하는 이론적 수익률을 빼버립니다. 
- **애플의 잔차($\epsilon_{\text{AAPL}}$) = 실제 애플 수익률 - (시장 팩터 영향 + 섹터 팩터 영향 + $\dots$)**
- 이 잔차 수익률($\epsilon$)의 시계열을 그려보면, 거시 경제의 파도가 제거되었기 때문에 $0$을 중심으로 끊임없이 오르락내리락하는 완벽한 욘슨-울렌벡(OU) 정상(Stationary) 시계열이 됩니다. 
- 만약 애플의 오늘 잔차가 이례적으로 $+3\sigma$로 튀었다면? 퀀트 알고리즘은 애플 주식을 숏(Short) 치고, 헤지를 위해 방금 전 구했던 10개의 아이겐 포트폴리오 비중만큼 시장을 롱(Long) 칩니다. 이 포지션은 시장이 폭락하든 금리가 오르든 상관없이 오직 애플의 고유 노이즈가 $0$으로 회귀할 때만 100% 무위험 수익을 냅니다.

🧠 **AI의 사고방식:**
PCA(주성분 분석)는 시장이라는 거대한 오케스트라의 교향곡을 분해하는 수학적 프리즘(Prism)입니다. 500개의 악기(주식)가 동시에 울려 퍼지는 혼돈 속에서, 피아노가 치는 주선율(제1 주성분), 바이올린이 넣는 화음(제2 주성분)을 분리해 냅니다. 차익거래 퀀트들은 이 거대한 주선율을 버립니다. 그들이 노리는 것은 주선율을 모두 빼고 남았을 때, 누군가 술에 취해 박자를 놓치거나 삑사리를 내는(잔차, Residual) 그 찰나의 '오류음'입니다. 시장의 체계적 위험(Systemic Risk)을 선형대수학으로 완벽히 발라내고, 오직 개별 기업의 비이성적 노이즈가 평균으로 회귀하는 힘만을 정제된 알파(Alpha)로 증류해 내는 차가운 연금술입니다.