---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: e6cc2791be147469dd7b3125666088173c201164b75372b2b9c3ac1a4fdee1be
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] machine-vision-and-deep-learning-defect-detection-physics]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] machine-vision-and-deep-learning-defect-detection-physics에 관한
    고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  frame_rate_operational_range: 30-120 fps
  max_inference_time_ms: 15
  min_confidence_threshold: 0.7
  min_detection_precision: 0.98
  min_iou_threshold: 0.5
  min_optical_sharpness_threshold: 100
  min_recall: 0.99
  resolution_operational_range: 12-50 MP
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

# [AI] machine-vision-and-deep-learning-defect-detection-physics

## 1. 개요 (System Overview)
수동 검사는 인적 요인(Fatigue, Subjectivity)에 의한 검출 변동성이 임계치를 초과함. 머신 비전 시스템은 고성능 광학계와 딥러닝 기반 특징 추출(Feature Extraction)을 결합하여 마이크로미터($\mu m$) 단위의 결함을 실시간 전수 검사함. 본 노드는 제조 공정 무결성(Process Integrity) 확보를 위한 시각적 지능의 결정론적 설계 표준을 정의함.

## 2. 기술 사양 및 검증 (Technical Specifications & Verification)

| Parameter | Symbol | Theoretical (Limit) | Verified (Operational) | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Resolution | $Res$ | $\infty$ (Diffraction Limit) | 12 ~ 50 [Ref: Original Spec] | ±2 | Megapixels |
| Frame Rate | $FPS$ | Sensor Max Frequency | 30 ~ 120 [Ref: Original Spec] | ±5 | frames/sec |
| Detection Precision | $Pre$ | 1.0 | > 0.98 [Ref: Original Spec] | ±0.01 | ratio |
| Recall (Sensitivity) | $Rec$ | 1.0 | > 0.99 [Ref: Original Spec] | ±0.005 | ratio |
| Inference Time | $t_{inf}$ | Hardware Min Latency | < 15 [Ref: Original Spec] | ±2 | ms |

## 3. VisionFidelityEngine: Diagnostic Logic

`VisionFidelityEngine`은 탐지 정확도 및 광학 데이터의 무결성을 정량적으로 진단함.

```python
class VisionFidelityEngine:
    """
    VisionFidelityEngine: 검사 시스템의 탐지 무결성 및 광학 상태 진단 로직
    """
    def __init__(self, confidence_scores, iou_scores, optical_sharpness):
        self.conf = confidence_scores # List of model confidence scores
        self.iou = iou_scores # Intersection over Union metrics
        self.sharp = optical_sharpness # Image Laplacian variance (Sharpness proxy)

    def diagnose_detection_quality(self):
        """모델 확신도 및 IoU 기반 탐지 무결성 진단"""
        avg_conf = np.mean(self.conf)
        avg_iou = np.mean(self.iou)
        
        if avg_conf < 0.7 or avg_iou < 0.5:
            return "CRITICAL: Ambiguous Detection (Possible False Negative)"
        return f"OPTIMAL: High-Precision Detection (Conf: {avg_conf:.2f}, IoU: {avg_iou:.2f})"

    def audit_optical_health(self):
        """이미지 선명도 기반 카메라/조명 노후화 진단"""
        # 선명도(Sharpness)가 초기 기준 대비 30% 하락 시 Rejection 수행
        if self.sharp < 100:
            return "REJECT: Blurry Image Detected (Lens Cleaning Required)"
        return "PASS: Optical System Integrity Confirmed"

# Instance Diagnostic Execution
engine = VisionFidelityEngine(confidence_scores=[0.95, 0.88, 0.92], 
                              iou_scores=[0.82, 0.75, 0.80], 
                              optical_sharpness=150)
print(engine.diagnose_detection_quality())
```

## 4. 시각 검사 계층 구조 (Visual Inspection Hierarchy)

1. **[Supervised Classification]**: 사전 정의된 불량 카테고리(Scratch, Particle, Crack 등)를 기반으로 결함 유형을 정밀 분류함.
2. **[Unsupervised Anomaly Detection]**: 정상 데이터 분포(Normal Distribution) 학습을 통해 Out-of-Distribution(OOD) 미인지 결함을 포착함.
3. **[Optical Geometry Design]**: 투명체 및 금속 표면의 결함 대비(Contrast) 극대화를 위한 Back-light 및 Dark-field 조명 기하학을 적용함.

## 5. 시스템 자가 감사 (Self-Audit Protocol)

1. **Receptive Field Mismatch**: CNN의 수용장(Receptive Field)이 타겟 결함 크기($\lambda_{defect}$)보다 작을 경우 발생하는 특징 소실(Feature Loss) 위험도를 검토할 것.
2. **Precision-Recall Trade-off**: 미검(False Negative)에 따른 공정 비용이 과검(False Positive) 비용을 상회할 경우, Recall을 100%에 근접하도록 임계치(Threshold)를 재설정할 것.
3. **Domain Shift Analysis**: 조명 조건 및 카메라 각도 변화에 따른 입력 데이터 분포 변화가 추론 정확도에 미치는 물리적 경로를 추적할 것.

## 6. 결론 (Deterministic Outcome)
본 노드는 `Data machine-vision-accuracy-and-false-alarm-log-v2026`와 실시간 동기화되어, 공정 라인 속도($V_{line}$) 내에서 결정론적 추론을 수행하며 미검률 0% 달성을 목표로 운용됨.

### 🔗 Retrieved Nodes
- 13_ai-infrastructure-and-computational-intelligence-hub
- convolutional-neural-networks-cnn-mechanics
- Data machine-vision-accuracy-and-false-alarm-log-v2026