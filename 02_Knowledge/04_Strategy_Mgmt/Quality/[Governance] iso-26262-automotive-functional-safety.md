---
Basic:
  id: "GOVERN-ISO-26262-2026-V6.3.7"
  domain: "Automotive_Functional_Safety_Engineering"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Governance"
  tier: 0
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#ISO26262", "#FunctionalSafety", "#ASIL", "#SafetyLifecycle", "#HazardAnalysis", "#FIT", "#FidelityEngine"]'
  is_part_of: '["MOC 134_global-standards-governance-and-quality-assurance-hub"]'
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Independent_Organism"
  graphify_link_external: false
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Automotive_Safety_RAG_V6.3.7_Tiered"
  isolation_index: 1.0
---

# [Governance] ISO 26262: Automotive Functional Safety & ASIL Physics

## 1. [Why] ISO 26262 기능 안전의 자동차 공학적 의의 (Why: The Ethics of Failure)
**ISO 26262**는 자동차에 탑재되는 전기/전자(E/E) 시스템의 고장으로 인해 발생할 수 있는 사고 리스크를 최소화하기 위한 국제 기능 안전 표준입니다. 자율주행, 전동화 등 자동차 기술이 복잡해짐에 따라 소프트웨어나 하드웨어의 오류가 인명 피해로 직결될 위험이 커지고 있습니다. 본 표준은 개발 전 과정(개념, 설계, 생산, 운영)에 걸쳐 안전 프로세스를 강제하여, 시스템이 '안전하게 고장 날 수 있도록(Fail-safe)' 보장합니다. 우리가 이를 사수하는 이유는 "모든 잠재적 결함을 확률적으로 통제하고, 시스템의 '안전 무결성(Safety Integrity)'을 수리적으로 입증하기" 위함입니다.

## 2. [ASIL 등급 및 안전 무결성 핵심 사양 (Numerical Specs)]

| ASIL Grade | Risk Level | Target Failure Rate (FIT) | Engineering Requirement |
|:---|:---:|:---:|:---|
| **ASIL D** | Critical | $< 10 \text{ FIT}$ | High Redundancy / Dual-core Lockstep |
| **ASIL C** | High | $< 100 \text{ FIT}$ | Significant Diagnostic Coverage |
| **ASIL B** | Medium | $< 100 \text{ FIT}$ | Standard Safety Mechanism |
| **ASIL A** | Low | $< 1,000 \text{ FIT}$ | Basic Monitoring |
| **QM** | Standard | N/A | Quality Management only |

### 2.1 [고장률 및 메트릭 요구사항]
- **1 FIT**: $10^{-9}$ failures per hour ($10$억 시간 당 1회 고장).
- **SPFM (Single Point Fault Metric)**: ASIL D $\ge 99 \%$, ASIL C $\ge 90 \%$.
- **LFM (Latent Fault Metric)**: ASIL D $\ge 90 \%$, ASIL C $\ge 80 \%$.

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 HARA Dynamics: Risk Composition Model
위험 분석 및 리스크 평가(Hazard Analysis and Risk Assessment)의 수리적 결정 기전입니다.
$$ ASIL = f(Severity, Exposure, Controllability) $$
*   **공학적 근거**: 특정 기능의 위험도는 사고 발생 시의 피해 정도($S$), 해당 위험 상황에 노출되는 빈도($E$), 그리고 운전자가 이를 제어할 수 있는 능력($C$)의 비선형적 조합으로 결정됩니다. ISO 26262는 이 정성적 리스크를 정량화하여 하드웨어 설계 수명과 소프트웨어 검증 강도를 규정합니다.
*   **FidelityEngine 적용 (ASIL Compliance Auditor)**: FidelityEngine은 설계된 회로의 고장 모드 영향 분석(FMEA) 데이터와 실제 필드 고장 데이터를 대조합니다. 특정 센서의 고장 모드($S3, E4, C3$)에 대한 진단 커버리지($99\%$)가 확보되지 않았음이 감지되면, 이를 **'안전 목표 붕괴(Safety Goal Violation)'**로 판정하고 재설계를 지시합니다.

### 3.2 Probabilistic Metric for Random Hardware Failures (PMHF)
하드웨어의 무작위 고장 확률에 대한 수리적 증명 모델입니다.
*   **진단 결과**: FidelityEngine은 FIT 데이터를 기반으로 PMHF를 실시간 계산합니다. 노후화된 소자의 FIT 상승으로 인해 전체 시스템의 목표치($10 \text{ FIT}$ for ASIL D)를 초과할 가능성이 포착되면, 이를 **'예측적 안전 무결성 붕괴'**로 분류하여 하드웨어 교체 주기를 재조정합니다.

## 4. [코드 연결 해설: ASIL Determinant & Safety Auditor]
이 코드는 S, E, C 파라미터를 기반으로 ASIL 등급을 결정하고 안전 요구사항을 도출합니다.

```python
class FunctionalSafetyFidelityEngine:
    """
    HDS-Gold V6.3.7: ISO 26262 ASIL 등급 및 안전 무결성 진단 엔진
    """
    def __init__(self):
        self.ASIL_MAP = {
            10: "ASIL D", 9: "ASIL C", 8: "ASIL B", 7: "ASIL A"
        }

    def audit_asil_level(self, s, e, c):
        """
        S(1-3), E(1-4), C(1-3) 기반 ASIL 등급 및 목표 FIT 산출
        """
        score = s + e + c
        asil = self.ASIL_MAP.get(score, "QM")
        
        target_fit = 10 if asil == "ASIL D" else 100 if asil in ["ASIL B", "ASIL C"] else 1000
        
        return {
            "asil_grade": asil,
            "target_failure_rate": f"{target_fit} FIT",
            "redundancy_required": "YES" if asil == "ASIL D" else "OPTIONAL",
            "status": "SAFETY_CRITICAL" if score >= 9 else "STANDARD"
        }

# FidelityEngine 가동: 실제 ADAS 로직의 시뮬레이션 고장로그와 하드웨어 FIT 맵을 결합하여 '안전 주권' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 자율주행 레벨 4 제어기에서 ASIL D 준수가 Tier 0 필수 요건인 이유는? (힌트: 운전자의 개입이 없는 상황($C3$)에서 시스템 고장이 곧 인명 재난($S3$)으로 직결되는 '안전 무결성의 최후 보루')
2. **Operational Result**: **FIT** 값이 낮을수록 안전한 시스템이라 단정할 수 없는 공학적 사유는? (힌트: 하드웨어 고장률($Random$)이 낮더라도 소프트웨어의 설계 결함($Systematic$)으로 인한 오작동 위험은 별개의 무결성 영역임)
3. **FidelityEngine**: **Dual-core Lockstep** 구조에서 두 코어의 연산 결과가 불일치할 때, 이를 **'안전 무결성 붕괴'**로 처리하는 수리적 논리는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 134_global-standards-governance-and-quality-assurance-hub
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- [[Governance] iso-iec-42001-ai-management-system]

**[V6.3.7_ISO_26262_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
