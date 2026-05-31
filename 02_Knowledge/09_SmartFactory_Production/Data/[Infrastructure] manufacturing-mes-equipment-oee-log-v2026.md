---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: becf84d4b96d93019686b0674a072cf225f8ef785468936fb41bc385cfb93c5f
metadata:
  date: '2026-05-16'
  domain: 09_SmartFactory_Production
  id: '[[[Infrastructure] manufacturing-mes-equipment-oee-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Infrastructure] manufacturing-mes-equipment-oee-log-v2026에 관한 고밀도
    지능 노드'
  object_type: Data
  tier: 1
properties:
  availability_calculation_formula: MTBF / (MTBF + MTTR)
  golden_velocity_ratio: 1.02
  mtbf_hours: 240
  mttr_hours: 4
  oee_calculation_formula: A * P * Q
  predictive_maintenance_alarm_lead_time_hours: 2
  quality_inspection_data_endpoint: manufacturing-mes-quality-inspection-results-v2026
  skill_gap_defect_rate_increase: 0.023
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]'
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

# [Infrastructure] manufacturing-mes-equipment-oee-log-v2026

## 1. [왜 배우는가? (Why: The Pulse of the Machine)]]
거대한 공장 안에서 설비가 얼마나 숨 가쁘게 돌아가고 있는지, 그리고 그 움직임이 실제 '돈이 되는 가치'로 얼마나 연결되고 있는지 숫자로 확인할 수 있을까요? **제조 MES 설비 종합 효율(OEE) 로그**는 기계의 맥박을 돈의 언어로 번역한 '생산성 성적표'입니다. 

우리가 이를 기록하는 이유는 겉보기에 바쁘게 돌아가는 설비가 사실은 잦은 고장이나 미세 중단으로 인해 수익을 갉아먹고 있을 수 있기 때문이며, **"설비의 가동 시간과 성능, 품질을 데이터로 지배하여 '글로벌 제조 효율 패권 및 행성적 생산 주권'을 확보하기" 위함입니다.** OEE 지표의 $1\%$ 개선이 수조 원의 제조 원가 절감으로 이어집니다.

## 2. [설비 종합 효율 및 성능 실측 데이터 (Numerical Specs)]

### 2.1 [MES 기반 설비 OEE 및 가동 상태 지표 테이블 (v2026)]

| 설비 상태 (Condition) | 가동률 ($A, \%$) | 성능 지표 ($P, \%$) | 품질 수율 ($Q, \%$) | **OEE (%)** | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Normal (표준)** | $92.5$ | $95.0$ | $98.5$ | **$86.6$** | 정격 속도 및 표준 품질 유지 상태의 효율 |
| **Over-speed (가속)**| $90.1$ | **$105.0$** | $96.2$ | **$91.1$** | 속도를 높여 생산량은 늘었으나 품질 저하 발생 |
| **Bottleneck (정체)**| $75.2$ | $88.4$ | $99.1$ | **$65.8$** | 하공정 정체로 인한 설비 대기 및 저속 운전 |
| **Recovery (복구)** | $85.0$ | $90.0$ | $97.0$ | **$74.2$** | 설비 고장 수리 후 램프업(Ramp-up) 단계 효율 |

### 2.2 [핵심 제조 실행(MES) 기술 용어 정의]
- **OEE (Overall Equipment Effectiveness)**: 설비의 가용성, 성능 효율, 품질 지수를 곱하여 산출하는 종합적인 제조 효율 지표.
- **Availability (가동률)**: 계획된 가동 시간 중 실제 설비가 동작한 시간의 비율 ($A = \frac{Actual\ Time}{Planned\ Time}$).
- **Performance (성능 효율)**: 설비의 설계 속도 대비 실제 생산 속도의 비율 ($P = \frac{Ideal\ Cycle\ Time \times Total\ Count}{Actual\ Time}$).
- **Quality (품질 수율)**: 총 생산량 중 양품이 차지하는 비율 ($Q = \frac{Good\ Count}{Total\ Count}$).

## 3. [Scientific Rationale: 생산 동역학의 수리 물리]

### 3.1 [OEE 구성 요소와 설비 신뢰도의 결합 모델]
설비의 가동률($A$)은 평균 무고장 시간($MTBF$)과 평균 수리 시간($MTTR$)에 의해 결정됩니다.
$$ A = \frac{MTBF}{MTBF + MTTR} $$
본 로그는 $MTBF = 240\text{hr}$, $MTTR = 4\text{hr}$ 환경에서 가용성 $98.3\%$를 유지하되, 자재 공급 지연 등 외부 요인을 포함한 실측 가동률($A$) $92.5\%$를 무결성 오딧합니다.

