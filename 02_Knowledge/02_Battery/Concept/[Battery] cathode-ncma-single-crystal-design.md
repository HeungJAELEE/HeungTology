---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault / Material-Standard-Group
  original_hash: f81287e4653f32dbd5d4fa6114567e922d8ebd8f553db04d24a81f175effa3b5
metadata:
  ai_status: pending_review
  date: '2026-05-17'
  domain: 02_Battery
  id: '[[[Battery] cathode-ncma-single-crystal-design]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: "하이니켈 양극재의 $H2 \to H3$ 상전이 응력을 물리적으로 극복하기 위한 입자 구조의 단일 도메인화 및 안정화 설계"
  object_type: Hardware
  tier: 1
properties:
  aluminum_doping_mol_percent: 1-3
  capacity_retention_1k_cycles: '> 90%'
  grain_size_d50_um: 2-5
  lattice_volume_change_threshold: < 5%
  micro_crack_density: approx 0
  nickel_content_mol_percent: 90-94
  pressing_density_g_cc: '> 3.6'
  residual_li_ppm: < 500
  thermal_onset_temp_c: '> 230'
  yield_strength_gpa: '> 1'
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 02_Battery]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Section 1'
  intent: structural_validation
  object: < 5 %
  predicate: measured_value
  subject: Lattice Vol. Change
  weight: 0.9
- evidence_coordinate: '[데이터 부재] Section 2'
  intent: mechanical_property_threshold
  object: '> 1 G p a'
  predicate: measured_value
  subject: Fracture Strength
  weight: 0.8
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

# [Battery] cathode-ncma-single-crystal-design

## 1. 공학적 당위성: 구조적 무결성 분석 (Why)
High-Nickel ($Ni > 85\%$) 양극재는 에너지 밀도 극대화가 가능하나, 충방전 과정 중 발생하는 $H1 \to H2 \to H3$ 상전이에 의한 격자 변형($c$-axis contraction)이 입자 내 미세 균열(Micro-cracking)을 유발합니다. 이러한 균열은 전해액 침투 및 부반응(Gas generation)을 가속화하여 수명 및 안전성을 저하시킵니다. 단결정(Single Crystal) NCMA 설계는 다결정(Polycrystalline)의 경계면(Grain boundary)을 제거하여 물리적 파손을 원천 차단하며, $Ni, Co, Mn, Al$ 조성을 최적화하여 고전압/고온 환경에서의 구조적 안정성을 확보하는 것을 목적으로 합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| 항목 (Property) | 수리적 정의 및 물리적 기전 (Scientific Rationale) | 목표 사양 (V7.6.2) | 공학적 근거 (Ref) |
| :--- | :--- | :--- | :--- |
| **Nickel Content** | High Capacity Agent ($Ni \ge 90\%$) | $90 \sim 94 \text{ mol}\%$ | [데이터 부재] |
| **Aluminum Doping** | Structural Stabilizer ($Al$ Ion) | $1 \sim 3 \text{ mol}\%$ | [데이터 부재] |
| **Grain Size ($D_{50}$)** | Single Crystal Domain Diameter | $2 \sim 5 \mu\text{m}$ | [데이터 부재] |
| **Micro-crack Den.** | Cracks/Surface Area (500 Cycles) | $\approx 0$ | [데이터 부재] |
| **Residual Li** | Surface $LiOH$ & $Li_2CO_3$ Concentration | $< 500 \text{ ppm}$ | [데이터 부재] |
| **Capacity Retention**| 1C/1C Cycle Life at $45^\circ\text{C}$ | $> 90\%$ (1k Cycles) | [데이터 부재] |
| **Thermal Onset** | DSC Exothermic Peak Temperature | $> 230^\circ\text{C}$ | [데이터 부재] |
| **Pressing Density**| Electrode Loading Support | $> 3.6 \text{ g/cc}$ | [데이터 부재] |

## 3. 핵심 공학 분석 (Scientific Rationale)
- **Phase Transition Kinetics**: NCMA 조성의 원소 비율은 격자 상수의 비등방성(Anisotropy)을 결정합니다. $Ni$ 함량 증가는 $H2 \to H3$ 상전이 시 $c$-축 방향의 급격한 수축($-8\%$ 이상)을 유도하나, $Al^{3+}$ 이온 치환은 격자 내 반발력을 제어하여 $\Delta V_{lattice} < 5\%$ 수준으로 완화합니다.
- **Solid Mechanics**: 단결정 입자는 다결정 대비 높은 항복 강도($\sigma_y > 1 \text{ GPa}$)를 보유합니다. 압연(Pressing) 공정 시 다결정 입자가 파쇄되며 새로운 계면을 형성하는 것과 달리, 단결정은 구형도를 유지하며 전도성 경로(Conductive Path)를 보존합니다.

## 4. [Skill] Material Fidelity Engine
단결정 합성 시 Over-sintering에 의한 입자 거대화 및 리튬 잔류를 소성 온도($T$)와 산소 분압($P_{O2}$) 궤적을 통해 실시간 Audit하며, 임계 입경 초과 시 출력 저하 리스크를 산출하는 진단 루틴을 포함합니다.

## 5. 검증 프로토콜 (Audit)
1. **Lattice Constancy**: XRD 데이터를 통해 SOC 80% 이상의 고전압 구간에서 격자 부피 변화율이 $5\%$ 이내로 유지되는지 검증.
2. **Crack Integrity**: 500 사이클 후의 단면 SEM 분석을 통해 입자 내부의 기계적 균열 발생 여부를 전수 조사.
3. **Swelling Defense**: 가스 발생 실측 데이터를 근거로, 단결정 표면 코팅($B, Zr, Ti$)이 전해액 산화 전위창을 얼마나 확장했는지 분석.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] battery-materials-and-chemistry-master-guide]]
- [[[Concept] mat-single-crystal-cathode]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**