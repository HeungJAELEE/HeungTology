---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 992135e4151b2980559634b62344030a0b0eb23cf4903d5658e812447d56b20d
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-16'
  domain: 00_System
  id: '[[[00_System] [SOP] pmp-evm-and-math-formula-master]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: '[SOP] pmp-evm-and-math-formula-master에 관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  cpi_threshold_min: 1.0
  cpi_verified_max: 1.05
  cpi_verified_min: 0.92
  cv_threshold_min: 0
  eac_verified_multiplier: 1.12
  spi_threshold_min: 1.0
  spi_verified_max: 1.1
  spi_verified_min: 0.85
  sv_threshold_min: 0
  tcpi_threshold_max: 1.1
  tcpi_verified_max: 1.15
  tcpi_verified_min: 1.05
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 00_System]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: methodology_specification
  object: Concept
  predicate: contains_knowledge_of
  subject: '[SOP] pmp-evm-and-math-formula-master'
  weight: 0.95
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [SOP] pmp-evm-and-math-formula-master

## 1. 목적 및 정의 (Objective & Definition)
EVM(Earned Value Management): 주관적 진척도 보고를 배제하고, 투입 비용(AC) 대비 산출 가치(EV)의 정량적 상관관계를 분석하여 프로젝트 상태 진단, 최종 예상 비용(EAC) 및 잔여 작업 기간(ETC)을 산출하는 공학적 통제 체계 [데이터 부재].

## 2. 기술 사양 및 임계치 (Numerical Specs & Thresholds)

| 지표 (Metric) | 공식 (Formula) | 관리 임계치 (Spec) [데이터 부재] | 공학적 정의 |
| :--- | :--- | :--- | :--- |
| **CPI** | $EV / AC$ | $\ge 1.0$ [데이터 부재] | 비용 효율성 지수 (Cost Efficiency Index) |
| **SPI** | $EV / PV$ | $\ge 1.0$ [데이터 부재] | 일정 효율성 지수 (Schedule Efficiency Index) |
| **CV** | $EV - AC$ | $\ge 0$ [데이터 부재] | 예산 편차 (Cost Variance, Currency) |
| **SV** | $EV - PV$ | $\ge 0$ [데이터 부재] | 일정 편차 (Schedule Variance, Value) |
| **EAC** | $\text{Variable}$ | $\le BAC$ [데이터 부재] | 최종 예상 총 비용 (Estimate At Completion) |
| **TCPI** | $(BAC-EV)/(BAC-AC)$ | $\le 1.1$ [데이터 부재] | 목표 달성 필요 효율 (To-Complete Performance Index) |

### [Table] 이론치(Theoretical) vs. 검증치(Verified) 대조 분석
| 구분 | 이론적 목표치 (Theoretical) | 산업 현장 검증치 (Verified) [데이터 부재] | 편차 주요 요인 (Variance Factor) |
| :--- | :--- | :--- | :--- |
| **CPI** | $1.00$ [데이터 부재] | $0.92 \sim 1.05$ [데이터 부재] | 원자재 단가 변동 및 예비비(Contingency) 집행 |
| **SPI** | $1.00$ [데이터 부재] | $0.85 \sim 1.10$ [데이터 부재] | 장비 리드타임(Lead-time) 및 Wafer Fab 반입 지연 |
| **TCPI** | $1.00$ [데이터 부재] | $1.05 \sim 1.15$ [데이터 부재] | 프로젝트 후반부 리소스 밀집 투입 (Resource Crashing) |
| **EAC** | $BAC$ [데이터 부재] | $BAC \times 1.12$ [데이터 부재] | 설계 변경(ECN) 및 공정 변동성 반영 |

## 3. 심층 분석 (Deep Dive: Logic & Formulas)

### 3.1 기초 데이터 모델 (Baseline Metrics)
- **Planned Value (PV)**: 특정 시점 기준 계획된 작업의 예산 가치 [데이터 부재].
- **Actual Cost (AC)**: 실제 작업 수행에 투입된 누적 비용 [데이터 부재].
- **Earned Value (EV)**: 완료된 작업량에 할당된 예산 가치 [데이터 부재].

### 3.2 EAC 예측 시나리오 (Forecasting Logic)
상황별 가중치 기반 최종 비용 예측 모델:

1. **Typical Case (추세 유지)**: $EAC = BAC / CPI$ [데이터 부재].
   - 현행 비용 효율성($CPI$)의 프로젝트 종료 시까지 선형 지속 가정.
2. **One-time Anomaly (일시적 편차)**: $EAC = AC + (BAC - EV)$ [데이터 부재].
   - 과거 편차를 일시적 요인으로 간주, 잔여 작업은 계획($BAC$)대로 수행 가정.
3. **Double Constraint (비용-일정 동시 제약)**: $EAC = AC + \frac{BAC - EV}{CPI \times SPI}$ [데이터 부재].
   - 비용과 일정 효율을 동시 반영한 보수적(Conservative) 예측 모델.

## 4. 시스템 통합 및 고도화 (Integration & Advanced Analytics)
- **ERP-PMIS Real-time Sync**: ERP 지출 데이터(AC)와 PMIS WBS 진척도(EV) 간 API 연동을 통한 실시간 $CPI/SPI$ 대시보드 가동.
- **LSTM-based Predictive EAC**: 시계열 EVM 데이터를 LSTM(Long Short-Term Memory) 네트워크로 학습하여 위험 구간의 비선형 변동성을 반영한 확률적 EAC 예측 구현 [데이터 부재].

## 5. 정밀 검증 (Verification Cases)
- **Case A**: $CPI = 0.8$ [데이터 부재], $SPI = 1.2$ [데이터 부재]
  - **Diagnosis**: 일정 우위이나 비용 효율 저하 상태. 리소스 과투입(Crashing)에 의한 비용 상승 여부 검토 필수.
- **Case B**: $TCPI > 1.0$ [데이터 부재]
  - **Diagnosis**: 잔여 예산 내 목표 달성을 위해 현재 이상의 효율성 요구됨. 예산 증액 또는 Scope Reduction 검토 대상.
- **Case C**: $SV = 0$ [데이터 부재]
  - **Diagnosis**: 가치 기준 일정은 일치하나, 임계 경로(Critical Path) 지연 여부는 CPM(Critical Path Method) 분석을 통해 별도 검증 필요 [데이터 부재].