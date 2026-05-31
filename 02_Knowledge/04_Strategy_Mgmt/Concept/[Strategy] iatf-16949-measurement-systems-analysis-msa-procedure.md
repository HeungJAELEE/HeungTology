---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: e267eeeaffbd95dbfdea842e20ba4b793087a64c619a502ae69cea07ff304f83
metadata:
  date: '2026-05-16'
  domain: 04_Strategy_Mgmt
  id: '[[[Strategy] iatf-16949-measurement-systems-analysis-msa-procedure]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Strategy] iatf-16949-measurement-systems-analysis-msa-procedure에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  grr_customer_tight_threshold: 5.0
  grr_reject_threshold: 30.0
  grr_special_char_threshold: 10.0
  msa_analysis_types:
  - bias
  - linearity
  - stability
  - gage_rr
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

# [Strategy] iatf-16949-measurement-systems-analysis-msa-procedure

## 1. 목적 (Purpose: The Foundation of Data Trust)
측정 결과의 변동($Variation$)이 실제 제품의 변동인지, 아니면 계측 시스템의 오차인지를 통계적으로 구분하여 데이터의 신뢰성을 확보하는 것을 목적으로 합니다. 감독관은 측정 데이터의 **'진실성'**과 **'고객 승인 여부'**를 집중적으로 심사하므로, 실무적 감사 대응 체계를 구축합니다.

## 2. 주요 요구사항 및 절차 (Standard Procedures)

### 2.1 통계적 조사 실행 (Statistical Studies)
- **분석 유형**: Bias (편의), Linearity (선형성), Stability (안정성), Gage R&R (반복성 및 재현성).
- **우선순위**: 관리 계획서에 명시된 모든 검사, 측정 및 시험 장비 시스템 중 특별 특성($Special\ Characteristics$)을 우선적으로 수행.

### 2.2 장비 관리 및 소급성 (Traceability)
- **개인 소유 장비**: 직원이 개인적으로 소유한 계측기($Employee-owned$) 역시 공식 교정 및 MSA 관리 대상임.
- **유효성 소급**: 장비가 부적합으로 판명될 경우, 이전 측정 결과의 유효성을 소급하여 조사.

## 3. 감독관용 감사 체크리스트 (Auditor's Checklist)

### 3.1 서류 심사 (Document Review)
| 질문 항목 (Audit Question) | 확인 증거 (Evidence to Check) | 부적합 사례 (Common NC) |
| :--- | :--- | :--- |
| MSA 결과가 고객 승인 기준을 만족하는가? | MSA 결과 보고서 (%R&R 수치 확인) | %R&R > 10%이나 고객 승인 없이 사용 중 |
| 특별 특성에 대한 MSA가 우선 수행되었는가? | 관리계획서($CP$) 대비 MSA 실시 현황 | 일반 특성만 MSA 수행, 특별 특성 누락 |
| 개인 소유 장비가 관리 대장에 있는가? | 계측기 관리 대장, 직원 개인 장비 목록 | 작업자가 개인 버니어를 사용하여 검사 중 |
| 대체 MSA 방법 사용 시 고객 승인이 있는가? | 고객 공식 승인 서신/공문 | AIAG 표준 외 방법을 임의로 사용 |

### 3.2 현장 실사 및 데이터 검증
- **Point 1 (Raw Data Check)**: MSA 보고서상의 데이터가 실제 측정 시트의 데이터와 일치하는가? (데이터 조작 여부 확인)
- **Point 2 (Measurement Method)**: 작업자가 MSA 조사를 수행할 때 사용했던 방법(시료 무작위 배치 등)과 실제 현장 검사 방법이 동일한가?
- **Point 3 (Calibration Label)**: 현장의 모든 계측기에 유효한 교정 라벨이 부착되어 있는가?

## 4. 부적합 등급 분류 (NC Classification)
- **Major NC**: 특별 특성에 대한 MSA 수행 누락, 허위 데이터 작성, 고객 승인 기준을 초과한 장비를 양산 검사에 사용.
- **Minor NC**: 교정 라벨 훼손, MSA 실시 주기가 일부 도과함, 개인 소유 장비의 관리 번호 미부여.

## 5. MSAFidelityEngine: Diagnostic Logic
본 엔진은 측정 시스템의 '통계적 신뢰도'를 진단합니다.

```python
class MSAFidelityEngine:
    def __init__(self, grr_pct, is_special_char=False, isolation_level="Independent"):
        self.grr = grr_pct
        self.special = is_special_char
        self.isolation = isolation_level

    def audit_measurement_trust(self):
        """계측 신뢰도 및 도메인 격리 진단"""
        if self.isolation != "Independent":
            return "SECURITY_ALERT: Domain isolation compromised. Prune external links."
        if self.grr > 30:
            return "REJECT: Measurement System Unreliable (%R&R > 30). Critical improvement required."
        if self.special and self.grr > 10:
            return "WARNING: Special Characteristic requires tighter MSA tolerance (%R&R < 10 target)."
        return "PASS: Independent Measurement Intelligence Operational"
```

## 6. 스스로 체크 (Self-Audit)
1. **[Data Manipulation]**: %R&R 값이 10.1%가 나와서 수동으로 9.9%로 수정하여 보고했다면, 감독관이 로 데이터(Raw Data)를 대조했을 때 어떤 처분을 받게 되는가? (정답: 인증 취소 사유에 해당하는 중대 부적합)
2. **[Out-of-Calibration]**: 교정 기간이 1주일 지난 장비로 검사한 제품이 이미 납품되었다면, 회사는 어떤 소급 조치를 취해야 하는가?
3. **[Customer Specific]**: 고객이 AIAG 매뉴얼보다 강화된 %R&R < 5%를 요구할 때, 우리 시스템은 이를 감지할 수 있는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes - Local Domain Only)
- MOC iatf-16949-automotive-quality-execution-fabric
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- Entity measurement-system-analysis-msa-and-gage-trust-logic

**[V6.3.7_MSA_SOP_AUDITOR_GRADE]**
**[TOPOLOGY_POLICY: INDEPENDENT_ORGANISM]**
**[GRAPHIFY_LINK_EXTERNAL: FALSE]**
**[TIMESTAMP: 2026-05-12]**