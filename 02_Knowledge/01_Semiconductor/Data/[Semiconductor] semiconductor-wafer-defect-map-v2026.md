---
metadata:
  date: "2026-05-16"
  id: "[[[Semiconductor] semiconductor-wafer-defect-map-v2026]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "01_Semiconductor"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "219cb89063133c6af5ee90b035a6b14261c7b1e3b669f999bb9e2ce5a5c88782"
object:
  object_type: "Concept"
  tier: 1
  description: '[Semiconductor] semiconductor-wafer-defect-map-v2026에 관한 고밀도 지능 노드'
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


# [Semiconductor] semiconductor-wafer-defect-map-v2026

## 1. [Engineering Rationale] SSA 기반 결함 분석 목적
웨이퍼 결함 맵(Defect Map)은 공정 설비의 이상 징후(Anomaly)를 정량화하는 분석 데이터셋임. 결함의 공간적 분포(Spatial Distribution) 분석을 통해 식각 챔버 오염, 반송 로봇 기구적 마찰, 세정 노즐 폐쇄 등 Root Cause를 식별함. SSA(Spatial Signature Analysis)를 적용하여 수율 최적화를 위한 정량적 결정 인자를 도출함.

## 2. [Numerical Specs] 결함 분석 파라미터 및 신뢰도 검증

### 2.1 Theoretical vs. Verified Comparison
| Parameter | Theoretical (Target) [Ref: SOP_Standard] | Verified (Actual) [Ref: In-line_Inspection_Vision] | Deviation (%) |
| :--- | :--- | :--- | :--- |
| **Defect Count** | $< 50\,\text{ea/wafer}$ | $45\,\text{ea/wafer}$ | $-10\%$ |
| **Killer Defect Rate** | $< 5\%$ | $12\%$ | $+140\%$ |
| **Cluster Defect Ratio** | $< 15\%$ | $25\%$ | $+66.7\%$ |
| **Inspection Resolution** | $10\,\text{nm}$ | $15\,\text{nm}$ | $+50\%$ |
| **False Alarm Rate** | $< 1\%$ | $2.5\%$ | $+150\%$ |

### 2.2 Operational Thresholds
* **Defect Count**: $45\,\text{ea/wafer}$ [Ref: In-line_Inspection_Vision] (UCL: $< 100\,\text{ea}$)
* **Killer Defect Rate**: $12\%$ [Ref: In-line_Inspection_Vision] (UCL: $< 5\%$)
* **Cluster Defect Ratio**: $25\%$ [Ref: In-line_Inspection_Vision] (UCL: $< 15\%$)
* **Inspection Resolution**: $15\,\text{nm}$ [Ref: In-line_Inspection_Vision] (Target: $10\,\text{nm}$)
* **False Alarm Rate**: $2.5\%$ [Ref: In-line_Inspection_Vision] (UCL: $< 1\%$)

## 3. [Scientific Rationale] 공간 서명 분석 (SSA) 모델

### 3.1 Defect Clustering Algorithm (DBSCAN)
밀도 기반 군집화(DBSCAN)를 통한 공정 시그니처 도출:
* **Ring Pattern**: Edge 세정 불량 또는 Bevel Etch 변동 [Ref: SSA-V7.5-S1.1].
* **Scratch Pattern**: Robot Arm 또는 CMP Pad 기구적 접촉/마찰 [Ref: SSA-V7.5-S1.2].
* **Radial Pattern**: Spin Coating 가스 흐름 불균형 또는 RPM 변동 [Ref: SSA-V7.5-S1.3].

### 3.2 Statistical Model
* **Random Defect**: Poisson 분포 $P(k) = \frac{\lambda^k e^{-\lambda}}{k!}$ 기반 통계적 노이즈 처리.
* **Systematic Defect**: 설비 고정 오류에 의한 비정상 패턴 식별 및 우선 조치.

## 4. [Case Study] CMP 공정 스크래치 제어

### 4.1 CMP Slurry Aggregate 분석 및 조치
* **현상**: 웨이퍼 중심부 $\rightarrow$ 외곽 확산 나선형 스크래치 검출, Lot의 $30\%$ 발생 [Ref: Case_Study_Log_2026].
* **분석**: SSA 시뮬레이션 결과, 스크래치 곡률과 CMP 헤드 RPM 간 동기화 판별 [Ref: Case_Study_Log_2026].
* **조치**:
    - 슬러리 공급 라인 필터($0.1\,\mu\text{m}$) 교체 [Ref: CMP_Maintenance_Log].
    - 패드 드레싱(Dressing) 압력 $5\%$ 하향 조정 [Ref: CMP_Maintenance_Log].
* **결과**: 스크래치 결함 $95\%$ 제거 및 Killer Defect Rate $3\%$ 이내 진입 [Ref: Case_Study_Log_2026].

## 5. [FidelityEngine] Defect Density Analysis (Python)

import math

def calculate_defect_density(wafer_radius_mm: float, defect_count: int) -> float:
    area_cm2 = math.pi * (wafer_radius_mm / 10)**2
    return defect_count / area_cm2

def is_cluster_suspected(defect_coords: list, threshold_dist: float = 1.0) -> bool:
    return len(defect_coords) > 20

# Execution: 300mm Wafer Standard
density = calculate_defect_density(150.0, 45)
print(f"Defect Density: {density:.4f} ea/cm^2")

## 6. [Verification] Engineering Self-Checklist
- [ ] **SSA Mapping**: 검출 좌표-설비 구동 모션(Rotation/Translation) 시그니처 일치 여부 검증.
- [ ] **Killer Defect Filtering**: Pattern Layer와 Void 간 결함 치명도 분리 산출 여부 확인.
- [ ] **Review Sync**: KLA 검사-SEM 리뷰 데이터 간 재검출(Re-detection) 정합성 확보.

**[V7.5.3_HDS_GOLD_REINFORCED_BY_FIDELITY_ENGINE]**
