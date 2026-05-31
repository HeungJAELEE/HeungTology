---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: f05704b70c6590a6e6de9e374db884390d5f9c7d28ea9d2cc5cb634d15c54efd
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] master-material-ipa]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] master-material-ipa에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  antoine_equation_reference: ANT-DB-V4
  boiling_point_temp: 82.6 C
  dynamic_viscosity_20c: 2.43 cP
  flash_point_temp: 11.7 C
  metal_impurity_max: 10 ppt
  moisture_content_max: 50 ppm
  nist_reference: NIST-CW
  purity_assay_min: 99.999%
  semi_standard_ref: SEMI-UP-S
  surface_tension_20c: 21.7 mN/m
  vapor_pressure_20c: 4.4 kPa
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

# [Semiconductor] master-material-ipa

## 1. Engineering Objective
IPA(Isopropyl Alcohol): 반도체, 배터리, 디스플레이 공정 내 표면 장력 제어 및 계면 정화를 위한 핵심 용제. Core Object Principle에 의거, 도메인 데이터 통합을 통한 전사 품질 표준 수립 및 공급망 영향 분석(Impact Analysis)의 물리적 기초 데이터로 기능함.

## 2. Material Specifications & Comparative Analysis

### 2.1 Technical Specification Matrix
| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Purity** | Assay (%) | $\ge 99.999\%$ [Ref: SEMI-UP-S Section 1.1] | 소자 신뢰성 확보 및 누설 전류 방지 |
| **Moisture** | Water (ppm) | $\le 50\text{ ppm}$ [Ref: BATT-EL-S Section 4.2] | 전해액 부반응 및 산화막 형성 억제 |
| **Surface Tension**| Tension (mN/m) | $21.7\text{ mN/m}$ (@ $20 \text{ }^\circ\text{C}$) [Ref: CRC-HCP Table 3.1] | Marangoni 건조 최적화 |
| **Vapor Press.** | Pressure (kPa) | $4.4\text{ kPa}$ (@ $20 \text{ }^\circ\text{C}$) [Ref: NIST-CW Section 2.0] | 잔류물 없는 휘발 건조 설계 |
| **Metal Impurity** | Metal (ppt) | $\le 10\text{ ppt}$ [Ref: SEMI-GS Section 3.5] | Gate Oxide Integrity(GOI) 확보 |
| **Boiling Point** | Temp ($^\circ\text{C}$) | $82.6 \text{ }^\circ\text{C}$ [Ref: NIST-CW Section 2.0] | 증류 재생 시스템 설계 기준 |
| **Flash Point** | Temp ($^\circ\text{C}$) | $11.7 \text{ }^\circ\text{C}$ [Ref: MSDS-IPA Section 9.1] | 방폭 설비 설계 임계치 |
| **Viscosity** | Dynamic (cP) | $2.43\text{ cP}$ (@ $20 \text{ }^\circ\text{C}$) [Ref: CRC-HCP Table 3.1] | 유체 역학적 흐름 제어 |

### 2.2 Theoretical vs. Verified Value Comparison
| Metric | Theoretical Value (Literature) | Verified Value (Industrial Target) | Variance/Margin | Reference |
|:---|:---:|:---:|:---:|:---|
| **Purity** | $100.0\%$ [Ref: Ideal] | $\ge 99.999\%$ [Ref: SEMI-UP-S] | $-0.001\%$ | SEMI-Standard |
| **Surface Tension** | $21.7\text{ mN/m}$ [Ref: CRC-HCP] | $21.5 \sim 21.9\text{ mN/m}$ [Ref: Internal] | $\pm 0.2$ | CRC/Internal |
| **Boiling Point** | $82.6 \text{ }^\circ\text{C}$ [Ref: NIST-CW] | $82.4 \sim 82.8 \text{ }^\circ\text{C}$ [Ref: Internal] | $\pm 0.2$ | NIST/Internal |
| **Moisture** | $0\text{ ppm}$ [Ref: Ideal] | $\le 50\text{ ppm}$ [Ref: BATT-EL-S] | $+50\text{ ppm}$ | BATT-EL-Std |

