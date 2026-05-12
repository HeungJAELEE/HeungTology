---
Basic:
  id: "[AI] Computer-Vision"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
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

# [AI] Computer-Vision

## 1. [왜 배우는가? (Why)]
컴퓨터 비전은 기계에 '눈'을 달아주는 기술입니다. 반도체 웨이퍼의 나노급 결함, 배터리 전극의 미세한 버(Burr), 로봇의 자율 주행을 위한 장애물 인식 등 현대 산업의 자동화 검사와 제어는 모두 컴퓨터 비전에 의존합니다. 인간의 시각은 피로도에 따라 정확도가 떨어지지만, AI 기반 시각 지능은 24시간 내내 일관된 정밀도로 사물을 식별하고 분류하여 제조 수율과 안전을 보장합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Architecture / Logic | Engineering Rationale |
|:---|:---:|:---|
| **Backbone** | CNN / ViT (Vision Transformer) | 공간 특징 추출 및 글로벌 문맥 이해 |
| **Object Detection** | YOLO (v10+) / RT-DETR | 실시간 객체 위치 탐지 및 분류 |
| **Segmentation** | Mask R-CNN / SAM | 객체 단위의 픽셀 수준 정밀 분할 |
| **Augmentation** | Diffusion-based Synthetic Data | 데이터 부족 문제를 가상 이미지로 해결 |
| **Evaluation** | mAP (mean Average Precision) | 탐지 정확도 및 신뢰도 정량 평가 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 CNN vs ViT: 시각 처리의 패러다임 변화
- **CNN (Convolutional Neural Network)**: 필터(Kernel)를 슬라이딩하며 지역적인 특징(Edge, Texture)을 추출합니다. 연산 효율이 좋고 데이터가 적어도 잘 작동하여 전통적인 불량 검사에 강점이 있습니다.
- **ViT (Vision Transformer)**: 이미지를 패치(Patch) 단위로 쪼개어 언어 모델처럼 어텐션을 적용합니다. 이미지 전체의 전역적 관계(Global Context)를 이해하는 데 탁월하며, 데이터가 많을수록 CNN의 성능을 압도합니다.

### 3.2 YOLO (You Only Look Once)의 실시간성 논리
이미지를 한 번만 보고 객체의 위치(Bounding Box)와 종류(Class)를 동시에 예측합니다.
- **로직**: 이미지를 격자(Grid)로 나누고 각 격자에서 직접 확률을 계산함으로써, 연산 속도를 획기적으로 높여 초당 수백 프레임의 실시간 처리가 가능합니다.

### 3.3 아노말리 디텍션 (Anomaly Detection)
정상 이미지만 학습하여, 이와 다른 '이상 현상'을 찾아내는 방식입니다. 학습 데이터가 부족한 신공정의 불량 검출에 필수적인 논리입니다.

## 4. [코드 연결 해설 (Inference & IO Control)]
산업용 카메라(Basler 등)와 연동하여 실시간으로 불량을 판정하고 배출 장치를 제어하는 논리입니다.
```python
# 실시간 불량 검출 및 릴레이(Relay) 제어 로직
def process_inspection_frame(camera_stream):
    frame = camera_stream.capture()
    
    # 1. 모델 추론 (YOLO / ViT 기반)
    results = vision_model.predict(frame, conf_threshold=0.85)
    
    for detection in results:
        # 2. 불량(Defect) 클래스 감지 시 즉시 배출(Reject) 신호 발생
        if detection.class_name == "Scratched_Defect":
            # 하드웨어 PLC와 통신하여 불량품 배출 암(Arm) 구동
            plc_bridge.send_signal(relay_pin=5, action="ON")
            log_defect_info(detection.bbox, detection.confidence)
            return "REJECT"
            
    return "PASS"
```

## 5. [스스로 체크 (Self-Audit)]
1. 컴퓨터 비전에서 '컨벌루션(Convolution)' 연산이 이미지의 지역적 특징을 효과적으로 잡아내는 수학적 원리는?
2. ViT(Vision Transformer)가 CNN 대비 고해상도 이미지 처리에서 가지는 장점과 단점은?
3. 객체 탐지 성능 지표인 mAP(mean Average Precision)에서 'Precision'과 'Recall'의 트레이드오프 관계는?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
