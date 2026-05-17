---
metadata:
  date: "2026-05-16"
  id: "[[[Semiconductor] semiconductor-metrology-cd-sem-profile-v2026]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "01_Semiconductor"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "c3c680da68b63f192696ee224a7ee8e2241e9eb42a009f5bf506f57afc5337ae"
object:
  object_type: "Concept"
  tier: 1
  description: '[Semiconductor] semiconductor-metrology-cd-sem-profile-v2026에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 반도체_백서_통합_지휘소]]"
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


# [Semiconductor] semiconductor-metrology-cd-sem-profile-v2026

## 1. [Engineering Significance] CD-SEM 프로파일 분석
CD-SEM(Critical Dimension Scanning Electron Microscope)은 나노미터 스케일 CD 정량화를 위한 고정밀 계측 프레임워크임 [Ref: CD-SEM_Metrology_Log Section 1.1]. SWA(Side Wall Angle) 및 LER/LWR(Line Edge/Width Roughness) 모폴로지 분석을 통해 Lithography 및 Etching 공정의 최적성을 검증하며, 고해상도 전자빔 데이터를 기반으로 패턴 물리 정밀도 및 공정 마진을 확보함 [Ref: CD-SEM_Metrology_Log Section 1.2].


## 2. [Numerical Specs] CD 계측 파라미터

| 항목 | 실측치 (Standard) | 관리 범위 (Tolerance) | 비고 |
| :--- | :--- | :--- | :--- |
| **Mean CD** | $14.20\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 2.1] | $\pm 0.3\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 2.1] | Gate 레이어 기준 |
| **CD Uniformity (3s)** | $0.25\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 2.2] | $< 0.5\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 2.2] | Wafer-level 균일도 |
| **LER** | $1.5\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 2.3] | $< 2.0\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 2.3] | 선폭 경계 거칠기 |
| **SWA** | $89.2^\circ$ [Ref: CD-SEM_Metrology_Log Section 2.4] | $88 \sim 90^\circ$ [Ref: CD-SEM_Metrology_Log Section 2.4] | 패턴 수직도 |
| **Beam Energy** | $500\,\text{eV}$ [Ref: CD-SEM_Metrology_Log Section 2.5] | $\pm 5\,\text{eV}$ [Ref: CD-SEM_Metrology_Log Section 2.5] | 시료 손상 방지 최적값 |


## 3. [Comparative Analysis] Theoretical vs. Verified

| Parameter | Theoretical (Ideal) | Verified (Measured) | Deviation |
| :--- | :--- | :--- | :--- |
| CD (nm) | $14.20$ | $14.20$ [Ref: CD-SEM_Metrology_Log Section 3.1] | $0.00$ |
| CD Uniformity (nm) | $0.00$ | $0.25$ [Ref: CD-SEM_Metrology_Log Section 3.2] | $+0.25$ |
| LER (nm) | $0.00$ | $1.50$ [Ref: CD-SEM_Metrology_Log Section 3.3] | $+1.50$ |
| SWA (deg) | $90.0$ | $89.2$ [Ref: CD-SEM_Metrology_Log Section 3.4] | $-0.8$ |
| Beam Energy (eV) | $500.0$ | $500.0$ [Ref: CD-SEM_Metrology_Log Section 3.5] | $0.0$ |


## 4. [Scientific Rationale] 전자빔 상호작용 및 프로파일 추출 모델

### 4.1 Secondary Electron (SE) Signal Analysis
시료 표면 탈출 이차 전자의 강도(Intensity)를 스캔 위치별로 매핑하여 Edge 검출 수행.
$$CD = \text{Edge}_{\text{right}} - \text{Edge}_{\text{left}}$$
- **Analysis**: Edge Slope 분석을 통해 Focus 상태 및 패턴 Taper 각도 추정 [Ref: CD-SEM_Metrology_Log Section 4.1].

### 4.2 LER/LWR Statistical Model
선폭 변동을 주파수 영역(Frequency Domain)에서 분석하여 특정 주기 진동 및 Mask Defect 식별 [Ref: CD-SEM_Metrology_Log Section 4.2].


## 5. [Real-world Case] 노광 Focus 이탈에 의한 CD 산포 악화

### 5.1 Observed Defect 및 Causal Analysis
- **Phenomenon**: Wafer 중심부 특정 Shot에서 CD $14.2\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 5.1] $\rightarrow$ $12.5\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 5.1] 급감, LER $3.0\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 5.1] 상승.
- **Root Cause**: Edge Slope 완화에 따른 'Top-rounding' 현상 발생. Scanner Best Focus 지점에서 $50\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 5.2] 이상 이탈 확인.
- **Action**: Scanner Tilt 재조정 및 Focus Calibration 수행.
- **Result**: CD $14.15\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 5.3] 복구, Shot 간 산포 $0.2\,\text{nm}$ [Ref: CD-SEM_Metrology_Log Section 5.3] 이내 제어.


## 6. [FidelityEngine] CD 측정치 및 산포(3-Sigma) 연산 모듈

```python
import numpy as np

def analyze_cd_data(cd_measurements):
    """
    Calculate Mean and 3-Sigma Uniformity for High-Fidelity Metrology.
    :param cd_measurements: List of CD values in nm
    :return: Mean, Std, 3-Sigma
    """
    data = np.array(cd_measurements)
    mean_val = np.mean(data)
    std_val = np.std(data, ddof=1)
    three_sigma = 3 * std_val
    
    return mean_val, std_val, three_sigma

# Real-time measurement data (9-point sampling)
cd_list = [14.1, 14.2, 14.15, 14.3, 14.05, 14.2, 14.1, 14.25, 14.18]
mean, std, ts = analyze_cd_data(cd_list)

print(f"Mean CD  : {mean:.3f} nm")
print(f"3-Sigma : {ts:.3f} nm")
```


## 7. [Verification] Metrology Integrity Checklist
- [ ] **Charging Effect**: 전자빔 조사에 의한 시료 대전(Charging) 보정 완료 여부.
- [ ] **Shrinkage Control**: 반복 측정 시 Beam Energy 기반 패턴 수축(Shrinkage) 관리 범위 준수 여부.
- [ ] **Algorithm Stability**: 3D 구조 등 복잡 패턴에서의 Edge Detection 알고리즘 안정성 검증.

**[V7.5.3_HDS_GOLD_REINFORCED_BY_FidelityEngine]**
