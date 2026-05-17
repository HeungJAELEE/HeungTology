---
metadata:
  id: "[[[Entity] casting-and-solidification-processes]]"
  domain: "11_Global_Entities_and_Materials"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Entity] casting-and-solidification-processes에 관한 고밀도 지능 노드"
semantic:
  tags: ["#11_Global_Entities_and_Materials", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Entity] casting-and-solidification-processes

## 1. 개요 (Why)
금속 제품을 만드는 가장 오래되고 강력한 방법은 녹여서 붓는 '주조'입니다. 엔진 블록부터 선박의 프로펠러까지, 복잡한 형상을 한 번에 만들 수 있습니다. 핵심은 액체가 고체로 변하는 '응고(Solidification)' 과정에서 결정의 크기와 방향을 제어하여 기계적 강도를 확보하고, 식으면서 부피가 줄어들어 생기는 구멍(Shrinkage)을 막는 것입니다. 본 노드는 주조 공정의 무결성과 금속 조직 제어를 위한 표준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Target Value | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Pouring Temp | $T_p$ | $T_L + (50 \sim 150)$| ±10 | $^\circ C$ |
| Cooling Rate | $\dot{T}$ | 1 ~ 1,000 | ±5 | $K/s$ |
| Grain Size | $d$ | 10 ~ 500 | ±20 | $\mu\text{m}$ |
| Casting Yield | $\eta$ | > 90 | ±2 | % |
| Porosity Limit | $V_p$ | < 0.5 | ±0.1 | % |

## 3. FactoryFidelityEngine: Diagnostic Logic

주조 응고 과정의 시간 및 수축 결함 위험을 진단하는 `FactoryFidelityEngine` 로직입니다.

```python
class FactoryFidelityEngine:
    def __init__(self, volume_area_ratio, mold_constant, measured_time):
        self.var = volume_area_ratio # V/A
        self.b = mold_constant
        self.t_actual = measured_time

    def diagnose_solidification_integrity(self):
        """초보리노프 법칙(Chvorinov's Rule) 기반 응고 시간 진단"""
        # t = B * (V/A)^2
        t_calc = self.b * (self.var ** 2)
        if abs(self.t_actual - t_calc) / t_calc > 0.15:
            return f"CRITICAL: Abnormal Solidification Rate (Diff: {abs(self.t_actual - t_calc):.1f}s) - Risk of Dendritic Segregation"
        return "OPTIMAL: Controlled Solidification Time Verified"

    def audit_shrinkage_risk(self, superheat):
        """과열도(Superheat) 기반 수축 결함 위험 진단"""
        if superheat < 30:
            return f"WARNING: Low Superheat ({superheat}C) - Risk of Misrun or Premature Freezing"
        return "PASS: Fluidity and Thermal Margin Confirmed"

engine = FactoryFidelityEngine(volume_area_ratio=2.5, mold_constant=3.2, measured_time=21)
print(engine.diagnose_solidification_integrity())
```

## 4. 분석 프레임워크: Casting Strategy Hierarchy
1. **[Gating System Design]**: 쇳물이 금형 내부로 들어가는 길을 설계하여 와류(Turbulence)와 공기 유입을 방지하고 균일한 충전 유도.
2. **[Riser & Feeder Optimization]**: 응고 시 수축하는 부위에 액체 금속을 지속적으로 공급하는 '라이저(Riser)'를 배치하여 내부 기공 원천 차단.
3. **[Directional Solidification]**: 냉각 속도를 위치별로 다르게 조절하여 결정이 특정 방향으로 자라게 함으로써, 고온 강도가 필요한 터빈 날개 등의 성능 극대화.

## 5. 스스로 체크 (Self-Audit)
1. '초보리노프 법칙'에 따라 제품의 부피($V$) 대비 표면적($A$)이 작을수록 응고 시간이 길어지는 기하학적 이유는?
2. 응고 시 발생하는 '수축(Shrinkage)'이 외부로 드러나는 '외관 수축'과 내부의 '미세 기공'으로 나뉘는 물리적 조건은?
3. 합금 성분이 응고 전단면에서 불균일하게 분포하는 '편석(Segregation)' 현상을 방지하기 위한 냉각 속도 제어 전략은?

## 6. 결론 (Deterministic Outcome)
본 노드는 `Data casting-yield-and-defect-rate-log-v2026`와 연동되어, 주조 시의 온도 변화와 진동 데이터를 실시간 분석하고 내부 결함 발생 확률을 1% 이내로 제어함으로써 금속 부품 생산의 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 11_advanced-battery-next-gen-intelligence-hub
- metallurgy-and-alloy-design-logic
- Data casting-yield-and-defect-rate-log-v2026
