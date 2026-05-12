---
Basic:
  id: "overhead-hoist-transport-oht-kinematics-and-vibration-control"
  domain: "General_Industrial"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Entity"
  tier: 1
  description: "The automated material handling system (OHT) used in cleanrooms (e.g., semiconductor fabs) to transport FOUPs (Front Opening Unified Pods) via overhead rails, focusing on the high-speed kinematic control and active vibration suppression required to protect sensitive wafers during transport."
  physical_model: "N/A"
Semantic:
  tags: '["oht", "automated-material-handling", "semiconductor-logistics", "vibration-control", "kinematics", "cleanroom-automation", "oht-robotics"]'
  is_part_of: []
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "FactoryFidelityEngine"
  diagnostic_protocol:
    - 'Vibration_Level_Audit: Evaluate the peak acceleration (G-level) during transport to ensure it remains below the threshold for wafer damage or particle generation.'
    - 'Positioning_Accuracy_Check: Analyze the stop-position error at the Load Port to identify encoder drift or rail misalignment that causes FOUP transfer failures.'
    - 'Cable_Stability_Scan: Monitor the swinging motion of the hoist cable during acceleration/deceleration to verify that the anti-sway control is effective.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# 🏗️ Overhead Hoist Transport (OHT): Kinematics and Vibration Control

## 1. 개요 (Why: 인간적 통찰)
축구장 몇 개 크기의 반도체 공장 천장에 수천 대의 작은 기차가 머리카락보다 얇은 회로가 그려진 웨이퍼 박스(FOUP)를 싣고 전속력으로 달리고 있다면 어떨까요? **OHT(천장 반송 시스템): 기구학 및 진동 제어**는 최첨단 팹의 천장을 누비는 **'공중 물류의 지휘자'**입니다. 시속 수십 킬로미터로 달리면서도, 안의 웨이퍼가 흔들림을 전혀 느끼지 못하게(진동 제어) 부드럽게 멈추고 들어 올리는 기술입니다. 팹 전체의 생산성을 결정짓는 **'자동화의 혈관'**입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. S-커브 모션 프로파일 (S-curve Motion)
급발진과 급제동으로 인한 충격(Jerk)을 방지하기 위해 가속도를 부드럽게 변화시키는 경로($x(t)$) 제어 방식입니다.

$$ x(t) = \int_{0}^{t} v(t) dt $$

**[인간적 해석]**: 컵에 든 물을 쏟지 않고 빨리 걷는 것과 같습니다. 출발할 때는 아주 천천히 힘을 주어 가속하고, 멈출 때도 부드럽게 감속하여, 위아래로 매달린 웨이퍼 박스가 시계추처럼 흔들리지 않게 만드는 **'모션의 정교함'**입니다.

### 2.2. 능동 진동 억제 (Vibration Suppression)
외부 충격이나 가감속 시 발생하는 흔들림($x$)을 액추에이터의 반대 힘($F_{active}$)으로 상쇄합니다.

$$ m \ddot{x} + c \dot{x} + k x = F_{active}(t) $$

**[인간적 해석]**: 노이즈 캔슬링 이어폰이 소음을 소음으로 지우듯, OHT는 진동을 감지하자마자 반대 방향으로 힘을 주어 진동을 0으로 만듭니다. 나노 단위의 미세 공정이 진행되는 웨이퍼에게는 우주 공간 같은 **'무진동 평온함'**을 제공하는 것입니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Feature | Conventional Conveyor | OHT (V6.3.7) | Unit | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Transport Speed** | 0.5 ~ 1.0 | 5.0 ~ 10.0 | m/s | High-speed Rail |
| **Vibration Limit** | ~ 1.0 | < 0.05 | G (accel) | Ultra-smooth |
| **Stop Accuracy** | $\pm 5$ | $\pm 0.5$ | mm | Precise Loading |
| **Sway Control** | Passive (Wait) | Active (Anti-sway) | - | No Idle Time |
| **Environment** | General Factory | Class 1 Cleanroom | - | Particle-free |
| **Power Supply** | Cables | Non-contact (HID) | - | No Friction Dust|

