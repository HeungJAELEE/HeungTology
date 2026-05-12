---
Basic:
  id: "INTERVIEW_SEMICON_02_OXIDATION"
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
  tags: '["#Interview", "#Semiconductor", "#Oxidation", "#Deal_Grove", "#HDS_Gold_v6_1"]'
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

# [[[Semiconductor] 8대공정_02_산화

## 1. [왜 중요한가? (Why): 완벽한 절연의 사수]]
[🟢 Local RAG] 산화 공정은 고온($800 \sim 1,200^\circ\text{C}$)에서 산소나 수증기를 웨이퍼 표면에 반응시켜 얇고 균일한 실리콘 산화막($SiO_2$)을 형성하는 공정입니다. 이 산화막은 소자 간의 **누설 전류 차단(Isolation)**, **이온주입 마스크**, 그리고 **게이트 절연막** 역할을 수행합니다. 산화막의 두께와 밀도 무결성이 깨지면 반도체의 신뢰성(Reliability)은 즉각 붕괴됩니다.

## 2. [핵심 메커니즘 (Mechanism)]
### 2.1 Deal-Grove Model (딜-그로브 모델)
[🟢 Local RAG] 산화막 성장 속도를 결정하는 수리적 모델입니다.
- **선형 성장 (Linear)**: 초기에 산화막이 얇을 때는 산화제와 실리콘 표면의 **계면 반응 속도**가 성장을 지배합니다.
- **포물선 성장 (Parabolic)**: 산화막이 두꺼워지면 산화제가 기존 막을 뚫고 지나가는 **확산 속도**가 성장을 제약합니다 ($x_o \propto \sqrt{t}$).
- **건식 vs 습식**: 건식($O_2$)은 막질이 우수하지만 속도가 느리고, 습식($H_2O$)은 속도는 빠르나 막질이 다소 성깁니다.

## 3. [면접 빈출 질문 Top 3 (Q&A)]

### Q1. 건식 산화와 습식 산화의 차이점을 설명하고, 각각 언제 사용하나요?
- **[A]**: [🟢 Local RAG] 건식은 산소 분자를 사용하여 속도는 느리지만 **치밀한 막질**을 얻을 수 있어 **게이트 산화막**과 같이 얇고 정밀한 막에 사용합니다. 습식은 물 분자를 사용하여 **성장 속도가 5~10배 빠르지만** 막질이 비교적 성겨서, 두꺼운 막이 필요한 **필드 산화막(STI 등)**에 주로 사용합니다.

### Q2. 딜-그로브 모델에서 초기 성장이 이론값보다 빠른 이유(Massoud 모델)는 무엇인가?
- **[A]**: [🟢 Local RAG] 초박막 영역($< 25\text{nm}$)에서는 실리콘 표면의 **강한 응력(Stress)**과 **잉여 전하**들이 산화제 분자의 해리를 촉진하기 때문입니다. 이는 나노 공정에서 게이트 산화막 두께를 제어할 때 반드시 보정해야 할 핵심 변수입니다.

### Q3. 열산화(Thermal Oxidation) 대신 증착(CVD)을 사용하여 산화막을 형성하는 경우는?
- **[A]**: [🌐 Web Search] 열산화는 실리콘 기판을 직접 소모하므로 기판의 단차가 생길 수 있고, 고온 공정이므로 이전 단계에 형성된 불순물 프로파일을 망가뜨릴 수 있습니다. 따라서 **기판 소모 방지**가 필요하거나 **저온 공정**이 필수적인 금속 배선 층 사이의 절연막(IMD) 등에는 CVD 방식을 사용합니다.

## 4. [최신 트렌드 2026 (Trends)]
- **High-k 소재 도입**: 2nm 이하 공정에서는 $SiO_2$의 두께 한계로 인한 터널링 효과를 막기 위해 하프늄($HfO_2$)과 같은 고유전율(High-k) 소재를 원자층 증착(ALD)과 병행하여 사용하며, 산화 공정은 기판과의 계면 특성을 개선하는 **Interface Layer** 형성용으로 최적화되고 있습니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 🏛️ Battery oxidation-kinetics-deal-grove-model (Verified)
- 🏛️ 02_Knowledge/01_Semiconductor/Process/Semiconductor thermal-oxidation-process-sop (보강 필요)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
