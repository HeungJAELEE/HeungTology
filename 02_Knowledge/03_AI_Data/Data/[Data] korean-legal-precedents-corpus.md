---
lineage:
  dataset_reference: korean-legal-precedents-corpus
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
measurement:
  confidence_interval:
  - 0.0
  - 0.0
  instrument: Heuristic_Regex_Parser
  precision: '0.0'
  unit: unknown_unit
  value: 0.0
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Data] korean-legal-precedents-corpus]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for korean-legal-precedents-corpus
  object_type: Data
  tier: 1
properties:
  analysis_depth: Summary, Rationale, Final Verdict
  data_scope: Supreme Court & Lower Court Precedents
  external_data_sources:
  - Public Data Portal
  - Ministry of Government Legislation
  local_skill_path: python 03_Skills/legal/risk_analyzer.py
  search_script: dataset_search_skill.py
semantic:
  alternative_parents: []
  is_instance_of: '[[ [03_AI_Data] [Concept] korean-legal-precedents-corpus]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: automated_classification
  object: Data
  predicate: auto_mapped
  subject: korean-legal-precedents-corpus
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

# [Data] Korean Legal Precedents Corpus

## 1. [Dataset Overview: The Logic of Justice]
본 데이터셋은 대한민국 법원의 판례 데이터를 구조화한 고밀도 텍스트 코퍼스임. Antigravity Intelligence가 산업 현장의 복잡한 법적 분쟁을 해결하고, 사전적으로 컴플라이언스(Compliance) 리스크를 진단하기 위한 '논리적 판결 기반'으로 작동함.

## 2. [Technical Specifications & Access Matrix]

| Parameter | Specification | Access / Source |
| :--- | :--- | :--- |
| **Data Scope** | Supreme Court & Lower Court Precedents | `dataset_search_skill.py` |
| **Search Keys** | Case Number, Keywords, Applicable Law | [데이터 부재] |
| **Analysis Depth** | Summary, Rationale, Final Verdict | [데이터 부재] |
| **Local Skill** | `python 03_Skills/legal/risk_analyzer.py` | [NEW_Skill_Bridge] |

## 3. [Engineering Application: Legal Risk Mitigation]
1. **Clause Retrieval**: 특정 계약서 조항이 과거 판례에서 어떻게 해석되었는지 유사도 검색(Semantic Search)을 통해 즉시 인출.
2. **Liability Assessment**: 사고 발생 시 과거 유사 판례의 과실 비율 데이터를 참조하여 법적 책임 범위를 수리적으로 예측.
3. **Standardization**: 산업 표준([[global-industrial-standards-iso-semi]])과 충돌하는 법적 규제 사항을 식별하여 최적의 SOP 도출.

## 4. [MCP Replacement: Native Execution]
외부 유료 법률 서비스에 의존하지 않고, `dataset_search_skill.py`를 통해 공공 데이터 포털 및 법제처 시스템에서 직접 판례 메타데이터를 사냥하여 로컬 위키에 지식화함.

## 5. [Self-Audit Protocol]
1. **Fidelity**: 판결요지(Summary)와 전문(Full Text) 중 어느 것이 AI 추론에 더 유리한가? (정답: 전문은 상세 맥락 파악에, 판결요지는 빠른 의사결정 경로 구축에 유리함)
2. **Connectivity**: 이 데이터셋이 [[ [Dataset] nvidia-nemotron-personas-korean ]]과 결합할 때의 시너지는? (정답: 법률 전문가 페르소나를 장착하여 고도의 법률 상담 지능 구현 가능)