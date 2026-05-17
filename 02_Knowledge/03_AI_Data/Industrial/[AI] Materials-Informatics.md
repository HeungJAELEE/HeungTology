---
metadata:
  id: "[[[AI] Materials-Informatics]]"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[AI] Materials-Informatics에 관한 고밀도 지능 노드"
semantic:
  tags: ["#03_AI_Data", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [AI] Materials-Informatics

## 1. [왜 배우는가? (Why)]
소재 정보학(Materials Informatics, MI)은 새로운 배터리 활물질이나 반도체 신소재를 개발하는 데 소요되는 막대한 시간(평균 10~20년)과 비용을 인공지능과 데이터 과학을 통해 획기적으로 단축하는 '디지털 소재 혁명'의 핵심 분야입니다. 과거의 시행착오(Trial-and-Error) 방식에서 벗어나, 원자 수준의 물리량과 결정 구조 데이터를 학습한 AI가 목표 물성(전도성, 내열성, 에너지 밀도 등)을 만족하는 최적의 후보 물질을 사전에 선별하거나 역으로 설계(Inverse Design)합니다. 소재 경쟁력이 곧 국가와 기업의 핵심 자산인 시대에, MI는 연구의 불확실성을 제거하고 시장 선점 속도를 10배 이상 가속화하는 연구개발의 '지능형 나침반'입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---:|:---:|:---|
| **Prediction Acc.** | RMSE (Formation Energy) | $< 0.05 \text{ eV/atom}$ | 물리 시뮬레이션(DFT) 대비 오차 최소화 |
| **Search Space** | Screening Speed | $> 10^6 \text{ compounds/sec}$ | 광대한 화합물 조합 공간의 초고속 탐색 |
| **DFT Speedup** | Surrogate Modeling | $1,000 \times \sim 10,000 \times$ | 양자 역학 시뮬레이션을 AI 근사 모델로 대체 |
| **Hit Rate** | Exp. Validation Success | $> 30\%$ | AI 추천 후보 중 실제 물성 목표 달성 확률 |
| **Descriptor Dim.** | Feature Vector Size | $128 \sim 512$ | 원자 정보(전기음성도, 반경 등)의 고차원 압축 |
| **GNN Layers** | Message Passing Depth | $3 \sim 6$ Layers | 원자 간의 장거리 상호작용 반영 범위 |
| **Acquisition** | Expected Improvement | Maximize | 베이지안 최적화를 통한 실험 효율 극대화 |
| **Data Fidelity** | Multimodal Integration | High | 실험(EXP)과 시뮬레이션(DFT) 데이터의 편차 보정 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 결정 그래프 신경망 (CGCNN)의 원리
결정 구조의 원자를 노드(Node)로, 결합을 에지(Edge)로 정의하여 그래프 신경망(GNN)을 구성합니다.
- **로직**: 원자 주변의 환경 정보를 메시지 패싱(Message Passing)을 통해 업데이트하며, 고유한 기하학적 특징을 유지한 채 물성을 예측합니다.
- **수식**: $v_i^{(t+1)} = v_i^{(t)} + \sum_{j \in N(i)} f(v_i^{(t)}, v_j^{(t)}, e_{ij})$

### 3.2 밀도 범함수 이론 (DFT)과의 융합
AI 모델의 정확도를 보증하기 위해 양자 역학 기반의 DFT 계산 결과를 학습 데이터로 사용합니다.
- **Kohn-Sham Functional**: $E_{xc}[\rho] = \int \rho(r) \epsilon_{xc}[\rho(r)] dr$
- AI는 DFT 계산의 고비용 연산 과정을 건너뛰는 **대리 모델(Surrogate Model)** 역할을 수행하여 전체 R&D 리소스를 최적화합니다.

### 3.3 능동 학습 (Active Learning) 및 역설계
실험 데이터가 부족한 영역(Uncertainty)을 AI가 스스로 판단하여 다음 실험을 제안합니다.
- **Inverse Design**: 목표 물성을 입력하면 생성형 AI(VAE/GAN)가 잠재 공간(Latent Space)에서 최적의 원자 배열을 생성합니다.

## 4. [코드 연결 해설 (MI Discovery Engine with Bayesian Opt.)]
아래 코드는 가용한 소재 데이터로부터 다음 최적의 실험 후보를 추천하는 능동 학습(Active Learning) 로직입니다.

```python
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel

class MIDiscoveryEngine:
    """
    HDS-Gold V6.3.7 규격의 소재 정보학 최적화 엔진
    """
    def __init__(self, search_space):
        self.search_space = search_space
        self.kernel = ConstantKernel(1.0) * RBF(length_scale=1.0)
        self.gpr = GaussianProcessRegressor(kernel=self.kernel, alpha=0.1)

    def update_and_recommend(self, observed_x, observed_y):
        """
        관측된 물성 데이터를 바탕으로 모델을 갱신하고 다음 실험 후보 추천
        """
        # 1. 가우시안 프로세스 회귀 모델 학습 (불확실성 추정)
        self.gpr.fit(observed_x, observed_y)
        
        # 2. 전 탐색 공간에 대한 예측값 및 표준 편차 산출
        mu, sigma = self.gpr.predict(self.search_space, return_std=True)
        
        # 3. Expected Improvement (EI) 획득 함수 계산
        # 탐색(Exploration)과 활용(Exploitation)의 균형
        best_f = np.max(observed_y)
        improvement = mu - best_f
        ei = improvement * self._norm_cdf(improvement / sigma) + \
             sigma * self._norm_pdf(improvement / sigma)
        
        # 4. EI가 최대인 지점 추천
        next_idx = np.argmax(ei)
        return self.search_space[next_idx], ei[next_idx]

    def _norm_cdf(self, x):
        return 0.5 * (1 + np.erf(x / np.sqrt(2)))

    def _norm_pdf(self, x):
        return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

# Example Usage:
# engine = MIDiscoveryEngine(candidate_pool)
# next_compound, score = engine.update_and_recommend(exp_x, exp_y)
```

## 5. [스스로 체크 (Self-Audit)]
1. **GNN** 기반의 소재 모델이 기존의 **SMILES** 문자열 기반 모델 대비 결정 구조(Crystal Structure) 표현에서 가지는 우위는?
2. **DFT** 계산값과 실제 **실험(EXP)**값 사이의 편차를 줄이기 위한 **Delta-Learning** 기법의 수리적 구조는?
3. **Materials Project**와 같은 공개 데이터베이스를 활용할 때 발생할 수 있는 **Data Sparsity** 문제와 이를 해결하기 위한 **Transfer Learning** 전략은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/Industrial/AI Generative-AI-Discovery
- 02_Knowledge/03_AI_Data/Industrial/AI Autonomous-Discovery
- 02_Knowledge/02_Battery/Materials/Battery Cathode

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
