---
Basic:
  id: "[data]-smart-factory-machine-vision-fpr-fnr-log-v2026-v6.3.7"
  domain: "AI_Engineering"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Data"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Machine_Vision'
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
  source: "Vision_Inspection_System_Log"
  isolation_index: 0.0
---

# [[[Data] smart-factory-machine-vision-fpr-fnr-log-v2026

## 1. [Why]] 머신 비전 FPR/FNR 로그의 품질 공학적 의의
AI 기반 머신 비전 검사 시스템에서 **과검율(FPR)**과 **미검율(FNR)**은 공정의 생산성과 품질 신뢰성을 결정하는 핵심 지표다. 과검(양품을 불량으로 판정)이 높으면 불필요한 재작업과 폐기 비용이 발생하고, 미검(불량을 양품으로 판정)이 발생하면 치명적인 품질 사고로 이어진다. 본 노드는 검사 시스템의 혼동 행렬(Confusion Matrix)을 실시간 분석하여 최적의 판정 임계치(Threshold)를 사수하는 데이터를 제공한다.

---

## 2. [Numerical Specs] 비전 검사 성능 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 목표 (Target) | 비고 |
| :--- | :--- | :--- | :--- |
| **FPR (Over-kill Rate)** | $0.85\%$ | $< 1.0\%$ | 생산성 저하 지표 |
| **FNR (Under-kill Rate)** | $0.005\%$ | $< 0.01\%$ | 품질 유출 지표 (Critical) |
| **Accuracy** | $99.1\%$ | $> 99.5\%$ | 전체 판정 정확도 |
| **Recall (Sensitivity)** | $99.995\%$ | $> 99.99\%$ | 불량을 불량으로 맞출 확률 |
| **Precision** | $94.2\%$ | $> 95.0\%$ | 불량 판정 중 실제 불량 비율 |

---

## 3. [Scientific Rationale] 판정 임계치 및 성능 분석 모델

### 3.1 Confusion Matrix (혼동 행렬)
모델의 예측값과 실제 정답(Ground Truth)을 4가지 경우로 분류하여 분석한다.
*   **TP (True Positive)**: 불량을 불량으로 정판.
*   **TN (True Negative)**: 양품을 양품으로 정판.
*   **FP (False Positive)**: 양품을 불량으로 오판 (FPR).
*   **FN (False Negative)**: 불량을 양품으로 오판 (FNR).

### 3.2 Precision-Recall Curve (PR 곡선)
판정 임계치를 조절함에 따라 정밀도와 재현율 사이의 트레이드오프를 시각화하고 최적점(Optimal Point)을 도출한다.

---

## 4. [Real-world Case] 조명 노후화에 따른 과검율(FPR) 급증 해결 사례

### 4.1 특정 검사기의 과검율이 $0.5\% \rightarrow 3.2\%$로 상승
- **현상**: 조립 최종 검사 단계에서 양품 롯트임에도 불구하고 '표면 스크래치 불량' 알람이 빈번하게 발생하여 라인 정지 횟수 증가.
- **분석**: **Python FidelityEngine** 기반의 로그 분석 결과, 이미지 전체의 평균 밝기가 $15\%$ 감소함에 따라 AI 모델이 먼지를 스크래치로 오판하는 경향 포착. 이는 LED 조명의 수명 저하에 따른 광량 감소로 판별됨.
- **조치**: 조명 모듈을 교체하고, 변화된 광량 조건에 맞춰 AI 모델의 신뢰도 임계치(Confidence Threshold)를 $0.85$에서 $0.90$으로 미세 조정.
- **결과**: 과검율 $0.6\%$로 즉시 안정화 및 생산 가동률 복구.

---

## 5. [FidelityEngine] FPR, FNR 및 정확도 산출 코드
```python
def calculate_vision_metrics(tp, tn, fp, fn):
    """
    Calculate performance metrics for vision system
    :return: dict of results
    """
    total = tp + tn + fp + fn
    accuracy = (tp + tn) / total if total > 0 else 0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0
    
    return {
        "Accuracy (%)": accuracy * 100,
        "FPR (%)": fpr * 100,
        "FNR (%)": fnr * 100
    }

# 실측 데이터 대입 (검사 10,000건)
res = calculate_vision_metrics(tp=480, tn=9450, fp=70, fn=0)
print(f"Accuracy: {res['Accuracy (%)']:.2f}%")
print(f"FPR (Over-kill): {res['FPR (%)']:.2f}%")
print(f"FNR (Under-kill): {res['FNR (%)']:.4f}%")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Golden Sample Test**: 판정 성능 유지를 위해 매 교대 가동 전 마스터 시료(Golden Sample)를 투입하여 정상 판정 여부를 확인하는가?
- [ ] **Data Re-training**: 현장에서 발생하는 오판 샘플들을 자동으로 수집하여 AI 모델 재학습(Fine-tuning) 데이터셋으로 활용하는가?
- [ ] **Multi-Thresholding**: 결함의 치명도(Criticality)에 따라 서로 다른 판정 임계치를 적용하여 관리 효율을 높이고 있는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
