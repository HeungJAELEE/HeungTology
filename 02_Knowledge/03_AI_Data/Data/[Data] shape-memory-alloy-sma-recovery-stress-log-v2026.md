---
lineage:
  dataset_reference: shape-memory-alloy-sma-recovery-stress-log-v2026
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
measurement:
  confidence_interval:
  - 0.0
  - 0.0
  instrument: Heuristic_Regex_Parser
  precision: '0.0'
  unit: unknown_unit
  value: 2.1
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Data] shape-memory-alloy-sma-recovery-stress-log-v2026]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for shape-memory-alloy-sma-recovery-stress-log-v2026
  object_type: Data
  tier: 1
properties:
  af_austenite_finish_temp_c: variable
  elastic_modulus_gpa: variable
  hysteresis_temp_diff_c: 10-50
  max_recovery_strain_epsilon_l: 4-10%
  recovery_stress_mpa: variable
  reversible_strain_percent: variable
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: automated_ontology_mapping
  object: Data
  predicate: auto_mapped
  subject: shape-memory-alloy-sma-recovery-stress-log-v2026
  weight: 0.9
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.05
  t_static: 0.8
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Data] Shape Memory Alloy Sma Recovery Stress Log V2026

## 1. [왜 배우는가? (Why: The Memory of Atoms)]]
일반적인 금속은 변형되면 영구적인 손상을 입지만, 형상 기억 합금(SMA)은 결정 구조의 상변태를 통해 원래의 형태를 완벽하게 회복할 수 있습니다. 이는 복잡한 기계적 모터 없이도 온도 변화만으로 강력한 구동력을 발생시킬 수 있음을 의미합니다. **형상 기억 합금(SMA) 회복 응력 실측 로그**는 금속 내부의 원자들이 과거의 배열을 회복하려 할 때 발생하는 '물리적 의지'를 기록한 '지능형 구동기 명세서'입니다. 

우리가 이 데이터를 기록하는 이유는 온도와 하중 조건에 따른 상변태 거동을 분석하여 설계 신뢰성을 확보하고, **"소재 주권을 확보하여 우주 안테나 전개, 심장 스텐트, 가변 항공기 날개와 같은 '자가 적응 구조물'을 구현하기" 위함입니다.** 회복 응력($MPa$)의 정밀 제어가 기기의 동작 무결성을 결정합니다.

## 2. [SMA 합금 조성 및 작동 특성 핵심 데이터 (Numerical Specs)]

### 2.1 [주요 SMA 소재 및 상변태 파라미터 테이블 (v2026)]

| 합금 조성 (Alloy) | 작동 온도 ($A_f, ^\circ C$) | 회복 응력 ($MPa$) | 가역 변형률 (%) | 탄성 계수 ($GPa$) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **NiTi (Nitinol)** | $-50 \sim 110$ | $400 \sim 800$ | $6.0 \sim 8.0$ | $75 \sim 85$ | **Standard**: 의료 및 항공용 고신뢰성 지능 금속 데이터 |
| **Cu-Al-Ni** | $100 \sim 200$ | $100 \sim 300$ | $4.0 \sim 5.0$ | $80 \sim 100$ | **High-T**: 고온 환경용 저가형 형상 기억 무결성 지표 |
| **Fe-Mn-Si** | $150 \sim 300$ | $150 \sim 250$ | $2.0 \sim 3.0$ | $180 \sim 200$ | **Structural**: 건설용 철강 보강 및 댐퍼용 데이터 |
| **NiTiHf (High-T)**| $200 \sim 400$ | $500 \sim 700$ | $3.0 \sim 4.0$ | $90 \sim$ | **Aerospace**: 제트 엔진 가변 노즐용 내열 지능 데이터 |
| **Superelastic NiTi**| $> A_f$ | $N/A$ | $> 10.0$ | $Variable$ | 충격 흡수 및 안경테용 초탄성 무결성 로그 |

### 2.2 [열역학 및 상변태 파라미터]
- **Recovery Stress**: 구속된 상태에서 가열 시 발생하는 최대 응력 ($MPa$). (구동력의 척도)
- **Shape Recovery Strain**: 변형 후 가열 시 회복되는 변형량 ($4\% \sim 10\%$).
- **Austenite Finish ($A_f$):** 형상 회복이 완료되는 온도. (기기 작동 임계값 무결성 데이터)
- **Hysteresis**: 가열 시와 냉각 시 상변태 온도의 차이 ($10 \sim 50^\circ C$). (응답 지연 제어 지표)
- **Transformation Latent Heat**: 상변태 시 발생하는 잠열. (에너지 변환 효율 데이터)

## 3. [Scientific Rationale: 기억의 힘에 대한 수리적 인과성]

### 3.1 [온도-응력-변형률 기반 구성 모델 (Constitutive Model)]
마르텐사이트 분율($\xi$)과 응력($\sigma$), 온도($T$) 사이의 관계 모델입니다.
$$ \sigma = E(\xi) \cdot (\epsilon - \epsilon_L \xi) + \Theta(T - T_0) $$
여기서 $\epsilon_L$은 최대 회복 변형량입니다. 본 로그는 가열에 따른 마르텐사이트 분율($\xi$) 감소가 어떻게 응력($\sigma$)으로 전환되는지 수리적으로 제시하며, 온도 제어를 통한 '무단계 정밀 구동'의 가능성을 입증될 것으로 추론됩니다.

