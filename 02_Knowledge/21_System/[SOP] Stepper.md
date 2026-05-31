---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 11807417cbb1eebad9420224ed1e1d8fae23c5226b829e82ff5a7a39921e5c29
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-16'
  domain: 00_System
  id: '[[[00_System] [SOP] Stepper]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: '[SOP] Stepper에 관한 고밀도 지능 노드'
  object_type: Hardware
  tier: 1
properties:
  alignment_accuracy_deviation_nm: 20
  alignment_accuracy_g_line_nm: 100
  alignment_accuracy_i_line_nm: 50
  alignment_accuracy_krf_nm: 30
  exposure_time_msec: 250
  krf_resolution_deviation_um: 0.05
  max_field_size_g_line_mm: 22x22
  max_field_size_i_line_mm: 26x26
  max_field_size_krf_mm: 26x33
  numerical_aperture_formula: NA = n * sin(theta)
  rayleigh_criterion_formula: R = k1 * (lambda / NA)
  resolution_g_line_um: 0.5
  resolution_i_line_um: 0.35
  resolution_krf_um: 0.15
  wavelength_g_line_nm: 436
  wavelength_i_line_nm: 365
  wavelength_krf_nm: 248
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 00_System]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: encapsulates_domain_knowledge
  object: Concept
  predicate: contains_knowledge_of
  subject: '[SOP] Stepper'
  weight: 0.9
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [SOP] Stepper

## 1. Functional Necessity
Step-and-repeat lithography system. Core node for TFT-LCD, OLED, and analog semiconductor manufacturing. Utilizes sequential shot exposure to ensure process stability, serving as the fundamental physical model for optical projection analysis.

## 2. Technical Specifications

| Parameter | G-line Stepper | i-line Stepper | KrF Stepper |
|:---|:---:|:---:|:---:|
| **Wavelength ($\lambda$)** | 436 nm [데이터 부재] | 365 nm [데이터 부재] | 248 nm [데이터 부재] |
| **Exposure Method** | Full-Field | Full-Field | Full-Field |
| **Max Field Size** | ~22 x 22 mm [데이터 부재] | ~26 x 26 mm [데이터 부재] | ~26 x 33 mm [데이터 부재] |
| **Resolution ($R$)** | ~0.5 $\mu$m [데이터 부재] | ~0.35 $\mu$m [데이터 부재] | ~0.15 $\mu$m [데이터 부재] |
| **Alignment Accuracy** | ~100 nm [데이터 부재] | ~50 nm [데이터 부재] | ~30 nm [데이터 부재] |

### 2.1. Fidelity Comparison Analysis
| Parameter | Theoretical | Verified | Deviation ($\Delta$) |
|:---|:---|:---|:---|
| Resolution (KrF) | $< 0.1$ $\mu$m | $0.15$ $\mu$m [데이터 부재] | $+0.05$ $\mu$m |
| Alignment Accuracy | $< 10$ nm | $30$ nm [데이터 부재] | $+20$ nm |

## 3. Physical Mechanism & Governing Equations

### 3.1. Step-and-Repeat Kinematics
Employs mask pattern reduction and projection onto discrete wafer regions. Post-exposure, the stage executes a vector-based displacement (Step). Optimizes Effective Aperture relative to Full-field Aligners to maximize resolution.

### 3.2. Optical Resolution & Aberration Control
Resolution governed by Rayleigh Criterion:
$R = k_1 \times \frac{\lambda}{NA}$ [데이터 부재]

* **Numerical Aperture (NA):** $NA = n \sin \theta$ [데이터 부재]
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