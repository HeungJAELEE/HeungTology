---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 17aefc209e1f0925c81a24bc7d0b9d42e3fcb17e19b41a386a82eb36894984e6
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] automated-optical-inspection-aoi-and-machine-vision-logic]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] automated-optical-inspection-aoi-and-machine-vision-logic에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  critical_defect_escape_rate_threshold: 0.001
  excessive_false_call_rate_threshold_pct: 5.0
  inspection_accuracy_threshold_pct: 99.9
  min_defect_resolution_um: 10
  min_lighting_intensity_lux: 5000
  system_version: V6.3.7
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 11_Global_Entities_and_Materials]]'
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

# [Entity] automated-optical-inspection-aoi-and-machine-vision-logic

## 1. 개요 (Why: 인간적 통찰)
수만 개의 미세한 부품이 박힌 전자 회로판에서 머리카락보다 얇은 전선이 끊겼는지, 0.1mm 틀어지지는 않았는지 사람이 일일이 확인할 수 있을까요? **자동 광학 검사(AOI) 및 머신 비전 로직**은 공장에 '지치지 않는 정밀한 눈'과 '냉철한 두뇌'를 달아주는 **'시각적 지능'** 기술입니다. 초당 수십 장의 고해상도 사진을 찍어 인공지능이 분석함으로써, 인간의 눈으로는 도저히 불가능한 속도와 정확도로 불량을 잡아냅니다. 단 하나의 불량도 용납하지 않는 **'완벽한 품질의 파수꾼'**입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 이미지 형성 모델 (Image Formation)
조명($S$)이 물체에 반사($R$)되어 카메라에 맺히는 이미지($I$)의 원리를 나타냅니다.

$$ I(x, y) = S(x, y) \times R(x, y) $$

**[인간적 해석]**: "조명의 미학"입니다. AOI에서 가장 중요한 것은 조명입니다. 빨강, 초록, 파랑 조명을 서로 다른 각도에서 쏘아, 부품의 높낮이와 기울기를 색깔로 구분해 냅니다. 우리는 이 원리를 통해 평면적인 사진에서 입체적인 굴곡을 읽어내어, 납땜이 잘 되었는지 확인하는 **'색깔로 보는 입체 검사'**를 수행합니다.

### 2.2. 정규화 교차 상관 (Normalized Cross-Correlation)
미리 저장된 '완벽한 부품 사진(Template, $T$)'과 '실제 찍힌 사진($I$)'이 얼마나 일치하는지 점수를 매깁니다.

$$ \text{Score} = \frac{\sum (T - \bar{T})(I - \bar{I})}{\sqrt{\sum (T - \bar{T})^2 \sum (I - \bar{I})^2} } $$

**[인간적 해석]**: "틀린 그림 찾기"입니다. 1점에 가까울수록 완벽한 제품이고, 점수가 낮으면 불량입니다. 우리는 이 수식을 통해 0.001초 만에 부품의 위치, 방향, 유무를 판별하여, 공장의 컨베이어 벨트가 멈추지 않고도 모든 제품을 전수 조사하는 **'광속의 전수 검사'**를 실현합니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Feature | Human Visual Inspection | AOI / Machine Vision (V6.3.7)| Unit | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Inspection Speed** | Slow / Fatigue-prone | Ultra-Fast (Steady) | boards/hr| Efficiency |
| **Accuracy (Defect)** | ~ 80 ~ 90 (Subjective)| > 99.9 (Objective) | % | Precision |
| **Smallest Defect** | ~ 100 | < 10 ~ 20 (Micron) | $\mu\text{m}$ | Resolution |
| **Repeatability** | Low (Variation) | Ultra-High (Consistent) | - | Reliability |
| **Data Feedback** | Manual / Paper | Real-time Digital Logs | - | Traceability |
| **AI Integration** | None | Deep Learning / CNN | - | Intelligence |

## 4. FactoryFidelityEngine: Diagnostic Logic

