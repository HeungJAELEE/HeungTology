---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 642543adb52cd12e5659c85b21a93310169504bef73821e54c65cda894cb0b56
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] semiconductor-dry-etch-anisotropy-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] semiconductor-dry-etch-anisotropy-log-v2026에 관한 고밀도
    지능 노드'
  object_type: Concept
  tier: 1
properties:
  anisotropy_formula: A = 1 - (Rh / Rv)
  bias_power_measured: 450 W
  esc_temperature_measured: 45.0 C
  source_power_reduction_threshold: 5%
  target_anisotropy_factor: '> 0.92'
  theoretical_anisotropy_factor: '1.0'
  theoretical_bias_power_stability: ±0.5 W
  theoretical_etch_rate: 3600 A/min
  theoretical_selectivity_si_pr: 20.0:1
  verified_anisotropy_factor: '0.95'
  verified_bias_power_stability: ±5 W
  verified_etch_rate: 3500 A/min
  verified_selectivity_si_pr: 15.0:1
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

# [Semiconductor] semiconductor-dry-etch-anisotropy-log-v2026

## 1. [Engineering Definition] Dry Etch Anisotropy
Dry Etch Anisotropy: Physical indicator defining vertical dominance in etch direction [Ref: Section 1]. High-Aspect-Ratio(HAR) pattern implementation requires minimization of lateral etch rate ($R_h$) [Ref: Section 1] and maximization of vertical etch rate ($R_v$) [Ref: Section 1]. Anisotropy factor ($A$) deficiency induces Undercut or Bowing, resulting in pattern defects and inter-circuit shorts [Ref: Section 1].

## 2. [Comparative Analysis] Theoretical vs Verified

| Parameter | Theoretical Value | Verified Value | Variance |
| :--- | :--- | :--- | :--- |
| **Anisotropy Factor ($A$)** | $1.0$ [Ref: Physical_Model] | $0.95$ [Ref: Plasma_Etch_System_Log] | $-5.0\%$ |
| **Etch Rate** | $3,600\,\text{\AA/min}$ [Ref: Physical_Model] | $3,500\,\text{\AA/min}$ [Ref: Plasma_Etch_System_Log] | $-2.7\%$ |
| **Selectivity (Si:PR)** | $20.0:1$ [Ref: Physical_Model] | $15.0:1$ [Ref: Plasma_Etch_System_Log] | $-25.0\%$ |
| **Bias Power Stability** | $\pm 0.5\,\text{W}$ [Ref: Physical_Model] | $\pm 5\,\text{W}$ [Ref: Plasma_Etch_System_Log] | $+900\%$ |

## 3. [Numerical Specs] Process Control Parameters

| Item | Measured (Standard) | Target | Remarks |
| :--- | :--- | :--- | :--- |
| **Anisotropy Factor ($A$)** | $0.95$ [Ref: Plasma_Etch_System_Log] | $> 0.92$ | Verticality convergence to $1.0$ |
| **Etch Rate** | $3,500\,\text{\AA/min}$ [Ref: Plasma_Etch_System_Log] | $\pm 100\,\text{\AA/min}$ | Vertical etch velocity |
| **Selectivity (Si:PR)** | $15:1$ [Ref: Plasma_Etch_System_Log] | $> 12:1$ | PR relative etch selectivity |
| **Bias Power** | $450\,\text{W}$ [Ref: Plasma_Etch_System_Log] | $\pm 5\,\text{W}$ | Ion acceleration energy control |
| **ESC Temperature** | $45.0^\circ\text{C}$ [Ref: Plasma_Etch_System_Log] | $\pm 0.5^\circ\text{C}$ | Wafer thermal stability |

## 4. [Scientific Rationale] Etch Mechanism Modeling

### 4.1 Ion-Assisted Chemical Etching
Synergy between radical chemical reaction and ion bombardment physical energy accelerates vertical etching.
$$A = 1 - \frac{R_h}{R_v}$$
*   **$R_h$**: Lateral (Horizontal) Etch Rate [Ref: Section 1].
*   **$R_v$**: Vertical Etch Rate [Ref: Section 1].

### 4.2 Paschen's Law
Discharge voltage ($V$) defined as a function of chamber pressure ($P$) and electrode gap ($d$): $V = f(P \cdot d)$ [Ref: Physical_Model].

## 5. [Real-world Case] Bowing Suppression and Verticality Optimization

### 5.1 HAR Pattern Bowing Analysis
- **Phenomenon**: Side-wall expansion (Bowing) observed in 3D NAND channel hole mid-section.
- **Root Cause**: Passivation layer gas dissociation rate lower than flow rate, resulting in excessive side-wall exposure time.
- **Countermeasure**: Source Power $5\%$ [Ref: Case_Study_Report] reduction for radical density control; Bias Power transition to Pulse Mode for enhanced ion directionality.
- **Result**: Anisotropy Factor $0.96$ [Ref: Case_Study_Report] achieved; profile verticality normalized.

## 6. [FidelityEngine] Anisotropy Calculation Logic

[CODE_START]
def calculate_anisotropy(vertical_rate, horizontal_rate):
    """
    Calculate Etch Anisotropy Factor
    :param vertical_rate: Etch rate in vertical direction (A/min)
    :param horizontal_rate: Etch rate in horizontal direction (A/min)
    :return: Anisotropy factor (0 to 1)
    """
    if vertical_rate <= 0: return 0
    anisotropy = 1 - (horizontal_rate / vertical_rate)
    return max(0, anisotropy)

# Data Input: Vertical 3500, Horizontal 150 [Ref: Plasma_Etch_System_Log]
a_factor = calculate_anisotropy(3500, 150)
print(f"Calculated Anisotropy Factor: {a_factor:.4f}")
[CODE_END]

## 7. [Verification] Process Integrity Checklist
- [ ] **Plasma Stability**: Plasma impedance fluctuation within $1\%$ [Ref: Standard_Verification].
- [ ] **End-point Detection (EPD)**: OES-based detection error within $10\,\text{ms}$ [Ref: Standard_Verification].
- [ ] **Polymer Balance**: Chamber wall polymer accumulation and cleaning cycle optimization status.

**[V7.5.3_HDS_HARDCORE_FIDELITY_CONFIRMED]**