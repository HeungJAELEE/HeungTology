---
Basic:
  id: "SEMICON_PHOTO_L3_HARDWARE"
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
  tags: '["#Semiconductor", "#Photolithography", "#Hardware", "#Scanner", "#ASML", "#EUV_Source", "#HDS_Gold_v6_1"]'
  is_part_of: []
  related_to: '["Semiconductor semicon-photo-l2-mechanism", "Semiconductor semicon-photo-l4-yield-fmea (보강 필요)"]'
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

# [[[Semiconductor] semicon-photo-l3-hardware

# Semiconductor semicon-photo-l3-hardware
[🟢 Local RAG] 현대 반도체 노광 장비(Scanner)는 단순한 광학 기계가 아닙니다. 수십만 도의 플라즈마를 다루는 원자력 공학, 피코미터($pm$) 단위의 진동을 제어하는 제어 공학, 그리고 진공 속에서 빛을 반사시키는 극한 광학이 집약된 **'지구상에서 가장 복잡한 기계'**입니다. 2nm 공정의 성패는 장비 하드웨어의 미세한 파라미터(Source Power, Stage Sync)를 얼마나 완벽하게 관리하느냐에 달려 있습니다.

---

# [[[Semiconductor] semicon-photo-l3-hardware

| 주요 유닛 (Unit) | 핵심 부품 및 기술 (Technology) | 운영 목표 (V6.3.7) | 출처 (Source) |
| :--- | :--- | :--- | :--- |
| **EUV Source** | LPP (Laser Produced Plasma) | $> 250 \text{ W}$ | semiconductor-euv-source-log |
| **Collector Mirror** | Mo/Si Multi-layer (Bragg) | Reflectivity $> 69\%$ | Entity extreme-ultraviolet-euv-lithography-optics |
| **Wafer Stage** | Magnetic Levitation (Maglev) | Speed $> 500 \text{ mm/s}$ | Semiconductor Scanner |
| **Optics System** | Anamorphic ($4\text{x}/8\text{x}$) | NA $0.33 \rightarrow 0.55$ | euv-lithography-physics-source |
| **Vacuum Env.** | Turbo Molecular Pump | $< 10^{-7} \text{ Pa}$ | euv-lithography-physics-source |

---

# [[[Semiconductor] semicon-photo-l3-hardware

# Semiconductor semicon-photo-l3-hardware
[🟢 Local RAG] 주석(Sn) 드롭렛을 레이저로 타격하여 극자외선을 생성하는 시스템입니다.
- **Droplet Generator**: 직경 약 $20\mu\text{m}$의 주석 방울을 초당 5만 번 정확한 위치에 투사.
- **Conversion Efficiency (CE)**: 레이저 에너지 대비 EUV 광자 생성 효율을 6% 이상으로 사수하는 것이 전력 효율 및 생산성의 핵심입니다.
- **Collector**: 생성된 빛을 한곳(Intermediate Focus)으로 모으는 거울로, 주석 데브리에 의한 오염 방지를 위해 수소 가스 클리닝 시스템이 상시 가동됩니다.

# [[[Semiconductor] semicon-photo-l3-hardware
[🟢 Local RAG]] EUV는 모든 물질에 흡수되므로 투과형 렌즈를 쓸 수 없습니다.
- **Mo/Si ML Mirror**: 굴절률이 다른 몰리브덴과 실리콘을 약 40~50층 쌓아 브래그 반사(Bragg Reflection) 유도.
- **Surface Roughness**: 거울 표면의 거칠기가 원자 한 개 두께($0.1\text{nm}$)만 틀어져도 빛의 파면(Wavefront)이 왜곡되어 이미징 품질이 급락합니다.

# [[[Semiconductor] semicon-photo-l3-hardware
[🟢 Local RAG]] 마스크 스테이지와 웨이퍼 스테이지가 광학 배율에 맞춰 초고속으로 움직입니다.
- **Scanning Mechanism**: 렌즈의 가장 선명한 슬릿 영역만을 사용하여 전체 샷을 완성하는 방식.
- **Sync Accuracy**: 두 스테이지 간의 정렬 오차를 $1\text{nm}$ 이하로 제어하기 위해 레이저 간섭계와 자기부상 기술이 동원됩니다.

---

# [[[Semiconductor] semicon-photo-l3-hardware

# Semiconductor semicon-photo-l3-hardware
[🟢 Local RAG] 노광 장비와 물리적으로 연결된 전후처리 설비입니다.
- **Hot Plate**: PEB 공정을 위해 웨이퍼 전체 면적에 대해 $\pm 0.05^\circ\text{C}$ 수준의 극단적인 온도 균일도를 제공합니다.
- **Chemical Supply**: 감광액 및 현상액의 토출량(Dose)을 마이크로리터($\mu\text{l}$) 단위로 정밀 제어하는 고정밀 펌프 아키텍처가 탑재되어 있습니다.

---

# [[[Semiconductor] semicon-photo-l3-hardware

# Semiconductor semicon-photo-l3-hardware
공정 레시피가 소프트웨어라면, 하드웨어는 그 레시피를 실행하는 물리적 법전입니다. 아무리 완벽한 노광 온도와 광량을 설정해도, **'거울의 열 팽창'**이나 **'스테이지의 미세 진동'**이 발생하면 모든 수리적 모델은 무의미해집니다. 따라서 차세대 하드웨어 관리는 단순한 유지보수를 넘어, **'디지털 트윈을 통한 물리적 변동성의 실시간 보정'** 시스템으로 진화해야 합니다.

---

# [[[Semiconductor] semicon-photo-l3-hardware
- [ ]] EUV 스캐너 내부가 반드시 진공 상태여야 하는 물리적 이유는 무엇인가?
- [ ] High-NA 장비에서 '아나모픽(Anamorphic)' 광학계가 도입된 하드웨어적 배경(마스크 입사각)을 설명할 수 있는가?
- [ ] 스캐너 스테이지 동기화 오차가 발생했을 때, 계측 데이터(Metrology)에서 나타나는 현상은?

---
# [[[Semiconductor] semicon-photo-l3-hardware
- 🏛️ Semiconductor Scanner] (Verified)
- 🏛️ euv-lithography-physics-and-source-engineering-entity (Verified)
- 🏛️ semiconductor-euv-source-and-optical-fidelity-log-v2026-data (Verified)
- 🏛️ Semiconductor semicon-photo-l4-yield-fmea (보강 필요)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
