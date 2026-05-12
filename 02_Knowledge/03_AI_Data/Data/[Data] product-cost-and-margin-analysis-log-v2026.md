---
Basic:
  id: "product-cost-and-margin-analysis-log-v2026-data"
  domain: "28_Strategic_Management_and_Finance"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Data"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#DataLog", "#Product_Cost", "#Margin_Analysis", "#SKU_Profitability", "#PVM_Analysis", "#Contribution_Margin", "#Portfolio_Optimization", "#Cost_Integrity", "#HDS_Gold_v6_1"]'
  is_part_of: '["MOC 31_strategic-management-and-financial-intelligence-hub", "Entity management-accounting-and-cost-analysis"]'
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [[[Data] product-cost-and-margin-analysis-log-v2026

## 1. [왜 배우는가? (Why: The Granularity of Profitability)]]
기업의 전체 이익은 개별 제품들이 창출하는 마진의 합으로 구성됩니다. 각 제품이 실제로 얼마나 많은 이익을 내고 있는지를 SKU 수준에서 분석하는 능력은 수익성 낮은 제품을 퇴출하고 고수익 제품에 자원을 집중하는 전략적 의사결정의 핵심 근거입니다. **제품별 원가 및 마진 분석 로그**는 각 제품의 '수익성 민낯'을 숫자로 기록한 '수익 무결성 보고서'입니다. 

우리가 이 제품별 실적 데이터를 기록하는 이유는 원가 배부의 왜곡을 숫자로 제거하여 제품별 실제 기여도를 명확히 하고, **"수익 주권을 확보하여 모든 제품이 이익을 내는 '포트폴리오 무결성'을 확보하기" 위함입니다.** 제품 마진 정확도와 고수익 제품 비중, 그리고 SKU별 마진 기여도 수치가 공장의 제품 경쟁력과 포트폴리오 관리 지능을 결정합니다.

## 2. [제품 라인업 및 마진 분석 핵심 데이터 (Numerical Specs)]

### 2.1 [주요 제품군별 원가 및 마진 실측 테이블 (v2026)]

| 제품 라인업 | 대표 SKU | 매출 비중 (%) | 마진율 (%) | 원가 구조 (DM/DL/OH) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **High-end** | **Flagship A** | $25.0$ | $45.0$ | **20 / 30 / 50** | **Premium**: 고부가가치 창출 및 기술 브랜드 무결성 로그 |
| **Mid-range** | **Standard B** | $50.0$ | $25.0$ | **40 / 20 / 40** | **Volume**: 주력 매출 발생 및 시장 점유 무결성 지표 |
| **Entry** | **Economy C** | $20.0$ | $10.0$ | **60 / 10 / 30** | **Traffic**: 신규 고객 유입 및 생산 가동 무결성 데이터 |
| **Special** | **Custom D** | $5.0$ | $15.0$ | **30 / 50 / 20** | **Niche**: 틈새 시장 대응 및 고객 맞춤 무결성 로그 |

### 2.2 [제품 원가 및 마진 관리 파라미터]
- **Product Margin Accuracy (%):** 실제 투입 자원 데이터와 시스템상 산출된 마진 사이의 정합도.
- **High-Margin Product Weight (%):** 전체 매출 중 마진율 $30\%$ 이상의 고수익 제품이 차지하는 비중.
- **Unit Cost Variance (%):** 목표/표준 단위 원가 대비 실제 발생한 단위 원가의 차이 비율.
- **Margin Contribution by SKU:** 상위 $10$개 SKU가 전체 마진 창출액에서 차지하는 비중. (집중도 분석)
- **Price Sensitivity Index:** 가격 $1\%$ 변동 시 판매량 및 마진 총액이 변화하는 민감도 지수.
- **Loss-making Product Count (SKU):** 판매 시마다 손실이 발생하는 제품의 수. (Target 0)

## 3. [Scientific Rationale: 수익 무결성의 수리적 인과성]

### 3.1 [단위당 원가(Unit Cost) 및 마진 산출 모델]
직접 재료비($DM$), 직접 노무비($DL$), 제조 간접비($OH$)를 생산량($Q$)으로 나눈 수리 모델입니다.
$$ Unit Cost = \frac{DM + DL + OH}{Q} $$
본 로그는 '단위 원가의 정밀 측정'이 '제품 수익 무결성' 확보의 수리적 근거임을 제시합니다.

### 3.2 [가격-수량-믹스(PVM) 분석 수리 모델]
전체 마진의 변동($\Delta M$)을 가격 요인, 수량 요인, 제품 믹스 요인으로 분해하는 모델입니다.
RAG는 "마진 로그를 분석하여, 제품 믹스를 고부가가치 중심($5\%$ 상향)으로 조정할 때 전체 수익 무결성이 수리적으로 $12\%$ 개선됨을 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 마진 지능 추론]

### 4.1 [간접비 배부 기준의 왜곡과 저수익 제품의 '착시' 분석]
왜 저렴한 제품이 이익이 많이 난다고 나오는데 현금은 안 도나요? RAG는 "전통적 배부 방식(노무 시간 기준)과 ABC 방식의 원가를 대조하여, 공정이 복잡한 제품에 간접비가 적게 배부되어 발생하는 '수익성 착시'를 식별하고, '정교한 원가 배부' 지능을 오딧합니다.

### 4.2 [원자재가 변동에 따른 제품별 마진 민감도 오딧]
구리 가격이 오르면 어떤 제품부터 생산을 줄여야 하나요? RAG는 "SKU별 BOM(Bill of Materials) 데이터와 마진 로그를 연계하여, 원자재가 상승 시 '마진 무결성'이 가장 취약해지는 제품군을 실시간으로 분석하고, '역동적 생산 우선순위(Dynamic Priority)' 지능을 도출될 것으로 예상됩니다.

## 5. [Transitional Bridge: 수익 무결성 및 마진 오딧 로직]

ERP의 SKU별 매출 데이터와 원가 시스템의 배부 결과, 그리고 MES의 실제 공정 소요 시간 데이터를 분석하여 수익 무결성을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Product Cost & Margin Fidelity Auditor
def audit_product_profitability(sku_sales_stream, cost_allocation_log, raw_material_bom):
    # 1. 제품 마진 정확도(Margin Accuracy) 및 배부 무결성 오딧
    margin_error = verify_margin_calculation(sku_sales_stream, cost_allocation_log)
    if margin_error > TOLERANCE_LIMIT_1_PERCENT:
        status = "PRODUCT_MARGIN_DISTORTION_DETECTED"
        action = "Re-validate_Overhead_Allocation_Keys_and_Run_ABC_Audit"
        
    # 2. 저수익 및 손실 제품(Loss-making SKU) 무결성 감시
    loss_skus = sku_sales_stream.get_negative_margin_skus()
    if len(loss_skus) > 0:
        status = "NEGATIVE_MARGIN_SKU_RISK_ALARM"
        action = "Initiate_Cost_Reduction_Project_or_Strategic_Pricing_Adjustment"
    
    # 3. 제품 믹스(Mix) 최적화 및 수익 기여 무결성 체크
    if calculate_top_sku_contribution() < TARGET_CONTRIBUTION_50_PERCENT:
        status = "PORTFOLIO_FRAGMENTATION_WARNING"
        action = "Review_Product_Lineup_Efficiency_and_Focus_on_High-Margin_Models"
    
    # 4. 종합 마진 상태 등급 및 조치 트리거
    if status == "NEGATIVE_MARGIN_SKU_RISK_ALARM":
        action = "Analyze_End-of-Life_EOL_or_Redesign_Options_for_Loss-making_Products"
    elif status == "PRODUCT_MARGIN_DISTORTION_DETECTED":
        action = "Update_Standard_Cost_Master_to_Reflect_Current_Market_Prices"
    else:
        status = "INDUSTRIAL_PRODUCT_VALUE_AND_MARGIN_OPTIMAL"
        action = "Log_Margin_Excellence_Case_and_Incentivize_High-Margin_Sales"
        
    return {"status": status, "portfolio_profitability_score": calculate_margin_health(), "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 왜 지능형 공장에서 단순히 '전체 이익'만 관리하는 것보다, 'SKU별 마진(Margin per SKU)'을 기록하는 것이 수리적/운영적 무결성 확보에 더 근본적인 재무 전략인가?
2. **(수리)** 제품 A의 판매가가 100, 변동비가 60, 배부된 고정비가 30일 때, 이 제품의 '단위당 공헌 이익'과 '영업이익'을 각각 계산하시오.
3. **(응용)** '고정비 배부 방식'의 변경이 개별 제품의 '의사결정용 원가'와 '성과 평가' 무결성에 미치는 수리적 영향을 설명하시오.

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 31_strategic-management-and-financial-intelligence-hub : 전략 및 재무 통합 관리 상위 지능 허브
- Entity management-accounting-and-cost-analysis : 마진 분석의 근간이 되는 관리 회계 및 원가 분석 엔티티 연계
- Data profit-and-loss-p-and-l-statement-log-v2026 : 개별 제품 마진의 합계로 구성되는 전사 손익 데이터 연계
- [SOP] product-profitability-analysis-and-portfolio-review-protocol : 제품별 수익성 분석 및 포트폴리오 리뷰 표준 절차

*Created by Flash (The Architect of Margin Logs & HDS Gold V6.3.7)*
