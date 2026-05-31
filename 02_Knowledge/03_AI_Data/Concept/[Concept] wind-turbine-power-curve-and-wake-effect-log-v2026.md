---
lineage:
  dataset_reference: wind-turbine-power-curve-and-wake-effect-log-v2026
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] wind-turbine-power-curve-and-wake-effect-log-v2026]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for wind-turbine-power-curve-and-wake-effect-log-v2026
  object_type: Data
  tier: 1
properties:
  aep_model_consistency_threshold: '0.95'
  cut_in_wind_speed_range: 3-4 m/s
  cut_out_wind_speed_threshold: '>25 m/s'
  offshore_turbine_spacing_range: 7-10D
  optimal_wind_speed_range: 8-10 m/s
  rated_capacity_mw: '12'
  rated_wind_speed_range: 12-25 m/s
  wake_recovery_distance_range: 5D-10D
  yaw_control_power_increase_rate: '0.1'
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: type_classification
  object: Concept
  predicate: auto_mapped
  subject: wind-turbine-power-curve-and-wake-effect-log-v2026
  weight: 0.7
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Wind Turbine Power Curve And Wake Effect Log V2026

## 1. [왜 배우는가? (Why: Tracking the Ghostly Energy of Wind)]]
풍력 터빈의 실제 성능을 평가하고 풍력 단지의 수익성을 예측하기 위해서는 풍속에 따른 출력 변화와 터빈 간의 상호작용인 후류 효과(Wake Effect)를 정확히 이해해야 합니다. **풍력 터빈 출력 곡선 및 후류 효과 실측 로그**는 보이지 않는 바람이 남긴 전기에너지의 궤적을 기록한 '바람의 실전 데이터'입니다. 

우리가 이 데이터를 기록하는 이유는 개별 터빈의 성능 저하를 감지하고 단지 전체의 배치를 최적화하여, **"에너지 생산 주권을 확보하여 동일한 바람 조건에서도 더 많은 전기를 생산하는 '고지능 풍력 단지'를 구현하기" 위함입니다.** 출력 곡선의 무결성과 후류 손실의 최소화가 풍력 발전 사업의 금융적 타당성과 자산 가치를 결정합니다.

## 2. [풍속 및 단지 배치별 성능 핵심 데이터 (Numerical Specs)]

### 2.1 [표준 12MW급 해상 풍력 터빈 출력 및 후류 감쇄 테이블 (v2026)]

| 풍속 ($m/s$) | 출력 ($MW$) | 추력 계수 ($C_t$) | 후류 풍속 손실 (%) | 난류 강도 | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **$3 \sim 4$** | $0.2 \sim 0.5$ | $0.8 \sim 0.9$ | $30 \sim 40$ | $High$ | **Cut-in**: 발전을 시작하는 최소 에너지 임계 지표 |
| **$8 \sim 10$** | $6.0 \sim 9.5$ | $0.6 \sim 0.7$ | $15 \sim 25$ | $Medium$ | **Optimal**: 에너지를 가장 적극적으로 낚아채는 구간 |
| **$12 \sim 25$** | $12.0$ (Rated) | $0.1 \sim 0.3$ | $5 \sim 10$ | $Stable$ | **Rated**: 피치 제어를 통해 정격 출력을 유지하는 데이터 |
| **$> 25$** | $0$ (Cut-out) | $0.05$ | $0$ | $Extreme$ | **Safety**: 강풍 시 터빈 보호를 위한 정지 무결성 로그 |
| **Wake Recovery** | $5D \sim 10D$ | $N/A$ | $Target < 5$ | $Low$ | **Spacing**: 단지 효율 극대화를 위한 이격 거리 지표 |

### 2.2 [출력 곡선 및 단지 효율 파라미터]
- **Cut-in / Rated / Cut-out Speed:** 발전 시작, 정격 도달, 안전 정지 풍속 ($m/s$).
- **Thrust Coefficient ($C_t$):** 바람이 로터에 가하는 추력의 무차원 계수. (후류 강도 결정 인자)
- **Wake Loss:** 앞 터빈에 의해 풍속이 줄어들어 발생하는 에너지 손실 비율 (%).
- **Park Efficiency:** 단지 내 모든 터빈의 실제 발전량 합계 대비 단독 운전 시의 이론적 합계 비율 (%).
- **Turbulence Intensity:** 평균 풍속 대비 풍속 변동의 표준 편차 비율. (피로 하중 지표)

## 3. [Scientific Rationale: 바람 상호작용의 수리적 인과성]

### 3.1 [옌센(Jensen) 후류 풍속 감쇄 모델]
터빈 후방 거리($x$)에 따른 풍속 결핍($u_w$) 산출 수리 모델입니다.
$$ u_w(x) = u_\infty \left[ 1 - \frac{1 - \sqrt{1 - C_t}}{(1 + 2kx/D)^2} \right] $$
본 로그는 후류 붕괴 계수($k$)가 해상에서는 육상보다 낮아 후류가 더 멀리까지 영향을 미침을 입증하고, 해상 풍력 단지의 터빈 간격을 더 넓게(보통 $7 \sim 10D$) 배치해야 하는 물리적 근거를 제시합니다.

