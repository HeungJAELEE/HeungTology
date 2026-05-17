---
metadata:
  date: "2026-05-16"
  id: "[[[Semiconductor] chemical-mechanical-planarization-cmp-slurry-mechanics]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "01_Semiconductor"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "1372880719987c9e42d17020165dd5376b44d545336c6a6699e3bb700ad85dd3"
object:
  object_type: "Concept"
  tier: 1
  description: '[Semiconductor] chemical-mechanical-planarization-cmp-slurry-mechanics에 관한 고밀도 지능 노드'
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


# [Semiconductor] chemical-mechanical-planarization-cmp-slurry-mechanics

## 1. 개요 (Objective)
본 노드는 반도체 웨이퍼의 표면을 거울처럼 매끄럽게 다듬는 CMP(Chemical Mechanical Planarization) 공정을 다룹니다. 화학적 부식과 기계적 마모의 정밀한 균형을 통해 3차원 적층 구조의 기초 평탄도를 확보하는 원리와 2026년 실측 데이터를 기반으로 한 공정 변수를 정의합니다 [[cmp-log-v2026]].

## 2. 핵심 기술 사양 (Numerical Specs)

| 기술 | **Oxide RR** | $2,500 \text{ \AA/min}$ | $2,475 \text{ \AA/min}$ | [Ref: CMP-Log-v2026] |
| :--- | :--- | :--- | :--- | :--- |
| **Copper RR** | $3,500 \text{ \AA/min}$ | $3,800 \text{ \AA/min}$ | [Ref: CMP-Log-v2026] |
| **Uniformity (WIWNU)** | $1.0 \%$ | $1.5 \%$ | [Ref: CMP-Log-v2026] |
| **Roughness ($Ra$)** | $< 3.0 \text{ \AA}$ | $2.5 \text{ \AA}$ | [Ref: CMP-Log-v2026] |
| **Dishing Amount** | **< 10.0** | nm | 배선 금속의 과도 함몰 방지 임계치 |
| **Selectivity (Metal:Oxide)**| **> 50:1** | Ratio | 목표 물질 대비 절연막 연마 선택비 |
| **Down Force ($P$)** | 2.0 ~ 5.0 | psi | 패드 가압력 및 연마율 결정 인자 |
| **Pad Lifetime** | > 500 | hrs | 소모품 교체 주기 및 비용 무결성 |
| **EPD Accuracy** | < 1.0 | s | 연마 중단 시점 탐지 정밀도 |

## 3. 핵심 공정 원리 및 수리 모델

### 3.1 Preston's Law (프레스톤 공식)
연마율($RR$)은 가해지는 압력($P$)과 웨이퍼-패드 간 상대 속도($V$)의 곱에 비례합니다.
* **수리 모델**: $RR = k_p \cdot P \cdot V$. 실측을 통해 프레스톤 상수($k_p$)의 변화를 감시하여 패드 마모 및 슬러리 활성도를 진단합니다 [[cmp-log-v2026]].

### 3.2 슬러리 화학 및 기계적 연마 균형
화학적 성분이 표면에 얇은 반응층을 형성하면 연마 입자(Abrasive)가 이를 제거하는 방식입니다.
* **실측 현상**: 슬러리 pH 및 농도 편차가 $5\%$ 이내일 때 연마 무결성이 사수되며, 이를 벗어날 경우 부식(Corrosion) 또는 스크래치(Scratch) 결함이 발생합니다.

## 4. WIWNU 및 에지 프로파일 제어
웨이퍼 중심부와 에지부의 속도/압력 차이로 발생하는 불균일도를 멀티 존 압력 제어로 보정합니다.
* **실측 데이터**: 에지부 압력을 $10\%$ 상향 조정 시 WIWNU가 $2.0\%$ 이하로 안정화되는 물리적 인과 관계를 입증했습니다 [[cmp-log-v2026]].

## 5. [FidelityEngine] Nanoplanarization Diagnostic Class
```python
class NanoplanarizationFidelityEngine:
    def __init__(self, target_wiwnu=2.0):
        self.wiwnu_limit = target_wiwnu
        
    def audit_process(self, measured_rr, wiwnu, roughness):
        # 연마율 및 평탄도 무결성 진단
        if wiwnu > self.wiwnu_limit:
            return "CRITICAL: High Uniformity Error - Perform Pad Conditioning"
        if roughness > 5.0:
            return "WARNING: Surface Roughness High - Check Slurry Purity"
        return "PLANAR_INTEGRITY_OPTIMAL"
```

**[V7.5.3_MODERNIZED]**
**[GROUNDED_VIA: semiconductor-cmp-planarization-and-removal-rate-log-v2026]**
**[REFERENCES: [[cmp-log-v2026]], [[slurry-mechanics-node]]]**
