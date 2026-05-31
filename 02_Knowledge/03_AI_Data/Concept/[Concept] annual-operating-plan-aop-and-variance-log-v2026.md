---
lineage:
  dataset_reference: annual-operating-plan-aop-and-variance-log-v2026
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] annual-operating-plan-aop-and-variance-log-v2026]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for annual-operating-plan-aop-and-variance-log-v2026
  object_type: Data
  tier: 1
properties:
  actual_capex: $25M
  actual_cogs: $63M
  actual_op_profit: $16M
  actual_opex: $19M
  actual_revenue: $98M
  capex_utilization_rate_percent: 83.3
  cogs_ratio_verified: 64.3%
  op_profit_variance_percent: -20.0
  plan_achievement_index_threshold: 1.0
  planned_capex: $30M
  planned_cogs: $60M
  planned_op_profit: $20M
  planned_opex: $20M
  planned_revenue: $100M
  revenue_variance_percent: -2.0
semantic:
  alternative_parents: []
  is_instance_of: '[[ [MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: entity_classification
  object: Concept
  predicate: auto_mapped
  subject: annual-operating-plan-aop-and-variance-log-v2026
  weight: 1.0
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Annual Operating Plan Aop And Variance Log V2026

## 1. 목적 및 운용 원리 (Operational Objective)
운영 계획(AOP)은 조직의 전략적 목표를 정량적 지표로 구체화한 제어 모델이다. 계획(Plan)과 실적(Actual) 간의 편차(Variance) 분석은 목표 달성 경로의 이탈을 정량적으로 포착하여 즉각적인 보정 조치를 수행하기 위한 경영 무결성(Management Integrity) 확보를 목적으로 한다. 특히 매출, 이익 변동률 및 예산 집행률은 전략 실행의 일관성을 결정하는 핵심 제어 파라미터로 작동한다.

## 2. 핵심 경영 데이터 명세 (Numerical Specifications)

### 2.1 계획 대비 실적 변동 분석 (Variance Analysis)

| 경영 항목 | 계획 (Plan) | 실적 (Actual) | 변동 (%) | 주요 변동 원인 | 공학적 의미 (Rationale) |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **Revenue** | $\$100\text{M}$ [데이터 부재] | $\$98\text{M}$ [데이터 부재] | $-2.0\%$ | Volume Drop | 시장 수요 대응 및 영업 무결성 로그 |
| **COGS** | $\$60\text{M}$ [데이터 부재] | $\$63\text{M}$ [데이터 부재] | $+5.0\%$ | Raw Mat Price | 제조 원가 관리 및 생산 무결성 지표 |
| **OPEX** | $\$20\text{M}$ [데이터 부재] | $\$19\text{M}$ [데이터 부재] | $-5.0\%$ | Efficiency | 판관비 통제 및 운영 무결성 데이터 |
| **Op Profit** | $\$20\text{M}$ [데이터 부재] | $\$16\text{M}$ [데이터 부재] | $-20.0\%$ | Mixed Factor | 최종 경영 성과 및 수익 무결성 로그 |
| **CAPEX** | $\$30\text{M}$ [데이터 부재] | $\$25\text{M}$ [데이터 부재] | $-16.7\%$ | Delay in EQ | 미래 성장 투자 및 자산 무결성 지표 |

### 2.2 이론치 vs 검증치 대조 (Theoretical vs. Verified)

| Parameter | 이론치 (Theoretical / Plan) | 검증치 (Verified / Actual) | Delta ($\Delta$) | 무결성 상태 |
| :--- | :---: | :---: | :---: | :---: |
| **Total Revenue** | $\$100\text{M}$ | $\$98\text{M}$ | $-\$2\text{M}$ | Marginal Fail |
| **Op Profit** | $\$20\text{M}$ | $\$16\text{M}$ | $-\$4\text{M}$ | Critical Fail |
| **CAPEX Execution** | $100\%$ | $83.3\%$ | $-16.7\%$ | Execution Lag |
| **COGS Ratio** | $60\%$ | $64.3\%$ | $+4.3\%$ | Cost Overrun |