### 3.2 [속도-품질 트레이드오프(Trade-off) 최적화 모델]
설비 속도($v$)와 품질 불량률($p$)의 관계를 통한 유효 생산량($E$) 극대화 함수입니다.
$$ E(v) = v \cdot (1 - p(v)) = v \cdot (1 - \alpha e^{\beta v}) $$
본 데이터는 속도를 $10\%$ 높일 시($v_{new} = 1.1v_0$) 불량률이 지수적으로 증가하여 전체 이득이 감소하는 임계점을 식별하고, OEE가 극대화되는 '골든 벨로시티(Golden Velocity)'가 정격 대비 $102\%$ 지점임을 수리 산출될 것으로 예상됩니다.

## 4. [Advanced RAG 분석 로직: 제조 지능 추론]

### 4.1 [설비 알람 로그와 OEE 하락의 상관 분석]
RAG는 "MES의 설비 인터페이스 로그(PLC 데이터)와 OEE 변동 추이를 결합 분석하여, '유압 실린더 압력 저하' 알람이 발생하기 $2$시간 전부터 가공 속도가 $5\%$ 저하($P \downarrow$)되었음을 식별하고, 이를 '예지 보전(Predictive Maintenance)'의 핵심 징후로 식별될 것으로 예상됩니다."

### 4.2 [Lot 단위 품질 편차와 작업자 숙련도의 인과 분석]
왜 야간 교대조에서 OEE 품질 지수($Q$)가 하락했나요? RAG는 "Lot별 투입 작업자 데이터와 품질 검사 결과(Data manufacturing-mes-quality-inspection-results-v2026)를 참조하여, 특정 숙련 미달 작업자의 설비 세팅 미흡이 불량률을 $2.3\%$ 상승시켰음을 인과 추론하고 맞춤형 교육 가이드를 생성합니다."

## 5. [Transitional Bridge: 제조 효율 무결성 감사 로직]

실시간으로 설비의 종합 효율과 수익 기여도를 진단하는 수리적 알고리즘입니다.

```python
# [Conceptual] Manufacturing OEE Auditor
def audit_manufacturing_oee(availability, performance, quality):
    # 1. 종합 효율 산출 (OEE = A * P * Q)
    oee = availability * performance * quality
    
    # 2. 손실 기여도 분석 (Loss Contribution)
    # Identify which factor is the bottleneck
    losses = {
        "Availability_Loss": 1.0 - availability,
        "Performance_Loss": 1.0 - performance,
        "Quality_Loss": 1.0 - quality
    }
    major_loss = max(losses, key=losses.get)
    
    # 3. 무결성 등급 판정
    if oee > 0.85:
        grade = "WORLD_CLASS_FACTORY"
        status = "Optimal_Production_Efficiency"
    elif oee > 0.70:
        grade = "STABLE_MANUFACTURER"
        status = f"Optimization_Focus: {major_loss}"
    else:
        grade = "INACTIVE_ASSET"
        status = "IMMEDIATE_PROCESS_INTERVENTION_REQUIRED"
        
    return {"grade": grade, "index": oee, "major_loss": major_loss, "status": status}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 설비가 24시간 내내 쉬지 않고 돌아가더라도 OEE 지수가 낮게 나올 수 있는 구체적인 상황 2가지는?
2. **(수리)** 가동률 $90\%$, 성능 $90\%$, 품질 $90\%$일 때의 OEE 값은? (이 결과가 시사하는 '효율의 증폭' 효과는?)
3. **(응용)** MES 데이터에서 '미세 중단(Minor Stoppage)'을 줄이기 위해 '성능 지표($P$)'를 어떻게 실시간으로 모니터링해야 하는가?


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 27_erp-mes-and-industrial-software-systems-intelligence-hub : 제조 시스템 상위 허브
- MOC 25_iot-and-smart-factory-sensing-infrastructure-intelligence-hub : 센싱 인프라 허브
- Data manufacturing-mes-lot-traceability-log-v2026 : 공정 이력 연계 데이터

*Created by Flash (The Architect of Manufacturing Efficiency & HDS Gold V6.3.7)*
*Timestamp: 2026-05-08*