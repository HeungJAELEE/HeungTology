---
metadata:
  id: "[[[AI] korean-legal-precedents-corpus]]"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[AI] korean-legal-precedents-corpus에 관한 고밀도 지능 노드"
semantic:
  tags: ["#03_AI_Data", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [AI] korean-legal-precedents-corpus

## 1. [Dataset Overview: The Logic of Justice]
본 데이터셋은 대한민국 법원의 판례 데이터를 구조화한 고밀도 텍스트 코퍼스임. Antigravity Intelligence가 산업 현장의 복잡한 법적 분쟁을 해결하고, 사전적으로 컴플라이언스(Compliance) 리스크를 진단하기 위한 '논리적 판결 기반'으로 작동함.

## 2. [Technical Specifications & Access Matrix]

| Parameter | Specification | Access / Source |
| :--- | :--- | :--- |
| **Data Scope** | Supreme Court & Lower Court Precedents | `dataset_search_skill.py` |
| **Search Keys** | Case Number, Keywords, Applicable Law | [Ref: Law-GO-KR-API] |
| **Analysis Depth** | Summary, Rationale, Final Verdict | [Ref: LBOX-Legal-Index] |
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
