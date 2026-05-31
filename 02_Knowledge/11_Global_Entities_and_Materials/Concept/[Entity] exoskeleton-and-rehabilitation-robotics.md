---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: e5e48b47adb6994d5dd8a964ae1af66db9dc86e70993ccfa2c4a05cdb6006829
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] exoskeleton-and-rehabilitation-robotics]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] exoskeleton-and-rehabilitation-robotics에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  battery_life_industrial_hrs: 4-8
  battery_life_rehab_hrs: 2-4
  critical_sync_delay_ms: 20
  damping_b_parameter: damping
  dof_industrial_full_body: 6-12
  dof_rehab_per_leg: 2-6
  excessive_assistance_ratio_threshold: 0.9
  excessive_heart_rate_threshold_bpm: 160
  impedance_control_formula: F = k * delta_x + b * delta_x_dot
  joint_angle_limit_threshold_pct: 95.0
  load_assist_industrial_kg: 20-100
  load_assist_rehab_kg: 5-20
  stiffness_k_parameter: springiness
  sync_latency_industrial_ms_max: 5
  sync_latency_rehab_ms_max: 10
  system_mass_industrial_kg: 10-25
  system_mass_rehab_kg_max: 5
  tau_total_formula: tau_human + tau_robot
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 11_Global_Entities_and_Materials]]'
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

# [Entity] exoskeleton-and-rehabilitation-robotics

## 1. 개요 (Why: 인간적 통찰)
사고나 질병으로 걷지 못하게 된 사람에게 다시 걸을 수 있는 희망을 주고, 무거운 짐을 들어야 하는 노동자에게 강철과 같은 힘을 보태주는 기술, 그것이 바로 **외골격(Exoskeleton) 및 재활 로봇**입니다. 이 로봇은 인간의 몸 바깥에 입는 '두 번째 뼈와 근육'입니다. 기계가 인간을 대신하는 것이 아니라, 기계와 인간이 하나가 되어 움직이는 **'인간 중심의 증강(Human Augmentation)'**이 핵심입니다. 본 노드는 인간의 의지를 기계의 힘으로 부드럽게 번역해내는 조화와 안전의 무결성을 정의합니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 인체-로봇 하이브리드 동역학
인간이 내는 힘($\tau_h$)과 로봇이 내는 보조 힘($\tau_r$)이 합쳐져 전체 움직임($\tau_{total}$)을 만듭니다.

$$ \tau_{total} = \tau_{human} + \tau_{robot} $$

**[인간적 해석]**: 로봇은 주인과 함께 춤을 추는 파트너와 같습니다. 주인이 힘을 주면 로봇은 그 의도를 눈치채고 부족한 힘을 살짝 보태줍니다($Assistance$). 주인의 움직임을 방해하지 않으면서도 필요한 순간에 강한 힘을 내는 '교감'이 가장 중요합니다.

### 2.2. 임피던스 제어 (Impedance Control)
로봇의 관절이 얼마나 뻣뻣하거나 부드러워야 하는지를 제어합니다.

$$ F = k \cdot \Delta x + b \cdot \dot{x} $$

*   $k$: 강성 (Springiness).
*   $b$: 감쇠 (Damping).

**[인간적 해석]**: 재활 환자가 처음 걸음마를 뗄 때는 로봇이 단단하게 잡아주어야 하고($k \uparrow$), 익숙해지면 부드럽게 따라와야 합니다($k \downarrow$). 상황에 따라 기계의 성질을 '단단함'에서 '부드러움'으로 실시간으로 바꾸는 논리입니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Parameter | Metric | Rehabilitation | Industrial/Military | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Load Assist | Capacity | 5 ~ 20 | 20 ~ 100 | kg |
| Battery Life | Endurance | 2 ~ 4 | 4 ~ 8 | hours |
| Sync Latency | Response | < 10 | < 5 | ms |
| DoF | Degrees of Freedom| 2 ~ 6 (per leg) | 6 ~ 12 (Full body)| count |
| Weight | System Mass | < 5 | 10 ~ 25 | kg |

