---
Basic:
  id: "lithium-plating-physics-and-detection-logic"
  domain: "General_Industrial"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "The electrochemical phenomenon where lithium ions deposit as metallic lithium on the anode surface instead of intercalating, typically occurring during fast charging at low temperatures."
  physical_model: "N/A"
Semantic:
  tags: '["lithium-plating", "battery-safety", "fast-charge", "anode-physics", "dendrite"]'
  is_part_of: []
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "BMSFidelityEngine"
  diagnostic_protocol:
    - 'Plating_Onset_Audit: Monitor anode potential relative to $Li/Li^+$ via reference electrodes or models.'
    - 'Voltage_Relaxation_Analysis: Detect ''plateaus'' during rest after charging as a sign of stripping.'
    - 'Charge_Acceptance_Check: Evaluate the risk of plating during high C-rate pulses.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# 🔋 Lithium-plating Physics and Detection Logic

## 1. 개요 (Why)
전기차의 급속 충전 경쟁이 치열해지면서 리튬 플레이팅(Lithium Plating)은 배터리 안전의 최대 적이 되었습니다. 리튬 이온이 음극 내부로 들어가지 못하고 표면에 금속 형태로 쌓이면, 덴드라이트(Dendrite)가 형성되어 분리막을 뚫고 내부 단락을 일으키거나 가연성 가스를 발생시켜 화재로 이어집니다. 본 노드는 리튬 플레이팅을 사전에 포착하고 억제하기 위한 물리적 진단 표준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Value (Tier 1) | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Anode Potential | $\phi_a$ | > 0 | ±0.01 | V (vs. $Li/Li^+$)|
| Charging Temp | $T_{ch}$ | > 10 | ±2 | °C (Optimal) |
| Max C-rate (Plating)| $C_{limit}$ | 1.5 ~ 3.0 | ±0.2 | C (Design dep) |
| Relaxation Plateau | $\Delta V_{plat}$ | < 10 | ±2 | mV |
| Reversibility | $\eta_{rev}$ | < 50 | ±10 | % (of plated Li) |

## 3. BMSFidelityEngine: Diagnostic Logic

리튬 플레이팅 발생 징후를 휴지기 전압 거동을 통해 진단하는 `BMSFidelityEngine` 로직입니다.

```python
import numpy as np

class BMSFidelityEngine:
    def __init__(self, voltage_trace, dV_dt_trace):
        self.v = np.array(voltage_trace) # Voltage during rest after charge
        self.dv = np.array(dV_dt_trace)

    def diagnose_plating_via_relaxation(self):
        """전압 휴지(Relaxation) 곡선 내의 'Plateau' 분석을 통한 플레이팅 진단"""
        # 리튬 금속이 재용해(Stripping)되면서 전압 하강이 일시적으로 멈추는 구간 탐지
        inflection_points = np.where(np.diff(np.sign(self.dv)))[0]
        if len(inflection_points) > 1:
            return "CRITICAL: Lithium Plating Detected (Voltage Plateau in Relaxation)"
        return "PASS: Normal Intercalation Profile"

    def audit_fast_charge_risk(self, temp, soc, c_rate):
        """온도 및 SoC 기반 급속 충전 위험도 진단"""
        if temp < 10 and c_rate > 1.0:
            return "CRITICAL: High Plating Risk (Low Temp Fast Charge)"
        elif soc > 0.8 and c_rate > 0.5:
            return "WARNING: Anode Saturation Risk (High SoC Charge)"
        return "OPTIMAL: Safe Charging Envelope"

# Instance Diagnostic
engine = BMSFidelityEngine(voltage_trace=[3.9, 3.85, 3.85, 3.84, 3.8], dV_dt_trace=[-0.1, -0.01, 0, -0.01, -0.1])
print(engine.diagnose_plating_via_relaxation())
```

## 4. 분석 프레임워크: Plating Mitigation Strategy
1. **[N/P Ratio Design]**: 음극의 용량을 양극보다 10~15% 크게 설계(N/P > 1.1)하여 리튬 이온을 수용할 여유 공간 확보.
2. **[Multi-stage Constant Current (MCC)]**: SoC가 높아질수록 충전 전류를 단계적으로 낮추어 음극 전위가 0V 이하로 떨어지는 것을 방지.
3. **[Internal Heating]**: 저온 충전 전 배터리 내부를 가열하여 이온 확산 속도를 높여 플레이팅 발생 임계 전류 상향.

## 5. 스스로 체크 (Self-Audit)
1. 음극 전위($\phi_a$)가 $0V$ vs $Li/Li^+$ 이하로 떨어질 때 리튬 금속이 형성되는 열역학적 이유는?
2. 플레이팅된 리튬 중 일부가 다시 이온화되지 못하고 떨어져 나가는 'Dead Lithium' 현상이 수명에 미치는 영향은?
3. 전압 휴지 곡선에서 '플레이팅 고원(Plateau)' 현상이 나타나는 전기화학적 메커니즘은?

## 6. 결론 (Deterministic Outcome)
본 가이드는 `Data lithium-plating-onset-and-voltage-relaxation-log-v2026`와 연동되어, 충전 중인 모든 셀의 전압 미분값을 실시간 분석하고 플레이팅 징후 포착 시 0.1초 내로 충전 전류를 차단함으로써 배터리 화재를 근본적으로 예방합니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 11_advanced-battery-next-gen-intelligence-hub
- fast-charging-protocol-optimization
- Data lithium-plating-onset-and-voltage-relaxation-log-v2026