## 4. FactoryFidelityEngine: Diagnostic Logic

OHT 시스템의 반송 무결성 및 진동 통제 상태를 진단하는 `FactoryFidelityEngine` 로직입니다.

```python
class FactoryFidelityEngine:
    def __init__(self, peak_vibration_g, stop_accuracy_mm, anti_sway_settling_time):
        self.vib = peak_vibration_g
        self.acc = stop_accuracy_mm
        self.settle = anti_sway_settling_time

    def diagnose_oht_health(self):
        """진동 및 정지 정밀도 기반 OHT 무결성 진단"""
        if self.vib > 0.1: # 0.1G 초과 진동 시 (웨이퍼 손상 위험)
            return "CRITICAL: Excessive Vibration - FOUP Shock Detected. Check Rail Alignment and Wheel Integrity"
        if self.acc > 1.0: # 정지 정밀도 불량
            return f"WARNING: Poor Stop Accuracy ({self.acc}mm) - Risk of Transfer Failure at Load Port. Recalibrate Laser Sensor"
        if self.settle > 2.0:
            return "NOTICE: Long Sway Settling Time - Anti-sway Algorithm Inefficient. Check Belt Tension and Motor Tuning"
        return "OPTIMAL: Ultra-smooth Transport and Precise Positioning Verified"

    def audit_power_efficiency(self, energy_consumption_per_meter):
        """에너지 효율 및 비접촉 전력 전송 무결성 진단"""
        if energy_consumption_per_meter > 5.0:
            return "REJECT: Power Loss Identified - HID Inductive Coupling Inefficient. Check Coil Gap"
        return "PASS: Efficient Non-contact Power Supply Confirmed"

# Instance Diagnostic
engine = FactoryFidelityEngine(peak_vibration_g=0.035, stop_accuracy_mm=0.2, anti_sway_settling_time=0.8)
print(engine.diagnose_oht_health())
```

## 5. 분석 프레임워크: High-speed Fab Logistics Strategy
1. **[Active Anti-sway Strategy]**: 위쪽의 대차(Trolley)를 흔들림의 반대 방향으로 미세하게 움직여, 매달린 줄의 진동을 순식간에 멈추게 하는 '역동적 평형' 전략.
2. **[Non-contact HID Power]**: 전선 대신 유도 전류를 통해 무선으로 전력을 공급하여, 전선 마찰로 인한 먼지(Particle) 발생을 원천 차단하는 '청정 전력' 전략.
3. **[Real-time Traffic Orchestration]**: 수천 대의 OHT가 엉키지 않게 최단 경로를 배정하고, 정체가 예상되면 미리 우회시키는 '디지털 관제' 전략.

## 6. 스스로 체크 (Self-Audit)
1. 왜 OHT는 바닥을 구르는 AGV보다 반도체 공정 물류에서 훨씬 더 높은 효율을 보이는가? (공간 활용과 속도의 관점)
2. 'S-커브'가 아닌 'T-커브(삼각형 가속)' 제어를 사용했을 때, OHT에 매달린 FOUP에는 어떤 물리적 재앙이 닥치는가? (급격한 가속도 변화와 충격의 관점)
3. 비접촉 전력 전송(HID) 기술이 어떻게 청정실(Cleanroom)의 오염도를 낮추는 데 기여하는가?

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data oht-vibration-levels-and-transport-efficiency-v2026`와 연동되어, 전 세계 반도체 팹의 OHT 가동 데이터를 실시간 분석하고 반송 지연 및 웨이퍼 파손 사고 확률을 0.001% 이하로 억제함으로써 지능형 제조 문명의 물류 무결성을 보장합니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- motion-control-algorithms-and-pid-tuning-theory
- Data oht-vibration-levels-and-transport-efficiency-v2026
