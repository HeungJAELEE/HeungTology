---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: d9dc27d364c42038096c511caa6e0b5af4ff056615aecab1d9f9a5fbd363d3a3
metadata:
  date: '2026-05-16'
  domain: 02_Battery
  id: '[[[Battery] Battery-Lithium-Plating-Detection-Performance-Log_2026-05-16]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Battery] Battery-Lithium-Plating-Detection-Performance-Log_2026-05-16에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  coulombic_efficiency: 95.2%
  critical_c_rate_low_temp: 0.4C
  detection_delay_time: 120 ms
  low_temp_threshold: -10°C
  plateau_inflection_sensitivity: 8.4 mV
  plating_onset_potential: -38 mV
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 02_Battery]]'
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

# [Battery] Battery-Lithium-Plating-Detection-Performance-Log_2026-05-16

## 1. 실측 안전 데이터 요약 (Empirical Summary)
저온($-10\text{ }^\circ\text{C}$) 및 상온 환경에서의 리튬 플레이팅 발생 임계치 및 검출 성능 실측 데이터입니다.

| 측정 지표 | 실측치 (Actual) | 설계 목표 (Target) | 상태 (Status) |
| :--- | :---: | :---: | :---: |
| **플레이팅 개시 전위** | **-38 mV** | $< 0\text{ mV}$ | **Detected** |
| **Plateau 변곡점 감도** | **8.4 mV** | $< 10.0\text{ mV}$ | **Pass** |
| **가역 효율 (C.E)** | **95.2 %** | $\approx 100\%$ | **Degraded** |
| **검출 지연 시간** | **120 ms** | $< 500\text{ ms}$ | **Excellent** |
| **임계 C-rate (-10°C)** | **0.4C** | $> 0.3\text{C}$ | **Qualified** |

## 2. 데이터 기반 추론 (Engineering Reasoning)
🧠 **AI의 사고방식:**
실측된 **-38 mV**의 개시 전위는 저온($-10\text{ }^\circ\text{C}$) 환경에서 음극 표면에 물리적인 금속 리튬 증착이 시작되었음을 의미합니다. 전압 이완 곡선에서 **8.4 mV** 수준의 미세 변곡점(Plateau)을 **120 ms** 이내에 포착해낸 것은 BMS의 고해상도 샘플링과 $dV/dt$ 분석 알고리즘이 플레이팅 초기 징후를 성공적으로 감지하고 있음을 보여줍니다. 가역 효율이 **95.2%**로 떨어진 것은 일부 증착된 리튬이 비가역적인 'Dead Li'로 변했음을 시사하므로, 해당 셀의 수명 가속 노화 관리가 필요합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] Battery-Lithium-Plating-Physics-and-Detection-Standards]]