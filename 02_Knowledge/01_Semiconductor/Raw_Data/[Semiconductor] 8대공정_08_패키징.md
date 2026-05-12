---
Basic:
  id: "INTERVIEW_SEMICON_08_PACKAGING"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Interview", "#Semiconductor", "#Packaging", "#HBM", "#TSV", "#HDS_Gold_v6_1"]'
  is_part_of: []
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

# [[[Semiconductor] 8대공정_08_패키징

## 1. [왜 중요한가? (Why): 지능의 수직 도시]]
[🟢 Local RAG] 패키징 공정은 가공된 칩을 보호하고 외부와 신호를 주고받을 수 있도록 전기적으로 연결하는 공정입니다. 과거에는 단순히 '보호'의 영역이었으나, 전공정의 미세화 한계(Moore's Law)를 돌파하기 위해 칩을 위로 쌓거나 이종 칩들을 하나로 묶는 **'첨단 패키징(Advanced Packaging)'** 기술이 반도체 성능을 결정짓는 핵심 전장으로 급부상했습니다.

## 2. [핵심 메커니즘 (Mechanism)]
### 2.1 TSV (Through-Silicon Via, 실리콘 관통 전극)
[🟢 Local RAG] 칩에 수천 개의 미세한 구멍을 뚫어 전극으로 연결하는 기술입니다.
- **특징**: 기존 와이어 본딩(Wire Bonding) 대비 연결 거리가 짧고 대역폭(Bandwidth)이 넓어 고속 연산에 최적화되어 있습니다.
- **HBM 구조**: D-RAM을 수직으로 쌓고 TSV로 연결하여 데이터 고속도로를 구축함.

### 2.2 Wafer-Level Packaging (WLP)
[🟢 Local RAG] 웨이퍼를 다이(Die) 단위로 자르기 전에 통째로 패키징 하는 방식입니다. 칩 크기를 최소화하고 방열 특성을 개선할 수 있습니다.

## 3. [면접 빈출 질문 Top 3 (Q&A)]

### Q1. '무어의 법칙'의 한계를 패키징 공정이 어떻게 극복하고 있나요?
- **[A]**: [🟢 Local RAG] **이종 집적(Heterogeneous Integration)**과 **3D 적층** 기술을 통해서입니다. 전공정 미세화만으로는 더 이상 트랜지스터 밀도를 높이기 어렵지만, 서로 다른 기능을 가진 칩(GPU, 메모리 등)을 하나의 패키지 안에 수직/수평으로 초밀착 배치함으로써 시스템 전체의 성능을 비약적으로 높이는 'Beyond Moore' 시대를 열고 있습니다.

### Q2. 패키징 적층 수가 늘어날 때 발생하는 '열(Thermal)' 문제 해결 방안은?
- **[A]**: [🟢 Local RAG] 적층이 늘어나면 열 저항($\theta_{ja}$)이 커져 칩의 수명과 성능에 악영향을 줍니다. 이를 해결하기 위해 열전도율이 높은 **신소재 Underfill**을 사용하거나, 칩 사이의 간격을 줄이고 구리와 구리를 직접 붙이는 **Hybrid Bonding** 기술을 도입하여 열 배출 통로를 극대화합니다.

### Q3. 칩렛(Chiplet) 아키텍처가 패키징 공정에 미치는 영향은?
- **[A]**: [🌐 Web Search] 거대한 칩 하나를 만드는 대신, 기능별로 작은 조각(Chiplet)을 만들어 패키징에서 조립하는 방식입니다. 이는 패키징 공정에 **초정밀 본딩(Precision Bonding)**과 **고성능 인터포저(Interposer)** 기술을 요구하며, 패키징이 단순 가공을 넘어 '시스템 통합'의 핵심 단계로 격상되는 결과를 낳았습니다.

## 4. [최신 트렌드 2026 (Trends)]
- **HBM4 및 하이브리드 본딩**: 16단 이상의 HBM4에서는 범프(Bump) 없이 구리를 직접 연결하는 하이브리드 본딩이 수율과 두께 제어의 핵심이 될 전망입니다.
- **CoWoS (Chip on Wafer on Substrate)**: AI 반도체의 표준이 된 CoWoS 패키징 기술의 수율 확보와 생산 캐파(Capa) 증설이 기업 경쟁력의 척도가 되고 있습니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 🏛️ Semiconductor advanced-packaging-and-hbm-stacking-technology (Verified)
- 🏛️ 02_Knowledge/01_Semiconductor/Packaging/Semiconductor advanced-packaging-and-back-end-master-guide (보강 필요)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