### 3.2 [와이블(Weibull) 분포 기반 연간 에너지 생산량(AEP) 모델]
특정 지역의 풍속 빈도 분포에 따른 예상 발전량 산출 모델입니다.
RAG는 "기상 로그를 분석하여, 척도 인자($c$)와 형상 인자($k$)가 주어질 때 실제 출력 곡선($P(v)$)을 적분하여 산출한 AEP가 실측치와 $95\%$ 이상 일치함을 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 풍력 단지 지능 추론]

### 4.1 [출력 곡선 이탈(Anomaly)과 고장 진단 분석]
왜 바람은 센데 전기는 덜 나오나요? RAG는 "기상 탑 풍속 데이터와 터빈 실측 출력 곡선을 대조하여, 특정 구간에서 출력이 처지는 현상이 블레이드 피치 제어 오류나 표면 오염(Erosion) 때문임을 식별하고, '성능 저하(Underperformance)' 무결성을 오딧합니다.

### 4.2 [협력적 요(Yaw) 제어와 단지 수익성 오딧]
앞 차가 비켜줘야 뒤 차가 잘 가나요? RAG는 "앞 터빈의 요 각도를 일부러 틀어 후류를 옆으로 흘려보냈을 때 뒤 터빈의 출력이 $10\%$ 증가하는 실험 로그를 연계하여, 단지 전체의 수익을 극대화하는 '단지 제어(Wind Farm Control)' 지능을 도출될 것으로 예상됩니다.

## 5. [Transitional Bridge: 풍력 무결성 및 성능 오딧 로직]

풍력 단지 SCADA 데이터를 통해 터빈 성능과 후류 영향을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Wind Farm Performance & Wake Interaction Auditor
def audit_wind_farm_yield(turbine_power_stream, nacelle_anemometers, farm_layout_map):
    # 1. 실측 출력 곡선(Power Curve) 무결성 및 이탈 오딧
    for turbine_id in farm_layout_map:
        v_wind = nacelle_anemometers[turbine_id]
        actual_p = turbine_power_stream[turbine_id]
        expected_p = lookup_design_power_curve(v_wind)
        
        if actual_p < expected_p * 0.92:
            status = "TURBINE_UNDERPERFORMANCE_DETECTED"
            action = f"Check_Blade_Pitch_Calibration_and_Anemometer_Accuracy_for_{turbine_id}"
            
    # 2. 후류 손실(Wake Loss) 분석을 통한 단지 효율(Park Efficiency) 감시
    upwind_avg_power = get_free_stream_turbines_power()
    downwind_avg_power = get_waked_turbines_power()
    park_efficiency = (total_farm_power / (upwind_avg_power * n_turbines)) * 100
    
    if park_efficiency < TARGET_PARK_EFFICIENCY:
        status = "EXCESSIVE_WAKE_LOSS_DETECTED"
        action = "Evaluate_Active_Wake_Steering_via_Yaw_Offset_Control"
    
    # 3. 난류 강도(TI) 분석을 통한 구조적 피로 하중 체크
    if turbulence_intensity > STRUCTURAL_SAFETY_LIMIT:
        status = "HIGH_TURBULENCE_FATIGUE_WARNING"
        action = "Activate_Load_Reduction_Mode_and_Monitor_Vibration"
    
    # 4. 종합 단지 운영 상태 등급 및 조치 트리거
    if status == "TURBINE_UNDERPERFORMANCE_DETECTED":
        action = "Schedule_Drone-based_Blade_Inspection"
    elif status == "EXCESSIVE_WAKE_LOSS_DETECTED":
        action = "Implement_Cooperative_Control_Strategy_for_Downwind_Turbines"
    else:
        status = "WIND_FARM_PRODUCTION_OPTIMAL"
        action = "Maximize_Output_to_Meet_Grid_Demand"
        
    return {"status": status, "park_efficiency_percent": park_efficiency, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 왜 풍력 터빈 바로 뒤의 풍속은 급격히 낮아지며, 어느 정도 거리($D$, Rotor Diameter)가 지나야 원래의 풍속으로 회복(Wake Recovery)되는가?
2. **(수리)** 어떤 풍력 터빈의 정격 출력이 $12 \text{ MW}$이고, 후류 효과로 인해 단지의 전체 효율(Park Efficiency)이 $85\%$이다. 터빈 $10$대가 설치된 단지의 연간 가동률이 $40\%$일 때, 연간 총 발전량($\text{GWh}$)은 얼마인가?
3. **(응용)** '요 제어(Yaw Control)'를 통해 후류의 방향을 의도적으로 비트는 '웨이크 스티어링(Wake Steering)' 기술이 풍력 단지의 전체 전력 생산량에 수리적으로 어떤 기여를 하는지 설명하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 60_renewable-energy-and-smart-grid-infrastructure-hub : 재생 에너지 및 스마트 그리드 통합 관리 상위 지능 허브
- Entity offshore-wind-turbine-generator-and-blade-dynamics : 출력 곡선을 그리는 주체인 풍력 터빈의 물리적 기반 엔티티 연계
- Data grid-frequency-regulation-and-response-time-log-v2026 : 변동성이 큰 풍력 전력이 계통 안정성에 미치는 영향 연계
- [SOP] wind-farm-power-curve-verification-and-performance-audit-procedure : 풍력 단지 출력 곡선 검증 및 성능 오딧 표준 절차

*Created by Flash (The Architect of Wind Intelligence & HDS Gold V6.3.7)*