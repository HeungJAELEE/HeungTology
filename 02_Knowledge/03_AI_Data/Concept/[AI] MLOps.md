---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 83d3627f8c5f20f56ff0fa3840e2be092d894bd1521e6b035827d63ca6e3b732
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] MLOps]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] MLOps에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  deployment_error_rate_threshold: 0.001
  inference_api_latency_ms: 50
  kl_divergence_threshold: 0.05
  lineage_tracking_coverage: 1.0
  mttr_target_hours: 4
  psi_threshold: 0.1
  spec_version: HDS-Gold V6.3.7
  training_serving_skew_target: 0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [AI] MLOps

## 1. [왜 배우는가? (Why)]
머신러닝 모델은 개발이 완료된 시점부터 현실 데이터와의 괴리가 발생하는 '성능 저하(Model Decay)'의 운명을 지닙니다. MLOps(Machine Learning Operations)는 모델의 개발(Dev)과 운영(Ops)을 통합하여, 지속적으로 변화하는 비즈니스 환경에서도 AI 시스템이 안정적인 성능을 유지하도록 보장하는 인프라 지능화 기술입니다. MLOps를 구축하는 것은 단순히 모델을 배포하는 것을 넘어, 데이터의 변화를 실시간으로 감지하고 자동으로 재학습(Retraining)하여 시스템을 갱신하는 '자율 회복력'을 공장에 부여하는 과정입니다. 이는 AI를 실험실 도구에서 엔터프라이즈 급 산업 인프라로 격상시키기 위한 필수 요건입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---:|:---:|:---|
| **Drift Detection** | PSI (Pop. Stability Index) | $< 0.1$ (Stable) | 데이터 분포 변화 감지 임계치 (0.1~0.2 주의) |
| **Divergence** | KL-Divergence Score | $< 0.05$ | 참조 데이터와 실시간 데이터의 확률 정보 차이 |
| **Automation** | CT (Cont. Training) | Full-Auto Trigger | 성능 저하 시 수동 개입 없는 파이프라인 가동 |
| **Efficiency** | MTTR (Time to Retrain) | $< 4 \text{ hours}$ | 사고 발생 시 모델 복구까지의 소요 시간 |
| **Deployment** | Canary / Blue-Green | Error Rate $< 0.1\%$ | 무중단 및 리스크 최소화 배포 전략 |
| **Versioning** | Lineage Tracking | $100\%$ Data-Model-Code | 모델 결과에 대한 완전한 인과 추적성 확보 |
| **Latency** | Inference API Latency | $< 50 \text{ ms}$ | 실시간 서빙 성능 목표 (User Experience) |
| **Data Integrity** | Training-Serving Skew | $0$ Deviation | 피처 스토어를 통한 데이터 일관성 보장 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 드리프트 감지 (Drift Detection)의 통계적 원리
모델 성능 저하의 핵심 지표인 드리프트를 정량화하기 위해 KL-발산(Kullback-Leibler Divergence)을 사용합니다.
$$D_{KL}(P || Q) = \sum_{x \in \mathcal{X}} P(x) \log\left(\frac{P(x)}{Q(x)}\right)$$
- $P$: 원본 학습 데이터 분포, $Q$: 현재 운영 데이터 분포.
- 이 값이 임계치를 초과하면 데이터의 특성이 변했음을 의미하며, 즉시 **재학습 파이프라인**을 가동합니다.

### 3.2 지속적 학습 (CT: Continuous Training) 루프
MLOps는 기존 소프트웨어의 CI/CD에 CT를 추가합니다.
1. **Monitoring**: 드리프트 발생 감지.
2. **Data Ingestion**: 최신 데이터를 피처 스토어에서 추출.
3. **Training**: 분산 환경에서 모델 재학습.
4. **Validation**: **Champion-Challenger** 테스트를 통해 기존 모델보다 우수한지 검증.
5. **Deployment**: 우위 모델을 서빙 엔진에 배포.

### 3.3 피처 스토어 (Feature Store)의 필연성
학습 시점에 사용한 복잡한 특징 추출 로직과 실제 서빙 시점의 로직이 다르면 성능이 왜곡됩니다. 피처 스토어는 정제된 특징을 중앙에서 관리하여 **Training-Serving Skew**를 원천 차단합니다.

## 4. [코드 연결 해설 (MLOps Drift & Lifecycle Manager)]
아래 코드는 통계 지표를 실시간 감시하여 모델 재학습 및 배포를 자동화하는 MLOps 핵심 엔진 로직입니다.

```python
import numpy as np
from scipy.stats import entropy

class MLOpsLifecycleManager:
    """
    HDS-Gold V6.3.7 규격의 MLOps 드리프트 감지 및 CT 엔진
    """
    def __init__(self, model_registry, feature_store):
        self.registry = model_registry
        self.feature_store = feature_store

    def check_data_drift(self, ref_dist, curr_dist, threshold=0.1):
        """
        KL-Divergence를 이용한 데이터 드리프트 정량 분석
        """
        kl_div = entropy(ref_dist, curr_dist)
        print(f"Current KL-Divergence: {kl_div:.4f}")
        
        if kl_div > threshold:
            return self.trigger_retraining_pipeline()
        return "MODEL_STABLE"

    def trigger_retraining_pipeline(self):
        """
        자동 재학습 및 Champion-Challenger 검증 수행
        """
        new_data = self.feature_store.get_latest_batch(size=10000)
        challenger_model = self.registry.train_new_version(new_data)
        
        # 성능 비교 검증
        current_champion = self.registry.get_active_model()
        if challenger_model.accuracy > current_champion.accuracy + 0.01:
            self.registry.promote_model(challenger_model.id)
            return "CHALLENGER_PROMOTED: System Updated"
        return "RETRAINING_COMPLETE: Champion Retained"

# Example Integration:
# manager = MLOpsLifecycleManager(MyRegistry, MyFeatureStore)
# status = manager.check_data_drift(p_dist, q_dist)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Population Stability Index (PSI)**가 **KL-발산** 대비 현업 MLOps 대시보드에서 더 선호되는 해석적 이유는?
2. **Concept Drift**와 **Data Drift**를 구분하여 탐지하기 위한 타겟 변수($y$) 모니터링의 중요성은?
3. 모델 배포 시 **Shadow Deployment** 전략이 **Canary Deployment**보다 더 안전한 환경에서 수행되어야 하는 이유는?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/Data_Science_and_MLOps/AI Data-Science-Foundations
- 02_Knowledge/03_AI_Data/Governance_and_Evaluation/AI AI-TRiSM
- 02_Knowledge/03_AI_Data/Data_Science_and_MLOps/AI Feature-Engineering

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**