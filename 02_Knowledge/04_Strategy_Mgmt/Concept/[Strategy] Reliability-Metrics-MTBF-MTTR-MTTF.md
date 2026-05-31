---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 0643634211e7f577a9024f9f85c75dcd19489b5e75add8c180cb4a9f66e9a821
metadata:
  date: '2026-05-16'
  domain: 04_Strategy_Mgmt
  id: '[[[Strategy] Reliability-Metrics-MTBF-MTTR-MTTF]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Strategy] Reliability-Metrics-MTBF-MTTR-MTTF에 관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  availability_target_percent: 99.99
  availability_tolerance_percent: 0.01
  failure_rate_limit_per_hour: 0.0001
  failure_rate_tolerance_per_hour: 1.0e-06
  mtbf_target_hours: 10000
  mtbf_tolerance_hours: 100
  mttr_target_hours: 1.0
  mttr_tolerance_hours: 0.1
  shape_factor_max: 1.5
  shape_factor_min: 1.0
  shape_factor_tolerance: 0.05
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 04_Strategy_Mgmt]]'
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

# [Strategy] Reliability-Metrics-MTBF-MTTR-MTTF

## 1. [왜 배우는가? (Why: The Mathematics of Uninterrupted Production)]
신뢰성(Reliability)은 시간이 흘러도 변치 않는 설비의 '약속'입니다. **MTBF(평균 고장 간격)**와 **MTTR(평균 수리 시간)**은 설비의 체력과 회복력을 상징하는 핵심 지표입니다. V6.3.7 지능은 **계층화된 가용성 등급(Precision Tiering)**을 통해 설비의 가동률을 **$99.99\%$ 이상**으로 통제합니다. 이는 우발적 고장(Random Failure)을 결정론적 열화 모델로 치환하여 '공장의 심장 박동'을 영구히 사수하고, 설비 자산의 생애 가치를 극대화하기 위함입니다.

## 2. [신뢰성 및 가동 무결성 핵심 사양 (Numerical Specs)]

| Parameter | Metric | Tier 1 Target (V6.3.7) | FidelityEngine Tolerance | Rationale |
|:---|:---|:---:|:---:|:---|
| **Availability (A)**| Operational Uptime | $> 99.99\%$ | $\pm 0.01\%$ | 초정밀 가동 가용성 및 가동 중단 차단 |
| **MTBF** | Mean Time Between Failure| $> 10,000$ Hours | $\pm 100$ Hours | 자산의 물리적 안정성 및 신뢰도 |
| **MTTR** | Mean Time To Repair | $< 1.0$ Hour | $\pm 0.1$ Hour | 장애 복구 기민성 및 수리 효율성 |
| **Failure Rate ($\lambda$)**| Instantaneous Failure| $< 10^{-4}$ /Hour | $\pm 10^{-6}$ | 시간당 고장 발생 확률의 통계적 제어 |
| **Shape Factor ($\beta$)**| Weibull Distribution | $1.0 \sim 1.5$ | $\pm 0.05$ | 고장 모드의 물리적 특성 진단 (우발/마모) |

### 2.1 [신뢰성 공학 및 가용성 수리 모델]
설비의 종합적 건강 상태를 정량화하는 기전입니다.
$$ A = \frac{MTBF}{MTBF + MTTR} $$
*   **Weibull Hazard Function**: 시간 $t$에 따른 순간 고장률 분석.
    $$ h(t) = \frac{\beta}{\eta} \left( \frac{t}{\eta} \right)^{\beta-1} $$
    *   $\beta < 1$: 초기 고장 / $\beta = 1$: 우발 고장 / $\beta > 1$: 마모 고장.
