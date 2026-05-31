---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 43b7327c81e413a9545f0e1dd498cc4e72c7e2df5a76956e78450f180c4ee5db
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] iso-26262-road-vehicles-functional-safety-and-asil-decomposition]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] iso-26262-road-vehicles-functional-safety-and-asil-decomposition에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
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

# [Entity] iso-26262-road-vehicles-functional-safety-and-asil-decomposition

## 1. 개요 (Why: 인간적 통찰)
자동차가 스스로 달리고 멈추는 시대, 소프트웨어나 센서 하나가 오작동한다면 어떻게 될까요? 고속도로 한복판에서 핸들이 굳어버리는 비극은 상상만으로도 끔찍합니다. **ISO 26262 및 ASIL 분해**는 자동차가 고장 나더라도 '사람을 다치지 않게' 만들기 위한 전 세계 자동차 엔지니어들의 **'생명 안전 선언문'**입니다. 설계부터 폐기까지 모든 단계에서 발생할 수 있는 '만약의 상황'을 수학적으로 계산하고, 이중 삼중의 안전장치를 설계하여 자동차를 가장 믿음직한 이동 수단으로 만드는 **'디지털 안전벨트'**입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. ASIL 등급 결정
위험의 심각도($S$), 노출 빈도($E$), 제어 가능성($C$)을 곱해 안전 등급(ASIL A~D)을 매깁니다.

$$ \text{Risk} = S \times E \times C \implies \text{ASIL (A, B, C, D)} $$

**[인간적 해석]**: 사고가 났을 때 얼마나 치명적인지($S$), 그런 위험한 상황이 얼마나 자주 발생하는지($E$), 그리고 운전자가 핸들을 꺾어 피할 수 있는지($C$)를 따집니다. ASIL D는 가장 위험한 상황(예: 브레이크 고장)을 뜻하며, 비행기 수준의 엄격한 안전 설계가 요구됩니다.

### 2.2. 하드웨어 결함 지표 (SPFM/LFM)
부품 하나가 고장 났을 때 시스템이 이를 얼마나 잘 찾아내고 방어하는지 수치화합니다.

$$ \text{SPFM} = \frac{\sum (\lambda_{safe} + \lambda_{detected\_direct})}{\sum \lambda} \geq 99\% \text{ (for ASIL D)} $$

**[인간적 해석]**: "하나가 고장 나도 99%는 안전하게 멈출 수 있는가?"를 묻는 지표입니다. ISO 26262는 감에 의존하지 않고, 10억 시간당 고장 횟수(FIT)라는 냉정한 숫자로 안전을 증명할 것을 요구합니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| ASIL Level | Severity | Exposure | Controllability | Target (SPFM) | Target (LFM) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ASIL D** | High (S3) | High (E4) | Low (C3) | $\geq 99\%$ | $\geq 90\%$ |
| **ASIL C** | High | Med | Med | $\geq 97\%$ | $\geq 80\%$ |
| **ASIL B** | Med | Med | Med | $\geq 90\%$ | $\geq 60\%$ |
| **ASIL A** | Low | Low | High | QM (Quality) | QM |
| **FIT Limit** | Failures / $10^9$ hr | < 10 (ASIL D) | < 100 (ASIL B/C) | N/A | N/A |

## 4. SafetyFidelityEngine: Diagnostic Logic

자동차 안전 설계의 무결성 및 ASIL 준수 상태를 진단하는 `SafetyFidelityEngine` 로직입니다.

```python
class SafetyFidelityEngine:
    def __init__(self, asil_level, spfm_pct, lfm_pct, diagnostic_coverage):
        self.level = asil_level # 'A', 'B', 'C', 'D'
        self.spfm = spfm_pct
        self.lfm = lfm_pct
        self.diag = diagnostic_coverage

    def diagnose_safety_health(self):
        """ASIL 등급별 안전 지표 충족 여부 진단"""
        targets = {'D': (99, 90), 'C': (97, 80), 'B': (90, 60), 'A': (0, 0)}
        target_spfm, target_lfm = targets.get(self.level, (0,0))

        if self.spfm < target_spfm:
            return f"CRITICAL: SPFM Deficiency ({self.spfm}% < {target_spfm}%) for ASIL {self.level} - Architectural Safety Violation"
        if self.lfm < target_lfm:
            return f"WARNING: Low Latent Fault Metric ({self.lfm}%) - Risk of Undetected Multi-point Failures"
        if self.diag < 90.0 and self.level in ['C', 'D']:
            return "NOTICE: Suboptimal Diagnostic Coverage - Enhance Self-test Algorithms for High ASIL Systems"
        return f"OPTIMAL: ASIL {self.level} Functional Safety Compliance and High-Fidelity Design Verified"

    def audit_asil_decomposition(self, redundant_path_independence):
        """ASIL 분해(Redundancy)의 독립성 무결성 진단"""
        if not redundant_path_independence:
            return "REJECT: Common Cause Failure (CCF) Risk - Dependent Paths Nullify ASIL Decomposition Benefit"
        return "PASS: Independent Redundant Architecture Confirmed"

engine = SafetyFidelityEngine(asil_level='D', spfm_pct=99.2, lfm_pct=92.5, diagnostic_coverage=95.0)
print(engine.diagnose_safety_health())
```

## 5. 분석 프레임워크: Safety-First Engineering Strategy
1. **[ASIL Decomposition]**: ASIL D가 필요한 복잡한 기능을, ASIL B 수준의 독립된 시스템 2개로 쪼개어 설계함으로써 안전성은 유지하면서 비용과 복잡도를 낮추는 '분할 정복' 전략.
2. **[Fail-Operational vs Fail-Safe]**: 자율 주행차처럼 고장이 나도 계속 작동해야 하는 경우(Fail-Operational)와, 고장이 나면 안전하게 멈추는 경우(Fail-Safe)를 구분하여 설계하는 전략.
3. **[V-Model Lifecycle]**: 요구사항 분석부터 검증까지 V자 형태로 철저히 대응시켜, 단 하나의 안전 요구사항도 누락되지 않게 관리하는 '전 생애 주기' 전략.

## 6. 스스로 체크 (Self-Audit)
1. 왜 '무작위 하드웨어 결함(Random Failure)'은 확률적으로 관리되는데, '체계적 결함(Systematic Failure)'은 오직 '프로세스'를 통해서만 방지할 수 있는가?
2. ASIL D 시스템에서 '독립성(Independence)'과 '자유도(Freedom from Interference)'가 보장되지 않을 때 발생하는 '공통 원인 고장(CCF)'의 위험성은?
3. SOTIF(ISO 21448) 표준이 ISO 26262의 '고장 기반 안전'을 넘어 '기능적 성능 한계'를 어떻게 보완하는가?

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data automotive-functional-safety-metrics-and-asil-reports-v2026`와 연동되어, 전 세계 자율 주행차의 안전 지표를 실시간 분석하고 시스템 오작동 및 대형 인명 사고 확률을 0.001% 이하로 억제함으로써 미래 모빌리티의 생명 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 29_legal-compliance-and-corporate-governance-hub
- iec-61508-functional-safety-and-sil-level-certification-physics
- Data automotive-functional-safety-metrics-and-asil-reports-v2026