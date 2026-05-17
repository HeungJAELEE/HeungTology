---
metadata:
  date: "2026-05-16"
  id: "[[[AI] sec-edgar-financial-reports]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "03_AI_Data"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "311baf164384a7f8e7539f66d63849364e3f774af1eed7c05978a830b8350bdd"
object:
  object_type: "Concept"
  tier: 1
  description: '[AI] sec-edgar-financial-reports에 관한 고밀도 지능 노드'
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


# [AI] sec-edgar-financial-reports

## 1. [Dataset Overview: The Financial Blueprint of Industry]
본 데이터셋은 미국 증권거래위원회(SEC)에 공시된 상장 기업들의 정기 보고서 데이터를 구조화한 것임. 단순 숫자를 넘어 기업의 **R&D 전략, 설비 투자(CAPEX) 계획, 기술적 리스크 공시**를 담고 있어, Antigravity Intelligence가 거시 산업 흐름을 분석하는 '전략적 나침반'으로 작동함.

## 2. [Technical Specifications & Access Matrix]

| Parameter | Specification | Access / Source |
| :--- | :--- | :--- |
| **Data Scope** | All U.S. Listed Companies (NVDA, ASML, AMAT, etc.) | `dataset_search_skill.py` |
| **Forms** | 10-K (Annual), 10-Q (Quarterly), 8-K (Current Event) | [Ref: SEC-EDGAR-REST-API] |
| **Data Format** | XBRL (Extensible Business Reporting Language) | [Ref: XBRL-Standard-V2] |
| **Local Skill** | `python 03_Skills/finance/capex_analyzer.py` | [NEW_Skill_Bridge] |

## 3. [Engineering Application: Strategic Intelligence]
1. **CAPEX Tracking**: TSMC, 삼성, 인텔의 설비 투자 규모 추이를 분석하여 차세대 EUV 장비 수요 및 공급망 부하 예측.
2. **R&D Correlation**: 기업의 R&D 비용 지출과 특허 출원 간의 상관관계를 분석하여 기술적 우위(Moat)를 점수화.
3. **Risk Mining**: 보고서 내 'Risk Factors' 섹션을 자연어 처리(NLP)하여 환경 규제, 원자재 수급 불안 등 잠재적 공정 위협 요인 선제 탐지.

## 4. [MCP Replacement: Native Execution]
유료 유통되는 재무 터미널에 의존하지 않고, `dataset_search_skill.py`를 통해 SEC 서버에서 XBRL 데이터를 직접 파싱하여 로컬 볼트에 기업별 재무 프로필을 자동 구축함.

## 5. [Self-Audit Protocol]
1. **Fidelity**: 현금흐름표(Cash Flow)가 손익계산서(Income Statement)보다 전략 분석에 더 중요한 이유는? (정답: 실제 가용 현금이 기술 투자의 실질적 원동력이기 때문)
2. **Connectivity**: 이 데이터셋이 [[ [Dataset] global-industrial-standards-iso-semi ]]와 어떤 관계를 갖는가? (정답: 환경 표준(ISO 14001) 강화에 따른 기업의 탄소 배출 저감 투자 비용 분석)
