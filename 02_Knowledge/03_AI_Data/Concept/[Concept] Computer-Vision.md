---
lineage:
  dataset_reference: Computer-Vision
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] Computer-Vision]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for Computer-Vision
  object_type: Concept
  tier: 1
properties:
  augmentation_reliability: 85%
  conf_threshold: '0.85'
  detection_accuracy_theoretical_map: '> 98.5%'
  detection_accuracy_verified_map: 92.4%
  inference_latency_theoretical_ms: < 10
  inference_latency_verified_ms: 15-25
  plc_reject_arm_pin: '5'
  segmentation_precision_theoretical_px: '0.1'
  segmentation_precision_verified_px: 0.5-1.2
semantic:
  alternative_parents: []
  is_instance_of: '[[ [MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: semantic_classification
  object: Concept
  predicate: auto_mapped
  subject: Computer-Vision
  weight: 1.0
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Computer Vision

## 1. Functional Definition (Purpose)
Computer Vision (CV)은 산업 자동화 공정의 시각적 피드백 루프를 완성하는 핵심 센서리 레이어(Sensory Layer)이다. 반도체 웨이퍼의 나노급 결함 [데이터 부재], 배터리 전극의 미세 Burr [데이터 부재], 자율 주행 로봇의 장애물 인지 등 고정밀 검사 및 제어를 목적으로 한다. 인간의 시각적 인지 편차를 제거하고, 24/7 일관된 정밀도(Consistency)를 통해 제조 수율(Yield)을 극대화한다.

## 2. Technical Specification Comparison

| Metric | Component | Theoretical (Model) | Verified (Industrial) | Ref |
|:---|:---|:---:|:---:|:---|
| **Inference Latency** | YOLO (v10+) | < 10ms [데이터 부재] | 15-25ms [데이터 부재] | [데이터 부재] |
| **Detection Accuracy** | mAP (50:95) | > 98.5% [데이터 부재] | 92.4% [데이터 부재] | [데이터 부재] |
| **Segmentation Precision**| Mask R-CNN | 0.1px [데이터 부재] | 0.5-1.2px [데이터 부재] | [데이터 부재] |
| **Data Augmentation** | Diffusion-based | 100% Variance [데이터 부재] | 85% Reliability [데이터 부재] | [데이터 부재] |

## 3. Engineering Rationale

### 3.1 CNN vs ViT: Spatial-Semantic Paradigm
- **CNN (Convolutional Neural Network)**: 커널(Kernel) 기반 슬라이딩 윈도우 연산을 통해 지역적 특징(Edge, Texture)을 추출한다. 연산 복잡도가 낮아 저전력/엣지 디바이스 환경의 불량 검사에 최적화되어 있다. [데이터 부재]
- **ViT (Vision Transformer)**: 이미지를 패치(Patch) 단위로 분할하여 Multi-Head Self-Attention을 적용한다. 이미지 전체의 전역적 상관관계(Global Context)를 모델링하며, 대규모 데이터셋 환경에서 CNN의 성능 한계를 상회한다. [데이터 부재]

### 3.2 YOLO (You Only Look Once) 실시간성 논리
Single-stage Detector로서, 이미지를 격자(Grid)로 분할하고 각 격자에서 Bounding Box 좌표와 Class 확률을 단일 신경망을 통해 동시 회귀(Regression)한다. 이 구조는 연산 파이프라인을 단순화하여 초당 수백 프레임(FPS) 이상의 실시간 처리를 보장한다. [데이터 부재]

### 3.3 Anomaly Detection (비지도 학습 기반 이상 탐지)
정상(Normal) 데이터의 분포(Distribution)만을 학습하여, 통계적 임계값을 벗어나는 데이터(Outlier)를 결함으로 판정한다. 이는 결함 데이터 확보가 어려운 신규 공정(New Process)의 불량 검출에 필수적인 논리이다. [데이터 부재]

## 4. Implementation Logic (Inference & IO Control)

산업용 카메라(Basler, Cognex 등) 인터페이스를 통한 실시간 불량 판정 및 PLC(Programmable Logic Controller) 연동 제어 로직이다.

```python
def execute_inspection_cycle(camera_stream, vision_model, plc_bridge):
    """
    Standard Inspection & Reject Control Logic [V7.5.2]
    """
    frame = camera_stream.capture()
    
    # 1. Inference: High-confidence thresholding [데이터 부재]
    detections = vision_model.predict(frame, conf_threshold=0.85)
    
    for det in detections:
        # 2. Defect Classification & Hardware Trigger
        if det.class_name == "Scratched_Defect":
            # PLC Relay Signal: Pin 5 (Reject Arm) -> ON
            plc_bridge.send_signal(relay_pin=5, action="ON")
            log_event(type="REJECT", data={"bbox": det.bbox, "conf": det.confidence})
            return "REJECT_ACTION_EXECUTED"
            
    return "PASS_CONTINUE"
```

## 5. Self-Audit Checklist
1. **Convolutional Mathematics**: 커널 연산이 이미지의 공간적 국소성(Spatial Locality)을 어떻게 보존하는가?
2. **Transformer Scalability**: ViT의 Attention Map이 고해상도 이미지에서 가지는 연산 복잡도(Complexity) 문제는 무엇인가?
3. **Metric Trade-off**: mAP 산출 시 Precision(정밀도)과 Recall(재현율)의 가중치 설정이 공정 수율에 미치는 영향은?