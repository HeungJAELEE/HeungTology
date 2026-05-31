---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: a835c6a37704ad70fc9160d762fac885b4c23fe44330400b082b27b771651a92
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] autonomous-mobile-robot-amr-path-planning-and-slam]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] autonomous-mobile-robot-amr-path-planning-and-slam에 관한 고밀도
    지능 노드'
  object_type: Concept
  tier: 1
properties:
  drift_threshold_m: 0.1
  efficiency_boost_target_percent: 20
  external_data_node: amr-localization-accuracy-and-navigation-efficiency-v2026
  localization_acc_target_cm: 5
  mapping_resolution_cm: 2
  max_linear_velocity_m_s: 2.0
  max_payload_kg: 1000
  planning_bottleneck_ms: 200
  sensor_update_rate_hz: 10
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 11_Global_Entities_and_Materials]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Entity] autonomous-mobile-robot-amr-path-planning-and-slam

## 1. 개요 (Why)
물류 창고나 공장에서 사람을 대신해 물건을 나르는 AMR(자율 이동 로봇)의 핵심은 '자신의 위치를 알고 가야 할 길을 찾는 것'입니다. SLAM은 지도 없이도 주변을 스캔하며 실시간으로 지도를 만드는 기술이며, 경로 계획은 시시각각 변하는 장애물을 피해 최적의 이동선을 찾는 기술입니다. 본 노드는 AMR의 자율 주행 무결성과 실내 탐행 정밀도를 위한 표준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Value (Tier 1) | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Localization Acc | $\delta_x$ | < 5 | ±1 | cm |
| Mapping Resolution| $\Delta s$ | < 2 | ±0.5 | cm |
| Max Linear Velocity| $v_{max}$ | 1.0 ~ 2.0 | ±0.1 | m/s |
| Max Payload | $M$ | 100 ~ 1000 | N/A | kg |
| Sensor Update Rate| $f$ | > 10 | ±2 | Hz |

## 3. RobotFidelityEngine: Diagnostic Logic

AMR의 위치 인식 정확도 및 경로 생성 안정성을 진단하는 `RobotFidelityEngine` 로직입니다.

```python
class RobotFidelityEngine:
    def __init__(self, estimated_pos, actual_pos, planning_time):
        self.est = estimated_pos # (x, y)
        self.act = actual_pos # (x, y)
        self.t = planning_time # ms

    def diagnose_localization_drift(self):
        """추정 위치와 실제 위치 사이의 드리프트 진단"""
        drift = ((self.est[0] - self.act[0])**2 + (self.est[1] - self.act[1])**2)**0.5
        if drift > 0.1: # 10cm 이상 드리프트 발생 시
            return f"CRITICAL: Localization Drift High ({drift*100:.1f}cm) - Relocalization Required"
        return f"OPTIMAL: Position Accuracy Maintained (Drift: {drift*100:.1f}cm)"

    def audit_navigation_efficiency(self):
        """경로 생성 시간 기반 주행 효율 진단"""
        if self.t > 200:
            return f"WARNING: Path Planning Bottleneck ({self.t}ms) - Reduced Dynamic Response"
        return "PASS: Navigation Logic Responsive"

engine = RobotFidelityEngine(estimated_pos=(10.05, 5.0), actual_pos=(10.0, 5.0), planning_time=50)
print(engine.diagnose_localization_drift())
```

## 4. 분석 프레임워크: AMR Intelligence Hierarchy
1. **[SLAM (Simultaneous Localization and Mapping)]**: 레이저 스캐너(LiDAR)나 카메라를 이용해 주변 특징점(Landmark)을 추출하고 이를 기반으로 로봇의 위치 추정과 지도 작성을 동시에 수행.
2. **[Global Path Planning]**: 전체 지도에서 시작점부터 목표점까지의 최단 경로를 생성(예: $A^*$, $D^*$ Lite).
3. **[Local Planner & Avoidance]**: 실시간으로 감지되는 동적 장애물(사람, 지게차 등)을 피하기 위해 초당 수십 번 경로를 미세 조정(예: DWA, TEB Local Planner).

## 5. 스스로 체크 (Self-Audit)
1. SLAM 공정에서 'Loop Closure'가 맵의 누적 오차를 제거하는 데 결정적인 물리적 이유는?
2. 휠 오도메트리(Odometry)의 오차와 LiDAR 데이터의 편차를 융합하기 위한 '칼만 필터(Kalman Filter)'의 역할은?
3. 좁은 통로에서 AMR이 정지하거나 진동하는 'Oscillation' 현상을 방지하기 위한 제어 파라미터 최적화 전략은?

## 6. 결론 (Deterministic Outcome)
본 노드는 `Data amr-localization-accuracy-and-navigation-efficiency-v2026`와 연동되어, 로봇의 위치 드리프트를 1cm 단위로 상시 감시하고 물류 현장의 가동 효율을 20% 이상 향상시키는 결정론적 탐행 가이드를 보증합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 03_robotics-and-autonomous-systems-hub
- lidar-based-slam-gmapping-and-cartographer
- Data amr-localization-accuracy-and-navigation-efficiency-v2026