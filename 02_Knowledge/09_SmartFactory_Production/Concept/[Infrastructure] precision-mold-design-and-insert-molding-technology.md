---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: d34f571c2f2386390fb84b913ac3719a81f0adb30082402f23423b5ea63eec0d
metadata:
  date: '2026-05-16'
  domain: 09_SmartFactory_Production
  id: '[[[Infrastructure] precision-mold-design-and-insert-molding-technology]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Infrastructure] precision-mold-design-and-insert-molding-technology에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  expansion_gap_cold_hot_offset_um: 5.0
  fit_tolerance_um_default: 5
  insert_bonding_interface_strength_mpa: 30
  mold_tolerance_core_cavity_fit_um: 2.0
  slider_stroke_motion_accuracy_mm: 0.01
  steel_cte_default: 1.2e-05
  steel_hardness_hrc_max: 55
  steel_hardness_hrc_min: 52
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]'
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

# [Infrastructure] precision-mold-design-and-insert-molding-technology

## 1. [왜 배우는가? (Why: The Mastery of Tooling Integrity Sovereignty)]
초정밀 플라스틱 부품은 강철로 만들어진 금형의 미세한 움직임과 기하학적 정밀도에 의해 그 운명이 결정됩니다. **Precision Mold Design and Insert Technology**는 가혹한 압력과 열기 속에서도 나노 단위의 치수 공차를 유지하는 금형 가동 구조(Slider, Lifter)와 이종 재료(Metal + Plastic)의 물리적 결합을 지배하는 **'제조의 하드웨어 사령탑(Tooling Core)'**입니다. V6.3.7 지능은 **금형 열팽창**에 따른 동적 정합과 **인서트 성형**의 계면 결합 에너지를 수리적으로 지배합니다. 우리가 이를 배우는 이유는 언더컷(Undercut)을 완벽히 해소하고 복합 기능을 일체화하여, "강철의 육체에 데이터의 영혼을 불어넣는 '정밀 조형 주권'을 확보하기" 위함입니다.

## 2. [금형 설계 및 인서트 핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Focus Metric | Tier 0 Requirement (V6.3.7) | Rationale |
|:---|:---|:---:|:---|
| **Mold Tolerance** | Core/Cavity Fit | $<\pm 2.0 \mu\text{m}$ | 수지 누출(Flash) 방지 및 치수 무결성 사수 |
| **Slider Stroke** | Motion Accuracy | $\pm 0.01 \text{ mm}$ | 언더컷 취출 정밀도 및 작동 주권 확보 |
| **Insert Bonding** | Interface Strength| $> 30 \text{ MPa}$ | 이종 재료 간 박리 방지 및 신뢰 무결성 |
| **Expansion Gap** | Cold/Hot Offset | $\pm 5.0 \mu\text{m}$ | 가동 시 고착(Seizure) 방지 및 기계 무결성 |
| **Steel Hardness** | Cavity State | $52 \sim 55 \text{ HRC}$ | 내마모성 확보 및 금형 수명 주권 사수 |

### 2.1 [금형 열동역학 및 인서트 계면 수리 모델]
금형 온도($T$) 변화에 따른 부품 간 간극 변화와 인서트 결합 시의 열적 수축 응력($\sigma_{shrink}$)을 산출하는 기전입니다.
$$ \Delta G = (L_1 \alpha_1 - L_2 \alpha_2) \cdot \Delta T $$
$$ \sigma_{shrink} = E_{poly} \cdot \int_{T_{mold}}^{T_{melt}} \alpha_{poly}(T) dT $$
*   **공학적 근거**: 금형은 상온에서 제작되지만 100°C 이상의 고온에서 가동됩니다. 서로 다른 강재(예: NAK80 vs DH31) 간의 열팽창 계수($\alpha$) 차이는 가동부의 정합 무결성을 파괴할 수 있습니다. 인서트 성형 시 플라스틱이 금속을 감싸며 수축할 때 발생하는 응력($\sigma_{shrink}$)은 이종 재료 간의 기계적 체결력(Mechanical Interlocking)을 형성하는 핵심 기전입니다.
*   **FidelityEngine 적용**: FidelityEngine은 가동부의 마찰 토크를 분석하여 **'기구학적 실질 무결성'**을 진단합니다.

## 3. [공학적 근거: FidelityEngine Tooling Intelligence Logic]

