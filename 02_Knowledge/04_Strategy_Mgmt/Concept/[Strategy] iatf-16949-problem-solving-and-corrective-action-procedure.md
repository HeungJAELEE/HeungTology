---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 77c83e215cbedfc0df58fa41185a880de1d1f487ec7f02075c11c07f33e01964
metadata:
  date: '2026-05-16'
  domain: 04_Strategy_Mgmt
  id: '[[[Strategy] iatf-16949-problem-solving-and-corrective-action-procedure]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Strategy] iatf-16949-problem-solving-and-corrective-action-procedure에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  clause_reference: 10.2.3.f
  rca_depth_threshold: 3
  version: V6.3.7
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

# [Strategy] iatf-16949-problem-solving-and-corrective-action-procedure

## 1. 목적 (Purpose: The Systemic Immune System)
발생한 부적합의 근본 원인을 규명하고 시스템적 시정 조치를 통해 재발을 방지하는 것을 목적으로 합니다. 감독관은 **'5-Why의 깊이'**와 **'PFMEA/관리계획서의 업데이트 여부'**를 집중적으로 심사하므로, 실전적 감사 대응 체계를 구축합니다.

## 2. 주요 요구사항 및 절차 (Standard Procedures)

### 2.1 문제 해결 접근법 (8D / 5-Why)
- **근본 원인 분석**: 현상에 대한 '발생 원인'과 시스템적 '유출 원인'을 모두 규명.
- **표준화**: 시정 조치 결과를 반드시 PFMEA 및 관리 계획서에 반영.

### 2.2 수평 전개 (Read-across)
- **유사 공정 적용**: 발생한 문제가 다른 라인이나 유사 제품에서도 발생할 수 있는지 검토하고 선제적 조치 수행.

## 3. 감독관용 감사 체크리스트 (Auditor's Checklist)

### 3.1 서류 심사 (Document Review)
| 질문 항목 (Audit Question) | 확인 증거 (Evidence to Check) | 부적합 사례 (Common NC) |
| :--- | :--- | :--- |
| 근본 원인이 '사람의 실수'로만 결론 났는가? | 8D 보고서, 5-Why 분석 시트 | 근본 원인이 "작업자 부주의"로 종료됨 (시스템적 원인 부재) |
| 시정 조치 후 PFMEA가 업데이트되었는가? | PFMEA 개정 이력, 리스크 점수(RPN) 조정 | 8D는 완료되었으나 PFMEA는 구버전 그대로임 |
| 유사 제품에 대한 수평 전개가 되었는가? | Read-across 검토서, 타 라인 시정조치 | A 라인에서 터진 문제가 B 라인에서 재발함 |
| 시정 조치의 유효성이 검증되었는가? | 조치 후 품질 지표($C_{pk}$, 불량률) 추이 | 조치만 하고 불량률 변화 확인 안 함 |

### 3.2 현장 실사 및 데이터 검증
- **Point 1 (Standard Update)**: 8D 보고서에 명시된 시정 조치(예: 센서 추가)가 실제 현장 설비에 반영되어 있는가?
- **Point 2 (Operator Awareness)**: 해당 공정 작업자가 과거에 발생했던 문제와 그에 따른 시정 조치 내용을 알고 있는가?
- **Point 3 (Verification Record)**: 유효성 검증 기간 동안 생산된 제품의 검사 기록이 존재하는가?

## 4. 부적합 등급 분류 (NC Classification)
- **Major NC**: 중대 부적합 재발, 시정 조치 후 PFMEA 업데이트 누락, 5-Why 분석 부재.
- **Minor NC**: 시정 조치 완료 예정일 도과, 8D 보고서의 일부 항목 기재 미흡.

## 5. ImprovementFidelityEngine: Diagnostic Logic
본 엔진은 문제 해결의 '논리적 완결성'을 진단합니다.

```python
class ImprovementFidelityEngine:
    def __init__(self, rca_depth, read_across_done, docs_updated, isolation="Independent"):
        self.depth = rca_depth
        self.read_across = read_across_done
        self.updated = docs_updated
        self.isolation = isolation

    def audit_corrective_action(self):
        """시정 조치 프로세스 무결성 및 격리 진단"""
        if self.isolation != "Independent":
            return "SECURITY_ALERT: Domain isolation compromised. Prune external links."
        if self.depth < 3:
            return "WARNING: Root Cause Analysis too shallow."
        if not self.read_across:
            return "REJECT: Read-across missing."
        if not self.updated:
            return "CRITICAL: PFMEA/Control Plan not updated (Clause 10.2.3.f Violation)."
        return "PASS: Independent Improvement Intelligence Operational"
```

## 6. 스스로 체크 (Self-Audit)
1. **[Root Cause]**: "작업자 재교육"이 시정 조치의 전부일 때, 감독관이 던질 수 있는 치명적인 질문은? (정답: "왜 시스템적으로 작업자가 실수할 수밖에 없었는가?")
2. **[Standardization]**: 8D 보고서가 승인된 날짜와 PFMEA가 개정된 날짜가 6개월 차이 난다면 감독관은 무엇을 지적하겠는가?
3. **[Read-across]**: "유사 제품이 없다"는 핑계가 감독관에게 통하지 않을 때는 언제인가? (정답: 유사한 '공정 요소'가 존재할 때)

### 🔗 참조된 로컬 지식망 (Retrieved Nodes - Local Domain Only)
- MOC iatf-16949-automotive-quality-execution-fabric
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- SOP iatf-16949-risk-analysis-and-preventive-action-procedure

**[V6.3.7_IMPROVEMENT_SOP_AUDITOR_GRADE]**
**[TOPOLOGY_POLICY: INDEPENDENT_ORGANISM]**
**[GRAPHIFY_LINK_EXTERNAL: FALSE]**
**[TIMESTAMP: 2026-05-12]**