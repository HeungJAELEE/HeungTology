---
Basic:
  id: "SEMICON_ETCH_L3_HARDWARE"
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
  tags: '["#Semiconductor", "#Etching", "#Hardware", "#ICP", "#CCP", "#RF_Matcher", "#ESC", "#HDS_Gold_v6_1"]'
  is_part_of: []
  related_to: '["Semiconductor semicon-etch-l2-mechanism", "Semiconductor semicon-etch-l4-yield-fmea (보강 필요)"]'
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

# [[[Semiconductor] semicon-etch-l3-hardware

# Semiconductor semicon-etch-l3-hardware
[🟢 Local RAG] 식각 설비는 고진공 상태에서 수천 와트의 전력을 인가하여 인위적으로 '벼락(플라즈마)'을 가두고 다스리는 장치입니다. 플라즈마의 밀도($n_e$)와 이온 에너지($E_i$)를 독립적으로 제어하기 위한 ICP/CCP 아키텍처와, 웨이퍼를 0.1도 단위로 냉각하는 ESC(정전척) 기술은 선단 공정 수율의 물리적 기반입니다. 설비 하드웨어의 무결성을 이해하는 것은 공정 드리프트를 방지하고 장비 가동률을 극대화하는 엔지니어의 숙명입니다. Semiconductor semicon-troubleshoot-etching-plasma

---

# [[[Semiconductor] semicon-etch-l3-hardware

| 주요 유닛 (Unit) | 핵심 부품 및 기술 | 운영 목표 (V6.3.7) | 출처 (Source) |
| :--- | :--- | :--- | :--- |
| **Plasma Source** | ICP (Inductive) / CCP (Capacitive) | Density $10^{10} \sim 10^{12} \text{ cm}^{-3}$ | Semiconductor Etching] |
| **RF Generator** | 13.56 MHz / Multi-frequency | Power stability $< \pm 1\%$ | Semiconductor semicon-troubleshoot-etching-plasma |
| **RF Matcher** | Auto-impedance matching | Reflected Power $< 1\%$ | Semiconductor semicon-troubleshoot-etching-plasma |
| **ESC (Chuck)** | Electrostatic Attraction & Helium Cooling | Temp unif. $\pm 0.1^\circ\text{C}$ | Semiconductor semicon-troubleshoot-etching-plasma |
| **Turbo Pump** | High-vacuum evacuation | Pressure $1 \sim 100 \text{ mTorr}$ | Semiconductor Etching |

---

# [[[Semiconductor] semicon-etch-l3-hardware

# Semiconductor semicon-etch-l3-hardware
[🟢 Local RAG] 두 개의 평행 전극판 사이에 고주파 전력을 인가하여 플라즈마를 형성하는 방식입니다.
- **특징**: 구조가 단순하고 대면적 균일도가 우수하지만, 플라즈마 밀도와 이온 에너지를 독립적으로 조절하기 어렵습니다. Semiconductor Etching
- **주요 용도**: 이온 타격 에너지가 중요한 산화막(Oxide) 식각 공정에 주로 사용됩니다.

# [[[Semiconductor] semicon-etch-l3-hardware
[🟢 Local RAG]] 챔버 외벽의 안테나 코일에 전류를 흘려 유도 자기장을 발생시키고, 이로 인해 형성된 전기장으로 가스를 전리시키는 방식입니다.
- **장점**: 고밀도 플라즈마($> 10^{12} \text{ cm}^{-3}$) 생성이 가능하며, 소스 파워(밀도 제어)와 바이어스 파워(에너지 제어)를 **독립적으로 제어**할 수 있습니다. Semiconductor Etching
- **주요 용도**: 미세 패턴의 폴리실리콘 및 금속 식각에 필수적입니다.

---

# [[[Semiconductor] semicon-etch-l3-hardware

# Semiconductor semicon-etch-l3-hardware
[🟢 Local RAG] 전원 공급 장치와 플라즈마 부하 사이의 임피던스를 일치시켜 전력 전달 효율을 극대화합니다.
- **물리적 신호**: 반사 전력(Reflected Power)이 급격히 상승하면 매처의 가변 캐패시터 모터 결함이나 케이블 손상을 의심해야 합니다. Semiconductor semicon-troubleshoot-etching-plasma

# [[[Semiconductor] semicon-etch-l3-hardware
[🟢 Local RAG]] 정전기력을 이용해 웨이퍼를 고정하고, 뒷면에 헬륨($He$) 가스를 흘려 열을 배출합니다.
- **냉각 무결성**: ESC의 에지 링(Edge Ring) 소모나 헬륨 누설은 웨이퍼 가장자리의 온도 상승을 유발하여 식각률 불균일 및 아킹(Arcing)의 주원인이 됩니다. Semiconductor semicon-troubleshoot-etching-plasma

---

# [[[Semiconductor] semicon-etch-l3-hardware

# Semiconductor semicon-etch-l3-hardware
식각 장비는 단순한 용기가 아니라 **'에너지의 조각 도구'**입니다. 2nm 공정으로 갈수록 이온의 입사 각도 산포($\Delta\theta$)를 $1^\circ$ 이내로 좁혀야 하며, 이를 위해 하드웨어는 **'다중 주파수 중첩(Multi-freq superposition)'**과 **'고속 펄스 바이어스'** 기술을 통해 플라즈마의 파동을 나노초 단위로 제어하는 지능형 물리 머신으로 진화하고 있습니다.

---

# [[[Semiconductor] semicon-etch-l3-hardware
- [ ]] ICP 설비에서 소스 파워와 바이어스 파워를 독립적으로 제어할 수 있는 구조적 이유는? Semiconductor Etching
- [ ] RF Matcher가 정합에 실패하여 반사 전력이 증가할 때, 플라즈마 벌크 내의 이온 밀도는 어떻게 변하겠는가? Semiconductor semicon-troubleshoot-etching-plasma
- [ ] ESC 하부의 헬륨 압력이 불안정할 때, 웨이퍼 전면의 식각 균일도(Uniformity)에 미치는 영향은? Semiconductor semicon-troubleshoot-etching-plasma

---
# [[[Semiconductor] semicon-etch-l3-hardware
- Semiconductor Etching]
- Semiconductor semicon-troubleshoot-etching-plasma
- Semiconductor semicon-etch-l2-mechanism (Verified)
- Semiconductor semicon-etch-l4-yield-fmea (보강 필요)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
