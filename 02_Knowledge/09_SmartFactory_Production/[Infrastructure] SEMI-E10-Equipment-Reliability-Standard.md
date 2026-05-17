---
metadata:
  id: "[[[Infrastructure] SEMI-E10-Equipment-Reliability-Standard]]"
  domain: "09_SmartFactory_Production"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Infrastructure] SEMI-E10-Equipment-Reliability-Standard에 관한 고밀도 지능 노드"
semantic:
  tags: ["#09_SmartFactory_Production", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Infrastructure] SEMI-E10-Equipment-Reliability-Standard

## 1. [왜 배우는가? (Why)]
반도체 공장은 1분 1초가 돈입니다. 수천억 원짜리 장비가 멈춰 있는 시간은 고스란히 손실로 이어집니다. SEMI E10은 장비가 얼마나 믿을만한지(Reliability), 언제든 쓸 수 있는지(Availability), 고장 나면 얼마나 빨리 고칠 수 있는지(Maintainability)를 전 세계 반도체 업계가 똑같은 기준으로 계산하게 만든 약속입니다. SEMI E10을 이해하는 것은 장비의 가동률을 극대화하고, 데이터에 기반하여 유지보수 전략을 세우는 '장비 운영의 표준 언어'를 마스터하는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Metric | Full Name | Engineering Rationale |
|:---|:---:|:---|
| **Availability**| Uptime Ratio | 전체 시간 중 장비가 실제 가동 가능한 상태로 유지된 비율 |
| **MTBF** | Mean Time Between Failures | 고장과 고장 사이의 평균 시간. 장비의 '신뢰성'을 나타내는 지표 |
| **MTTR** | Mean Time To Repair | 고장 발생 후 수리가 완료될 때까지의 평균 시간. '유지보수성' 지표 |
| **MTBA** | Mean Time Between Assist | 엔지니어의 수동 개입이 필요할 때까지의 평균 시간. '자동화 수준' 지표 |
| **State 1~6** | Equipment States | 장비를 가동(Productive), 대기(Standby), 보수(Scheduled/Unscheduled) 등 6단계로 분류 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 가동률(Availability) 산출의 객관성
- **논리**: 단순히 "잘 돌아간다"는 주관적인 판단은 공장 운영에 도움이 되지 않습니다. 
- **결과**: SEMI E10은 168시간(1주일)을 기준으로 장비의 상태를 6가지(Productive, Standby, Engineering, Scheduled Downtime, Unscheduled Downtime, Non-Scheduled Time)로 명확히 구분하여, 누구나 동의할 수 있는 객관적인 가동률 지표를 산출될 것으로 예상됩니다.

### 3.2 고장 패턴 분석과 예방 정비
- **논리**: MTBF가 짧아진다는 것은 장비의 부품 노후화나 공정 조건의 불안정을 의미합니다. 
- **효과**: SEMI E10 데이터를 장기적으로 추적하면 장비의 수명 주기를 예측할 수 있으며, 이는 사후 수리(Reactive)에서 사전 예방(Preventive) 및 예후 관리(Predictive)로 유지보수 패러다임을 전환하는 근거가 됩니다.

## 4. [코드 연결 해설 (RAM Metrics Calculation Logic)]
장비 상태 로그를 기반으로 주요 신뢰성 지표를 계산하는 논리 구조입니다.
```python
# 장비 지능 기반 SEMI E10 지표 산출 논리
def calculate_semi_e10_metrics(total_time, state_logs):
    # 1. 각 상태별 시간 합산
    productive_time = sum(log.duration for log in state_logs if log.state == "PRODUCTIVE")
    unscheduled_downtime = sum(log.duration for log in state_logs if log.state == "UNSCHEDULED")
    
    # 2. 가동률(Availability) 계산
    availability = (productive_time + standby_time) / (total_time - non_scheduled_time) * 100
    
    # 3. MTBF 계산 (고장 횟수로 나눔)
    mtbf = productive_time / len([log for log in state_logs if log.state == "UNSCHEDULED"])
    
    # 4. MTTR 계산 (수리 시간의 평균)
    mttr = unscheduled_downtime / len([log for log in state_logs if log.state == "UNSCHEDULED"])
    
    return {"availability": availability, "mtbf": mtbf, "mttr": mttr}
```

## 5. [스스로 체크 (Self-Audit)]
1. 'Scheduled Downtime'과 'Unscheduled Downtime'의 결정적인 차이점은?
2. 'Availability'가 90% 이상임에도 불구하고 'MTBF'가 매우 짧다면, 장비 운영상 어떤 문제가 있는 것인가?
3. 'MTBA(Mean Time Between Assist)'를 개선하기 위해 '자율 제어(APC)' 기술이 어떻게 기여하는가?
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
