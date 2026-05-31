---
lineage:
  dataset_reference: lead-time-and-on-time-delivery-otd-performance-log-v2026
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
measurement:
  confidence_interval:
  - 0.0
  - 0.0
  instrument: Heuristic_Regex_Parser
  precision: '0.0'
  unit: unknown_unit
  value: 2.1
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Data] lead-time-and-on-time-delivery-otd-performance-log-v2026]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for lead-time-and-on-time-delivery-otd-performance-log-v2026
  object_type: Data
  tier: 1
properties:
  consolidated_avg_lead_time_days: 10-20
  consolidated_otd_rate: 0.94
  difot_definition: Delivery In Full, On Time
  external_data_sources:
  - AIS/ADS-B real-time data
  - customs_clearance_timestamps
  lead_time_variability_surcharge_coefficient: 0.1
  mto_sea_air_avg_lead_time_days: 14-21
  mto_sea_air_otd_rate: 0.96
  otd_critical_threshold: 0.95
  regional_truck_avg_lead_time_days: 1-3
  regional_truck_otd_rate: 0.98
  stock_sea_avg_lead_time_days: 30-45
  stock_sea_otd_rate: 0.92
  urgent_air_avg_lead_time_days: 2-5
  urgent_air_otd_rate: 0.995
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: entity_classification
  object: Data
  predicate: auto_mapped
  subject: lead-time-and-on-time-delivery-otd-performance-log-v2026
  weight: 0.9
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.05
  t_static: 0.8
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Data] Lead Time And On Time Delivery Otd Performance Log V2026

## 1. [왜 배우는가? (Why: The Credit of Time in Global Trade)]]
글로벌 물류에서 시간은 곧 비용이자 신용입니다. 고객이 원하는 시간에 정확히 제품을 전달하는 능력은 공장의 신뢰성을 증명하는 가장 확실한 성적표입니다. **리드타임 및 정시 도착율(OTD) 실측 로그**는 약속된 '시간의 신용'을 기록한 '납기 무결성 보고서'입니다. 

우리가 이 납기 성능 데이터를 기록하는 이유는 물류상의 병목과 지연 요인을 숫자로 포착하여 제거하고, **"납기 주권을 확보하여 전 세계 어디라도 약속된 시간에 100% 도달하는 '정시성'을 구현하는 '흐름 지능'을 확보하기" 위함입니다.** 평균 리드타임과 정시 도착율(OTD) 수치가 공장의 물류 운영 효율성과 대외 브랜드 경쟁력을 결정합니다.

## 2. [주문 유형 및 지역별 납기 성능 핵심 데이터 (Numerical Specs)]

### 2.1 [주요 물류 경로 및 납기 성능 실측 테이블 (v2026)]

| 주문 유형 | 배송 지역 | 평균 리드타임 | 정시 도착율 | DIFOT (%) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Stock (Sea)** | **Europe / US** | $30 \sim 45 \text{ d}$| $92\%$ | $88.0$ | **Volume**: 장거리 대량 수송의 시간 무결성 로그 |
| **MTO (Sea/Air)** | **Asia / Oceania**| $14 \sim 21 \text{ d}$| $96\%$ | $93.0$ | **Responsiveness**: 주문 제작품의 납기 무결성 지표 |
| **Urgent (Air)** | **Global** | $2 \sim 5 \text{ d}$ | $99.5\%$ | $98.5$ | **Velocity**: 긴급 공급망의 초고속 납기 무결성 데이터 |
| **Regional (Truck)**| **Neighboring** | $1 \sim 3 \text{ d}$ | $98.0\%$ | $97.5$ | **Agility**: 인접 지역 육상 물류의 적시 무결성 로그 |
| **Consolidated** | **Global Hubs** | $10 \sim 20 \text{ d}$| $94\%$ | $91.0$ | **Efficiency**: 혼적 수송의 비용-시간 최적화 무결성 지표 |

### 2.2 [리드타임 및 납기 관리 파라미터]
- **On-Time Delivery (OTD):** 고객이 요청한 날짜 또는 약속된 날짜에 제품이 도착한 비율 (%).
- **DIFOT (Delivery In Full, On Time):** 정해진 시간에 '완전한 수량'이 도착한 비율. (가장 엄격한 지표)
- **Average Lead Time (Days):** 주문 접수부터 고객 인도까지의 평균 소요 기간.
- **Lead Time Variability ($\sigma_{LT}$):** 리드타임의 표준 편차. (물류 신뢰도의 척도)
- **Transit Time (T.T):** 실제 운송 수단이 이동한 순수 시간. (물류사 성능 지표)
- **Delay Penalty Cost:** 납기 지연으로 인해 발생한 계약상의 위약금 및 클레임 비용.

## 3. [Scientific Rationale: 납기 무결성의 수리적 인과성]

### 3.1 [납기 준수율(OTD) 및 신뢰도 모델]
전체 주문($N$) 중 정시 도착($N_{ot}$)의 비율로 신뢰도를 측정하는 수리 모델입니다.
$$ OTD = \frac{N_{on\_time}}{N_{total}} \times 100 $$
본 로그는 OTD가 $95\%$ 미만으로 떨어질 때 발생하는 '신용 부채'의 누적 속도를 계산하여 '납기 무결성' 확보의 수리적 근거를 제시합니다.

