---
lineage:
  dataset_reference: Antigravity Knowledge Vault
  original_author: Antigravity Vault
  original_hash: 1123dba9bdbce0b23bcbc57109d9440c21a5ca62b7a7efd83264f495872008df
metadata:
  ai_status: pending_review
  date: '2026-05-16'
  domain: AI_Generative
  id: '[[[MOC] 03_02_Generative_AI]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 텍스트, 이미지, 단백질 구조 등 신규 데이터를 생성하는 생성형 AI 핵심 기술 노드 거점
  object_type: Concept
  tier: 0
properties:
  sop_fidelity_guard_objective: physical_validity_verification
  sop_model_distillation_target: edge_ai_lightweighting
  sop_prompt_governance_focus: data_leakage_prevention
  version: 7.5.3
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: synthetic_content_generation
  object: Synthetic Content
  predicate: creates
  subject: Generative AI
  weight: 1.0
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

# 03_02_Generative_AI

## 1. 개요
본 MOC는 인간의 창의성을 기계적으로 모사하고 확장하는 생성형 AI(Generative AI)의 핵심 모델들과 알고리즘을 연결합니다.

## 2. 핵심 지식 맵 (Knowledge Map)

### 2.1 대규모 언어 모델 (LLM) 및 에이전트
- [[MOC] LLM_&_Agentic_Workflow] (V7.5.3)
- [[AI] transformer-architecture-and-attention-mechanism] (V7.5.3)
- [[AI] reinforcement-learning-agentic-control] (V7.5.3)

### 2.2 확산 모델 (Diffusion) 및 멀티모달
- [[AI] synthetic-biology-protein-design-ai] (V7.5.3)
- [[Concept] Diffusion-Models-in-Biological-Design]
- [[AI] multimodal-fusion-strategies]

### 2.3 생성 무결성 및 윤리
- [[Strategy] Hallucination-Mitigation-in-Industrial-AI]
- [[AI] agi-alignment-theory]

## 3. 실무 가이드라인 (SOP)
1. **Model Distillation**: 대형 생성 모델의 지식 증류를 통한 산업용 에지 AI 경량화.
2. **Fidelity Guard**: 생성된 데이터(이미지, 단백질 구조)의 물리적 타당성 검증 루프.
3. **Prompt Governance**: 기업용 보안 프롬프트 가이드라인 및 데이터 유출 방지 체계.

---
**[V7.5.3_MODERNIZED]**