### 3.1 Kinematic Physics: Slider/Lifter Alignment Audit
언더컷 처리를 위한 가동 부품들의 위치 정밀도와 작동 간섭을 오딧하는 기전입니다.
*   **공학적 근거**: 슬라이더가 닫힐 때 $10\mu\text{m}$의 오차만 있어도 파팅 라인이 어긋나 불량이 발생합니다. 각 부품의 기하학적 구속 조건과 가이드 핀의 마모도가 핵심입니다.
*   **FidelityEngine 적용 (Alignment Auditor)**: FidelityEngine은 형체력(Clamping Force)의 편차를 오딧합니다. 특정 구역에 압력이 집중되면 이를 **'금형 정렬 주권 침해'**로 식별하고 가이드 부시(Bush)의 교체 또는 수평도 보정을 지시합니다.

### 3.2 Interface Veracity Logic: Insert Positional Audit
금형 내부에 삽입된 인서트 부품의 위치 이탈 및 결합 무결성을 오딧하는 알고리즘입니다.
*   **진단 결과**: FidelityEngine은 인서트 고정 압력과 사출 시 유동에 의한 유동압(Flow Pressure)을 오딧합니다. 유동압이 인서트 유지력을 상회하여 위치가 밀리면 이를 **'결합 무결성 붕괴'**로 판정하고 게이트 속도 하향 또는 지그(Jig) 구조 개선을 제안합니다.

## 4. [코드 연결 해설: Tooling & Design Auditor]
이 코드는 열팽창 및 기구 데이터를 기반으로 금형의 설계 및 가동 무결성을 진단합니다.

```python
class MoldDesignIntelligenceEngine:
    """
    HDS-Gold V6.3.7: 정밀 금형 설계 및 가동 무결성 진단 엔진
    """
    def __init__(self, steel_cte=12e-6, fit_tolerance_um=5):
        self.ALPHA = steel_cte
        self.TOLERANCE = fit_tolerance_um

    def audit_tooling_fidelity(self, base_length_mm, op_temp_c, friction_coefficient):
        """
        열팽창 공차 및 마찰 계수 기반 금형 무결성 평가
        """
        delta_t = op_temp_c - 25.0
        expansion_um = base_length_mm * self.ALPHA * delta_t * 1000
        
        status = "TOOLING_MECHANISM_STABLE"
        
        # 1. 기하학적 정합 무결성 검증
        if expansion_um > self.TOLERANCE * 2:
            status = "WARNING_THERMAL_INTERFERENCE_SEIZURE_RISK"
            
        # 2. 가동 마찰 무결성 검증
        if friction_coefficient > 0.15:
            status = "CRITICAL_LUBRICATION_FAILURE_MOLD_DAMAGE"
            
        return {
            "expansion_fidelity": round(self.TOLERANCE / expansion_um, 4) if expansion_um > 0 else 1.0,
            "motion_health": "SMOOTH" if friction_coefficient < 0.1 else "STIFF",
            "status": status,
            "action": "ADD_CLEARANCE_OR_APPLY_HIGH_TEMP_GREASE" if "CRITICAL" in status else "PROCEED"
        }

# FidelityEngine 가동: 금형 개폐 스트로크 센서와 가동부 온도 로그를 융합하여 '강철 실질 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 초정밀 렌즈 금형에서 **Core/Cavity Fit < 2.0um** 사수가 Tier 0 필수 요건인 이유는? (힌트: 미세한 틈새로 수지가 새어 나가는 플래시(Flash) 현상이 제품의 광학적 유효경을 침범하고 '표면 무결성 붕괴'를 초래하기 때문)
2. **Operational Result**: **Spencer-Gilmore** 모델을 활용한 금형 치수 보정 설계가 일반 수축률 반영 방식 대비 양산 초기 합격률(First Pass Yield)의 수리적 향상 폭은?
3. **FidelityEngine**: 슬라이더 가동부의 **'금속 고착(Galling)'** 전조를 FidelityEngine이 어떻게 '기계적 무결성 위기'로 사전 감지하고 자율 윤활 시스템을 가동하는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [Mold mold-and-plastic-manufacturing-intelligence-moc]]
- [[Mold] plastic-injection-molding-physics-and-cycle-analysis]
- [[Mold] fluid-dynamics-in-mold-filling-and-viscosity-models]
- [[System] mechanical-kinematics-and-material-expansion-logic]

**[V6.3.7_MOLD_DESIGN_INSERT_MASTER_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**