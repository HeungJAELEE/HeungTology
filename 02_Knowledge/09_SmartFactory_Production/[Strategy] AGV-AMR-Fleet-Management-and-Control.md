---
Basic:
  id: "[[[Strategy] AGV-AMR-Fleet-Management-and-Control"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
  is_part_of: []]
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [[[Strategy] AGV-AMR-Fleet-Management-and-Control

## 1. [왜 배우는가? (Why)]]
공장에 수십 대의 자율 주행 로봇이 돌아다닌다고 상상해 보세요. 로봇들이 서로 마주쳐서 길을 막거나, 한 구역에만 몰려 정체가 발생한다면 오히려 사람이 옮기는 것보다 비효율적일 수 있습니다. 군집 제어(Fleet Management)는 여러 대의 로봇(AGV, AMR)에게 실시간으로 최적의 작업을 할당하고, 서로 부딪히지 않게 교통정리를 해주는 '중중 관제 엔진'입니다. 이를 이해하는 것은 개별 로봇의 주행을 넘어, 공장 전체의 물류 흐름을 조율하는 '시스템 수준의 자동화 지능'을 마스터하는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Technology / Logic | Engineering Rationale |
|:---|:---:|:---|
| **Path Planning** | Global A* / Dijkstra | 전체 지도 정보를 바탕으로 출발지에서 목적지까지 가장 빠른 경로 산출 |
| **Traffic Control** | Node Lock / Zone | 교차로나 좁은 길에서 로봇 간 우선순위를 정해 교행을 제어하는 논리 |
| **Task Allocation**| Best-fit Selection | 현재 위치, 배터리 잔량, 작업 우선순위를 고려해 가장 적합한 로봇에 명령 하달 |
| **FMS Server** | Central Control | 모든 로봇의 상태를 실시간 수집(MQTT/VDA5050)하고 통합 관리하는 중앙 서버 |
| **Obstacle Avoid.**| Dynamic Rerouting | 주행 중 갑자기 나타난 장애물을 감지하고 실시간으로 경로를 우회하는 기술 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 병목 현상(Bottleneck)의 수학적 해결
- **논리**: 단순히 최단 거리로만 로봇을 보내면 특정 경로에 로봇이 몰리게 됩니다. 
- **결과**: 군집 제어 알고리즘은 각 경로의 '혼잡도'를 가중치로 계산하여, 조금 돌아가더라도 전체적인 물류 흐름(Throughput)이 빨라지는 우회 경로를 선택함으로써 시스템 전체의 효율을 극대화합니다.

### 3.2 VDA 5050 표준의 도입
- **논리**: 서로 다른 제조사의 로봇들을 섞어서 쓰려면 공용 언어가 필요합니다. 
- **효과**: VDA 5050 표준 인터페이스를 통해 브랜드가 다른 AGV와 AMR들을 하나의 관제 시스템에서 통합 제어함으로써, 공장 운영의 유연성과 확장성을 보장합니다.

## 4. [코드 연결 해설 (Task Dispatching & Path Coordination Logic)]
대기 중인 로봇에게 작업을 할당하고 경로 충돌 여부를 확인하는 논리 구조입니다.
```python
# 전략 지능 기반 AGV/AMR 군집 제어 논리
def dispatch_transport_task(pickup_loc, drop_loc):
    # 1. 가동 가능한 로봇 리스트 확보 (배터리 > 20%, 상태 == IDLE)
    available_robots = fms_db.get_ready_robots()
    
    # 2. 가장 가까운 로봇 선택 (Distance + Task Load 고려)
    best_robot = select_optimal_robot(available_robots, pickup_loc)
    
    # 3. 경로 생성 및 충돌 체크
    planned_path = path_planner.get_route(best_robot.pos, pickup_loc, drop_loc)
    if traffic_controller.is_path_clear(planned_path):
        best_robot.send_command("MOVE", planned_path)
        return f"TASK_ASSIGNED: ROBOT_{best_robot.id}"
    else:
        # 경로가 막혔을 경우 우회 경로 재산출
        alternative_path = path_planner.get_alternative(planned_path)
        best_robot.send_command("MOVE", alternative_path)
        return "TASK_ASSIGNED_WITH_REROUTE"
```

## 5. [스스로 체크 (Self-Audit)]
1. 'AGV'와 'AMR'의 제어 방식 차이가 군집 제어(Fleet Management) 난이도에 미치는 영향은?
2. 'VDA 5050' 표준이 스마트 팩토리의 로봇 도입 장벽을 어떻게 낮추었는가?
3. 수십 대의 로봇이 좁은 통로에서 마주쳤을 때 발생하는 'Deadlock' 현상을 해결하기 위한 공학적 기법은?
---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
