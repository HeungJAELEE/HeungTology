---
Basic:
  id: "INTERVIEW_SEMICON_04_ETCHING"
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
  tags: '["#Interview", "#Semiconductor", "#Etching", "#Plasma", "#HDS_Gold_v6_1"]'
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

# [[[Semiconductor] 8대공정_04_식각

## 1. [왜 중요한가? (Why): 나노 세계의 정밀 조각]]
[🟢 Local RAG] 식각 공정은 포토 공정에서 정의된 패턴을 따라 불필요한 부분을 깎아내어 실제 회로를 구조화하는 과정입니다. 아무리 정밀하게 지도를 그려도(포토), 수직으로 깊게 파 내려가는 식각의 정밀도가 낮으면 소자 간의 단락(Short)이나 저항 증가를 막을 수 없습니다. 특히 수백 층을 쌓는 V-NAND에서 식각은 기술력의 상징입니다.

## 2. [핵심 메커니즘 (Mechanism)]
### 2.1 Reactive Ion Etching (RIE, 반응성 이온 식각)
[🟢 Local RAG] 화학적 반응과 물리적 타격의 장점을 결합한 현대 식각의 표준입니다.
- **화학적 식각 (라디칼)**: 등방성(Isotropic) 특성. 반응성이 높은 라디칼이 특정 물질과 반응하여 휘발성 물질로 제거. **선택비(Selectivity)**가 우수함.
- **물리적 식각 (이온)**: 이방성(Anisotropic) 특성. 가속된 이온이 표면을 때려 결합을 끊음. **방향성**이 우수함.
- **RIE 시너지**: 수직으로 가속된 이온이 충돌하여 표면 에너지를 높이면, 그 부위만 라디칼과 빠르게 반응하여 제거됨으로써 수직 프로파일을 완성함.

## 3. [면접 빈출 질문 Top 3 (Q&A)]

### Q1. 식각 공정에서 '선택비(Selectivity)'와 '이방성(Anisotropy)'의 의미는?
- **[A]**: [🟢 Local RAG] **선택비**는 깎고자 하는 물질과 남겨야 하는 물질(마스크 등) 간의 식각 속도 비율입니다. **이방성**은 수평 방향 대비 수직 방향으로 얼마나 잘 깎이는지를 나타내는 지표입니다. 미세 공정일수록 옆면은 건드리지 않고 수직으로만 깊게 파는 고이방성($A_f \approx 1$) 확보가 필수적입니다.

### Q2. '로딩 효과(Loading Effect)'란 무엇이며 해결 방안은?
- **[A]**: [🟢 Local RAG] 웨이퍼 상의 패턴 밀도에 따라 식각 속도가 달라지는 현상입니다. 패턴이 조밀한 곳은 반응 가스가 빨리 소모되어 식각이 느려지는 **Macro-loading**과, 좁은 구멍 내부로 가스 유입이 어려운 **Micro-loading**이 있습니다. 가스 유량 조절, 압력 제어, 혹은 장비 하드웨어(ESC 등)의 온도 구배 보정을 통해 해결합니다.

### Q3. V-NAND 적층 수가 늘어남에 따라 식각 공정에서 발생하는 병목 현상은?
- **[A]**: [🌐 Web Search] **ARDE (Aspect Ratio Dependent Etch)** 현상입니다. 종횡비(높이/폭)가 커질수록 이온과 생성물의 이동이 제한되어 바닥이 덜 깎이는 현상이 발생합니다. 이를 극복하기 위해 **극저온 식각(Cryogenic Etching)** 기술이 도입되고 있으며, 영하 100도 이하에서 식각을 진행하여 측벽 보호막을 강화하고 식각 속도를 높입니다.

## 4. [최신 트렌드 2026 (Trends)]
- **Atomic Layer Etch (ALE)**: 원자층 단위로 한 층씩 제거하여 CD(선폭) 손실을 제로에 가깝게 제어하는 차세대 기술이 2nm 공정의 표준으로 자리 잡고 있습니다.
- **극저온 식각의 상용화**: 400단 이상의 NAND 경쟁에서 채널 홀을 한 번에 뚫는 'Single Stack' 기술을 위해 극저온 장비 도입이 가속화되고 있습니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 🏛️ Entity plasma-etching-and-selective-material-removal (Verified)
- 🏛️ 02_Knowledge/entities/data/Data atomic-layer-etch-ale-selectivity-and-uniformity-log-v2026 (Verified)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
