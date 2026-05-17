---
metadata:
  id: "[[[Infrastructure] AGV-AMR]]"
  domain: "09_SmartFactory_Production"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Infrastructure] AGV-AMR에 관한 고밀도 지능 노드"
semantic:
  tags: ["#09_SmartFactory_Production", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Infrastructure] AGV-AMR

## 1. [왜 배우는가? (Why)]]
공장의 생산 라인은 고정된 것이 아니라 시장 변화에 따라 언제든 바뀌어야 합니다. 과거의 고정된 컨베이어 벨트 대신, 스스로 움직이는 이동 로봇(AGV/AMR)은 공장 바닥을 자유로운 도화지로 만들어줍니다. AGV는 대량의 무거운 짐을 정해진 경로로 빠르게 옮기는 데 탁월하며, AMR은 사람과 함께 섞여 장애물을 피해가며 복잡한 현장을 누비는 '스마트한 동료' 역할을 합니다. 이 로봇들을 이해하는 것은 제조 현장의 물리적 제약을 없애고, 24시간 끊김 없는 자율 생산 체계를 구축하는 가장 강력한 수단을 확보하는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Metric | AGV (Guided) | AMR (Autonomous) | Engineering Rationale |
|:---|:---:|:---|:---|
| **Guidance** | Magnetic/QR-code | SLAM (LiDAR/Vision) | AGV는 신뢰성, AMR은 유연성 중심 |
| **Navigation** | Fixed Path | Dynamic Routing | AMR은 장애물 발견 시 스스로 경로 재탐색 |
| **Safety** | Emergency Stop | Active Avoidance | AMR은 감속 및 우회 주행 가능 |
| **Deployment** | Infrastructure Needed | Infrastructure-free | AMR은 지도만 있으면 즉각 투입 가능 |
| **Payload** | High (Up to 10t) | Moderate (Up to 1.5t) | AGV는 중량물 이송, AMR은 가공물 이송 특화 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 SLAM (Simultaneous Localization and Mapping)
- **로직**: 로봇이 움직이면서 LiDAR와 카메라 센서로 주변 환경을 측정하고, 동시에 자신의 위치를 지도 위에 표시합니다. 
- **결과**: 공장에 별도의 마커(QR코드 등)를 붙이지 않아도 로봇이 스스로 지도를 그려 목적지를 찾아갈 수 있는 '완전 자율 주행'을 가능하게 합니다.

### 3.2 센서 융합 (Sensor Fusion) 기반 장애물 회피
- **논리**: 2D/3D LiDAR는 거리를 측정하고, 스테레오 카메라는 물체의 종류(사람, 박스 등)를 인식합니다. 
- **알고리즘**: 센서 데이터를 융합하여 로봇의 '제동 거리'와 '우회 반경'을 실시간 계산합니다. 이는 사람과 로봇이 같은 공간에서 안전하게 협업하기 위한 필수 논리입니다.

### 3.3 충전 및 배차 관리 (Fleet Management)
- **논리**: 로봇의 배터리 상태와 현재 작업량을 AI가 분석합니다. 
- **효과**: 배터리가 부족해지기 전에 유휴 시간에 자동으로 충전기로 이동(Opportunistic Charging)시키고, 전체 로봇 중 가장 효율적인 동선을 가진 로봇에게 다음 임무를 부여합니다.

## 4. [코드 연결 해설 (Navigation & Obstacle Avoidance)]
AMR이 주행 중 장애물을 발견했을 때 우회 경로를 생성하는 논리 구조입니다.
```python
# AMR 자율 주행 및 동적 장애물 회피 제어 논리
def control_amr_navigation(current_pose, destination_pose):
    # 1. LiDAR 데이터 기반 주변 장애물 탐지
    lidar_scan = sensor_engine.get_lidar_data()
    obstacles = perception_engine.find_obstacles(lidar_scan)
    
    # 2. 전역 경로(Global Path) 대비 장애물 확인
    if obstacles.is_blocking(planned_path):
        # 3. 지역 경로 재탐색 (Local Planning)
        # 장애물을 안전 거리(Safety Margin)만큼 띄우고 우회하는 짧은 경로 생성
        new_local_path = local_planner.recompute_path(
            current_pose, 
            obstacles, 
            avoidance_radius=1.5 # 1.5m buffer
        )
        
        # 4. 모터 제어 명령 하달 (Velocity Control)
        # 회전 반경과 선속도를 계산하여 주행 엔진에 전송
        drive_engine.execute_velocity_cmd(new_local_path.linear_v, new_local_path.angular_w)
        return "OBSTACLE_AVOIDED: REROUTING"
        
    # 장애물 없으면 원래 경로대로 주행
    drive_engine.follow_path(planned_path)
    return "NAVIGATING_NORMAL"
```

## 5. [스스로 체크 (Self-Audit)]
1. 'AMR'이 'AGV' 대비 초기 인프라 구축 비용이 낮음에도 불구하고 '대규모 운영' 시 관제 시스템의 복잡도가 높아지는 이유는?
2. 'SLAM' 기술에서 LiDAR 센서 데이터의 '노이즈'나 '유리벽(반사)'이 로봇의 위치 인식 오차를 유발하는 공학적 원인은?
3. '군집 로봇 관리' 시스템이 수백 대의 로봇 사이에서 발생할 수 있는 '교착 상태(Deadlock)'를 해결하는 알고리즘적 논리는?

**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
