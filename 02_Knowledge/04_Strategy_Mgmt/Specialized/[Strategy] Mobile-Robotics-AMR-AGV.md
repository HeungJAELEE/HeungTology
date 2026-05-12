---
Basic:
  id: "[[[Strategy] Mobile-Robotics-AMR-AGV"
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

# [[[Strategy] Mobile-Robotics-AMR-AGV

## 1. [왜 배우는가? (Why)]]
공장의 바닥에 더 이상 검은 테이프나 마커가 필요 없습니다. 모바일 로보틱스(Mobile-Robotics-AMR-AGV)는 로봇이 스스로 길을 찾고, 장애물을 피하며, 물건을 나르는 기술입니다. 과거의 무인 운반차(AGV)가 정해진 길로만 다녔다면, 현재의 자율 이동 로봇(AMR)은 눈(LiDAR/Camera)을 통해 실시간으로 지도를 그리며 가장 빠른 길을 찾아냅니다. 이를 이해하는 것은 수백 대의 로봇이 개미 떼처럼 일사불란하게 움직이는 '역동적인 물류망'을 구축하여, 공장 전체의 흐름을 지능적으로 가속하는 '자율 물류의 지휘자'가 되는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Feature | AGV (Legacy) | AMR (Autonomous) | Engineering Rationale |
|:---|:---:|:---:|:---|
| **Navigation** | Fixed Path (Magnetic/QR) | SLAM (LiDAR/Vision) | 유연한 공정 배치를 위해 가이드 없는 자율 주행 필수 |
| **Obstacle** | Stop and Wait | Dynamic Rerouting | 생산 라인의 혼잡을 막기 위해 장애물 우회 및 경로 재탐색 능력 중요 |
| **Localization** | Beacon/Encoder | Feature Matching | 공장 환경 변화에도 정확한 자기 위치 파악(1cm 이내) |
| **Fleet Mgmt** | Centralized Dispatch | Distributed Coordination | 수백 대의 로봇이 충돌 없이 협업하기 위한 군집 지능 관리 |
| **Integration** | Manual I/O | API / WMS Integration | 전사적 자원 관리 시스템과 연동된 지능형 작업 할당 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 SLAM (Simultaneous Localization and Mapping)
- **논리**: 로봇은 자신의 위치를 모르고는 지도를 그릴 수 없고, 지도가 없으면 위치를 알 수 없습니다. (닭과 달걀의 문제) 
- **결과**: LiDAR와 오도메트리(바퀴 회전수) 데이터를 칼만 필터(Kalman Filter)나 그래프 최적화로 융합하여, 움직이면서 동시에 지도를 완성하고 자신의 위치를 정밀하게 추정합니다.

### 3.2 RobotOps를 통한 군집 효율 극대화
- **논리**: 개별 로봇이 똑똑해도 서로 엉키면 전체 효율은 떨어집니다. 
- **효과**: 수백 대의 로봇 상태를 실시간 모니터링하고, 배터리 충전 시점과 작업 경로를 AI로 최적화하여 공장 내 물류 정체(Bottleneck)를 30% 이상 해소합니다.

### 3.3 경로 계획 (Path Planning) 알고리즘
- **논리**: 최단 거리가 반드시 최적의 길은 아닙니다. 
- **결과**: A* 알고리즘으로 최단 경로를 찾고, 동적 장애물이 나타나면 D* 알고리즘을 통해 즉시 우회 경로를 생성함으로써 작업 지연을 최소화합니다.

## 4. [코드 연결 해설 (Autonomous Path Selection Logic)]
현재 위치에서 목표 지점까지 장애물을 회피하며 이동 경로를 생성하고 상태를 보고하는 논리 구조입니다.
```python
# 모바일 로봇(ISM) 기반 자율 주행 및 경로 최적화 논리
def plan_autonomous_navigation(current_pose, target_destination, obstacles):
    # 1. 실시간 지도 상 위치 보정 (Localization)
    # 주변 지형지물(Map Features)과 센서 데이터 매칭
    refined_pose = slam_engine.update_pose(current_pose, sensor_data.lidar)
    
    # 2. 전역 경로 생성 (Global Path Planning)
    # A* 알고리즘을 사용하여 정적 지도상의 최적 경로 탐색
    global_path = path_planner.find_global_path(refined_pose, target_destination)
    
    # 3. 국부 장애물 회피 (Local Obstacle Avoidance)
    # 경로상에 갑자기 나타난 장애물(작업자 등) 감지 시 D* 알고리즘 가동
    if obstacles.is_blocking(global_path):
        local_reroute = path_planner.generate_local_reroute(refined_pose, global_path)
        final_path = local_reroute
    else:
        final_path = global_path
        
    # 4. 모터 제어 명령 전송 (Motion Control)
    # 가감속 곡선을 고려한 속도 및 조향 값 계산
    velocity_cmd = motion_controller.calculate_velocity(final_path)
    
    # 5. 군집 관리 시스템(FMS) 상태 보고
    fms_client.report_status(refined_pose, battery_level, current_task="DELIVERY")
    
    return {"path": final_path, "velocity": velocity_cmd}
```

## 5. [스스로 체크 (Self-Audit)]
1. 'AMR'이 'AGV'보다 초기 도입 비용은 높지만 'TCO(총 소유 비용)' 측면에서 장기적으로 유리한 공학적 이유는 무엇인가?
2. 'LiDAR SLAM'과 'Visual SLAM'의 기술적 장단점과, 금속 반사가 심한 '반도체 클린룸'에서 더 권장되는 방식은?
3. '수백 대의 로봇'이 좁은 통로에서 마주쳤을 때 발생하는 '데드락(Deadlock)' 현상을 해결하기 위한 'FMS(군집 관리 시스템)'의 우선순위 제어 논리는?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
