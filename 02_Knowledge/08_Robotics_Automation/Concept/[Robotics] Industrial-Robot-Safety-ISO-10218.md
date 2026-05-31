---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 7d52414c863d917c1305b4dc21ee1ee605bf57f849a2db3be761b3f1f65538e2
metadata:
  date: '2026-05-16'
  domain: 08_Robotics_Automation
  id: '[[[Robotics] Industrial-Robot-Safety-ISO-10218]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Robotics] Industrial-Robot-Safety-ISO-10218에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  performance_level_range: a-e
  stop_zone_meters: 0.5
  warning_zone_meters: 2.0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 08_Robotics_Automation]]'
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

# [Robotics] Industrial-Robot-Safety-ISO-10218

## 1. [왜 배우는가? (Why)]]
공장의 로봇은 강력하고 빠릅니다. 하지만 그 힘이 사람을 향하게 되면 치명적인 사고로 이어집니다. ISO 10218은 로봇이 사람과 같은 공간에서 안전하게 일하기 위해 갖춰야 할 최소한의 '안전 설계'와 '설치 기준'을 정의한 국제 표준입니다. 특히 협동 로봇(Cobot)의 대중화로 로봇과 사람이 펜스 없이 일하는 경우가 많아지면서 이 표준의 중요성은 더욱 커졌습니다. ISO 10218을 이해하는 것은 로봇의 성능을 넘어 '인간의 안전'을 공학적으로 보장하고, 글로벌 규제를 충족하는 안전한 로봇 시스템을 구축하는 법을 배우는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Requirement / Mode | Engineering Rationale |
|:---|:---:|:---|
| **SMS** | Safety Monitored Stop | 사람이 로봇 작업 영역에 들어오면 로봇이 즉각 멈추고, 나가면 다시 가동되는 모드 |
| **Hand Guiding** | Direct Teaching | 사람이 직접 로봇 팔을 잡고 움직여 동작을 학습시킬 때 적용되는 안전 제어 기술 |
| **PFL** | Power and Force Limiting| 충돌 발생 시 로봇이 가하는 힘과 압력을 인체가 견딜 수 있는 수준 이하로 제한하는 기술 |
| **Speed/Sep. Mon.**| Laser Scanner | 사람과의 거리에 따라 로봇의 속도를 단계적으로 줄여 충돌을 사전에 방지하는 모니터링 |
| **Risk Assessment**| PL (Performance Level)| 시스템의 안전 기능이 얼마나 신뢰할 수 있는지(a~e 등급)를 통계적으로 평가하는 지표 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 협업 모드별 리스크 제어 (Safety Modes)
- **논리**: 모든 로봇 작업을 똑같은 수준으로 통제하는 것은 비효율적입니다. 
- **결과**: ISO 10218은 4가지 협업 모드(SMS, Hand Guiding, Speed/Sep. Mon., PFL)를 정의하여, 작업의 성격과 위험도에 따라 최적의 안전 기술을 선택적으로 적용할 수 있게 합니다.

### 3.2 설계부터 설치까지의 통합 안전 (Life-cycle Safety)
- **논리**: 로봇 자체만 안전하다고 시스템 전체가 안전한 것은 아닙니다. 
- **효과**: ISO 10218-1(제조사)과 -2(통합업체)의 구분을 통해, 로봇 본체뿐만 아니라 엔드이펙터(그리퍼), 펜스, 센서 등 시스템 전체의 레이아웃과 작업 시나리오를 종합적으로 검증하여 사각지대 없는 안전을 확보합니다.

## 4. [코드 연결 해설 (Safety Monitoring Logic)]
로봇과 사람 사이의 거리를 측정하여 속도를 제어하는 안전 로직입니다.
```python
# 로봇 지능 기반 ISO 10218 안전 제어 논리
def control_robot_safety(human_distance):
    # 1. 안전 거리(Speed & Separation Monitoring) 기준 설정
    warning_zone = 2.0  # 2미터 이내 접근 시 감속
    stop_zone = 0.5     # 0.5미터 이내 접근 시 정지
    
    if human_distance < stop_zone:
        # 즉각 정지 (Safety Monitored Stop)
        robot.emergency_stop(mode="CATEGORY_0")
        return "IMMEDIATE_STOP_EXECUTED"
    elif human_distance < warning_zone:
        # 속도 제한 (Speed Limiting)
        safe_speed = calculate_safe_speed(human_distance)
        robot.set_velocity(safe_speed)
        return "REDUCED_SPEED_MODE"
    else:
        # 정상 가동
        robot.resume_normal_operation()
        return "NORMAL_OPERATION"
```

## 5. [스스로 체크 (Self-Audit)]
1. ISO 10218에서 정의하는 '협동 로봇(Cobot)'의 4가지 협업 모드는 무엇인가?
2. 로봇의 '성능 수준(PL)' 등급 중 가장 높은 안전성을 의미하는 등급은?
3. 로봇 본체가 안전 인증을 받았더라도 '시스템 통합(Integration)' 후에 다시 위험성 평가를 받아야 하는 이유는?
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**