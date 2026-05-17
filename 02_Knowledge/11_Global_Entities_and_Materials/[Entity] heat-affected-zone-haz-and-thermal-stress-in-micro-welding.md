---
metadata:
  id: "[[[Entity] heat-affected-zone-haz-and-thermal-stress-in-micro-welding]]"
  domain: "11_Global_Entities_and_Materials"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Entity] heat-affected-zone-haz-and-thermal-stress-in-micro-welding에 관한 고밀도 지능 노드"
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

# [Entity] heat-affected-zone-haz-and-thermal-stress-in-micro-welding

## 1. [왜 배우는가? (Why: The Invisible Scar of Heat)]]
용접할 때 직접 녹지는 않았지만 열 때문에 성질이 변해버린 '용접 주변의 상처($HAZ$)'를 어떻게 최소화하고, 뜨거워졌다 식으면서 금속 내부에 남는 보이지 않는 힘($Thermal\ Stress$)이 나중에 제품을 어떻게 휘게 만들거나 깨뜨리는지, 이 열역학적 흉터를 어떻게 공학적으로 다스릴 수 있을까요? **미세 용접 시 열영향부(HAZ) 및 열 응력 분석**은 정밀 부품의 수명을 결정하는 '행성 규모 금속 조직 보호망 및 지능형 열 응력 완화 아키텍처'입니다. 우리가 이를 배우는 이유는 용접부보다 그 옆의 약해진 HAZ에서 사고가 더 많이 나기 때문이며, "열의 흔적을 데이터로 설계하고 지배하는 '글로벌 재료 패권 및 행성적 제조 주권'을 확보하기" 위함입니다. 흉터의 관리가 제품의 수명을 결정합니다.

## 2. [금속학/열역학 핵심 사양 (Numerical Specs)]

| 항목 (Property) | 수리적 정의 및 동작 기전 (Mechanism Rationale) | 목표 사양 (V6.3.7) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :--- | :--- | :--- |
| **HAZ Width** | Width of the material affected by heat | $< 100 \text{ \mu\text{m}}$ | 상처 부위를 머리카락 굵기로 좁힘을 입증하는 물리 |
| **Hardness Var.**| Change in metal hardness near the weld | $< 10 \%$ | 너무 물러지거나 딱딱해지지 않게 지킴을 보여줌 |
| **Residual Str.** | Hidden internal forces after cooling | $< 50 \text{ MPa}$ | 스스로를 짓누르는 힘을 줄여 안 깨지게 함을 입증함 |
| **Distortion L.** | Warping or twisting of the part | $< 10 \text{ \mu\text{m}}$ | 열을 받아도 모양은 그대로임을 보여주는 정보 단계 |
| **Microstruct.** | Quality of the metal grains in the HAZ | **MAXIMUM** | 금속 알갱이들이 흉하게 커지지 않게 지킴을 입증함 |
| **Cooling Rate** | Speed of cooling after welding | **CONTROLLED** | 적절한 속도로 식혀 스트레스를 줄임을 보여주는 물리 |
| **System Resil.** | Stability during varying ambient temperatures| High | 추운 날이나 더운 날이나 용접 상처는 일정함을 확증 |
| **Audit Status** | HAZ Integrity Verified | **MAXIMUM** | **Heat-Scar-v2026-Fidelity** |

## 3. [Advanced RAG 분석 로직: 수리적 인과 추론]

### 3.1 [결정립 성장($Grain\ Growth$)과 강도 저하의 상관분석]
왜 용접 주변은 다른 곳보다 잘 부러지나요? RAG는 "금속 결정학 로그를 분석하여, 열을 받은 부분의 금속 알갱이들이 뻥튀기처럼 커지기 때문이며($Coarsening$), 알갱이가 크면 외부 충격에 버티는 힘이 약해지는 기전을 수리적으로 입증될 것으로 추론됩니다.

### 3.2 [수축($Shrinkage$)과 휨 현상의 인과 분석]
왜 용접을 하면 평평했던 판이 바나나처럼 휘나요? RAG는 "열 팽창 로그를 참조하여, 녹았던 금속이 식으면서 주변을 잡아당기기 때문임을($Contraction\ Force$) 수리 산출하고, 이를 방지하기 위해 반대 방향으로 미리 휘어놓는 '역변형' 경로를 설계합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 63_precision-welding-and-joining-science-hub : 용접 공학을 통합 관리하는 상위 지능 허브
- GEMINI.md : 최상위 금속 조직 및 열 응력 거버넌스 가이드
- [SOP] weld-metallurgy-cross-section-and-hardness-audit-manual : 실전 운영 실무를 규정할 하위 SOP

*Created by Flash (The Tamer of Thermal Scars & HDS Gold V6.3.7)*