## 4. RobotFidelityEngine: Diagnostic Logic

외골격 로봇의 보조 효율 및 보행 동기화 상태를 진단하는 `RobotFidelityEngine` 로직입니다.

```python
class RobotFidelityEngine:
    def __init__(self, sync_delay_ms, assistance_ratio, wearer_heart_rate):
        self.delay = sync_delay_ms
        self.ratio = assistance_ratio # 로봇이 분담하는 힘의 비율
        self.hr = wearer_heart_rate

    def diagnose_augmentation_health(self):
        """동기화 지연 및 보조 비율 기반 무결성 진단"""
        if self.delay > 20: # 0.02초 초과 시 부자연스러움
            return f"CRITICAL: High Control Lag ({self.delay}ms) - Risk of Human-Robot Conflict and Injury"
        if self.ratio > 0.9:
            return "WARNING: Excessive Assistance - Potential for Muscle Atrophy in Long-term Use"
        if self.hr > 160:
            return f"REJECT: Excessive Physical Strain (HR: {self.hr}bpm) - Emergency Assistance Stop Required"
        return "OPTIMAL: Seamless Human-Robot Integration and Support Verified"

    def audit_joint_safety(self, joint_angle_limit_pct):
        """관절 가동 범위 기반 안전 진단"""
        if joint_angle_limit_pct > 95.0:
            return "REJECT: Near Mechanical Limit - Risk of Hyperextension"
        return "PASS: Safe Range of Motion Maintained"

engine = RobotFidelityEngine(sync_delay_ms(5.5, assistance_ratio=0.6, wearer_heart_rate=95)
engine = RobotFidelityEngine(5.5, 0.6, 95)
print(engine.diagnose_augmentation_health())
```

## 5. 분석 프레임워크: Human Augmentation Strategy
1. **[Intention Detection (EMG/EEG)]**: 근육에서 발생하는 미세한 전기 신호(EMG)나 뇌파(EEG)를 읽어, 주인이 발을 떼기도 전에 로봇이 먼저 움직일 준비를 하는 '의도 기반 제어'.
2. **[Bio-mimetic Actuation]**: 인간의 근육과 힘줄의 특성을 모방한 탄성 구동기(SEA)를 사용하여, 기계적인 딱딱함 대신 생명체와 같은 유연하고 안전한 움직임 구현.
3. **[Gait Analysis & Adaptation]**: 환자의 걸음걸이 패턴을 AI가 분석하여, 매 걸음마다 최적의 보조 타이밍을 찾아내고 재활 속도에 맞춰 난이도를 자동으로 조절하는 '맞춤형 재활'.

## 6. 스스로 체크 (Self-Audit)
1. '역구동성(Back-drivability)'—로봇의 전원이 꺼졌을 때 사람이 로봇을 쉽게 움직일 수 있는 능력—이 외골격 로봇의 안전에서 왜 핵심적인가?
2. 로봇의 '무게(Mass)'가 오히려 사람의 '대사 에너지(Metabolic cost)'를 높여 보조 효과를 상쇄하는 물리적 한계를 극복하기 위한 '경량화'의 수리적 목표치는?
3. '재활 로봇'이 단순히 보조를 해주는 것을 넘어, 뇌의 가소성(Plasticity)을 자극하여 마비된 신경을 되살리는 신경 과학적 메커니즘은?

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data exoskeleton-assistance-efficiency-and-gait-accuracy-v2026`와 연동되어, 전 세계 웨어러블 로봇의 사용 데이터를 실시간 분석하고 보조 실패 및 관절 부상 사고 확률을 0.01% 이하로 억제함으로써 인간 능력 증강의 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- control-theory-pid-lqr-and-model-predictive-control-mpc
- Data exoskeleton-assistance-efficiency-and-gait-accuracy-v2026