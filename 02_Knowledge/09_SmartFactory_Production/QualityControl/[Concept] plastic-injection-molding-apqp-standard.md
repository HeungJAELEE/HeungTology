---
metadata:
  date: "2026-05-17"
  id: "[[[Concept] plastic-injection-molding-apqp-standard]]"
  project: "May_2026_Injection_Molding_Quality_Standardization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "09_SmartFactory_Production"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "AIAG APQP Manual 2nd Edition & Moldflow Engineering Guide"
  original_author: "Automotive Quality Action Group (AIAG) & Antigravity Vault"
  original_hash: "85e91507fa9723c9f5fddec1e3784c3263b82367ca811fb920b81709f5656e37"
object:
  object_type: "Concept"
  tier: 1
  description: '플라스틱 사출 성형 부품 및 금형의 초기 설계부터 시사출(Trial) 최적화에 이르기까지 품질 리스크를 단계별 품질 게이트를 통해 원천 소거하는 사전 제품 품질 계획 표준 지능'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]"
  alternative_parents: []
spo_graph:
  - subject: "plastic-injection-molding-apqp-standard"
    predicate: "implements"
    object: "automotive-quality-planning-process"
    evidence_coordinate: "[Ref: AIAG APQP Manual] Chapter 1"
    evidence_hash: "85e91507fa97"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
  - subject: "plastic-injection-molding-apqp-standard"
    predicate: "requires_validation"
    object: "Ppk > 1.67"
    evidence_coordinate: "[Ref: AIAG PPAP Manual] Section 2.2.9"
    evidence_hash: "85e91507fa97"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Concept] plastic-injection-molding-apqp-standard

## 1. [왜 배우는가? (Why: Engineering the Future Quality)]
**APQP (Advanced Product Quality Planning: 사전 제품 품질 계획)**는 자동차 부품 설계 초기 단계에서부터 양산 인도에 이르기까지 발생할 수 있는 모든 품질 리스크를 개발 단계에서 선제적으로 제어하기 위한 '제조 지식의 통합 아키텍처'입니다. 플라스틱 사출 성형 공정의 경우, 금형(Mold Tooling)이 일단 설계되고 강철 블록이 가공(Milling/EDM)된 후에는 설계를 변경하거나 가공오차를 수정하기 위해 막대한 물리적 재작업 비용과 시간 지연이 발생합니다. 이는 프로젝트 전체의 수익성을 저해하는 치명적인 리스크 요소입니다.

따라서 금형 발주 전 가상 공간에서 **Moldflow** 유한요소해석(FEA) 시뮬레이션을 통해 수지의 흐름 변동을 수리적으로 완벽히 소거하고, 시사출(T0 ~ T3 Trials) 단계별 게이트 패스(Gate Pass) 적합성을 실증적으로 검증해야 합니다. 이 표준을 따르는 이유는 개발 주기를 단축하여 개발 주권을 수호하고, 양산 첫 시점부터 단 하나의 결함도 발생시키지 않는 **'실패 없는 양산(First Time Right)'**의 구조적 무결성을 결정론적으로 확보하기 위함입니다.

---

## 2. [사출 APQP 단계별 핵심 기술 사양 (Numerical Specs)]

사출 성형 사전 품질 계획의 성공을 보증하기 위한 단계별 기술 사양 및 검증 임계치입니다.

| APQP Phase | Core Milestone | Primary Technical Target | Engineering Rationale |
| :--- | :--- | :--- | :--- |
| **Phase 1: Planning** | Concept Freeze | Resin Selection & PVT Data | 고분자 수지의 압력-부피-온도(PVT) 특성에 기반한 타겟 수축률 확립 |
| **Phase 2: Design** | DFM / Moldflow | Gate Balance $> 95.0 \%$ | 유로 저항을 균등 제어하여 캐비티 충진 압력 및 시간 불균형 소거 |
| **Phase 3: Process** | Tooling Build | Cavity Finish $R_a < 0.1 \mu\text{m}$ | 금형 표면 조도 확보를 통해 이형 응력 극소화 및 가스 트랩 방지 |
| **Phase 4: Validation** | T0 ~ T3 Trials | Initial Capability $P_{pk} > 1.67$ | 양산 가동성 실증 및 300샘플 기반 단기 통계적 안정성 입증 |
| **Phase 5: Feedback** | Mass SOP | Cycle Time Dev. $\pm 0.1 \text{ s}$ | 양산 단계 열평형 유지 여부 감사 및 Lessons Learned 피드백 |

---

## 3. [시사출(Trial) 최적화 및 게이트 패스 기전 (Mechanism)]

### 3.1 [단계별 시사출(Trial) 최적화 프로토콜]
사출 금형 제작 완료 후, 설계 무결성을 점진적으로 확보하기 위해 4단계의 시사출 검증 주기를 가동합니다.
*   **T0 (Functional Test Gate)**: 제품 추출이 정상적으로 수행되는지, 이젝터(Ejector)의 핀 압력 밸런스가 균일한지, 금형 내 코어 냉각 회로의 압력 강하 및 유량이 사양에 부합하는지 육안 및 기계적 작동성을 확인합니다.
*   **T1 (Dimensional Target Gate)**: 성형 부품의 3D 스캔 정합성(Alignment)을 분석하고, 수축률 편차로 인한 싱크 마크(Sink Mark) 및 뒤틀림(Warpage) 거동을 분석합니다. 이를 통해 금형 캐비티 코어의 미세 보정치(Design Optimization)를 도출합니다.
*   **T2 (Process Windows Gate)**: 사출 속도($Q$) 및 보압 프로파일의 안정 범위를 설정하는 공정 윈도우(DOE: Design of Experiments) 테스트를 수행합니다. 2시간 연속 사출을 통해 온도 및 사이클 타임 안정성을 검증합니다.
*   **T3 (PSW Gate)**: 양산 조건과 동일한 툴링 및 자동화 설비를 통해 연속 300개의 마스터 샘플을 취출하고, 치수 측정 데이터 세트를 PPAP 부품 제출 승인서(PSW)에 바인딩합니다.

