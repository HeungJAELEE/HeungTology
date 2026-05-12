---
Basic:
  id: "INTERVIEW_SEMICON_06_METALLIZATION"
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
  tags: '["#Interview", "#Semiconductor", "#Metallization", "#Interconnect", "#HDS_Gold_v6_1"]'
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

# [[[Semiconductor] 8대공정_06_금속배선

## 1. [왜 중요한가? (Why): 데이터 고속도로의 건설]]
[🟢 Local RAG] 금속배선 공정은 회로 패턴을 따라 전기가 흐를 수 있는 길을 만드는 과정입니다. 아무리 소자(트랜지스터)의 성능이 좋아도 이를 연결하는 배선의 저항이 높거나 신호 지연(RC Delay)이 발생하면 반도체 전체의 속도는 저하됩니다. 미세화에 따라 좁아지는 배선 폭에서 **신뢰성**과 **저저항**을 동시에 확보하는 것이 핵심 과제입니다.

## 2. [핵심 메커니즘 (Mechanism)]
### 2.1 Copper Damascene Process (구리 다마신 공정)
[🟢 Local RAG] 구리는 식각이 어렵기 때문에 절연막에 미리 홈을 파고 구리를 채워 넣는 방식을 사용합니다.
1. **Trench Etching**: 절연막에 배선용 홈을 형성.
2. **Barrier/Seed Deposition**: 구리의 확산을 막는 장벽층(Ta/TaN)과 전기도금을 위한 Seed 층 증착.
3. **Electroplating**: 전기도금으로 구리를 홈에 채움.
4. **CMP**: 과도하게 증착된 구리를 연마하여 평탄화하고 절연막 사이를 고립시킴.

## 3. [면접 빈출 질문 Top 3 (Q&A)]

### Q1. 배선 소재로 알루미늄(Al) 대신 구리(Cu)를 사용하는 이유는 무엇인가요?
- **[A]**: [🟢 Local RAG] 크게 두 가지 장점이 있습니다. 첫째, **비저항이 낮아** 신호 전달 속도가 빠르고 발열이 적습니다. 둘째, **일렉트로마이그레이션(Electromigration, EM)** 내성이 우수하여 미세 배선에서도 높은 수명을 유지할 수 있기 때문입니다.

### Q2. '일렉트로마이그레이션(Electromigration)'이란 무엇이며 어떻게 제어하나요?
- **[A]**: [🟢 Local RAG] 고밀도의 전류가 흐를 때 전자와 금속 원자의 충돌로 인해 금속 원자가 이동하여 배선에 빈 공간(Void)이나 돌기(Hillock)를 만드는 현상입니다. 이를 방지하기 위해 구리 배선 위에 **Capping Layer**를 형성하거나, 배선 구조를 최적화하여 원자 이동을 억제합니다.

### Q3. BSPDN(Backside Power Delivery Network) 기술이 왜 최근 화두인가요?
- **[A]**: [🌐 Web Search] 2nm 이하 공정에서는 웨이퍼 앞면에 신호 배선과 전력 배선이 섞여 있어 공간 부족과 간섭(Noise) 문제가 심각합니다. **BSPDN**은 전력 배선을 웨이퍼 **뒷면**으로 옮겨 신호 배선의 밀도를 높이고 저항에 의한 전압 강하(IR Drop)를 개선하는 획기적인 선단 기술입니다.

## 4. [최신 트렌드 2026 (Trends)]
- **신소재 도입**: 구리의 한계를 넘기 위해 루테늄(Ru)이나 몰리브덴(Mo) 등 장벽층 없이도 확산이 적고 저항이 낮은 차세대 금속 연구가 활발합니다.
- **Direct Bonding**: 칩렛 구조에서 칩 간 배선 거리를 최소화하기 위해 범프 없이 구리와 구리를 직접 붙이는 **Hybrid Bonding** 기술이 배선 공정의 연장선에서 중요해지고 있습니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 🏛️ Entity metallization-and-interconnect-reliability (Verified)
- 🏛️ 02_Knowledge/entities/Entity advanced-packaging-and-hbm-stacking-technology (Verified)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
