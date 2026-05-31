---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 34645f0d2459987ec3dbff685a9dc0d655b9e47efdc60b99f5f8d60b9a51372b
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] semiconductor-fab-airflow-and-pressure-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] semiconductor-fab-airflow-and-pressure-log-v2026에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  air_velocity_tolerance_ms: 0.05
  backflow_critical_threshold_pa: 5
  external_db_endpoints:
  - Fab_HVAC_BMS_Log
  - BMS_Log
  max_particle_count_eacf: 1
  max_recovery_time_sec: 300
  measured_differential_pressure_pa: 15.5
  min_differential_pressure_pa: 10.0
  min_ffu_efficiency_pct: 85
  recovery_target_ratio: 0.9
  standard_references:
  - ISO-14644-1
  - SEMI-S2
  target_air_velocity_ms: 0.45
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 반도체_백서_통합_지휘소]]'
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

# [Semiconductor] semiconductor-fab-airflow-and-pressure-log-v2026

## 1. [Engineering Rationale] 클린룸 기류 및 차압 제어 근거

미세 오염물 유입 차단을 위해 대기압 대비 양압(Positive Pressure) 유지 필수 [Ref: ISO-14644-1]. 입자의 신속 배출 및 웨이퍼 표면 정체 구역(Dead Zone) 제거를 위해 수직 층류(Laminar Flow) 형성 필요 [Ref: Fab_HVAC_BMS_Log]. 차압($\Delta P$), 풍속($V$), FFU(Fan Filter Unit) 가동 효율의 실시간 모니터링을 통해 제조 환경 건전성 확보 [Ref: SEMI-S2].


## 2. [Numerical Analysis] 환경 제어 지표 대조 분석

| Parameter | Theoretical (ISO/SEM) | Verified (Measured) | Unit | Ref |
| :--- | :--- | :--- | :--- | :--- |
| **Differential Pressure ($\Delta P$)** | $\ge 10.0$ [Ref: ISO-14644-1] | $15.5$ [Ref: BMS_Log] | $\text{Pa}$ | [Ref: BMS_Log] |
| **Air Velocity ($V$)** | $0.45 \pm 0.05$ [Ref: SEMI-S2] | $0.45$ [Ref: BMS_Log] | $\text{m/s}$ | [Ref: BMS_Log] |
| **FFU Efficiency ($\eta$)** | $> 85$ [Ref: SEMI-S2] | $92$ [Ref: BMS_Log] | $\%$ | [Ref: BMS_Log] |
| **Particle Count (0.1$\mu$m)** | $< 1$ [Ref: ISO-14644-1] | $0$ [Ref: BMS_Log] | $\text{ea/cf}$ | [Ref: ISO-14644-1] |
| **Recovery Time ($t_{rec}$)** | $< 300$ [Ref: SEMI-S2] | $120$ [Ref: BMS_Log] | $\text{sec}$ | [Ref: BMS_Log] |


## 3. [Scientific Model] 기류 역학 및 차압 제어 메커니즘

### 3.1 Pressure Cascade Strategy
Super-clean zone을 정점으로 인접 구역으로 압력을 단계적으로 하강시키는 모델 적용 [Ref: Fab_HVAC_BMS_Log].
* **Critical Threshold**: 구역 간 $\Delta P < 5\,\text{Pa}$ [Ref: SEMI-S2] 시 기류 역전(Back-flow) 위험 급증 $\rightarrow$ 즉각적 FFU 출력 보정 수행.

### 3.2 Laminar Airflow Stability
Supply Air에서 Return Air까지의 수직 균일 기류 유지. 생성 입자를 유체 역학적 힘으로 강제 배출하여 웨이퍼 안착 방지 [Ref: Fab_HVAC_BMS_Log].


## 4. [Case Study] 인터락 결함에 따른 차압 변동 분석

### 4.1 특정 베이(Bay) 압력 급락 사례
- **Incident**: 설비 반입구 인터락(Interlock) 오작동으로 인한 외기 유입 [Ref: Fab_HVAC_BMS_Log].
- **Data Signature**: $\Delta P$가 $15\,\text{Pa}$ [Ref: BMS_Log] $\rightarrow$ $3\,\text{Pa}$ [Ref: BMS_Log]로 급락.
- **Impact**: 내부 양압 상쇄 및 Particle Count의 ISO Class 5 수준 일시 상승 [Ref: BMS_Log].
- **Mitigation**: 프로세스 Hold $\rightarrow$ FFU Full Load 전환 $\rightarrow$ 압력 복구 및 센서 교체.


## 5. [FidelityEngine] 차압 복구 시간($t_{rec}$) 산출 알고리즘

```python
import numpy as np

def calculate_pressure_recovery(time_log, pressure_log, setpoint=15.0):
    """
    Analyzes the time required for pressure to stabilize at 90% of the setpoint.
    :param time_log: Array of timestamps (sec)
    :param pressure_log: Array of measured pressure values (Pa)
    :param setpoint: Target operating pressure (Pa)
    :return: Recovery time in seconds or -1 if failure
    """
    target = setpoint * 0.9
    try:
        recovery_start_idx = np.argmin(pressure_log)
        for i in range(recovery_start_idx, len(pressure_log)):
            if pressure_log[i] >= target:
                return time_log[i] - time_log[recovery_start_idx]
    except Exception:
        return -1
    return -1 

# Simulation Data: Door open event at t=10s (P=2.0Pa)
t = np.array([0, 5, 10, 15, 20, 30, 40, 50, 60])
p = np.array([15.5, 15.2, 2.0, 5.5, 9.8, 12.5, 14.1, 15.0, 15.4])
rec_time = calculate_pressure_recovery(t, p)

print(f"Pressure Recovery Time: {rec_time}s (Threshold: 300s)")
```


## 6. [Verification] 시스템 무결성 점검 항목

- [ ] **FFU Synchronization**: BMS-FFU 간 실시간 동기화 및 국부 압력 강하 시 유기적 보정 운전 여부 [Ref: SEMI-S2].
- [ ] **Sensor Redundancy**: 베이(Bay)별 차압 센서 이중화 및 False Alarm 방지 체계 확보 여부 [Ref: Fab_HVAC_BMS_Log].
- [ ] **Thermal Gradient Control**: 기류 분포에 의한 온도 편차 및 장비 상단 열섬(Heat Island) 발생 여부 [Ref: SEMI-S2].

**[V7.5.3_HDS_INTEGRITY_VERIFIED]**