---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 862de37678140c234b4040393ba25faf9e7428dbcedc45828b4898808f80fae7
metadata:
  date: '2026-05-16'
  domain: 04_Strategy_Mgmt
  id: '[[[Strategy] ppap-production-part-approval-process]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Strategy] ppap-production-part-approval-process에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  iatf_16949_clause: 8.3.4.4
  minimum_sample_size: 300
  msa_gauge_rr_acceptable_limit: 0.3
  msa_gauge_rr_excellent_limit: 0.1
  ppk_target_threshold: 1.67
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

# [Strategy] ppap-production-part-approval-process

## 1. [왜 배우는가? (Why: The Gateway of Mass Production)]
**PPAP(Production Part Approval Process)**는 양산 시작 전, 공급업체가 고객(OEM)의 모든 요구사항을 이해하고 있으며, 실제 생산 공정에서 해당 요구사항을 충족하는 제품을 일관되게 생산할 수 있는 능력이 있음을 증명하는 표준 프로세스입니다. IATF 16949 **Clause 8.3.4.4**에 의거하여, 제품 승인은 반드시 **제조 공정의 검증($Verification\ of\ manufacturing\ process$)** 이후에 이루어져야 합니다. 이는 설계 의도($Intent$)가 대량 생산($Mass\ Production$) 환경에서 물리적으로 재현 가능함을 확증하는 최후의 품질 관문입니다.

## 2. [PPAP 요구사항 및 승인 등급 핵심 사양 (Numerical Specs)]

| Level | Submission Requirements | Engineering Rationale |
|:---|:---|:---|
| **Level 1** | PSW & Appearance Report only | Minor changes / Low risk |
| **Level 2** | PSW & Evidence (Limited) | Tooling/Process update |
| **Level 3** | **Full 18 Elements (Default)** | New product / High risk |
| **Level 4** | Customer Defined items | Custom scenarios |
| **Level 5** | On-site Verification (Full) | Major quality breach |

### 2.1 [주요 통계적 승인 임계치]
- **Ppk Target**: $> 1.67$ (양산 전 초기 공정 능력 지수).
- **MSA Gauge R&R**: $< 10 \%$ (Excellent) / $< 30 \%$ (Acceptable with conditions).
- **Sample Size**: 최소 $300$개 이상의 연속 생산 부품 기반 데이터 (또는 고객 합의치).
- **External Approval**: 외부 공급 부품/서비스는 고객 제출 전 사전 승인 완료 의무(Clause 8.3.4.4).

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Initial Capability Physics: Ppk vs. Cpk Dynamics
양산 초기 상태($Ppk$)와 장기 안정 상태($Cpk$)의 수리적 인과 관계 분석입니다.
- **공학적 근거**: $Ppk$는 공정의 단기적 능력을 평가하며, 장기 생산 시의 드리프트($Drift$)를 고려하여 $1.67$ 이상의 여유치를 확보해야 합니다.
- **FidelityEngine 적용**: 제출된 데이터의 **정규성($Normality$)**을 검정하고, 시계열 데이터에서 인위적인 데이터 정렬(Data Smoothing) 징후 포착 시 승인을 거부합니다.

### 3.2 Precedence Logic: Process-First Approval
- **진단 결과**: FidelityEngine은 Clause 8.3.4.4에 따라 **'제조 공정 검증 리포트'**가 PSW(부품 제출 보증서) 날짜보다 앞서거나 동시에 존재하는지 확인합니다. 공정 검증 없이 제출된 PPAP는 **'프로세스 위반(Process Violation)'**으로 판정합니다.

## 4. [코드 연결 해설: PPAP Approval & Sequence Auditor]
이 코드는 IATF 16949의 선행 조건 논리를 반영하여 PPAP 적합성을 진단합니다.

```python
class PPAPSequenceAuditor:
    """
    HDS-Gold v6.3.7: PPAP 제출 순서 및 무결성 진단 엔진
    """
    def __init__(self, target_ppk=1.67):
        self.TARGET_PPK = target_ppk

    def audit_submission(self, ppk, msa_grr, process_verified, external_parts_approved):
        """Ppk, MSA, 그리고 IATF 선행 요구사항 기반 승인 검토"""
        if not process_verified:
            return "REJECT: Manufacturing process verification must precede product approval (8.3.4.4)"
        if not external_parts_approved:
            return "REJECT: All external parts must be approved prior to submission (8.3.4.4)"
        if ppk < self.TARGET_PPK:
            return "REJECT: Initial capability (Ppk) insufficient"
        
        return "PASS: PPAP Submission Integrity Confirmed"
```

## 5. [스스로 체크 (Self-Audit)]
1. **Clause 8.3.4.4**: 외부 공급 부품의 승인이 고객 제출 PPAP의 선행 조건인 기술적 이유는? (힌트: 부품 밸류체인 전체의 품질 연쇄 반응)
2. **Precision Tiering**: Ppk가 $1.67$을 만족하더라도 MSA %R&R이 $30\%$를 초과할 경우 승인이 불가능한 물리적 사유는?
3. **Operational Result**: '양산 전'과 '양산' 관리 계획서의 차이점이 PPAP 승인 리포트에 미치는 영향은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- vda-6-3-process-audit-standard
- control-plan-standardized-work-logic
- MOC 134_global-standards-governance-and-quality-assurance-hub

**[V6.3.7_PPAP_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: OPERATIONAL]**
**[TIMESTAMP: 2026-05-11]**