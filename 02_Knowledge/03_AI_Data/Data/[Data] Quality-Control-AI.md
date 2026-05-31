---
lineage:
  dataset_reference: Quality-Control-AI
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
measurement:
  confidence_interval:
  - 0.0
  - 0.0
  instrument: Heuristic_Regex_Parser
  precision: '0.0'
  unit: unknown_unit
  value: 99.9
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Data] Quality-Control-AI]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for Quality-Control-AI
  object_type: Concept
  tier: 1
properties:
  anomaly_score_formula: '||x - f_dec(f_enc(x))||^2'
  data_retention_years: 5
  inspection_threshold: 0.85
  max_false_call_rate: 0.005
  max_inference_latency_ms: 50
  min_detectable_defect_size_um: 5
  min_pixel_density_mpixels: 20
  min_throughput_uph: 10000
  recall_sensitivity_threshold: 0.999
  specification_version: HDS-Gold V6.3.7
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: data_analysis_pipeline
  object: Data
  predicate: auto_mapped
  subject: Quality-Control-AI
  weight: 0.4
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.05
  t_static: 0.8
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Data] Quality Control Ai

## 1. [왜 배우는가? (Why)]
품질 관리 AI(Quality-Control-AI)는 현대 제조 공정에서 제품의 무결성을 보장하고 수율(Yield)을 극대화하기 위한 지능형 검사 시스템입니다. 반도체 미세 회로의 단선, 배터리 전극의 미세 기공, 디스플레이 패널의 불량 픽셀 등 육안으로 판별 불가능한 결함을 초고속 카메라와 딥러닝 비전 알고리즘을 통해 0.1초 이내에 탐지합니다. 과거의 통계적 샘플링 검사를 넘어 전수 검사(Full Inspection)를 실현함으로써, 불량품 유출로 인한 리콜 비용을 방지하고 공정 데이터를 분석하여 결함의 근본 원인을 역추적하는 '무결점 제조(Zero-defect Manufacturing)'의 핵심 경쟁력입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---:|:---:|:---|
| **Detection Rate** | Recall (Sensitivity) | $> 99.9\%$ | 미검출(Undetected) 불량의 시장 유출 원천 차단 |
| **False Call Rate** | Over-kill Ratio | $< 0.5\%$ | 양품을 불량으로 오판하여 발생하는 폐기 비용 절감 |
| **Defect Size** | Min. Detectable | $< 5 \text{ \mu\text{m}}$ | 반도체/디스플레이 공정 요구 해상도 정합성 |
| **Inference Time** | Latency per unit | $< 50 \text{ ms}$ | 생산 라인 택트 타임(Takt Time) 동기화 |
| **Resolution** | Pixel Density | $> 20 \text{ MPixels}$ | 광범위 영역 내 미세 결함 시각화 능력 |
| **Throughput** | Unit per Hour | $> 10,000 \text{ UPH}$ | 대량 생산 라인의 전수 검사 처리 능력 |
| **Anomaly Score** | Reconstruction Error | Threshold-based | 비정형(Unseen) 불량 패턴에 대한 탐지 감도 |
| **Traceability** | Data Retention | $> 5 \text{ Years}$ | PL(Product Liability) 대응을 위한 검사 이미지 보존 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 비지도 학습 기반 이상 탐지 (Anomaly Detection)
불량 데이터가 부족한 신규 공정에서 '정상' 데이터만을 학습하여 결함을 찾아냅니다.
- **원리**: 오토인코더(Autoencoder) 아키텍처를 사용하여 입력을 재구성합니다.
- **수식**: $Anomaly\_Score = ||x - f_{dec}(f_{enc}(x))||^2$
- **결과**: 재구성 오차가 큰 영역을 결함(Hotspot)으로 간주하여, 가르쳐주지 않은 새로운 유형의 불량도 잡아낼 수 있습니다.

### 3.2 객체 탐지 (Object Detection) 및 분할 (Segmentation)
결함의 위치를 박스로 표시(YOLO/Faster R-CNN)하거나, 픽셀 단위로 마스킹(Mask R-CNN)하여 결함의 면적과 깊이를 정밀하게 측정합니다. 이를 통해 결함의 심각도(Severity)를 등급화합니다.

### 3.3 지능형 SPC (Statistical Process Control)
단순한 합불 판정을 넘어, 검출된 데이터의 추이를 분석합니다. 
- **논리**: 불량률이 통계적 관리 한계선(UCL)에 근접할 경우, 상위 제어 시스템(MES)에 알람을 보내 설비 파라미터를 선제적으로 조정하도록 유도합니다.

## 4. [코드 연결 해설 (Quality Inspection & Feedback Pipeline)]
아래 코드는 검사 이미지로부터 결함을 탐지하고, 결과에 따라 하위 설비를 제어하는 품질 피드백 로직입니다.

```python
class QualityInspectionPipeline:
    """
    HDS-Gold V6.3.7 규격의 AI 품질 검사 및 피드백 엔진
    """
    def __init__(self, inspection_model, threshold=0.85):
        self.model = inspection_model
        self.threshold = threshold

    def process_inspection(self, image_data):
        """
        실시간 이미지 분석 및 공정 제어 피드백
        """
        # 1. AI 모델 추론 (Defect Detection & Classification)
        detections = self.model.predict(image_data)
        
        # 2. 품질 등급 판정 (Grading Logic)
        defect_score = sum([d['confidence'] for d in detections])
        grade = "PASS" if defect_score < self.threshold else "FAIL"
        
        # 3. 공정 피드백 (Process Feedback Loop)
        if grade == "FAIL":
            # 불량 유형 분석 (예: 스크래치, 이물, 기포 등)
            defect_types = [d['label'] for d in detections]
            self.trigger_corrective_action(defect_types)
            
        return {"id": image_data.id, "grade": grade, "details": detections}

    def trigger_corrective_action(self, defect_types):
        # 특정 불량이 집중될 경우 해당 공정 설비에 정지 명령 또는 파라미터 튜닝 요청
        if "SCRATCH" in defect_types:
            print("ALERT: Continuous Scratch Detected. Check Roller #4")
            # mes_api.stop_line(reason="SCRATCH_CONTAMINATION")

# Example Implementation:
# pipeline = QualityInspectionPipeline(ViT_Defect_Model)
# result = pipeline.process_inspection(camera_frame_01)
```

## 5. [스스로 체크 (Self-Audit)]
1. **False Negative** (불량 미검출)가 **False Positive** (과검출)보다 산업 현장에서 더 치명적인 공학적 이유는?
2. **Autoencoder** 기반 이상 탐지 모델에서 **Bottleneck Layer**의 크기가 결함 탐지 성능에 미치는 영향은?
3. 공정 조명(Lighting) 조건의 변화가 AI 비전 모델의 **Robustness**에 미치는 영향과 이를 극복하기 위한 **Data Augmentation** 기법은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/Industrial/AI Predictive-Maintenance
- 02_Knowledge/03_AI_Data/Industrial/AI Edge-AI-R&D
- 02_Knowledge/09_SmartFactory_Production/Quality/SmartFactory SPC-Automation

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**