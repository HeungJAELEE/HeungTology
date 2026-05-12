---
Basic:
  id: "SOP-IATF-4-4-1-2-V6.3.7"
  domain: "Product_Safety_and_Liability"
  project: "Antigravity_Vault_Modernization"
  date: 2026-05-12
  version: "v6.3.7"
Object:
  object_type: "SOP/Procedure"
  tier: 2 # Procedure Layer
  description: "Inspector-level SOP for Product Safety Management (IATF 16949:2016 Clause 4.4.1.2), detailing audit checklists, evidence requirements, and common nonconformity scenarios for high-stakes certification audits."
Semantic:
  tags: '["#ProductSafety", "#AuditChecklist", "#InspectorGuide", "#SafetyCritical", "#IATF16949", "#ZeroDefect"]'
  is_part_of: '["MOC iatf-16949-automotive-quality-execution-fabric"]'
  korean_aliases: '["제품 안전 실사 대응 SOP", "감독관용 제품 안전 교본"]'
Dynamic:
  status: "Modernized_v6.3.7_Independent_Organism"
  topology_policy: "Independent_Organism"
  graphify_link_external: false
  fidelity_engine: "SafetyAuditorEngine"
  diagnostic_protocol:
    - 'Statutory_Scan: Verify that all relevant statutory and regulatory safety requirements are identified.'
    - 'FMEA_Safety_Audit: Ensure special approvals exist for design and process FMEAs of safety-related parts.'
    - 'Traceability_Audit: Audit lot-level traceability throughout the supply chain.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "IATF 16949:2016 Clause 4.4.1.2 / Antigravity Industrial RAG"
  isolation_index: 1.0 # 100% Domain Isolation
---

# [SOP] iatf-16949-product-safety-management-procedure (Inspector Level)

## 1. 목적 (Purpose: The Zero-Harm Mandate)
본 절차는 인명 피해나 법적 규제 위반으로 이어질 수 있는 제품 안전($Product\ Safety$) 관련 리스크를 설계부터 선적까지 전 과정에서 통제하는 것을 목적으로 합니다. IATF 16949 **Clause 4.4.1.2**의 13가지 필수 요구사항을 감독관의 시각에서 분석하여, 실사 시 지적될 수 있는 허점을 사전에 방어합니다.

## 2. 주요 요구사항 및 절차 (Standard Procedures)

### 2.1 법적 및 규제적 요구사항 파악 (Identification)
- **모니터링**: 제품이 판매되는 국가의 법규($Statutory$) 및 규제($Regulatory$) 요구사항을 주기적으로 파악하고 리스트업함.
- **고객 통지**: 파악된 법적 요구사항을 고객에게 공식적으로 알리고 제품 사양에 반영되었음을 확인받음.

### 2.2 설계 및 공정 리스크 통제 (Risk Control)
- **특별 승인 (Special Approvals)**: 제품 안전 관련 부품의 설계 FMEA($DFMEA$) 및 공정 FMEA($PFMEA$), 관리 계획서($Control\ Plan$)는 반드시 고객 또는 사내 안전 책임자의 특별 승인을 득해야 함.
- **특성 파악**: 도면 및 공정 지침서에 안전 관련 특성($Safety-related\ Characteristics$)을 명확히 식별(예: $[S]$, $\nabla$ 기호 사용).
- **대응 계획 (Reaction Plans)**: 안전 특성 검사에서 부적합 발생 시, 즉각적인 라인 정지 및 로트 봉쇄를 포함한 강화된 대응 계획 수립.

### 2.3 조직적 책임 및 교육 (Responsibility & Training)
- **에스컬레이션 (Escalation)**: 안전 이슈 발생 시 최고 경영진($Top\ Management$) 및 고객에게 즉시 보고되는 공식적인 단계적 확대 프로세스 정의.
- **전문 교육**: 제품 안전에 관여하는 모든 인원(설계, 생산, 검사)에 대해 정기적인 안전 의식 및 기술 교육 실시 및 기록 보유.

