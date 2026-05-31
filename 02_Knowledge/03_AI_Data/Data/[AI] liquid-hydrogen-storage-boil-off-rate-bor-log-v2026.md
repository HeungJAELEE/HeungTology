---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 4c8a6efe5f305a98bb079bf592e35e7eb61c134403f733adc599bd890b131536
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] liquid-hydrogen-storage-boil-off-rate-bor-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] liquid-hydrogen-storage-boil-off-rate-bor-log-v2026에 관한 고밀도 지능
    노드'
  object_type: Concept
  tier: 1
properties:
  bor_advanced_reliquefac_percent_per_day_max: 0.01
  bor_large_spherical_percent_per_day_range: 0.05-0.1
  bor_small_iso_tank_percent_per_day_range: 0.5-1.0
  bor_space_rocket_percent_per_day_range: 2.0-5.0
  critical_pressure_threshold_bar: 6
  latent_heat_of_vaporization_kj_kg: 446
  ortho_to_para_conversion_heat_kj_kg: 527
  para_conversion_target_percent: 99.9
  reliquefaction_energy_efficiency_threshold_percent: 15
  storage_temperature_celsius: -253
  storage_temperature_kelvin: 20
  tank_design_pressure_range_bar: 1-10
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
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

# [AI] liquid-hydrogen-storage-boil-off-rate-bor-log-v2026

## 1. [왜 배우는가? (Why: The Battle against Thermal Ingress)]]
수소를 기체가 아닌 액체로 저장하는 이유는 부피당 에너지 밀도를 $800$배 이상 높여 장거리 운송을 가능하게 하기 위함입니다. 하지만 액체 수소는 영하 $253^\circ C$라는 극한의 저온 상태로 유지되어야 하며, 외부의 아주 작은 열 유입도 수소를 기체로 증발시켜 막대한 경제적 손실과 안전 리스크를 유발합니다. **액체 수소 저장 증발률(BOR) 실측 로그**는 보이지 않는 열의 침투를 얼마나 완벽히 막아내고 있는지를 기록한 '저온 저장의 무결성 성적표'입니다. 

우리가 이 데이터를 기록하는 이유는 단열 성능과 증발 가스(BOG) 재액화 효율을 분석하여 수소 물류의 경제성을 확보하고, **"수소 저장 주권을 확보하여 글로벌 수소 허브를 지탱하는 완벽한 혹한의 저장 지능을 구현하기" 위함입니다.** 증발률 0.1%의 차이가 수소 경제의 수익성을 결정합니다.

## 2. [액체 수소 저장 탱크 및 단열 핵심 데이터 (Numerical Specs)]

### 2.1 [탱크 크기 및 단열 방식별 증발 성능 테이블 (v2026)]

| 저장 규모 (Scale) | 단열 방식 (Insulation) | 증발률 (BOR, %/day) | 진공도 ($Torr$) | 유지 시간 ($Days$) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Small (ISO Tank)** | MLI + Vacuum | $0.5 \sim 1.0$ | $10^{-6}$ | $30 \sim 60$ | **Standard**: 트럭/컨테이너 운송용 표준 무결성 데이터 |
| **Large (Spherical)**| Perlite + Vacuum | $0.05 \sim 0.1$ | $10^{-3}$ | $> 365$ | 대규모 인수 기지용 초저증발 무결성 지표 |
| **Space (Rocket)** | Foam + MLI | $2.0 \sim 5.0$ | $Atm.$ | $< 1$ | **Extreme**: 발사체용 고밀도/단기 저장 데이터 |
| **With Reliquefac.** | Active Cooling | $< 0.01$ | $Variable$ | $Infinite$ | **Advanced**: 증발 가스 재액화를 통한 제로-BOR 무결성 |
| **Para-Conversion** | Catalyst Bed | $N/A$ | $N/A$ | $N/A$ | 자가 기화 방지를 위한 99.9% 파라 변환 무결성 데이터 |

### 2.2 [저온 저장 및 열역학 파라미터]
- **Storage Temperature**: $-253^\circ C$ ($20 \text{ K}$ at $1 \text{ atm}$). (수소가 액체로 존재하기 위한 극한의 조건)
- **Latent Heat of Vaporization**: $446 \text{ kJ/kg}$. (기화 시 주변에서 뺏어가는 열에너지 무결성 데이터)
- **Ortho-to-Para Heat**: $527 \text{ kJ/kg}$ (conversion energy). (상변화보다 큰 자가 기화 에너지 지표)
- **Heat Leak (Q):** $\text{Watts (W)}$. (단열재를 뚫고 들어오는 물리적 열량 무결성)
- **Tank Design Pressure**: $1 \sim 10 \text{ bar}$. (증발 가스에 의한 압력 상승을 견디는 설계 강도 데이터)

## 3. [Scientific Rationale: 저온 물리학의 수리적 인과성]

### 3.1 [단열재 열전달 및 증발량($\dot{m}$) 산출 모델]
복사, 전도, 대류를 포함한 총 유입 열량($Q$)에 따른 증발량 모델입니다.
$$ \dot{m} = \frac{Q_{total}}{h_{fg}} = \frac{Q_{rad} + Q_{cond} + Q_{conv}}{h_{fg}} $$
본 로그는 특히 진공 공간에서의 복사($Q_{rad} \propto T^4$)가 지배적임을 입증하고, MLI(다층 단열재)의 층수($N$)가 복사 열전달을 $1/N$로 줄이는 수리적 근거를 제시합니다.

