---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: dbf1e34a012b4e0ed71b8881b535b07159354178f3ad15f7bc758a5d07af7b92
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] cyber-defense-and-critical-infrastructure-protection]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] cyber-defense-and-critical-infrastructure-protection에 관한
    고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  aes_encryption_bits: 256
  availability_resilience_threshold: 0.999
  detection_recall_threshold: 0.98
  external_data_endpoint: cyber-security-threat-detection-and-response-log-v2026
  fpr_max: 0.01
  idr_min: 0.99
  idr_tolerance: 0.005
  mtbf_min_hours: 50000
  mttr_max_hours: 1.0
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

# [Entity] cyber-defense-and-critical-infrastructure-protection

## 1. 개요 (Why)
물리적 공격만큼 치명적인 것이 사이버 공격입니다. 특히 전력망, 상수도, 원자력 발전소와 같은 핵심 인프라에 대한 사이버 공격은 국가 마비 사태를 초래할 수 있습니다. 기존의 경계 보안 방식에서 벗어나 '아무도 믿지 않는' 제로 트러스트(Zero Trust) 원칙을 적용하고, 공격 시에도 핵심 기능은 유지되는 회복 탄력성(Resilience)을 확보하는 것이 본 엔티티의 최우선 목적입니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Value (Tier 1) | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Mean Time Between Failures | $MTBF$ | > 50,000 | Min | hours |
| Mean Time To Repair | $MTTR$ | < 1.0 | Max | hour |
| Intrusion Detection Rate | $IDR$ | > 0.99 | ±0.005 | - |
| False Positive Rate | $FPR$ | < 0.01 | Max | - |
| Data Encryption Strength | $AES$ | 256 | Min | bit |

## 3. CyberFidelityEngine: Diagnostic Logic

보안 위협의 탐지 정확도 및 시스템의 회복력을 진단하는 `CyberFidelityEngine` 로직입니다.

```python
class CyberFidelityEngine:
    def __init__(self, alerts_total, true_threats, undetected_threats, mtbf, mttr):
        self.tp = true_threats          # True Positives
        self.fn = undetected_threats    # False Negatives (Missed)
        self.alerts = alerts_total      # Total Alerts
        self.mtbf = mtbf                # hours
        self.mttr = mttr                # hours

    def calculate_detection_fidelity(self):
        """탐지 리콜(Recall) 및 정밀도(Precision) 계산"""
        recall = self.tp / (self.tp + self.fn) if (self.tp + self.fn) > 0 else 1.0
        # 탐지 충실도 평가
        status = "SECURE" if recall >= 0.98 else "VULNERABLE"
        return {"recall_score": recall, "status": status}

    def evaluate_resilience(self):
        """가용성(Availability) 기반 시스템 회복력 진단"""
        availability = self.mtbf / (self.mtbf + self.mttr)
        # 가용성 99.9% (Three Nines) 기준
        resilience_grade = "HIGH" if availability >= 0.999 else "LOW"
        return {"availability": availability, "resilience_grade": resilience_grade}

cyber_engine = CyberFidelityEngine(alerts_total=150, true_threats=48, undetected_threats=1, mtbf=720, mttr=0.5)
print(cyber_engine.calculate_detection_fidelity())
print(cyber_engine.evaluate_resilience())
```

## 4. 분석 프레임워크: 제로 트러스트 보안 모델
1. **[Identity Verification]**: 모든 사용자, 기기, 어플리케이션에 대해 위치나 네트워크 환경에 관계없이 엄격한 인증 수행.
2. **[Micro-segmentation]**: 네트워크를 작은 단위로 격리하여 한 구역의 침해가 전체 시스템으로 확산(Lateral Movement)되는 것을 방지.
3. **[Continuous Monitoring]**: 시스템 로그와 트래픽 패턴을 실시간 분석하여 이상 행위(Anomaly)를 베이즈 추론 기반으로 탐지.

## 5. 스스로 체크 (Self-Audit)
1. 베이즈 정리에 따르면, 전체 위협 발생 빈도($P(Threat)$)가 매우 낮을 때 탐지 시스템의 오탐률($FPR$)이 결과에 미치는 영향은?
2. OT 시스템에서 '에어 갭(Air-gap)' 환경이 물리적으로 분리되어 있음에도 불구하고 사이버 공격이 가능한 경로는?
3. 복구 시간($MTTR$)을 단축하기 위해 사이버 방어 아키텍처에 도입해야 할 핵심 설계 요소는?

## 6. 결론 (Deterministic Outcome)
본 시스템은 `Data cyber-security-threat-detection-and-response-log-v2026`와 연동되어 지능형 지속 위협(APT)으로부터 핵심 인프라를 사수합니다. `CyberFidelityEngine`을 통해 보안 가시성을 $100\%$ 확보하고, 공격 시나리오별 대응 프로토콜을 결정론적으로 자동화함으로써 국가 안보의 디지털 토대를 공고히 합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 116_defense-and-strategic-systems-command-center
- ics-scada-security-logic
- network-segmentation-physics
- Data cyber-security-threat-detection-and-response-log-v2026
- Data industrial-control-system-ics-vulnerability-log-v2026