---
metadata:
  id: "[[[MOC] LLM_&_Agentic_Workflow]]"
  domain: "AI_NLP"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.5.3"
object:
  object_type: "MOC"
  tier: 0
  description: "대규모 언어 모델(LLM) 및 자율적 에이전트 워크플로우를 위한 지식 거점 (Map of Content)"
semantic:
  tags: ["#AI", "#LLM", "#Agentic_Workflow", "#NLP", "#Generative_AI", "#MOC"]
lineage:
  dataset_reference: "Antigravity Knowledge Vault"
  original_author: "Antigravity Vault"
spo_graph:
  - subject: "LLM"
    predicate: "powers"
    object: "Agentic Workflow"
fidelity_engine:
  engine_id: "GraphFidelityEngine_V7.5.3"
  status: "Active"
dynamic:
  status: "Ratified"
  decay_rate: 0.0
Trust Metrics:
  T_static: 1.0
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
