---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 7043e198cf095232353cdb3ebd1d725958ad12ad036c157a27079dfe18891b92
metadata:
  date: '2026-05-16'
  domain: 02_Battery
  id: '[[[Battery] battery-raw-material-psd-analysis]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Battery] battery-raw-material-psd-analysis에 관한 고밀도 지능 노드'
  object_type: Data
  tier: 1
properties:
  bi_modal_mixing_ratio: '7:3'
  d10_fine_um: 4.2
  d50_median_um: 11.5
  d90_coarse_um: 22.8
  lip_gap_max_particle_ratio: 0.5
  psd_span_ratio: 1.62
  shear_rate_reference_s_inv: 100
  span_critical_limit: 2.0
  specific_surface_area_m2_g: 0.85
  tap_density_actual_g_cm3: 2.45
  tap_density_target_g_cm3: 2.4
  viscosity_span_threshold: 1.8
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 02_Battery]]'
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

# [Battery] battery-raw-material-psd-analysis

## 1. 개요 (Objective)
본 분석 노드는 배터리 활물질의 입도 분포(PSD)를 정량적으로 측정하여, 전극 제조 공정의 효율성과 셀 성능의 무결성을 확보하기 위한 기초 데이터를 제공합니다. 입자의 크기와 분포는 슬러리의 흐름 특성, 코팅층의 밀도, 그리고 전하 이동 경로의 굴곡도(Tortuosity)를 결정하는 핵심 파라미터입니다 [Ref: psd-analysis-log-v2026].

## 2. PSD 실측 사양 및 입자 통계 (Verified Specs)

본 데이터는 `battery-raw-material-psd-analysis-log-v2026` 실측 로그를 기반으로 작성되었습니다. (Safe-Table 규격)

| 분석 항목 (Metric) | 실측치 (Verified) | 단위 | 오차 (Tol) | 분석 장비 | 공학적 의미 |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **D10 (Fine)** | 4.2 | um | ±0.2 | Laser Diff. | 미분(Fine) 함량 및 안전성 |
| **D50 (Median)** | 11.5 | um | ±0.5 | Laser Diff. | 대표 입경 및 비표면적 |
| **D90 (Coarse)** | 22.8 | um | ±1.0 | Laser Diff. | 거대 입자 및 코팅 불량 리스크 |
| **Span (Width)** | 1.62 | Ratio | ±0.1 | Calculation | 분포의 균일도 (D90-D10/D50) |
| **Specific Surface** | 0.85 | m2/g | ±0.05 | BET | 리튬 이온 반응 면적 |
| **Tap Density** | 2.45 | g/cm3 | ±0.1 | Tap Vol. | 충진 효율 및 에너지 밀도 |

## 3. 입도 분포와 전극 성능의 수리적 상관관계 분석

### 3.1 바이모달(Bi-modal) 배합을 통한 충진 밀도 극대화
큰 입자 사이의 빈 공간을 작은 입자가 채움으로써 전극의 에너지 밀도를 향상시킵니다.
* **실측 현상**: D50이 15um인 대입자와 5um인 소입자를 7:3 비율로 혼합한 결과, 단일 입자 대비 전극 충진 밀도가 12% 향상되어 목표 탭 밀도(2.45 g/cm3)를 달성하는 소재 무결성이 실측되었습니다 [Ref: psd-analysis-log-v2026].

### 3.2 입도 편차($\sigma$)와 슬러리 점도(Viscosity)의 관계
입도 분포가 넓어질수록(Span 증가) 입자 간의 상호작용이 복잡해져 슬러리의 유변 물성이 변합니다.
* **실측 데이터**: PSD Span 지수가 1.8을 초과할 때, 전단 속도(Shear Rate) $100\text{ s}^{-1}$에서의 슬러리 점도가 15% 이상 변동하며 코팅 두께 균일도에 악영향을 미치는 임계점이 탐지되었습니다 [Ref: psd-analysis-log-v2026].

## 4. [Skill] Particle Size Fidelity Auditor

```python
class PSDFidelityHealer:
    """
    HDS-Gold V7.5.3: 활물질 입도 분포 및 충진 무결성 진단 엔진
    Grounded via battery-raw-material-psd-analysis-log-v2026
    """
    def __init__(self, d50, span, tap_density):
        self.d50 = d50 # um
        self.span = span # Ratio
        self.density = tap_density # g/cm3
        self.density_target = 2.40

    def audit_material_quality(self):
        # 탭 밀도 및 입도 분포 기반 소재 무결성 진단
        material_fidelity = (self.density / self.density_target) * (1.0 / self.span)
        
        status = "OPTIMAL"
        if self.density < self.density_target:
            status = "WARNING: Low Packing Density (Check Particle Mixing Ratio)"
        if self.span > 2.0:
            status = "CRITICAL: Broad PSD (Risk of Coating Non-uniformity)"
            
        return {"Material_Fidelity_Index": round(material_fidelity, 4), "Status": status}

# 실측 로그 데이터 적용
engine = PSDFidelityHealer(d50=11.5, span=1.62, tap_density=2.45)
print(f"Material Audit: {engine.audit_material_quality()}")
```

## 5. 공학적 검증 프로토콜 (Audit Checklist)
1. **굴절률(RI) 보정 오딧**: 레이저 회절법 측정 시 소재의 복소 굴절률($n+ik$)이 정확히 적용되었는지 실측 검증.
2. **분산 상태(Dispersion) 확인**: 측정 전 초음파 분산(Sonication) 시간 및 강도에 따른 입도 변화 안정성 테스트.
3. **거대 입자(Coarse) 전수 감리**: D90 이상의 조대 입자가 슬롯 다이 립 갭(Lip Gap)의 50%를 초과하여 줄무늬(Streak) 불량을 유발할 리스크 오딧 [Ref: psd-analysis-log-v2026].

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[MOC] 02_Battery]]
- [[Battery] battery-raw-material-log-v2026]
- [[Battery] slot-die-coating-and-web-handling-physics]

**[V7.5.3_HARDCORE_FIDELITY_VERIFIED]**
**[GROUNDED_VIA: battery-raw-material-psd-analysis-log-v2026]**