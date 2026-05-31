---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 33b0066ef255b7671afcde777e20db7615d31c6d1fb0a55c8312bc1537f31d87
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] maintenance-work-order-history-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] maintenance-work-order-history-v2026에 관한 고밀도 지능 노드'
  object_type: Data
  tier: 1
properties:
  avg_labor_hours_per_wo: 3.5
  emergency_rate_standard_pct: 12.0
  emergency_rate_target_pct: 5.0
  external_db_wms: warehouse_management_system
  maintenance_efficiency_ratio_formula: delta_mtbf / sum_maintenance_cost
  mttr_standard_hr: 1.8
  mttr_target_hr: 1.5
  pm_compliance_standard_pct: 96.5
  pm_compliance_target_pct: 98.0
  process_temp_increase_celsius: 10.0
  spare_parts_availability_standard_pct: 98.2
  spare_parts_availability_target_pct: 99.0
  spares_consumption_prediction_distribution: poisson
  text_mining_keyword_threshold_pct: 80.0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
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

# [AI] maintenance-work-order-history-v2026

## 1. [Why]] 정비 작업 오더(Work Order) 이력의 관리 공학적 의의
**정비 작업 오더(Work Order)** 이력은 설비의 유지보수 활동을 정량적으로 기록한 '병원 차트'와 같다. 어떤 설비에 어떤 부품이 교체되었는지, 수리에 얼마나 많은 시간(Labor Hours)과 비용이 발생했는지를 분석함으로써, 설비의 고유한 결함을 파악하고 최적의 **예방 정비(PM)** 주기를 설정할 수 있다. 이는 설비 가용성을 높이고 유지보수 비용(OpEx)을 최적화하는 핵심 데이터다.


## 2. [Numerical Specs] 정비 운영 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 목표 (Target) | 비고 |
| :--- | :--- | :--- | :--- |
| **PM Compliance** | $96.5\%$ | $> 98\%$ | 예방 정비 계획 준수율 |
| **Emergency Rate** | $12\%$ | $< 5\%$ | 전체 정비 중 긴급 수리 비중 |
| **Avg. Labor Hours** | $3.5\,\text{hr/WO}$ | N/A | 작업 오더 당 평균 소요 인시 |
| **Spare Parts Availability** | $98.2\%$ | $> 99\%$ | 정비 시 부품 가용율 |
| **MTTR (Mean Time To Repair)** | $1.8\,\text{hr}$ | $< 1.5\,\text{hr}$ | 고장 후 복구까지 평균 시간 |


## 3. [Scientific Rationale] 정비 효율 및 신뢰성 분석 모델

### 3.1 Maintenance Efficiency Ratio
투입된 정비 시간 대비 설비 가동 시간의 증가분을 통해 정비의 효율성을 평가한다.
$$Efficiency = \frac{\Delta MTBF}{\sum \text{Maintenance Cost}}$$

### 3.2 Spares Consumption Prediction
과거 정비 이력을 바탕으로 특정 부품의 향후 수요를 Poisson 분포를 통해 예측한다.


## 4. [Real-world Case] 반복 고장 분석을 통한 부품 재질 개선 사례

### 4.1 특정 밸브의 고무 패킹 마모 주기 단축 현상 포착
- **현상**: 화학 용액 배관의 제어 밸브 작업 오더가 평소 6개월 주기에서 최근 2개월 주기로 빈번하게 발생(긴급 정비 비중 증가).
- **분석**: **Python FidelityEngine** 기반의 작업 오더 텍스트 마이닝 결과, "패킹 마모로 인한 누설" 키워드가 $80\%$ 이상 차지함을 확인. 인근 신규 공정 도입으로 인한 용액 온도 $10^\circ\text{C}$ 상승이 원인으로 판별됨.
- **조치**: 패킹 재질을 일반 고무에서 내열/내화학성이 우수한 바이톤(Viton) 재질로 변경하고 PM 주기 재설정.
- **결과**: 해당 부품 수명 1년 이상으로 연장 및 돌발 정지 감소.


## 5. [FidelityEngine] MTTR 및 정비 준수율 계산 코드
```python
import datetime

def calculate_maintenance_stats(work_orders):
    """
    Calculate MTTR and PM Compliance
    :param work_orders: List of dicts {type: 'PM/CM', planned: bool, start: datetime, end: datetime}
    :return: dict of results
    """
    repair_times = []
    pm_count = 0
    pm_done = 0
    
    for wo in work_orders:
        if wo['type'] == 'CM': # Corrective Maintenance
            duration = (wo['end'] - wo['start']).total_seconds() / 3600
            repair_times.append(duration)
        elif wo['type'] == 'PM': # Preventive Maintenance
            pm_count += 1
            if wo['done_on_time']: pm_done += 1
            
    mttr = np.mean(repair_times) if repair_times else 0
    compliance = (pm_done / pm_count) * 100 if pm_count > 0 else 0
    
    return {"MTTR": mttr, "Compliance": compliance}

# 실측 데이터 대입 시뮬레이션 생략 (개념 위주)
```


## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Data Granularity**: 작업 오더에 사용된 모든 예비 부품의 파트 번호와 수량이 WMS와 실시간 연동되어 기록되는가?
- [ ] **Root Cause Tagging**: 모든 긴급 정비 오더(CM)에 대해 표준 고장 코드(Failure Code)가 정확히 입력되었는가?
- [ ] **Skill Management**: 작업 오더 담당자의 숙련도에 따른 수리 시간 편차가 분석에 반영되는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**