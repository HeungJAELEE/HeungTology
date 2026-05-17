---
metadata:
  date: "2026-05-16"
  id: "[[[SOP] Stepper]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "00_System"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "11807417cbb1eebad9420224ed1e1d8fae23c5226b829e82ff5a7a39921e5c29"
object:
  object_type: "Concept"
  tier: 1
  description: '[SOP] Stepper에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 00_System]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [SOP] Stepper

## 1. Functional Necessity
Step-and-repeat lithography system. Core node for TFT-LCD, OLED, and analog semiconductor manufacturing. Utilizes sequential shot exposure to ensure process stability, serving as the fundamental physical model for optical projection analysis.

## 2. Technical Specifications

| Parameter | G-line Stepper | i-line Stepper | KrF Stepper |
|:---|:---:|:---:|:---:|
| **Wavelength ($\lambda$)** | 436 nm [Ref: ISO/TS 2024] | 365 nm [Ref: ISO/TS 2024] | 248 nm [Ref: ISO/TS 2024] |
| **Exposure Method** | Full-Field | Full-Field | Full-Field |
| **Max Field Size** | ~22 x 22 mm [Ref: SEMI_Std] | ~26 x 26 mm [Ref: SEMI_Std] | ~26 x 33 mm [Ref: SEMI_Std] |
| **Resolution ($R$)** | ~0.5 $\mu$m [Ref: Fab_Spec] | ~0.35 $\mu$m [Ref: Fab_Spec] | ~0.15 $\mu$m [Ref: Fab_Spec] |
| **Alignment Accuracy** | ~100 nm [Ref: Fab_Spec] | ~50 nm [Ref: Fab_Spec] | ~30 nm [Ref: Fab_Spec] |

### 2.1. Fidelity Comparison Analysis
| Parameter | Theoretical | Verified | Deviation ($\Delta$) |
|:---|:---|:---|:---|
| Resolution (KrF) | $< 0.1$ $\mu$m | $0.15$ $\mu$m [Ref: Fab_Spec] | $+0.05$ $\mu$m |
| Alignment Accuracy | $< 10$ nm | $30$ nm [Ref: Fab_Spec] | $+20$ nm |

## 3. Physical Mechanism & Governing Equations

### 3.1. Step-and-Repeat Kinematics
Employs mask pattern reduction and projection onto discrete wafer regions. Post-exposure, the stage executes a vector-based displacement (Step). Optimizes Effective Aperture relative to Full-field Aligners to maximize resolution.

### 3.2. Optical Resolution & Aberration Control
Resolution governed by Rayleigh Criterion:
$R = k_1 \times \frac{\lambda}{NA}$ [Ref: Rayleigh_1879]

* **Numerical Aperture (NA):** $NA = n \sin \theta$ [Ref: Optics_Standard]
* **Aberration Mitigation:** Employs multi-layer precision lens assemblies to suppress Spherical, Coma, and Astigmatism aberrations, optimizing the Optical Transfer Function (OTF).

### 3.3. Process Divergence
Sub-10nm nodes utilize Scanner technology. Stepper deployment remains dominant in high-layer-count packaging and display processes due to cost-efficiency and process stability.

## 4. Algorithmic Implementation (Wafer Tiling)

```python
def generate_wafer_exposure_map(die_size, wafer_diameter):
    # Calculate maximum die coordinates within wafer boundary
    shot_coordinates = calculate_grid_positions(die_size, wafer_diameter)
    
    # Generate Serpentine path for motion efficiency
    path = optimize_stepping_path(shot_coordinates, mode="Serpentine")
    
    for x, y in path:
        move_to_stage(x, y)
        verify_alignment(mark_type="Global")
        trigger_shutter(exposure_time=250) # msec precision control
```

## 5. Self-Audit Protocol
1. Contrast MTF and aberration control between Step-and-repeat and Step-and-scan architectures.
2. Correlate lens aberration magnitude with CD (Critical Dimension) Uniformity.
3. Analyze ROI of 'Mix-and-Match' strategies (Stepper/Scanner hybrid) in multi-layer manufacturing.
