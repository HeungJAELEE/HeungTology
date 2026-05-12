---
Basic:
  id: "[[[Strategy] Collaborative-Robots-Cobots-Safety"
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

# [[[Strategy] Collaborative-Robots-Cobots-Safety

## 1. [왜 배우는가? (Why)]]
우리는 지금까지 로봇을 '위험한 괴물'로 보았습니다. 그래서 로봇 주위에는 항상 철조망(펜스)을 쳤고, 사람이 들어가면 로봇은 멈춰야 했습니다. 하지만 협동 로봇 및 협업 안전(Collaborative-Robots-Cobots-Safety)은 펜스를 걷어치우고 로봇과 사람이 짝을 지어 함께 일하는 기술입니다. 로봇이 무거운 짐을 들고 있으면, 사람이 옆에서 정밀하게 조립합니다. 살짝만 닿아도 로봇이 즉시 멈추므로 안전합니다. 이를 이해하는 것은 로봇을 단순한 도구가 아닌 '든든한 동료'로 만들고, 사람의 지능과 로봇의 힘이 시너지를 내는 '조화로운 작업장'을 설계하는 '협업 로봇 전문가'가 되는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Technology / Logic | Engineering Rationale |
|:---|:---:|:---|
| **ISO/TS 15066** | Safety Standard | 협동 로봇이 인간과 접촉했을 때 허용되는 최대 힘과 압력을 규정한 국제 표준 가이드라인 |
| **PFL** | Power & Force Limiting | 로봇 내부의 토크 센서가 미세한 저항을 감지하여, 사람과 닿는 즉시 안전한 수준으로 힘을 줄이거나 정지 |
| **SSM** | Speed & Separation | 센서가 사람과의 거리를 감지하여, 사람이 다가오면 천천히 움직이고 멀어지면 정상 속도로 복귀 |
| **Hand-guiding** | Direct Interaction | 사람이 로봇 팔을 직접 잡고 움직여서 위치를 가르치거나(Teaching) 조작하는 모드 |
| **Cyber-Safety** | Probabilistic Safety | 센서 데이터와 AI를 결합하여 잠재적인 충돌 위험을 실시간 확률로 계산하고 선제 대응 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 접촉 에너지 제어를 통한 부상 방지
- **논리**: 충돌 에너지는 속도의 제곱에 비례합니다. 
- **결과**: ISO/TS 15066에 따라 인체 부위별 통증 한계치를 기준으로 로봇의 운동 에너지와 속도를 실시간 제한함으로써, 불의의 접촉 시에도 타박상 이상의 부상이 발생하지 않도록 물리적으로 보장합니다.

### 3.2 펜스 제거를 통한 공간 효율성 및 유연성
- **논리**: 고정된 펜스는 공장 공간을 많이 차지하고 공정 변경을 어렵게 만듭니다. 
- **효과**: 협동 로봇은 펜스가 필요 없어 공장 면적당 생산성을 30% 이상 높일 수 있으며, 바퀴를 달아 오늘은 이 공정, 내일은 저 공정으로 이동하며 일하는 '이동형 협업'이 가능해집니다.

### 3.3 정밀 토크 센싱과 인공 피부
- **논리**: 관절의 센서만으로는 로봇 팔 중간에 닿는 것을 감지하기 어려울 수 있습니다. 
- **결과**: 로봇 전체를 감싸는 '정전용량형 인공 피부(Smart Skin)' 기술을 도입하여, 로봇의 어떤 부위에라도 사람의 손길이 닿으면 즉시 인지하고 대응하는 '전신 안전 감감'을 구현합니다.

## 4. [코드 연결 해설 (Cobot Collision Detection & Speed Scaling)]
주변 센서 데이터를 수신하여 사람과의 거리에 따라 로봇의 작동 속도를 동적으로 조절하는 논리 구조입니다.
```python
# 로봇 지능(ISM) 기반 협동 로봇 안전 제어 및 속도 최적화 논리
def execute_safe_collaboration(robot_arm, human_sensor_data):
    # 1. 사람과의 거리 측정 (Distance Monitoring)
    # 레이저 스캐너나 AI 카메라를 통해 가장 가까운 사람과의 거리(D) 산출
    distance_to_human = human_sensor_data.get_min_distance()
    
    # 2. 안전 모드 결정 (Safety Mode Selection)
    if distance_to_human < CRITICAL_ZONE:
        # 충돌 직전: 로봇 즉시 정지 (Category 0 Stop)
        robot_arm.emergency_stop()
        status = "HALTED_FOR_SAFETY"
    elif distance_to_human < CAUTION_ZONE:
        # 주의 구간: 속도를 안전한 수준(예: 250mm/s 이하)으로 제한 (SSM 모드)
        speed_factor = (distance_to_human - CRITICAL_ZONE) / (CAUTION_ZONE - CRITICAL_ZONE)
        robot_arm.set_speed_limit(max_speed=MAX_COLLAB_SPEED * speed_factor)
        status = "SPEED_REDUCED"
    else:
        # 안전 구간: 최고 효율 모드로 작동
        robot_arm.set_speed_limit(max_speed=MAX_INDUSTRIAL_SPEED)
        status = "NORMAL_OPERATION"
        
    # 3. 충돌 감지 및 토크 분석 (PFL 모드 감시)
    # 관절 토크 센서가 예상치 못한 외력(Ext-Force) 감지 시 즉시 정지
    if robot_arm.detect_external_collision():
        robot_arm.stop_and_retract() # 살짝 뒤로 물러나며 정지
        status = "COLLISION_DETECTED_STOP"
        
    return {"status": status, "distance": distance_to_human, "current_limit": robot_arm.get_speed_limit()}
```

## 5. [스스로 체크 (Self-Audit)]
1. 'ISO/TS 15066'에서 규정하는 '통증 한계치(Pain Threshold)'가 협동 로봇의 '최대 주행 속도'와 '제동 성능' 설계에 미치는 공학적 영향은?
2. '속도 및 간격 감시(SSM)' 기술이 '산업용 펜스'를 대체함으로써 얻을 수 있는 '공정 유연성'과 '설비 종합 효율(OEE)'의 인과관계는?
3. '협동 로봇' 도입 시 '위험성 평가(Risk Assessment)'를 통해 로봇뿐만 아니라 '그리퍼(End-effector)'와 '작업물'의 날카로움까지 고려해야 하는 이유는?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
