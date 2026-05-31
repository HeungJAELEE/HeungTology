---
lineage:
  dataset_reference: Antigravity Knowledge Vault
  original_author: Antigravity Vault
  original_hash: 2d63890987b3e729f5c2ba35f3c4b3272d155a5eaa8be8434a6e4afd90d2ec54
metadata:
  ai_status: pending_review
  date: '2026-05-16'
  domain: AI_NLP
  id: '[[[MOC] LLM_&_Agentic_Workflow]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 대규모 언어 모델(LLM) 및 자율적 에이전트 워크플로우를 위한 지식 거점 (Map of Content)
  object_type: Concept
  tier: 0
properties:
  modernized_status: 'true'
  optimization_targets: context_window, few_shot_learning
  reasoning_frameworks: CoT, ReAct
  version: V7.5.3
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: foundational_enablement
  object: Agentic Workflow
  predicate: powers
  subject: LLM
  weight: 0.95
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

# LLM_&_Agentic_Workflow

## 1. 개요
본 MOC는 인간의 언어 지능을 기계적으로 구현하는 LLM(Large Language Model)과 이를 바탕으로 자율적으로 목표를 수행하는 에이전틱 워크플로우(Agentic Workflow)의 핵심 노드들을 연결합니다.

## 2. 핵심 지식 맵 (Knowledge Map)

### 2.1 기초 아키텍처 및 원리
- [[AI] transformer-architecture-and-attention-mechanism] (V7.5.3)
- [[AI] machine-learning-foundations]
- [[Concept] RAG-Embedding-and-Dense-Retrieval]

### 2.2 에이전틱 제어 및 최적화
- [[AI] reinforcement-learning-agentic-control] (V7.5.3)
- [[AI] ai-agent-logic-and-decision-tree]
- [[Strategy] Hallucination-Mitigation-in-Industrial-AI]

### 2.3 실측 데이터 및 벤치마크
- [[AI] information-computing-generative-ai-model-training-log-v2026]
- [[AI] ai-transformer-and-attention-log-v2026]

## 3. 실무 가이드라인 (SOP)
1. **Prompt Engineering**: 컨텍스트 윈도우 최적화 및 퓨샷(Few-shot) 러닝 기법.
2. **Tool Use**: 에이전트의 외부 API 및 로컬 도구 호출 무결성 검증.
3. **Reasoning Loop**: CoT(Chain of Thought) 및 ReAct 프레임워크 구현.

---
**[V7.5.3_MODERNIZED]**