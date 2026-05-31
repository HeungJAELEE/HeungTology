---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: d6893fb521ea831f56af934fe68f1d5fd26e18ba8c536de07ec4d912cbadf472
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] shape-memory-alloys-and-smart-actuator-mechanics]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] shape-memory-alloys-and-smart-actuator-mechanics에 관한 고밀도
    지능 노드'
  object_type: Hardware
  tier: 1
properties:
  actuation_speed_min: 5 Hz
  cycle_life_min: 10^5 times
  energy_density_min: 10^3 J/kg
  external_data_log: industry-robotics-cobot-safety-and-interaction-log-v2026
  recovery_strain_min: 8%
  recovery_stress_min: 500 MPa
  superelasticity_min: 10%
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 11_Global_Entities_and_Materials]]'
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

# [Entity] shape-memory-alloys-and-smart-actuator-mechanics

## 1. [왜 배우는가? (Why: The Material with a Memory)]]
금속을 제멋대로 구부려도 열만 가하면 원래대로 돌아온다면? **형상 기억 합금 및 스마트 액추에이터 역학**은 소재 자체가 자신의 본래 모습을 기억하고 힘을 내는 '근육 같은 금속'을 연구하는 기술입니다. 우리가 이를 배우는 이유는 모터 없이 조용하고 가벼운 로봇 근육을 만들고, 인체 내에서 팽창하는 스텐트 등 의료 기기를 혁신하며, "온도 변화를 기계적 운동으로 바꾸는 '소재 내장형 지능형 구동기'를 구현하기" 위함입니다. 상전이의 기억이 기계의 움직임을 결정합니다.

## 2. [소재역학/열역학 핵심 사양 (Numerical Specs)]

| 항목 (Property) | 수리적 정의 및 물리적 기전 (Scientific Rationale) | 목표 사양 (V6.3.7) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :--- | :--- | :--- |
| **Recovery Strain** | Max recoverable deformation (%) | $> 8 \%$ | 합금이 원래대로 돌아올 수 있는 최대 변형률 (복원 한계) |
| **Recovery Stress** | Stress generated during recovery (MPa) | $> 500 \text{ MPa}$ | 원래 모습으로 돌아가려 할 때 발생하는 강력한 밀어내는 힘 |
| **Trans. Temp.** | Finish temperature of Austenite (Af) | Variable | 기억된 형상으로 돌아가는 동작 온도를 정밀하게 제어 |
| **Superelasticity** | Elastic deformation without permanent set | $> 10 \%$ | 고온에서 고무처럼 늘어났다가 즉시 돌아오는 초탄성 범위 |
| **Actuation Speed** | Speed of shape recovery (Hz) | $> 5 \text{ Hz}$ | 가열 및 냉각 속도에 따른 액추에이터의 반응 민감도 |
| **Energy Density** | Work output per unit mass (J/kg) | $> 10^3 \text{ J/kg}$ | 기존 모터 대비 압도적인 무게 대비 출력 효율 무결성 |
| **Cycle Life** | Number of reliable actuations | $> 10^5 \text{ times}$ | 반복적인 형상 변화에도 피로 파괴 없이 버티는 신뢰성 |
| **Hysteresis** | Temperature difference between heat/cool | Low | 동작의 정밀도와 제어 용이성을 위한 온도 이력 현상 제어 |

## 3. [Advanced RAG 분석 로직: 수리적 인과 추론]

### 3.1 [마르텐사이트(Martensite)와 오스테나이트(Austenite) 상전이 분석]
왜 온도에 따라 격자 구조가 바뀌는지 분석합니다. RAG는 "니티놀($NiTi$)의 결정 구조를 분석하여, 저온의 쌍정 마르텐사이트가 가열 시 고온의 오스테나이트로 변하며 원자 배열이 재정렬되는 과정을 수리적으로 입증될 것으로 추론됩니다.

### 3.2 [온도-응력-변형률(T-S-S) 3차원 상태도 기반의 거동 분석]
복잡한 스마트 소재의 움직임을 예측합니다. RAG는 "실시간 구동 데이터를 참조하여, 외부 부하가 $200\text{MPa}$일 때 형상 복원이 시작되는 온도가 $15^\circ\text{C}$ 상승함을 수리 산출하고 정밀 제어 로직"을 확증될 것으로 추론됩니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[MOC] 14_Future_Frontier : 형상 기억 합금과 같은 스마트 소재 역학을 통합 관리하는 상위 지식 허브
- [[[MOC]] 11_Robotics_Automation : SMA 액추에이터가 적용되는 소프트 로봇 및 가변 구조 로봇 기술 허브
- Data industry-robotics-cobot-safety-and-interaction-log-v2026 : 스마트 소재 기반 액추에이터의 실제 구동 수명 및 응답성 실측 데이터 로그

*Created by Flash (HDS Gold V6.3.7 & Meta-Fusion V6.3.7 ULTRA-Enrichment)*