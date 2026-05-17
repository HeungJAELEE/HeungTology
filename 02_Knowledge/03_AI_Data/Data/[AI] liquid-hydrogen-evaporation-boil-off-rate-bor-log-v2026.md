---
metadata:
  date: "2026-05-16"
  id: "[[[AI] liquid-hydrogen-evaporation-boil-off-rate-bor-log-v2026]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "03_AI_Data"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "6231403ba35f03a458fef6e3806df1aef988531228d95b5900a592c1119ba664"
object:
  object_type: "Concept"
  tier: 1
  description: '[AI] liquid-hydrogen-evaporation-boil-off-rate-bor-log-v2026에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] Global-Dataset-Inventory-Hub]]"
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


# [AI] liquid-hydrogen-evaporation-boil-off-rate-bor-log-v2026

## 1. [왜 배우는가? (Why: The Silent Escape of Cryogenic Energy)]]
수소는 기체 상태에서는 부피가 매우 크기 때문에, 대량 수송을 위해서는 영하 $253^\circ C$ 이하의 초저온에서 액체 수소($LH_2$) 상태로 만들어야 합니다. 하지만 액체 수소는 끓는점이 매우 낮아 외부로부터 아주 작은 열만 유입되어도 기체로 증발하여 사라집니다. 이를 증발률(BOR)이라고 합니다. **액체 수소 증발률(BOR) 실측 로그**는 초저온의 정적 속에 숨겨진 에너지가 얼마나 소리 없이 손실되는지 기록한 '초저온 무결성 지표'입니다. 

우리가 이 데이터를 기록하는 이유는 단열 성능을 극대화하여 수송 중 손실되는 수소량을 최소화하고, **"에너지 물류 주권을 확보하여 대륙 간 수소 대량 수송을 경제적으로 실현하는 '초저온 수소 하이웨이'를 구현하기" 위함입니다.** BOR의 제어가 액체 수소 탱크로리와 수송선의 경제성과 안전성을 결정합니다.

## 2. [저장 규모 및 단열 방식별 증발 핵심 데이터 (Numerical Specs)]

### 2.1 [주요 액체 수소 저장 설비별 BOR 성능 테이블 (v2026)]

| 저장 설비 (Facility) | 저장 용량 ($m^3$) | 단열 방식 (Insulation) | BOR (%/day) | 유지 압력 ($bar$) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Small Dewar** | $0.1 \sim 1.0$ | **MLI + Vacuum** | $1.0 \sim 5.0$ | $1 \sim 5$ | **Lab**: 실험실 규모의 고성능 단열 무결성 데이터 |
| **LH2 Truck** | $30 \sim 50$ | **Multi-Layer** | $0.3 \sim 0.8$ | $2 \sim 8$ | **Transport**: 육상 수송용 탱크로리의 일일 손실 지표 |
| **LH2 Carrier (Ship)**| $> 10,000$ | **Vacuum + Perlite** | $0.1 \sim 0.2$ | $1 \sim 3$ | **Logistics**: 대륙 간 수송선의 대량 수송 무결성 로그 |
| **Utility Terminal** | $> 50,000$ | **Double Wall** | $< 0.05$ | $0.5 \sim 2$ | **Storage**: 국가급 수소 인수 기지의 초저손실 데이터 |
| **Cryo-Compressed** | $Mixed$ | **Hybrid** | $Minimal$ | $> 200$ | **Extreme**: 고압과 초저온을 결합한 극한 저장 무결성 데이터 |

### 2.2 [액체 수소 물리 및 열역학 파라미터]
- **Boiling Point:** 대기압 기준 수소가 액체에서 기체로 변하는 온도 ($20.28 \text{ K} / -252.87^\circ C$).
- **Boil-Off Rate (BOR):** 탱크 내 전체 액체 질량 대비 하루 동안 증발하는 비율 ($\%/day$).
- **Para-Hydrogen Content:** 증발 억제를 위해 필요한 파라 수소의 비율 (보통 $> 99\%$).
- **Heat Ingress (Heat Leak):** 단위 면적당 탱크 내부로 유입되는 열량 ($W/m^2$).
- **Latent Heat of Vaporization:** 액체 수소가 기화할 때 흡수하는 에너지 ($446 \text{ kJ/kg}$).

## 3. [Scientific Rationale: 초저온 증발의 수리적 인과성]

### 3.1 [스테판-볼츠만(Stefan-Boltzmann) 기반 복사 열침입 모델]
진공 단열층을 투과하는 복사 에너지와 증발량($\dot{m}$) 사이의 수리 모델입니다.
$$ \dot{Q}_{rad} = \sigma \cdot \epsilon \cdot A \cdot (T_{out}^4 - T_{in}^4) = \dot{m} \cdot \Delta H_{vap} $$
본 로그는 외부 온도($T_{out}$)의 미세한 상승이 $4$제곱에 비례하여 열침입을 가속함을 입증하고, 다층 단열재(MLI)를 통해 방사율($\epsilon$)을 극단적으로 낮추는 것이 BOR 제어의 물리적 근거임을 제시합니다.