## 3. 감독관용 감사 체크리스트 (Auditor's Checklist)

### 3.1 서류 심사 (Document Review)
| 질문 항목 (Audit Question) | 확인 증거 (Evidence to Check) | 부적합 사례 (Common NC) |
| :--- | :--- | :--- |
| 안전 관련 법규 리스트가 최신인가? | 법규 등록부, 업데이트 이력 로그 | 폐기된 구형 법규 적용 중 |
| DFMEA/PFMEA에 고객 승인이 있는가? | 고객 서명 날인된 FMEA, 승인 공문 | 내부 승인만으로 양산 진행 |
| 안전 특성이 현장에 전파되었는가? | 작업 표준서($SOP$), 도면 식별 기호 | 현장 SOP에 안전 특성 미표기 |
| 에스컬레이션 프로세스가 작동하는가? | 비상 연락망, 모의 훈련 기록 | 담당자 부재 시 보고 체계 마비 |

### 3.2 현장 실사 (Shop Floor Observation)
- **Point 1**: 안전 부품 보관 구역의 식별 상태 (SUSPECT 제품과 혼입 리스크 확인).
- **Point 2**: 작업자 인터뷰 - "본인이 생산하는 제품의 안전 특성이 무엇이며, 불량 시 누구에게 즉시 보고해야 하는가?"
- **Point 3**: 추적성($Traceability$) 현장 검증 - 임의의 완제품 로트 번호를 지정하여 원소재 로트까지 1시간 이내 추적 가능한지 테스트.

## 4. 부적합 등급 분류 (NC Classification)
- **Major NC**: 안전 관련 특성에 대한 관리 계획서 미수립, 고객의 FMEA 특별 승인 없이 양산 공급, 법적 규제 요구사항 파악 누락.
- **Minor NC**: 안전 교육 기록 일부 누락, 에스컬레이션 연락망의 일부 정보(전화번호 등) 최신화 지연.

## 5. SafetyAuditorEngine: Diagnostic Logic
본 엔진은 실제 오딧 상황에서의 '방어력'을 측정합니다.

```python
class SafetyAuditorEngine:
    def __init__(self, documentation_score, field_interview_score):
        self.doc_score = documentation_score # 0~100
        self.field_score = field_interview_score # 0~100

    def calculate_audit_risk(self):
        """실사 수검 리스크 진단"""
        total = (self.doc_score * 0.6) + (self.field_score * 0.4)
        if total < 70:
            return "HIGH RISK: Major Nonconformity Expected. Immediate Action Required."
        if total < 85:
            return "MODERATE RISK: Minor NCs likely. Review field communication."
        return "OPTIMAL: Audit Ready (Zero Major NC target)."
```

## 6. 스스로 체크 (Self-Audit)
1. **[Concession]**: 고객이 안전 부품의 사소한 규격 이탈을 '그냥 써도 된다'고 구두로 말했을 때, 감독관에게 이를 어떻게 소명할 것인가? (정답: 반드시 문서화된 승인이 있어야 함)
2. **[Change]**: 설비의 센서를 교체했을 때, 이것이 '제품 안전'에 미치는 영향 평가를 수행했는가?
3. **[Supply Chain]**: 하위 협력사에서 안전 특성 관리가 누락되었을 때, 우리 회사가 받을 수 있는 지적 사항은? (정답: 4.4.1.2.k 공급망 요구사항 전파 실패)

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes - Local Domain Only)
- MOC iatf-16949-automotive-quality-execution-fabric
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- SOP iatf-16949-risk-analysis-and-preventive-action-procedure

**[V6.3.7_SAFETY_SOP_AUDITOR_GRADE]**
**[TOPOLOGY_POLICY: INDEPENDENT_ORGANISM]**
**[GRAPHIFY_LINK_EXTERNAL: FALSE]**
**[TIMESTAMP: 2026-05-12]**
