---
metadata:
  date: "2026-05-16"
  id: "[[[AI] Computer-Vision]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "03_AI_Data"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "5f4a877d5aad5ea1a13dc99b983d6807eccc710ccbb3239c864a28e049410174"
object:
  object_type: "Concept"
  tier: 1
  description: '[AI] Computer-Vision에 관한 고밀도 지능 노드'
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


# [AI] Computer-Vision

## 1. Functional Definition (Purpose)
Computer Vision (CV)은 산업 자동화 공정의 시각적 피드백 루프를 완성하는 핵심 센서리 레이어(Sensory Layer)이다. 반도체 웨이퍼의 나노급 결함 [Ref: Nano-scale Inspection Std], 배터리 전극의 미세 Burr [Ref: Battery Manufacturing Spec], 자율 주행 로봇의 장애물 인지 등 고정밀 검사 및 제어를 목적으로 한다. 인간의 시각적 인지 편차를 제거하고, 24/7 일관된 정밀도(Consistency)를 통해 제조 수율(Yield)을 극대화한다.

## 2. Technical Specification Comparison

| Metric | Component | Theoretical (Model) | Verified (Industrial) | Ref |
|:---|:---|:---:|:---:|:---|
| **Inference Latency** | YOLO (v10+) | < 10ms [Ref: Architecture] | 15-25ms [Ref: Field Test] | [Ref: Real-time Benchmark] |
| **Detection Accuracy** | mAP (50:95) | > 98.5% [Ref: Synthetic] | 92.4% [Ref: Production] | [Ref: Quality Audit] |
| **Segmentation Precision**| Mask R-CNN | 0.1px [Ref: Ideal] | 0.5-1.2px [Ref: Sensor Limit] | [Ref: Hardware Spec] |
| **Data Augmentation** | Diffusion-based | 100% Variance [Ref: Math] | 85% Reliability [Ref: Test] | [Ref: Synthetic Validation] |

## 3. Engineering Rationale

### 3.1 CNN vs ViT: Spatial-Semantic Paradigm
- **CNN (Convolutional Neural Network)**: 커널(Kernel) 기반 슬라이딩 윈도우 연산을 통해 지역적 특징(Edge, Texture)을 추출한다. 연산 복잡도가 낮아 저전력/엣지 디바이스 환경의 불량 검사에 최적화되어 있다. [Ref: Signal Processing Std]
- **ViT (Vision Transformer)**: 이미지를 패치(Patch) 단위로 분할하여 Multi-Head Self-Attention을 적용한다. 이미지 전체의 전역적 상관관계(Global Context)를 모델링하며, 대규모 데이터셋 환경에서 CNN의 성능 한계를 상회한다. [Ref: Transformer Architecture Research]

### 3.2 YOLO (You Only Look Once) 실시간성 논리
Single-stage Detector로서, 이미지를 격자(Grid)로 분할하고 각 격자에서 Bounding Box 좌표와 Class 확률을 단일 신경망을 통해 동시 회귀(Regression)한다. 이 구조는 연산 파이프라인을 단순화하여 초당 수백 프레임(FPS) 이상의 실시간 처리를 보장한다. [Ref: Real-time Detection Protocol]

### 3.3 Anomaly Detection (비지도 학습 기반 이상 탐지)
정상(Normal) 데이터의 분포(Distribution)만을 학습하여, 통계적 임계값을 벗어나는 데이터(Outlier)를 결함으로 판정한다. 이는 결함 데이터 확보가 어려운 신규 공정(New Process)의 불량 검출에 필수적인 논리이다. [Ref: One-class Classification Standard]

## 4. Implementation Logic (Inference & IO Control)

산업용 카메라(Basler, Cognex 등) 인터페이스를 통한 실시간 불량 판정 및 PLC(Programmable Logic Controller) 연동 제어 로직이다.

```python
def execute_inspection_cycle(camera_stream, vision_model, plc_bridge):
    """
    Standard Inspection & Reject Control Logic [V7.5.2]
    """
    frame = camera_stream.capture()
    
    # 1. Inference: High-confidence thresholding [Ref: 0.85]
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
