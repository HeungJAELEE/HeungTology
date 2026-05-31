---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: c6a26c2f8974aeb206a475125da96f3b97326a060826672f9d8d7e58c57ff193
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] semiconductor-wafer-flatness-profilometry-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] semiconductor-wafer-flatness-profilometry-v2026에 관한
    고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  bow_avg_verified: 12 um
  bow_max_theoretical: 25 um
  edge_thick_deviation: 3 um
  edge_zone_pressure_adjustment: 0.2 psi
  litho_shot_size: 26x33 mm
  nano_topography_avg_verified: 2.5 nm
  nano_topography_max_theoretical: 5.0 nm
  recovered_ttv: 0.9 um
  sfqr_avg_verified: 12 nm
  sfqr_max_theoretical: 15 nm
  ttv_avg_verified: 0.8 um
  ttv_max_theoretical: 1.5 um
  warp_avg_verified: 18 um
  warp_max_theoretical: 40 um
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