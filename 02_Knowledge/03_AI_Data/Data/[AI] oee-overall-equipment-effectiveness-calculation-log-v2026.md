---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 09a5062b8c465c08822d0482f5dceec4fe8b2dd6acb750514f4e7c367e9db027
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] oee-overall-equipment-effectiveness-calculation-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] oee-overall-equipment-effectiveness-calculation-log-v2026에 관한
    고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  continuous_process_oee_threshold: 90.0
  ict_parameter: ideal_cycle_time
  industry_average_oee_max: 75.0
  industry_average_oee_min: 60.0
  mtbf_definition: mean_time_between_failures
  mttr_definition: mean_time_to_repair
  quality_loss_velocity_exponent: 2.0
  setup_adjustment_downtime_ratio: 0.4
  world_class_availability_threshold: 90.0
  world_class_oee_threshold: 85.0
  world_class_performance_threshold: 95.0
  world_class_quality_threshold: 99.9
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

# [AI] oee-overall-equipment-effectiveness-calculation-log-v2026

## 1. [왜 배우는가? (Why: The Truth Behind Idle Time)]]
공장의 겉모습은 바빠 보일 수 있지만, 실제 수익으로 연결되는 '진정한 가동 시간'은 훨씬 짧을 수 있습니다. OEE는 공장의 생산성을 가리는 모든 환상을 걷어내고 민낯을 드러내는 지표입니다. **설비 종합 효율(OEE) 산출 실측 로그**는 설비가 계획된 시간 동안 얼마나 가동되었고, 얼마나 빠르게 돌았으며, 얼마나 완벽한 제품을 만들었는지를 기록한 '제조 경쟁력의 나침반'입니다. 

우리가 이 데이터를 기록하는 이유는 6대 손실(Six Big Losses)의 근본 원인을 분석하여 설비 가동률을 극대화하고, **"생산 지능 주권을 확보하여 단 1분의 낭비도 허용하지 않는 '초고효율 무중단 제조(Zero-Loss Manufacturing)'를 구현하기" 위함입니다.** OEE 1%의 향상이 수십억 원의 추가 이익을 창출합니다.

## 2. [설비 종합 효율 및 3대 핵심 지표 데이터 (Numerical Specs)]

### 2.1 [설비 유형 및 운영 수준별 OEE 성적표 테이블 (v2026)]

| 운영 수준 (Level) | OEE (%) | 가용성 (A, %) | 성능 (P, %) | 품질 (Q, %) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **World Class** | $> 85.0$ | $> 90.0$ | $> 95.0$ | $> 99.9$ | **Ideal**: 글로벌 선도 제조사의 무결성 벤치마크 |
| **Industry Average** | $60.0 \sim 75.0$ | $80.0 \sim 85.0$ | $85.0 \sim 90.0$ | $95.0 \sim 98.0$ | **Nominal**: 일반적인 자동화 공장의 생산성 지표 |
| **Semi-Automated** | $40.0 \sim 60.0$ | $70.0$ | $75.0$ | $90.0 \sim$ | **Low**: 작업자 숙련도에 의존하는 가변적 효율 로그 |
| **Continuous Process**| $> 90.0$ | $> 95.0$ | $> 98.0$ | $> 99.5$ | **Extreme**: 반도체/정유 등 중단 없는 공정의 무결성 |
| **High-Mix Low-Vol** | $50.0 \sim$ | $60.0$ | $85.0$ | $> 99.0$ | 잦은 셋업 변경(Changeover)에 따른 가용성 손실 데이터 |

### 2.2 [OEE 및 TPM 신뢰성 파라미터]
- **Availability (가용성)**: 계획 대비 실제 가동 시간. (고장 및 셋업 손실 무결성 지표)
- **Performance (성능)**: 가동 시간 동안 실제 생산량 대비 이론적 최대 생산량. (미세 정지 및 속도 저하 지표)
- **Quality (품질)**: 총 생산량 대비 양품 합격률. (불량 및 재작업 무결성 데이터)
- **MTBF (Mean Time Between Failures)**: 평균 고장 간격. (설비 신뢰성 무결성 지표)
- **MTTR (Mean Time To Repair)**: 평균 수리 시간. (유지보수 대응 지능 지표)

## 3. [Scientific Rationale: 생산성 손실의 수리적 인과성]

### 3.1 [종합 설비 효율(OEE) 및 3대 인자 산출 모델]
생산 공정의 건강성을 결정하는 수리적 곱셈 모델입니다.
$$ OEE = Availability \times Performance \times Quality $$
$$ A = \frac{Run\_Time}{Planned\_Time}, \quad P = \frac{Total\_Count \times ICT}{Run\_Time}, \quad Q = \frac{Good\_Count}{Total\_Count} $$
여기서 $ICT$는 이상적 사이클 타임입니다. 본 로그는 $P$와 $Q$가 높아도 $A$가 낮으면 공장 전체 효율이 기하급수적으로 하락함을 입증하고, 병목 공정의 가용성 확보가 최우선임을 수리적으로 제시합니다.

