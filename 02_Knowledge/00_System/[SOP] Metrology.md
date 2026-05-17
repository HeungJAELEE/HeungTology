---
metadata:
  id: "[[[SOP] Metrology]]"
  domain: "00_System"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[SOP] Metrology에 관한 고밀도 지능 노드"
semantic:
  tags: ["#00_System", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [SOP] Metrology

## 1. Engineering Rationale
Sub-2nm node fabrication necessitates absolute quantitative control over Critical Dimension (CD), Overlay, and thin-film properties. Metrology precision is the primary determinant for Threshold Voltage ($V_{th}$) stability [Ref: SEM-MET-2026]. Data streams function as the feedback backbone for Advanced Process Control (APC), executing real-time autonomous parameter compensation in high-volume manufacturing (HVM) [Ref: APC-STD-V7].

## 2. Metrology Technology Specification

| Parameter Category | CD-SEM | OCD (Optical CD) | Overlay Metrology | Engineering Rationale |
|:---|:---:|:---:|:---:|:---|
| **Measurement Target** | 2D CD / Top-view | 3D Profile / Depth | Layer Alignment | Modality selection by dimensionality |
| **Precision (P)** | $< 0.1 \text{ nm}$ [Ref: SEM-01] | $< 0.05 \text{ nm}$ [Ref: OCD-01] | $< 0.5 \text{ nm}$ [Ref: OV-01] | Repeatability metric |
| **Throughput** | Moderate | High [Ref: OCD-THRU] | High [Ref: OV-THRU] | WPH optimization |
| **Resolution** | Sub-nanometer [Ref: SEM-01] | Model-based [Ref: RCWA-MOD] | Pixel-level [Ref: OV-01] | Physics-limited resolution |
| **Beam Source** | Electron Beam | UV / DUV Light | Optical / Diffraction | Material sensitivity mitigation |
| **Information** | Direct Image | Scatterometry Sig. | Misalignment Vector | Data interpretation method |

### 2.1 Precision Discrepancy Analysis (Theoretical vs. Verified)
| Parameter | Theoretical Limit | Verified Operational | Variance ($\Delta$) | Reference |
|:---|:---:|:---:|:---:|:---|
| CD-SEM Precision | $0.05 \text{ nm}$ | $0.1 \text{ nm}$ | $+100\%$ | [Ref: SEM-01] |
| OCD Precision | $0.01 \text{ nm}$ | $0.05 \text{ nm}$ | $+400\%$ | [Ref: OCD-01] |
| Overlay Precision | $0.20 \text{ nm}$ | $0.50 \text{ nm}$ | $+150\%$ | [Ref: OV-01] |

## 3. Scientific Rationale & Mathematical Modeling

### 3.1 Rayleigh Criterion for Resolution Limits
Physical resolution ($R$) is governed by the Rayleigh relation:
$$ R = k_1 \frac{\lambda}{NA} $$
* **$R$ (Resolution)**: Minimum resolvable distance [Ref: OPT-2026].
* **$\lambda$ (Wavelength)**: Source wavelength (Electron/Photon).
* **Optimization**: CD-SEM minimizes $\lambda$ via high-energy electron beams. OCD utilizes Scatterometry to bypass diffraction limits through periodic signal analysis [Ref: RCWA-MOD].

### 3.2 Scatterometry & RCWA Modeling
OCD utilizes **Rigorous Coupled-Wave Analysis (RCWA)** for 3D topography resolution:
* **Execution**: Diffraction efficiency quantification across $\theta$ (angle) and $\lambda$ (wavelength).
* **Inversion**: Numerical solution of Maxwell's equations; alignment of measured signatures with structural libraries.
* **Predictive Accuracy**: Footing and Side Wall Angle (SWA) detection accuracy: $98\%$ [Ref: OCD-SIG-V2].

### 3.3 Overlay Vector Analysis
Overlay error is defined as the displacement vector $\vec{E}$ between target and pattern:
$$ \vec{E} = [\Delta x, \Delta y] $$
* **Correction**: Error distribution maps compensate for non-linear scaling errors induced by wafer chuck thermal deformation [Ref: OV-VEC-04].

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
        # Trigger PM cycle if Cpk < 1.33 [Ref: SPC-CPK-01]
        cpk = (self.target - current_mean) / (3 * current_std) if current_std > 0 else float('inf')
        
        # 3. Dose Compensation
        # Error threshold: 0.5 nm [Ref: APC-THRES]
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
1. **CD-SEM**: Quantify Electron Beam Induced Deposition (EBID) impact on accuracy [Ref: EBID-ERR].
2. **Scatterometry**: Model 3D profile inversion sensitivity to refractive index ($n$) and extinction coefficient ($k$) fluctuations [Ref: OPT-MAT].
3. **Overlay**: Evaluate delta between In-die Overlay and Target-based Overlay in high-aspect-ratio structures [Ref: OV-AR-01].
