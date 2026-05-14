---
Basic_Layer:
  id: "dummy-action-node"
  title: "Dummy Action Node"
  category: "Test"
  tags: ["AIP", "Test", "Actionable"]
Object_Layer:
  object_type: "Concept"
  priority: "Low"
Semantic_Layer:
  domain: "System"
  topology: "Infrastructure"
Dynamic_Layer:
  status: "Experimental"
  version: "V6.4.2"
Trust_Metrics:
  T_static: 0.0
  T_dynamic: 0.0
Lineage:
  logic_provenance: "V6.4 Test Protocol"
Executable_Action:
  has_action: false
  action_type: "run_dummy_script"
  target_script: "C:/Anitigravity/04_Tools/dummy_execute.py"
  params: { "mode": "fast", "value": "100" }
---

# Dummy Action Node (더미 액션 테스트 노드)

이 문서는 V6.4 Palantir AIP 모드의 **실행 가능성(Actionable)** 및 **더미 액션 테스트**를 위한 노드입니다. 
이 노드가 검색되면, 에이전트는 반드시 하단의 `Executable_Action` 레이어를 해석하여 사용자에게 결재(Y/N)를 요청해야 합니다.

본문에는 특별한 기술적 내용이 없으며, 오직 AIP 핸드오프 인터페이스의 무결성을 검증하기 위한 용도로만 사용됩니다.
