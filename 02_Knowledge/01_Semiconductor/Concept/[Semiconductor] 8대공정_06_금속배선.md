---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 371ad6a3e26dd379fe65ebc35557f69e149793b0c9c8d28fff6e853a0d4ad770
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] 8대공정_06_금속배선]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] 8대공정_06_금속배선에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  bspdn_implementation_threshold: 2nm
  cu_resistivity_theoretical: 1.68 uOhm-cm
  cu_resistivity_verified: 2.2-2.6 uOhm-cm
  diffusion_barrier_materials: Ta/TaN
  em_mitigation_capping_materials: Co, Ru
  ir_drop_improvement_bspdn: 20-30%
  rc_delay_critical_threshold: 5nm
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

# [Semiconductor] 8대공정_06_금속배선

## 1. Engineering Requirement: Interconnect Connectivity
Metallization facilitates the electrical interconnect network for signal transmission. In sub-$5\text{nm}$ scaling $[Ref: Section 1]$, parasitic RC delay remains the critical bottleneck, where increased resistance ($\text{R}$) and capacitance ($\text{C}$) degrade signal propagation velocity. Optimization of resistivity and reliability is the primary objective for advanced nodes.

## 2. Process Mechanism: Copper Damascene
Due to the non-etchable nature of Copper ($\text{Cu}$), the Damascene process integrates interconnects within dielectric layers.

### 2.1 Sequential Integration Steps
1. **Trench Etching**: Formation of interconnect cavities within the dielectric insulation $[Ref: Damascene Standard]$.
2. **Barrier/Seed Deposition**: Deposition of $\text{Ta/TaN}$ diffusion barriers to inhibit $\text{Cu}$ migration into the dielectric, followed by a $\text{Cu}$ seed layer $[Ref: Diffusion Control Manual]$.
3. **Electroplating (ECP)**: Electrochemical deposition of $\text{Cu}$ for trench filling $[Ref: ECP Protocol]$.
4. **CMP (Chemical Mechanical Planarization)**: Surface planarization to eliminate excess $\text{Cu}$ and ensure dielectric isolation $[Ref: CMP Process Standard]$.

## 3. Comparative Analysis: Material & Topology

### 3.1 Theoretical vs. Verified Performance
| Parameter | Theoretical (Bulk/Ideal) | Verified (Thin-film/Process) | Reference |
| :--- | :--- | :--- | :--- |
| $\text{Cu}$ Resistivity | $1.68\ \mu\Omega \cdot \text{cm}$ | $2.2\text{--}2.6\ \mu\Omega \cdot \text{cm}$ $[Ref: Metallurgy Handbook]$ | $[Ref: Material Data]$ |
| EM Resistance | High (Standard) | Optimized via Capping Layer $[Ref: EM Control]$ | $[Ref: Reliability Test]$ |
| IR Drop (BSPDN) | Baseline | $\downarrow\ 20\text{--}30\%$ Improvement $[Ref: BSPDN Research]$ | $[Ref: Node Analysis]$ |

### 3.2 Material Evolution: $\text{Al}$ vs. $\text{Cu}$
* **Aluminum ($\text{Al}$)**: Characterized by higher resistivity and inferior Electromigration ($\text{EM}$) resistance $[Ref: Physical Properties]$.
* **Copper ($\text{Cu}$)**: Exhibits lower resistivity $[Ref: Physical Properties]$ and superior $\text{EM}$ resistance due to higher atomic bonding energy, enabling higher current densities.

## 4. Reliability & Advanced Architectures

### 4.1 Electromigration (EM) Control
$\text{EM}$ is the atomic displacement caused by high current density via electron bombardment, inducing voids or hillocks $[Ref: EM Theory]$.
* **Mitigation Strategy**: Implementation of Capping Layers (e.g., $\text{Co, Ru}$) and structural optimization to suppress atomic migration $[Ref: Reliability Engineering]$.

### 4.2 BSPDN (Backside Power Delivery Network)
In nodes below $2\text{nm}$ $[Ref: Next-Gen Scaling]$, routing congestion between signal and power lines induces severe $\text{IR}$ Drop and noise.
* **Mechanism**: Relocation of the Power Delivery Network ($\text{PDN}$) to the wafer backside $[Ref: Next-Gen Scaling]$.
* **Benefit**: Decouples signal and power routing, increasing routing density and reducing $\text{IR}$ Drop $[Ref: BSPDN Architecture]$.

### 4.3 Emerging Materials & Hybrid Bonding
* **Next-Gen Metals**: Transition to Ruthenium ($\text{Ru}$) or Molybdenum ($\text{Mo}$) to bypass thick diffusion barriers and minimize resistance at ultra-scaled dimensions $[Ref: 2026 Trend Report]$.
* **Hybrid Bonding**: Direct $\text{Cu-to-Cu}$ bonding for chiplet integration, bypassing micro-bumps to minimize interconnect distance $[Ref: Advanced Packaging Standard]$.