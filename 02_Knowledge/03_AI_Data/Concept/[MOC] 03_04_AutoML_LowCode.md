---
lineage:
  dataset_reference: Antigravity Knowledge Vault
  original_author: Antigravity Vault
  original_hash: ddf5c7515152256651396371701e0bff351af6a857485768157391f5986f3edd
metadata:
  ai_status: pending_review
  date: '2026-05-16'
  domain: AI_Automation
  id: '[[[MOC] 03_04_AutoML_LowCode]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: AI 모델 자동 최적화(AutoML) 및 현업 사용자용 저코드(Low-Code) 개발 환경 핵심 노드 거점
  object_type: Concept
  tier: 0
properties:
  deployment_method: container_based
  performance_metrics: accuracy, f1_score
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: process_automation
  object: Model Selection
  predicate: automates
  subject: AutoML
  weight: 0.9
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

# 03_04_AutoML_LowCode

## 1. 개요
본 MOC는 전문 개발자 없이도 고성능 AI를 구축할 수 있게 하는 AutoML(Automated Machine Learning)과 저코드(Low-Code) 플랫폼의 핵심 기술을 연결합니다.

## 2. 핵심 지식 맵 (Knowledge Map)

### 2.1 하이퍼파라미터 및 아키텍처 탐색 (NAS)
- [[AI] machine-learning-foundations]
- [[Strategy] AI-Driven-Industrial-Process-Optimization]
- [[AI] training-iteration-logic]

### 2.2 현업용 AI 솔루션 및 배포
- [[MOC] MLOps_&_Data_Engineering]
- [[Concept] Knowledge-Distillation-for-Industrial-Edge-AI]

### 2.3 실측 데이터 및 자동화 로그
- [[Data] ai-hpc-cluster-gpu-utilization-and-training-efficiency-log-v2026]
- [[Data] ai-model-drift-and-real-time-re-training-log-v2026]

## 3. 실무 가이드라인 (SOP)
1. **Citizen Data Scientist**: 현업 전문가가 직접 AI 모델을 튜닝하고 현장에 적용하는 프로세스.
2. **Auto-ML Integrity**: 자동 생성된 모델의 성능 지표(Accuracy, F1-score) 및 편향성 검증 가이드.
3. **Low-Code Deployment**: 컨테이너 기반의 원클릭 AI 모델 배포 및 모니터링 체계.

---
**[V7.5.3_MODERNIZED]**