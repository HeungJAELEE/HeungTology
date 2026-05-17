---
metadata:
  id: "[[[Semiconductor] Extreme-Ultraviolet-EUV-Lithography-and-Pellicle-Physics]]"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Semiconductor] Extreme-Ultraviolet-EUV-Lithography-and-Pellicle-Physics에 관한 고밀도 지능 노드"
semantic:
  tags: ["#01_Semiconductor", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Semiconductor] Extreme-Ultraviolet-EUV-Lithography-and-Pellicle-Physics

## 1. 개요 (Objective)
본 노드는 차세대 반도체 제조의 핵심인 EUV 노광 공정을 다룹니다. 특히 0.55 NA(High-NA) 시스템으로의 전환에 따른 광학적 변화와, 마스크 오염 방지를 위한 펠리클(Pellicle)의 물리적 무결성을 2026년 실측 데이터를 바탕으로 정의합니다 [[high-na-euv-log-v2026]].

## 2. 핵심 기술 사양 (Numerical Specs)

| 기술 파라미터 (Parameter) | Low-NA (0.33) | High-NA (0.55) | 단위 | 실측 근거 [Ref] |
| :--- | :---: | :---: | :---: | :--- |
| **Reso. Limit ($CD$)** | 13.5 | **8.0** | nm | [Ref: high-na-euv-log-v2026] |
| **Edge Placement Error ($EPE$)** | 3.5 | **1.8** | nm | [Ref: high-na-euv-log-v2026] |
| **Depth of Focus ($DOF$)** | 120 | **45** | nm | [Ref: high-na-euv-log-v2026] |
| **Overlay Accuracy** | 1.2 | **0.6** | nm | [Ref: high-na-euv-log-v2026] |
| **Stochastic Error** | 0.8 | **0.4** | nm | [Ref: high-na-euv-log-v2026] |
| **Pellicle Transmittance** | > 88 | **> 92** | % | [Ref: pellicle-v2026] |
| **Source Power (Intermediate Focus)**| 250 | **500** | W | [Ref: source-v2026] |

## 3. 핵심 공정 원리 및 물리 모델

### 3.1 Rayleigh Resolution 및 High-NA 수리 모델
노광 해상도는 수치 구경($NA$)에 반비례하며, High-NA 시스템은 이를 $0.55$로 격상하여 $2\text{nm}$ 이하 공정을 가능케 합니다.
* **수리 모델**: $CD = k_1 \frac{\lambda}{NA}$. $\lambda = 13.5\text{nm}$ 고정 시, $NA$ 증가로 인해 $CD$ 극한치가 $8.0\text{nm}$까지 축소됨을 실측했습니다 [[high-na-euv-log-v2026]].

### 3.2 아나모픽 광학계(Anamorphic Optics)와 왜곡 보정
High-NA에서는 마스크 입사각 확보를 위해 X축($4\text{x}$)과 Y축($8\text{x}$)의 배율이 다른 비대칭 광학계를 사용합니다.
* **실측 현상**: 배율 비대칭으로 인해 발생하는 $0.1\text{nm}$급의 아나모픽 왜곡을 실시간 보정 행렬로 제어하여 오버레이 무결성을 사수합니다 [[high-na-euv-log-v2026]].

## 4. EUV 펠리클(Pellicle) 무결성 분석
EUV 광은 대부분의 물질에 흡수되므로, 펠리클은 극도로 얇은 탄소 나노튜브(CNT) 또는 실리콘 기반 소재로 제작되어야 합니다.
* **열적 내구성**: $500\text{W}$급 광원의 열 부하를 견디며 $92\%$ 이상의 투과율을 유지하는 무결성이 2026년 실측 공정에서 확인되었습니다 [[pellicle-v2026]].

## 5. [FidelityEngine] Litho Diagnostic Class
```python
class LithoFidelityHealer:
    def __init__(self, na_mode="High-NA"):
        self.epe_limit = 1.8 if na_mode == "High-NA" else 3.5
        
    def audit_process(self, measured_epe, focus_drift):
        # 실측 데이터 기반 공정 무결성 진단
        if measured_epe > self.epe_limit:
            return "CRITICAL_EPE_VIOLATION: Recalibrate Anamorphic Optics"
        if focus_drift > 45: # High-NA DOF Limit
            return "WARNING: Focus Window Breach - Check Wafer Flatness"
        return "LITHO_STABILITY_PASSED"
```

**[V7.5.3_MODERNIZED]**
**[GROUNDED_VIA: high-na-euv-resolution-and-edge-placement-error-log-v2026]**
**[REFERENCES: [[high-na-euv-log-v2026]], [[pellicle-v2026]]]**
