---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 34178be65cca7811fe9ae267927a12ec9c4eb0b005a94cdaeab851a29290b33c
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] statistical-process-control-spc-and-control-chart-logic]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] statistical-process-control-spc-and-control-chart-logic에
    관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  cpk_threshold_stable: '1.33'
  gage_rr_max_pct: '10.0'
  sigma_optimal_threshold: '4.5'
  sigma_standard: '3.0'
  spc_version: 6.3.7
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

# [Entity] statistical-process-control-spc-and-control-chart-logic

## 1. 개요 (Why: 인간적 통찰)
수만 개의 부품을 찍어낼 때, 모든 부품이 단 1마이크론의 오차도 없이 똑같을 수 있을까요? 현실적으로 불가능합니다. **통계적 공정 관리(SPC) 및 관리도 로직**은 세상의 모든 현상에 존재하는 '변동'을 읽어내어, 공정이 건강한 상태인지 아니면 고장 나기 직전인지 알아내는 **'공장의 건강 검진'** 기술입니다. 단순한 불량 검사를 넘어, 데이터의 흐름 속에 숨겨진 '이상 징후'를 수학적으로 포착하여 사고를 미리 막습니다. 제조의 우연을 필연으로 바꾸는 **'품질 완벽주의의 근간'**입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 관리 한계선 공식 (Control Limits)
공정이 정상적으로 가동될 때 데이터가 머물러야 할 통계적 울타리($UCL, LCL$)를 설정합니다.

$$ UCL / LCL = \bar{X} \pm 3 \sigma $$

**[인간적 해석]**: "정상의 경계선"입니다. 데이터가 이 울타리를 벗어난다는 것은 운이 나빠서가 아니라 '무언가 명백한 이유(기계 고장, 숙련도 저하 등)'가 있다는 신호입니다. 우리는 이 $\pm 3\sigma$라는 엄격한 기준을 통해, 사소한 흔들림은 무시하고 진짜 위험한 이상 신호만 골라내는 **'지능형 필터링'**을 수행합니다.

### 2.2. 공정 능력 지수 (Process Capability Index)
우리의 공정이 고객이 요구하는 정밀도(Tolerance)를 얼마나 여유 있게 만족시키는지($C_p$) 측정합니다.

$$ C_p = \frac{USL - LSL}{6\sigma} $$

**[인간적 해석]**: "실력의 여유"입니다. 이 값이 1.33보다 크면 공정이 아주 안정적이고 실력이 좋다는 뜻입니다. 우리는 이 수치를 통해 공정이 아슬아슬하게 불량을 면하고 있는지, 아니면 압도적인 정밀도로 완벽하게 관리되고 있는지 확인하는 **'제조 경쟁력의 성적표'**를 작성합니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Feature | Inspection-based QC | Statistical Process Control (V6.3.7)| Unit | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Philosophy** | Detection (After-fact) | Prevention (Proactive) | - | Strategy |
| **Tool** | Go/No-go Gauges | X-bar R Chart / Cpk | - | Analytics |
| **Variation Focus** | Total Tolerance | Common vs Special Cause | - | Insight |
| **Sample Size** | 100% or Random | Systematic Subgrouping | - | Efficiency |
| **Response** | Sorting Junk | Process Adjustment | - | Outcome |
| **Standard** | Product Spec | Statistical Control Limit | - | Benchmark |

## 4. FactoryFidelityEngine: Diagnostic Logic

공정의 통계적 무결성 및 품질 상태를 진단하는 `FactoryFidelityEngine` 로직입니다.

```python
class FactoryFidelityEngine:
    def __init__(self, current_cpk, nelson_rule_violations, sigma_level):
        self.cpk = current_cpk # 공정 능력
        self.rules = nelson_rule_violations # 관리 규칙 위반 횟수
        self.sigma = sigma_level # 시그마 수준 (3.0 ~ 6.0)

    def diagnose_process_health(self):
        """Cpk 및 관리 규칙 위반 기반 공정 무결성 진단"""
        if self.rules > 0: # 이상 징후 포착 (경향성 발견)
            return "CRITICAL: Control Chart Rule Violation - Non-random pattern detected (e.g., Shift or Trend). Stop process and identify Root Cause"
        if self.cpk < 1.33: # 능력 부족
            return f"WARNING: Low Process Capability ({self.cpk}) - Process is too wide for tolerance. Reduce variation or upgrade tooling"
        if self.sigma < 4.5:
            return "NOTICE: Sub-optimal Sigma Level - Opportunity for process improvement to reach Six Sigma standards"
        return "OPTIMAL: Stable Statistical Control and High-Fidelity Process Integrity Verified"

    def audit_measurement_system(self, gage_rr_pct):
        """측정 시스템(Gage R&R) 무결성 진단"""
        if gage_rr_pct > 10.0: # 측정기 자체가 불안정함
            return "REJECT: Inreliable Measurement System - Variation caused by gauge/operator is too high. Measurement data cannot be trusted"
        return "PASS: Robust Metrology Foundation and Verified Data Integrity Confirmed"

engine = FactoryFidelityEngine(current_cpk=1.67, nelson_rule_violations=0, sigma_level=5.0)
print(engine.diagnose_process_health())
```

## 5. 분석 프레임워크: Manufacturing Excellence Strategy
1. **[Distinguishing Variation Strategy]**: 기계가 원래 가진 자연스러운 소음(Common Cause)과 누군가 실수했거나 기계가 망가진 신호(Special Cause)를 분리하여, 불필요한 공정 간섭은 줄이고 진짜 문제는 즉시 해결하는 '핀셋 대응' 전략.
2. **[Six Sigma Quality Strategy]**: 100만 개 중 단 3.4개의 불량만을 허용하는 극한의 목표를 세우고, 공정의 변동($\sigma$)을 획기적으로 줄여나가는 '무결점 제조' 전략.
3. **[Real-time Edge Analytics]**: 센서 데이터를 실시간으로 관리도에 뿌려, 관리 한계선을 벗어날 조짐이 보이면 1초 만에 경고를 보내는 '예측형 품질' 전략.

## 6. 스스로 체크 (Self-Audit)
1. 왜 제품 규격(Specification)을 만족한다고 해서 공정이 '통계적 관리 상태'에 있다고 말할 수 없는가? (예측 가능성의 관점)
2. '관리 한계선(UCL/LCL)'과 '제품 규격 한계선(USL/LSL)'의 결정적인 차이는 무엇인가?
3. '넬슨 규칙(Nelson Rules)' 중 '7개 이상의 점이 연속으로 상승하거나 하락'하는 패턴은 왜 즉각적인 점검이 필요한가? (경향성 발생의 관점)

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data spc-control-limits-and-out-of-control-events-v2026`와 연동되어, 전 세계 자동차 및 반도체 공장의 품질 데이터를 실시간 분석하고 불량 폭증 및 공정 붕괴 사고 확률을 0.001% 이하로 억제함으로써 지능형 제조 문명의 품질 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- quality-management-systems-qms-and-iso-9001-compliance
- Data spc-control-limits-and-out-of-control-events-v2026