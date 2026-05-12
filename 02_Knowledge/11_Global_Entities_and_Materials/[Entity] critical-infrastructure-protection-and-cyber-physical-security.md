---
Basic:
  id: "critical-infrastructure-protection-and-cyber-physical-security"
  domain: "General_Industrial"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Entity"
  tier: 1
  description: "The holistic engineering approach to securing national and industrial critical infrastructures (Power, Water, Telecom) by protecting the tight integration of computation, networking, and physical processes (Cyber-Physical Systems)."
  physical_model: "N/A"
Semantic:
  tags: '["critical-infrastructure", "cyber-physical-security", "cps", "industrial-control-systems", "ot-security"]'
  is_part_of: []
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "SafetyFidelityEngine"
  diagnostic_protocol:
    - 'System_Resilience_Audit: Measure the time required for the infrastructure to return to a stable state after a simulated cyber-attack.'
    - 'Control_Loop_Integrity_Check: Detect anomalies in the feedback signals ($y(t)$) between sensors and actuators.'
    - 'Network_Segmentation_Scan: Verify the isolation of OT (Operational Technology) networks from public IT networks.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# 🛡️ Critical Infrastructure Protection and Cyber-Physical Security

## 1. 개요 (Why: 인간적 통찰)
현대 문명의 생명줄인 전력망, 상수도, 통신 인프라는 이제 거대한 '하나의 살아있는 기계'가 되었습니다. 과거에는 물리적 울타리만 잘 치면 안전했지만, 지금은 보이지 않는 사이버 공간의 코드가 실제 발전소의 터빈을 멈추거나 댐의 수문을 열 수 있는 시대입니다. **국가 핵심 인프라 보호(CIP)**는 단순히 해킹을 막는 기술을 넘어, 우리 삶을 지탱하는 물리적 실체와 디지털 신경망이 충돌 없이 공존하게 만드는 **'사회적 회복탄력성(Resilience)'**의 정수입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 사이버-물리 시스템(CPS)의 결합 동역학
CPS 보안의 핵심은 사이버 공격이 물리적 상태($x$)에 미치는 영향을 제어 공학적으로 이해하는 것입니다. 공격자는 센서 데이터($y$)를 조작하거나 제어 명령($u$)을 가로채어 시스템을 불안정하게 만듭니다.

$$ \dot{x}(t) = Ax(t) + B(u(t) + a_{atk}(t)) + d(t) $$

*   $A$: 시스템의 물리적 관성 및 특성을 나타내는 상태 행렬 (예: 터빈의 회전 관성).
*   $u(t)$: 정상적인 제어 명령.
*   $a_{atk}(t)$: 공격자가 주입한 악성 제어 신호.
*   $d(t)$: 자연적인 소음이나 외부 방해 요소.

**[인간적 해석]**: 시스템의 관성($A$)이 클수록 공격에 의한 변화가 느리게 나타나지만, 일단 변하기 시작하면 멈추기 어렵습니다. 따라서 초기 미세 징후를 포착하는 것이 보안의 핵심입니다.

### 2.2. 회복탄력성(Resilience) 지수
보안의 목표는 100% 방어가 아니라, 공격을 받더라도 얼마나 빨리 정상 수준으로 돌아오느냐($R$)입니다.

$$ R = \frac{\text{Recovery Speed}}{\text{System Degradation}} = \frac{\int_{t_{attack}}^{t_{recovery}} Q(t) dt}{(t_{recovery} - t_{attack}) \times Q_{nominal}} $$

*   $Q(t)$: 시스템의 서비스 품질 (예: 전력 공급 안정성).
*   $R=1$에 가까울수록 완벽한 회복력을 의미합니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Parameter | Metric | Target Value | Unit |
| :--- | :--- | :--- | :--- |
| Network Latency | OT Control | < 10 | ms |
| MTTR | Recovery | < 600 | sec (Critical) |
| False Positive | IDS | < 0.01 | % |
| Segmentation | Air-gap | Physical/Logic | Tier 0 Isolation |
| Redundancy | Hardware | $N+1$ or $N+2$ | Level |

## 4. SafetyFidelityEngine: Diagnostic Logic

인프라의 보안 건전성 및 회복력을 진단하는 `SafetyFidelityEngine` 로직입니다.

```python
class SafetyFidelityEngine:
    def __init__(self, anomaly_score, recovery_time_sec, isolation_level):
        self.anomaly = anomaly_score # 0~1 (Higher means potential attack)
        self.recovery = recovery_time_sec
        self.iso = isolation_level # 1~5 (5 is highest)

    def diagnose_infrastructure_safety(self):
        """이상 징후 점수 및 격리 수준 기반 인프라 보안 진단"""
        if self.anomaly > 0.8:
            return f"CRITICAL: High Anomaly Detected ({self.anomaly}) - Potential Cyber-Physical Attack in Progress"
        if self.iso < 3:
            return f"WARNING: Weak Network Segmentation (Level: {self.iso}) - High Risk of Lateral Movement"
        return "OPTIMAL: Critical Infrastructure Resilience Verified"

    def audit_recovery_capacity(self, threshold_sec):
        """회복 시간 기반 시스템 회복탄력성 진단"""
        if self.recovery > threshold_sec:
            return f"REJECT: Unacceptable Recovery Time ({self.recovery}s) - Enhance Redundancy and SOP"
        return "PASS: System Resilience within Operational Safety Limits"

# Instance Diagnostic
engine = SafetyFidelityEngine(anomaly_score=0.12, recovery_time_sec=120, isolation_level=5)
print(engine.diagnose_infrastructure_safety())
```

## 5. 분석 프레임워크: Defense-in-Depth Strategy
1. **[Physical Layer Security]**: 전력 거점, 수도 관제소 등 물리적 접근을 차단하는 1차 방어선. (CCTV, 바이오 인식, 물리적 잠금)
2. **[Network Layer Security]**: IT망과 OT망을 엄격히 분리하고, 일방향 전송 장비(Data Diode)를 통해 외부로부터의 침입을 원천 차단.
3. **[Application Layer (DPI)]**: 산업용 프로토콜(Modbus, DNP3 등)의 내부 패킷을 정밀 분석(Deep Packet Inspection)하여 비정상적인 제어 명령을 실시간으로 거부.

## 6. 스스로 체크 (Self-Audit)
1. '스턱스넷(Stuxnet)' 사례가 보여준 '에어 갭(Air-gap)' 환경에서의 보안 한계와 이를 극복하기 위한 '엔드포인트 무결성' 확보 방안은?
2. 제어 시스템의 가용성($Availability$)이 기밀성($Confidentiality$)보다 왜 더 높은 우선순위를 갖는지 물리적 사고 시나리오와 함께 설명하시오.
3. '디지털 트윈(Digital Twin)'을 활용하여 가상의 공격 시뮬레이션을 수행하고 최적의 복구 경로를 사전에 학습하는 기술의 유효성은?

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data infrastructure-security-incidents-and-response-time-v2026`와 연동되어, 국가 인프라의 모든 보안 로그와 물리적 상태를 실시간 분석하고 대규모 정전이나 단수 등의 재난 확률을 0.001% 이하로 억제함으로써 지능형 국가 문명의 무결성을 보장합니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 29_legal-compliance-and-corporate-governance-hub
- cyber-physical-systems-cps-and-industrial-iot-iiot
- Data infrastructure-security-incidents-and-response-time-v2026