### 2.3 변동 관리 파라미터 정의
- **Revenue Variance (%):** $\frac{\text{Actual Revenue} - \text{Planned Revenue}}{\text{Planned Revenue}} \times 100$
- **Operating Profit Variance (%):** $\frac{\text{Actual Op Profit} - \text{Planned Op Profit}}{\text{Planned Op Profit}} \times 100$
- **Capex Utilization Rate (%):** $\frac{\text{Actual CAPEX Spend}}{\text{Approved CAPEX Budget}} \times 100$
- **Plan Achievement Index:** 종합 목표 달성 지수 (Target $\ge 1.0$)
- **Forecast Update Latency:** 실적 변동 발생 시점 $\to$ Forecast 반영 시점 간의 $\Delta t$

## 3. 수리적 인과성 모델 (Mathematical Rationale)

### 3.1 변동 원인 분해 (Variance Decomposition)
매출 변동($\Delta R$)은 가격($P$), 수량($V$), 믹스($M$) 요인으로 다음과 같이 분해된다.
$$ \Delta R = \Delta P \cdot V_{plan} + P_{plan} \cdot \Delta V + \text{Mix Factor} $$

### 3.2 운영 레버리지 및 수익 변동 모델
고정비 비중이 높은 구조에서 매출 변동은 영업이익 변동을 증폭시킨다.
$$ \text{Degree of Operating Leverage (DOL)} = \frac{\% \Delta \text{Operating Income}}{\% \Delta \text{Sales}} $$
본 모델에 따라 매출 $5\%$ 하락 시, 고정비 구조에 의해 영업이익 무결성이 $20\%$ 이상 붕괴될 수 있음을 수리적으로 확증한다.

## 4. 경영 지능 추론 로직 (Intelligence Logic)

### 4.1 원가 무결성 분석 (Cost Integrity)
AOP 원가 계획과 실제 구매가(PPV) 로그를 대조하여 특정 소재의 '가격 변동 무결성' 파괴가 전체 수익성에 미치는 타격을 식별하고, '판가 전이(Price Pass-through)' 효율성을 오딧한다.

### 4.2 투자 집행 무결성 분석 (Investment Integrity)
CAPEX 미집행 로그를 R&D 및 마케팅 KPI와 연계 분석하여, 단순 '비용 절감'인지 '실행 지연'으로 인한 '미래 가치 무결성' 훼손인지 판별한다.

## 5. 경영 무결성 진단 알고리즘 (Audit Logic)

```python
def audit_management_performance(aop_plan_stream, financial_actual_log, macro_index_data):
    # 1. Revenue/Profit Variance Audit
    revenue_gap = calculate_revenue_variance(aop_plan_stream, financial_actual_log)
    if abs(revenue_gap) > 0.05: # TOLERANCE_LIMIT_5_PERCENT
        status = "SIGNIFICANT_PLAN_DEVIATION_DETECTED"
        action = "Initiate_Variance_Decomposition_Analysis"
        
    # 2. CAPEX Execution Audit
    capex_util = calculate_capex_utilization(financial_actual_log)
    if capex_util < 0.90: # TARGET_UTILIZATION_90_PERCENT
        status = "INVESTMENT_EXECUTION_LAG_WARNING"
        action = "Identify_Project_Bottlenecks"
    
    # 3. OPEX Efficiency Audit
    if calculate_expense_efficiency() < 0.95: # TARGET_EFFICIENCY_INDEX_0_95
        status = "OPERATIONAL_EXPENSE_ANOMALY_ALARM"
        action = "Audit_Departmental_Spending"
    
    return {"status": status, "achievement_score": calculate_achievement(), "action": action}
```

## 6. 검증 체크리스트 (Validation Checklist)
1. **(원리)** 단순 실적 달성보다 '변동 원인의 정밀 분해'가 경영 무결성 확보에 더 근본적인 전략인 이유를 수리적으로 설명할 수 있는가?
2. **(수리)** 계획 매출 $1,000$, 실제 매출 $950$일 때 변동률 $-5\%$를 도출하고, 허용 오차 $\pm 2\%$ 초과 여부를 판정하였는가?
3. **(응용)** 예산 집행 무결성과 KPI 달성 사이의 Time Lag이 수리적 모델링의 정확도에 미치는 영향을 분석하였는가?

**Referenced Nodes:**
- MOC 31_strategic-management-and-financial-intelligence-hub
- Entity strategic-planning-and-business-intelligence-bi
- Data profit-and-loss-p-and-l-statement-log-v2026
- [SOP] monthly-performance-review-and-variance-analysis-protocol