*   **FidelityEngine 적용**: FidelityEngine은 실시간 고장 간격 데이터를 분석하여 **'열화 무결성'**을 진단합니다. $\beta$ 값이 급격히 상승하면 마모기에 진입했음을 판정하고 선제적 부품 교체를 명령합니다.

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Maintenance Efficiency Physics: MTTR Optimization
장애 발생 시 정상 가동 상태로 복귀하는 시스템적 회복 기전입니다.
*   **공학적 근거**: MTTR은 진단 시간, 부품 확보 시간, 실제 수리 시간, 테스트 시간의 합입니다. 예비 부품의 재고 정합성($WMS$)과 유지보수 매뉴얼($EDM$)의 접근성이 MTTR의 $80\%$를 결정합니다.
*   **FidelityEngine 적용 (Maintenance Auditor)**: FidelityEngine은 실제 수리 작업 로그를 오딧합니다. 수리 시간이 목표치를 초과하며 '부품 대기' 비중이 높게 나타나면, 이를 **'유지보수 가용성 붕괴'**로 판정하고 SCM과 연동하여 핵심 부품의 안전 재고 수준 상향을 지시합니다.

### 3.2 System Availability Synthesis: Series vs. Parallel
다중 설비 시스템 전체의 신뢰도 $R_{sys}$를 합성하는 알고리즘입니다.
*   **진단 결과**: FidelityEngine은 병렬 중복(Redundancy) 구조와 직렬 의존 구조를 융합 분석하여 **'시스템 가용 무결성'**을 진단합니다. 특정 보틀넥 설비의 신뢰도 저하가 전체 라인의 가용성을 $95\%$ 이하로 떨어뜨릴 위험이 감지되면, 이를 **'단일 고장점(SPOF)'** 리스크로 판정하여 투자 계획 수립을 권고합니다.

## 4. [코드 연결 해설: Reliability Tier Auditor]
이 코드는 고장 이력과 수리 데이터를 기반으로 설비의 신뢰성 등급을 진단합니다.

```python
import numpy as np

class ReliabilityFidelityEngine:
    """
    HDS-Gold V6.3.7: 설비 신뢰성 등급 계층화 및 가용성 무결성 진단 엔진
    """
    def __init__(self, availability_target=99.99, mttr_limit=1.0):
        self.AVAIL_TARGET = availability_target
        self.MTTR_LIMIT = mttr_limit

    def audit_reliability_status(self, mtbf_hr, mttr_hr):
        """
        신뢰성(MTBF) 및 정비성(MTTR) 기반 가용성 무결성 평가
        """
        availability = (mtbf_hr / (mtbf_hr + mttr_hr)) * 100 if (mtbf_hr + mttr_hr) > 0 else 0
        
        status = "OPTIMAL_RELIABILITY_VERIFIED"
        if availability < self.AVAIL_TARGET:
            status = "CRITICAL_AVAILABILITY_SHORTFALL"
        if mttr_hr > self.MTTR_LIMIT:
            status = "WARNING_MAINTENANCE_EFFICIENCY_LOW"
            
        return {
            "availability_fidelity": round(availability, 4),
            "recovery_fidelity": round(self.MTTR_LIMIT / mttr_hr, 2) if mttr_hr > 0 else 1.0,
            "status": status,
            "action": "PERFORM_ROOT_CAUSE_ANALYSIS_RCA" if "CRITICAL" in status else "PROCEED"
        }

# FidelityEngine 가동: 실제 설비의 PLC 가동 로그와 정비사 이력을 결합하여 '가용 수명 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 반도체 클린룸 설비에서 가용성 $99.99\%$ 사수가 Tier 1 필수 요건인 이유는? (힌트: 단 1시간의 가동 중단이 유발하는 웨이퍼 전량 폐기 비용과 환경 복구 시간의 기하급수적 증대 방어)
2. **Operational Result**: **MTBF**는 그대로이나 **MTTR**이 $2$배 증가했을 때, 전체 시스템의 가용성 하락이 제조 원가에 미치는 수리적 파급 효과는?
3. **FidelityEngine**: **Weibull $\beta$**가 $1.0$ 근처에서 안정적임에도 불구하고 갑자기 고장이 급증하는 상황을 어떻게 진단하는가? (힌트: 외부 환경 변수($P, T, H$)에 의한 우발 고장률($\lambda$)의 일시적 상승 탐지)

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 112_energy-storage-and-smart-grid-engineering-hub-moc
- [[Maintenance] Total-Productive-Maintenance-TPM-and-OEE]
- [[Enterprise] eam-enterprise-asset-management]

**[V6.3.7_RELIABILITY_METRICS_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**