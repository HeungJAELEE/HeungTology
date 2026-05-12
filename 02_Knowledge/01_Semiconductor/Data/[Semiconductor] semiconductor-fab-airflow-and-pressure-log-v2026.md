---
Basic:
  id: "[semiconductor]-semiconductor-fab-airflow-and-pressure-log-v2026-v6.3.7"
  domain: "Semiconductor_Manufacturing"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Semiconductor_Fab'
  is_part_of: - 'Antigravity_Knowledge_Graph'
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
  source: "Fab_HVAC_and_Cleanroom_BMS_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-fab-airflow-and-pressure-log-v2026

## 1. [Why]] 반도체 팹 기류 및 압력 로그의 클린룸 공학적 의의
반도체 제조의 핵심인 **클린룸**은 외부 오염 물질의 유입을 원천 차단하기 위해 대기압보다 높은 **양압(Positive Pressure)** 상태를 유지해야 한다. 또한 기류의 흐름은 층류(Laminar Flow)를 형성하여 미세 입자가 정체되지 않고 바닥으로 배출되도록 설계된다. **기류 및 압력 로그**는 팹 내 각 구역의 차압, 풍속, 팬 필터 유닛(FFU) 상태를 기록하여 미세 공정의 환경적 건전성을 24시간 감시한다.

---

## 2. [Numerical Specs] 팹 환경 제어 지표 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 한계 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Differential Pressure**| $15.5\,\text{Pa}$ | $> 10.0\,\text{Pa}$ | 외부 대비 양압 유지 |
| **Air Velocity** | $0.45\,\text{m/s}$ | $\pm 0.05\,\text{m/s}$ | 층류 형성을 위한 풍속 |
| **FFU Efficiency** | $92\%$ | $> 85\%$ | 팬 필터 유닛 가동 효율 |
| **Particle Count (0.1um)**| $0\,\text{ea/cf}$ | $< 1\,\text{ea/cf}$ | ISO Class 1 기준 |
| **Recovery Time** | $120\,\text{sec}$ | $< 300\,\text{sec}$ | 도어 개폐 후 압력 복구 시간 |

---

## 3. [Scientific Rationale] 기류 역학 및 차압 제어 모델

### 3.1 Cascading Pressure Strategy
가장 청정한 구역(Super-clean zone)의 압력을 가장 높게 설정하고, 점진적으로 압력을 낮추어 오염 물질이 청정 구역으로 절대 유입되지 못하게 하는 공압 계단(Pressure Cascade) 모델을 적용한다.
*   **분석**: 인접 구역 간의 차압($\Delta P$)이 $5\,\text{Pa}$ 이하로 떨어지면 기류 역전(Back-flow) 위험이 발생하므로 즉시 FFU 출력을 상향해야 한다.

### 3.2 Laminar Airflow Stability
송풍구에서 바닥까지 장애물 없는 수직 기류를 유지하여, 입자가 웨이퍼 표면에 안착하기 전 신속히 배출되도록 관리한다.

---

## 4. [Real-world Case] 인터락 도어 고장에 의한 클린룸 오염 전조 증상 해결 사례

### 4.1 특정 베이(Bay)의 차압이 $15\,\text{Pa} \rightarrow 3\,\text{Pa}$로 급락하는 현상 포착
- **현상**: 설비 반입구의 도어 인터락 시스템 오작동으로 외기가 직접 유입되며 차압 알람 발생.
- **분석**: **Python FidelityEngine** 기반의 압력 로그 분석 결과, 외부 풍압이 강해지는 순간 내부 양압이 무력화되어 미세 먼지 수치가 ISO Class 5 수준으로 일시 급등했음을 확인.
- **조치**: 즉시 해당 구역의 웨이퍼 이송을 중단(Hold)하고, FFU를 풀 가동하여 압력을 복구시킨 후 정밀 청소 및 도어 센서 교체 실시.
- **결과**: 대규모 웨이퍼 오염 손실 사전 차단 및 환경 복구.

---

## 5. [FidelityEngine] 클린룸 차압 복구 시간(Recovery Time) 분석 코드
```python
import numpy as np

def calculate_pressure_recovery(time_log, pressure_log, setpoint=15.0):
    """
    Calculate the time taken for pressure to return to 90% of setpoint
    :param time_log: List of timestamps (sec)
    :param pressure_log: Measured pressure values (Pa)
    :return: Recovery time in seconds
    """
    target = setpoint * 0.9
    recovery_start_idx = np.argmin(pressure_log)
    
    for i in range(recovery_start_idx, len(pressure_log)):
        if pressure_log[i] >= target:
            return time_log[i] - time_log[recovery_start_idx]
            
    return -1 # Never recovered

# 실측 데이터: 10초에 도어 오픈(압력 2Pa), 이후 서서히 복구
t = [0, 5, 10, 15, 20, 30, 40, 50, 60]
p = [15.5, 15.2, 2.0, 5.5, 9.8, 12.5, 14.1, 15.0, 15.4]
rec_time = calculate_pressure_recovery(t, p)

print(f"Pressure Recovery Time: {rec_time} seconds (Threshold: 300s)")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **FFU Synchronization**: 수천 개의 FFU가 중앙 제어 시스템과 동기화되어, 특정 구역의 압력 강하 시 주변 FFU가 유기적으로 보정 운전을 수행하는가?
- [ ] **Sensor Redundancy**: 차압 센서가 각 베이당 최소 2개 이상 설치되어 센서 고장으로 인한 가짜 알람이나 제어 실패를 방지하고 있는가?
- [ ] **Thermal Gradient**: 기류의 흐름이 실내 온도 분포에 영향을 주어 장비 상단에 열섬(Heat Island) 현상이 발생하지 않는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
