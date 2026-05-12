---
Basic:
  id: "manufacturing-resource-planning-mrp-ii-and-enterprise-logic"
  domain: "General_Industrial"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Entity"
  tier: 1
  description: "An integrated information system used by businesses to plan all resources of a manufacturing company (Manufacturing Resource Planning), evolving from MRP to include financial, engineering, and human resource planning with feedback loops (Enterprise Logic)."
  physical_model: "N/A"
Semantic:
  tags: '["mrp-ii", "manufacturing-resource-planning", "erp-precursor", "closed-loop-mrp", "capacity-planning", "production-logic", "enterprise-resource"]'
  is_part_of: []
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "LogicFidelityEngine"
  diagnostic_protocol:
    - 'Closed_Loop_Fidelity_Audit: Evaluate the high-fidelity ''Feedback Delay'' between shop-floor execution and master scheduling to identify if high-fidelity ''Plan Inaccuracy'' is causing resource idle time.'
    - 'Capacity_Load_Fidelity_Check: Analyze the high-fidelity ''Workload Distribution'' across work centers to ensure that high-fidelity ''Overload'' or high-fidelity ''Underutilization'' is not disrupting the production flow.'
    - 'Financial_Sync_Fidelity_Scan: Verify the high-fidelity ''Costing Accuracy'' by comparing estimated resource costs with actual high-fidelity consumption data.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# Manufacturing Resource Planning (MRP II) and Enterprise Logic

## 1. 개요 (Why: 인간적 통찰)
공장이 단순히 '자재'만 있다고 돌아갈까요? 아닙니다. 숙련된 작업자, 가동 가능한 기계, 그리고 이 모든 것을 살 수 있는 자금이 맞물려야 합니다. **Manufacturing Resource Planning (MRP II) and Enterprise Logic**은 공장을 하나의 거대한 **'동기화된 생명체'**로 만드는 두뇌입니다. 단순 자재 계산(MRP)을 넘어, "우리가 이 물건을 만들 수 있는 실질적인 능력이 있는가?"를 묻고 재무와 인사를 생산 계획에 통합합니다. 이는 공장의 **'경제적 무결성'**과 **'실행 가능성'**을 동시에 담보하는 산업 운영의 핵심 로직입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Logic)

### 2.1. 생산 능력 소요 계획 (Capacity Requirements Planning, CRP)
MRP가 '무엇을, 언제' 살지를 결정한다면, CRP는 '그것을 가공할 기계와 사람이 충분한가'를 계산합니다.

$$ Load_{center} = \sum (Setup\_Time + Run\_Time \times Qty) $$
$$ Utilization = \frac{Actual\_Hours\_Worked}{Available\_Capacity} $$

**[인간적 해석]**: "체력 측정"입니다. 아무리 좋은 재료가 있어도 요리사의 팔이 두 개뿐이라면 요리는 늦어집니다. 우리는 이 수식을 통해 "공장의 부하(Load)를 평탄화하여 병목 현상을 사전에 차단하는" **'운영 무결성'**을 달성합니다.

### 2.2. Closed-loop MRP 피드백 루프 (Feedback Logic)
계획(MPS)이 현장(Shop Floor)에서 어긋났을 때, 그 정보를 다시 상위 계획으로 전달하여 실시간으로 수정하는 순환 논리입니다.

$$ Plan_{Revised} = f(Plan_{Initial}, Gap_{Execution}) $$

**[인간적 해석]**: "반성하는 기계"입니다. MRP II는 계획이 틀렸음을 인정하고, 그 차이를 다음 계획에 즉각 반영합니다. 우리는 이 로직을 통해 "현장과 경영진이 동일한 숫자를 보고 판단하는" **'정보 무결성'**을 사수합니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Feature | MRP (Legacy) | MRP II (Gold V6.3.7) | Note |
| :--- | :--- | :--- | :--- |
| **Integration Scope** | Materials Only | **Materials + HR + Finance + M/C** | Holistic |
| **Feedback Loop** | Open-loop (One way) | **Closed-loop (Bi-directional)** | Dynamic |
| **Planning Horizon**| Short-term | **Strategic Long-term (S&OP)** | Foresight |
| **Costing Logic** | Estimated Cost | **Actual Cost vs Standard Cost** | Precision |
| **Simulation** | Basic | **What-if Scenario Modeling** | Intelligence |
| **ISA-95 Level** | Level 3 | **Level 3 ~ 4 (Bridging)** | Connectivity |

