---
Basic:
  id: "[battery]-battery-ncma-xrd-lattice-analysis-v2026-v6.3.7"
  domain: "Battery_Materials_Science"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'XRD'
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
  source: "XRD_Diffractometer_Log"
  isolation_index: 0.0
---

# [[[Battery] battery-ncma-xrd-lattice-analysis-v2026

## 1. [Why]] NCMA 양극재 XRD 결정 구조 분석의 의의
**NCMA(Nickel-Cobalt-Manganese-Aluminum)** 양극재의 결정 구조는 배터리의 수명과 용량을 결정하는 근본적인 요소다. **XRD(X-Ray Diffraction)** 분석을 통해 격자 상수(Lattice Parameter)의 변화와 **양이온 혼합(Cation Mixing)** 정도를 파악할 수 있으며, 이는 충방전 시 발생하는 상전이(Phase Transition)의 안정성을 예측하는 지표가 된다. 본 노드는 소재 합성 및 소성(Calcination) 공정에서 수집된 결정 구조 데이터를 분석하여 하이-니켈 소재의 구조적 건전성을 검증한다.

---

## 2. [Numerical Specs] XRD 결정 구조 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 임계치 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Lattice Parameter $a$** | $2.875\,\text{\AA}$ | $\pm 0.005\,\text{\AA}$ | 육방정계(Hexagonal) 격자 상수 |
| **Lattice Parameter $c$** | $14.195\,\text{\AA}$ | $\pm 0.010\,\text{\AA}$ | 층상 구조 간격 지표 |
| **$c/a$ Ratio** | $4.937$ | $> 4.90$ | 층상 구조 형성의 건전도 |
| **Cation Mixing ($I_{003}/I_{104}$)** | $1.45$ | $> 1.20$ | 값이 클수록 결정성 우수 |
| **Crystallite Size** | $120\,\text{nm}$ | $> 100\,\text{nm}$ | Scherrer 식 기반 결정 크기 |

---

## 3. [Scientific Rationale] X-선 회절 및 격자 모델

### 3.1 Bragg's Law (회절 조건)
결정 격자 면 간격($d$)과 X-선 파장($\lambda$), 회절각($\theta$) 사이의 관계를 정의한다.
$$n\lambda = 2d \sin\theta$$
*   **분석**: 회절 피크의 위치 이동을 통해 충방전 시 리튬 이온 탈삽입에 따른 격자 수축/팽창률을 계산한다.

### 3.2 Scherrer Equation (결정 크기 계산)
회절 피크의 반치폭($\beta$)을 이용해 결정립의 크기($\tau$)를 산출한다.
$$\tau = \frac{K\lambda}{\beta \cos\theta}$$

---

## 4. [Real-world Case] 소성 온도 과다에 따른 양이온 혼합 심화 사례

### 4.1 $I_{003}/I_{104}$ 비 하락에 의한 수명 급락
- **현상**: 신규 소성로 가동 후 NCMA 소재의 초기 용량은 유지되나, 50회 사이클 후 용량 유지율(Retenion)이 $80\%$ 미만으로 하락.
- **분석**: **XRD 리트벨트 분석(Rietveld Refinement)** 결과, 소성 온도가 설계치보다 $20^\circ\text{C}$ 높아 $Li^+$ 자리에 $Ni^{2+}$가 침범하는 **Cation Mixing** 현상이 $5\%$ 증가했음을 확인.
- **조치**: 소성 온도를 $780^\circ\text{C}$로 하향 조정하고 산소 분압을 $5\%$ 상향하여 결정 구조 안정화.
- **결과**: $I_{003}/I_{104}$ 비 $1.42$로 복구 및 500회 수명 유지율 $92\%$ 달성.

---

## 5. [FidelityEngine] 결정 크기(Scherrer) 계산 코드
```python
import numpy as np

def calculate_crystallite_size(beta_deg, theta_deg, wavelength=0.15406, k=0.9):
    """
    Calculate crystallite size using Scherrer Equation
    :param beta_deg: FWHM (Full Width at Half Maximum) in degrees
    :param theta_deg: Bragg angle in degrees
    :param wavelength: X-ray wavelength in nm (Cu Ka = 0.15406)
    :param k: Scherrer constant
    :return: Size in nm
    """
    beta_rad = np.radians(beta_deg)
    theta_rad = np.radians(theta_deg)
    
    # tau = (K * lambda) / (beta * cos(theta))
    size = (k * wavelength) / (beta_rad * np.cos(theta_rad))
    return size

# 실측 데이터: beta=0.15, theta=18.5
c_size = calculate_crystallite_size(0.15, 18.5)
print(f"Calculated Crystallite Size: {c_size:.2f} nm")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Instrument Calibration**: NIST 표준 시료($LaB_6$ 등)를 이용한 기기적 회절 피크 보정이 완료되었는가?
- [ ] **Phase Purity**: 불순물(NiO, $Li_2CO_3$ 등)에 의한 이종 회절 피크가 검출 한계 이하인가?
- [ ] **Lattice Strain**: 결정 크기 외에 미세 응력(Micro-strain)에 의한 피크 넓어짐 효과가 분리 분석되었는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
