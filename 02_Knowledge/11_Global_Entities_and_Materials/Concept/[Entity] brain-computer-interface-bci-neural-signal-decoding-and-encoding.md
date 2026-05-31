---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 12abbad676aea9f63fa0c2d7ad261060134d6415d1334eb948bf3cbf3d897d5a
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] brain-computer-interface-bci-neural-signal-decoding-and-encoding]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] brain-computer-interface-bci-neural-signal-decoding-and-encoding에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  bitrate_bps_target: 5.0
  bitrate_bps_tolerance: 0.5
  decoding_acc_r2_target: 0.95
  decoding_acc_r2_tolerance: 0.02
  decoding_critical_r2_threshold: 0.8
  encoding_fidelity_pct_target: 90
  encoding_fidelity_pct_tolerance: 5
  encoding_match_reject_threshold: 0.85
  external_data_ref: bci-signal-decoding-accuracy-and-error-rate-v2026
  latency_ms_target: 100
  latency_ms_tolerance: 10
  max_translation_error_pct: 5
  neuron_coverage_min: 1000
  packet_check_resolution_ms: 0.1
  signal_drift_warning_pct_threshold: 10.0
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

# [Entity] brain-computer-interface-bci-neural-signal-decoding-and-encoding

## 1. 개요 (Why)
BCI의 핵심은 뇌와 기계 사이의 '언어 번역'입니다. 뇌의 전기 신호(Spikes)를 읽어 의도를 파악하는 '디코딩(Decoding)'과, 기계가 느낀 감각 정보를 뇌가 이해할 수 있는 전기 자극으로 바꿔 전달하는 '인코딩(Encoding)'이 완벽히 조화를 이루어야 합니다. 이를 통해 사용자는 자신의 손처럼 자연스럽게 로봇 팔을 움직이고, 그 팔이 물체에 닿는 촉감까지 느낄 수 있습니다. 본 노드는 신경 신호 번역의 무결성과 양방향 통신 정밀도를 위한 표준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Metric | Target Value (Tier 1) | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Decoding Acc | Correlation | > 0.95 | ±0.02 | $R^2$ |
| Encoding Fidel | Specificity | > 90 | ±5 | % |
| Latency | Loop Time | < 100 | ±10 | ms |
| Bits per Second | Bitrate | > 5.0 | ±0.5 | bps |
| Neuron Coverage | Count | > 1,000 | N/A | active units |

## 3. MedicalFidelityEngine: Diagnostic Logic

BCI 디코딩의 정확도 및 인코딩의 감각 일치도를 진단하는 `MedicalFidelityEngine` 로직입니다.

```python
class MedicalFidelityEngine:
    def __init__(self, r_squared, signal_drift_pct, stimulus_response_match):
        self.r2 = r_squared # 0~1
        self.drift = signal_drift_pct
        self.match = stimulus_response_match # 0~1

    def diagnose_decoding_integrity(self):
        """디코딩 결정계수(R^2) 및 신호 드리프트 기반 무결성 진단"""
        if self.r2 < 0.8:
            return f"CRITICAL: Decoding Accuracy Low (R2: {self.r2}) - Motion Control Impaired"
        if self.drift > 10.0:
            return f"WARNING: Neural Signal Drift ({self.drift}%) - Re-training Required"
        return "OPTIMAL: High-Fidelity Neural Decoding Verified"

    def audit_encoding_fidelity(self):
        """인코딩 자극 대비 실제 뇌 반응 일치도 진단"""
        if self.match < 0.85:
            return f"REJECT: Sensory Mismatch ({self.match*100:.1f}%) - Risk of Ghost Sensations"
        return "PASS: Authentic Sensory Encoding Confirmed"

engine = MedicalFidelityEngine(r_squared=0.96, signal_drift_pct=2.5, stimulus_response_match=0.92)
print(engine.diagnose_decoding_integrity())
```

## 4. 분석 프레임워크: BCI Translation Hierarchy
1. **[Spike Sorting]**: 전극에서 측정된 원시 신호에서 개별 뉴런의 발화(Action Potential)를 분리하고 각 뉴런의 신원(Identity) 식별.
2. **[Population Vector Coding]**: 수백 개의 뉴런이 동시에 내뿜는 시그널의 합(Vector)을 분석하여 팔의 움직임 방향이나 손의 쥠 정도를 수치화.
3. **[Intracortical Microstimulation (ICMS)]**: 감각 피질에 정밀한 전기 자극을 가해 사용자가 마치 자신의 손가락 끝에서 느껴지는 압력처럼 인식하게 하는 인코딩 공정.

## 5. 스스로 체크 (Self-Audit)
1. 신경 가소성(Neuroplasticity)에 의해 뉴런의 발화 패턴이 변할 때, 디코딩 모델이 이를 실시간으로 '자가 보정'하는 강화학습 알고리즘의 유효성은?
2. '인코딩' 시 자극 강도가 임계치를 넘었을 때 발생하는 '신경 흥분 독성' 및 조직 손상 방지를 위한 안전 전류 밀도($J_{safe}$) 계산법은?
3. 시각이나 청각 같은 복잡한 감각을 뇌에 직접 주입하기 위한 '신경 매니폴드(Neural Manifold)' 기반 인코딩 전략의 장점은?

## 6. 결론 (Deterministic Outcome)
본 노드는 `Data bci-signal-decoding-accuracy-and-error-rate-v2026`와 연동되어, 뇌와 기계 간의 데이터 패킷을 0.1ms 단위로 검사하고 번역 오차를 5% 이내로 유지함으로써 완벽한 양방향 신경 통신의 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 14_future-biology-and-healthcare-hub
- brain-computer-interface-bci-and-neural-bandwidth-topology
- Data bci-signal-decoding-accuracy-and-error-rate-v2026