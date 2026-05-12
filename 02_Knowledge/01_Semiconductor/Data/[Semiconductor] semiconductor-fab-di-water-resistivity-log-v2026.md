---
Basic:
  id: "[semiconductor]-semiconductor-fab-di-water-resistivity-log-v2026-v6.3.7"
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
  source: "Ultrapure_Water_UPW_System_Monitoring_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-fab-di-water-resistivity-log-v2026

## 1. [Why]] 반도체 팹 초순수 비저항 및 TOC 로그의 환경 공학적 의의
**초순수(Ultrapure Water, UPW)**는 반도체 제조 공정의 약 $30\%$ 이상을 차지하는 세정 공정에서 웨이퍼의 오염 물질을 제거하는 유일한 매체다. 물속의 미세한 이온 농도를 나타내는 **비저항(Resistivity)**과 유기물 농도인 **TOC(Total Organic Carbon)**는 초순수의 품질을 결정하는 절대적인 지표다. 비저항이 떨어지면 웨이퍼 표면에 이온성 오염물이 잔류하여 회로의 전기적 특성을 변질시키며, TOC가 높으면 유기 막이 형성되어 박막의 접착력을 떨어뜨린다.

---

## 2. [Numerical Specs] 초순수(UPW) 품질 기준 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 한계 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Resistivity** | $18.2\,\text{M}\Omega\cdot\text{cm}$ | $> 18.0\,\text{M}\Omega\cdot\text{cm}$ | 이론적 최고 순도 |
| **Total Organic Carbon (TOC)** | $0.8\,\text{ppb}$ | $< 1.0\,\text{ppb}$ | 유기물 오염도 |
| **Dissolved Oxygen (DO)** | $1.2\,\text{ppb}$ | $< 5.0\,\text{ppb}$ | 용존 산소 (산화 방지) |
| **Particles (0.05um)** | $0.5\,\text{ea/mL}$ | $< 1.0\,\text{ea/mL}$ | 미세 입자 수 |
| **Bacteria Count** | $0\,\text{cfu/100mL}$ | $< 1\,\text{cfu/100mL}$ | 미생물 오염도 |

---

## 3. [Scientific Rationale] 수질 분석 및 이온 평형 모델

### 3.1 Ionic Purity and Resistivity
물속의 이온 농도가 낮아질수록 전기가 흐르기 어려워지며, 이론적 한계치는 $25^\circ\text{C}$에서 $18.25\,\text{M}\Omega\cdot\text{cm}$이다.
*   **분석**: 비저항이 $0.1\,\text{M}\Omega\cdot\text{cm}$만 떨어져도 이는 수천 개의 금속 이온이 추가로 유입되었음을 의미하므로 즉시 혼상 이온교환수지(MBP)의 교체 주기를 점검해야 한다.

### 3.2 TOC UV Oxidation
자외선(UV) 램프를 이용해 유기물을 이산화탄소로 산화시킨 후 전도도 변화를 측정하여 유기물 총량을 계산한다.

---

## 4. [Real-world Case] 이온교환수지 파손에 의한 비저항 급락 및 생산 중단 사례

### 4.1 메인 초순수 루프의 비저항이 $15\,\text{M}\Omega\cdot\text{cm}$까지 하락
- **현상**: 세정 장비로 공급되는 초순수의 수질 알람이 발생하며, 웨이퍼 표면의 워터마크(Watermark) 불량 급증.
- **분석**: **Python FidelityEngine** 기반의 수질 로그 역추적 결과, MBP(Mixed Bed Polisher) 내부의 여재가 파손되어 미세 수지 입자가 유출되었음을 확인.
- **조치**: 본 로그 데이터를 바탕으로 즉시 비상 급수 라인으로 전환하고, 파손된 MBP 탱크 격리 및 세정(Flushing) 수행.
- **결과**: 세정 공정 내 이온성 오염 확산 차단 및 수질 정상화.

---

## 5. [FidelityEngine] 비저항 기반 이온 농도 추정 코드
```python
def estimate_ion_concentration(resistivity_mohm_cm):
    """
    Estimate total dissolved solids (TDS) equivalent from resistivity
    :param resistivity_mohm_cm: Measured resistivity in M-Ohm-cm
    :return: Estimated ion concentration in ppb (NaCl equivalent)
    """
    # 18.2 Mohm*cm is ~0.05 ppb (background H+/OH-)
    # Simplified inverse relation
    if resistivity_mohm_cm >= 18.2:
        return 0.05
    
    # Approx: 1 Mohm*cm ~ 500 ppb conductivity equiv
    conductivity_us = 1.0 / resistivity_mohm_cm
    tds_ppb = conductivity_us * 500 # rough estimate factor
    
    return tds_ppb

# 실측 데이터: 17.5 M-Ohm-cm 측정됨
ion_est = estimate_ion_concentration(17.5)
print(f"Estimated Ion Level: {ion_est:.2f} ppb (Limit: < 1.0 ppb)")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Temperature Compensation**: 비저항 측정치가 표준 온도($25^\circ\text{C}$)로 자동 보정(ATC)되어 온도 변화에 따른 왜곡이 제거되고 있는가?
- [ ] **Degasifier Efficiency**: 용존 산소(DO) 수치를 낮추기 위한 진공 탈기 장치(Degasifier)의 압력이 정상 범위를 유지하고 있는가?
- [ ] **Dead Leg Audit**: 초순수 배관망 내에 물이 정체되어 미생물이 증식할 수 있는 '데드 레그(Dead Leg)' 구간이 없는지 정기적으로 검사하는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
