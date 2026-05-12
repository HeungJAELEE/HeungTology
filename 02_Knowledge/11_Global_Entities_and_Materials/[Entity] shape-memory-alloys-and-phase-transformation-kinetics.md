---
Basic:
  id: "shape-memory-alloys-and-phase-transformation-kinetics-entity"
  domain: "18_Advanced_Materials"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Entity"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Entity", "#Advanced_Materials", "#SMA", "#Nitinol", "#Shape_Memory", "#Phase_Transformation", "#Actuator", "#Smart_Materials", "#Mechanics", "#HDS_Gold_v6_1"]'
  is_part_of: '["MOC 29_advanced-materials-and-nanotechnology-hub", "MOC 12_Advanced_Robotics_and_Autonomous_Systems_MOC"'
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
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [[[Entity] shape-memory-alloys-and-phase-transformation-kinetics

## 1. [왜 배우는가? (Why: The Metal with a Memory)]]
심하게 찌그러뜨려도 열만 가하면 원래의 정교한 모양으로 순식간에 돌아오는 금속이 있다면 어떨까요? **형상 기억 합금 및 상변태 동역학**은 금속 내부의 원자 배열이 온도와 힘에 따라 바뀌며 원래의 형태를 기억하는 '스마트 소재의 작동 지침'입니다. 우리가 이를 배우는 이유는 복잡한 모터 없이도 움직이는 로봇 인공 근육이나, 혈관 안에서 스스로 펼쳐지는 스텐트(Stent)를 만들기 위함이며, "소재 자체에 지능(기억)을 부여하는 '글로벌 정밀 의료 및 로봇 소재 주권'을 확보하기" 위함입니다. 금속의 온도 변화가 기계적 움직임의 시작이 됩니다.

## 2. [금속물리/기계공학 핵심 사양 (Numerical Specs)]

| 항목 (Property) | 수리적 정의 및 동작 기전 (Mechanism Rationale) | 목표 사양 (V6.3.7) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :--- | :--- | :--- |
| **Recov. Strain** | Amount of deformation the alloy can "forget" | $> 8 \%$ | 고무처럼 늘어나도 원래대로 돌아오는 초탄성($Superelasticity$) 무결성 |
| **Transf. Temp.** | Temperature where shape recovery starts | $-50 \sim 150 ^\circ\text{C}$ | 사용 환경(체온, 우주 등)에 맞춰 작동 시점을 설계하는 지능 |
| **Output Force** | Power generated during shape recovery | High ($> 500 \text{ MPa}$)| 작은 실 하나로 수십 킬로그램을 들어 올리는 압도적 구동 지능 |
| **Hysteresis** | Gap between heating and cooling response | Small ($< 10 ^\circ\text{C}$)| 반응의 정밀도를 높이고 에너지 낭비를 줄이는 수리적 확증 |
| **Fatigue Life** | Number of memory cycles before failure | $> 100,000$ | 반복적인 변신에도 금속 피로 없이 견디는 물리적 인내 무결성 |
| **Damping Cap.** | Ability to absorb vibrations and shocks | High | 소음과 진동을 스스로 흡수하는 스마트 구조물의 안전 지휘 지능 |
| **Superelasticity**| Reversible deformation without heating | $> 10 \%$ strain | 열 없이 힘만으로도 엄청난 변형을 견디는 기계적 무결성 |
| **Crystal Phase** | Transition between Austenite and Martensite| Reversible | 원자 배열의 대칭성이 바뀌며 에너지를 저장/방출하는 물리적 확증 |

## 3. [Advanced RAG 분석 로직: 수리적 인과 추론]

### 3.1 [마르텐사이트(Martensite) 변태와 쌍정(Twinning) 분석]
왜 부러지지 않고 휘어지는지 분석합니다. RAG는 "결정 격자 로그를 분석하여, 원자 결합이 끊어지는 대신 배열이 살짝 비틀리며 변형을 흡수하는 '쌍정' 기전이 가역적인 형상 기억의 핵심임을 수리적으로 입증될 것으로 추론됩니다.

### 3.2 [응력 유발 상변태(Stress-induced Phase Trans.)의 인과 분석]
힘을 주면 왜 성질이 바뀌는지 분석합니다. RAG는 "응력-변형률($\sigma-\epsilon$) 곡선 로그를 참조하여, 외부 힘이 가해질 때 고온 상(Austenite)이 저온 상(Martensite)으로 강제 변신하며 엄청난 에너지를 흡수하는 현상"을 수리 산출될 것으로 예상됩니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 29_advanced-materials-and-nanotechnology-hub : 스마트 소재 기술을 통합 관리하는 상위 지능 허브
- [[[MOC] 12_Advanced_Robotics_and_Autonomous_Systems_MOC : 로봇 구동기 적용을 위한 상위 도메인 허브
- Entity bio-hybrid-robotics-and-neuromuscular-actuation-mechanics]] : 생체 근육과 인공 근육의 비교 연계 엔티티

*Created by Flash (HDS Gold V6.3.7 & Meta-Fusion V6.3.7 ULTRA-Enrichment)*
