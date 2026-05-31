---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 49f1ba3f332fb32de0a2ab147fe3862c6cbee0b1fb5d0e8bdca64e1c0b251912
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] CBM-Condition-Based-Maintenance-Logic]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] CBM-Condition-Based-Maintenance-Logic에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  acoustic_emission_frequency_range: 20kHz-100kHz
  astm_standard_acoustic: ASTM E1067
  astm_standard_thermal: ASTM E1934
  critical_health_threshold: 60.0
  failure_detection_lead_time_actual: 0.75 * (P to F)
  ieee_standard_current: IEEE Std 1459
  iso_standard_vibration: ISO 10816
  maintenance_cost_reduction_actual: 25-35%
  rul_accuracy_actual: ±12-18%
  rul_accuracy_ideal: ±2%
  thermal_analysis_weight: 0.3
  vibration_analysis_weight: 0.7
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

# [AI] CBM-Condition-Based-Maintenance-Logic

## 1. Engineering Objective (Operational Context)
CBM(Condition-Based Maintenance)은 실시간 자산 상태 모니터링을 통해 물리적 결함 전조를 식별하고 최적 정비 시점을 결정하는 확률론적 유지보수 전략임. 기존 TBM(Time-Based Maintenance)의 과잉 정비(Over-maintenance) 및 미정비 고장(Under-maintenance) 리스크를 최소화하며, 자산의 가용 수명(Useful Life) 극대화를 목적으로 함.

## 2. Technical Specification & Modality

| Component | Methodology | Engineering Rationale |
|:---|:---:|:---|
| **Vibration Analysis** | FFT / Wavelet Transform | 주파수 도메인 변환을 통한 결함 고유 주파수(Fault Frequency) 추출 [Ref: ISO 10816] |
| **Acoustic Emission** | Ultrasound Detection | 20kHz~100kHz [Ref: ASTM E1067] 고주파 신호 분석을 통한 미세 균열/누설 탐지 |
| **Thermography** | IR Thermal Imaging | 적외선 방사율 분석 기반 접점 과부하 및 절연 파괴 열화 모니터링 [Ref: ASTM E1934] |
| **Current Analysis** | MCSA (Motor Current Signature Analysis) | 전동기 전류 파형의 고조파(Harmonics) 분석을 통한 로터/스테이터 결함 진단 [Ref: IEEE Std 1459] |
| **RUL Estimation** | Regression-based AI / Particle Filter | 상태 지표 기반 퇴화 모델링(Degradation Modeling) 및 잔존 수명 예측 [Ref: PHM Society] |

## 3. Comparative Reliability Analysis

| Parameter | Theoretical Model (Ideal) | Verified Field Data (Actual) | Variance Factor |
|:---|:---:|:---:|:---|
| **Failure Detection Lead Time** | $t_{detection} \to P_{point}$ | $t_{detection} \approx 0.75 \times (P \to F)$ [Ref: Reliability Manual] | Sensor Noise / SNR |
| **RUL Accuracy (Error Rate)** | $\pm 2\%$ [Ref: Pure Stochastic Model] | $\pm 12-18\%$ [Ref: Field Empirical Data] | Environmental Stochasticity |
| **Maintenance Cost Reduction** | $\approx 45\%$ [Ref: Optimization Theory] | $\approx 25-35\%$ [Ref: Industry Case Study] | Implementation/CapEx |

## 4. Reliability Engineering Framework

### 4.1 P-F Curve 기반 징후 포착 (Incipient Failure Detection)
기계적 결함 발생 시 기능적 고장(F) 전 잠재적 결함(P) 단계에서 발생하는 물리적 신호(진동, 온도, 소음) 변화를 포착함. CBM은 $P \to F$ 인터벌을 정량화하여 정비 골든 타임을 산출함.

### 4.2 Just-in-Time Maintenance Logic
자산별 운용 부하(Operating Load) 및 환경 변수를 반영하여 교체 주기를 동적으로 가변함. 이를 통해 부품의 잔존 유효 수명을 극대화하고 자산 회전율을 개선함.

## 5. Algorithmic Diagnostic Logic (High-Density Implementation)

```python
# CBM Real-time Diagnostic Engine
def execute_diagnostic_protocol(vibration_spectrum: list, thermal_gradient: float) -> dict:
    """
    Performs multi-modal sensor fusion for Health Index (HI) calculation.
    """
    # 1. Fault Frequency Peak Detection (FFT Analysis)
    # anomaly_score: 0.0 (Normal) to 1.0 (Critical Failure)
    anomaly_score = fault_detector.analyze_spectral_peaks(vibration_spectrum) 
    
    # 2. Thermal Degradation Slope Calculation
    # temp_slope: K/s (Kelvin per second)
    temp_slope = calculate_derivative(thermal_gradient)
    
    # 3. Composite Health Index (HI) Computation
    # Weighting: Vibration (0.7), Thermal (0.3)
    health_index = 100 - (anomaly_score * 70 + temp_slope * 30)
    
    # 4. Decision Logic based on Critical Thresholds
    if health_index < 60.0:
        return {
            "status": "CRITICAL_FAILURE_IMMINENT",
            "action": "EMERGENCY_SHUTDOWN",
            "RUL_est": "48h"
        }
    elif health_index < 85.0:
        return {
            "status": "DEGRADATION_DETECTED",
            "action": "SCHEDULED_INSPECTION",
            "RUL_est": "168h"
        }
        
    return {"status": "NOMINAL", "HI": health_index}
```

## 6. Technical Audit Checklist
1. **Hybrid Strategy**: TBM의 정기 신뢰성과 CBM의 동적 최적화 결합을 통한 비용-효율 임계점(Cost-Efficiency Threshold) 산출 여부.
2. **FFT Determinism**: 비선형 노이즈(Non-linear Noise) 제거를 위한 Band-pass Filtering 적용 적정성.
3. **Data Robustness**: 데이터 결측치(Missing Value) 및 이상치(Outlier) 발생 시 RUL 예측 모델의 강건성(Robustness) 확보 여부.