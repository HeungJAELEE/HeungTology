---
Basic:
  id: "[semiconductor]-semiconductor-nanolithography-euv-exposure-yield-log-v2026-v6.3.7"
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
  tags: - 'EUV'
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
  source: "EUV_Lithography_Scanner_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-nanolithography-euv-exposure-yield-log-v2026

## 1. [Why]] EUV 노광 수율 로그의 나노 공학적 의의
$7\,\text{nm}$ 이하의 초미세 반도체 제조에서 **EUV(Extreme Ultraviolet)** 노광 공정은 수율을 결정하는 가장 핵심적인 관문이다. $13.5\,\text{nm}$의 짧은 파장을 사용하는 EUV는 광원 출력의 안정성, 포토마스크의 결함, 감광액(PR)의 반응성에 매우 민감하다. **EUV 노광 수율 로그**는 웨이퍼 당 노광 시간, 초점 오차(Focus Error), 에너지 선량(Dose) 데이터를 기록하여, 패턴 전사 품질을 관리하고 고가의 EUV 장비 가동 효율을 극대화하는 데이터를 제공한다.

---

## 2. [Numerical Specs] EUV 노광 핵심 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 임계치 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **EUV Source Power** | $250\,\text{W}$ | $> 200\,\text{W}$ | 생산성(WPH) 직결 |
| **Overlay Accuracy** | $1.2\,\text{nm}$ | $< 1.5\,\text{nm}$ | 층간 정렬 정밀도 |
| **CD Uniformity (3$\sigma$)**| $0.8\,\text{nm}$ | $< 1.0\,\text{nm}$ | 선폭 균일도 |
| **Focus Margin** | $40\,\text{nm}$ | $> 30\,\text{nm}$ | 초점 심도 여유분 |
| **Dose Stability** | $\pm 0.1\%$ | $\pm 0.2\%$ | 노광 에너지 변동폭 |

---

## 3. [Scientific Rationale] 나노 패터닝 및 수율 손실 모델

### 3.1 Rayleigh Criterion (해상도 한계)
EUV 노광의 최소 선폭($R$)은 파장($\lambda$)과 개구수($NA$)에 의해 결정된다.
$$R = k_1 \cdot \frac{\lambda}{NA}$$
*   **분석**: High-NA EUV($NA=0.55$) 도입 시 해상도는 향상되지만, 초점 심도(DOF)가 급격히 얕아져 나노미터 단위의 스테이지 제어가 필수적이다.

### 3.2 Shot Noise (양자 노이즈)
포톤(Photon) 수의 확률적 변동에 의해 발생하는 패턴 거칠기(LER/LWR)를 모델링한다.

---

## 4. [Real-world Case] EUV 광원 출력 저하에 따른 패턴 전사 불량 해결 사례

### 4.1 소스 미러(Collector Mirror) 오염에 의한 수율 하락 현상 포착
- **현상**: EUV 스캐너 가동 중 동일한 노광 조건임에도 불구하고 패턴의 선폭(CD)이 점진적으로 굵어지며 수율이 $2\%$ 하락.
- **분석**: **Python FidelityEngine** 기반의 장비 로그 분석 결과, EUV 광원의 중간 초점(IF) 파워가 1주일 새 $15\%$ 감소했음을 확인. 이는 주석(Sn) 입자가 컬렉터 미러에 흡착되어 반사율이 저하된 것이 원인으로 판별됨.
- **조치**: 즉시 수소($H_2$) 클리닝 공정을 수행하여 미러 표면의 주석 오염 제거 및 광원 출력 복구.
- **결과**: 노광 에너지 선량 정상화 및 패턴 수율 $100\%$ 복구.

---

## 5. [FidelityEngine] EUV 해상도(Resolution) 및 DOF 계산 코드
```python
def calculate_euv_limits(lambda_nm, na, k1=0.3):
    """
    Calculate EUV resolution and Depth of Focus
    :param lambda_nm: Wavelength (default 13.5)
    :param na: Numerical Aperture
    :param k1: Process factor
    :return: (Resolution, DOF) in nm
    """
    resolution = k1 * (lambda_nm / na)
    # DOF = k2 * (lambda / na^2)
    k2 = 0.5
    dof = k2 * (lambda_nm / (na ** 2))
    
    return resolution, dof

# Standard EUV (NA=0.33) vs High-NA (NA=0.55)
res_std, dof_std = calculate_euv_limits(13.5, 0.33)
res_high, dof_high = calculate_euv_limits(13.5, 0.55)

print(f"Standard NA: Res {res_std:.2f}nm, DOF {dof_std:.2f}nm")
print(f"High-NA:     Res {res_high:.2f}nm, DOF {dof_high:.2f}nm")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Mask Inspection**: 노광 전 EUV 마스크의 반사층에 결함(Phase Defect)이 없는지 화이트 라이트 및 화학적 검사가 완료되었는가?
- [ ] **Vacuum Integrity**: EUV는 대기에 흡수되므로 스캐너 내부 진공도가 $10^{-7}\,\text{Torr}$ 이하로 유지되고 있는가?
- [ ] **Resist Sensitivity**: 사용 중인 감광액(PR)의 감도가 광원 출력과 매칭되어 최적의 노광 시간을 확보하고 있는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
