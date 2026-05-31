---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 546edd6b2dac09fb0f265c0a45ebd511f916382d2927661459ba815ccf7f46b3
metadata:
  date: '2026-05-16'
  domain: 08_Robotics_Automation
  id: '[[[Robotics] Electric-Vehicle]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Robotics] Electric-Vehicle에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  charging_time_80_percent_min: 18
  regen_soc_threshold: 0.95
  sic_efficiency_gain_range: 5-10%
  standard_voltage_v: 400
  ultra_fast_charger_power_kw: 350
  voltage_architecture_v: 800
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

# [Robotics] Electric-Vehicle

## 1. [왜 배우는가? (Why)]
전기차는 탄소 중립 시대를 선도하는 이동 수단의 표준입니다. 엔진의 폭발 에너지가 아닌 전기의 자기력을 동력으로 삼아 에너지 효율을 비약적으로 높였으며, 부품 수를 1/3 수준으로 줄여 정비의 편리함과 실내 공간의 자유로움을 제공합니다. 또한 움직이는 거대한 배터리(V2G)로서 미래 에너지 망의 핵심 구성 요소가 되어, 전력 수급을 조절하는 지능형 인프라의 역할까지 수행하게 됩니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| System | Core Component | Engineering Rationale |
|:---|:---:|:---|
| **PE System** | Motor / Inverter / Reducer | 전기에너지를 회전력으로 변환 및 제어 |
| **High Voltage** | 800V Architecture | 충전 시간 단축 및 전선 무게/열 손실 저감 |
| **Power Semi.** | SiC (Silicon Carbide) Inverter | 고전압 환경에서의 스위칭 효율 극대화 |
| **Structure** | B2C (Battery-to-Chassis) | 배터리를 차체 구조물로 활용해 강성/밀도 향상 |
| **Efficiency** | Regenerative Braking | 감속 시 운동에너지를 전기로 회수 (에너지 회생) |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 800V 고전압 시스템의 수치적 논리
전압(V)을 높여 전류(I)를 줄이는 것이 핵심입니다.
- **로직**: 동일한 전력($P=V \times I$)을 보낼 때 전압이 2배(400V -> 800V)가 되면 전류는 절반으로 줄어듭니다. 전선에서의 열 손실은 전류의 제곱($I^2R$)에 비례하므로, 열 발생이 1/4로 줄어듭니다.
- **결과**: 전선을 얇게 만들어 무게를 줄일 수 있고, 초급속 충전기(350kW) 사용 시 18분 만에 80% 충전이 가능한 물리적 토대가 됩니다.

### 3.2 PE (Power Electric) 시스템의 통합
모터, 인버터, 감속기를 하나의 하우징에 통합하여 부피와 무게를 줄입니다.
- **인버터**: 배터리의 직류(DC)를 모터 구동을 위한 교류(AC)로 변환합니다. 이때 SiC 전력 반도체를 사용하여 기존 Si(실리콘) 대비 전력 손실을 5~10% 줄여 주행 거리를 늘립니다.

### 3.3 B2C (Battery-to-Chassis) 구조
- **논리**: 배터리 팩을 단순히 싣는 것이 아니라, 차체 바닥의 구조물로 직접 사용합니다. 부품 수가 줄어들어 에너지 밀도(Wh/kg)가 높아지며, 무게 중심이 낮아져 주행 안정성이 향상됩니다.

## 4. [코드 연결 해설 (Regenerative Braking Control)]
운전자가 가속 페달에서 발을 뗐을 때 모터를 발전기로 전환하여 에너지를 회수하는 논리입니다.
```python
# 에너지 회생 제동 및 토크 제어 논리
def calculate_regenerative_torque(pedal_position, battery_soc):
    # 1. 가속 페달이 해제되었는지 확인 (One-pedal Driving)
    if pedal_position == 0:
        # 2. 배터리 상태(SOC) 확인: 꽉 찼으면 에너지를 받을 수 없음
        if battery_soc < 0.95:
            # 3. 속도에 따른 회생 제동 강도 결정
            current_speed = vehicle_speed_sensor.get()
            target_regen_torque = map_speed_to_regen(current_speed)
            
            # 4. 모터를 발전기 모드로 전환 (Negative Torque 발생)
            inverter.set_motor_mode("GENERATOR")
            motor.apply_torque(-target_regen_torque)
            
            # 5. 생성된 전기를 배터리로 충전
            bms.charge_from_regen(motor.generated_power)
            return "REGEN_ACTIVE"
            
    return "COASTING_OR_ACCEL"
```

## 5. [스스로 체크 (Self-Audit)]
1. 전기차에서 전압을 400V에서 800V로 높였을 때 충전 속도 외에 얻을 수 있는 공학적 이점은?
2. SiC(탄화규소) 전력 반도체가 기존 실리콘(Si) 반도체 대비 고전압 EV 인버터에 최적인 이유는?
3. 'B2C(Battery-to-Chassis)' 구조가 사고 시 안전성과 배터리 교체 용이성 측면에서 가지는 과제는?

**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**