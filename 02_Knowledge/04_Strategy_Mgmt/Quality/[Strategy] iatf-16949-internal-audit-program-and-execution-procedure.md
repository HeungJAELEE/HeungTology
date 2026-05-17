---
metadata:
  date: "2026-05-16"
  id: "[[[Strategy] iatf-16949-internal-audit-program-and-execution-procedure]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "04_Strategy_Mgmt"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "2fc22e92dd99d547f2fd3e3b0deffc4fc084efb0a19755a9ab6e8b427aca913f"
object:
  object_type: "Concept"
  tier: 1
  description: '[Strategy] iatf-16949-internal-audit-program-and-execution-procedure에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 04_Strategy_Mgmt]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Strategy] iatf-16949-internal-audit-program-and-execution-procedure

## 1. 목적 (Purpose: The Self-Correcting Loop)
본 절차는 조직의 품질경영시스템(QMS)이 표준 및 고객 요구사항에 적합하게 운영되고 있는지를 주기적으로 검증하는 내부 심사 시스템을 정의합니다. 감독관은 내부 심사의 **'독립성'**과 **'범위의 완결성'**을 집중적으로 심사하므로, IATF 16949 **Clause 9.2.2**에 따른 철저한 증빙 체계 구축이 필수적입니다.

## 2. 주요 요구사항 및 절차 (Standard Procedures)

### 2.1 심사 프로그램 및 주기 (Audit Program)
- **3개년 주기 (3-Year Cycle)**: 모든 QMS 프로세스 및 제조 공정은 3개년 단위로 최소 1회 이상 전수 심사되어야 함.
- **리스크 기반 우선순위**: 내부/외부 품질 성과 지표(불량률, 고객 클레임), 공정 변경 이력, 이전 심사 부적합 결과를 고려하여 심사 빈도를 조정.
- **통합 심사**: 고객 지정 요구사항(CSR)을 심사 프로그램에 통합하여 샘플링 수행.

### 2.2 심사 유형별 실행 가이드
- **QMS 심사**: 시스템 전체의 유효성 및 리스크 기반 사고 적용 여부 검증.
- **제조공정 심사**: 고객 지정 접근법(예: VDA 6.3)을 사용하여 효과성 및 효율성 측정. 모든 교대조($All\ Shifts$) 및 인수인계 과정($Handover$)을 샘플링에 포함.
- **제품 심사**: 출하 전 완제품이 모든 사양을 만족하는지 검증 (고객 지정 빈도 준수).

## 3. 감독관용 감사 체크리스트 (Auditor's Checklist)

### 3.1 서류 심사 (Document Review)
| 질문 항목 (Audit Question) | 확인 증거 (Evidence to Check) | 부적합 사례 (Common NC) |
| :--- | :--- | :--- |
| 모든 프로세스가 3개년 내에 심사되었는가? | 3개년 심사 마스터 플랜, 실시 현황표 | 일부 비핵심 프로세스(인사, 교육 등) 누락 |
| 심사의 독립성이 보장되는가? | 심사원 배정표 (업무 관련성 대조) | 본인이 작성한 SOP를 본인이 심사함 |
| 야간 교대조 심사 기록이 있는가? | 교대조별 심사 일지, 야간 시간대 서명 | 주간조 위주로만 심사 수행 |
| 심사 발견사항이 적절히 종결되었는가? | 시정조치 보고서($CAR$), 유효성 검증 기록 | 부적합 지적만 있고 후속 조치 및 검증 부재 |

### 3.2 현장 실사 (Shop Floor Observation)
- **Point 1**: 심사 당일 현장 작업자가 내부 심사가 진행되었음을 인지하고 있는가?
- **Point 2**: 현장 사무실에 게시된 품질 지표와 내부 심사 보고서상의 성과 데이터가 일치하는가?
- **Point 3**: 부적합품 격리 구역에 대해 최근 내부 심사원이 점검한 흔적이 있는가?

## 4. 부적합 등급 분류 (NC Classification)
- **Major NC**: 연간 내부 심사 계획이 수립되지 않음, 심사 독립성 완전 상실, 중대 고객 클레임 발생 공정에 대한 심사 누락.
- **Minor NC**: 교대조 샘플링 일부 누락, 심사 보고서의 증거 기록(Evidence) 기술 부족.

## 5. AuditCycleFidelityEngine: Diagnostic Logic
본 엔진은 내부 심사 시스템의 '망라성(Coverage)'을 진단합니다.

```python
class AuditCycleFidelityEngine:
    def __init__(self, coverage_pct, independence_check, shift_sampling_done):
        self.coverage = coverage_pct # Total processes audited in 3 years
        self.independent = independence_check
        self.shifts = shift_sampling_done

    def audit_system_trust(self):
        """내부 심사 시스템 완결성 진단"""
        if self.coverage < 100:
            return f"REJECT: Audit Coverage Incomplete ({self.coverage}%). Prune gap."
        if not self.independent:
            return "CRITICAL: Objectivity Compromised. Independence violation detected."
        if not self.shifts:
            return "WARNING: Multi-shift sampling missing. Shop floor risk elevated."
        return "PASS: Independent Audit Intelligence Operational"
```

## 6. 스스로 체크 (Self-Audit)
1. **[Independence]**: 품질팀 직원이 품질 시스템 전체를 심사할 때, 감독관이 지적할 수 있는 논리는? (정답: 객관성 및 공평성 훼손 가능성)
2. **[Night Shift]**: 우리 회사는 주간 2교대만 운영한다. 이때 야간 심사를 하지 않아도 되는가? (정답: 생산이 발생하는 모든 교대조를 심사해야 함)
3. **[Effectiveness]**: 내부 심사에서는 '적합성'만 보면 되는가? (정답: 제조공정 심사의 경우 '효과성'과 '효율성'까지 판단해야 함 - Clause 9.2.2.3)

### 🔗 참조된 로컬 지식망 (Retrieved Nodes - Local Domain Only)
- MOC iatf-16949-automotive-quality-execution-fabric
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- SOP iatf-16949-internal-auditor-qualification-and-competency-procedure

**[V6.3.7_INTERNAL_AUDIT_SOP_AUDITOR_GRADE]**
**[TOPOLOGY_POLICY: INDEPENDENT_ORGANISM]**
**[GRAPHIFY_LINK_EXTERNAL: FALSE]**
**[TIMESTAMP: 2026-05-12]**
