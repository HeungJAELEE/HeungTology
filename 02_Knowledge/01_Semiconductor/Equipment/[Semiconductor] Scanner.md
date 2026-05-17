---
metadata:
  date: "2026-05-16"
  id: "[[[Semiconductor] Scanner]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "01_Semiconductor"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "f7d9ff5cb583278d7ebd4caef318a9b63293366e00d23ce77788ab761c77841e"
object:
  object_type: "Concept"
  tier: 1
  description: '[Semiconductor] Scanner에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 반도체_백서_통합_지휘소]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Semiconductor] Scanner

## 1. Functional Objective
고해상도 패턴 전사를 위해 Stepper(Step-and-Repeat)에서 Scanner(Step-and-Scan)로 아키텍처 전이. 유효 개구수(NA) 내 수차(Aberration) 최소화 영역인 중앙 슬릿(Slit)만을 활용, 마스크-웨이퍼 스테이지의 동기화 구동을 통해 노광 면적(Exposure Field) 확장 및 해상도 정밀도 확보 [Ref: Lithography_Core]. 7nm 이하 미세 공정 구현을 위한 EUV(Extreme Ultraviolet) 스캐너는 핵심 전략 자산으로 정의됨 [Ref: EUV_Strategy].

## 2. Technical Specification Comparison

| Feature | Stepper (Legacy) | DUV Scanner | EUV Scanner (Next-Gen) |
|:---|:---:|:---:|:---:|
| **Operation Mode** | Step-and-Repeat | Step-and-Scan | Step-and-Scan (Vacuum) |
| **Exposure Field** | Lens-limited | Large (Scanning) | Optimized (Reflective) |
| **Overlay Accuracy** | $\sim 10 \text{ nm}$ [Ref: Legacy_Doc] | $< 2 \text{ nm}$ [Ref: DUV_Standard] | $< 1 \text{ nm}$ [Ref: EUV_Spec] |
| **Scanning Speed** | N/A | $600 \sim 800 \text{ mm/s}$ [Ref: DUV_Manual] | $1000 \text{ mm/s+}$ [Ref: EUV_Perf] |
| **Wavelength ($\lambda$)** | i-line / KrF | ArF / ArF-i | $13.5 \text{ nm}$ [Ref: EUV_Physics] |

## 3. Comparative Analysis: Theoretical vs. Verified

| Parameter | Theoretical Value | Verified Value | Discrepancy Driver |
|:---|:---|:---|:---|
| **Stage Velocity Sync** | $V_{mask} = M \times V_{wafer}$ | $\Delta V \approx \pm 0.05\%$ [Ref: Stage_Audit] | Laser Interferometry Jitter |
| **EUV Reflectivity** | $R \approx 1.0$ (Ideal) | $R \approx 0.7$ per Mirror [Ref: EUV_Optics] | Multi-layer absorption loss |
| **Overlay Offset** | $0.00 \text{ nm}$ | $< 1 \text{ nm}$ [Ref: ASML_Spec] | Thermal expansion & Vibration |

## 4. Engineering Rationale

### 4.1 Step-and-Scan Kinematics
렌즈 중심부 광학 최적 영역(Slit) 기반 노광 수행. 마스크-웨이퍼 스테이지는 축소 배율($M$)에 따라 상호 반대 방향으로 동기화 이동 필수.
- **Kinematic Equation**: $V_{mask} = M \times V_{wafer}$ [Ref: Lithography_Mechatronics]
- **Control Requirement**: 자기 부상(Maglev) 스테이지 및 레이저 간섭계(Laser Interferometer)를 통한 나노미터 단위 가속도/위치 제어 [Ref: Stage_Control_Spec].

### 4.2 EUV Optical Constraints
EUV($\lambda = 13.5 \text{ nm}$ [Ref: EUV_Physics]) 광원의 고흡수 특성에 따른 광학계 설계 변경.
- **Optical Path**: 굴절 렌즈 사용 불가 $\rightarrow$ Multi-layer Reflective Mirror 시스템 채택 [Ref: EUV_Physics].
- **Environment**: 광학계 내 산란 방지 및 광자 흡수 최소화를 위한 진공(Vacuum) 상태 유지 필수 [Ref: EUV_Standard].

## 5. Control Logic (Overlay Error Correction)

패턴 정렬 오차(Overlay Error) 보정을 위한 PID 및 고차 다항식 기반 제어 알고리즘.

```python
# Scanner Overlay Correction Logic (V7.5.3 Optimized)
def calculate_scanner_offsets(metrology_data):
    """
    Analyzes alignment error and calculates stage bias.
    :param metrology_data: Input from metrology sensor (dx, dy, theta, temp)
    """
    # 1. Extraction of alignment error from previous layer
    dx, dy = extract_alignment_error(metrology_data)
    
    # 2. Calculation of Stage Bias using PID gains
    # Target: Compensation of X, Y positional error
    correction_x = -dx * PID_GAIN_X
    correction_y = -dy * PID_GAIN_Y
    
    # 3. Transmission of compensation values to Scanner Controller
    scanner_controller.apply_stage_bias(correction_x, correction_y)
    
    # 4. High-order Wafer Distortion Compensation
    # Compensates for wafer expansion due to thermal gradients
    apply_wafer_expansion_compensation(metrology_data.temperature)
```

## 6. Self-Audit Checklist
1. **Structural Advantage**: Scanner의 Slit 기반 노광이 Stepper 대비 대면적 노광 및 저수차 구현에 유리한 광학적 메커니즘을 정의하였는가?
2. **Kinematic Impact**: 스테이지 동기화 오차($\Delta V \approx \pm 0.05\%$ [Ref: Stage_Audit])가 CD 및 Overlay에 미치는 물리적 영향이 정량화되었는가?
3. **Optical Necessity**: EUV 흡수 특성에 따른 Refractive $\rightarrow$ Reflective 광학계 전환 및 Vacuum 환경의 필연성이 명시되었는가?
