---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: c10f5736c9a64e44e45960f32c0e7aca5cf3b5cd6da1eb250d537878904c3b60
metadata:
  date: '2026-05-16'
  domain: 04_Strategy_Mgmt
  id: '[[[Strategy] eam-enterprise-asset-management]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Strategy] eam-enterprise-asset-management에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  asset_utilization_fidelity_tolerance_percent: 0.5
  asset_utilization_target_percent: 92.0
  maintenance_revenue_ratio_fidelity_tolerance_percent: 0.2
  maintenance_revenue_ratio_max_percent: 10.0
  mtbf_fidelity_tolerance_hours: 10
  mtbf_target_hours: 500
  mttr_fidelity_tolerance_hours: 0.1
  mttr_target_hours: 2.0
  pdm_coverage_fidelity_tolerance_percent: 2.0
  pdm_coverage_target_percent: 70.0
  tco_replacement_cost_threshold_ratio: 0.6
  vibration_ucl_threshold_increase_ratio: 0.15
  weibull_beta_infant_mortality: < 1
  weibull_beta_random_failure: '1'
  weibull_beta_wear_out: '> 1'
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

# [Strategy] eam-enterprise-asset-management

## 1. [왜 배우는가? (Why: The Guardian of Assets)]
기업의 생산 능력은 보유한 물리적 자산의 '건강 상태'에 수렴합니다. **Enterprise Asset Management (EAM)**은 설비, 건물, 인프라의 전 수명 주기를 관리하여 자산 가용성을 극대화하고 운영 비용($OpEx$)을 최적화하는 '자산의 수호자'입니다. 설비의 고장이 발생한 후 수리하는 사후 보전(BM)은 이미 늦습니다. V6.3.7 지능은 **신뢰성 중심 유지보수(RCM)**와 **예지 보전(PdM)**을 통해, 돌발 고장 리스크를 제로화하고 기업의 자산 가치를 결정론적으로 방어합니다.

## 2. [EAM 자산 신뢰성 및 운영 사양 (Numerical Specs)]

| Parameter | Metric | Tier 1 Target (V6.3.7) | FidelityEngine Tolerance | Rationale |
|:---|:---|:---:|:---:|:---|
| **MTBF** | Mean Time Between Failure| $> 500$ Hours | $\pm 10$ Hours | 자산의 신뢰성 및 가동 지속성 |
| **MTTR** | Mean Time To Repair | $< 2.0$ Hours | $\pm 0.1$ Hours | 수리 기민성 및 가동 중단 최소화 |
| **PdM Coverage**| Predictive Maintenance | $> 70.0\%$ | $\pm 2.0\%$ | 데이터 기반의 선제적 장애 예방 |
| **Utilization** | Asset Utilization Rate | $> 92.0\%$ | $\pm 0.5\%$ | 자산 투자 효율 및 가동 정규성 |
| **Cost Ratio** | Maintenance/Revenue | $< 10.0\%$ | $\pm 0.2\%$ | 유지보수 비용의 재무적 적정성 |

### 2.1 [자산 신뢰성 및 수명 수리 모델]
고장 확률을 수학적으로 예측하여 교체 주기를 최적화하는 기전입니다.
*   **Weibull Distribution Analysis**: 고장 데이터($t$)의 분포를 통한 고장 단계 분석.
    $$ f(t) = \frac{\beta}{\eta} \left( \frac{t}{\eta} \right)^{\beta-1} e^{-(t/\eta)^\beta} $$
    *   $\beta < 1$: 초기 고장(Infant Mortality) / $\beta = 1$: 우발 고장 / $\beta > 1$: 마모 고장(Wear-out).
