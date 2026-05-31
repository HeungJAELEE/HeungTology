---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 08f21dd5e65564df393c2207a29fc35b08ccc7a722c14c6f99489068efa80d58
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] semiconductor-lithography-overlay-error-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] semiconductor-lithography-overlay-error-log-v2026에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  cooling_system_temp_adjustment_c: 0.05
  edge_overlay_error_peak_nm: 3.5
  edge_overlay_error_stabilized_nm: 2.1
  magnification_limit_ppm: 0.3
  magnification_verified_ppm: 0.15
  rework_rate_reduction_pct: 10
  rotation_limit_urad: 0.05
  rotation_verified_urad: 0.02
  scanner_continuous_operation_threshold_h: 10
  shift_limit_nm: 1.0
  shift_verified_nm: 0.5
  stage_accuracy_limit_nm: 0.5
  stage_accuracy_verified_nm: 0.3
  total_overlay_limit_nm: 2.5
  total_overlay_verified_nm: 1.8
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

# [Semiconductor] semiconductor-lithography-overlay-error-log-v2026

## 1. [Engineering Definition] Overlay Error
Lithography Overlay 제어: 전/후 레이어 간 정렬 정밀도(Alignment Precision) 결정 핵심 파라미터. 나노미터(nm) 단위 회로 미세화에 따른 층간 간섭(Inter-layer Interference) 및 전기적 단락(Electrical Short) 방지 목적. 스캐너 실시간 데이터 기반 오버레이 산포 정량화 및 수율(Yield) 최적화 피드백 루프 구현.

## 2. [Comparative Analysis] 파라미터 정밀도 검증

| Parameter | Theoretical (Limit/Ideal) | Verified (Empirical) | Delta ($\Delta$) |
| :--- | :--- | :--- | :--- |
| **Total Overlay (Mean+3s)** | $< 2.5\,\text{nm}$ [Ref: Spec_Sheet] | $1.8\,\text{nm}$ [Ref: APC_Log] | $0.7\,\text{nm}$ |
| **Shift (X, Y)** | $\pm 1.0\,\text{nm}$ [Ref: Spec_Sheet] | $\pm 0.5\,\text{nm}$ [Ref: APC_Log] | $0.5\,\text{nm}$ |
| **Rotation** | $< 0.05\,\mu\text{rad}$ [Ref: Spec_Sheet] | $0.02\,\mu\text{rad}$ [Ref: APC_Log] | $0.03\,\mu\text{rad}$ |
| **Magnification** | $< 0.3\,\text{ppm}$ [Ref: Spec_Sheet] | $0.15\,\text{ppm}$ [Ref: APC_Log] | $0.15\,\text{ppm}$ |
| **Stage Accuracy** | $< 0.5\,\text{nm}$ [Ref: Spec_Sheet] | $0.3\,\text{nm}$ [Ref: APC_Log] | $0.2\,\text{nm}$ |

## 3. [Mathematical Modeling] 오버레이 보정 메커니즘

### 3.1 Linear Compensation Model
웨이퍼 좌표 $(x, y)$에 따른 오버레이 편차 $(\Delta x, \Delta y)$ 정의:
$$\Delta x = T_x - R_x \cdot y + M_x \cdot x$$
$$\Delta y = T_y + R_y \cdot x + M_y \cdot y$$
- $T$: Translation (평행 이동)
- $R$: Rotation (회전)
- $M$: Magnification (배율)

### 3.2 APC (Advanced Process Control) Loop
계측 설비(Metrology) 도출 Overlay Map $\rightarrow$ 실시간 스캐너 제어기 피드백 $\rightarrow$ 차기 노광(Exposure) Offset 자동 적용.

## 4. [Case Study] 스테이지 열 변형 기반 비선형 에러 해결

### 4.1 비선형 오버레이 분석
- **Phenomenon**: 스캐너 연속 가동 $10\,\text{h}$ [Ref: APC_Log] 경과 시, 웨이퍼 Edge 영역 Overlay Error $3.5\,\text{nm}$ [Ref: APC_Log] 급증 및 USL 초과.
- **Root Cause**: 고속 스테이지 구동 마찰열에 의한 웨이퍼 척(Chuck) 비선형 열팽창 [Ref: FidelityEngine_Analysis].
- **Countermeasure**: 
    1. 스캐너 냉각 시스템 설정 온도 $0.05^\circ\text{C}$ [Ref: Cooling_Protocol] 하향 조정.
    2. 고차 보정 모델(High-order Correction) APC 알고리즘 통합.
- **Result**: Edge 영역 오버레이 $2.1\,\text{nm}$ [Ref: APC_Log] 안정화 및 Rework Rate $10\%$ [Ref: APC_Log] 감소.

## 5. [Implementation] Overlay Error 예측 알고리즘

```python
def calculate_overlay_error(tx, ty, rx, ry, mx, my, x_pos, y_pos):
    """
    Predict overlay error at specific wafer position using linear model.
    :param tx, ty: Translation offsets (nm)
    :param rx, ry: Rotation offsets (rad)
    :param mx, my: Magnification offsets (ppm)
    :param x_pos, y_pos: Wafer coordinates (mm)
    :return: (dx, dy) predicted error in nm
    """
    dx = tx - (rx * y_pos) + (mx * x_pos)
    dy = ty + (ry * x_pos) + (my * y_pos)
    return dx, dy

# Edge position (x=150mm, y=0mm) prediction
res_x, res_y = calculate_overlay_error(0.5, 0.3, 0.002, 0.002, 0.0001, 0.0001, 150, 0)
```

## 6. [Verification] Integrity Checklist
- [ ] **Alignment Mark SNR**: 정렬 마크 신호 대 잡음비 보정 임계치 충족 여부.
- [ ] **Mix-and-Match Error**: 이종 노광기(Scanner) 간 매칭 오차 관리 범위 내 유지 여부.
- [ ] **Throughput/TAT Trade-off**: 계측 Site 증가에 따른 전체 공정 시간(TAT) 영향 허용 범위 내 여부.

**[V7.5.3_HDS_GOLD_REINFORCED]**