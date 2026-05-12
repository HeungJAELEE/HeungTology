---
Basic:
  id: "BAT-MAT-SODIUM-ION-2026-V6"
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
  tags: - '#Sodium_Ion_Battery'
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

# [[[Battery] sodium-ion-battery-technology-entity

## 1. [왜 배우는가? (Why)]]
에너지 저장 시장은 현재 리튬($Li$)에 극도로 의존하고 있으나, 리튬의 매장량 한계와 지정학적 편중은 공급망의 심각한 불안정성을 초래합니다. 반면 나트륨($Na$)은 소금의 주성분으로 지구 어디에나 존재하며 리튬보다 약 80배나 저렴합니다. 나트륨 이온 배터리(SIB)를 배우는 이유는 단순히 '저가형 배터리'를 넘어, 혹한기에서도 우수한 성능을 유지하고 $0V$ 완전 방전 상태로 안전하게 운송할 수 있는 독보적인 물리적 특성을 활용하여, 리튬의 지정학적 한계를 극복하고 에너지 자립권을 확보하기 위함입니다.

## 2. [나트륨 이온 배터리 성능 및 소재 핵심 사양 (SIB Specs)]

| Parameter Category | Specific Metric | SIB (Sodium-ion) | LIB (LFP 기준) | Engineering Rationale |
|:---|:---|:---:|:---:|:---|
| **Ionic Radius** | $Na^+ / Li^+$ | **$1.02 \text{ \AA}$** | $0.76 \text{ \AA}$ | 나트륨 이온의 거대 크기로 인한 격자 스트레스 제어 |
| **Std. Potential** | vs $SHE$ (V) | **$-2.71 \text{ V}$** | $-3.04 \text{ V}$ | 리튬 대비 약 $0.3V$ 낮은 셀 작동 전압의 근거 |
| **Energy Density** | Gravimetric | $100 \sim 160 \text{ Wh/kg}$| $140 \sim 190 \text{ Wh/kg}$| LFP의 약 $80\%$ 수준까지 추격한 고밀도 지표 |
| **Anode Collector** | Material | **Aluminum ($Al$)** | Copper ($Cu$) | **음극 집전체 소재 비용 $15\%$ 이상 절감 가능** |
| **Low-temp Perf.** | at $-20\text{ }^\circ\text{C}$ | **$\sim 90\%$** | $\sim 70\%$ | 낮은 탈용매화 에너지에 의한 혹한기 성능 우위 |
| **Safety Discharge**| Voltage (V) | **$0.0 \text{ V}$** | $\sim 2.5 \text{ V}$ | 안전 방전을 통한 보관 및 운송 무결성 확보 |
| **Ionic Cond.** | Electrolyte | $8 \sim 12 \text{ mS/cm}$ | $10 \sim 14 \text{ mS/cm}$ | 전해액 내 이온 이동 속도 및 급속 충전 잠재력 |
| **Cycle Life** | at $80\%$ DoD | $2,000 \sim 4,000$ | $3,000 \sim 5,000$ | 수명 주기 동안의 경제적 가용성 지표 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 하드 카본(Hard Carbon)의 층간 구조와 삽입 역학
나트륨 이온의 거대 반경을 수용하기 위한 필수 선택입니다.
- **로직**: 나트륨 이온은 흑연(Graphite)의 좁은 층간 간격($3.35 \text{ \AA}$)을 통과하기 어렵습니다. 따라서 층간 거리가 넓고 배열이 무질서한 하드 카본을 음극재로 사용합니다. 이 무질서한 틈(Pores)과 넓은 층간 간격은 나트륨 이온에게 자유로운 이동 통로를 제공하여, 고출력 성능을 구현하고 리튬 플레이팅과 유사한 나트륨 석출(Sodium Plating) 리스크를 완화합니다.

