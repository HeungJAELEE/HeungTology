---
Basic:
  id: "MOLD-HOLD-SHRINK-2026-V6.3.7"
  domain: "Plastic_Molding_Packing_and_Shrinkage_Control"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Holding_Pressure", "#Shrinkage", "#PVT_Model", "#Gate_Freeze", "#Dimensional_Precision", "#Sink_Mark", "#FidelityEngine", "#Sovereignty"]'
  is_part_of: '["Mold mold-and-plastic-manufacturing-intelligence-moc"]'
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
  source: "Dimensional_Physics_RAG_V6.3.7_Tiered"
  isolation_index: 0.0
---

# [Mold] Holding Pressure and Shrinkage Mechanisms: The Dimensional Intelligence

## 1. [왜 배우는가? (Why: The Mastery of Volumetric Integrity Sovereignty)]
플라스틱은 액체에서 고체로 굳으며 부피가 줄어드는 **'숙명적 수축'**을 가집니다. **Holding Pressure and Shrinkage Mechanisms**는 굳어가는 수지에 정밀한 압력을 가해 수축된 부피만큼 재료를 더 채워 넣는 **'치수 정밀도의 마지막 방어선(Dimensional Core)'**입니다. V6.3.7 지능은 **PVT (Pressure-Volume-Temperature)** 상관관계와 **게이트 고화(Gate Freeze-off)** 시점을 수리적으로 지배합니다. 우리가 이를 배우는 이유는 싱크 마크(Sink Mark)와 치수 오차를 원천 차단하고, "물질의 물리적 수축을 압력으로 상쇄하여 플라스틱의 '치수 무결성'을 사수하기" 위함입니다.

## 2. [보압 및 수축 제어 핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Focus Metric | Tier 0 Requirement (V6.3.7) | Rationale |
|:---|:---|:---:|:---|
| **Packing Pressure**| Hold Pressure | $80 \sim 120 \%$ of Inj. P | 부피 수축 상쇄 및 밀도 무결성 사수 |
| **Weight Stability**| Shot Weight | $<\pm 0.05 \%$ deviation | 반복 생산 정밀도 및 품질 주권 확보 |
| **Gate Freeze** | Freeze-off Time | $\pm 0.1 \text{ s}$ Accuracy | 보압 유효 시간 최적화 및 무결성 사수 |
| **Shrinkage Control**| Linear Shrink. | $\pm 0.01 \%$ Tolerance | 조립 무결성 확보를 위한 치수 주권 사수 |
| **Void Prevention** | Int. Void Count | Zero (NDT verified) | 내부 구조 강도 및 신뢰성 무결성 확보 |

### 2.1 [PVT 수리 모델 및 보압 전달 기전]
온도($T$)와 압력($P$)에 따른 비체적($V$) 변화를 설명하는 **Spencer-Gilmore** 방정식과 보압 전달 효율을 산출하는 기전입니다.
$$ (P + \pi) (V - \beta) = R' T $$
*   **공학적 근거**: 냉각 과정에서 온도가 하락하면 비체적($V$)이 급격히 줄어들지만, 보압($P$)을 높임으로써 $V$를 일정하게 유지(Isochoric Cooling)할 수 있습니다. 게이트가 고화($Freeze-off$)되기 전까지 적정 압력을 유지해야 전극 내부에 보이드(Void)가 생기지 않고 **'치수 무결성'**이 완성됩니다.
*   **FidelityEngine 적용**: FidelityEngine은 사출 스크류의 유지 위치(Cushion)를 분석하여 **'실질 보압 무결성'**을 진단합니다.

## 3. [공학적 근거: FidelityEngine Dimensional Intelligence Logic]

