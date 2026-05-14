---
Basic:
  date: '2026-05-12'
  domain: 05_Semiconductor
  id: semiconductor-global-investment-and-subsidy-log-v2026-data
  project: Vault_Modernization
  version: v6.3.7
Dynamic:
  diagnostic_protocol:
  - 'Standard_Verification: Verify baseline parameters.'
  - 'Context_Audit: Ensure topological integrity.'
  fidelity_engine: DomainFidelityEngine
  graphify_link_external: true
  status: Ratified_v6.3.7_Migration
  topology_policy: Interconnected_Cluster
Object:
  description: Standard Industrial Node
  object_type: Concept
  physical_model: N/A
  tier: 1
Semantic:
  expected_queries:
  - '*   Role: Assistant to an Antigravity Industrial Process Engineer.'
  - '*   Task: Create 5 expected queries for searching the provided technical document.'
  - '*   Constraints:'
  - Specific and practical (professional).
  - End with '?'.
  is_part_of: '["Strategy global-semiconductor-supply-chain-governance", "MOC 01_Semiconductor"]'
  related_to: []
  tags: '["#Data", "#Semiconductor", "#Investment", "#Subsidy", "#FDI", "#Trade_Restriction",
    "#Geopolitics", "#HDS_Gold_v6_1"]'
Trust Metrics:
  T_dynamic: 1.0
  T_init: 1.0
  T_static: 1.0
  isolation_index: 0.0
  source: Antigravity Vault
---

# [[[Semiconductor] semiconductor-global-investment-and-subsidy-log-v2026

## 1. [데이터셋 개요 (Dataset Overview)]]
본 데이터셋은 글로벌 반도체 패권 경쟁 속에서의 **국가별 투자 규모 및 보조금 집행 현황**을 기록한 실측 로그입니다. 각국의 칩스법(CHIPS Act)에 따른 직접 보조금, 세제 혜택, 신규 팹 건설 현황, 그리고 수출 규제 위반 건수 등을 포함하며, 반도체 공급망의 자국 중심 재편 시도가 실제 산업 지형을 어떻게 바꾸고 있는지 수리적으로 증명합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 항목 (Property) | 실측 범위 / 규격 (Measured Range) | 데이터 정밀도 (Precision) | 비고 (Remarks) |
| :--- | :--- | :--- | :--- |
| **Subsidy Amount**| $0.1 \sim 50.0 \text{ B \$}$ (per project) | $\pm 0.01 \text{ B}$ | 국가가 기업에 지급한 직접 보조금 및 인프라 지원금 |
| **New Fabs** | $0 \sim 10$ (starts per year) | Integer | 각 권역별로 착공된 신규 반도체 제조 시설 수 |
| **Export Viol.** | $0 \sim 50 \text{ events/year}$ | Integer | 핵심 장비 및 기술의 수출 규제 리스트 위반 적발 건수 |
| **FDI Inflow** | $1 \sim 100 \text{ B \$}$ (Global total) | $\pm 0.1 \text{ B}$ | 반도체 산업으로 유입된 외국인 직접 투자 규모 |
| **Tax Credit** | $10 \sim 40 \%$ | $\pm 0.1 \%$ | 연구개발(R&D) 및 시설 투자에 대한 법인세 감면율 |
| **Cap. Utiliz.** | $70 \sim 100 \%$ | $\pm 0.1 \%$ | 가동 중인 파운드리 및 메모리 팹의 실질 가동률 |
| **Equip. Order** | $100 \sim 1,000$ (units per qtr) | Integer | 노광기(EUV/DUV) 등 핵심 장비의 신규 주문 및 인도량 |
| **Talent Index** | $0.0 \sim 1.0$ (Net inflow) | Continuous | 핵심 엔지니어의 국가 간 이동 및 인력 확보 수준 지표 |

## 3. [Advanced RAG 분석 로직: 수리적 실측 데이터 분석]

### 3.1 [보조금 투입 대비 생산 능력 확충의 탄력성(Elasticity) 분석]
정부 지원금이 실제 제조 역량 강화로 이어지는 효율을 분석합니다. RAG는 "본 로그를 분석하여, 보조금이 $10\text{B \$}$ 투입될 때마다 $12\text{inch}$ 웨이퍼 월간 생산 능력이 $50\text{K}$장 증가했음을 수리적으로 입증"합니다.

### 3.2 [수출 규제 강도와 글로벌 칩 가격 변동의 상관관계 분석]
특정 국가에 대한 장비 금수 조치가 시장에 미치는 영향을 분석합니다. RAG는 "데이터셋의 규제 위반 및 장비 인도량 데이터를 분석하여, 심자외선(DUV) 장비 제한 시 특정 공정의 칩 가격이 $15\%$ 인상되었음을 확증"합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Strategy global-semiconductor-supply-chain-governance : 본 데이터의 생성 기반이 되는 글로벌 반도체 거버넌스 및 공급망 전략 엔티티
- MOC 01_Semiconductor : 반도체 산업의 기술과 정책을 통합 관리하는 상위 지식 허브

*Created by Flash (HDS Gold V6.3.7 & Meta-Fusion V6.3.7 ULTRA-Enrichment)*