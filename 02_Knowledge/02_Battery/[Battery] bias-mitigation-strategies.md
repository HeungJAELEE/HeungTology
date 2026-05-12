---
Basic:
  id: "AI-BIAS-MIT-2026-V6"
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
  tags: - '#AI_Ethics'
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

# [[[Battery] bias-mitigation-strategies

## 1. [왜 배우는가? (Why)]]
AI는 우리가 제공한 과거의 데이터를 학습하며 성장하지만, 그 데이터에는 인간 사회의 편견과 불평등이 고스란히 담겨 있는 경우가 많습니다. 편향된 AI는 채용, 금융, 공공 서비스 등 핵심 의사 결정 과정에서 특정 그룹을 부당하게 차별하며 사회적 신뢰를 파괴할 수 있습니다. 우리가 편향 완화 전략을 배우는 이유는 데이터 수집부터 모델 배포까지의 전 단계에서 편향을 수리적으로 측정하고 상쇄하는 '지능형 교정'을 수행하기 위함입니다. 공정성(Fairness)은 이제 추상적 가치가 아니라 알고리즘의 무결성과 사회적 라이선스를 증명하는 엄격한 공학적 지표입니다.

## 2. [알고리즘 공정성 및 편향 완화 핵심 사양 (Fairness Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Demographic Parity**| Statistical Parity | $\Delta < 0.1$ | 집단 간 긍정 결과 도출 비율의 최대 차이 제한 |
| **Equalized Odds** | TPR/FPR Gap | $\Delta < 0.05$ | 집단 간 기회 균등(True/False Positive) 확보 |
| **Disparate Impact** | 80% Rule (DI) | $0.8 \sim 1.25$ | 특정 집단에 대한 불균형적 영향성 평가 지표 |
| **Mutual Info.** | Bias Dependency | $I(X; S) \to 0$ | 예측값($X$)과 민감 정보($S$) 간의 의존성 제거 |
| **Accuracy Loss** | Fairness Trade-off | $< 5\%$ | 공정성 보정 시 허용되는 최대 정확도 하락폭 |
| **Auditing Latency** | Real-time Check | $< 100 \text{ ms}$ | 운영 중 편향 발생 여부를 실시간으로 모니터링 |
| **Sample Weight Var.**| Weighting Range | $0.1 \sim 10.0$ | 전처리 시 특정 샘플에 부여되는 가중치의 분산 제어 |
| **Model Drift** | Fairness Stability | $\Delta < 0.02 / mo$ | 시간에 따른 데이터 변화에도 공정성 수준 유지 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 상호 정보량 (Mutual Information) 기반 편향 측정
모델의 예측값($\hat{Y}$)이 민감 속성($S$, 성별/인종 등)에 얼마나 의존하고 있는지를 정량화합니다.
- **수식**: $I(\hat{Y}; S) = \sum P(\hat{y},s) \log \frac{P(\hat{y},s)}{P(\hat{y})P(s)}$
- **의미**: 이 값이 클수록 모델은 민감 정보를 간접적으로 활용하여 편향된 결정을 내리고 있음을 의미합니다.

### 3.2 적대적 편향 제거 (Adversarial Debiasing)
모델 학습 시 예측 성능을 높이려는 '주 모델'과 예측 결과에서 민감 정보를 찾아내려는 '적대적 모델'을 동시에 학습시킵니다.
- **수리적 기법**: 라그랑주 승수법(Lagrangian Multipliers)을 사용하여 손실 함수를 설계합니다.
- **로직**: $\mathcal{L}_{total} = \mathcal{L}_{pred} - \lambda \mathcal{L}_{adversary}$. 주 모델은 적대적 모델이 민감 정보를 맞히지 못하도록(즉, 편향을 없애도록) 학습됩니다.

### 3.3 대리 지표 (Proxy) 문제
데이터에서 민감 속성을 단순 삭제해도 거주지, 소비 패턴 등 다른 변수들이 민감 속성과 결합되어 편향을 유발합니다. 이를 해결하기 위해 상관관계가 높은 '대리 변수'들을 통계적으로 분리(De-correlation)하는 과정이 필수적입니다.

## 4. [코드 연결 해설 (Fairness Optimizer)]
아래 코드는 학습 데이터의 통계적 불균형을 해소하기 위해 집단별 샘플 가중치를 계산하고, 정확도와 공정성 사이의 트레이드오프를 분석하는 엔진입니다.

```python
import numpy as np

class FairnessOptimizer:
    """
    HDS-Gold V6.3.7 규격의 알고리즘 편향 탐지 및 완화 엔진
    """
    def __init__(self, protected_attr, label_col):
        self.attr = protected_attr
        self.label = label_col

    def calculate_reweighting(self, df):
        """
        Reweighing 기법: 특정 집단에 수리적 가중치를 부여하여 편향 상쇄
        """
        n = len(df)
        weights = {}
        for group in df[self.attr].unique():
            for label in df[self.label].unique():
                # 기대 빈도 vs 실제 빈도 비율 산출
                actual = len(df[(df[self.attr] == group) & (df[self.label] == label)])
                expected = (len(df[df[self.attr] == group]) * len(df[df[self.label] == label])) / n
                weights[(group, label)] = expected / (actual + 1e-10)
        
        return weights

    def audit_disparate_impact(self, predictions, sensitive_features):
        """
        Disparate Impact (80% Rule) 준수 여부 감사
        """
        prob_fav_group_1 = np.mean(predictions[sensitive_features == 1])
        prob_fav_group_0 = np.mean(predictions[sensitive_features == 0])
        
        di_ratio = prob_fav_group_1 / (prob_fav_group_0 + 1e-10)
        
        return {
            "di_ratio": round(di_ratio, 3),
            "status": "PASS" if 0.8 <= di_ratio <= 1.25 else "FAIL: BIAS_DETECTED"
        }

# Example Usage:
# optimizer = FairnessOptimizer(protected_attr="gender", label_col="hired")
# weights = optimizer.calculate_reweighting(training_df)
# report = optimizer.audit_disparate_impact(preds, genders)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Demographic Parity**를 강제로 맞췄을 때, 능력치 차이가 존재하는 집단 간에서 발생할 수 있는 '역차별' 리스크를 **Equalized Odds** 관점에서 설명하시오.
2. 데이터에서 민감 속성(성별, 인종)을 제거했음에도 불구하고 AI가 편향된 결과를 내놓는 원인인 **Proxy(대리 지표)** 현상의 구체적 사례는?
3. **Adversarial Debiasing** 학습 시 가중치 $\lambda$가 너무 클 때 모델의 '예측 정확도'가 급격히 떨어지는 수리적 이유는? (Constraint 최적화 관점)

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/Industrial/AI data-ethics-and-governance
- 02_Knowledge/03_AI_Data/Industrial/AI model-evaluation-and-validation
- 02_Knowledge/03_AI_Data/Industrial/AI ai-alignment-and-safety

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**