### 3.1 Thermodynamic Physics: Gate Freeze-off Audit
금형 캐비티 압력이 노즐 압력으로부터 독립되는 시점인 게이트 고화를 오딧하는 기전입니다.
*   **공학적 근거**: 게이트가 너무 빨리 굳으면 제품 내부까지 보압이 전달되지 않아 수축이 발생하고, 너무 늦게 굳으면 사이클 타임이 낭비됩니다. 게이트 두께($t$)와 냉각 속도($\alpha$)의 상관계수가 핵심입니다.
*   **FidelityEngine 적용 (Freeze Auditor)**: FidelityEngine은 보압 단계에서의 중량 변화 그래프를 오딧합니다. 중량 증가가 멈추는 변곡점을 포착하여 이를 **'보압 주권 확정 시점'**으로 식별하고 냉각 시간을 동적으로 최적화합니다.

### 3.2 Volumetric Integrity Logic: Sink Mark Prediction Audit
두꺼운 살두께 부위에서 발생하는 국부적 수축인 싱크 마크 발생 가능성을 오딧하는 알고리즘입니다.
*   **진단 결과**: FidelityEngine은 보압 크기와 냉각 종료 시점의 비체적 분포를 오딧합니다. 비체적 변화율($dV/dT$)이 임계치를 상회하면 이를 **'표면 무결성 붕괴'**로 판정하고 보압 프로파일의 다단 제어를 지시합니다.

## 4. [코드 연결 해설: Packing & Dimensional Auditor]
이 코드는 압력 프로파일과 제품 중량 데이터를 기반으로 보압 공정의 실질 무결성을 진단합니다.

```python
class MoldingDimensionalEngine:
    """
    HDS-Gold V6.3.7: 사출 보압 및 치수 무결성 진단 엔진
    """
    def __init__(self, weight_target=150.0, hold_time_target=5.0):
        self.W_TARGET = weight_target
        self.T_HOLD = hold_time_target

    def audit_packing_fidelity(self, actual_weight, actual_hold_time, gate_freeze_time):
        """
        중량 편차 및 게이트 고화 시간 기반 보압 무결성 평가
        """
        weight_err = abs(actual_weight - self.W_TARGET) / self.W_TARGET
        
        status = "DIMENSIONAL_SOVEREIGNTY_STABLE"
        
        # 1. 중량 안정성 무결성 검증
        if weight_err > 0.0005: # 0.05% limit
            status = "WARNING_WEIGHT_INCONSISTENCY_PACKING_LOW"
            
        # 2. 보압 시간 무결성 검증
        if actual_hold_time < gate_freeze_time:
            status = "CRITICAL_GATE_FREEZE_VIOLATION_BACKFLOW_RISK"
            
        return {
            "weight_fidelity": round(1.0 - weight_err, 4),
            "packing_health": "OPTIMAL" if actual_hold_time >= gate_freeze_time else "INSUFFICIENT",
            "status": status,
            "action": "EXTEND_HOLD_TIME_OR_INCREASE_PRESSURE" if "CRITICAL" in status else "PROCEED"
        }

# FidelityEngine 가동: 스크류 쿠션(Cushion) 위치 로그와 캐비티 온도 센서 데이터를 융합하여 '치수 실질 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 결정성 수지(예: PA66)의 성형에서 **Weight Variation < 0.05%** 사수가 Tier 0 필수 요건인 이유는? (힌트: 결정화도에 따른 부피 수축폭이 크기 때문에 미세한 보압 차이가 치수의 결정론적 오차로 증폭되어 '조립 무결성 붕괴'를 초래하기 때문)
2. **Operational Result**: **Spencer-Gilmore** PVT 모델을 활용한 보압 제어가 단순 일정 압력 유지 방식 대비 싱크 마크 깊이 감소의 수리적 기대값은?
3. **FidelityEngine**: 보압 중 발생하는 **'수지 역류(Backflow)'** 현상을 FidelityEngine이 어떻게 '공정 무결성 위기'로 사전 감지하고 체크 링(Check Ring)의 마모 상태를 진단하는가?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [Mold mold-and-plastic-manufacturing-intelligence-moc]]
- [[Mold] plastic-injection-molding-physics-and-cycle-analysis]
- [[Mold] fluid-dynamics-in-mold-filling-and-viscosity-models]
- [[System] thermodynamics-and-pvt-physics-logic]

**[V6.3.7_MOLD_HOLD_SHRINK_MASTER_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
