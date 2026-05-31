---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: e0292262ea8dc3015a0344ca14e85cb71b4cdc2239e6087d333b5042fbbde95b
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-16'
  domain: _Archive
  id: '[[[_Archive] dummy-action-node]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: dummy-action-node에 관한 고밀도 지능 노드
  object_type: Data
  tier: 1
properties:
  action_layer: Executable_Action
  aip_version: V6.4
  system_name: Palantir AIP
  test_purpose: integrity_verification
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] _Archive]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: interface_integrity_verification
  object: Concept
  predicate: contains_knowledge_of
  subject: dummy-action-node
  weight: 0.5
temporal:
  valid_from: '2026-05-24T00:28:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# dummy-action-node

이 문서는 V6.4 Palantir AIP 모드의 **실행 가능성(Actionable)** 및 **더미 액션 테스트**를 위한 노드입니다. 
이 노드가 검색되면, 에이전트는 반드시 하단의 `Executable_Action` 레이어를 해석하여 사용자에게 결재(Y/N)를 요청해야 합니다.

본문에는 특별한 기술적 내용이 없으며, 오직 AIP 핸드오프 인터페이스의 무결성을 검증하기 위한 용도로만 사용됩니다.