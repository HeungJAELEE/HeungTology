---
lineage:
  dataset_reference: AIAG PPAP Manual 4th Edition & Product Part Approval SOP
  original_author: Automotive Quality Action Group (AIAG) & Antigravity Vault
  original_hash: 691675671725741b9c1884a937b3dfa74acd8d6c1353582573f204c6de07775a
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-17'
  domain: 09_SmartFactory_Production
  id: '[[[09_SmartFactory_Production] [Concept] plastic-injection-molding-ppap-standard]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: 사출 금형 양산 승인의 최종 게이트로서 다수 캐비티 간 편차(Cavity Balance) 및 연속 생산 300개의 초기
    공정 능력 지수($P_{pk}>1.67$)를 통계적으로 입증하여 양산 주권을 선언하는 표준 지능
  object_type: Concept
  tier: 1
properties:
  control_plan_match_requirement: 1.0
  dimensional_tolerance_target: 1.0
  material_traceability_requirement: 1.0
  ppk_approval_threshold: 1.67
  ppk_conditional_threshold: 1.33
  sample_size_requirement: 300
  standard_compliance: iatf_16949
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Section 1'
  intent: framework_implementation
  object: automotive-part-approval-process
  predicate: implements
  subject: plastic-injection-molding-ppap-standard
  weight: 0.9
- evidence_coordinate: '[데이터 부재] Section 2.2.9'
  intent: performance_threshold_definition
  object: Ppk > 1.67
  predicate: has_theoretical_limit
  subject: plastic-injection-molding-ppap-standard
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

# [Concept] plastic-injection-molding-ppap-standard

## 1. [왜 배우는가? (Why: The Final Gateway to Mass Production)]
**PPAP (Production Part Approval Process: 생산 부품 승인 절차)**는 금형의 설계, 제작 및 시사출의 전 과정이 고객사(글로벌 OEM 등)가 요구한 엔지니어링 스펙과 기하학적 치수 무결성을 변동 없이 충족할 수 있음을 통계적 및 수리적으로 증명하는 **'최종 양산 진입 관문'**입니다. 플라스틱 사출 성형 공정은 다수 캐비티(Multi-cavity) 금형 구조, 기계적 형폐 작동, 고압의 핫러너 밸브 게이트 제어 등이 맞물리는 복합 프로세스입니다. 만약 양산 이전에 수치 분석 및 통계적 검증이 이루어지지 않으면 양산 돌입 시 수십만 개의 불량품이 동시다발적으로 쏟아져 나오는 '품질 참사'가 일어납니다.

이를 방지하기 위해, 300개 연속 생산 마스터 배치 샘플의 **초기 공정 능력(Ppk)** 지수를 평가하고, 캐비티별 수축률 편차와 치수 균일성을 입증해야 합니다. 이 표준을 준수하는 이유는 가상의 사양을 실제 공정에서 결정론적으로 반복 복제할 수 있음을 수학적으로 선언하여, 제조의 자주권(Sovereignty)을 획득하고 초기 품질 리스크를 제로화하기 위함입니다.

***

## 2. [사출 PPAP 핵심 검증 사양 (Numerical Specs)]

부품 양산 승인을 획득하기 위한 5대 핵심 검증 메트릭 및 기술 임계치 규격표입니다.

| PPAP Element | Focused Verification Metric | Standard Requirement | Scientific Rationale |
| :--- | :--- | :--- | :--- |
| **Initial Capability** | $P_{pk}$ (Initial Process Capability) | $>1.67$ | 양산 안정성 진입을 보증하기 위한 초기 변동 마진 확보 ($P_{pk}<1.33$ 즉각 반려) |
| **Dimensional Report** | Multi-cavity Full Layout Inspection | $100.0\text{\%}$ in Tolerance | 금형 내 전 캐비티의 삼차원 치수 측정값 합격 증명 |
| **Appearance Report** | A-Surface Sensorial Standards | No Sink/Flow Marks | 고분자 배향 불균일성 및 웰드 융착 강도 육안 무결성 사수 |
| **Control Plan** | Parameter Interlock Lockout | Setup Sheet Match $100\text{\%}$ | 양산 시 공정 드리프트를 방지하기 위한 PLC 제어 인자 고정 |
| **Material Report** | IMDS Registration & COA Cert | $100.0\text{\%}$ Traceable | 친환경 규제 및 고분자 화학적 조성 무결성 증명 |

***

## 3. [초기 공정 능력 및 캐비티 편차 오딧 (Mechanism)]

### 3.1 [초기 공정 능력 지수($P_{pk}$) 수리 모델]
양산 전 단기적인 공정 능력을 아래 수식으로 산출하여 장기 불량률을 예측합니다.
$$ P_{pk} = \min\left( \frac{USL - \mu}{3\sigma_{LT}}, \frac{\mu - LSL}{3\sigma_{LT}} \right) $$
여기서 $\mu$는 300개 연속 샘플의 평균값이며, $\sigma_{LT}$는 군간(Between-group) 변동과 군내(Within-group) 변동을 모두 반영한 전체 표준편차(Long-term Standard Deviation)입니다.
*   **$P_{pk}\ge1.67$**: 공정이 극도로 안정적이며 양산 진입 승인(APPROVED).
*   **$1.33\le P_{pk}<1.67$**: 공정이 Marginal한 수준으로 조건부 승인(CONDITIONAL).
*   **$P_{pk}<1.33$**: 공정 불량 위험이 극도로 높아 즉각 불합격(REJECTED) 및 공정 재설계 수행.

