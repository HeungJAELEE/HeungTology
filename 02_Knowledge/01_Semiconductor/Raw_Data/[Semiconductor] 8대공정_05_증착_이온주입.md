---
Basic:
  id: "INTERVIEW_SEMICON_05_DEP_ION"
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
  tags: '["#Interview", "#Semiconductor", "#Deposition", "#Ion_Implantation", "#HDS_Gold_v6_1"]'
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

# [[[Semiconductor] 8대공정_05_증착_이온주입

## 1. [왜 중요한가? (Why): 반도체의 생명력 부여]]
[🟢 Local RAG] 증착은 웨이퍼 위에 원하는 물질(절연막, 전도막 등)을 얇게 쌓는 과정이며, 이온주입은 부도체인 실리콘에 불순물을 주입하여 전기적 특성을 갖게(도핑) 만드는 과정입니다. 증착의 두께 정밀도와 이온주입의 농도 제어는 트랜지스터의 성능($I_{on}/I_{off}$)을 결정짓는 핵심입니다.

## 2. [핵심 메커니즘 (Mechanism)]
### 2.1 Atomic Layer Deposition (ALD, 원자층 증착)
[🟢 Local RAG] 원자 한 층씩 번갈아 가며 화학적 흡착을 통해 증착하는 방식입니다.
- **특징**: **단차 피복성(Step Coverage)**이 매우 우수하여 3D 구조나 고종횡비 구멍에도 균일한 막질 형성이 가능합니다.
- **사이클**: Precursor 공급 $\rightarrow$ Purge $\rightarrow$ Reactant 공급 $\rightarrow$ Purge (자기 제한적 반응).

### 2.2 Ion Implantation (이온 주입)
[🟢 Local RAG] 이온 입자를 강한 전기에너지로 가속하여 웨이퍼 내부로 때려 넣는 방식입니다.
- **장점**: 주입량(Dose)과 깊이(Range)를 독립적으로 정밀 제어할 수 있습니다.
- **주의점**: 충격으로 인한 **격자 손실(Damage)**이 발생하므로, 공정 후 열처리(Annealing)를 통해 격자를 회복하고 이온을 활성화해야 합니다.

## 3. [면접 빈출 질문 Top 3 (Q&A)]

### Q1. CVD 대비 ALD의 장단점은 무엇인가요?
- **[A]**: [🟢 Local RAG] ALD는 CVD보다 **단차 피복성**과 **두께 조절 능력**이 압도적입니다. 하지만 원자층 단위로 쌓기에 **증착 속도가 매우 느리다**는 단점이 있습니다. 따라서 선단 공정의 초미세 막질 형성에는 ALD를, 두꺼운 막 형성이나 생산성이 중요한 공정에는 CVD를 전략적으로 사용합니다.

### Q2. 이온주입 공정 시 '채널링(Channeling)' 현상이란 무엇이며 어떻게 방지하나요?
- **[A]**: [🟢 Local RAG] 이온이 실리콘 격자 사이의 빈 통로를 따라 예상보다 더 깊게 뚫고 들어가는 현상입니다. 이를 방지하기 위해 웨이퍼를 약간 기울여서 쏘는 **Tilt** 공정을 적용하거나, 표면에 산화막(Screen Oxide)을 미리 형성하여 이온의 궤적을 무작위화(Randomize)합니다.

### Q3. GAA(Gate-All-Around) 구조에서 증착 공정의 난제는?
- **[A]**: [🌐 Web Search] GAA는 게이트가 채널의 4면을 모두 감싸는 구조입니다. 나노시트(Nanosheet) 사이의 좁은 틈새에 고유전율(High-k) 절연막과 금속 게이트를 균일하게 채워 넣어야 하므로, 기존 CVD로는 한계가 있으며 극한의 **ALD 기술**이 필수적입니다.

## 4. [최신 트렌드 2026 (Trends)]
- **Selective ALD**: 원하는 영역에만 선택적으로 증착하여 마스크 공정을 줄이는 차세대 기술이 활발히 연구되고 있습니다.
- **Plasma Doping (PLAD)**: 이온주입의 낮은 생산성을 극복하고 얕은 접합(Shallow Junction) 형성을 위해 플라즈마를 이용한 도핑 기술 도입이 늘고 있습니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 🏛️ Entity ion-implantation-and-doping-profile-control (Verified)
- 🏛️ 02_Knowledge/01_Semiconductor/Process/Semiconductor Ion-Implantation (Verified)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
