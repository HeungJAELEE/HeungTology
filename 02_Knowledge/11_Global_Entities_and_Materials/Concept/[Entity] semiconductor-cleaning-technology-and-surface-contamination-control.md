---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: ec97bce094ff5d58d148cf76a825861b421d518a1fb5782060fdaa2304e6b6e9
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] semiconductor-cleaning-technology-and-surface-contamination-control]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] semiconductor-cleaning-technology-and-surface-contamination-control에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  dhf_operating_temp_celsius: '25'
  external_data_endpoint: wafer-surface-particle-count-and-removal-efficiency-v2026
  metallic_impurity_limit_atoms_cm2: 10^10
  pre_critical_threshold_percent: 95.0
  sc1_operating_temp_celsius: 70-80
  sc2_operating_temp_celsius: 70-80
  target_residual_particle_density_per_cm2: 0.1
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

# [Entity] semiconductor-cleaning-technology-and-surface-contamination-control

## 1. 개요 (Why)
반도체 제조 공정의 약 30%는 세정(Cleaning)입니다. 나노미터 단위의 공정에서는 보이지 않는 아주 작은 파티클 하나가 전체 칩을 파괴하는 치명적 불량(Killer Defect)이 됩니다. 식각, 증착, 이온 주입 등 각 공정 단계 전후로 웨이퍼 표면을 완벽하게 정화하는 세정 기술은 수율 사수의 최전방 방어선입니다. 본 노드는 웨이퍼 표면의 원자 수준 청정도를 확보하기 위한 세정 공정 표준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Cleaning Step | Chemicals | Target Contaminant | Operating Temp | Unit |
| :--- | :--- | :--- | :--- | :--- |
| SC-1 (APM) | NH4OH:H2O2:H2O | Particles, Organic | 70 ~ 80 | °C |
| SC-2 (HPM) | HCl:H2O2:H2O | Trace Metals | 70 ~ 80 | °C |
| DHF | HF:H2O | Native Oxide | 25 | °C |
| PRE | N/A | > 99 | N/A | % (>19nm) |
| Metallic Imp | N/A | < $10^{10}$ | N/A | atoms/cm^2 |

## 3. CleanFidelityEngine: Diagnostic Logic

세정 공정의 파티클 제거 효율 및 표면 손실을 진단하는 `CleanFidelityEngine` 로직입니다.

```python
class CleanFidelityEngine:
    def __init__(self, initial_particles, final_particles, etch_loss_nm):
        self.p_in = initial_particles
        self.p_out = final_particles
        self.loss = etch_loss_nm

    def calculate_pre(self):
        """파티클 제거 효율(Particle Removal Efficiency) 진단"""
        pre = (1 - self.p_out / self.p_in) * 100
        if pre < 95.0:
            return f"CRITICAL: Low Cleaning Efficiency ({pre:.1f}%) - Check Chemical Ratio"
        return f"OPTIMAL: High-Fidelity Cleaning (PRE: {pre:.1f}%)"

    def diagnose_surface_damage(self, limit_nm):
        """세정 중 의도치 않은 기판 식각(Etch Loss) 진단"""
        if self.loss > limit_nm:
            return f"WARNING: Excessive Etch Loss ({self.loss}nm) - Potential Device Thinning"
        return "PASS: Surface Integrity Maintained"

engine = CleanFidelityEngine(initial_particles=1000, final_particles=5, etch_loss_nm=0.2)
print(engine.calculate_pre())
```

## 4. 분석 프레임워크: Contamination Control Hierarchy
1. **[RCA Clean Standard]**: 유기물 및 파티클 제거(SC-1)와 금속 불순물 제거(SC-2)를 순차적으로 수행하는 전통적 습식 세정의 근간.
2. **[Physical Assisted Cleaning]**: 메가소닉(Megasonic) 진동이나 극저온 에어로졸(Cryogenic Aerosol)을 이용하여 물리적 힘으로 미세 파티클을 박리.
3. **[Dry Cleaning & Drying]**: 미세 패턴의 붕괴(Pattern Collapse)를 막기 위한 초임계 $CO_2$ 세정 및 마랑고니(Marangoni) 건조 기술.

## 5. 스스로 체크 (Self-Audit)
1. SC-1 세정 시 pH가 높을 때 제타 전위(Zeta Potential) 변화가 파티클 재부착을 억제하는 물리적 원리는?
2. 불산(HF) 세정 후 웨이퍼 표면이 수소 종단(Hydrogen Termination)되어 소수성(Hydrophobic)을 띄는 것이 오염 방지에 유리한 이유는?
3. 10nm 이하의 미세 패턴에서 '건조' 단계의 표면 장력이 패턴 쓰러짐을 유발하는 Laplace Pressure 공식의 의미는?

## 6. 결론 (Deterministic Outcome)
본 노드는 `Data wafer-surface-particle-count-and-removal-efficiency-v2026`와 연동되어, 공정별 오염 유입원을 추적하고 세정 후 잔류 파티클을 0.1개/cm^2 이하로 유지함으로써 반도체 소자의 장기 신뢰성을 결정론적으로 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 10_semiconductor-and-nanofabrication-intelligence-hub
- rca-cleaning-sc1-sc2-mechanics
- Data wafer-surface-particle-count-and-removal-efficiency-v2026