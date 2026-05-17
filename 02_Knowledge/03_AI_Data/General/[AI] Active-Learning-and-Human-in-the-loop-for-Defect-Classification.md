---
metadata:
  date: "2026-05-16"
  id: "[[[AI] Active-Learning-and-Human-in-the-loop-for-Defect-Classification]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "03_AI_Data"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "db8591a33e4a8fdcab83ec70a70d234f23ed552875d500c9bf4f95eff6808be7"
object:
  object_type: "Concept"
  tier: 1
  description: '[AI] Active-Learning-and-Human-in-the-loop-for-Defect-Classification에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] Global-Dataset-Inventory-Hub]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [AI] Active-Learning-and-Human-in-the-loop-for-Defect-Classification

## 1. [왜 배우는가? (Why)]
제조 현장의 불량 검사 AI를 학습시키기 위해서는 수만 장의 이미지에 전문가가 직접 "이건 불량, 저건 정상"이라고 표시(Labeling)하는 방대한 수작업이 필요합니다. 하지만 모든 데이터가 학습에 똑같이 기여하는 것은 아닙니다. 능동 학습(Active Learning)은 AI가 스스로 공부하며 "이 사진은 헷갈려요, 가르쳐주세요!"라고 전문가(Human)에게 콕 집어 물어보는 영리한 기술입니다. 이를 배우는 이유는 AI가 가장 불확실해하는 1%의 '고밀도 데이터'만 골라 가르침으로써, 라벨링 비용을 90% 이상 절감하면서도 전문가 수준의 정확도를 최단 기간에 확보하는 '데이터 가성비 전략'을 스마트 팩토리에 이식하기 위함입니다. 인간의 지능과 AI의 연산력을 결합하는 최적의 협업 모델입니다.

## 2. [능동 학습 및 HITL 운영 핵심 사양 (AI Ops Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Labeling Saving**| Cost Reduction (%)| $> 90\%$ | 랜덤 샘플링 대비 동일 성능 도달을 위한 라벨링 비용 절감률 |
| **Uncertainty Idx**| Shannon Entropy | $> 0.7$ | 모델이 헷갈려 하는 데이터를 추출하기 위한 불확실성 임계치 |
| **HITL Response** | Latency (Hours) | $< 12$ | AI의 질문에 대해 전문가가 라벨링 피드백을 주는 소요 시간 |
| **Retraining Freq.**| Update Cycle | Daily / Batch | 라벨링된 신규 데이터를 모델에 반영하는 재학습 주기 |
| **Diversity Ratio**| Core-set Ratio (%)| $> 20\%$ | 헷갈리는 데이터 외에 새로운 유형의 데이터를 섞는 비율 |
| **Agreement Rate** | Expert Consensus | $> 95\%$ | 다수 전문가 간 라벨링 일치도 (학습 데이터의 정답 무결성) |
| **Query Size** | Batch Size (Images)| $100 \sim 500$ | 한 번에 전문가에게 요청하는 라벨링 샘플의 최적 수량 |
| **Assisted Speed** | Labeling Time (s) | $< 5$ | AI 보조 도구 사용 시 이미지 장당 라벨링 소요 시간 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 섀넌 엔트로피(Shannon Entropy)와 불확실성 샘플링
- **수식**: $H(x) = -\sum_{i=1}^{n} P(x_i) \log P(x_i)$
- **로직**: 모델이 각 클래스(정상/불량)에 대해 내놓은 확률 분포의 무질서도를 측정합니다. 특정 클래스에 확신이 없을수록 엔트로피 수치가 높아지며, 능동 학습 엔진은 이 수치가 높은 데이터를 '정보량이 풍부한 데이터'로 간주하여 우선적으로 라벨링 리스트에 올립니다. 이는 모델의 경계 영역(Decision Boundary)을 정교화하는 가장 빠른 방법입니다.