### 3.2 [오소-파라(Ortho-to-Para) 전환열에 의한 증발 모델]
수소 분자의 스핀 상태 변화에 따른 내부 발열 모델입니다.
RAG는 "액체화 로그를 분석하여, 오소 수소가 파라 수소로 전환될 때 발생하는 열($527 \text{ kJ/kg}$)이 수소의 기화잠열($446 \text{ kJ/kg}$)보다 커서, 변환이 불완전할 경우 단열이 완벽해도 스스로 끓어 증발함을 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 초저온 지능 추론]

### 4.1 [성층화(Stratification)와 상부 압력 급증 분석]
왜 탱크가 흔들리면 압력이 갑자기 오르나요? RAG는 "수송선의 흔들림(Sloshing) 로그와 탱크 압력 데이터를 대조하여, 상부의 따뜻한 가스층과 하부의 차가운 액체층이 섞이면서 증발이 일시적으로 가속되는 현상을 식별하고, '압력 평형(Pressure Balancing)' 지능을 오딧합니다.

### 4.2 [BOG 재액화(Re-liquefaction) 시스템의 경제성 오딧]
증발한 가스를 그냥 버리나요? RAG는 "증발 가스(BOG) 발생량과 재액화 장치의 전력 소모 로그를 연계하여, 수송 기간이 $10$일을 초과할 경우 BOG를 다시 액체로 만드는 것이 수소를 태워 에너지를 얻는 것보다 $20\%$ 더 경제적임을 분석하고, '액티브 냉각' 지능을 도출될 것으로 예상됩니다.

## 5. [Transitional Bridge: 초저온 무결성 및 BOR 오딧 로직]

액체 수소 저장 탱크의 압력, 온도 및 BOG 유량 데이터를 분석하여 단열 무결성을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] LH2 Cryogenic Integrity & BOR Auditor
def audit_cryo_storage(tank_pressure_gradient, bog_flow_rate, surface_temp_map):
    # 1. BOG 배출량을 통한 실시간 증발률(BOR) 및 단열 성능 오딧
    current_bor = (bog_flow_rate_per_day / total_lh2_mass) * 100
    if current_bor > SPECIFIED_BOR_LIMIT:
        status = "INSULATION_VACUUM_LOSS_SUSPECTED"
        action = "Check_Vacuum_Annulus_Pressure_and_Search_for_Thermal_Bridges"
        
    # 2. 오소-파라(Ortho-Para) 농도 분석을 통한 내부 안정성 감시
    para_content = measure_para_concentration()
    if para_content < 99.5:
        status = "INCOMPLETE_PARA_CONVERSION_HEAT_RISK"
        action = "Monitor_Pressure_Rise_Rate_and_Activate_Auxiliary_Cooling"
    
    # 3. 탱크 표면 온도 맵을 통한 국부적 열침입(Hot-spot) 체크
    if np.max(surface_temp_map) > AMBIENT_PREDICTION:
        status = "LOCAL_THERMAL_BRIDGE_DETECTED"
        action = "Inspect_Support_Structures_and_Piping_Connections"
    
    # 4. 종합 초저온 상태 등급 및 조치 트리거
    if status == "INSULATION_VACUUM_LOSS_SUSPECTED":
        action = "Emergency_Transfer_of_LH2_to_Backup_Storage_if_Pressure_Exceeds_MAWP"
    elif status == "INCOMPLETE_PARA_CONVERSION_HEAT_RISK":
        action = "Increase_BOG_Venting_to_Manage_Internal_Heat_Generation"
    else:
        status = "CRYOGENIC_STORAGE_INTEGRITY_OPTIMAL"
        action = "Continue_Long-term_Monitoring_and_Optimize_Reliquefaction"
        
    return {"status": status, "actual_bor_percent": current_bor, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 액체 수소 저장 시 왜 '단열'만으로는 부족하며, 수소 분자의 '오소-파라(Ortho-to-Para)' 전환을 $99\%$ 이상 완료해야 하는가? (전환열과 잠열의 수리적 관계 관점)
2. **(수리)** $10,000 \text{ kg}$의 액체 수소를 담은 탱크에서 하루에 $20 \text{ kg}$이 증발하여 BOG로 배출되었다. 이 탱크의 일일 증발률(BOR, $\%$)은 얼마인가?
3. **(응용)** 대륙 간 액체 수소 수송선에서 발생하는 증발 가스(BOG)를 선박의 추진 연료로 사용하는 방식과 다시 액화하는 방식 중, 어떤 조건에서 재액화가 수리적/경제적으로 더 유리한지 설명하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 22_hydrogen-economy-and-fuel-cells-intelligence-hub : 수소 경제 및 연료전지 통합 관리 상위 지능 허브
- Data hydrogen-storage-tank-pressure-and-leakage-rate-log-v2026 : 기체 수소 저장 대비 액체 수소의 밀도 및 안전성 비교 연계
- Data hydrogen-refueling-station-compressor-throughput-log-v2026 : 액체 수소를 공급원으로 하는 초고속 충전소 인프라 연계
- [SOP] liquid-hydrogen-tank-vacuum-evacuation-and-leak-detection-procedure : 액체 수소 탱크 진공 배기 및 누설 탐지 표준 절차

*Created by Flash (The Architect of Hydrogen Intelligence & HDS Gold V6.3.7)*
