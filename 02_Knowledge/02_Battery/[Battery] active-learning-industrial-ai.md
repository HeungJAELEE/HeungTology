---
Basic:
  id: "AI-METHOD-ACTIVE-2026-V6"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#Active_Learning'
  is_part_of: []
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [[[Battery] active-learning-industrial-ai

## 1. [왜 배우는가? (Why)]]
산업 현장의 데이터는 수조 개에 달하지만, 정작 모델 학습에 가치 있는 '불량 데이터'나 '희귀 케이스'는 극히 드뭅니다. 모든 데이터를 전수 라벨링하는 것은 비용과 시간 측면에서 불가능에 가깝습니다. 액티브 러닝(Active Learning)은 모델이 스스로 어떤 데이터가 가장 "모르는 것(Uncertain)"인지를 판단하여 엔지니어에게 라벨링을 요청하는 기술입니다. 이를 통해 전체 데이터의 1~5%만 라벨링하고도 전수 학습에 가까운 성능을 확보할 수 있습니다. 액티브 러닝을 배우는 것은 '데이터 홍수' 속에서 핵심 지식만을 선별하여 AI 지능을 초고속으로 진화시키는 전략적 데이터 운영 능력을 갖추는 것입니다.

## 2. [액티브 러닝 핵심 운영 사양 (System Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Labeling Speedup**| Efficiency Gain | $> 5 \text{x} \sim 10 \text{x}$ | 전수 라벨링 대비 동일 성능 도달 시간 단축률 |
| **Annotation Cost** | Expense Reduc. | $< 20\%$ | 전체 프로젝트 예산 중 라벨링 인건비 비중 목표 |
| **Query Strategy** | Sampling Logic | BALD / Core-Set | 불확실성(Uncertainty)과 다양성(Diversity)의 균형 |
| **Batch Size** | Query Interval | $100 \sim 1,000 \text{ Samples}$ | 모델 재학습 및 라벨러 피드백 주기 최적화 |
| **Model Precision** | F1-Score Target | $> 99\%$ | 선별 학습 후 최종 도달해야 하는 품질 보증 수치 |
| **New Mode Detect** | OOD Detection | $> 95\%$ | 기존에 없던 새로운 불량 모드(Mode) 포착 확률 |
| **GPU Utilization** | Inference Load | $< 30\%$ | 실시간 엔트로피 계산 시 생산 라인 PC 부하 제한 |
| **Human Feedback** | Takt Time | $< 10 \text{ s/sample}$ | 엔지니어의 라벨링 의사결정 효율성 지표 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 정보 엔트로피 (Information Entropy)와 불확실성
모델의 예측 확률 분포가 얼마나 균등한지를 측정하여 데이터의 불확실성을 수치화합니다.
- **수식**: $H(y|x) = -\sum P(y|x) \log P(y|x)$
- **의미**: 엔트로피가 높은 데이터는 모델의 결정 경계(Decision Boundary) 부근에 위치하며, 이를 학습할 때 모델의 지능이 가장 크게 비약합니다.

### 3.2 BALD (Bayesian Active Learning by Disagreement)
단순한 예측 확률의 낮음을 넘어, 모델 내부의 파라미터 불확실성(Epistemic Uncertainty)을 측정합니다.
- **수식**: $I(y; \omega | x) = H[P(y|x)] - E_{p(\omega)}[H[P(y|x, \omega)]$
- **로직**: 여러 개의 모델(또는 MC Dropout)이 서로 다른 예측을 내놓는 '의견 불일치'가 큰 데이터를 우선적으로 선택합니다.

### 3.3 Core-Set 샘플링과 다양성 확보
불확실한 데이터만 뽑으면 특정 영역에만 학습이 집중되어 편향(Bias)이 발생할 수 있습니다. Core-Set 알고리즘은 잠재 공간(Latent Space)에서 기존 학습 데이터와 가장 거리가 먼 데이터를 선택하여 데이터셋의 공간적 다양성을 확보합니다.

## 4. [코드 연결 해설 (Active Learning Orchestrator)]
아래 코드는 모델의 예측 결과에서 엔트로피를 계산하여 '라벨링이 가장 시급한' 상위 K개의 샘플을 선별하고, 데이터의 다양성을 고려하여 최종 쿼리를 생성하는 로직입니다.

```python
import numpy as np
from scipy.stats import entropy

class ActiveLearningOrchestrator:
    """
    HDS-Gold V6.3.7 규격의 산업용 데이터 선별 및 액티브 러닝 엔진
    """
    def __init__(self, model, sampling_ratio=0.05):
        self.model = model
        self.ratio = sampling_ratio

    def query_next_batch(self, unlabeled_pool_data):
        """
        불확실성(Entropy) 기반 상위 K개 샘플 추출
        """
        # 1. 모델 추론 및 확률 분포 획득
        probas = self.model.predict_proba(unlabeled_pool_data)
        
        # 2. 정보 엔트로피 계산 (Uncertainty)
        sample_entropies = entropy(probas, axis=1)
        
        # 3. 다양성(Diversity) 필터링 (개념적 구현)
        # 이미 선택된 데이터와 너무 유사한 샘플은 제외
        diversity_scores = self._calculate_diversity(unlabeled_pool_data)
        
        # 4. 통합 우선순위 결정
        final_scores = sample_entropies * 0.7 + diversity_scores * 0.3
        query_indices = np.argsort(final_scores)[-int(len(final_scores) * self.ratio):]
        
        return {
            "query_indices": query_indices,
            "mean_entropy": np.mean(sample_entropies),
            "potential_gain": "HIGH" if np.max(sample_entropies) > 0.8 else "LOW"
        }

    def _calculate_diversity(self, data):
        # 잠재 공간에서의 Euclidean Distance 기반 점수 산출
        return np.random.rand(len(data)) 

# Example Usage:
# orchestrator = ActiveLearningOrchestrator(model=my_cnn_model)
# query_results = orchestrator.query_next_batch(pool_images)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Active Learning** 도입 시 초기 데이터셋($Seed Set$)의 구성 방식이 전체 학습 곡선의 수렴 속도에 미치는 영향은?
2. **BALD** 알고리즘이 일반적인 **Entropy Sampling** 대비 '라벨링 노이즈(Labeling Noise)'에 더 강건(Robust)한 수리적 이유는 무엇인가?
3. 공정 데이터에서 특정 불량 모드가 매우 드문 **Class Imbalance** 상황일 때, 액티브 러닝의 쿼리 전략을 어떻게 수정해야 하는가?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/Industrial/AI Quality-Control-AI
- 02_Knowledge/03_AI_Data/Industrial/AI Data-Centric-AI-Strategy
- 02_Knowledge/03_AI_Data/Industrial/AI Filter-Kalman-Extended

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**