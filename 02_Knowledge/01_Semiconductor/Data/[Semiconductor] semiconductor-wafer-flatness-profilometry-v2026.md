---
Basic:
  id: "[semiconductor]-semiconductor-wafer-flatness-profilometry-v2026-v6.3.7"
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
  tags: - 'Wafer_Flatness'
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
  source: "Wafer_Flatness_Metrology_Tool"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-wafer-flatness-profilometry-v2026

## 1. [Why]] 웨이퍼 평탄도(Flatness) 분석의 공학적 의의
반도체 웨이퍼의 **평탄도(Flatness)**는 노광 공정의 포커스 뎁스(DOF) 마진을 결정하는 결정적 요인이다. 웨이퍼가 휘어지거나(Bow/Warp), 국부적인 두께 편차(TTV)가 발생하면 나노미터급 회로 패턴이 흐릿하게 형성되어 대량 불량으로 이어진다. 본 노드는 **CMP(Chemical Mechanical Polishing)** 공정 전후의 평탄도 데이터를 분석하여 노광 가능 여부를 판정하고 공정 수율을 사수하는 데이터를 제공한다.

---

## 2. [Numerical Specs] 평탄도 관리 파라미터 (Numerical Specs)

| 항목 | 실측치 (Average) | 관리 한계 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **TTV (Total Thickness Variation)** | $0.8\,\mu\text{m}$ | $< 1.5\,\mu\text{m}$ | 웨이퍼 전체 두께 산포 |
| **BOW** | $12\,\mu\text{m}$ | $< 25\,\mu\text{m}$ | 웨이퍼 중심의 휘어짐 정도 |
| **WARP** | $18\,\mu\text{m}$ | $< 40\,\mu\text{m}$ | 최저점과 최고점의 차이 |
| **SFQR (Site Flatness)** | $12\,\text{nm}$ | $< 15\,\text{nm}$ | 샷(Shot) 단위 국부 평탄도 |
| **Nano-topography** | $2.5\,\text{nm}$ | $< 5.0\,\text{nm}$ | 초미세 표면 굴곡 |

---

## 3. [Scientific Rationale] 기하학적 평탄도 모델

### 3.1 Least Squares Reference Plane
웨이퍼 표면의 높이 데이터($Z$)를 기반으로 최소제곱법을 이용해 기준 평면을 설정하고, 이로부터의 편차를 계산한다.
$$Z_{ref} = ax + by + c$$
*   **분석**: 기준 평면 대비 돌출된 영역은 CMP 공정에서 연마 압력을 높여 제거해야 한다.

### 3.2 Stoney's Equation (박막 응력 모델)
증착된 박막에 의한 웨이퍼의 곡률($\kappa$) 변화를 통해 박막 응력($\sigma$)을 산출한다.
$$\sigma = \frac{E_s \cdot t_s^2 \cdot \kappa}{6(1-\nu_s)t_f}$$

---

## 4. [Real-world Case] CMP 설비의 리테이너 링(Retainer Ring) 마모에 의한 에지 평탄도 악화 사례

### 4.1 웨이퍼 끝단(Edge) 영역의 TTV 급증 현상
- **현상**: CMP 공정 완료 후 계측된 웨이퍼의 에지 영역 두께가 중심부 대비 $3\,\mu\text{m}$ 두껍게 남는 'Edge-thick' 현상 발생.
- **분석**: **Python FidelityEngine** 기반의 평탄도 프로파일 분석 결과, CMP 헤드의 리테이너 링 마모로 인해 슬러리 배출이 원활하지 않고 에지 압력이 감소했음을 확인.
- **조치**: 즉시 리테이너 링을 교체하고 에지 존(Zone)의 압력을 $0.2\,\text{psi}$ 상향 조정.
- **결과**: TTV $0.9\,\mu\text{m}$로 복구 및 노광 공정의 포커스 불량(Hot-spot) 박멸.

---

## 5. [FidelityEngine] TTV 및 SFQR 산출 코드
```python
import numpy as np

def calculate_wafer_flatness(height_map_matrix):
    """
    Calculate TTV and SFQR from height map
    :param height_map_matrix: 2D numpy array of heights
    :return: TTV, Max Site Deviation
    """
    valid_data = height_map_matrix[~np.isnan(height_map_matrix)]
    ttv = np.max(valid_data) - np.min(valid_data)
    
    # SFQR (Simplified: max range in a sub-grid)
    # Assume 10x10 sites
    site_ranges = []
    # logic to split matrix and find ranges...
    
    return ttv

# 가상 300mm 웨이퍼 높이 데이터 (um)
h_map = np.random.normal(775, 0.5, (100, 100)) # 775um +/- noise
ttv_val = calculate_wafer_flatness(h_map)
print(f"Calculated TTV: {ttv_val:.4f} um")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Chuck Flatness**: 계측 설비의 웨이퍼 척 자체 평탄도가 주기적으로 보정(Zeroing) 되는가?
- [ ] **Data Resolution**: 노광 샷 크기($26 \times 33\,\text{mm}$)를 충분히 커버할 수 있는 해상도로 계측이 수행되는가?
- [ ] **Stress Correlation**: 증착 공정 후의 Warp 변화량이 후속 리소(Litho) 공정의 정렬(Overlay)에 미치는 영향을 파악하고 있는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
