---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: f0c67dbe2e16a7b0f64fb4df50268a4c269f9b5fea0ef22ffc02a9410dddbdc5
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-16'
  domain: 00_System
  id: '[[[00_System] [SOP] Metrology]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: '[SOP] Metrology에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  cd_sem_precision_theoretical: 0.05nm
  cd_sem_precision_verified: 0.1nm
  node_size: sub-2nm
  ocd_precision_theoretical: 0.01nm
  ocd_precision_verified: 0.05nm
  overlay_error_vector: '[delta_x, delta_y]'
  overlay_precision_theoretical: 0.2nm
  overlay_precision_verified: 0.5nm
  rayleigh_resolution_formula: R = k1 * lambda / NA
  rcwa_predictive_accuracy: 98%
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 00_System]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: technical_specification
  object: Concept
  predicate: contains_knowledge_of
  subject: '[SOP] Metrology'
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

# [SOP] Metrology

## 1. Engineering Rationale
Sub-2nm node fabrication necessitates absolute quantitative control over Critical Dimension (CD), Overlay, and thin-film properties. Metrology precision is the primary determinant for Threshold Voltage ($V_{th}$) stability [데이터 부재]. Data streams function as the feedback backbone for Advanced Process Control (APC), executing real-time autonomous parameter compensation in high-volume manufacturing (HVM) [데이터 부재].

## 2. Metrology Technology Specification

| Parameter Category | CD-SEM | OCD (Optical CD) | Overlay Metrology | Engineering Rationale |
|:---|:---:|:---:|:---:|:---|
| **Measurement Target** | 2D CD / Top-view | 3D Profile / Depth | Layer Alignment | Modality selection by dimensionality |
| **Precision (P)** | $< 0.1 \text{ nm}$ [데이터 부재] | $< 0.05 \text{ nm}$ [데이터 부재] | $< 0.5 \text{ nm}$ [데이터 부재] | Repeatability metric |
| **Throughput** | Moderate | High [데이터 부재] | High [데이터 부재] | WPH optimization |
| **Resolution** | Sub-nanometer [데이터 부재] | Model-based [데이터 부재] | Pixel-level [데이터 부재] | Physics-limited resolution |
| **Beam Source** | Electron Beam | UV / DUV Light | Optical / Diffraction | Material sensitivity mitigation |
| **Information** | Direct Image | Scatterometry Sig. | Misalignment Vector | Data interpretation method |

### 2.1 Precision Discrepancy Analysis (Theoretical vs. Verified)
| Parameter | Theoretical Limit | Verified Operational | Variance ($\Delta$) | Reference |
|:---|:---:|:---:|:---:|:---|
| CD-SEM Precision | $0.05 \text{ nm}$ | $0.1 \text{ nm}$ | $+100\%$ | [데이터 부재] |
| OCD Precision | $0.01 \text{ nm}$ | $0.05 \text{ nm}$ | $+400\%$ | [데이터 부재] |
| Overlay Precision | $0.20 \text{ nm}$ | $0.50 \text{ nm}$ | $+150\%$ | [데이터 부재] |

## 3. Scientific Rationale & Mathematical Modeling

### 3.1 Rayleigh Criterion for Resolution Limits
Physical resolution ($R$) is governed by the Rayleigh relation:
$$ R = k_1 \frac{\lambda}{NA} $$
* **$R$ (Resolution)**: Minimum resolvable distance [데이터 부재].
* **$\lambda$ (Wavelength)**: Source wavelength (Electron/Photon).
* **Optimization**: CD-SEM minimizes $\lambda$ via high-energy electron beams. OCD utilizes Scatterometry to bypass diffraction limits through periodic signal analysis [데이터 부재].

### 3.2 Scatterometry & RCWA Modeling
OCD utilizes **Rigorous Coupled-Wave Analysis (RCWA)** for 3D topography resolution:
* **Execution**: Diffraction efficiency quantification across $\theta$ (angle) and $\lambda$ (wavelength).
* **Inversion**: Numerical solution of Maxwell's equations; alignment of measured signatures with structural libraries.
* **Predictive Accuracy**: Footing and Side Wall Angle (SWA) detection accuracy: $98\%$ [데이터 부재].

### 3.3 Overlay Vector Analysis
Overlay error is defined as the displacement vector $\vec{E}$ between target and pattern:
$$ \vec{E} = [\Delta x, \Delta y] $$
* **Correction**: Error distribution maps compensate for non-linear scaling errors induced by wafer chuck thermal deformation [데이터 부재].

## 4. Statistical Process Control (SPC) & APC Feedback Logic

APC Feedback Engine for autonomous scanner dose adjustment.

```python
import numpy as np

class APCFeedbackController:
    """
    HDS-Gold V7.5.3 Standard: SPC & Auto-Correction Engine
    """
    def __init__(self, target_cd: float, sigma_limit: float = 3.0):
        self.target = target_cd
        self.limit = sigma_limit
        self.history = []

    def process_cd_data(self, measured_cd: float) -> dict:
        self.history.append(measured_cd)
        
        # 1. Statistical Metric Derivation
        window = self.history[-50:]
        current_mean = np.mean(window)
        current_std = np.std(window)
        
        # 2. Process Capability Index (Cpk)
        # Trigger PM cycle if Cpk < 1.33 [데이터 부재]
        cpk = (self.target - current_mean) / (3 * current_std) if current_std > 0 else float('inf')
        
        # 3. Dose Compensation
        # Error threshold: 0.5 nm [데이터 부재]
        if abs(self.target - measured_cd) > 0.5:
            correction_dose = (self.target - measured_cd) * 1.2 
            return {
                "action": "ADJUST_SCANNER_DOSE", 
                "value": correction_dose, 
                "cpk": cpk
            }
            
        return {"action": "STABLE", "cpk": cpk}
```

## 5. Self-Audit Protocol (Fidelity Check)
1. **CD-SEM**: Quantify Electron Beam Induced Deposition (EBID) impact on accuracy [데이터 부재].
2. **Scatterometry**: Model 3D profile inversion sensitivity to refractive index ($n$) and extinction coefficient ($k$) fluctuations [데이터 부재].
3. **Overlay**: Evaluate delta between In-die Overlay and Target-based Overlay in high-aspect-ratio structures [데이터 부재].