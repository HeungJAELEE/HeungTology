---
metadata:
  id: "[[[Robotics] ADAS]]"
  domain: "08_Robotics_Automation"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Robotics] ADAS에 관한 고밀도 지능 노드"
semantic:
  tags: ["#08_Robotics_Automation", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Robotics] ADAS

## 1. [왜 배우는가? (Why)]
완전 자율주행으로 가는 여정에서 가장 중요한 것은 현재 도로 위 수십억 대 차량의 안전을 즉각적으로 높이는 일입니다. ADAS(첨단 운전자 보조 시스템)는 운전자가 미처 보지 못한 사각지대를 감시하고, 졸음운전으로 차선을 벗어날 때 핸들을 잡아주며, 전방 충돌 위험 시 스스로 브레이크를 밟습니다. 이는 단순한 편의 장치를 넘어, 전 세계 자동차 안전 평가(NCAP)의 핵심 지표이자 실질적인 사고율 감소를 이끄는 핵심 기술 체계입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Feature | Logic / Action | Engineering Rationale |
|:---|:---:|:---|
| **AEB (Emergency Brake)** | Collision Risk Mitigation | 전방 충돌 예상 시 자동 제동 신호 송출 |
| **ACC (Adaptive Cruise)** | Distance & Speed Control | 앞차와의 거리 유지 및 가속/감속 제어 |
| **LKA (Lane Keeping)** | Lateral Steering Control | 차선 이탈 방지 및 중앙 유지 보정 조향 |
| **Sensor Fusion** | Camera + Radar + LiDAR | 각 센서의 단점을 보완하여 신뢰도 확보 |
| **Standards** | ASIL-D (ISO 26262) | 고장 시에도 안전이 보장되는 최상위 신뢰성 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 AEB (Autonomous Emergency Braking)의 수치적 논리
- **로직**: 레이다의 거리/속도 데이터와 카메라의 객체 인식 정보를 융합하여 충돌 시간(TTC: Time to Collision)을 계산합니다.
- **단계**: 1) 경고(Visual/Audio) -> 2) 부분 제동(Partial Braking) -> 3) 최대 제동(Full Braking)의 순서로 개입하여 사고를 회피하거나 피해를 최소화합니다.

### 3.2 센서 퓨전 (Sensor Fusion)의 필요성
- **논리**: 카메라는 사물의 종류를 잘 알지만 거리에 약하고, 레이다는 거리에 강하지만 사물의 형태 구분에 약합니다. 이 두 데이터를 통합함으로써 안개 낀 날(레이다 강점)이나 급격한 차선 변경(카메라 강점) 상황 모두에 대응하는 강력한 인지 능력을 확보합니다.

### 3.3 주행 보조 시스템의 통합 제어 (HDA: Highway Driving Assist)
- **논리**: ACC와 LKA를 결합하여 고속도로 환경에서 핸들과 페달 조작을 시스템이 주도합니다. 정밀 지도(HD-Map)와 연동하여 곡선 구간이나 톨게이트에서 속도를 미리 조절하는 수준까지 발전했습니다.

## 4. [코드 연결 해설 (Lane Keeping Logic)]
카메라로 차선을 인식하여 핸들 토크를 제어하는 논리 구조입니다.
```python
# 차로 유지 보조(LKA) 및 조향 제어 로직
def lka_steering_control(camera_lane_data):
    # 1. 좌/우 차선 방정식 추출 및 차량의 이격(Offset) 계산
    left_lane, right_lane = camera_lane_data.get_equations()
    vehicle_offset = calculate_center_deviation(left_lane, right_lane)
    
    # 2. 차선 이탈 위험(Lane Departure) 판단
    if abs(vehicle_offset) > DEPARTURE_THRESHOLD:
        # 3. 반대 방향으로의 보정 토크(Corrective Torque) 계산 (PID 제어 등)
        target_steering_angle = pid_controller.compute(vehicle_offset)
        
        # 4. 운전자의 조향 의지(Hand-on detection) 확인 및 개입
        if not driver_is_steering_actively():
            steering_actuator.apply_torque(target_steering_angle)
            trigger_haptic_warning("STEERING_INTERVENTION")
            return "INTERVENING"
            
    return "MONITORING"
```

## 5. [스스로 체크 (Self-Audit)]
1. '센서 퓨전' 과정에서 카메라와 레이다 데이터의 우선순위가 상황(기상, 조도)에 따라 어떻게 바뀌는가?
2. ADAS 시스템이 ISO 26262의 'ASIL-D' 등급을 충족해야 하는 공학적 필연성은?
3. AEB 시스템이 보행자나 자전거 이용자를 인식할 때 카메라 센서가 수행하는 '시맨틱 분할(Semantic Segmentation)'의 역할은?

**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
