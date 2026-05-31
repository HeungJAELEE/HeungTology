---
lineage:
  dataset_reference: nvidia-nemotron-personas-korean-instruction-tuning
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
measurement:
  confidence_interval:
  - 0.0
  - 0.0
  instrument: Heuristic_Regex_Parser
  precision: '0.0'
  unit: unknown_unit
  value: 2.1
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Data] nvidia-nemotron-personas-korean-instruction-tuning]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for nvidia-nemotron-personas-korean-instruction-tuning
  object_type: Data
  tier: 1
properties:
  base_model: nvidia-nemotron-3-8b
  data_format: jsonl/parquet
  dataset_size: 20,000+
  huggingface_endpoint: https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea
  integration_environment: antigravity_mcp
  language_profile: korean
  mcp_connector: mcp-server-dataset-navigator
  open_graph_link: open-graph-dataset-crawler
semantic:
  alternative_parents: []
  is_instance_of: '[[ [03_AI_Data] [Concept] nvidia-nemotron-personas-korean-instruction-tuning]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: automated_system_mapping
  object: Data
  predicate: auto_mapped
  subject: nvidia-nemotron-personas-korean-instruction-tuning
  weight: 0.7
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

# [Data] Nvidia Nemotron Personas Korean Instruction Tuning

## 1. [Dataset Overview: High-Fidelity Persona Alignment]
NVIDIA Nemotron-Personas-Korea는 한국어 LLM의 **지침 이행(Instruction Following)** 및 **페르소나 일관성(Persona Consistency)** 강화를 위해 설계된 고밀도 합성 데이터셋임. NVIDIA Nemotron-3 8B 모델을 활용하여 생성되었으며, 단순 번역이 아닌 한국어 고유의 문화적 맥락과 비즈니스 에티켓, 기술적 전문 용어를 포함하도록 정제됨 [데이터 부재].

## 2. [Technical Specifications & Access Matrix]

| Parameter | Specification | Access / Source |
| :--- | :--- | :--- |
| **Dataset Size** | 20,000+ Samples | [🌐 HuggingFace Repo](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea) |
| **Language Profile** | Korean (Native Level) | [데이터 부재] Section 2.1 |
| **Data Format** | JSONL / Parquet | [데이터 부재] Section 2.2 |
| **MCP Connector** | `mcp-server-dataset-navigator` | [데이터 부재] |
| **Open-Graph Link** | `open-graph-dataset-crawler` | [데이터 부재] |

## 3. [MCP & Open-Graph Integration Guide]
본 데이터셋은 Antigravity MCP 환경을 통해 '실시간 리트리벌'이 가능하도록 맵핑됨.

### 3.1 Dataset Retrieval Protocol
*   **MCP Command**: `mcp call dataset-navigator search --query "NVIDIA Nemotron Korean"`
*   **Open-Graph Integration**: 오픈크랩(Open-Graph) 엔진을 가동하여 HuggingFace의 최신 업데이트 및 파생 데이터셋(Derived Datasets)을 자동으로 크롤링하여 `01_Inbox`에 동기화함 [데이터 부재].

## 4. [Engineering Application: Persona-Based SFT]
1. **Persona Injection**: 시스템 프롬프트에 정의된 페르소나와 데이터셋의 질의응답 쌍을 매칭하여 일관성 점수(Consistency Score) 산출.
2. **Instruction Tuning**: 한국어 특유의 존칭어 체계와 기술적 문맥을 동시에 유지하는 Supervised Fine-Tuning 파이프라인 구축.
3. **Fidelity Audit**: 생성된 답변의 공학적 정확도를 `FidelityEngine`을 통해 교차 검증 [데이터 부재].

## 5. [Self-Audit Protocol]
1. **Retrieval**: MCP를 통해 이 데이터셋의 최신 Parquet 파일 경로를 확보하는 방법은? (정답: `dataset-navigator` 툴 가동)
2. **Fidelity**: 합성 데이터 특유의 환각(Hallucination)을 방지하기 위한 NVIDIA의 필터링 기전은 무엇인가?
3. **Connectivity**: 이 데이터셋 노드가 **Open-Graph** 내에서 '화학 데이터셋'과 어떤 시맨틱 위상차를 갖는가?