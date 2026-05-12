---
Basic:
  id: "[semiconductor]-semiconductor-fab-cd-sem-measurement-log-v2026-v6.3.7"
  domain: "Semiconductor_Manufacturing"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Semiconductor_Fab'
  is_part_of: - 'Antigravity_Knowledge_Graph'
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Critical_Dimension_Scanning_Electron_Microscope_CD-SEM_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-fab-cd-sem-measurement-log-v2026

## 1. [Why]] 반도체 CD-SEM 계측 및 임계 치수 로그의 미세 공학적 의의
반도체 회로의 선폭인 **임계 치수(Critical Dimension, CD)**는 소자의 동작 속도와 전력 소모를 결정하는 핵심 파라미터다. 단 몇 나노미터($\text{nm}$)의 선폭 차이로도 트랜지스터의 성능이 완전히 달라지거나 소자가 작동하지 않을 수 있다. **CD-SEM 로그**는 전자 현미경을 통해 수만 개의 지점을 고속 계측하여, 노광 및 식각 공정의 정밀도를 수치화하고 공정 산포를 제어하는 근거를 제공한다.

---

## 2. [Numerical Specs] 임계 치수(CD) 관리 기준 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 한계 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Target CD** | $14.5\,\text{nm}$ | $\pm 0.5\,\text{nm}$ | 타겟 선폭 (Gate Width) |
| **CD Uniformity** | $0.3\,\text{nm}$ | $< 0.8\,\text{nm}$ | 웨이퍼 내 선폭 균일도 |
| **Line Edge Roughness**| $1.2\,\text{nm}$ | $< 2.0\,\text{nm}$ | 선단부 거칠기 (LER) |
| **Measurement Prec** | $0.05\,\text{nm}$ | $< 0.1\,\text{nm}$ | 계측 반복 정밀도 |
| **Throughput (SEM)** | $60\,\text{wph}$ | N/A | 시간당 웨이퍼 처리량 |

---

## 3. [Scientific Rationale] 나노 계측 및 산포 모델

### 3.1 Secondary Electron Imaging (SEI)
전자빔을 시편에 조사하여 발생하는 2차 전자를 포착, 수 나노미터 해상도의 이미지를 얻어 선단(Edge)을 검출한다.
*   **분석**: 전자빔에 의한 시편 손상(Shrinkage)을 최소화하기 위해 저가속 전압($500\text{V}$ 이하) 기술을 적용하며, 알고리즘을 통해 실제 물리적 선폭과 이미지상의 선폭 간의 오차를 보정한다.

### 3.2 CD Uniformity (CDU) Analysis
웨이퍼 전체 영역의 CD 데이터를 지도(Map)로 시각화하여, 노광 장비의 렌즈 수차나 식각 장비의 가스 농도 불균형 지점을 식별한다.

---

## 4. [Real-world Case] 노광 장비 포커스 드리프트에 의한 CD 산포 확대 해결 사례

### 4.1 특정 생산 로트의 게이트 선폭이 목표치 대비 $2\,\text{nm}$ 굵게 형성됨
- **현상**: 전체 웨이퍼의 CD 평균은 정상이지만, 좌측 영역의 선폭이 우측보다 비정상적으로 넓어지는 기울어짐(Tilt) 현상 발생.
- **분석**: **Python FidelityEngine** 기반의 CD 로그 분석 결과, 노광기 스테이지의 수평도가 $100\,\text{nm}$ 단위로 틀어지며 포커스(Focus)가 빗나갔음을 확인.
- **조치**: 본 로그 데이터를 APC 시스템으로 전송하여 다음 웨이퍼 노광 시 스테이지의 기울기를 역보정하고, CD-SEM 데이터를 기반으로 자동 노광량(Dose) 조절 실시.
- **결과**: CD 산포 $0.5\,\text{nm}$ 이내로 복구 및 게이트 공정 마진 확보.

---

## 5. [FidelityEngine] 공정 능력 지수(Cpk) 및 CD 적합성 분석 코드
```python
import numpy as np

def calculate_cd_cpk(cd_measurements, lsl, usl):
    """
    Calculate Process Capability Index (Cpk) for CD measurements
    :param cd_measurements: List of measured CD values (nm)
    :param lsl: Lower Specification Limit
    :param usl: Upper Specification Limit
    :return: Cpk value
    """
    data = np.array(cd_measurements)
    mean = np.mean(data)
    sigma = np.std(data)
    
    if sigma == 0: return 0.0
    
    cpu = (usl - mean) / (3 * sigma)
    cpl = (mean - lsl) / (3 * sigma)
    cpk = min(cpu, cpl)
    
    status = "STABLE" if cpk > 1.67 else "PROCESS_DRIFT_WARNING"
    return {"Mean": mean, "Sigma": sigma, "Cpk": cpk, "Status": status}

# 실측 데이터: Target 14.5, LSL 14.0, USL 15.0
measured = [14.45, 14.55, 14.50, 14.48, 14.52, 14.60]
res = calculate_cd_cpk(measured, 14.0, 15.0)
print(f"CD Metrology: {res['Status']} (Cpk: {res['Cpk']:.2f})")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Magnification Calibration**: 계측 장비의 배율(Magnification)이 표준 시편(Standard Grating)을 통해 매일 교정되고 있는가?
- [ ] **Electron Beam Damage**: 동일 지점 반복 계측 시 전자빔에 의한 선폭 변형(Shrinkage)이 관리 범위 내에 있는가?
- [ ] **Recipe Consistency**: 다른 CD-SEM 장비 간의 측정 편차(Tool-to-Tool Matching)가 $0.1\,\text{nm}$ 이하로 유지되고 있는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
