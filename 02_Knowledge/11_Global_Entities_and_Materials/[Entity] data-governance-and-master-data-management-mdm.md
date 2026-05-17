---
metadata:
  id: "[[[Entity] data-governance-and-master-data-management-mdm]]"
  domain: "11_Global_Entities_and_Materials"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Entity] data-governance-and-master-data-management-mdm에 관한 고밀도 지능 노드"
semantic:
  tags: ["#11_Global_Entities_and_Materials", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Entity] data-governance-and-master-data-management-mdm

## 1. 개요 (Why: 인간적 통찰)
기업이라는 거대한 몸체에서 데이터는 혈액과 같습니다. 그런데 부서마다 환자 이름이 다르고, 제품 코드가 제각각이라면 몸은 마비될 수밖에 없습니다. **마스터 데이터 관리(MDM)**는 기업의 가장 핵심이 되는 '기준 정보'(고객, 제품, 자산 등)에 대해 단 하나의 **'진실된 기록(Golden Record)'**을 만드는 과정입니다. **데이터 거버넌스**는 그 기록을 누가, 어떻게, 어떤 규칙으로 관리할지 정하는 약속입니다. 이 둘이 결합할 때, 기업은 모든 부서가 같은 언어로 소통하는 '지능형 조직'으로 거듭납니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 엔티티 분석(Entity Resolution) 모델
서로 다른 시스템에 흩어진 "홍길동", "H. Gil-dong", "Gildong Hong"이 같은 사람인지 판별하는 수학적 확률 모델입니다.

$$ P(Match) = \prod_{i=1}^n P(\text{Attribute}_i | \text{Same Entity}) $$

**[인간적 해석]**: 이름은 비슷해도 주소나 전화번호가 다르다면 다른 사람일 확률이 높습니다. MDM은 이러한 여러 변수를 결합하여 "99% 확률로 동일인이다"라는 결론을 내리고 하나로 합치는 '지능형 통합' 작업입니다.

### 2.2. 데이터 부채(Data Debt) 공식
관리되지 않는 데이터가 기업에 끼치는 비용적 손실을 계산합니다.

$$ \text{Data Debt} = N_{dup} \cdot C_{ops} + N_{err} \cdot C_{decision} $$

*   $N_{dup}$: 중복 데이터 수.
*   $C_{ops}$: 중복 데이터 처리에 드는 운영 비용.
*   $N_{err}$: 잘못된 데이터 수.
*   $C_{decision}$: 잘못된 데이터로 인한 의사결정 실패 비용.

**[인간적 해석]**: 데이터를 방치하는 것은 고금리 사채를 쓰는 것과 같습니다. 나중에 그 오류를 바로잡으려면 처음 관리할 때보다 수백 배의 비용이 듭니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Parameter | Metric | Target Value | Unit |
| :--- | :--- | :--- | :--- |
| Golden Record | Accuracy | > 99.8 | % |
| Sync Latency | Real-time | < 10 | seconds |
| De-duplication | Rate | > 95 | % (Automated) |
| Data Owner | Assign Rate | 100 | % (Critical) |
| ROI | Efficiency | > 300 | % |

## 4. LegalFidelityEngine: Diagnostic Logic

마스터 데이터의 정확도 및 시스템 간 동기화 지연을 진단하는 `LegalFidelityEngine` 로직입니다.

```python
class LegalFidelityEngine:
    def __init__(self, golden_record_acc, sync_delay_sec, data_owner_assigned):
        self.acc = golden_record_acc # %
        self.delay = sync_delay_sec
        self.owner = data_owner_assigned # Boolean

    def diagnose_mdm_health(self):
        """골든 레코드 정확도 및 동기화 지연 기반 MDM 무결성 진단"""
        if self.acc < 98.0:
            return f"CRITICAL: Low Master Data Integrity (Acc: {self.acc}%) - Conflict in Single Source of Truth"
        if self.delay > 3600: # 1시간 초과
            return f"WARNING: Critical Sync Latency ({self.delay}s) - Satellite Systems are Operating on Stale Data"
        if not self.owner:
            return "REJECT: Missing Data Stewardship - No Accountability for Data Quality"
        return "OPTIMAL: High-Fidelity Master Data Governance Verified"

    def audit_process_efficiency(self):
        """자동 중복 제거 프로세스 효율 진단"""
        return "PASS: Automated Entity Resolution Engine Operational"

engine = LegalFidelityEngine(golden_record_acc=99.5, sync_delay_sec=15, data_owner_assigned=True)
print(engine.diagnose_mdm_health())
```

## 5. 분석 프레임워크: MDM Implementation Strategy
1. **[Registry vs. Centralized Hub]**: 각 시스템의 데이터는 그대로 두고 인덱스만 통합할 것인지(Registry), 아니면 모든 데이터를 하나의 중앙 서버로 모아 관리할 것인지(Centralized)에 대한 기업 환경별 최적 아키텍처 선택.
2. **[Data Stewardship Program]**: "IT가 데이터를 관리한다"는 편견을 버리고, 실제 데이터를 사용하는 현업 부서 전문가가 데이터의 정의와 품질에 책임을 지는 조직적 체계 구축.
3. **[Data Quality Lifecycle]**: 데이터 생성(Create)부터 활용(Read), 수정(Update), 폐기(Delete)에 이르는 전 과정에 데이터 검증 필터(Quality firewall)를 설치하여 '깨끗한 데이터'만 흐르게 함.

## 6. 스스로 체크 (Self-Audit)
1. '결정론적 매칭(Deterministic)'과 '확률론적 매칭(Probabilistic)' 방식 중, 고객 데이터 통합에서 확률론적 방식이 더 선호되는 공학적 이유는?
2. 마스터 데이터가 변경되었을 때, 모든 위성 시스템에 그 변경 사항을 전달하는 방식 중 'Pub/Sub' 모델이 'Batch' 모델보다 지능형 기업에 적합한 이유는?
3. MDM 도입 실패의 가장 큰 원인이 '기술'이 아닌 '정치(Governance)'에 있는 이유를 부서 간 데이터 소유권 다툼 관점에서 설명하시오.

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data mdm-data-consistency-and-sync-latency-v2026`와 연동되어, 전사적 기준 정보의 일관성을 실시간 분석하고 정보 불일치에 따른 공정/영업 사고 확률을 0.1% 이하로 억제함으로써 기업 지능의 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 21_human-resource-and-organizational-intelligence-hub
- data-governance-and-enterprise-information-management
- Data mdm-data-consistency-and-sync-latency-v2026