*   **FidelityEngine 적용**: FidelityEngine은 실시간 IoT 진동/열 데이터를 분석하여 **'자산 신뢰성 무결성'**을 진단합니다.

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Predictive Maintenance Physics (Vibration & Thermal)
설비의 물리적 신호를 통해 잠재적 결함을 포착하는 기전입니다.
*   **공학적 근거**: 베어링 마모나 축 정렬 불량(Misalignment)은 초기 단계에서 특정 주파수의 미세 진동과 열 변형으로 나타납니다. EAM은 이를 FFT(Fast Fourier Transform)로 분석하여 고장 시점을 정밀하게 예측해야 합니다.
*   **FidelityEngine 적용 (Asset Health Auditor)**: FidelityEngine은 센서 데이터의 트렌드를 오딧합니다. 진동 진폭이 통계적 관리 한계(UCL)를 $15\%$ 이상 초과하며 $\beta$ 값이 급격히 상승하면, 이를 **'치명적 고장 징후'**로 판정하고 즉시 생산 라인 정지 및 부품 교체를 권고합니다.

### 3.2 Total Cost of Ownership (TCO) Optimization
자산의 도입부터 폐기까지의 경제적 타당성을 분석하는 알고리즘입니다.
*   **진단 결과**: FidelityEngine은 자산의 수리 비용 누적액과 신규 도입 비용을 대조하여 **'자산 운영 경제성'**을 진단합니다. 수리 비용이 자산 가액의 $60\%$를 초과하는 지점을 포착하여, 최적의 자산 교체(Replacement) 시점을 전략적으로 도출합니다.

## 4. [코드 연결 해설: EAM Reliability Auditor]
이 코드는 자산의 가용성(Availability)과 신뢰성 지표를 진단합니다.

```python
class EAMFidelityEngine:
    """
    HDS-Gold V6.3.7: 자산 신뢰성 및 유지보수 무결성 진단 엔진
    """
    def __init__(self, availability_target=0.92, mttr_limit=2.0):
        self.AVAIL_TARGET = availability_target
        self.MTTR_LIMIT = mttr_limit

    def audit_asset_integrity(self, mtbf_hr, mttr_hr):
        """
        가용성(Availability) 및 복구 속도 기반 무결성 평가
        """
        availability = mtbf_hr / (mtbf_hr + mttr_hr) if (mtbf_hr + mttr_hr) > 0 else 0
        
        status = "ASSET_RELIABILITY_VERIFIED"
        if availability < self.AVAIL_TARGET:
            status = "CRITICAL_AVAILABILITY_DEFICIT"
        if mttr_hr > self.MTTR_LIMIT:
            status = "WARNING_MAINTENANCE_LATENCY_HIGH"
            
        return {
            "availability_fidelity": round(availability, 4),
            "mttr_fidelity": round(self.MTTR_LIMIT / mttr_hr, 2) if mttr_hr > 0 else 1.0,
            "status": status,
            "action": "PERFORM_ROOT_CAUSE_ANALYSIS_RCA" if "CRITICAL" in status else "CONTINUE_PM"
        }

# FidelityEngine 가동: IoT 진동 센서 로그와 유지보수 작업(Work Order) 이력을 결합하여 '자산 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: EAM 시스템에서 **MTTR**이 Tier 1 필수 요건인 이유는? (힌트: 고정밀 설비의 정지 시간은 분당 수백만 원의 기회 손실을 발생시키며, 수리 시간이 2시간을 초과할 경우 전체 공정 밸런스가 붕괴되는 '생산 연속성 위기' 방지)
2. **Operational Result**: **MTBF**가 $10\%$ 개선될 때, 연간 생산량 증대 및 부품 재고 비용 절감 효과를 수리적으로 어떻게 증명하는가?
3. **FidelityEngine**: **Availability**는 높으나 **OEE**가 낮은 파라독스 상황을 어떻게 진단하는가? (힌트: 설비는 켜져 있으나 실제 속도 손실이나 품질 불량이 발생하는 '성능 저하' 포착)

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 01_Enterprise_Core
- [[Enterprise] erp-enterprise-resource-planning]
- [[Enterprise] mes-manufacturing-execution-system]

**[V6.3.7_ENT_EAM_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**