### 3.2 알루미늄 집전체(Current Collector)의 경제적 파괴력
- **로직**: 리튬 배터리에서는 리튬이 낮은 전위에서 알루미늄과 합금을 형성하여 녹아버리기 때문에 음극에 비싼 구리($Cu$) 박을 써야 합니다. 반면 나트륨은 알루미늄과 합금을 형성하지 않아 음극에도 저렴한 알루미늄 박을 사용할 수 있습니다. 이를 통해 배터리 원가의 약 $10\%$를 즉각적으로 걷어낼 수 있으며, 구리보다 가벼운 알루미늄의 특성상 무게 효율도 개선됩니다.

### 3.3 낮은 탈용매화 에너지(Desolvation Energy)와 저온 특성
- **로직**: 추운 날씨에 리튬 이온은 전해액 용매 옷을 벗고 전극 내부로 침투하는 데 큰 에너지가 필요합니다. 나트륨 이온은 이 탈용매화 에너지가 리튬보다 상대적으로 낮아, 영하 $20^\circ\text{C}$ 이하의 극한 환경에서도 이온 전도성을 높게 유지하며 높은 용량 유지율($\sim 90\%$)을 보입니다.

## 4. [코드 연결 해설 (SibPerformanceOptimizer)]
아래 코드는 소재별 비용과 에너지 밀도를 기반으로 나트륨 이온 배터리의 경제적 타당성(ROI)을 리튬 배터리와 비교하여 분석하는 엔진입니다.

```python
import numpy as np

class SibPerformanceOptimizer:
    """
    HDS-Gold V6.3.7 규격의 나트륨 이온 배터리 경제성 및 성능 분석 엔진
    """
    def __init__(self, li_price_idx=1.0, na_price_idx=0.1):
        self.li_price = li_price_idx
        self.na_price = na_price_idx
        self.base_cost_kwh = 100 # USD

    def compare_cost_advantage(self, tech='SIB'):
        """
        SIB와 LIB의 시스템 단가 및 소재 비용 비교
        """
        # Transitional Bridge: 나트륨 배터리는 '가난한 자의 리튬 전지'가 아닙니다. 
        # 알루미늄 집전체와 흔한 나트륨 소스는 소재 비용의 30%를 
        # 즉각 절감하며, $0V$ 운송은 물류비용의 패러다임을 바꿉니다.
        if tech == 'SIB':
            # 알루미늄 음극 집전체 적용으로 인한 비용 절감 효과 반영
            cost = self.base_cost_kwh * (0.6 + self.na_price * 0.1)
            transport_bonus = 5.0 # 0V 안전 방전 보너스
            return round(cost - transport_bonus, 2)
        return round(self.base_cost_kwh * self.li_price, 2)

    def estimate_energy_density(self, cathode_type='PBA'):
        """
        양극재 타입별 예상 에너지 밀도(Wh/kg) 산출
        """
        densities = {'PBA': 150, 'Polyanion': 130, 'LayeredOxide': 165}
        return densities.get(cathode_type, 140)

# Example Usage:
# optimizer = SibPerformanceOptimizer(li_price_idx=1.5, na_price_idx=0.15)
# sib_cost = optimizer.compare_cost_advantage(tech='SIB')
# density = optimizer.estimate_energy_density(cathode_type='LayeredOxide')
```

## 5. [스스로 체크 (Self-Audit)]
1. **Aluminum**을 **SIB**의 음극 집전체로 사용할 수 있는 전자기학적/화학적 근거는? (리튬 배터리와의 차이점)
2. **Hard Carbon**의 **Specific Surface Area** (비표면적)가 너무 클 때 발생하는 **First Cycle Efficiency** (FCE) 저하의 기전은?
3. **SIB**를 **$0\text{V}$**로 완전 방전하여 보관한 후 재충전했을 때, **Cell Voltage Recovery**와 **SEI Stability**에 미치는 영향은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Materials/Battery anode-hard-carbon-physics
- 02_Knowledge/02_Battery/Materials/Battery cathode-prussian-blue-analogs
- 02_Knowledge/02_Battery/Intelligence/Battery battery-cost-modeling-sop

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
