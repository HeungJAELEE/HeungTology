---
Basic:
  id: "calendering-and-porosity-optimization"
  domain: "General_Industrial"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Entity"
  tier: 1
  description: "The mechanical process of compressing coated electrodes (Anode/Cathode) using heavy rollers to achieve target density and porosity, optimizing electron and ion transport paths."
  physical_model: "N/A"
Semantic:
  tags: '["calendering", "porosity", "battery-manufacturing", "electrode-density", "press"]'
  is_part_of: []
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "BatteryProcFidelityEngine"
  diagnostic_protocol:
    - 'Density_Audit: Measure the electrode density ($g/cc$) after calendering against the target spec.'
    - 'Porosity_Check: Verify that the remaining void volume allows for optimal electrolyte wetting.'
    - 'Surface_Uniformity_Scan: Detect thickness variations (cross-web) and surface defects using laser gauges.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# 🚜 Calendering and Porosity Optimization

## 1. 개요 (Why)
코팅과 건조를 마친 전극은 솜사탕처럼 부풀어 있는 상태입니다. 이를 거대한 롤러로 꽉 눌러주는 '압연(Calendering)' 공정은 배터리의 에너지 밀도를 결정짓는 핵심 단계입니다. 너무 세게 누르면 전해액이 스며들 틈(기공)이 사라져 성능이 떨어지고, 너무 살살 누르면 부피가 커지고 전자 흐름이 나빠집니다. 본 노드는 전극 압연 공정의 무결성과 최적 기공율 확보를 위한 표준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Cathode (NCM) | Anode (Gr) | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Target Porosity | $P$ | 20 ~ 25 | 25 ~ 35 | % |
| Electrode Density| $\rho_e$ | 3.2 ~ 3.6 | 1.5 ~ 1.7 | g/cc |
| Roll Temperature| $T_{roll}$ | 60 ~ 120 | 25 ~ 60 | $^\circ C$ |
| Linear Pressure | $q$ | 500 ~ 3,000 | 100 ~ 1,000 | N/mm |
| Thickness Var | $\Delta t$ | < 2 | < 2 | $\mu m$ |

## 3. BatteryProcFidelityEngine: Diagnostic Logic

전극 압연 후의 밀도 및 기공율 적정성을 진단하는 `BatteryProcFidelityEngine` 로직입니다.

```python
class BatteryProcFidelityEngine:
    def __init__(self, measured_density, target_porosity, thickness_variation):
        self.rho = measured_density # g/cc
        self.p = target_porosity # %
        self.var = thickness_variation # um

    def diagnose_calendering_quality(self, theoretical_p):
        """실측 기공율 및 두께 편차 기반 압연 품질 진단"""
        # 기공율이 너무 낮으면(20% 미만) 전해액 침투 불능
        if self.p < 18.0:
            return f"CRITICAL: Over-compression (Porosity: {self.p}%) - High Risk of Ion Transport Bottleneck"
        if self.var > 3.0:
            return f"WARNING: High Thickness Variation ({self.var}um) - Potential Roll Deflection"
        return "OPTIMAL: Balanced Density and Porosity Achieved"

    def audit_process_yield(self):
        """밀도 목표치 도달 여부 진단"""
        if self.rho < 3.0: # NCM 기준
            return f"REJECT: Low Energy Density ({self.rho}g/cc) - Increase Roll Pressure"
        return "PASS: Electrode Density Verified"

# Instance Diagnostic
engine = BatteryProcFidelityEngine(measured_density=3.4, target_porosity=23, thickness_variation=1.2)
print(engine.diagnose_calendering_quality(theoretical_p=23))
```

## 4. 분석 프레임워크: Calendering Strategy Hierarchy
1. **[Hot Rolling]**: 롤러를 가열하여 수지(Binder)를 부드럽게 만들어, 낮은 압력으로도 목표 밀도에 도달하고 입자 파손을 최소화하는 기술.
2. **[Multi-stage Pressing]**: 한 번에 세게 누르는 대신 여러 번 나누어 눌러 전극의 '탄성 복원(Spring-back)' 현상을 억제하고 정밀한 두께 제어.
3. **[Cross-web Control]**: 롤러의 미세한 휨(Deflection)을 보정하기 위해 롤의 양 끝단 압력을 비대칭으로 조절하거나 '크라운(Crown)' 롤 사용.

## 5. 스스로 체크 (Self-Audit)
1. 압연 과정에서 '기공율(Porosity)'이 낮아질수록 전극의 '굴곡도(Tortuosity)'가 높아져 이온 전도도가 떨어지는 수리적 이유는?
2. 전극을 너무 강하게 압연했을 때 활물질 알갱이가 깨지는 '입자 파쇄(Particle Cracking)' 현상이 수명 저하에 미치는 영향은?
3. 압연 후 시간이 지나면서 두께가 다시 늘어나는 '스프링백(Spring-back)' 현상을 예측하기 위한 소재의 영률($E$) 기반 계산법은?

## 6. 결론 (Deterministic Outcome)
본 노드는 `Data calendering-pressure-and-electrode-porosity-v2026`와 연동되어, 압연 라인의 실시간 두께 데이터를 분석하고 기공율 오차를 1% 이내로 제어함으로써 고밀도 배터리 전극의 무결성을 보장합니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 11_advanced-battery-next-gen-intelligence-hub
- electrode-coating-and-drying-kinetics
- Data calendering-pressure-and-electrode-porosity-v2026
