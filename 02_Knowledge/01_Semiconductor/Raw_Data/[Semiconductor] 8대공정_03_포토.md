---
Basic:
  id: "INTERVIEW_SEMICON_03_PHOTOLITHOGRAPHY"
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
  tags: '["#Interview", "#Semiconductor", "#Photolithography", "#EUV", "#HDS_Gold_v6_1"]'
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

# [[[Semiconductor] 8대공정_03_포토

## 1. [왜 중요한가? (Why): 빛의 조각술]]
[🟢 Local RAG] 포토 공정은 웨이퍼 위에 회로 설계가 담긴 마스크의 패턴을 빛을 이용해 전사하는 공정입니다. 반도체의 집적도를 결정하는 핵심이자, 전체 제조 비용의 30% 이상, 공정 시간의 상당 부분을 차지하는 **가장 결정적인 병목(Bottleneck)** 공정입니다. 선폭(CD) 제어 실패는 곧 칩 성능과 수율의 직결된 실패를 의미합니다.

## 2. [핵심 메커니즘 (Mechanism)]
### 2.1 Rayleigh Criterion (레이일리 공식)
[🟢 Local RAG] 해상도($R$)와 공정 변수 사이의 관계를 정의합니다.
$$ R = k_1 \frac{\lambda}{NA} $$
- **해상도 개선 방법**: 파장($\lambda$)을 줄이거나(EUV 도입), 렌즈 성능($NA$)을 높이거나(High-NA), 공정 계수($k_1$)를 최적화해야 합니다.
- **EUV (Extreme Ultraviolet)**: $13.5\text{nm}$의 짧은 파장을 사용하여 기존 ArF($193\text{nm}$) 대비 미세 패턴 형성에 유리하지만, 모든 물질에 흡수되는 성질 때문에 **반사형 광학계**를 사용합니다.

## 3. [면접 빈출 질문 Top 3 (Q&A)]

### Q1. EUV 공정에서 마스크가 기존과 다른 점은 무엇인가요?
- **[A]**: [🟢 Local RAG] 기존 마스크는 빛을 투과시키는 방식이었으나, EUV는 모든 물질에 흡수되므로 몰리브덴(Mo)과 실리콘(Si)을 교대로 쌓은 **다층막(Multi-layer) 반사 마스크**를 사용합니다. 또한, 빛이 거울에 반사될 때의 각도(Chief Ray Angle)에 의한 **그림자 효과(Shadowing Effect)**를 보정하는 디자인이 필수적입니다.

### Q2. 포토 공정의 3대 지표인 Resolution, DOF, Overlay에 대해 설명하시오.
- **[A]**: [🟢 Local RAG] **Resolution**은 그릴 수 있는 최소 선폭입니다. **DOF(초점심도)**는 회로가 선명하게 찍히는 수직적 깊이의 범위이며, 고해상도일수록 DOF가 좁아져 공정 난도가 상승합니다. **Overlay**는 적층된 각 층간의 정렬 정밀도로, 2nm 공정에서는 원자 몇 개 수준의 오차($< 2\text{nm}$)만을 허용합니다.

### Q3. High-NA EUV가 왜 필요하며, 어떤 변화가 있나요?
- **[A]**: [🌐 Web Search] 기존 $0.33$ NA 장비로는 2nm 이하 단일 노광(Single Patterning)이 어렵습니다. **High-NA($0.55$ NA)**는 렌즈의 크기를 키워 해상도를 비약적으로 높인 장비입니다. 이로 인해 칩 설계 시 배율(Magnification)이 비대칭으로 변하는 등 설계와 공정 전반의 혁신이 필요합니다.

## 4. [최신 트렌드 2026 (Trends)]
- **PR 혁신**: 기존 유기 PR에서 감도가 높고 패턴 무너짐이 적은 **MOR (Metal Oxide Photoresist)**로의 전환이 선단 공정의 핵심 과제입니다.
- **Pellicle 국산화**: EUV 마스크의 오염을 막는 투과율 90% 이상의 고내열성 펠리클(Pellicle) 양산 적용이 수율 확보의 관건입니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 🏛️ Entity photolithography-and-asml-euv-optics-physics (Verified)
- 🏛️ 02_Knowledge/entities/Entity photolithography-mask-design-and-optical-proximity-correction-opc (Verified)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
