---
metadata:
  id: "[[[MOC] 03_01_Vision_AI]]"
  domain: "AI_Vision"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.5.3"
object:
  object_type: "MOC"
  tier: 0
  description: "컴퓨터 비전 및 시각 지능 알고리즘 핵심 노드 거점 (Vision AI MOC)"
semantic:
  tags: ["#AI", "#Vision", "#CNN", "#ObjectDetection", "#Segmentation", "#Industrial_Vision", "#MOC"]
lineage:
  dataset_reference: "Antigravity Knowledge Vault"
  original_author: "Antigravity Vault"
spo_graph:
  - subject: "Vision AI"
    predicate: "processes"
    object: "Visual Data"
fidelity_engine:
  engine_id: "GraphFidelityEngine_V7.5.3"
  status: "Active"
dynamic:
  status: "Ratified"
  decay_rate: 0.0
Trust Metrics:
  T_static: 1.0
---

# 03_01_Vision_AI

## 1. 개요
본 MOC는 이미지 및 비디오 데이터를 분석하여 객체 인식, 결함 검출, 세그멘테이션을 수행하는 비전 지능(Vision AI)의 핵심 노드들을 연결합니다.

## 2. 핵심 지식 맵 (Knowledge Map)

### 2.1 기초 알고리즘 및 신경망
- [[AI] machine-vision-and-deep-learning-defect-detection-physics] (V7.5.3)
- [[AI] convolutional-neural-networks-cnn-mechanics]
- [[AI] visual-language-alignment]

### 2.2 산업용 비전 및 품질 검사
- [[Battery] battery-qc-and-metrology-standards] (V7.5.3)
- [[AI] machine-vision-for-semiconductor-wafer-inspection]

### 2.3 실측 데이터 및 벤치마크
- [[Data] ai-vision-object-detection-mAP-vs-latency-benchmark-log-v2026]
- [[Data] industrial-defect-detection-image-dataset-v2026]

## 3. 실무 가이드라인 (SOP)
1. **Defect Detection**: 2026년 실측 mAP 및 재현율(Recall) 기준 품질 합격 판정 로직.
2. **Edge Vision**: 온디바이스 비전 모델의 양자화(Quantization) 및 추론 지연 시간 최적화.
3. **Data Augmentation**: 산업용 소량 데이터를 위한 확산 모델 기반 합성 데이터 생성 기법.

---
**[V7.5.3_MODERNIZED]**
