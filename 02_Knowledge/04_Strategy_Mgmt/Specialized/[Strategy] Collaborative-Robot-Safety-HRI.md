---
metadata:
  date: "2026-05-16"
  id: "[[[Strategy] Collaborative-Robot-Safety-HRI]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "04_Strategy_Mgmt"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "0dc567c71c755a0e5d0aaee721b81c12c364f371261440edfe491873c03997ab"
object:
  object_type: "Concept"
  tier: 1
  description: '[Strategy] Collaborative-Robot-Safety-HRI에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 04_Strategy_Mgmt]]"
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


# [Strategy] Collaborative-Robot-Safety-HRI

## 1. [왜 배우는가? (Why)]]
과거의 산업용 로봇은 사람을 다치게 할 수 있어 쇠창살(Safety Fence) 안에 갇혀 있었습니다. 하지만 이제 로봇은 우리 바로 옆에서 부품을 건네주고 함께 조립을 합니다. 협동 로봇 안전 및 HRI(Collaborative-Robot-Safety-HRI)는 로봇과 사람이 울타리 없이 '공존'하기 위한 기술적/법적 약속입니다. 로봇이 사람의 위치를 귀신같이 알아채고 거리에 맞춰 속도를 줄이거나, 설령 부딪히더라도 아프지 않게 힘을 빼는 기술입니다. 이를 이해하는 것은 로봇을 단순한 기계가 아닌 '안전한 동료'로 변모시켜, 공장의 유연성을 극대화하고 작업자의 안전을 지능적으로 보장하는 '미래형 공장 설계자'가 되는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Feature | Technology / Logic | Engineering Rationale |
|:---|:---:|:---|
| **SSM** | Speed & Separation Monitoring | 센서로 사람과의 거리를 실시간 측정하여 거리가 가까워지면 로봇 속도를 단계적 감축 |
| **PFL** | Power & Force Limiting | 로봇 내부의 토크 센서를 통해 충돌 시 가해지는 힘을 인체 허용치 이하로 제한 |
| **Hand-guiding** | Intuitive Programming | 사람이 직접 로봇 팔을 잡고 움직여 동작을 가르치는 직관적인 인터칭 방식 |
| **Safety Zones** | Dynamic Geofencing | 작업자의 위치와 로봇의 관성을 계산하여 매 순간 변하는 가상의 안전 영역 설정 |
| **Intent Sensing** | AI-based Interaction | 카메라와 AI를 통해 사람의 시선이나 동작을 분석하여 다음 행동을 예측하고 대응 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 속도 및 이격 모니터링 (SSM)의 물리적 제어
- **논리**: 로봇은 갑자기 멈출 수 없습니다. (관성 때문) 
- **결과**: 사람의 진입 속도와 로봇의 정지 거리(Stopping Distance)를 실시간 계산하여, 안전 거리(Separation Distance)가 확보되지 않으면 로봇이 즉시 멈추거나 안전한 방향으로 회피하게 합니다.

### 3.2 동력 및 힘 제한 (PFL)과 생체 역학적 한계
- **논리**: 부딪혔을 때 통증을 느끼는 임계치는 신체 부위마다 다릅니다. 
- **효과**: ISO/TS 15066에서 정의한 신체 부위별 압력/힘 허용 기준치를 로봇 제어 알고리즘에 이식하여, 의도치 않은 충돌 발생 시에도 근로자에게 상해를 입히지 않도록 설계합니다.

### 3.3 차세대 로봇(휴머노이드) 안전 표준 (ISO 25785-1)
- **논리**: 고정된 로봇 팔과 걸어 다니는 로봇의 안전 기준은 달라야 합니다. 
- **결과**: 동적으로 균형을 잡는 휴머노이드 로봇이 넘어지거나 사람과 부딪힐 때의 위험성을 평가하고, 이를 방어하기 위한 소프트웨어적/하드웨어적 안전 기제를 구축합니다.

## 4. [코드 연결 해설 (Adaptive Speed Control for Safety)]
사람과의 거리에 따라 로봇의 이동 속도를 실시간으로 조정하는 논리 구조입니다.
```python
# 협동 로봇 안전(ISM) 기반 적응형 속도 제어 논리
def control_robot_speed_for_safety(human_distance, robot_speed):
    # 1. 안전 거리 임계치 설정 (ISO/TS 15066 기반)
    # 정지 거리 = 로봇 반응 시간 * 속도 + 제동 거리
    stop_distance = calculate_stop_distance(robot_speed)
    safe_buffer = 0.5 # 0.5m 여유 공간
    
    # 2. 실시간 거리 모니터링 및 상태 판단
    if human_distance < stop_distance + safe_buffer:
        # 3. 비상 정지 또는 보호 정지 실행 (Category 0/1/2 Stop)
        if human_distance < stop_distance:
            robot_controller.trigger_emergency_stop()
            return "EMERGENCY_STOP: IMMINENT_DANGER"
        else:
            # 4. 단계적 속도 감축 (Speed Reduction)
            target_speed = robot_speed * (human_distance / (stop_distance + safe_buffer))
            robot_controller.set_speed_limit(target_speed)
            return f"SPEED_REDUCED: TARGET_{target_speed:.2f}"
            
    # 5. 작업자 의도 분석 기반 경로 회피 (Intent-aware Evasion)
    if ai_intent_engine.predict_collision(human_path, robot_path):
        new_path = path_planner.recalculate_evasive_path()
        robot_arm.update_path(new_path)
        return "PATH_DIVERTED: COLLISION_AVOIDED"
        
    return "STATUS_NORMAL"
```

## 5. [스스로 체크 (Self-Audit)]
1. '협동 로봇' 운영 시 '펜스(Fence)'를 없앰으로써 얻는 '공간 효율성'과 '공정 유연성'의 구체적인 공학적 가치는?
2. 'PFL(동력 및 힘 제한)' 방식이 'SSM(속도 및 이격 모니터링)' 방식보다 '협동 강도'가 높은 작업에서 더 유리한 이유는?
3. '휴머노이드 로봇'의 안전을 다루는 'ISO 25785-1' 표준이 기존 '고정형 로봇' 표준인 'ISO 10218'과 차별화되는 '동역학적 고려 사항'은 무엇인가?

**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
