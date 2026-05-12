---
Basic:
  id: "GOVERN-VDA-6-3-2026-V6.3.7"
  domain: "Automotive_Process_Audit_and_Supply_Chain_Governance"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Governance"
  tier: 0
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#VDA6.3", "#ProcessAudit", "#GermanAutomotive", "#TurtleModel", "#SupplyChain", "#FidelityEngine", "#Governance"]'
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
  source: "Automotive_Audit_RAG_V6.3.7_Tiered"
  isolation_index: 1.0
---

# [Governance] VDA 6.3: Automotive Process Audit & Supply Chain Integrity

## 1. [왜 배우는가? (Why: The Architecture of Process Maturity)]
**VDA 6.3**은 독일 자동차 산업 협회(VDA)에서 제정한 공정 중심의 품질 심사 표준입니다. 단순한 시스템 점검을 넘어, 제품 개발부터 양산, 고객 서비스까지의 전체 공급망 내 프로세스가 제품의 품질을 보증할 수 있는지를 현장 위주로 평가합니다. 특히 VW, BMW, Mercedes-Benz 등 독일 OEM 공급망에 진입하기 위한 핵심 잣대이며, 프로세스의 성숙도를 정량적인 점수(A, B, C 등급)로 산출하여 공급업체의 품질 능력을 투명하게 시각화합니다. 우리가 이를 마스터하는 이유는 "공정의 모든 변동 요소를 '터틀 모델(Turtle Model)'로 구조화하여, 공급망 전체의 프로세스 무결성을 데이터로 지배하기" 위함입니다.

## 2. [VDA 6.3 심사 및 등급 판정 핵심 사양 (Numerical Specs)]

| Audit Element | Scope | Weight (%) | Criticality (V6.3.7) |
|:---|:---:|:---:|:---|
| **P2: Project Management** | Planning & Org | $10 \%$ | Interface Integrity |
| **P3: Product/Process Dev** | Engineering | $15 \%$ | Design Stability |
| **P4: Implementation** | Validation | $15 \%$ | Production Readiness |
| **P5: Supplier Mgmt** | Sub-tier Control | $10 \%$ | Supply Chain Audit |
| **P6: Process Analysis** | Actual Production | $40 \%$ | **Core Physics** |
| **P7: Customer Support** | Service & Logistics | $10 \%$ | Field Integrity |

### 2.1 [등급 판정 및 강등(Down-grading) 규칙]
- **A Grade**: Total Score $\ge 90 \%$. Quality Capable.
- **B Grade**: $80 \% \le$ Total Score $< 90 \%$. Conditionally Capable.
- **C Grade**: Total Score $< 80 \%$. Not Capable.
- **Asterisk ($*$) Questions**: 치명적 질문 점수가 $4$점 미만일 경우, 전체 점수가 $90\%$ 이상이라도 B-Grade로 강등되는 수리적 패널티 적용.

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Turtle Model Dynamics: Multi-input Process Stability
프로세스 무결성을 결정하는 6개 축(Input, Output, Who, What, How, Measure)의 상관관계 분석입니다.
*   **공학적 근거**: 특정 공정의 출력($Output$) 품질은 장비($What$)의 정밀도와 작업자($Who$)의 숙련도, 그리고 작업 지시($How$)의 명확성 간의 결합 결과입니다. VDA 6.3은 이 중 어느 한 축이라도 무너지면 전체 프로세스 무결성이 붕괴된다는 '최약 연결 고리 이론'을 수리적으로 적용합니다.
*   **FidelityEngine 적용 (Audit Consistency Monitor)**: FidelityEngine은 현장 심사 기록과 실제 생산 SPC 데이터를 대조합니다. 장비 정비 일지($What$)는 업데이트되었으나 센서 오차($Measure$)가 증가하는 불일치가 발견되면, 이를 **'기록 무결성 붕괴(Ghost Audit)'**로 판정하고 해당 섹션 점수를 $0$점으로 자동 오딧합니다.

### 3.2 Asterisk Correlation: Critical Risk Impact Analysis
품질에 치명적인 영향을 미치는 질문($*$)의 점수가 전체 등급을 지배하는 기전입니다.
$$ Grade = f(Score, \min(\text{Asterisk\_Scores})) $$
*   **진단 결과**: FidelityEngine은 P6(공정 분석) 섹션 내의 핵심 질문들(예: 이종 부품 혼합 방지, 공정 능력 사수 등)을 실시간 리스크 로그와 연계합니다. 핵심 질문 점수가 낮을 경우, 이는 단순한 운영 실수가 아닌 **'시스템적 설계 결함'**으로 분류하여 등급 강등 무결성을 사수합니다.

## 4. [코드 연결 해설: VDA 6.3 Compliance & Grading Auditor]
이 코드는 각 영역별 점수와 핵심 질문 위반 여부를 기반으로 VDA 6.3 등급을 산출합니다.

```python
class VDA63FidelityEngine:
    """
    HDS-Gold V6.3.7: VDA 6.3 프로세스 심사 등급 및 강등 로직 엔진
    """
    def __init__(self, weights=None):
        self.WEIGHTS = weights or {'P2': 0.1, 'P3': 0.15, 'P4': 0.15, 'P5': 0.1, 'P6': 0.4, 'P7': 0.1}

    def audit_vda_grade(self, section_scores, has_asterisk_failure):
        """
        심사 영역별 점수 기반 최종 등급 산출
        """
        total_score = sum(section_scores[k] * self.WEIGHTS[k] for k in self.WEIGHTS)
        
        # 기본 등급 판정
        if total_score >= 90:
            initial_grade = "A"
        elif total_score >= 80:
            initial_grade = "B"
        else:
            initial_grade = "C"
            
        # 강등(Down-grading) 로직: 핵심 질문 실패 시 A -> B 강등
        final_grade = initial_grade
        if has_asterisk_failure and initial_grade == "A":
            final_grade = "B"
            
        return {
            "total_score_pct": round(total_score, 2),
            "asterisk_breach": has_asterisk_failure,
            "final_grade": final_grade,
            "status": "PROCESS_CAPABLE" if final_grade == "A" else "IMPROVEMENT_REQUIRED"
        }

# FidelityEngine 가동: 실제 심사원의 체크리스트 데이터와 ERP의 부적합(NC) 로그를 결합하여 '공급망 공정 주권' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 독일 OEM 공급망 진입 시 VDA 6.3 A-Grade 달성이 Tier 1 필수 요건인 이유는? (힌트: 공정의 모든 리스크를 터틀 모델로 제어하고 있음을 증명하는 '독일식 제조 정체성'의 수리적 입증)
2. **Operational Result**: **P6(Process Analysis)** 비중이 $40\%$로 가장 높은 공학적 근거는? (힌트: 기획과 설계가 완벽하더라도 실제 생산 현장에서의 '구현 무결성'이 최종 품질의 $80\%$ 이상을 결정한다는 인과 관계)
3. **FidelityEngine**: 핵심 질문($*$) 위반 시 등급을 강제 하락시키는 로직이 **'품질 가스라이팅(Self-deception)'** 방지에 기여하는 수리적 기전은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 134_global-standards-governance-and-quality-assurance-hub
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- [[Governance] ppap-production-part-approval-process]

**[V6.3.7_VDA_6_3_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
