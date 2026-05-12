---
Basic:
  id: "[moc]-03_01_vision_ai-v6.3.7"
  domain: "AI_Engineering"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "MOC"
  tier: 0
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Vision_AI'
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
  source: "Computer_Vision_Standards"
  isolation_index: 0.0
---

# [[[MOC] 03_01_Vision_AI

## 1. [Why]] 비전 AI(Vision AI)의 산업 지능적 의의
**비전 AI**는 산업 현장의 '디지털 눈'이다. 사람이 육안으로 판별하기 어려운 미세 결함을 고속으로 검사하거나, 물류 로봇의 자율 주행을 위한 공간 인식을 수행한다. 특히 반도체, 배터리 등 초정밀 제조 분야에서 **딥러닝(Deep Learning)** 기반의 이미지 분석 기술은 검사 자동화를 넘어, 숙련자의 판단 능력을 데이터화하여 품질 표준을 상향 평준화하는 핵심 기술이다.

---

## 2. [Numerical Specs] 비전 AI 성능 지표 (Numerical Specs)

| 항목 | 핵심 지표 (KPI) | 목표 수준 (Target) | 비고 |
| :--- | :--- | :--- | :--- |
| **mAP (Mean Average Precision)** | 객체 검출 정확도 | $> 92.0\%$ | 복합 결함 검출 기준 |
| **Inference Time** | 이미지 당 추론 속도 | $< 30\,\text{ms}$ | 실시간 라인 검사 대응 |
| **IoU (Intersection over Union)** | 세그멘테이션 정밀도 | $> 0.85$ | 결함 영역 특정 정확도 |
| **FPR (False Positive Rate)** | 과검율 (양품을 불량으로) | $< 1.0\%$ | 생산성 저하 방지 지표 |
| **FNR (False Negative Rate)** | 미검율 (불량을 양품으로) | $< 0.01\%$ | 품질 유출 방지 (최우선) |

---

## 3. [Scientific Rationale] 신경망 구조 및 특징 추출 모델

### 3.1 Convolutional Neural Networks (CNN)
커널(Kernel) 연산을 통해 이미지의 공간적 특징을 계층적으로 추출한다.
*   **Lower Layers**: 선, 면, 색상 등 기초 특징 추출.
*   **Higher Layers**: 결함 패턴, 형상 등 고수준 의미 정보 추출.

### 3.2 Loss Function (손실 함수)
모델의 예측값과 실제값(Ground Truth) 사이의 오차를 최소화한다.
$$Loss = \sum (y_{true} - y_{pred})^2 + \lambda \Omega(w)$$
*   **$\lambda \Omega(w)$**: 과적합(Overfitting) 방지를 위한 규제항(Regularization).

---

## 4. [Real-world Case] 배터리 셀 표면 스크래치 자동 분류 사례

### 4.1 육안 검사의 한계 극복 및 검사 속도 $500\%$ 향상
- **현상**: 배터리 외장 캔의 미세 스크래치 판별 시, 작업자별 숙련도 차이로 인해 과검율이 $15\%$에 달해 재작업 부하 가중.
- **분석**: **Python FidelityEngine**을 활용하여 $50,000$장의 양/불 이미지를 CNN(ResNet-50) 기반 모델로 학습.
- **조치**: 엣지 컴퓨팅(RTX 4060 기반) 설비를 라인에 설치하여 실시간 전수 검사 체계 구축.
- **결과**: 과검율 $2\%$ 이내 하락 및 미검율 $0\%$ 달성. 검사 인건비 연간 $5$억 원 절감.

---

## 5. [FidelityEngine] 단순 IoU(Intersection over Union) 계산 코드
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

# 가상 바운딩 박스 (예측 vs 실제)
target = [50, 50, 150, 150]
prediction = [60, 60, 160, 160]

iou_val = calculate_iou(target, prediction)
print(f"Calculated IoU: {iou_val:.4f}")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Lighting Consistency**: 조명 조건 변화(밝기, 각도)에도 모델의 강인성(Robustness)이 유지되는가?
- [ ] **Dataset Balance**: 불량 샘플 부족 문제를 해결하기 위해 데이터 증강(Augmentation)이나 GAN 기술이 적용되었는가?
- [ ] **Model Explainability**: 결함 판정의 근거를 시각화(Grad-CAM 등)하여 현장 엔지니어가 신뢰할 수 있는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