## 3. Scientific Rationale

### 3.1 Marangoni Effect & Wafer Drying
IPA 증기 분사를 통한 수계-비수계 계면의 표면 장력 구배($\nabla \gamma$) 형성 기제. IPA의 저표면장력($21.7\text{ mN/m}$ [Ref: CRC-HCP Table 3.1])과 물($72.8\text{ mN/m}$ [Ref: CRC-HCP Table 3.1]) 간의 장력 차가 마랑고니 흐름(Marangoni flow)을 유도하여 액체를 고장력 영역으로 강제 이동시킴. 나노 패턴의 stiction 및 워터마크(Watermark) 형성 방지의 핵심 물리 기제임.

### 3.2 Antoine Equation & Volatility Control
$\log_{10} P = A - \frac{B}{C + T}$ [Ref: ANT-DB-V4 Section 1.0]
온도($T$)에 따른 포화 증기압($P$)의 정밀 산출을 통해 대면적 기판 건조 속도 제어 및 배터리 극판 수분 치환 공정 내 용매 회수율 최적화.

### 3.3 Hansen Solubility Parameter (HSP)
분산력($\delta_d$), 극성($\delta_p$), 수소 결합 에너지($\delta_h$) 기반 유기 오염물(Photoresist 등) 상용성 분석. 양친매성(Amphiphilic) 특성을 활용하여 수계 세정과 비수계 공정 간의 'Bridge Solvent'로 기능함.

## 4. ChemicalPhysicsDiagnosticEngine (Implementation)

```python
import numpy as np

class ChemicalPhysicsDiagnosticEngine:
    """
    HDS-Gold V7.5.3 Spec: IPA Material Physics & Grade Validation Engine
    """
    def __init__(self):
        # Antoine constants for IPA (T in Celsius, P in mmHg) [Ref: ANT-DB-V4 Section 1.0]
        self.A, self.B, self.C = 8.11778, 1580.92, 219.61

    def calculate_vapor_pressure(self, temp_c):
        """
        Calculate saturation vapor pressure (kPa) via Antoine Equation.
        """
        log_p = self.A - (self.B / (temp_c + self.C))
        p_mmhg = 10**log_p
        p_kpa = p_mmhg * 0.133322
        return round(p_kpa, 2)

    def validate_material_grade(self, purity_percent, moisture_ppm):
        """
        Grade determination based on purity and moisture metrics.
        """
        if purity_percent >= 99.999 and moisture_ppm <= 50:
            return "GRADE: SEMICONDUCTOR_UPS_CERTIFIED"
        elif purity_percent >= 99.9 and moisture_ppm <= 500:
            return "GRADE: BATTERY_EL_CERTIFIED"
        return "GRADE: REJECTED_INDUSTRIAL_ONLY"
```

## 5. Engineering Audit Checklist
1. **Fluid Dynamics**: IPA 증기 농도 부족에 따른 Water Mark 발생의 유체역학적 원인과 표면 장력 구배($\nabla \gamma$) 상관관계 정의 여부.
2. **Electrochemical Stability**: 배터리 공정 내 Moisture $\le 50\text{ ppm}$ [Ref: BATT-EL-S Section 4.2] 관리가 전해액 분해(Electrolyte Decomposition) 억제에 미치는 영향 검증 여부.
3. **Device Reliability**: Semiconductor 등급의 Metal Impurity $\le 10\text{ ppt}$ [Ref: SEMI-GS Section 3.5] 제어가 Gate Oxide Integrity(GOI) 및 누설 전류 제어에 미치는 물리적 근거 명시 여부.

**[V7.5.3_HARDCORE_FIDELITY_VERIFIED]**
**[TIMESTAMP: 2026-05-14]**