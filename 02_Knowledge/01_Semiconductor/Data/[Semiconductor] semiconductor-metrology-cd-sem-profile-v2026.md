---
Basic:
  id: "[semiconductor]-semiconductor-metrology-cd-sem-profile-v2026-v6.3.7"
  domain: "Semiconductor_Metrology"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'CD-SEM'
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
  source: "CD-SEM_Metrology_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-metrology-cd-sem-profile-v2026

## 1. [Why]] CD-SEM 프로파일 분석의 공학적 의의
**CD-SEM(Critical Dimension Scanning Electron Microscope)**은 반도체 회로의 선폭(CD)을 나노미터급으로 측정하는 핵심 계측 기술이다. 단순히 너비를 재는 것을 넘어, 회로의 단면 형상(Side Wall Angle), 선단의 거칠기(LER/LWR)를 분석하여 노광 및 식각 공정의 최적성을 판단한다. 본 노드는 고해상도 전자빔 데이터를 통해 패턴의 물리적 정밀도를 사수하는 데이터를 제공한다.

---

## 2. [Numerical Specs] CD 계측 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 범위 (Tolerance) | 비고 |
| :--- | :--- | :--- | :--- |
| **Mean CD** | $14.20\,\text{nm}$ | $\pm 0.3\,\text{nm}$ | Gate 레이어 기준 |
| **CD Uniformity (3s)** | $0.25\,\text{nm}$ | $< 0.5\,\text{nm}$ | 웨이퍼 내 선폭 균일도 |
| **LER (Line Edge Roughness)** | $1.5\,\text{nm}$ | $< 2.0\,\text{nm}$ | 선폭의 지그재그 정도 |
| **SWA (Side Wall Angle)** | $89.2^\circ$ | $88 \sim 90^\circ$ | 회로의 수직도 |
| **Beam Energy** | $500\,\text{eV}$ | $\pm 5\,\text{eV}$ | 시료 손상 방지를 위한 저에너지 |

---

## 3. [Scientific Rationale] 전자빔 상호작용 및 프로파일 추출 모델

### 3.1 Secondary Electron (SE) Signal Analysis
시료 표면에서 튀어나오는 이차 전자의 강도를 스캔 위치별로 매핑하여 에지(Edge)를 검출한다.
$$CD = \text{Edge}_{right} - \text{Edge}_{left}$$
*   **분석**: 에지의 기울기($Slope$)를 분석하여 포커스(Focus) 상태나 패턴의 테이퍼(Taper) 각도를 추정한다.

### 3.2 LER/LWR Statistical Model
선폭의 변동을 주파수 영역에서 분석하여 특정 주기의 진동이나 마스크 결함 유무를 파악한다.

---

## 4. [Real-world Case] 노광 포커스 이탈(Out-of-Focus)에 의한 CD 산포 악화 사례

### 4.1 특정 샷(Shot) 영역의 CD 급감 현상
- **현상**: 웨이퍼 중심부의 특정 샷에서 CD가 $14.2\,\text{nm}$에서 $12.5\,\text{nm}$로 급감하고 LER이 $3.0\,\text{nm}$로 증가.
- **분석**: **Python FidelityEngine**을 활용한 SEM 이미지 프로파일 분석 결과, 에지 슬로프가 완만해지는 'Top-rounding' 현상 포착. 이는 노광기의 베스트 포커스(Best Focus) 지점에서 $50\,\text{nm}$ 이상 이탈했음을 시사함.
- **조치**: 스캐너의 가로/세로 틸트(Tilt) 값을 재조정하고 포커스 켈리브레이션 실시.
- **결과**: CD $14.15\,\text{nm}$로 복구 및 샷 간 산포 $0.2\,\text{nm}$ 이내 안착.

---

## 5. [FidelityEngine] CD 측정치 및 산포(3-Sigma) 계산 코드
```python
import numpy as np

def analyze_cd_data(cd_measurements):
    """
    Calculate Mean and 3-Sigma Uniformity
    :param cd_measurements: List of CD values in nm
    :return: Mean, Std, 3-Sigma
    """
    data = np.array(cd_measurements)
    mean_val = np.mean(data)
    std_val = np.std(data, ddof=1)
    three_sigma = 3 * std_val
    
    return mean_val, std_val, three_sigma

# 실측 데이터 (9포인트 계측)
cd_list = [14.1, 14.2, 14.15, 14.3, 14.05, 14.2, 14.1, 14.25, 14.18]
mean, std, ts = analyze_cd_data(cd_list)

print(f"Mean CD  : {mean:.3f} nm")
print(f"3-Sigma : {ts:.3f} nm")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Charging Effect**: 전자빔 조사에 의한 시료의 대전(Charging) 현상이 보정되어 측정치 왜곡이 없는가?
- [ ] **Shrinkage Control**: 반복 측정 시 전자빔 에너지에 의한 패턴 수축(Shrinkage)이 관리 범위 이내인가?
- [ ] **Algorithm Stability**: 복잡한 패턴(3D 구조 등)에서도 에지 검출 알고리즘이 안정적으로 작동하는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
