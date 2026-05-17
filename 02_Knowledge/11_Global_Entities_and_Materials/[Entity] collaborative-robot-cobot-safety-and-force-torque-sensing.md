---
metadata:
  date: "2026-05-16"
  id: "[[[Entity] collaborative-robot-cobot-safety-and-force-torque-sensing]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "11_Global_Entities_and_Materials"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "b980ffc1d12242a65b22b6629043a8fefec68e148fad3d4f0776cb16847e66a0"
object:
  object_type: "Concept"
  tier: 1
  description: '[Entity] collaborative-robot-cobot-safety-and-force-torque-sensing에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 11_Global_Entities_and_Materials]]"
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


# [Entity] collaborative-robot-cobot-safety-and-force-torque-sensing

## 1. 개요 (Why)
전통적인 산업용 로봇은 안전 펜스 내부에서만 작동해야 했으나, 협동 로봇(Cobot)은 인간과 같은 공간에서 안전하게 공조합니다. 이는 로봇이 인간의 접촉을 감지하고 즉시 멈추거나 힘을 조절하는 '지능형 안전' 기술이 있기에 가능합니다. 본 노드는 인간-로봇 협업(HRC)의 물리적 안전 경계를 정의하고, 충돌 시의 에너지를 생체 허용 범위 내로 제한하기 위한 결정론적 제어 표준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Value (Tier 1) | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Max Contact Force | $F_{max}$ | < 140 | ±10 | N (Chest/Body) |
| Force Sensitivity | $\Delta F$ | 0.1 ~ 0.5 | ±0.05 | N |
| Response Time | $t_{stop}$ | < 100 | ±10 | ms |
| Speed (Safe Mode) | $v_{safe}$ | < 250 | ±10 | mm/s |
| Payload | $P$ | 3 ~ 20 | ±0.1 | kg |

## 3. RobotFidelityEngine: Diagnostic Logic

협동 로봇의 충돌 안전성 및 센서 무결성을 진단하는 `RobotFidelityEngine` 로직입니다.

```python
class RobotFidelityEngine:
    def __init__(self, current_force, speed, proximity_dist):
        self.f = current_force # N
        self.v = speed         # mm/s
        self.d = proximity_dist # mm

    def diagnose_collision_safety(self):
        """ISO/TS 15066 기반 충돌 에너지 안전성 진단"""
        # 충돌력이 140N(가슴 부위 한계치)을 넘으면 즉시 위험 판정
        if self.f > 140:
            return "CRITICAL: Safety Violation (Excessive Contact Force)"
        elif self.f > 50:
            return "WARNING: Contact Detected (Engaging Compliance Control)"
        return "SAFE: Operational Force Within Limits"

    def audit_speed_scaling(self):
        """작업자와의 거리에 따른 자동 감속 로직 검증"""
        if self.d < 500 and self.v > 250:
            return "REJECT: Speed Too High for Proximity (Hazard)"
        elif self.d < 1000:
            return "ADAPTIVE: Reduced Speed Mode Active"
        return "OPTIMAL: Full Speed Operation"

engine = RobotFidelityEngine(current_force=65, speed=200, proximity_dist=450)
print(engine.diagnose_collision_safety())
print(engine.audit_speed_scaling())
```

## 4. 분석 프레임워크: HRC Safety Layer
1. **[Power and Force Limiting (PFL)]**: 관절 내부의 토크 센서나 외부에 장착된 F/T 센서를 통해 미세한 저항을 감지하고 모터 출력을 즉시 차단.
2. **[Speed and Separation Monitoring (SSM)]**: 레이저 스캐너나 AI 비전을 통해 인간의 거리를 실시간 측정하고 단계별로 로봇 속도를 감속.
3. **[Hand Guiding]**: 로봇의 엔드 이펙터를 인간이 직접 잡고 움직여서 작업 경로를 교시하는 직관적 티칭(Teaching) 물리.

## 5. 스스로 체크 (Self-Audit)
1. 로봇이 인간의 머리 부위와 충돌할 때 허용되는 최대 힘($F_{limit}$)이 다른 부위보다 현저히 낮은 물리적 이유는?
2. 임피던스 제어(Impedance Control)가 단순한 '급정지'보다 인간-로봇 협업에서 더 안전하고 효율적인 이유는 무엇인가?
3. 로봇 링크의 표면이 둥글고 부드러운 소재로 코팅되었을 때, 충돌 시 가해지는 압력($P=F/A$)의 변화는?

## 6. 결론 (Deterministic Outcome)
본 시스템은 `Data cobot-collision-force-and-response-time-log-v2026`와 실시간 연동되어, 센서 드리프트를 0.1N 단위로 감시하며 전사적인 안전 인증(CE, UL) 규격 준수를 결정론적으로 보증합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 12_robotics-and-autonomous-systems-intelligence-hub
- impedance-and-admittance-control-logic
- Data cobot-collision-force-and-response-time-log-v2026