### 3.2 [오르토-파라(Ortho-Para) 변환에 의한 자가 기화 모델]
상온의 오르토 수소($75\%$)가 액체 상태에서 파라 수소($100\%$)로 변하며 내뱉는 열에 의한 모델입니다.
RAG는 "저장 로그를 분석하여, 파라 변환이 $99.9\%$ 미만일 경우 잠열($446 \text{ kJ/kg}$)보다 큰 변환열($527 \text{ kJ/kg}$)이 발생하여 단열과 무관하게 폭발적으로 기화함을 식별하고, 자성 촉매를 이용한 사전 변환의 절대적 무결성을 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 수소 물류 지능 추론]

### 4.1 [탱크 내 온도 성층화(Stratification) 및 압력 급상승 분석]
왜 섞지 않으면 압력이 오르나요? RAG는 "탱크 수직 온도 분포 로그를 분석하여, 상부 가스층과 하부 액체층 사이의 온도차로 인해 상부 압력이 임계치($6 \text{ bar}$)를 초과함을 확인하고, 내부 순환 펌프(Spray)를 가동하여 성층화를 파괴하는 제어 전략을 오딧합니다."

### 4.2 [증발 가스(BOG) 재액화 시스템의 에너지 효율(COP) 오딧]
버려지는 수소를 어떻게 살리나요? RAG는 "BOG 회수 로그와 냉동기 소비 전력 데이터를 대조하여, 증발된 수소를 다시 액화하는 데 드는 에너지가 수소 에너지 함량의 $15\%$를 초과할 경우 재액화 대신 연료전지 발전용으로 전환하는 '지능형 BOG 하이브리드 운영'을 수리적으로 증명합니다."

## 5. [Transitional Bridge: 액체 수소 저장 무결성 및 BOR 오딧 로직]

저장 탱크의 압력과 온도 변화를 실시간 감시하여 수소 손실을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] LH2 Storage Integrity & Boil-off Rate Auditor
def audit_cryogenic_storage(tank_pressure, temp_profile, vacuum_sensor):
    # 1. 압력 상승률(dP/dt)을 통한 실시간 증발률(BOR) 추정
    current_bor = calculate_realtime_bor(tank_pressure.trend)
    
    # 2. 진공도 파괴(Vacuum Loss)에 의한 단열 성능 저하 감지
    insulation_health = analyze_vacuum_stability(vacuum_sensor.reading)
    
    # 3. 오르토-파라 변환 상태 및 자가 기화 리스크 평가
    para_ratio = read_ortho_para_sensor()
    conversion_risk = calculate_self_heating(para_ratio)
    
    # 4. 종합 저장 등급 및 시스템 트리거
    if current_bor > SPEC_LIMIT_BOR:
        status = "EXCESSIVE_BOIL-OFF_DETECTED"
        action = "Check_Vacuum_Seal_and_Activate_BOG_Reliquefier"
    elif insulation_health == "VACUUM_DEGRADED":
        status = "INSULATION_FAILURE_DANGER"
        action = "Immediate_Transfer_to_Buffer_Tank_and_Maintenance"
    elif conversion_risk > THERMAL_LIMIT:
        status = "PARA_CONVERSION_INCOMPLETE"
        action = "Increase_Cooling_Power_and_Log_Batch_Quality"
    else:
        status = "CRYOGENIC_STORAGE_OPTIMAL"
        action = "Maintain_Monitoring_and_Proceed_to_Shipment"
        
    return {"status": status, "bor_%/day": current_bor, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 액체 수소 저장에서 '다층 단열재(MLI)'가 진공 챔버 안에서 수많은 알루미늄 막을 겹쳐 사용하는 것이 '복사(Radiation) 열전달'을 차단하는 데 어떤 물리적 인과 관계를 갖는가?
2. **(수리)** 기화 잠열이 $446 \text{ kJ/kg}$인 액체 수소 탱크에 외부에서 $10 \text{ W}$의 열이 지속적으로 유입된다면, 하루($24$시간) 동안 증발하는 수소의 양($kg$)은 약 얼마인가?
3. **(응용)** 수소를 액화하기 전 반드시 '오르토(Ortho)'에서 '파라(Para)'로 변환시켜야 하는 이유를 '에너지 평형'과 '장기 저장의 경제성' 관점에서 수리적으로 설명하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 15_next-gen-energy-and-hydrogen-intelligence-hub : 차세대 에너지 및 수소 통합 관리 상위 지능 허브
- Data pem-electrolyzer-hydrogen-production-rate-log-v2026 : 수소를 생산하는 상위 시스템 데이터 로그 연계
- Data hydrogen-fuel-cell-stack-voltage-efficiency-log-v2026 : 저장된 수소를 사용하는 연료전지 시스템 데이터 로그 연계
- [SOP] liquid-hydrogen-tank-filling-and-vacuum-maintenance : 액체 수소 탱크 충전 및 진공 유지 관리 표준 절차

*Created by Flash (The Architect of Next-gen Energy & HDS Gold V6.3.7)*