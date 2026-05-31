---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 96b948bd96fed9351ad3b13b3d9a0a5a3bf099b0074283b55417f3f4c1251e8c
metadata:
  date: '2026-05-16'
  domain: 02_Battery
  id: '[[[Battery] battery-pouch-swelling-test-results-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Battery] battery-pouch-swelling-test-results-v2026에 관한 고밀도 지능 노드'
  object_type: Data
  tier: 1
properties:
  compression_pad_thickness_increase: 0.5 mm
  degassing_excess_rate: 10%
  fast_charge_thickness_growth: 4.1%
  frontal_deformation: 12.5 mm
  frontal_impact_speed: 64 km/h
  frontal_max_g_force: 42 G
  gas_composition_c2h4: 45%
  gas_composition_co2: 30%
  gas_composition_h2: 15%
  high_temp_expansion_limit: < 5.0%
  high_temp_storage_thickness_growth: 8.5%
  internal_pressure_threshold: 15 kgf/cm2
  max_deformation_limit: 20.0 mm
  max_von_mises_stress: 250 MPa
  normal_cycle_thickness_growth: 3.2%
  normal_expansion_limit: < 3.0%
  overcharge_thickness_growth: '> 25%'
  plastic_deformation_rate: 15%
  rear_deformation: 8.2 mm
  rear_impact_speed: 50 km/h
  rear_max_g_force: 35 G
  side_deformation: 28.4 mm
  side_impact_speed: 32 km/h
  side_max_g_force: 65 G
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

# [Battery] battery-pouch-swelling-test-results-v2026

## 1. [Numerical Swelling Data]

SOC 100% [Ref: Antigravity Vault] 기준, 온도 및 충전 조건별 두께 팽창(Thickness Growth) 정밀 측정 데이터임.

| Test Condition | SOC (%) | Temperature | Thickness Growth (%) | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Normal Cycle** | 100% [Ref: Antigravity Vault] | $25^\circ\text{C}$ [Ref: Antigravity Vault] | **3.2% [Ref: Antigravity Vault]** | 음극 리튬 삽입에 의한 격자 팽창 |
| **High-Temp Storage** | 100% [Ref: Antigravity Vault] | $60^\circ\text{C}$ [Ref: Antigravity Vault] | **8.5% [Ref: Antigravity Vault]** | 전해액 분해 및 SEI 부반응 가스 생성 |
| **Fast Charge** | 80% [Ref: Antigravity Vault] | $25^\circ\text{C}$ [Ref: Antigravity Vault] | **4.1% [Ref: Antigravity Vault]** | 리튬 석출(Plating) 및 열팽창 복합 작용 |
| **Overcharge** | 120% [Ref: Antigravity Vault] | $25^\circ\text{C}$ [Ref: Antigravity Vault] | **> 25% [Ref: Antigravity Vault]** | 가스 분출(Venting) 임계 상태 도달 |

### 1.1 [Theoretical vs. Verified Expansion]
| Parameter | Theoretical (Design) | Verified (Measured) | Deviation |
| :--- | :--- | :--- | :--- |
| Normal Expansion | < 3.0% [Ref: Design] | 3.2% [Ref: Antigravity Vault] | +0.2% |
| High-Temp Expansion | < 5.0% [Ref: Design] | 8.5% [Ref: Antigravity Vault] | +3.5% |

### 1.2 [Gas Composition & Internal Pressure]
- **Major Components**: $C_2H_4$ 45% [Ref: Antigravity Vault], $CO_2$ 30% [Ref: Antigravity Vault], $H_2$ 15% [Ref: Antigravity Vault]
- **Internal Pressure**: $15\text{ kgf/cm}^2$ [Ref: Antigravity Vault] 미만 유지. 파우치 외장재 인장 강도 내 거동 확인.

## 2. [Engineering Feedback]
- **Design Margin**: 고온 저장 시 8.5% [Ref: Antigravity Vault] 팽창 발생. 가압 패드(Compression Pad) 설계 임계치 초과. 패드 두께 $0.5\text{mm}$ [Ref: Antigravity Vault] 증대 필요.
- **Degassing Optimization**: 화성(Formation) 공정 가스 배출량 설계치 대비 10% [Ref: Antigravity Vault] 과다. 전해액 첨가제(Electrolyte Additives) 조성 최적화 권고.

# [[[Analysis] CTP (Cell-to-Pack) Crash Simulation Report]

## 1. [Numerical Crash Data]

CTP 구조 팩 충돌 시나리오별 구조적 건전성 및 응력 분포 데이터임.

| Crash Case | Impact Speed | Max G-force | Deformation (mm) | Safety Result |
| :--- | :--- | :--- | :--- | :--- |
| **Frontal** | $64\text{ km/h}$ [Ref: Antigravity Vault] | **42 G [Ref: Antigravity Vault]** | $12.5\text{ mm}$ [Ref: Antigravity Vault] | Pass (No Leak) |
| **Side (Pole)** | $32\text{ km/h}$ [Ref: Antigravity Vault] | **65 G [Ref: Antigravity Vault]** | **28.4 mm [Ref: Antigravity Vault]** | **Warning (Cell Crush)** |
| **Rear** | $50\text{ km/h}$ [Ref: Antigravity Vault] | **35 G [Ref: Antigravity Vault]** | $8.2\text{ mm}$ [Ref: Antigravity Vault] | Pass |

### 1.1 [Cell Stress & Strain Analysis]
- **Max Von-Mises Stress**: **250 MPa [Ref: Antigravity Vault]** (각형 캔 하단부 집중)
- **Plastic Deformation Rate**: **15% [Ref: Antigravity Vault]** (사이드 충돌 시 셀 캔 소성 변형률)

### 1.2 [Theoretical vs. Verified Structural Integrity]
| Parameter | Theoretical (Limit) | Verified (Simulation) | Margin |
| :--- | :--- | :--- | :--- |
| Max Deformation | < 20.0 mm [Ref: Design] | 28.4 mm [Ref: Antigravity Vault] | -8.4 mm (Fail) |
| Plastic Strain | < 20.0% [Ref: Design] | 15.0% [Ref: Antigravity Vault] | +5.0% (Pass) |

## 2. [Engineering Feedback]
- **Reinforcement Strategy**: 사이드 충돌 변형량 28.4mm [Ref: Antigravity Vault]로 구조적 취약점 확인. 팩 외부 프레임 강성 10% [Ref: Antigravity Vault] 보강 또는 셀 간 구조용 접착제(Structural Adhesive) 도포량 상향 필수.