## 4. LogicFidelityEngine: Diagnostic Logic

MRP II 시스템의 운영 논리적 무결성을 진단하는 `LogicFidelityEngine` 로직입니다.

```python
class LogicFidelityEngine:
    def __init__(self, plan_adherence_rate, capacity_utilization, lead_time_error):
        self.adherence = plan_adherence_rate # high-fidelity execution accuracy
        self.utilization = capacity_utilization # high-fidelity resource load
        self.error = lead_time_error # high-fidelity timing gap

    def diagnose_planning_health(self):
        """계획 무결성 및 자원 최적화 진단"""
        if self.adherence < 0.85: # 계획 준수율 저하
            return "WARNING: High-fidelity Plan Misalignment - High-fidelity Gap between MPS and Execution. Check for high-fidelity master data inaccuracies"
        if self.utilization > 0.95: # 과부하 상태
            return "CRITICAL: High-fidelity Resource Bottleneck - Work center overload detected. Risk of high-fidelity lead time explosion"
        if self.error > 0.15: # 리드타임 오차
            return "NOTICE: High-fidelity Lead Time Drift - Actual production takes longer than planned. Update high-fidelity routing data"
        return "OPTIMAL: Verified high-fidelity MRP II Logic and Resource Balance"

# Instance Diagnostic
engine = LogicFidelityEngine(plan_adherence_rate=0.92, capacity_utilization=0.88, lead_time_error=0.05)
print(engine.diagnose_planning_health())
```

## 5. 분석 프레임워크: Integrated Business Planning (IBP)
1. **[What-if Analysis]**: 원자재 가격 폭등이나 핵심 설비 고장 시, 생산 계획과 손익에 미치는 영향을 시뮬레이션하여 최적의 대안(Plan B)을 도출하는 전략.
2. **[Standard Costing Alignment]**: 제조 원가와 실제 소비된 자원(기계 시간, 인건비)을 실시간 매칭하여 공장의 '돈 버는 속도'를 측정하는 재무적 전략.
3. **[S&OP Synchronization]**: 영업의 수요 예측(Demand)과 공장의 생산 능력(Supply)을 매달 회의를 통해 하나로 맞추는 전사적 동기화 전략.

## 6. 스스로 체크 (Self-Audit)
1. MRP II가 MRP와 결정적으로 다른 점은 무엇인가? (자료의 흐름에 재무와 생산 능력 피드백 루프가 포함되어 전사 자원을 관리한다는 점)
2. '무한 능력 계획(Infinite Scheduling)'과 '유한 능력 계획(Finite Scheduling)'의 차이는 무엇인가? (자원의 한계를 고려하지 않고 계획하느냐, 실제 기계 용량을 따져서 계획하느냐의 차이)
3. 왜 MRP II 시스템에서 데이터의 '정확도(Accuracy)'가 가장 중요한가? (부정확한 리드타임이나 BOM은 잘못된 자재 주문과 자원 낭비로 직결되기 때문)

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data manufacturing-lead-time-benchmark-v2026`와 연동되어, 다국적 제조 기업의 글로벌 공급망(SCM) 내에서 자원 낭비를 15% 이상 감축하고, 계획 준수율을 98% 이상으로 유지함으로써 자본 효율성이 극대화된 **'자율 운영 팩토리'**의 논리적 근간을 제공합니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- material-requirements-planning-mrp-and-inventory-logic
- manufacturing-execution-system-mes-and-shop-floor-logic
- enterprise-resource-planning-erp-and-business-intelligence-logic
- Data manufacturing-lead-time-benchmark-v2026
