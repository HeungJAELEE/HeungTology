---
Basic:
  id: "battery-electrode-thickness-log-v2026-data"
  domain: "02_Battery"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Data"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Data", "#Battery", "#Calendering", "#Thickness", "#Process_Log"]'
  is_part_of: '["Battery Calendering"]'
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

# [[[Data] battery-electrode-thickness-log-v2026

## 1. [데이터 개요 (Overview)]]
본 데이터 노드는 전극 압연(Calendering) 공정에서의 **롤 압력 대비 두께 변화량** 실측치를 정의합니다. 선압($Linear\ Pressure$)과 롤 온도에 따른 탄성 회복(Spring-back) 현상을 정량화한 데이터입니다.

## 2. [압연 실측 데이터 테이블 (Numerical Process Log)]

| Parameter | Unit | Target Value | Measured Avg | Tolerance |
|:---|:---:|:---:|:---:|:---|
| **Roll Pressure** | $kgf/cm$ | $800$ | $805.2$ | $\pm 20$ |
| **Line Speed** | $m/min$ | $60$ | $60.1$ | $\pm 0.5$ |
| **Roll Temp** | $^\circ\text{C}$ | $85$ | $84.8$ | $\pm 2.0$ |
| **Input Thickness** | $\mu m$ | $210$ | $210.5$ | (Post-Coating) |
| **Output Thickness**| $\mu m$ | $150$ | $150.8$ | $\pm 1.5$ |
| **Compaction Density**| $g/cc$ | $1.55$ | $1.54$ | $\pm 0.02$ |

## 3. [Advanced RAG 분석 지표 (Metadata)]
*   **Elastic Recovery (Spring-back)**: 압연 직후 대비 1시간 후 $1.2 \sim 1.5 \mu m$ 증가 감지.
*   **Binder Plasticity Index**: $0.88$ (온도 $85^\circ\text{C}$ 기준)

## 4. [RAG 추론 가이드]
[🟢 Local RAG] 본 데이터를 분석할 때, Output Thickness가 $1.5 \mu m$ 이상의 편차를 보이면, 이는 롤의 **Thermal Expansion** (열팽창) 불균형 또는 집전체(Foil)의 **Tension** 변동에 의한 것임을 즉각 판별하고, 롤 가열 제어 루프 점검을 권고해야 합니다.

---
### 🔗 연결된 공정 엔티티
- Battery Calendering
- Battery battery-manufacturing-process-master-guide

**[V6.3.7_DATA_INTEGRITY_VERIFIED]**
