---
metadata:
  date: "2026-05-16"
  id: "[[[Strategy] iatf-16949-risk-analysis-and-preventive-action-procedure]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "04_Strategy_Mgmt"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "6b071b2ae29a7d0ae09eb66074fa0c9acaf20c78b0f80f10189a6a7713e517cc"
object:
  object_type: "Concept"
  tier: 1
  description: '[Strategy] iatf-16949-risk-analysis-and-preventive-action-procedure에 관한 고밀도 지능 노드'
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


# [Strategy] iatf-16949-risk-analysis-and-preventive-action-procedure

## 1. 목적 (Purpose: Proactive Quality Shield)
본 절차는 잠재적 부적합의 원인을 사전에 파악하고 리스크를 정량화하여, 문제가 발생하기 전에 예방 조치($Preventive\ Action$)를 취하는 것을 목적으로 합니다. 감독관은 리스크 관리가 단순히 '문서'로만 존재하는지, 아니면 '현장 데이터'와 연동되는지를 집중적으로 심사하므로, 실전적 감사 대응 체계를 구축합니다.

## 2. 주요 요구사항 및 절차 (Standard Procedures)

### 2.1 리스크 분석 (Risk Analysis)
- **범위**: 신제품 개발(APQP), 공정 변경, 공급망 변동, 필드 클레임 데이터를 포함한 조직 전반의 리스크.
- **도구**: FMEA(Failure Mode and Effects Analysis), 리스크 매트릭스($Severity \times Probability$), SWOT 분석.
- **데이터 소스**: 과거의 불량 이력, 리콜 데이터, 유사 제품의 공정 능력($C_{pk}$) 트렌드.

### 2.2 예방 조치 및 학습 교훈 (Preventive Action & Lessons Learned)
- **학습 교훈 이식**: 과거의 실패 사례($Lessons\ Learned$)를 데이터베이스화하여 신규 프로젝트의 설계 및 공정 계획에 의무적으로 반영.
- **효과성 검증**: 예방 조치가 실행된 후, 일정 기간 동안 실제 부적합 발생 여부를 추적하여 리스크 감소 여부를 검증.

## 3. 감독관용 감사 체크리스트 (Auditor's Checklist)

### 3.1 서류 심사 (Document Review)
| 질문 항목 (Audit Question) | 확인 증거 (Evidence to Check) | 부적합 사례 (Common NC) |
| :--- | :--- | :--- |
| 리스크 분석이 모든 제품/공정에 수행되었는가? | 리스크 평가 보고서, PFMEA 마스터 리스트 | 일부 신규 라인에 대한 리스크 평가 누락 |
| 과거 실패 사례가 신규 공정에 반영되었는가? | Lessons Learned 반영 이력, PFMEA 개정 이력 | 유사 불량이 신규 라인에서도 동일하게 발생 |
| 예방 조치의 효과성이 검증되었는가? | 조치 후 모니터링 기록, 리스크 점수 하향 조정 증빙 | 조치만 완료하고 실제 리스크 감소 여부 미확인 |
| 리스크 파악 시 '제품 안전'이 고려되었는가? | 안전 관련 리스크 식별 항목 (Clause 4.4.1.2 연계) | 일반 품질 리스크만 있고 안전 리스크 누락 |

### 3.2 현장 실사 및 데이터 검증
- **Point 1**: 현장 PFMEA의 '발생 빈도($Occurrence$)' 점수가 실제 공정 불량률 데이터와 동기화되어 있는가? (데이터 조작 여부 확인)
- **Point 2**: 예방 조치로 설치된 설비(센서 등)가 실제 리스크 평가서에 명시된 대로 작동하는가?

## 4. 부적합 등급 분류 (NC Classification)
- **Major NC**: 중대 필드 클레임 발생 원인이 리스크 분석에서 누락됨, 예방 조치 프로세스 자체가 부재함.
- **Minor NC**: 리스크 평가 주기가 일부 도과함, Lessons Learned 데이터베이스의 업데이트 지연.

## 5. RiskFidelityEngine: Diagnostic Logic
본 엔진은 리스크 관리 시스템의 '선제적 방어력'을 진단합니다.

```python
class RiskFidelityEngine:
    def __init__(self, risk_coverage, action_effectiveness, isolation="Independent"):
        self.coverage = risk_coverage # 0~100
        self.effectiveness = action_effectiveness # 0~100
        self.isolation = isolation

    def audit_risk_vitality(self):
        """리스크 관리 생명력 및 격리 진단"""
        if self.isolation != "Independent":
            return "SECURITY_ALERT: Domain isolation compromised. Prune external links."
        if self.coverage < 95:
            return "REJECT: Incomplete Risk Coverage. Systemic blind spots detected."
        if self.effectiveness < 80:
            return "WARNING: Preventive actions show low effectiveness. Recurrence risk high."
        return "PASS: Proactive Risk Intelligence Operational"
```

## 6. 스스로 체크 (Self-Audit)
1. **[Lessons Learned]**: 신규 라인을 셋업할 때, 3년 전 A 공장에서 발생했던 클레임 사례를 확인했다는 증거를 감독관에게 어떻게 보여줄 것인가?
2. **[Static Risk]**: 5년 전 작성된 PFMEA의 리스크 점수가 한 번도 변하지 않았다면, 감독관은 이를 어떻게 해석하겠는가? (정답: 리스크 관리가 형식적으로만 운영되고 있다고 판단)
3. **[Independent Fabric]**: 리스크 데이터가 타 도메인(재무 등)과 섞여 있을 때 발생하는 품질 거버넌스의 리스크는?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes - Local Domain Only)
- MOC iatf-16949-automotive-quality-execution-fabric
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- SOP iatf-16949-product-safety-management-procedure

**[V6.3.7_RISK_SOP_AUDITOR_GRADE]**
**[TOPOLOGY_POLICY: INDEPENDENT_ORGANISM]**
**[GRAPHIFY_LINK_EXTERNAL: FALSE]**
**[TIMESTAMP: 2026-05-12]**
