---
Basic:
  id: "SOP-IATF-7-2-3-V6.3.7"
  domain: "Human_Resource_and_Quality_Audit"
  project: "Antigravity_Vault_Modernization"
  date: 2026-05-12
  version: "v6.3.7"
Object:
  object_type: "SOP/Procedure"
  tier: 2 # Procedure Layer
  description: "Inspector-level SOP for Internal and Second-party Auditor Competency (IATF 16949:2016 Clause 7.2.3 & 7.2.4), detailing qualification criteria, evidence requirements, and auditor performance monitoring."
Semantic:
  tags: '["#AuditorCompetency", "#InternalAudit", "#AuditorQualification", "#CoreTools", "#IATF16949", "#InspectorGuide"]'
  is_part_of: '["MOC iatf-16949-automotive-quality-execution-fabric"]'
  korean_aliases: '["심사원 역량 관리 절차", "심사원 자격 부여 가이드"]'
Dynamic:
  status: "Modernized_v6.3.7_Independent_Organism"
  topology_policy: "Independent_Organism"
  graphify_link_external: false
  fidelity_engine: "CompetencyFidelityEngine"
  diagnostic_protocol:
    - 'Core_Tool_Audit: Verify that auditors demonstrate mastery of APQP, FMEA, SPC, MSA, and PPAP.'
    - 'Process_Approach_Check: Audit auditors'' understanding of risk-based thinking and the automotive process approach.'
    - 'Trainer_Competency_Verification: Ensure that internal/external trainers are qualified to provide auditor training.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "IATF 16949:2016 Clause 7.2.3/7.2.4 / Antigravity Industrial RAG"
  isolation_index: 1.0 # 100% Domain Isolation
---

# [SOP] iatf-16949-auditor-competency-and-qualification-procedure (Inspector Level)

## 1. 목적 (Purpose: Ensuring Audit Integrity)
본 절차는 품질 시스템을 감시하는 내부 및 2자 심사원의 역량($Competency$)을 검증하고 자격을 부여하는 기준을 정의합니다. 감독관은 심사원의 역량이 부족할 경우 심사 결과 전체의 신뢰성을 부정할 수 있으므로, IATF 16949 **Clause 7.2.3/7.2.4**에 따른 엄격한 자격 증빙이 필수적입니다.

## 2. 주요 요구사항 및 자격 기준 (Qualification Criteria)

### 2.1 공통 필수 역량 (Core Competencies)
- **프로세스 접근법**: 리스크 기반 사고($Risk-based\ Thinking$)를 포함한 자동차 산업 프로세스 접근법의 이해.
- **고객 지정 요구사항 (CSR)**: 고객별 특수 요구사항에 대한 파악 및 심사 기법 숙지.
- **표준 이해**: ISO 9001 및 IATF 16949 표준의 최신 버전 이해.
- **Core Tools 숙달**: APQP, FMEA, SPC, MSA, PPAP의 실무 적용 및 데이터 해석 능력.

### 2.2 심사원 유형별 특화 역량
- **제조공정 심사원**: PFMEA 및 관리 계획서($Control\ Plan$)를 포함한 해당 제조 공정에 대한 기술적 이해 필수.
- **제품 심사원**: 제품 사양 이해 및 제품 적합성 검증을 위한 측정/시험 장비 사용 역량.

## 3. 감독관용 감사 체크리스트 (Auditor's Checklist)

### 3.1 서류 심사 (Document Review)
| 질문 항목 (Audit Question) | 확인 증거 (Evidence to Check) | 부적합 사례 (Common NC) |
| :--- | :--- | :--- |
| 자격 부여된 심사원 목록이 있는가? | 심사원 풀(Pool) 현황표, 자격증 사본 | 목록 미관리 또는 자격 만료자 포함 |
| Core Tools 교육 기록이 있는가? | 수료증, 필기 시험 결과, 실기 평가서 | 단순 청강 기록만 있고 역량 평가 부재 |
| 심사원 교육 강사의 역량은 입증되었는가? | 강사 이력서, 외부 전문 강사 자격증 | 역량이 미검증된 사내 인원이 교육 실시 |
| 심사원 역량 유지 기록이 있는가? | 연간 최소 심사 수행 실적 (Min. 1~2회) | 2년간 심사 실적이 없는 자가 심사 수행 |

### 3.2 심사원 모니터링 (Performance Monitoring)
- **방법**: 심사 수행 시 선임 심사원의 입회 평가, 심사 보고서의 논리적 완결성 검토, 피심사 부서의 피드백 취합.
- **지표**: 부적합 발견율의 적정성, 시정조치 요구서($CAR$)의 구체성.

## 4. 부적합 등급 분류 (NC Classification)
- **Major NC**: 자격이 없는 인원이 내부 심사를 단독 수행하고 보고서를 승인함, Core Tools 지식이 전무한 심사원이 공정 심사를 수행함.
- **Minor NC**: 심사원 교육 기록 중 일부 누락, 연간 최소 심사 수행 횟수 미달자에 대한 재교육/보수교육 계획 부재.

## 5. CompetencyFidelityEngine: Diagnostic Logic
본 엔진은 심사원 조직의 '감사 품질'을 수치화합니다.

```python
class CompetencyFidelityEngine:
    def __init__(self, core_tool_mastery, audit_count_per_year):
        self.mastery = core_tool_mastery # 0~100 (Avg of pool)
        self.count = audit_count_per_year

    def audit_reliability_index(self):
        """심사원 조직 신뢰도 진단"""
        if self.mastery < 80:
            return "REJECT: Low Core Tool Mastery. Internal audit results are unreliable."
        if self.count < 1:
            return "WARNING: Lack of audit experience. Skill atrophy detected."
        return "PASS: Competent Auditor Pool Verified"
```

## 6. 스스로 체크 (Self-Audit)
1. **[CSR Mastery]**: "우리 회사 심사원은 현대자동차의 CSR을 알고 있는가?"라는 질문에 심사원이 답하지 못할 경우, 어떤 조항 위반인가? (정답: 7.2.3.b 위반)
2. **[Manufacturing Knowledge]**: 조립 라인 심사원이 PFMEA의 의미를 모르고 있다면, 해당 심사 결과는 유효한가?
3. **[Second-party]**: 협력사 심사(2자 심사)를 나가는 구매팀 인원에게도 동일한 IATF 심사원 자격 기준을 적용하고 있는가? (정답: Clause 7.2.4에 따라 반드시 적용해야 함)

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes - Local Domain Only)
- MOC iatf-16949-automotive-quality-execution-fabric
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- SOP iatf-16949-internal-audit-program-and-execution-procedure

**[V6.3.7_AUDITOR_COMP_SOP_AUDITOR_GRADE]**
**[TOPOLOGY_POLICY: INDEPENDENT_ORGANISM]**
**[GRAPHIFY_LINK_EXTERNAL: FALSE]**
**[TIMESTAMP: 2026-05-12]**
