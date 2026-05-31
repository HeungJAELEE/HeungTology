---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 29ee0e3dfe6a1194f50716bf3983ceb72604bb342d4f644d2522cbb5b26a4f36
metadata:
  date: '2026-05-16'
  domain: 02_Battery
  id: '[[[Battery] battery-pressing-load-profile-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Battery] battery-pressing-load-profile-v2026에 관한 고밀도 지능 노드'
  object_type: Data
  tier: 1
properties:
  external_db_endpoint: Antigravity Vault
  max_electrode_density_theoretical: 3.85 g/cc
  max_electrode_density_verified: 3.75 g/cc
  min_gap_theoretical: 80 um
  min_gap_verified: 85 um
  ncma_single_crystal_yield_strength: 1.2 GPa
  particle_breakage_at_4_2kncm_verified: 1.5%
  polycrystalline_breakage_threshold: '>8%'
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

# [Battery] battery-pressing-load-profile-v2026

## 1. [압연 공정 개요 (Process Overview)]
본 문서는 코팅 완료된 전극의 기공률(Porosity) 제어 및 체적 에너지 밀도 극대화를 위한 롤 프레스(Roll Press) 하중 인가 메커니즘을 정의한다. 롤 선압 인가에 따른 전극 밀도 변화 및 입자 파손(Particle Breakage)의 상관관계를 분석하여 최적의 압연 윈도우(Pressing Window)를 산출한다.

## 2. [선압 및 전극 밀도 데이터 (Line Force vs. Density)]

| 롤 선압 ($kN/cm$) | 갭 ($H, \mu\text{m}$) | 전극 밀도 ($g/cc$) | 입자 파손율 (%) | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 [Ref: Antigravity Vault] | 150 [Ref: Antigravity Vault] | 3.1 [Ref: Antigravity Vault] | 0.2 [Ref: Antigravity Vault] | 초기 압축 (Low-density) |
| 2.5 [Ref: Antigravity Vault] | 110 [Ref: Antigravity Vault] | 3.45 [Ref: Antigravity Vault] | 0.8 [Ref: Antigravity Vault] | 표준 공정 (Standard) |
| 4.2 [Ref: Antigravity Vault] | 85 [Ref: Antigravity Vault] | 3.75 [Ref: Antigravity Vault] | 1.5 [Ref: Antigravity Vault] | 고밀도 임계 (High-density) |

## 3. [이론치 및 검증치 대조 (Theoretical vs. Verified)]

| Parameter | Theoretical (Ideal) | Verified (Measured) [Ref: Antigravity Vault] | Deviation ($\Delta$) |
| :--- | :--- | :--- | :--- |
| Max Electrode Density | $3.85 \text{ g/cc}$ | $3.75 \text{ g/cc}$ | $-2.60\%$ |
| Minimum Gap ($H$) | $80 \mu\text{m}$ | $85 \mu\text{m}$ | $+6.25\%$ |
| Particle Breakage (at 4.2 kN/cm) | $0.5\%$ | $1.5\%$ | $+200.0\%$ |

## 4. [Yield Strength 및 구조적 무결성 (Structural Integrity)]
- **NCMA Single Crystal $\sigma_y$**: $1.2 \text{ GPa}$ [Ref: Antigravity Vault]
- **구조적 진단**: $4.2 \text{ kN/cm}$의 극한 선압 조건 하에서도 입자 파손율이 $1.5\%$ [Ref: Antigravity Vault]로 유지됨. 이는 다결정(Polycrystalline) 소재의 파손율($> 8\%$) 대비 압도적인 기계적 내구성을 입증하며, 단결정 구조의 전극 밀도 확보를 위한 공정 타당성을 뒷받침함.

*Document integrity verified by Antigravity V7.5.2 Architecture*