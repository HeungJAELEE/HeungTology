---
metadata:
  date: "2026-05-16"
  id: "[[[AI] mcp-opencrab-functional-blueprint-and-dataset-list]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "03_AI_Data"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "82736cf39e8620bb95ad2abd883ebe75c4cfdc60142ca2119515a7d1cbb0cef5"
object:
  object_type: "Concept"
  tier: 1
  description: '[AI] mcp-opencrab-functional-blueprint-and-dataset-list에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] Global-Dataset-Inventory-Hub]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [AI] mcp-opencrab-functional-blueprint-and-dataset-list

## 1. [왜 내재화하는가? (Knowledge Sovereignty)]
외부 서비스(MCP) 유료화 및 차단에 대비하여, MCP가 제공하던 핵심 데이터셋 검색 및 가공 기능을 Antigravity 로컬 볼트로 **강제 이식**함. 서비스가 중단되어도 위키의 좌표와 로컬 스크립트를 통해 지능의 연속성을 사수함.

## 2. [오픈크랩(Open-Graph) 핵심 기능 복제 (Functional Clones)]

| MCP Function (Original) | Local Wiki/Skill Counterpart | Logic & Coordinates |
| :--- | :--- | :--- |
| **Dataset Discovery** | `v637_quarantine_scanner.py` | 특정 도메인(반도체, 화학) 키워드 기반 웹 크롤링 로직 |
| **Chemical Structure Search** | [[ [Dataset] chemistry-datasets-structures-v6 ]] | ChEMBL/PubChem 직접 API 호출 좌표 및 활용 가이드 |
| **Persona Synthesis** | [[ [Dataset] nvidia-nemotron-personas-korean ]] | Nemotron-3 8B 기반 합성 데이터 생성 프롬프트 엔지니어링 |
| **Graph Topology Link** | `graphify-skill.md` | 데이터셋 간 관계를 Neo4j로 자동 맵핑하는 로컬 알고리즘 |

## 3. [긴급 백업 데이터셋 리스트 (Priority Target List)]
유료화 전 반드시 로컬로 긁어와야 할 데이터셋 좌표:
1. **Semiconductor Material Data**: [NIST/Materials Project] 기반 반도체 물성치 전수 리스트.
2. **Battery Cycle Logs**: 공공 배터리 성능 저하 데이터셋(NASA/MIT) 샘플링.
3. **Instruction Sets**: 오픈소스 최고 성능의 한국어 지침셋(KoAlpaca 등) 메타데이터.

## 4. [Action Plan: Total Internalization]
- **Step 1**: MCP가 막히기 전 모든 리소스의 `metadata`와 `schema`를 텍스트로 추출하여 위키 노드로 변환.
- **Step 2**: 추출된 스키마를 바탕으로 `03_Skills`에 전용 크롤러(Python) 구축.
- **Step 3**: MCP 서버 삭제 후 로컬 위키 기반의 독립 RAG 체계 가동.

## 5. [🔗 참조된 로컬 지식망]
- [[ [MOC] Global-Dataset-Inventory-Hub ]]
- [[ [MOC] 53_quantum-computing-and-advanced-ai-infrastructure-hub ]]
- [[ [MOC] 11_global-entities-and-materials-hub ]]
- [[[Data] opencrab-workspace-catalog-quarantine]] : 오픈크랩 55대 작업공간 데이터 팩 검역 노드
- [[[Data] opencrab-alexai-ontology-packs-quarantine]] : AlexAI 12대 온톨로지 지식 팩 검역 노드
