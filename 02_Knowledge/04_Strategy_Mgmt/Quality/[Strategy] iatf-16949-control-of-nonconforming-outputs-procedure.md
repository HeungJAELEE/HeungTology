---
metadata:
  id: "[[[Strategy] iatf-16949-control-of-nonconforming-outputs-procedure]]"
  domain: "04_Strategy_Mgmt"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Strategy] iatf-16949-control-of-nonconforming-outputs-procedure에 관한 고밀도 지능 노드"
semantic:
  tags: ["#04_Strategy_Mgmt", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Strategy] iatf-16949-control-of-nonconforming-outputs-procedure

## 1. 목적 (Purpose: Ensuring Zero-Escape)
부적합한 산출물($Nonconforming\ Outputs$)이 의도하지 않게 사용되거나 고객에게 인도되는 것을 방지하는 것을 목적으로 합니다. 감독관은 부적합품의 **'물리적 격리'**와 **'재작업의 적법성'**을 현장에서 직접 확인하므로, 실무적 감사 대응 체계를 구축합니다.

## 2. 주요 요구사항 및 절차 (Standard Procedures)

### 2.1 식별 및 봉쇄 (Identification & Containment)
- **의심 제품 (Suspect Product)**: 식별이 누락되었거나 상태가 불분명한 모든 제품은 부적합품으로 간주함.
- **격리**: 잠금 장치가 있는 격리 구역($Locked\ Segregation\ Area$) 보관 원칙.

### 2.2 재작업 및 수리 (Rework/Repair)
- **리스크 분석**: 재작업 결정 전 부작용에 대한 PFMEA 검토 필수.
- **재검사**: 재작업 후 관리 계획서에 따른 100% 재검사 및 합격 판정.
- **수리($Repair$)**: 제품 사양 변경을 수반하므로 고객 사전 승인 필수.

## 3. 감독관용 감사 체크리스트 (Auditor's Checklist)

### 3.1 서류 심사 (Document Review)
| 질문 항목 (Audit Question) | 확인 증거 (Evidence to Check) | 부적합 사례 (Common NC) |
| :--- | :--- | :--- |
| 특채(Concession) 제품에 고객 승인이 있는가? | 고객 승인서(Waiver), 승인 수량 관리 대장 | 고객 구두 승인만으로 납품 |
| 재작업 지침서가 있는가? | 재작업 전용 표준($SOP$), 리스크 분석서 | 일반 작업자가 임의의 방법으로 재작업 |
| 수리($Repair$) 전 고객 승인을 득했는가? | 고객 승인 기록, 기술 검토 보고서 | 수리 후 일반 제품과 섞어 납품 |
| 부적합 폐기 시 파기 증빙이 있는가? | 폐기 사진, 폐기 업체 확인서 | 폐기 대상이 외부로 유출되거나 재사용됨 |

### 3.2 현장 실사 (Shop Floor Observation)
- **Point 1 (Red Tag)**: 현장에 방치된 부적합품에 '부적합 라벨'이 명확히 부착되어 있는가?
- **Point 2 (Locked Area)**: 격리 구역이 실제로 잠겨 있는가? (열쇠 관리자 확인)
- **Point 3 (Suspect Logic)**: 작업자 인터뷰 - "바닥에 떨어진 제품을 발견하면 어떻게 처리하는가?" (정답: 즉시 부적합 용기로 투입)

## 4. 부적합 등급 분류 (NC Classification)
- **Major NC**: 부적합품이 정상 제품과 섞여서 포장됨, 고객 승인 없이 수리 제품 납품, 격리 구역 관리 부재.
- **Minor NC**: 부적합 라벨의 일부 기재 누락, 격리 구역의 청소 상태 불량.

## 5. NonconformanceFidelityEngine: Diagnostic Logic
본 엔진은 부적합 처리의 '법적/기술적 완결성'을 진단합니다.

```python
class NonconformanceFidelityEngine:
    def __init__(self, disposition, customer_approved, reinspected, isolation="Independent"):
        self.disposition = disposition
        self.approved = customer_approved
        self.reinspected = reinspected
        self.isolation = isolation

    def audit_disposition_legality(self):
        """부적합 처리 적법성 및 격리 진단"""
        if self.isolation != "Independent":
            return "SECURITY_ALERT: Domain isolation compromised. Prune external links."
        if self.disposition in ["Repair", "Concession"] and not self.approved:
            return "CRITICAL: Customer approval missing for Repair/Concession."
        if self.disposition == "Rework" and not self.reinspected:
            return "REJECT: Reworked product must be re-inspected."
        return "PASS: Independent Nonconformance Intelligence Operational"
```

## 6. 스스로 체크 (Self-Audit)
1. **[Containment]**: 부적합품 함이 꽉 차서 옆의 빈 박스에 제품을 넣어두었을 때, 감독관이 이를 발견한다면 어떤 조항 위반으로 지적하겠는가? (정답: 8.7.1.1 식별 및 격리 실패)
2. **[Rework Standard]**: "숙련된 작업자가 알아서 잘 고친다"는 소명이 감독관에게 통할 것인가?
3. **[Inventory]**: 전산상 재고와 격리 구역의 실물 부적합품 수량이 맞지 않을 때 발생하는 리스크는?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes - Local Domain Only)
- MOC iatf-16949-automotive-quality-execution-fabric
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- SOP iatf-16949-problem-solving-and-corrective-action-procedure

**[V6.3.7_NC_CONTROL_SOP_AUDITOR_GRADE]**
**[TOPOLOGY_POLICY: INDEPENDENT_ORGANISM]**
**[GRAPHIFY_LINK_EXTERNAL: FALSE]**
**[TIMESTAMP: 2026-05-12]**
