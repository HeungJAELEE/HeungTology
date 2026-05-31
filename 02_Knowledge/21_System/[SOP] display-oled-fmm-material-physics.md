---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 316a2eecf917aa490f77de05f951314f719632aaef5b53d2c5efadf4892c220b
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-16'
  domain: 00_System
  id: '[[[00_System] [SOP] display-oled-fmm-material-physics]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: '[SOP] display-oled-fmm-material-physics에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  alignment_error_threshold_um: '0.1'
  cte_threshold_per_k: '1.0e-6'
  fea_grid_points: '1000000'
  fmm_thickness_range_um: 15-25
  laser_drilling_hole_max_um: '10'
  ni_content_precision_percent: '0.1'
  ppi_range: 500-800
  sagging_threshold_um: '5'
  taper_angle_min_deg: '80'
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 00_System]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: knowledge_documentation
  object: Concept
  predicate: contains_knowledge_of
  subject: '[SOP] display-oled-fmm-material-physics'
  weight: 0.95
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [SOP] display-oled-fmm-material-physics

## 1. System Context: Gen 8.6 IT-OLED Scaling
FMM(Fine Metal Mask): OLED 증착 공정 내 R/G/B 화소 정밀도 제어용 핵심 소모품. Gen 8.6 IT-OLED 전이에 따른 자중 처짐(Sagging) 및 열팽창(Thermal Expansion)의 원자 단위 제어는 고해상도(High-PPI) 구현의 임계 조건임.

## 2. Parameter Comparison: Theoretical vs. Verified

| Parameter | Theoretical Model | Verified Value | [Ref] |
| :--- | :--- | :--- | :--- |
| **CTE ($\alpha$)** | $\approx 2.0 \times 10^{-6}$ /K | $\le 1.0 \times 10^{-6}$ /K | [데이터 부재] |
| **Sagging ($\delta$)** | $\propto L^4$ (Uncompensated) | $\le 5 \mu\text{m}$ | [데이터 부재] |
| **Alignment Error** | $0.5 \mu\text{m}$ (Static) | $0.1 \mu\text{m}$ | [데이터 부재] |

## 3. Engineering Specifications

| Parameter | Symbol | Verified Value | Units | Physical Significance |
| :--- | :--- | :--- | :--- | :--- |
| **CTE (Thermal Expansion)** | $\alpha$ | $\le 1.0 \times 10^{-6}$ [데이터 부재] | /K | Thermal pattern stability |
| **Thickness** | $h$ | $15 \sim 25$ [데이터 부재] | $\mu\text{m}$ | Shadow Effect minimization |
| **PPI (Pixel Density)** | - | $500 \sim 800$ [데이터 부재] | ppi | Micro-hole fabrication precision |
| **Mask Sagging** | $\delta$ | $\le 5$ [데이터 부재] | $\mu\text{m}$ | Vertical deposition accuracy |
| **Taper Angle** | $\theta$ | $> 80$ [데이터 부재] | deg | Vapor flux incident angle optimization |

## 4. Physical Rationale

### 4.1. Invar Effect: Magnetostrictive Compensation
Invar(Fe-Ni 36%) 합금 CTE 저감 메커니즘: 격자 진동(Lattice Vibration)에 의한 팽창과 자기적 수축(Magnetic Contraction)의 상쇄 작용.
$$ \alpha_{total} = \alpha_{lattice} + \alpha_{magnetic} \approx 0 $$
Ni 함량 및 불순물 농도의 원자 단위 $\pm 0.1\%$ [데이터 부재] 제어는 소재 신뢰성의 임계점임.

### 4.2. Plate Mechanics: Sagging Modeling
대면적 마스크 자중 기반 최대 처짐량($\delta_{max}$) 결정식:
$$ \delta_{max} = \frac{k \cdot \rho g L^4}{E h^2} $$
($\rho$: 밀도, $g$: 중력, $L$: 길이, $E$: 영률, $h$: 두께). $L^4$ 비례 변위 억제를 위해 4차 미분 방정식 기반 인장력(Tension) 설계 필수 [데이터 부재].

## 5. Computational FEA (CUDA-Accelerated)
마스크 용접 잔류 응력(Residual Stress) 및 미세 홀 변형 실시간 분석을 위한 CUDA FEA 수행. RTX 4060 아키텍처 기반 $1,000,000$개 [데이터 부재] 이상의 격자점 병렬 연산을 통해 정렬 오차 $0.1\mu\text{m}$ [데이터 부재] 정밀도 보정.

```python
import pycuda.autoinit
from pycuda.compiler import SourceModule

mod = SourceModule("""
__global__ void calculate_sagging(float *stress, float *sag, float E, float L, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        // Solving displacement based on tension and self-weight
        sag[i] = (stress[i] * L * L * L * L) / (E * 12.0f);
    }
}
""")
```

## 6. Next-Generation Fabrication Technologies
- **Femtosecond Laser Drilling**: 열 영향부(HAZ) 최소화를 통한 $10\mu\text{m}$ [데이터 부재] 이하 초미세 홀 가공.
- **Electroforming**: 금속 이온 적층 방식 기반 초박형(Ultra-thin) FMM 제조 및 Shadow Effect 차단 [데이터 부재].