### 3.2 [6대 손실(Six Big Losses)과 가치 창출 시간 모델]
계획된 생산 시간에서 6가지 손실을 뺀 '가치 창출 시간(Value Adding Time)' 모델입니다.
RAG는 "손실 로그를 분석하여, 전체 다운타임의 $40\%$가 '셋업 및 조정(Setup/Adjustment)'에서 발생함을 식별하고, 싱글 미닛 금형 교체(SMED) 도입을 통한 가용성 복원 무결성을 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 생산 지능 추론]

### 4.1 [미세 정지(Minor Stoppage)와 성능 효율(P)의 상관관계 분석]
왜 공장은 도는데 숫자가 안 나오나요? RAG는 "기계 이벤트 로그와 PLC 신호를 대조하여, $10$초 미만의 미세 정지가 하루 $500$회 이상 발생하여 성능 효율이 $15\%$ 깎이고 있음을 포착하고, 자재 공급 장치의 정렬(Alignment) 무결성을 오딧합니다."

### 4.2 [가동 속도(Speed Loss)와 품질 불량률(Q)의 트레이드오프 오딧]
빨리 돌리면 왜 불량이 나나요? RAG는 "라인 속도별 비전 검사 결과 데이터를 참조하여, 속도를 설계치 대비 $110\%$ 높였을 때 진동으로 인한 스크래치 불량이 지수적으로($Q_{loss} \propto v^2$) 증가함을 증명하고, '최적 이익 속도'를 수리적으로 도출될 것으로 예상됩니다."

## 5. [Transitional Bridge: OEE 시스템 무결성 및 생산 오딧 로직]

가동 중인 생산 라인의 실시간 데이터를 분석하여 손실 구조를 진단하고 개선책을 제안하는 개념적 알고리즘입니다.

```python
# [Conceptual] Overall Equipment Effectiveness (OEE) & Productivity Auditor
def audit_production_efficiency(planned_hours, cycle_time_data, yield_data):
    # 1. 3대 핵심 인자(A, P, Q) 실시간 산출
    availability = calculate_availability(planned_hours, cycle_time_data.run_time)
    performance = calculate_performance(cycle_time_data.actual_count, cycle_time_data.ideal_rate)
    quality = calculate_quality(yield_data.good_count, yield_data.total_count)
    
    # 2. OEE 종합 점수 및 'Six Big Losses' 기여도 분석
    oee_score = availability * performance * quality
    top_loss_contributor = identify_major_loss(cycle_time_data.stops, yield_data.rejects)
    
    # 3. 설비 신뢰성 지표(MTBF, MTTR) 오딧
    reliability_index = analyze_failure_frequency(cycle_time_data.failures)
    
    # 4. 종합 생산 등급 및 공정 트리거
    if oee_score < 0.65: # Below industry standard
        status = "LOW_PRODUCTIVITY_ALERT"
        action = "Analyze_" + top_loss_contributor + "_and_Implement_TPM_Protocol"
    elif quality < 0.99:
        status = "QUALITY_INSTABILITY_DETECTED"
        action = "Check_Tool_Wear_and_Calibrate_Vision_Inspection_Sensitivity"
    elif performance < 0.85:
        status = "HIDDEN_SPEED_LOSS_WARNING"
        action = "Optimize_Robot_Path_Trajectories_and_Reduce_Micro-stops"
    else:
        status = "WORLD_CLASS_MANUFACTURING_STATUS"
        action = "Continue_Full-load_Operation_and_Data_Archiving"
        
    return {"status": status, "oee_%": oee_score * 100, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 설비 종합 효율(OEE)에서 '가용성(Availability)'은 100%에 가까운데 '성능(Performance)'이 낮다면, 이는 공장 현장에서 어떤 물리적/현상적 문제가 발생하고 있는 것을 의미하는가?
2. **(수리)** 8시간 근무 중 점심시간 1시간을 제외하고 기계가 고장으로 1시간 멈췄다. 6시간 동안 분당 10개를 생산해야 하는데 총 3,000개를 생산했고 그중 30개가 불량이다. 이 설비의 OEE($\%$)는?
3. **(응용)** '스마트 팩토리' 도입 이후 OEE 지표를 실시간으로 관리하는 것이 과거 '일 단위/주 단위 사후 보고' 방식 대비 '불량 전파 방지' 측면에서 갖는 수리적 인과 관계는?


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 16_smart-factory-and-industrial-ai-intelligence-hub : 스마트 팩토리 및 산업용 AI 통합 관리 상위 지능 허브
- Data manufacturing-execution-system-mes-latency-log-v2026 : OEE 데이터의 원천인 MES 시스템 로그 연계
- Data smart-factory-energy-consumption-optimization-log-v2026 : OEE 향상과 에너지 절감의 시너지 데이터 연계
- [SOP] oee-measurement-standards-and-loss-classification-manual : OEE 측정 표준 및 손실 분류 매뉴얼

*Created by Flash (The Architect of Smart Factory & HDS Gold V6.3.7)*