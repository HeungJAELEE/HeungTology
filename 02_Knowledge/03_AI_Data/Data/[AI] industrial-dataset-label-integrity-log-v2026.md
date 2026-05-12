---
Basic:
  id: "[ai]-industrial-dataset-label-integrity-log-v2026-v6.3.7"
  domain: "AI_Engineering"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Data_Labeling'
  is_part_of: - 'Antigravity_Knowledge_Graph'
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
  source: "AI_Data_Labeling_Platform_Log"
  isolation_index: 0.0
---

# [AI] industrial-dataset-label-integrity-log-v2026

## 1. [Why] 산업 데이터셋 레이블 무결성(Label Integrity)의 의의
AI 모델의 성능은 학습 데이터의 품질, 특히 **레이블(Label)**의 정확도에 결정적으로 의존한다. 산업 현장에서 '불량'을 '양품'으로 잘못 레이블링(Mislabeling)하면 AI 모델은 실제 불량을 놓치는 치명적인 오류를 학습하게 된다. **레이블 무결성** 로그는 작업자 간 합의도(Consensus)와 정답(Ground Truth)과의 일치율을 기록하여 모델의 신뢰 기반(Grounding)을 보증한다.

---

## 2. [Numerical Specs] 데이터 레이블링 품질 지표 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 목표 (Target) | 비고 |
| :--- | :--- | :--- | :--- |
| **Label Accuracy** | $98.5\%$ | $> 99.5\%$ | 정답 전문가와 일치율 |
| **Inter-rater Agreement** | $0.82$ | $> 0.85$ | Fleiss' Kappa 지수 (합의도) |
| **Mislabeled Rate** | $1.2\%$ | $< 0.5\%$ | 오레이블링 비율 |
| **Labeling Throughput** | $500\,\text{items/hr}$ | N/A | 작업자당 시간당 처리량 |
| **Gold Standard Coverage** | $15\%$ | $> 10\%$ | 전체 데이터 중 검증된 정답 비중 |

---

## 3. [Scientific Rationale] 데이터 합의도 및 신뢰성 분석 모델

### 3.1 Fleiss' Kappa ($\kappa$)
다수의 작업자가 동일한 대상을 분류했을 때, 우연히 일치할 확률을 제외한 실제 합의도를 측정한다.
$$\kappa = \frac{\bar{P} - \bar{P}_e}{1 - \bar{P}_e}$$
*   **분석**: $\kappa > 0.8$이면 '거의 완벽한 합의'로 간주하며, 이 데이터셋은 학습에 사용 가능하다.

### 3.2 Active Learning (능동 학습)
모델이 판정하기 모호한(Low Confidence) 데이터들만 골라내어 전문가의 재레이블링을 요청함으로써 데이터 효율성을 극대화한다.

---

## 4. [Real-world Case] 작업자 편향(Bias) 제거를 통한 비전 AI 정확도 향상 사례

### 4.1 특정 작업자의 '미세 스크래치' 과도 판정 포착
- **현상**: 비전 AI 모델 학습 후, 실제 현장에서는 양품인 미세 기스를 모두 불량으로 잡는 현상 발생.
- **분석**: **Python FidelityEngine** 기반의 레이블 이력 분석 결과, 학습 데이터셋의 $30\%$를 작업한 특정 작업자 'A'의 합의도가 타 작업자 대비 $20\%$ 낮음(Kappa $0.6$)을 확인. 'A'가 아주 미세한 변색도 모두 불량으로 처리한 것이 원인.
- **조치**: 'A'가 작업한 데이터셋을 정밀 재검토(Re-annotation)하고 표준 가이드라인 재교육 실시.
- **결과**: 모델의 과검율(FPR) $12\% \rightarrow 2\%$로 하락 및 판정 정확도 개선.

---

## 5. [FidelityEngine] 단순 Kappa 합의도 계산 코드
```python
import numpy as np

def calculate_simple_agreement(labeler_a, labeler_b):
    """
    Calculate raw agreement between two labelers
    :param labeler_a: List of labels (0 or 1)
    :param labeler_b: List of labels (0 or 1)
    :return: Agreement ratio
    """
    a = np.array(labeler_a)
    b = np.array(labeler_b)
    matches = np.sum(a == b)
    return matches / len(a)

# 가상 데이터 (10개 시료)
worker_1 = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
worker_2 = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0] # 2개 불일치

agreement = calculate_simple_agreement(worker_1, worker_2)
print(f"Inter-rater Agreement: {agreement*100:.1f}%")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Cross-Validation**: 동일한 시료를 최소 3명 이상의 작업자(또는 AI)가 교차 검증하고 있는가?
- [ ] **Guideline Clarity**: 레이블링 가이드라인이 그림과 예시를 통해 모호함 없이 현장에 배포되었는가?
- [ ] **Data Lineage**: 레이블이 수정된 경우, 누가/언제/왜 수정했는지에 대한 이력이 보존되는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