### 3.2 [사출 게이트(Quality Gate) 패스 논리]
각 APQP 단계의 게이트 패스를 통과하기 위해, 이전 단계의 미결 리스크(Open Issue)가 다음 단계로 누출(Leakage)되는 것을 차단합니다. 
예를 들어, Phase 2(설계) 단계에서 Moldflow 해석 결과 웰드 라인의 발생 온도가 수지 융점($T_m$) 이하로 하락하여 접합 강도가 구조 설계치보다 낮아질 위험이 포착되면, 게이트 차단 인터락(Quality Gate Interlock)이 작동하여 금형 코어 가공 발주(PO)가 차단되고 게이트 구조 재설계 루프가 강제됩니다.

---

## 4. [코드 연결 해설: InjectionAPQPAuditor (양산 준비성 진단 엔진)]

아래 클래스는 APQP 각 단계별 필수 엔지니어링 산출물의 이행 상태를 평가하여 양산 진입 리스크 지수를 산출하는 FidelityEngine입니다.

```python
class InjectionAPQPAuditor:
    """
    플라스틱 사출 성형 사전 품질 계획(APQP) 마일스톤 이행 및 양산 준비 적합성 감사 엔진
    """
    def __init__(self, current_phase=4):
        self.CURRENT_PHASE = current_phase
        self.PHASE_CHECKLIST = {
            1: ["Resin_PVT_Selected", "Target_Dimensions_Defined"],
            2: ["Moldflow_Gate_Balanced", "DFM_SignOff"],
            3: ["Cavity_Surface_Polished", "Measurement_Jig_Ready"],
            4: ["Initial_Ppk_1.67_Proven", "PSW_Signed_Off"],
            5: ["Cycle_Time_Stability_Verified", "Lessons_Learned_Updated"]
        }

    def audit_milestone_readiness(self, completed_milestones):
        """
        Transitional Bridge: 사전 계획의 빈틈은 양산 현장의 누수로 직결됩니다. 
        이 감사 엔진은 사출 APQP 단계별 필수 산출물 중 누락된 리스크 인자를 탐지하고, 
        양산 진입 지연 및 품질 편차 발생 위험 지수를 정량적으로 진단합니다.
        """
        required_items = self.PHASE_CHECKLIST.get(self.CURRENT_PHASE, [])
        missing_items = [item for item in required_items if item not in completed_milestones]
        
        # 리스크 지수 산출 (누락 항목 하나당 25% 가중 위험도 가산)
        risk_index = len(missing_items) * 0.25
        
        status = "APQP_GATE_PASS_STABLE"
        recommendation = "PROCEED_TO_NEXT_PHASE"
        
        if risk_index > 0.0:
            status = "RISK_LEAKAGE_DETECTED"
            recommendation = f"HALT_GATE: Complete missing artifacts: {missing_items}"
        elif self.CURRENT_PHASE == 4:
            status = "READY_FOR_SOP_MASS_PRODUCTION"
            recommendation = "GENERATE_PSW_AND_SUBMIT_PPAP"
            
        return {
            "monitored_phase": self.CURRENT_PHASE,
            "completed_milestone_count": len(required_items) - len(missing_items),
            "missing_artifacts": missing_items,
            "calculated_leakage_risk_index": round(risk_index, 4),
            "gate_status": status,
            "architect_recommendation": recommendation
        }
```

---

## 5. [스스로 체크 (Self-Audit)]
1. Phase 2(설계)에서 **Gate Balance**가 $95.0\%$ 미만으로 떨어졌을 때, 수지의 유동 충진 속도 차이가 다수 캐비티 간의 **Ppk 편차**로 전이되는 수리적 열역학 인과관계는 무엇인가?
2. 시사출 단계에서 **T1(Dimensional Trial)**과 **T2(Process Windows)**를 명확히 분리하여 공정 윈도우를 잡지 않고 바로 **T3(PSW 샘플링)**을 감행할 때, 초기 공정 능력 지수($P_{pk}$)에 미치는 영향은 무엇인가?
3. APQP 게이트 패스 감사에서 **FidelityEngine**이 `RISK_LEAKAGE_DETECTED` 판정을 내렸음에도 불구하고 금형 발주 또는 양산 가동을 강행할 경우, 잠재적인 **FMEA RPN** 지수와 향후 제조 원가(LCC)에 미치는 장기 변동성은 어떻게 나타나는가?

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[Concept] plastic-injection-molding-iatf-16949-qms]]` : 최상위 IATF 16949 거버넌스 시스템
- `[[[Infrastructure] precision-mold-design-and-insert-molding-technology]]` : 금형 설계 및 제작 표준
- `[[[Infrastructure] molding-process-optimization-and-defect-prevention-ai]]` : Moldflow 기반 시뮬레이션 지능
- `[[ppap-production-part-approval-process]]` (외부자료) : 부품 승인 마일스톤 요구사항
- `[[plastic-injection-molding-physics-and-cycle-analysis]]` (외부자료) : 사출 공정 물리적 한계점

---
**[SPO_Graph: Injection_APQP -> concept_modernized (Evidence: [Ref: AIAG APQP Manual] Chapter 2)]**
**[HEUNGTOLOGY_INTEGRITY: MAXIMUM_SEALED]**