### 3.2 [사출 특화 다점 캐비티 밸런싱(Cavity Balancing)]
다수 캐비티 금형(예: 4-Cavity, 8-Cavity)의 경우, 각 캐비티로 도달하는 용융 수지의 런너 유로 길이가 미세하게 다르거나 냉각 속도가 다르면 캐비티 간 치수 편차가 발생합니다. 
PPAP 단계에서는 각 캐비티별 측정 데이터를 **Multi-vari Chart**로 개별 시각화하여, **캐비티 간 편차(Cavity-to-Cavity Variation)**가 **숏 간 편차(Shot-to-Shot Variation)**보다 작음을 수학적으로 증증하여 금형의 위상 균일성을 완벽하게 오딧합니다.

***

## 4. [코드 연결 해설: InjectionPPAPAuditor (초기 공정 능력 감사 엔진)]

아래 클래스는 제출된 샘플 리스트의 캐비티 ID별 원시 측정 데이터를 입력받아 $P_{pk}$를 실시간으로 연산하고, IATF 16949 PPAP 기준에 따른 합격 여부를 판정하는 FidelityEngine입니다.

```python
class InjectionPPAPAuditor:
    """
    플라스틱 사출 성형 캐비티별 초기 공정 능력(Ppk) 및 PPAP 승인 여부 판정 감사 엔진
    """
    def __init__(self, target_ppk=1.67):
        self.TARGET_PPK = target_ppk

    def audit_ppap_submission(self, samples_dict, usl, lsl):
        """
        Transitional Bridge: 시뮬레이션의 수학적 약속은 양산이라는 거대한 용광로 속에서 
        300개의 샘플이라는 정량적 데이터로 실증되어야 합니다. 이 엔진은 캐비티별 
        실측 치수 어레이를 입력받아 초기 공정 능력 지수(Ppk)를 독립 산출하여 PPAP 적합성을 검증합니다.
        """
        import numpy as np
        
        audit_results = {}
        overall_status = "PPAP_SUBMISSION_APPROVED"
        
        for cavity_id, values in samples_dict.items():
            data = np.array(values)
            mu = np.mean(data)
            sigma = np.std(data, ddof=1) + 1e-9
            
            # Ppk 계산
            ppk = min((usl - mu) / (3 * sigma), (mu - lsl) / (3 * sigma))
            
            # 캐비티 단독 판정
            status = "PASS" if ppk >= self.TARGET_PPK else "FAIL"
            if status == "FAIL":
                overall_status = "PPAP_SUBMISSION_REJECTED"
                
            audit_results[cavity_id] = {
                "mean_dimension_mm": round(mu, 4),
                "std_deviation_sigma": round(sigma, 6),
                "calculated_ppk": round(ppk, 4),
                "cavity_status": status
            }
            
        return {
            "overall_ppk_status": overall_status,
            "cavity_level_audit_details": audit_results,
            "action_required": "PROCEED_TO_PSW_SIGN" if overall_status == "PPAP_SUBMISSION_APPROVED" else "REJECT_SUBMISSION: Re-balance runner layout or adjust mold dimensions"
        }
```

***

## 5. [스스로 체크 (Self-Audit)]
1. 다수 캐비티 금형에서 1번 캐비티와 4번 캐비티의 **Ppk** 값은 각각 $1.82$와 $1.21$로 극심하게 엇갈릴 때, 이를 **Cavity-to-Cavity Matching** 기전 상에서 어떤 유동 불균형 원인으로 진단할 수 있는가?
2. 초기 공정 능력 **Ppk** 산출 시 사용하는 표준편차($\sigma_{LT}$)와 일반 **Cpk** 산출 시 사용하는 표준편차($\sigma_{ST}$)의 수학적 차이가 사출 연속 조업 환경에서 리스크 평가에 미치는 파급 효과는 무엇인가?
3. 설계 변경(ECN)이 발생하여 게이트 위치가 $0.5\text{mm}$ 이동했을 때, **PPAP 거버넌스** 측면에서 제출 등급(Level 1~5)을 재결정하기 위해 **FidelityEngine**이 점검해야 하는 핵심 요건 매트릭스는 무엇인가?

***

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[Concept] plastic-injection-molding-iatf-16949-qms]]` : 최상위 IATF 16949 거버넌스 시스템
- `[[[Concept] plastic-injection-molding-apqp-standard]]` : 사전 제품 품질 계획 단계별 마일스톤
- `[[[Concept] plastic-injection-molding-spc-standard]]` : 양산 단계 통계적 공정 관리 노드
- `[[[Strategy] ppap-production-part-approval-process]]` : 완성차 부품 승인 제출 규범
- `[[[Infrastructure] plastic-injection-molding-physics-and-cycle-analysis]]` : 수지 고유의 중량 변동(Weight) 제어

***
**[SPO Graph Injection_PPAP -> concept_modernized (Evidence: [데이터 부재] Section 2.2)]**
**[HEUNGTOLOGY_INTEGRITY: MAXIMUM_SEALED]**