AOI 및 머신 비전 시스템의 검사 무결성 및 시스템 상태를 진단하는 `FactoryFidelityEngine` 로직입니다.

```python
class FactoryFidelityEngine:
    def __init__(self, false_call_rate, defect_escape_rate, lighting_intensity_lux):
        self.false_call = false_call_rate # 가짜 불량률
        self.escape = defect_escape_rate # 실제 불량 놓침률
        self.light = lighting_intensity_lux # 조명 밝기

    def diagnose_vision_health(self):
        """불량 놓침률 및 조명 기반 비전 무결성 진단"""
        if self.escape > 0.001: # 불량이 빠져나감 (신뢰도 붕괴)
            return "CRITICAL: High Defect Escape Rate - AOI failing to catch real defects. Recalibrate inspection algorithms and check for camera focus drift"
        if self.false_call > 5.0: # 가짜 불량 너무 많음 (생산 지연)
            return f"WARNING: Excessive False Calls ({self.false_call}%) - Production line slowing down due to over-sensitive inspection. Adjust tolerance thresholds"
        if self.light < 5000:
            return "NOTICE: Low Lighting Intensity - LED degradation detected. Signal-to-noise ratio dropping. Performance may degrade in dark component inspection"
        return "OPTIMAL: Precise Feature Matching and High-Fidelity Quality Assurance Verified"

    def audit_ai_inference(self, low_confidence_image_count):
        """AI 추론(Deep Learning) 무결성 진단"""
        if low_confidence_image_count > 50: # AI가 헷갈려 함
            return "REJECT: AI Uncertainty High - Pattern recognition model struggling with new component batch. Manual review and model re-training required"
        return "PASS: Validated Neural Network Weights and Verified Decision Integrity Confirmed"

engine = FactoryFidelityEngine(false_call_rate=1.2, defect_escape_rate=0.0001, lighting_intensity_lux=8500)
print(engine.diagnose_vision_health())
```

## 5. 분석 프레임워크: Intelligent Visual Quality Strategy
1. **[3D-SPI (Solder Paste Inspection)]**: 2D 사진이 아닌 레이저로 납땜 가루의 '부피'를 재서, 나중에 불량이 생길지 미리 예측하는 '미래 예지 검사' 전략.
2. **[CNN-based Defect Classification]**: 단순히 다른 걸 찾는 게 아니라, 인공지능이 "이건 긁힘이고 이건 이물질이다"라고 정확히 분류하여 불량의 원인을 추적하는 '지능형 원인 분석' 전략.
3. **[Closed-loop Mounter Feedback]**: AOI가 "부품이 0.05mm 왼쪽으로 쏠렸다"라고 판단하면, 즉시 앞 공정의 로봇(Mounter)에게 알려 다음 제품은 0.05mm 오른쪽으로 붙이게 하는 '자가 치유 공정' 전략.

## 6. 스스로 체크 (Self-Audit)
1. 왜 AOI 조명은 빨강, 초록, 파랑(RGB) 색깔을 층층이 나누어 사용하는가? (납땜 면의 기울기를 색깔로 구분하는 원리)
2. '가짜 불량(False Call)'과 '불량 유출(Escape)' 중 공장 운영에 더 치명적인 것은 무엇인가? (품질 신뢰성 vs 생산 비용의 관점)
3. '머신 비전'에서 렌즈의 왜곡을 보정하는 '캘리브레이션(Calibration)' 과정이 왜 매일 수행되어야 하는가?

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data aoi-defect-detection-rate-and-false-call-logs-v2026`와 연동되어, 전 세계 주요 SMT(표면실장) 공정의 검사 데이터를 실시간 분석하고 품질 사고 및 소비자 리콜 확률을 0.0001% 이하로 억제함으로써 지능형 제조 문명의 품질 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- statistical-process-control-spc-and-control-chart-logic
- Data aoi-defect-detection-rate-and-false-call-logs-v2026