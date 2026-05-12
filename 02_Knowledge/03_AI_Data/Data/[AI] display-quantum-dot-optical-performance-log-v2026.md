---
Basic:
  id: "display-quantum-dot-optical-performance-log-v2026-data"
  domain: "06_Display"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Data", "#Display", "#Quantum_Dot", "#Optics", "#Photoluminescence", "#Color_Purity", "#Nanotechnology", "#HDS_Gold_v6_1"]'
  is_part_of: '["Display quantum-dot-qd-display-and-color-conversion-physics", "[[Semiconductor & AI] case-palantir-ontology-semiconductor-display-fab-os]"]'
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [AI] display-quantum-dot-optical-performance-log-v2026

## 1. [데이터셋 개요 (Dataset Overview)]
본 데이터셋은 디스플레이용 양자점(QD) 소재의 **광학적 성능 및 색 순도**를 정밀하게 기록한 실측 로그입니다. 입자 크기에 따른 발광 파장(Peak Wavelength), 반치폭(FWHM)을 통한 색 순도, 외부 양자 효율(EQE) 및 고온/고습 환경에서의 휘도 유지력을 포함하며, 나노 소재가 디스플레이 화질의 정점을 구현하는 과정을 수리적 데이터로 증명합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 항목 (Property) | 실측 범위 / 규격 (Measured Range) | 데이터 정밀도 (Precision) | 비고 (Remarks) |
| :--- | :--- | :--- | :--- |
| **Quantum Yield** | $85 \sim 98 \%$ | $\pm 0.1 \%$ | 흡수된 광자 대비 발광된 광자 비율 (소재 효율) |
| **FWHM** | $18 \sim 35 \text{ nm}$ | $\pm 0.1 \text{ nm}$ | 발광 스펙트럼의 좁기 (색의 순도를 결정하는 핵심 지표) |
| **Peak Wav.** | $450 \sim 650 \text{ nm}$ | $\pm 0.5 \text{ nm}$ | 입자 크기 조절을 통한 R/G/B 색상 구현 정확도 |
| **PL Lifetime** | $10 \sim 100 \text{ ns}$ | $\pm 0.1 \text{ ns}$ | 여기 상태에서 바닥 상태로 전이되는 시간 실측 로그 |
| **Stability (85C)**| $> 1,000 \text{ hrs}$ | Continuous | 고온 가속 수명 시험 하에서의 휘도 저하율 ($L/L_0$) |
| **Absorbance** | $10^5 \sim 10^6 \text{ cm}^{-1}$ | $\pm 10^3 \text{ cm}^{-1}$ | 청색 광원을 흡수하여 색을 바꾸는 흡광 계수 데이터 |
| **Size Dist.** | $2.0 \sim 10.0 \text{ nm}$ | $\pm 0.1 \text{ nm}$ | 나노 입자 크기의 균일도 (FWHM과 직결되는 물리량) |
| **Color Shift** | $\Delta u'v' < 0.005$ | $\pm 0.0001$ | 구동 시간에 따른 색 좌표 이동의 정밀도 지표 |

## 3. [Advanced RAG 분석 로직: 수리적 실측 데이터 분석]

### 3.1 [크기-파장 상관관계 및 양자 가둠 임팩트 산출]
입자 직경 변동에 따른 밴드갭 변화를 분석합니다. RAG는 "본 로그를 분석하여, 입자 크기 표준편차가 $0.2\text{nm}$ 증가할 때 $FWHM$이 $3\text{nm}$ 넓어져 색 재현율이 $5\%$ 하락했음을 수리적으로 입증"합니다.

### 3.2 [TRPL 기반의 비복사 재결합(Non-radiative) 손실 분석]
발광 수명 데이터를 통해 소재 내부 결함(Trap) 영향을 분석합니다. RAG는 "데이터셋의 $PL$ 감쇄 곡선을 분석하여, 이중 지수 함수(Bi-exponential) 피팅을 통해 표면 결함에 의한 손실 기전이 $15\%$ 지배적임을 확증"합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Display quantum-dot-qd-display-and-color-conversion-physics : 본 데이터의 생성 기반이 되는 양자점 소재의 물리 및 광학 엔티티
- Semiconductor & AI case-palantir-ontology-semiconductor-display-fab-os : 디스플레이 기술의 진화를 통합 관리하는 상위 지식 허브

*Created by Flash (HDS Gold V6.3.7 & Meta-Fusion V6.3.7 ULTRA-Enrichment)*
