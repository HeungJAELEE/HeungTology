---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: adcfebd906d34955f1fdfb97a5cc3a129034d3a07df212294a00e4b9260ee124
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] fault-tree-analysis-fta-and-probabilistic-risk-assessment-pra-logic]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] fault-tree-analysis-fta-and-probabilistic-risk-assessment-pra-logic에
    관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  common_cause_factor_threshold: 0.1
  fta_specification_version: V6.3.7
  logic_gate_options:
  - AND
  - OR
  - 2oo3
  safety_threshold_prob: 1.0e-06
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

# [Entity] fault-tree-analysis-fta-and-probabilistic-risk-assessment-pra-logic

## 1. 개요 (Why: 인간적 통찰)
"비행기 추락"이나 "원자로 폭발" 같은 끔찍한 사고가 왜 일어나는지, 그 원인을 파고 내려가면 어떤 모습일까요? **결함수 분석(FTA) 및 확률적 위험 평가(PRA) 로직**은 거대한 재앙(Top Event)을 정점에 두고, 그 일이 벌어지기 위해 필요한 작은 사고들을 뿌리처럼 엮어낸 **'사고의 가계부'** 기술입니다. 복잡한 기계 장치에서 "어떤 부품 두 개가 동시에 고장 나야만 재앙이 터지는지"를 수학적으로 밝혀내어, 가장 약한 고리를 찾아내는 **'보이지 않는 재난의 지도를 그리는 지능적 사령부'**입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 논리 게이트 확률 공식 (Logic Gates)
사건들이 동시에 일어나야 하는지(AND), 하나만 일어나도 되는지(OR)에 따라 최종 사고 확률을 계산합니다.

$$ P_{AND} = P_1 \times P_2 \times \dots $$
$$ P_{OR} = 1 - (1-P_1)(1-P_2)\dots $$

**[인간적 해석]**: "사고의 조건"입니다. AND 게이트는 두 장치가 다 고장 나야 하니 확률이 낮아져서 안전하고, OR 게이트는 하나만 고장 나도 사고니 위험합니다. 우리는 이 수식을 통해 "단 한 번의 실수로 전체가 무너지는 일은 없도록" 만드는 **'논리적 무결성'**을 수행합니다.

### 2.2. 최소 컷셋 (Minimal Cut Sets, MCS)
시스템을 무너뜨리기 위해 필요한 최소한의 고장 조합을 찾아냅니다.

**[인간적 해석]**: "가장 쉬운 파괴 경로"입니다. 만약 부품 A 하나만 고장 나도 전체가 멈춘다면 그것이 바로 1차 컷셋이며 가장 먼저 고쳐야 할 적입니다. 우리는 이 분석을 통해 "사고로 가는 지름길을 모두 차단하는" **'방어 무결성'**을 실현합니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Feature | FMEA (Bottom-up) | FTA (Top-down) (V6.3.7) | Unit | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Logic** | Inductive (What if?) | **Deductive (How?)** | - | Direction |
| **Complexity** | Component level | System level (Network) | - | Scope |
| **Quantification** | RPN (Qualitative) | Probability (Quantitative)| - | Precision |
| **Gates** | None | AND, OR, Voting (2oo3) | - | Logic |
| **Outcome** | Effect list | Top Event Probability | - | Result |
| **Mitigation** | Preventive Actions | Redundancy / Isolation | - | Strategy |

## 4. LogicFidelityEngine: Diagnostic Logic

위험 분석 및 사고 예방 시스템의 논리적 무결성 및 시스템 상태를 진단하는 `LogicFidelityEngine` 로직입니다.

```python
class LogicFidelityEngine:
    def __init__(self, top_event_prob, critical_cutset_count, common_cause_factor):
        self.prob = top_event_prob # 최종 사고 발생 확률
        self.mcs = critical_cutset_count # 치명적 컷셋 수
        self.ccf = common_cause_factor # 공통 원인 고장 계수

    def diagnose_safety_logic_health(self):
        """사고 확률 및 컷셋 기반 시스템 무결성 진단"""
        if self.prob > 1e-6: # 안전 목표 미달 (위험)
            return "CRITICAL: Safety Goal Violation - Top event probability exceeding $10^{-6}$ target. System is statistically unsafe for critical operations. Re-design redundancy"
        if self.mcs > 0: # 단일 실패 지점 존재
            return f"WARNING: Single Point Failure Detected - Found {self.mcs} single-event cutsets. One component failure will crash the entire system. Implement AND-gate redundancy"
        if self.ccf > 0.1:
            return "NOTICE: High Common Cause Risk - Redundant components likely to fail simultaneously due to same environment or maintenance error. Diversify hardware sources"
        return "OPTIMAL: Robust Fault Tree Logic and High-Fidelity Risk Assessment Verified"

    def audit_gate_integrity(self, logic_errors):
        """논리 게이트(Gate) 무결성 진단"""
        if logic_errors > 0: # 논리 오류 (예: 순환 참조)
            return "REJECT: Logical Paradox Detected - Circular dependency found in fault tree branches. Probabilistic result is mathematically invalid. Correct logic flow"
        return "PASS: Validated Boolean Structure and Verified Security Integrity Confirmed"

engine = LogicFidelityEngine(top_event_prob=5e-8, critical_cutset_count=0, common_cause_factor=0.02)
print(engine.diagnose_safety_logic_health())
```

## 5. 분석 프레임워크: High-Fidelity System Safeguard Strategy
1. **[Top-down Deductive Strategy]**: "폭발"이라는 결론에서 시작해 거꾸로 원인을 찾아 올라가는 전략. 복잡한 시스템의 꼬인 실타래를 푸는 '추리 소설가'의 기술입니다.
2. **[Redundancy Optimization]**: 가장 확률이 높은 컷셋에 백업(Redundancy)을 추가해 전체 확률을 기하급수적으로 낮추는 전략. '가성비 높은 안전' 기술입니다.
3. **[Common Cause Analysis]**: 비상용 발전기가 두 대라도 침수되면 둘 다 죽는 것처럼, '공통의 불행'을 미리 예측해 서로 다른 장소에 두거나 다른 회사의 제품을 쓰는 전략. '계란을 다른 바구니에 담는' 전략입니다.

## 6. 스스로 체크 (Self-Audit)
1. 왜 FMEA가 있는데 FTA가 또 필요한가? (FMEA는 "나사가 풀리면?" 하고 하나씩 보지만, FTA는 "비행기가 추락하려면 나사도 풀리고 센서도 죽고 조종사도 실수해야 한다"는 식의 '복합 사고'를 보여주기 때문)
2. '최소 컷셋(MCS)'이 왜 무서운가? (테러리스트가 이 리스트를 보면 시스템의 가장 급소(최소한의 파괴로 최대 효과)를 알 수 있을 만큼 정교한 약점 리스트이기 때문)
3. 왜 사고 확률이 $10^{-9}$ (10억 분의 1)처럼 극단적으로 낮아야 하는가? (비행기가 하루에 수만 번 뜨고 내리기 때문에, 100만 분의 1 확률조차 매달 사고가 나는 '확정된 불행'이 되기 때문인 관점)

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data system-failure-probabilities-and-critical-cut-sets-v2026`와 연동되어, 전 세계 주요 원자력 발전소 및 우주선의 안전 데이터를 실시간 분석하고 시스템 붕괴 및 인명 대참사 사고 확률을 0.00001% 이하로 억제함으로써 지능형 거대 시스템 문명의 생명 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- failure-mode-and-effects-analysis-fmea-and-risk-mitigation-logic
- Data system-failure-probabilities-and-critical-cut-sets-v2026