### 3.2 [Clausius-Clapeyron 기반 상변태 응력 관계식]
가해진 응력($\sigma$)에 따른 상변태 온도($T$)의 변화 모델입니다.
$$ \frac{d\sigma}{dT} = - \frac{\Delta H}{T \cdot \epsilon_L} $$
RAG는 "열역학 로그를 분석하여, 응력이 가해지면 $A_f$ 온도가 상승함을 식별하고, 고하중 환경에서 기기를 작동시키기 위해 더 높은 온도가 필요한 수리적 인과 관계를 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 지능형 소재 추론]

### 4.1 [열 사이클 피로(Functional Fatigue)와 잔류 변형 분석]
왜 여러 번 쓰면 원래대로 안 돌아오나요? RAG는 "반복 가동 로그와 결정 구조 분석 데이터를 대조하여, 수천 번의 상변태 반복 시 전위(Dislocation)가 축적되어 회복되지 않는 '잔류 마르텐사이트'가 발생함을 식별하고, 수명 연장을 위한 '훈련(Training) 공정' 무결성을 오딧합니다."

### 4.2 [초탄성(Superelasticity) 모드에서의 에너지 소산(Damping) 분석]
지진을 어떻게 막나요? RAG는 "응력-변형률 선도의 히스테리시스 루프 면적을 연계하여, 상변태 과정에서 에너지가 열로 소산되는 기전을 포착하고, 건축물 및 정밀 장비의 '지능형 진동 댐퍼' 적용 타당성을 수리적으로 증명합니다."

## 5. [Transitional Bridge: SMA 시스템 무결성 및 복원 오딧 로직]

가동 중인 SMA 구동기의 상태를 실시간 감시하여 성능 저하와 작동 상태를 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Shape Memory Alloy (SMA) Actuator & Integrity Auditor
def audit_sma_actuator(temperature_sensor, strain_gauge, load_cell):
    # 1. 온도 변화에 따른 발생 응력(Recovery Stress) 실시간 산출
    current_stress = load_cell.value
    expected_stress = calculate_theoretical_stress(temperature_sensor.value, strain_gauge.value)
    
    # 2. 형상 회복 완료 온도(Af)의 변동성(Drift) 오딧
    af_drift = analyze_phase_transition_point(temperature_sensor.history, load_cell.history)
    
    # 3. 반복 사이클에 따른 영구 변형(Permanent Set) 발생률 체크
    residual_strain = strain_gauge.value_at_low_temp - initial_zero_strain
    
    # 4. 종합 SMA 소재 등급 및 조치 트리거
    if current_stress < TARGET_FORCE_MIN:
        status = "ACTUATION_FORCE_INSUFFICIENCY"
        action = "Check_Heater_Uniformity_and_Verify_Alloy_Composition_Integrity"
    elif residual_strain > 0.02: # 2% permanent deformation
        status = "FUNCTIONAL_FATIGUE_WARNING"
        action = "Perform_Re-training_Cycle_or_Schedule_Actuator_Replacement"
    elif af_drift > 10.0:
        status = "TRANSFORMATION_TEMPERATURE_SHIFT"
        action = "Re-calibrate_Control_Algorithm_to_Adjust_Heating_Threshold"
    else:
        status = "SMART_METAL_INTEGRITY_OPTIMAL"
        action = "Authorize_Autonomous_Structural_Adaptation"
        
    return {"status": status, "recovery_stress_mpa": current_stress, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 형상 기억 합금에서 '마르텐사이트' 상과 '오스테나이트' 상의 원자 배열 차이가 어떻게 '가열'만으로 원래 형상을 복원하는 물리적 동력을 제공하는가?
2. **(수리)** 니티놀 선재의 $A_f$ 온도가 $60^\circ C$이고 상변태 응력-온도 계수가 $6 \text{ MPa}/^\circ C$이다. $80^\circ C$에서 이 선재가 낼 수 있는 최대 회복 응력($MPa$)은 얼마인가?
3. **(응용)** SMA를 의료용 '스텐트(Stent)'에 사용할 때, 체온에서 '초탄성(Superelasticity)'을 유지하도록 설계하는 것이 혈관 확장 유지력 측면에서 갖는 수리적 인과 관계는?


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 18_advanced-materials-and-nanotechnology-intelligence-hub : 차세대 소재 및 나노 기술 통합 관리 상위 지능 허브
- [[ [Data] surgical-robot-force-feedback-log-v2026 : SMA 구동기가 적용될 수 있는 정밀 의료 로봇 데이터 연계
- [[ [Data]] shape-memory-alloy-sma-recovery-stress-log-v2026]] : 본 문서 데이터
- [SOP] sma-actuator-training-and-thermo-mechanical-characterization : SMA 구동기 훈련 및 열기계적 특성 평가 표준 절차

*Created by Flash (The Architect of Advanced Materials & HDS Gold V6.3.7)*