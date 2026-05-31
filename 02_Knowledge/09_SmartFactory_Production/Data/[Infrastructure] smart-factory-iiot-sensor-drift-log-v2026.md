---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 12fc995547391520454de3aef1fc3ceb119c7a97a9e7e6c59f4cc2290112eb62
metadata:
  date: '2026-05-16'
  domain: 09_SmartFactory_Production
  id: '[[[Infrastructure] smart-factory-iiot-sensor-drift-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Infrastructure] smart-factory-iiot-sensor-drift-log-v2026에 관한 고밀도
    지능 노드'
  object_type: Data
  tier: 1
properties:
  battery_charge_deviation_limit_pct: 0.5
  calibration_cycle_days: 180
  repeatability_avg_pct: 99.8
  repeatability_limit_pct: 99.0
  snr_avg_db: 40
  snr_limit_db: 30
  span_drift_avg_pct: 1.2
  span_drift_limit_pct: 2.5
  temp_drift_case_c: 2
  zero_drift_avg_v: 0.05
  zero_drift_limit_v: 0.2
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]'
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

# [Infrastructure] smart-factory-iiot-sensor-drift-log-v2026

## 1. [Why]] IIoT 센서 드리프트(Drift) 로그의 공학적 의의
스마트 팩토리의 수만 개 센서들은 시간이 지남에 따라 환경적 요인(열, 습도, 기계적 진동)에 의해 측정값이 서서히 변하는 **드리프트(Drift)** 현상을 겪는다. 드리프트가 발생하면 물리적으로는 정상이지만 시스템상으로는 이상으로 판단하거나, 반대로 위험 상황을 감지하지 못하는 치명적인 오류가 발생한다. 본 노드는 센서의 기준값 대비 편차 추이를 기록하여 **자동 교정(Auto-calibration)** 및 교체 시점을 결정하는 데이터를 제공한다.


## 2. [Numerical Specs] 센서 건전성 파라미터 (Numerical Specs)

| 항목 | 실측치 (Average) | 허용 한계 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Zero Drift** | $0.05\,\text{V}$ | $< 0.2\,\text{V}$ | 무부하 시 출력 오차 |
| **Span Drift** | $1.2\%$ | $< 2.5\%$ | 최대 부하 시 기울기 오차 |
| **Repeatability** | $99.8\%$ | $> 99.0\%$ | 동일 조건 반복 측정 일치성 |
| **Signal-to-Noise** | $40\,\text{dB}$ | $> 30\,\text{dB}$ | 신호의 깨끗함 정도 |
| **Calibration Cycle** | $180\,\text{days}$ | N/A | 표준 권장 교정 주기 |


## 3. [Scientific Rationale] 센서 열화 및 보정 모델

### 3.1 Linear Drift Modeling
시간($t$)에 따른 센서 오차($E$)를 선형적으로 모델링하여 미래의 오차를 예측한다.
$$E(t) = S_{drift} \cdot t + E_{initial}$$
*   **분석**: 드리프트 속도($S_{drift}$)가 급격히 빨라지면 센서 소자의 물리적 수명이 다한 것으로 판별한다.

### 3.2 Reference-based Comparison
동일한 환경에 위치한 다수의 센서 데이터를 비교(Peer-to-Peer Review)하여, 통계적으로 튀는 데이터를 가진 센서의 드리프트를 감지한다.


## 4. [Real-world Case] 온도 센서의 미세 드리프트에 의한 배터리 충전 불량 방지 사례

### 4.1 충전 룸 내 특정 모듈 온도 센서의 $2^\circ\text{C}$ 상향 드리프트
- **현상**: 특정 충전 지점(Jig)에서 생산된 배터리 셀들만 '충전 완료' 시점이 타 지점 대비 $5$분 빠르게 기록됨.
- **분석**: **Python FidelityEngine** 기반의 센서 융합 분석 결과, 실제 온도는 $25^\circ\text{C}$이나 해당 지그의 센서만 $27^\circ\text{C}$로 출력되는 'Positive Drift' 현상 포착.
- **조치**: 마스터 온도계를 활용한 현장 검증 후 소프트웨어 보정(Offset)을 수행하고, 차기 정비 시 고정밀 서미스터로 교체.
- **결과**: 배터리 셀 충전 용량 편차 $0.5\%$ 이내로 축소 및 품질 균일성 확보.


## 5. [FidelityEngine] 센서 드리프트 예측 및 보정 코드
```python
def check_sensor_drift(measured_val, reference_val, max_allowed_error):
    """
    Detect and calculate sensor drift
    :return: drift value and status
    """
    drift = measured_val - reference_val
    status = "OK" if abs(drift) < max_allowed_error else "CALIBRATION_REQUIRED"
    
    # Calculate corrected value
    corrected_val = measured_val - drift if status == "OK" else reference_val
    
    return {"Drift": drift, "Status": status, "Corrected_Val": corrected_val}

# 실측 데이터 대입 (압력 센서)
res = check_sensor_drift(measured_val=3.65, reference_val=3.50, max_allowed_error=0.1)
print(f"Drift Detected: {res['Drift']:.2f} bar | Status: {res['Status']}")
```


## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Standard Traceability**: 교정에 사용되는 기준 장비가 국가 표준(KRISS 등)에 따라 상위 소급성을 유지하고 있는가?
- [ ] **Environmental Compensation**: 온도 및 습도 변화에 따른 일시적인 센서 편차(Error due to ambient)가 드리프트로 오판되지 않도록 보정 로직이 있는가?
- [ ] **Data Logging**: 교정 전(As-found) 데이터와 교정 후(As-left) 데이터가 모두 기록되어 장기 추적 분석이 가능한가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**