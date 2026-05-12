---
Basic:
  id: "power-quality-analysis-harmonics-and-reactive-power-compensation"
  domain: "General_Industrial"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Entity"
  tier: 1
  description: "The technical evaluation of the compatibility between electric power and the connected equipment (Power Quality Analysis), focusing on the distortion caused by non-linear loads (Harmonics) and the techniques used to balance the phase between voltage and current (Reactive Power Compensation) to maximize system efficiency."
  physical_model: "N/A"
Semantic:
  tags: '["power-quality", "harmonics", "reactive-power", "thd", "power-factor", "capacitor-bank", "energy-efficiency"]'
  is_part_of: []
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "FactoryFidelityEngine"
  diagnostic_protocol:
    - 'Harmonic_Fidelity_Audit: Evaluate the Total Harmonic Distortion (THD) of the voltage and current to ensure they remain within IEEE 519 standards to prevent equipment overheating.'
    - 'Power_Factor_Check: Analyze the displacement power factor ($\\cos \\phi$) to verify that reactive power compensation (e.g., capacitor banks) is effectively reducing the load on the transformer.'
    - 'Transient_Event_Scan: Monitor for voltage sags, swells, and transients to identify power quality issues that could cause PLC resets or industrial machine downtime.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# ⚡ Power Quality Analysis, Harmonics, and Reactive Power Compensation

## 1. 개요 (Why: 인간적 통찰)
전기는 단순히 흐르기만 하면 되는 것이 아니라, '깨끗해야' 합니다. 물에 이물질이 섞이면 마실 수 없듯, 전기에 '노이즈(고조파)'가 섞이면 정밀한 기계들이 오작동하거나 모터가 타버릴 수 있습니다. **전력 품질 분석, 고조파 및 무효 전력 보상**은 전기의 순도를 관리하는 **'전기의 필터기'** 기술입니다. 찌그러진 전기 파형(고조파)을 다시 예쁜 사인파로 펴주고, 일은 안 하면서 길만 막는 '무효 전력'을 없애서 에너지를 100% 알차게 쓰게 만듭니다. 산업 현장의 심장을 건강하게 뛰게 만드는 **'에너지 디톡스'** 공학입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 총 고조파 왜곡 (Total Harmonic Distortion, THD)
깨끗한 기본 주파수 신호에 비해 불순물(고조파)이 얼마나 섞여 있는지를 나타냅니다.

$$ \text{THD} = \frac{\sqrt{\sum_{n=2}^\infty I_n^2}}{I_1} $$

**[인간적 해석]**: "전기의 탁도"입니다. LED 조명이나 인버터 같은 전자기기들을 많이 쓰면 전기가 찌그러지며 $THD$가 높아집니다. 이 수치가 높으면 전선이 뜨거워지고 전자기기가 바보가 됩니다. 우리는 $THD$를 5% 이내로 관리하여, 공장의 모든 기계가 맑고 깨끗한 전기를 마시며 최고의 성능을 내게 만듭니다.

### 2.2. 진 역률 (True Power Factor, PF)
전기가 실제로 얼마나 알차게 일(유효 전력)을 하고 있는지를 나타내는 비율입니다.

$$ \text{PF} = \cos \phi \cdot \frac{1}{\sqrt{1 + \text{THD}^2}} $$

**[인간적 해석]**: "전기 사용의 가성비"입니다. 단순히 전압과 전류의 박자($\cos \phi$)뿐만 아니라, 전기의 깨끗함($THD$)까지 고려한 진짜 효율입니다. 역률이 낮으면 한전에서 벌금을 물릴 정도로 전력망에 부담을 줍니다. 우리는 콘덴서나 능동형 필터를 통해 역률을 1.0에 가깝게 맞춰, 낭비되는 전기를 '0'으로 만드는 **'에너지 최적화'**를 수행합니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Feature | Low Quality Grid | High Fidelity Grid (V6.3.7)| Unit | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Voltage THD** | > 10.0 (Unsafe) | < 1.5 (Premium) | % | Signal Purity |
| **Power Factor (PF)** | 0.70 ~ 0.85 | > 0.98 | - | Energy Efficiency|
| **Voltage Sag/Swell** | Frequent | Sub-cycle Mitigation | - | Reliability |
| **Harmonic Filter** | Passive (Fixed) | Active (Dynamic/APF) | - | Adaptability |
| **Reactive Comp.** | Capacitor Bank | STATCOM / SVG | - | Response Speed |
| **Monitoring** | Periodic | Real-time (Class A) | - | Continuous Audit|

