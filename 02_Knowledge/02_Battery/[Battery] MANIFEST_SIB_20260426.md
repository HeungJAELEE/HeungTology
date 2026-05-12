---
Basic:
  id: "BAT-MANIFEST-SIB-2026-V6"
  domain: "02_Battery"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#SIB'
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

# [[[Battery] MANIFEST_SIB_20260426

## 1. [왜 이 명세서가 중요한가? (Why)]]
나트륨 이온 배터리(Sodium-ion Battery, SIB)는 리튬 대비 풍부한 자원 매장량과 저렴한 원가 경쟁력을 바탕으로 차세대 ESS(에너지 저장 장치) 및 보급형 전기차 시장의 게임 체인저로 주목받고 있습니다. 본 매니페스트는 SIB의 핵심 소재인 하드 카본(Hard Carbon)의 메커니즘, 나트륨 이온($Na^+$)의 확산 동역학, 그리고 알루미늄 집전체 사용에 따른 경제적 이점 등을 총체적으로 관리하는 지식의 뿌리입니다. 파편화된 SIB 연구 데이터를 통합하여 RAG 엔진이 최적의 전략적 통찰을 도출할 수 있도록 돕는 '시맨틱 앵커(Semantic Anchor)' 역할을 수행합니다.

## 2. [SIB vs LIB 핵심 기술 비교 사양 (Numerical Specs)]

| Parameter Category | Lithium-ion (LIB) | Sodium-ion (SIB) | Engineering Rationale |
|:---|:---:|:---:|:---|
| **Raw Material Cost** | High (Li Carbonate) | **Very Low (NaCl)** | 나트륨의 풍부한 매장량에 따른 원가 절감 |
| **Energy Density** | $240 \sim 300 \text{ Wh/kg}$ | $140 \sim 160 \text{ Wh/kg}$ | 질량당 밀도는 낮으나 부피당 효율 개선 중 |
| **Anode Material** | Graphite | **Hard Carbon** | 나트륨 이온의 큰 반경을 수용하는 층간 구조 |
| **Current Collector** | Cu (Anode), Al (Cathode) | **Al (Both)** | 나트륨은 알루미늄과 합금화되지 않아 원가 절감 |
| **0V Discharge** | Dangerous (Cu diss.) | **Possible (Safe)** | 전압을 0V까지 낮춰도 손상 없어 운송 안정성 확보 |
| **Ionic Conductivity**| High ($Li^+$) | Lower ($Na^+$) | 이온 반경($1.02 \text{ \AA}$ vs $0.76 \text{ \AA}$) 차이 |
| **Temp Range** | $-20 \sim 60^\circ\text{C}$ | **$-40 \sim 80^\circ\text{C}$** | 저온 환경에서의 우수한 출력 유지 성능 |
| **Cycle Life** | $2,000 \sim 4,000$ Cycles | $3,000 \sim 5,000$ Cycles | 하드 카본의 구조적 안정성에 따른 장수명 가능성 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 나트륨 이온 확산 동역학 (Diffusion Kinetics)
나트륨 이온은 리튬보다 크고 무거워 전해액 및 전극 내 이동 속도가 느립니다.
- **수식**: $D_{Na^+} = \frac{k_B T}{6\pi \eta r}$ (Stokes-Einstein Relation)
- **의미**: 반경($r$)이 클수록 확산 계수($D$)가 작아지므로, 이를 극복하기 위해 전해액의 점도($\eta$)를 낮추거나 하드 카본의 층간 거리($d_{002}$)를 넓히는 설계가 필수적입니다.

### 3.2 하드 카본(Hard Carbon)의 'Pore Filling' 메커니즘
흑연과 달리 하드 카본은 무질서한 층상 구조와 미세 기공(Micropore)을 가집니다.
- **로직**: 나트륨 이온은 층간 삽입(Intercalation)뿐만 아니라 미세 기공을 채우는(Filling) 방식으로 저장됩니다. 이는 SIB 특유의 낮은 전압 평탄부(Voltage Plateau)를 형성하여 고용량을 구현합니다.

### 3.3 알루미늄 집전체와 0V 안정성
리튬은 저전위에서 알루미늄과 합금(Al-Li)을 형성하여 집전체를 파괴하지만, 나트륨은 알루미늄과 반응하지 않습니다. 따라서 음극에도 저렴한 알루미늄 박을 사용할 수 있으며, 완전 방전(0V) 상태로 안전하게 보관 및 운송이 가능합니다.

## 4. [코드 연결 해설 (SIB vs LIB Performance & Cost Analyzer)]
아래 코드는 소재 사양과 공정 비용을 바탕으로 SIB와 LIB의 단위당 에너지 비용($\$/kWh$)을 비교 시뮬레이션하는 로직입니다.

```python
class SIBvsLIBAnalyzer:
    """
    HDS-Gold V6.3.7 규격의 배터리 시스템 경제성 분석 엔진
    """
    def __init__(self, li_price, na_price, cu_price, al_price):
        self.prices = {'Li': li_price, 'Na': na_price, 'Cu': cu_price, 'Al': al_price}

    def compare_unit_cost(self, energy_density_lib, energy_density_sib):
        """
        에너지 밀도 대비 총 원가 분석
        """
        # LIB 원가: 리튬 + 구리(음극) + 알루미늄(양극)
        cost_lib = (self.prices['Li'] * 0.15 + self.prices['Cu'] * 0.2 + self.prices['Al'] * 0.1) / energy_density_lib
        
        # SIB 원가: 나트륨 + 알루미늄(양쪽)
        cost_sib = (self.prices['Na'] * 0.05 + self.prices['Al'] * 0.2) / energy_density_sib
        
        reduction_ratio = (cost_lib - cost_sib) / cost_lib
        
        return {
            "lib_cost_per_wh": cost_lib,
            "sib_cost_per_wh": cost_sib,
            "cost_reduction_percent": reduction_ratio * 100
        }

# Example Usage:
# analyzer = SIBvsLIBAnalyzer(li_price=30000, na_price=500, cu_price=8000, al_price=2500)
# comparison = analyzer.compare_unit_cost(250, 150)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Hard Carbon**의 층간 거리($d_{002}$)가 **$0.37 \text{ nm}$** 이상이어야 나트륨 이온이 원활하게 삽입될 수 있는 결정학적 근거는?
2. SIB에서 **NaPF6** 염이 **LiPF6** 대비 전해액의 '이온 전도도'와 '고온 안정성' 측면에서 가지는 장단점은?
3. $0\text{V}$ 완전 방전 상태로 운송 시, SIB 셀 내부의 화학적 평형 상태와 재충전 시의 **ICE** (초기 쿨롱 효율) 변화 가능성은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Materials/Battery Anode
- 02_Knowledge/02_Battery/Materials/Battery Cathode
- 02_Knowledge/02_Battery/Intelligence/Battery formation-and-sei-kinetics

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**