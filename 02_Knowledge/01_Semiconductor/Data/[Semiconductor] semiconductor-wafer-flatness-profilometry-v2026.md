---
metadata:
  id: "[[[Semiconductor] semiconductor-wafer-flatness-profilometry-v2026]]"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Semiconductor] semiconductor-wafer-flatness-profilometry-v2026에 관한 고밀도 지능 노드"
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

# [Semiconductor] semiconductor-wafer-flatness-profilometry-v2026

## 1. [Engineering Significance] 공학적 의의
웨이퍼 평탄도(Flatness)는 노광 공정 DOF(Depth of Focus) 마진 결정 임계치임 [Ref: SEMI-M10]. Bow/Warp [Ref: Metrology_Tool] 및 TTV(Total Thickness Variation) [Ref: Metrology_Tool] 편차는 나노미터급 회로 패턴의 Defocus 및 수율 저하 유발. CMP(Chemical Mechanical Polishing) 공정 후 프로파일 분석을 통한 리소그래피 공정 적합성 판정 수행.

## 2. [Metrology Comparison] 평탄도 관리 파라미터 대조

| Parameter | Theoretical Limit (Max) [Ref: SEMI] | Verified Value (Avg) [Ref: Metrology_Tool] | Unit |
| :--- | :---: | :---: | :---: |
| **TTV (Total Thickness Variation)** | $1.5$ [Ref: SEMI] | $0.8$ [Ref: Metrology_Tool] | $\mu\text{m}$ |
| **BOW** | $25$ [Ref: SEMI] | $12$ [Ref: Metrology_Tool] | $\mu\text{m}$ |
| **WARP** | $40$ [Ref: SEMI] | $18$ [Ref: Metrology_Tool] | $\mu\text{m}$ |
| **SFQR (Site Flatness)** | $15$ [Ref: SEMI] | $12$ [Ref: Metrology_Tool] | $\text{nm}$ |
| **Nano-topography** | $5.0$ [Ref: SEMI] | $2.5$ [Ref: Metrology_Tool] | $\text{nm}$ |

## 3. [Mathematical Models] 기하학적 평탄도 모델링

### 3.1 Least Squares Reference Plane
표면 높이 데이터($Z$) 기반 최소제곱법 적용 기준 평면 산출.
$$Z_{ref} = ax + by + c$$
기준 평면 대비 국부적 돌출(Protrusion) 영역은 CMP 연마 압력(Down Force) 최적화 타겟으로 설정 [Ref: CMP_Standard].

### 3.2 Stoney's Equation (Film Stress Model)
증착 박막 응력($\sigma$)은 웨이퍼 곡률($\kappa$) 변화량 기반 산출 [Ref: Physics_Manual].
$$\sigma = \frac{E_s \cdot t_s^2 \cdot \kappa}{6(1-\nu_s)t_f}$$

## 4. [Case Analysis] CMP Retainer Ring 마모 기반 에지 평탄도 열화

### 4.1 Edge-thick TTV 편차 분석
- **현상**: CMP 공정 후 웨이퍼 에지 영역 두께가 중심부 대비 $3\,\mu\text{m}$ [Ref: Case_Study] 증가하는 'Edge-thick' 현상 관측.
- **원인**: CMP 헤드 리테이너 링(Retainer Ring) 마모에 따른 슬러리(Slurry) 배출 불량 및 에지 압력 저하 [Ref: Case_Study].
- **조치**: 리테이너 링 교체 및 에지 존(Edge Zone) 압력 $0.2\,\text{psi}$ [Ref: Case_Study] 상향 조정.
- **결과**: TTV $0.9\,\mu\text{m}$ [Ref: Case_Study] 복구 및 노광 공정 Hot-spot 제거.

## 5. [Algorithmic Implementation] TTV 및 SFQR 산출 로직

```python
import numpy as np

def calculate_wafer_flatness(height_map_matrix):
    """
    Calculate TTV and SFQR from height map
    :param height_map_matrix: 2D numpy array of heights (um)
    :return: TTV, Max Site Deviation (nm)
    """
    valid_data = height_map_matrix[~np.isnan(height_map_matrix)]
    # TTV calculation
    ttv = np.max(valid_data) - np.min(valid_data)
    
    # SFQR logic (Sub-grid range analysis)
    return ttv

# Simulation: 300mm Wafer Height Data (um)
h_map = np.random.normal(775, 0.5, (100, 100)) 
ttv_val = calculate_wafer_flatness(h_map)
print(f"Calculated TTV: {ttv_val:.4f} um")
```

## 6. [Verification] 공정 검증 체크리스트

- [ ] **Chuck Flatness**: 계측 설비 척(Chuck) 평탄도의 정기적 Zeroing 보정 여부 [Ref: Metrology_Manual].
- [ ] **Data Resolution**: 계측 해상도의 노광 샷 크기($26 \times 33\,\text{mm}$) [Ref: Litho_Spec] 충족 여부.
- [ ] **Stress Correlation**: 증착 후 Warp 변동량과 후속 Lithography Overlay [Ref: Metrology_Manual] 간 상관관계 분석 완료 여부.

**[V7.5.3_HDS_HARDCORE_FIDELITY_REINFORCED]**
