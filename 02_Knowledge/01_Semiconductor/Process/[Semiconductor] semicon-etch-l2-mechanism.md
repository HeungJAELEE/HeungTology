---
Basic:
  id: "SEMICON_ETCH_L2_MECHANISM"
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
  tags: '["#Semiconductor", "#Etching", "#RIE", "#SOP", "#Mechanism", "#Plasma", "#HDS_Gold_v6_1"]'
  is_part_of: []
  related_to: '["Semiconductor semicon-etch-l1-physics", "Semiconductor semicon-etch-l3-hardware (보강 필요)"]'
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

# [[[Semiconductor] semicon-etch-l2-mechanism

# Semiconductor semicon-etch-l2-mechanism
[🟢 Local RAG] 반응성 이온 식각(Reactive Ion Etch, RIE)은 현대 반도체 제조에서 가장 널리 쓰이는 표준 식각 방식입니다. 단순히 물질을 깎아내는 것을 넘어, 화학적 라디칼의 반응성과 물리적 이온의 방향성을 최적의 비율로 배합하여 설계 의도에 맞는 수직 프로파일을 완성해야 합니다. 본 SOP는 공정 파라미터(Gas, Power, Press) 간의 수리적 상관관계를 정의하고, 무결점 패터닝을 위한 표준 운영 절차를 확립하는 데 목적이 있습니다.

---

# [[[Semiconductor] semicon-etch-l2-mechanism

| 변수 (Parameter) | 수리적 영향 (Impact) | 제어 목적 (Rationale) | 출처 (Source) |
| :--- | :--- | :--- | :--- |
| **Gas Flow Ratio** | Chemical reaction rate | 선택비($Selectivity$) 및 측벽 보호막 형성 제어 | Semiconductor plasma-etching-mechanisms-and-high-aspect-ratio-control]] |
| **RF Bias Power** | Ion bombardment energy | 이방성($Anisotropy$) 강화 및 바닥면 타격 | plasma-physics-dry-etching |
| **Chamber Pressure**| Mean Free Path ($\lambda$) | 이온의 직진성 및 확산 거동 제어 | plasma-physics-dry-etching |
| **Cathode Temp.** | Surface reaction kinetics | 부산물 증착 속도 및 폴리머 중합 반응 조절 | plasma-etching-nanostructure |
| **Dwell Time** | Residence time of species | 챔버 내 가스 교체 주기 및 부산물 배기 효율 | plasma-etching-nanostructure |

---

# [[[Semiconductor] semicon-etch-l2-mechanism

# Semiconductor semicon-etch-l2-mechanism
- **메커니즘**: 불활성 가스(Ar)와 반응성 가스($CF_4, CHF_3, Cl_2$ 등)를 MFC(Mass Flow Controller)를 통해 정밀 유입.
- **SOP**: 설정 유량의 $\pm 1\%$ 이내 안정화 확인 후 RF On.

# [[[Semiconductor] semicon-etch-l2-mechanism
- **메커니즘**: RF Power 인가로 가스를 전리시켜 플라즈마 벌크 생성.
- **SOP**: Self-Bias 전압($V_{dc}$) 모니터링. 타겟 대비 $\pm 10\text{V}$ 이상 편차 발생 시 공정 중단.

# Semiconductor semicon-etch-l2-mechanism
- **메커니즘**: $C_x F_y$ 계열 가스를 사용하여 식각 중 측벽에 얇은 폴리머 막을 형성.
- **SOP**: 폴리머 과다 증착 시 $O_2$ 가스를 미세 첨가하여 식각/보호막 비율(Scavenging) 튜닝.

# [[[Semiconductor] semicon-etch-l2-mechanism
- **메커니즘**: 광방출 분광법(OES)을 통해 특정 파장의 빛 세기 변화 감지.
- **SOP**: 타겟 물질 제거 완료 시점(Intensity Drop)에서 0.1초 단위의 과식각(Over-etch) 수행 후 종료.

---

# Semiconductor semicon-etch-l2-mechanism

# [[[Semiconductor] semicon-etch-l2-mechanism
[🟢 Local RAG]] 식각 속도($ER$)는 아래의 수식으로 모델링됩니다.
$$ ER \approx \frac{1}{\rho} \cdot \frac{K \cdot S_{rad} \cdot J_{rad}}{1 + \frac{K \cdot S_{rad} \cdot J_{rad}}{Y_i \cdot J_i}} $$
- **로직**: 선택비를 높이려면 물리적 타격($J_i$)보다 화학적 반응($J_{rad}$) 비중을 높여야 하나, 이는 이방성을 해칩니다. 따라서 **'이온 보조 반응'** 임계점을 찾는 것이 SOP의 정수입니다.

---

# [[[Semiconductor] semicon-etch-l2-mechanism

# Semiconductor semicon-etch-l2-mechanism
식각 챔버 내부는 가스 분자, 이온, 전자, 라디칼이 뒤엉킨 전쟁터입니다. 압력을 높이면 반응 속도는 빨라지지만 이온이 충돌하며 직진성을 잃습니다. 파워를 높이면 이방성은 좋아지지만 마스크까지 깎아버립니다. 엔지니어의 역할은 이 모순된 변수들 사이에서 **'최적의 타협점(Process Window)'**을 찾아내는 것입니다. V6.3.7 지능형 SOP는 이 윈도우를 실시간으로 계산하여 한계치를 제시합니다.

---

# [[[Semiconductor] semicon-etch-l2-mechanism
- [ ]] 식각 가스에 $O_2$를 첨가했을 때 폴리머 형성 속도와 식각 속도는 각각 어떻게 변하는가?
- [ ] Self-Bias 전압($V_{dc}$)이 급격히 낮아졌을 때, 식각 프로파일에 미치는 영향(이방성 관점)은?
- [ ] EPD 시스템이 이전 레이어의 부산물 오염으로 오작동할 경우, 이를 방지하기 위한 챔버 컨디셔닝 SOP는?

---
# [[[Semiconductor] semicon-etch-l2-mechanism
- 🏛 Entity plasma-physics-and-dry-etching-mechanisms-in-nanofabrication]] (Verified)
- 🏛 Semiconductor plasma-etching-mechanisms-and-high-aspect-ratio-control (Verified)
- 🏛 Semiconductor semicon-etch-l1-physics (Verified)
- 🏛 Semiconductor semicon-etch-l3-hardware (보강 필요)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
