---
Basic:
  id: "[[[Strategy] TBM-Time-Based-Maintenance-Strategy"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
  is_part_of: []]
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

# [[[Strategy] TBM-Time-Based-Maintenance-Strategy

## 1. [왜 배우는가? (Why)]]
자동차 엔진 오일을 일정 주행 거리마다 갈아주듯이, 산업 현장의 장비들도 일정 시간(또는 횟수)마다 점검하고 소모품을 바꿔줘야 합니다. 이를 TBM(Time Based Maintenance, 시간 기반 보전)이라고 합니다. 가장 고전적이면서도 확실한 예방 정비 방식입니다. TBM을 이해하는 것은 장비가 고장 나서 멈추기 전에 미리 선제적으로 대응하여, 공장의 가동률을 예측 가능한 범위 내에서 안정적으로 관리하는 '유지보수의 정석'을 배우는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Technology / Logic | Engineering Rationale |
|:---|:---:|:---|
| **PM Schedule** | Fixed Interval | 시간(Hours) 또는 가동 횟수(Cycles)에 따라 자동으로 유지보수 일정을 생성 |
| **Bathtub Curve**| Failure Pattern | 초기 고장, 우발 고장, 마모 고장 구간을 분석하여 최적의 교체 주기 설정 |
| **Consumables** | Parts Life-cycle | 베어링, 필터, 오링 등 수명이 정해진 부품들의 교체 이력 관리 |
| **PM Checklist** | SOP Integration | 점검 시 반드시 확인해야 할 항목들을 표준화하여 작업자의 편차 제거 |
| **Availability** | Scheduled Down | 정기 점검 시간을 미리 생산 계획에 반영하여 라인 중단 영향을 최소화 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 신뢰성 기반의 부품 교체 주기 산출
- **논리**: 너무 일찍 갈면 돈이 아깝고, 너무 늦게 갈면 고장이 납니다. 
- **결과**: 통계적 수명 분석(Weibull Distribution)을 통해 고장 확률이 급격히 높아지는 시점 직전에 부품을 교체함으로써, 고장 수리 비용(Corrective)보다 저렴한 예방 정비 비용(Preventive)으로 시스템 신뢰성을 극대화합니다.

### 3.2 작업 표준화와 숙련도 의존성 감소
- **논리**: 숙련된 기술자만 아는 노하우에 의존하면 정비 품질이 불균일해집니다. 
- **효과**: TBM은 정해진 시간에 정해진 매뉴얼에 따라 점검하도록 강제함으로써, 누가 정비를 하더라도 동일한 수준의 장비 가동 성능을 유지할 수 있는 운영 체계를 구축합니다.

## 4. [코드 연결 해설 (PM Scheduling Logic)]
장비 가동 시간을 추적하여 정기 점검 알람을 발생시키는 논리 구조입니다.
```python
# 전략 지능 기반 TBM 정기 점검 스케줄링 논리
def schedule_periodic_maintenance(tool_id):
    # 1. 장비 누적 가동 시간 및 사이클 수 획득
    accumulated_hours = tool_monitor.get_runtime(tool_id)
    cycle_count = tool_monitor.get_cycles(tool_id)
    
    # 2. 마스터 DB의 PM 임계치 확인 (예: 1000시간 또는 10만 사이클)
    pm_threshold_hours = pm_db.get_threshold(tool_id, "HOURS")
    
    # 3. PM 시점 도달 판단
    if accumulated_hours >= pm_threshold_hours:
        # 생산 관리 시스템(MES)에 장비 중단 예약 요청
        mes_bridge.request_pm_downtime(tool_id, priority="HIGH")
        return "SCHEDULE_PM_SOON"
        
    return "OPERATIONAL_NORMAL"
```

## 5. [스스로 체크 (Self-Audit)]
1. 'TBM' 방식이 'CBM(상태 기반 보전)'보다 경제적으로 불리할 수 있는 시나리오는?
2. '욕조 곡선(Bathtub Curve)'에서 마모 고장(Wear-out Failure) 구간이 시작되기 전에 교체를 수행해야 하는 공학적 이유는?
3. 정기 점검(PM) 준수율이 낮아질 때 '가용성(Availability)'에 미치는 장기적 영향은?
---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