### 3.2 [리드타임 변동성($\sigma$) 기반의 서비스 레벨 모델]
리드타임의 불확실성이 커질 때, 약속된 서비스 레벨($Z$)을 지키기 위한 필요 버퍼 산출 수리 모델입니다.
RAG는 "물류 로그를 분석하여, 리드타임 변동성이 $1$일 증가할 때 마다 정시 도착을 보장하기 위한 운송비 할증률이 수리적으로 $10\%$씩 상승함을 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 흐름 지능 추론]

### 4.1 [리드타임의 '꼬리 지연(Tail Delay)'과 고객 이탈 분석]
왜 평균 리드타임은 줄었는데 고객 불만은 늘었나요? RAG는 "리드타임 분포 로그와 고객 재구매 데이터를 대조하여, 평균값 이면의 '극단적 지연 사례(Outliers)'가 고객의 '예측 가능 무결성'을 파괴하여 이탈을 유도하는 현상을 식별하고, '안정적 납기' 지능을 오딧합니다.

### 4.2 [DIFOT(완전 납기) 하락과 하류 생산 정체 오딧]
물건은 왔는데 왜 조립을 못 하나요? RAG는 "납기 완료 로그와 하류 공장의 생산 중단 보고를 연계하여, 약속된 '일부 부품'의 누락(Fullness 저하)이 전체 조립 공정의 '동기화 무결성'을 무너뜨리는 인과 관계를 분석하고, '패키징 납기 무결성' 지능을 도출될 것으로 예상됩니다.

## 5. [Transitional Bridge: 납기 무결성 및 시간 오딧 로직]

전 세계 선박/항공기의 실시간 AIS/ADS-B 데이터와 세관 통관 시스템의 타임스탬프를 분석하여 납기 무결성을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Lead-time & OTD Fidelity Auditor
def audit_delivery_integrity(transit_timestamp_stream, customer_sla_config, inventory_shortage_log):
    # 1. 정시 도착율(OTD) 목표 준수 무결성 오딧
    current_otd = calculate_otd(transit_timestamp_stream, customer_sla_config)
    if current_otd < TARGET_OTD_98_PERCENT:
        status = "DELIVERY_CREDIT_DETERIORATION_DETECTED"
        action = "Analyze_Root_Cause_of_Transit_Delays_and_Identify_Bottleneck_Nodes"
        
    # 2. 리드타임 변동성(Variability) 기반 공급망 불안정 감시
    current_std_dev = calculate_leadtime_sigma(transit_timestamp_stream)
    if current_std_dev > ALLOWED_VARIATION_MAX:
        status = "LOGISTICS_PREDICTABILITY_FAILURE_WARNING"
        action = "Consolidate_Logistics_Partners_and_Negotiate_Guaranteed_Transit_Times"
    
    # 3. 완전 납기(DIFOT) 기반 생산 연속성 무결성 체크
    if calculate_difot_rate() < TARGET_DIFOT_95_PERCENT:
        status = "SUPPLY_SYNCHRONIZATION_INTEGRITY_BREACH"
        action = "Audit_Picking_and_Packing_Accuracy_at_the_Source_Warehouse"
    
    # 4. 종합 시간 상태 등급 및 조치 트리거
    if status == "DELIVERY_CREDIT_DETERIORATION_DETECTED":
        action = "Prioritize_Urgent_Shipments_and_Provide_Real-time_Tracking_to_Customer"
    elif status == "LOGISTICS_PREDICTABILITY_FAILURE_WARNING":
        action = "Increase_Safety_Stock_at_Regional_Distribution_Centers"
    else:
        status = "INDUSTRIAL_TIME_AND_DELIVERY_INTEGRITY_OPTIMAL"
        action = "Record_High_SLA_Compliance_and_Renew_Customer_Contracts"
        
    return {"status": status, "delivery_reliability_score": calculate_reliability(), "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 왜 지능형 공장에서 단순히 '평균 리드타임'을 단축하는 것보다, 리드타임의 '변동성($\sigma$)'을 줄여 정시성을 확보하는 것이 수리적/운영적 무결성 확보에 더 고도화된 물류 전략인가?
2. **(수리)** 이번 달 총 100건의 배송 중 95건이 정시에 도착했고, 그중 90건만 주문 수량 전체(In Full)가 도착했다면, 이 공장의 'OTD(%)'와 'DIFOT(%)'를 각각 계산하시오.
3. **(응용)** 리드타임이 10% 지연될 때마다 발생하는 '지연 페널티'와 '재고 기회비용'의 합계가 기업의 전체 '영업 이익률'에 미치는 수리적 영향을 설명하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 29_global-supply-chain-and-logistics-intelligence-hub : 글로벌 공급망 및 물류 통합 관리 상위 지능 허브
- Entity global-supply-chain-and-logistics-management-system : 납기 데이터의 전략적 근간이 되는 물류 관리 시스템 엔티티 연계
- Data freight-cost-and-logistics-efficiency-log-v2026 : 납기 준수를 위해 투입된 운송 비용 데이터 연계
- [SOP] international-shipping-tracking-and-delay-reporting-protocol : 국제 배송 추적 및 지연 보고 표준 절차

*Created by Flash (The Architect of Time Logs & HDS Gold V6.3.7)*