---
metadata:
  date: "2026-05-14"
  id: "[moc]-03_01_vision_ai-v7.5.2"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "03_AI_Data"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "https://doi.org/cv.standards.v6.3.7"
  original_author: "Computer_Vision_Standards"
  original_hash: "fcfee50d85cd89739d617d808cc5b7d24f97e5897f40d7accc09dac214c3bfad"
object:
  object_type: "Concept"
  tier: 0
  description: 'Hardcore Fidelity Industrial Vision AI Node'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] Global-Dataset-Inventory-Hub]]"
  alternative_parents: []
spo_graph:
  - subject: "Vision_AI"
    predicate: "functions_as"
    object: "Digital_Sensory_Interface"
    evidence_coordinate: "Essential for micro-defect detection and AMR spatial perception"
    evidence_hash: "fcfee50d85cd"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
  - subject: "CNN"
    predicate: "performs"
    object: "Hierarchical_Feature_Extraction"
    evidence_coordinate: "Spatial feature mapping via kernel-based layer hierarchy"
    evidence_hash: "fcfee50d85cd"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
  - subject: "ResNet-50"
    predicate: "yielded"
    object: "Zero_FNR"
    evidence_coordinate: "Battery cell scratch classification case study"
    evidence_hash: "fcfee50d85cd"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---

# [[[MOC] 03_01_Vision_AI

## 1. [Functional Definition] Vision AI의 산업적 메커니즘
Vision AI는 고정밀 제조 환경에서 광학적 데이터를 디지털 정보로 변환하는 핵심 센서리 인터페이스(Sensory Interface)다. 육안 검사가 불가능한 미세 결함(Micro-defect)의 고속 검출 및 자율 이동 로봇(AMR)의 공간 인지(Spatial Awareness)를 수행한다. 특히 반도체 및 이차전지 공정에서 딥러닝 기반 이미지 분석은 숙련공의 판단 로직을 정량적 데이터로 치환하여 품질 표준의 상향 평준화를 실현한다.

---

## 2. [Numerical Specs] 성능 지표 및 검증 데이터

### 2.1 핵심 성능 지표 (KPI)
| 항목 | 핵심 지표 (KPI) | 목표 수준 (Target) | 비고 |
| :--- | :--- | :--- | :--- |
| **mAP** | 객체 검출 정확도 | $> 92.0\%$ [Ref: Computer_Vision_Standards] | 복합 결함 검출 기준 |
| **Inference Time** | 이미지 당 추론 속도 | $< 30\,\text{ms}$ [Ref: Computer_Vision_Standards] | 실시간 라인 검사 대응 |
| **IoU** | 세그멘테이션 정밀도 | $> 0.85$ [Ref: Computer_Vision_Standards] | 결함 영역 특정 정확도 |
| **FPR** | 과검율 (False Positive) | $< 1.0\%$ [Ref: Computer_Vision_Standards] | 생산성 저하 방지 지표 |
| **FNR** | 미검율 (False Negative) | $< 0.01\%$ [Ref: Computer_Vision_Standards] | 품질 유출 방지 (Critical) |

### 2.2 이론치 vs 검증치 대조 (Theoretical vs. Verified)
| Metric | Theoretical (Ideal) | Verified (Case Study) | Status |
| :--- | :--- | :--- | :--- |
| **FPR** | $0.0\%$ | $< 2.0\%$ [Ref: Python_FidelityEngine_Report] | Optimized |
| **FNR** | $0.0\%$ | $0.0\%$ [Ref: Python_FidelityEngine_Report] | Achieved |
| **Throughput** | N/A | $+500\%$ [Ref: Python_FidelityEngine_Report] | Improved |

---

## 3. [Scientific Rationale] 신경망 아키텍처 및 최적화

### 3.1 Convolutional Neural Networks (CNN)
커널(Kernel) 연산을 통해 이미지의 공간적 특징(Spatial Features)을 계층적으로 추출한다.
* **Lower Layers**: 선(Edge), 면(Surface), 색상(Color) 등 저수준 기하학적 특징 추출.
* **Higher Layers**: 결함 패턴(Defect Pattern), 형상(Morphology) 등 고수준 의미 정보 추출.

### 3.2 Loss Function (손실 함수)
모델의 예측값($y_{pred}$)과 Ground Truth($y_{true}$) 간의 오차를 최소화한다.
$$Loss = \sum (y_{true} - y_{pred})^2 + \lambda \Omega(w)$$
* **$\lambda \Omega(w)$**: 과적합(Overfitting) 억제를 위한 규제항(Regularization).

---

## 4. [Case Study] 이차전지 셀 표면 스크래치 분류

### 4.1 공정 자동화 분석 결과
* **Problem**: 작업자 숙련도 편차로 인해 과검율(FPR) $15\%$ 발생 [Ref: Python_FidelityEngine_Report].
* **Methodology**: $50,000$장의 양/불 데이터셋을 활용, ResNet-50 기반 모델 학습 및 RTX 4060 기반 엣지 컴퓨팅 환경 구축 [Ref: Python_FidelityEngine_Report].
* **Results**: 
    - 과검율(FPR): $2\%$ 이내로 저감 [Ref: Python_FidelityEngine_Report].
    - 미검율(FNR): $0\%$ 달성 [Ref: Python_FidelityEngine_Report].
    - 검사 속도: 기존 대비 $500\%$ 향상 [Ref: Python_FidelityEngine_Report].
    - 경제적 효과: 연간 인건비 $5$억 원 절감 [Ref: Python_FidelityEngine_Report].

---

## 5. [FidelityEngine] IoU Calculation Module

```python
def calculate_iou(box_a, box_b):
    """
    Calculate IoU of two bounding boxes
    :param box_a: (x1, y1, x2, y2)
    :param box_b: (x1, y1, x2, y2)
    :return: IoU value
    """
    xA = max(box_a[0], box_b[0])
    yA = max(box_a[1], box_b[1])
    xB = min(box_a[2], box_b[2])
    yB = min(box_a[3], box_b[3])
    
    inter_area = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    
    box_a_area = (box_a[2] - box_a[0] + 1) * (box_a[3] - box_a[1] + 1)
    box_b_area = (box_b[2] - box_b[0] + 1) * (box_b[3] - box_b[1] + 1)
    
    iou = inter_area / float(box_a_area + box_b_area - inter_area)
    return iou

# Execution
target = [50, 50, 150, 150]
prediction = [60, 60, 160, 160]
iou_val = calculate_iou(target, prediction)
print(f"Calculated IoU: {iou_val:.4f}")
```

---

## 6. [Verification] Engineering Checklist
- [ ] **Lighting Consistency**: 조명 환경(Luminance, Angle) 변화에 대한 모델 강인성(Robustness) 검증 여부.
- [ ] **Dataset Balance**: 불량 샘my(Minority Class) 편향 해소를 위한 Data Augmentation 또는 GAN 적용 여부.
- [ ] **Explainability (XAI)**: 결함 판정 근거 시각화(Grad-CAM 등)를 통한 엔지니어 신뢰성 확보 여부.

**[V7.5.2_HARDCORE_FIDELITY_UPGRADE_COMPLETE]**