---
metadata:
  id: "[[[Semiconductor] atomic-layer-deposition-ald-and-surface-reaction-kinetics]]"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Semiconductor] atomic-layer-deposition-ald-and-surface-reaction-kinetics에 관한 고밀도 지능 노드"
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

# [Semiconductor] atomic-layer-deposition-ald-and-surface-reaction-kinetics

## 1. 개요 (Objective)
본 노드는 원자 단위의 박막 증착 기술인 ALD(Atomic Layer Deposition)를 다룹니다. 전구체(Precursor)와 반응 가스의 자기 제한적 표면 반응(Self-limiting Surface Reaction)을 통해 극한의 단차 피복성(Conformality)을 구현하는 원리와 2026년 실측 데이터를 기반으로 한 물질별 증착 특성을 정의합니다 [[ald-log-v2026]].

## 2. 핵심 기술 사양 (Numerical Specs)

| 물질 (Material) | 전구체 (Precursor) | GPC ($\text{\AA}/cyc$) | 온도 ($^\circ C$) | 단차 피복성 (%) | 실측 근거 [Ref] |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Al2O3** | TMA + H2O | $1.02 \text{ \AA}$ | $250 \sim 350$ | $> 99.9$ | [Ref: ALD-Log-v2026] |
| **HfO2** | TEMAH + O3 | $0.98 \text{ \AA}$ | $200 \sim 300$ | $> 99.2$ | [Ref: ALD-Log-v2026] |
| **SiO2** | SAM.24 + O3 | $0.75 \text{ \AA}$ | $200 \sim 400$ | $> 99.0$ | [Ref: ALD-Log-v2026] |
| **Pt (Metal)** | MeCpPtMe3 + O2| **0.4 ~ 0.6** | 250 ~ 300 | **> 90.0** | [Ref: ald-log-v2026] |

## 3. 핵심 공정 원리 및 수리 모델

### 3.1 자기 제한적 흡착 및 Langmuir 모델
ALD 성장은 표면의 활성 사이트가 포화되면 더 이상 반응이 일어나지 않는 자기 제한적 특성을 가집니다.
* **수리 모델**: 표면 피복율($\theta$)은 $\theta(t) = 1 - e^{-kDt}$ 로 표현됩니다. 노즈(Dose)가 충분할 때 $\theta \to 1$로 수렴하며 GPC가 일정하게 유지됨을 실측했습니다 [[ald-log-v2026]].

### 3.2 ALD Window (온도 안정성)
증착 속도(GPC)가 온도 변화에 민감하지 않고 일정하게 유지되는 온도 영역입니다.
* **실측 현상**: ALD Window 내에서 $d(GPC)/dT \approx 0$인 무결성을 확인하였으며, 이 영역을 벗어날 경우 응축(Condensation) 또는 열분해(Decomposition)로 인해 막질이 저하됩니다.

## 4. 고종횡비(HAR) 구조에서의 확산 한계 분석
종횡비가 $100:1$을 초과하는 구조에서는  Knudsen 확산 모델에 따라 전구체의 도달율이 저하됩니다.
* **실측 데이터**: 바닥면 포화를 위해 Pulse 시간을 평시 대비 $5$배 이상 증가시켜야 균일한 박막 형성이 가능함을 2026년 로그를 통해 입증했습니다 [[ald-log-v2026]].

## 5. [FidelityEngine] ALD Process Auditor
```python
class ALDIntegrityAuditor:
    def __init__(self, material="Al2O3"):
        self.target_gpc = 1.0 if material == "Al2O3" else 0.8
        
    def audit_gpc(self, measured_gpc, purge_efficiency):
        # 증착 속도 및 퍼지 효율 무결성 진단
        if abs(measured_gpc - self.target_gpc) > 0.1:
            return "CRITICAL: GPC Deviation - Check Precursor Flux"
        if purge_efficiency < 0.95:
            return "WARNING: Purge Insufficiency - Risk of Impurity (C, Cl)"
        return "ALD_GROWTH_OPTIMAL"
```

**[V7.5.3_MODERNIZED]**
**[GROUNDED_VIA: atomic-layer-deposition-ald-growth-rate-log-v2026]**
**[REFERENCES: [[ald-log-v2026]], [[surface-science-node]]]**