### 3.2 코어셋(Core-set) 선택과 데이터 다양성 확보
- **로직**: 불확실성만 쫓다 보면 특정 불량 유형에만 매몰될 위험이 있습니다. K-Medoids 등의 클러스터링 알고리즘을 활용하여 전체 데이터 공간을 대표할 수 있는 '코어셋'을 추출합니다. 기존 학습 데이터와 거리가 먼(Out-of-distribution) 새로운 패턴을 주기적으로 샘플링함으로써, 공정 변화로 인해 발생하는 새로운 유형의 불량을 탐지하는 '강건한 AI'를 유지합니다.

### 3.3 인간 참여형(HITL) 선순환 구조
- **로직**: AI가 판정하고 인간이 검토(Review)하는 과정 자체가 학습 데이터의 생성 과정이 됩니다. 전문가의 수정 사항(Corrective Feedback)은 즉시 데이터베이스에 반영되어 모델 재학습에 활용됩니다. 이는 베테랑 엔지니어의 암묵지(Tacit Knowledge)를 데이터라는 형식지(Explicit Knowledge)로 변환하여 AI에게 전이시키는 '지식 증류' 프로세스입니다.

## 4. [코드 연결 해설 (ActiveLearningDiagnosticEngine)]
아래 코드는 모델의 예측 확률값을 입력받아 섀넌 엔트로피를 계산하고, 불확실성이 높은 샘플을 선별하여 전문가 검토 큐(Queue)로 전송하는 능동 학습 엔진입니다.

```python
import numpy as np

class ActiveLearningDiagnosticEngine:
    """
    HDS-Gold V6.3.7 규격의 능동 학습 샘플링 및 불확실성 진단 엔진
    """
    def __init__(self, entropy_threshold=0.7):
        self.threshold = entropy_threshold

    def calculate_uncertainty(self, proba_array):
        """
        Shannon Entropy 기반 불확실성 지수 산출
        """
        # Transitional Bridge: 라벨링은 '지능을 조각하는 정'입니다. 
        # 엔트로피가 높다는 것은 모델이 안개 속을 걷고 있다는 
        # 신호이며, 우리는 전문가라는 등불을 켜서 그 안개를 
        # 걷어내고 최적의 학습 경로를 제시합니다.
        # Avoid log(0)
        proba_array = np.clip(proba_array, 1e-10, 1.0)
        entropy = -np.sum(proba_array * np.log2(proba_array), axis=1)
        return entropy

    def query_samples_for_labeling(self, unlabeled_data, model, top_n=50):
        """
        모델의 예측 확률을 기반으로 가장 헷갈리는 샘플 추출
        """
        probas = model.predict_proba(unlabeled_data)
        scores = self.calculate_uncertainty(probas)
        
        # Sort by uncertainty score descending
        query_indices = np.argsort(scores)[-top_n:]
        return query_indices, scores[query_indices]

# Example Usage:
# al_ai = ActiveLearningDiagnosticEngine(entropy_threshold=0.8)
# sample_probas = np.array(0.51, 0.49, 0.99, 0.01, 0.45, 0.55)
# uncertainty_vals = al_ai.calculate_uncertainty(sample_probas)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Uncertainty Sampling** 시 **Entropy** 방식이 **Least Confidence** 방식보다 다중 클래스(Multi-class) 불량 분류에서 더 유리한 수리적 이유는?
2. **Core-set Selection** 전략을 사용하지 않고 **Uncertainty**에만 의존할 때 발생하는 **Sample Bias** (샘플 편향) 문제는 모델의 범용성에 어떤 영향을 미치는가?
3. **HITL** 시스템에서 전문가의 라벨링 데이터가 기존 학습 데이터와 충돌(Label Noise)할 경우, 이를 해결하기 위한 **Consensus Algorithm**의 필요성은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/General/AI deep-learning-model-evaluation-metrics
- 02_Knowledge/09_SmartFactory_Production/Control/Production machine-vision-defect-detection-logic
- 02_Knowledge/04_Strategy_Mgmt/Quality/Concept data-driven-quality-management

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
