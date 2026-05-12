---
Basic:
  id: "[[[Semiconductor] Stepper"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
  is_part_of: []]
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
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [[[Semiconductor] Stepper

## 1. [왜 배우는가? (Why)]]
스캐너가 미세 공정의 첨단을 달린다면, 스테퍼는 노광 공정의 '전통적 강자'이자 디스플레이(TFT-LCD/OLED) 및 아날로그 반도체 제조의 핵심 장비입니다. 웨이퍼의 한 영역(Shot)을 찍고 다음 칸으로 이동(Step)하여 다시 찍는 Step-and-repeat 방식은 공정 제어가 상대적으로 단순하면서도 높은 신뢰성을 제공합니다. 최신 스캐너 기술의 근간이 되는 광학적 원리와 렌즈 제어 로직을 이해하기 위한 필수 노드입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | G-line Stepper | i-line Stepper | KrF Stepper |
|:---|:---:|:---:|:---:|
| **Wavelength ($\lambda$)** | 436 nm | 365 nm | 248 nm |
| **Exposure Method** | Full-Field (Single Shot) | Full-Field | Full-Field |
| **Max Field Size** | ~22 x 22 mm | ~26 x 26 mm | ~26 x 33 mm |
| **Resolution ($R$)** | ~0.5 $\mu$m | ~0.35 $\mu$m | ~0.15 $\mu$m |
| **Alignment Accuracy** | ~100 nm | ~50 nm | ~30 nm |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 Step-and-Repeat 논리
스테퍼는 마스크 전체의 이미지를 렌즈를 통해 축소 투영하여 웨이퍼의 특정 영역에 한 번에 노광합니다.
- **로직**: 전체 웨이퍼를 한 번에 노광하는 방식(Aligner)보다 렌즈의 유효 면적을 작게 유지하면서도 정밀도를 높일 수 있습니다. 한 샷이 끝나면 정해진 거리만큼 'Step' 이동하여 동일한 과정을 반복함으로써 웨이퍼 전체에 패턴을 형성합니다.

### 3.2 렌즈 수차 (Lens Aberration)와 해상도
스테퍼의 성능은 렌즈의 품질에 의해 결정됩니다.
- **문제**: 렌즈의 가장자리로 갈수록 빛의 경로가 왜곡되는 수차(Spherical, Coma, Astigmatism 등)가 발생하여 패턴의 선명도가 떨어집니다.
- **수식**: $ R = k_1 \times \frac{\lambda}{NA} $ (Rayleigh Criterion). 스테퍼는 $ NA $(개구수)를 키우기 위해 거대한 렌즈 뭉치를 사용하며, 수차를 최소화하기 위해 수십 장의 정밀 렌즈를 조합합니다.

### 3.3 활용 분야의 분화
초미세 공정은 스캐너가 담당하지만, 층수가 많고 선폭이 상대적으로 넓은 패키징 공정이나 디스플레이 패널 제조에서는 가성비와 안정성이 높은 스테퍼가 여전히 주력으로 사용됩니다.

## 4. [코드 연결 해설 (Wafer Map & Tiling)]
웨이퍼 상의 샷(Shot) 배치와 노광 순서를 결정하는 타일링 알고리즘입니다.
```python
# 스테퍼 샷 배치 및 경로 최적화 (Wafer Tiling)
def generate_wafer_exposure_map(die_size, wafer_diameter):
    # 웨이퍼 영역 내에 배치 가능한 최대 Die 개수 계산
    shot_coordinates = calculate_grid_positions(die_size, wafer_diameter)
    
    # 이동 거리를 최소화하기 위한 지그재그(Serpentine) 경로 생성
    path = optimize_stepping_path(shot_coordinates, mode="Serpentine")
    
    for x, y in path:
        move_to_stage(x, y)
        verify_alignment(mark_type="Global")
        trigger_shutter(exposure_time=250) # msec 단위 정밀 제어
```

## 5. [스스로 체크 (Self-Audit)]
1. 스테퍼의 Step-and-repeat 방식이 스캐너의 Step-and-scan 방식 대비 가지는 구조적 한계는 무엇인가?
2. 렌즈 수차가 노광된 패턴의 CD Uniformity(선폭 균일도)에 미치는 영향은?
3. 최신 스택킹(Stacking) 공정에서 하단부는 스테퍼, 상단부는 스캐너를 섞어 쓰는 'Mix-and-Match' 전략의 경제적 근거는?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