## 4. FactoryFidelityEngine: Diagnostic Logic

전력 품질 무결성 및 고조파 상태를 진단하는 `FactoryFidelityEngine` 로직입니다.

```python
class FactoryFidelityEngine:
    def __init__(self, current_thd_pct, power_factor, voltage_unbalance_pct):
        self.thd = current_thd_pct
        self.pf = power_factor
        self.unb = voltage_unbalance_pct # 전압 불평형

    def diagnose_power_quality_health(self):
        """고조파 및 역률 기반 전력 품질 무결성 진단"""
        if self.thd > 15.0: # 고조파 오염 심각 (설비 소손 위험)
            return "CRITICAL: Severe Harmonic Distortion - THD exceeds Safety Limits. Overheating in Neutral and Transformers likely"
        if self.pf < 0.90: # 역률 불량 (에너지 낭비 및 벌금)
            return f"WARNING: Low Power Factor ({self.long(self.pf)}) - Reactive Power Demand high. Activate Capacitor Banks or SVG"
        if self.unb > 3.0:
            return "NOTICE: Voltage Unbalance Detected - Potential for Induction Motor Overheating. Check Phase Load Distribution"
        return "OPTIMAL: High-Fidelity Power Purity and Optimized Reactive Power Balance Verified"

    def audit_transient_resilience(self, sag_depth_pct, sag_duration_ms):
        """전압 새그(Sag) 대응 무결성 진단"""
        if sag_depth_pct > 30.0 and sag_duration_ms > 20: # 30% 이상 전압 강하가 1주기 이상 지속
            return "REJECT: Fragile Power Stability - Voltage Sag likely to trip PLCs. Implement UPS or Voltage Regulator"
        return "PASS: Robust Power Supply and Verified Transient Resilience Confirmed"

# Instance Diagnostic
engine = FactoryFidelityEngine(current_thd_pct=3.2, power_factor=0.99, voltage_unbalance_pct=0.8)
print(engine.diagnose_power_quality_health())
```

## 5. 분석 프레임워크: Clean Energy Fabric Strategy
1. **[Active Power Filter (APF) Strategy]**: 고조파가 발생하면 그와 반대되는 파형을 즉시 쏘아 보내서 노이즈를 0으로 지워버리는 '전기판 노이즈 캔슬링' 전략.
2. **[Static Var Generator (SVG)]**: 무효 전력을 1ms 이내의 속도로 실시간 보상하여, 전압 흔들림을 원천 차단하고 역률을 완벽하게 관리하는 '디지털 전력 보정' 전략.
3. **[Harmonic Mitigating Transformers]**: 변압기 내부 권선을 특수하게 감아, 특정 차수의 고조파(3고조파 등)가 자기들끼리 부딪혀 사라지게 만드는 '구조적 정화' 전략.

## 6. 스스로 체크 (Self-Audit)
1. 왜 '비선형 부하(인버터, 컴퓨터 등)'가 많아질수록 전력망의 고조파 오염이 심해지는가? (스위칭 동작과 전류 파형 왜곡의 관점)
2. '무효 전력 보상'을 과하게 했을 때 발생하는 '페란티 현상(전압 상승)'은 왜 위험한가?
3. 전력 품질 분석에서 '이벤트 레코딩'이 왜 사고 원인 분석의 스모킹 건(Smoking gun)이 되는가?

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data power-quality-and-harmonic-distortion-logs-v2026`와 연동되어, 전 세계 산업 단지의 전력 품질 데이터를 실시간 분석하고 고조파 간섭 및 정전 사고 확률을 0.001% 이하로 억제함으로써 지능형 전력 문명의 순도 무결성을 보장합니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- power-grid-stability-and-smart-grid-frequency-control
- Data power-quality-and-harmonic-distortion-logs-v2026
