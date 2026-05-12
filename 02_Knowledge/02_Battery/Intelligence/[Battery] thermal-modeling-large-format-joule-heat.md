---
Basic:
  id: "BAT-INTEL-THERMAL-MODELING-2026-V6"
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
  tags: - '#Thermal_Modeling'
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

# [[[Battery] thermal-modeling-large-format-joule-heat

## 1. [왜 배우는가? (Why)]]
배터리 셀의 용량이 100Ah를 넘어서는 대형화(Large-format) 추세에서는 비표면적 대비 내부 부피가 급격히 커져 방열 효율이 물리적으로 저하됩니다. 특히 2C 이상의 고출력 운용이나 급속 충전 시 발생하는 줄 발열(Joule Heat)은 셀 중심부의 온도를 국부적으로 상승시켜 SEI 층의 파괴와 리튬 플레이팅을 가속화하며, 이는 열 폭주(Thermal Runaway)의 전초 증상이 됩니다. 이를 배우는 이유는 대형 셀 내부의 온도 구배(Gradient)를 수리적으로 예측하고, 집전체 방향의 열 이방성(Anisotropy)을 고려한 최적의 냉각 경로를 설계하여 안전한 고에너지 밀도 시스템을 구현하기 위함입니다.

## 2. [대형 셀 열 모델링 및 발열 핵심 사양 (Thermal Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Heat Gen ($q_v$)** | Volumetric Density | $1.2\times 10^5 \sim 2.5\times 10^6 \text{ W/m}^3$ | 단위 부피당 발열 밀도 (2C Peak Load 기준) |
| **Thermal Res.** | $R_{th}$ (Core-Case)| $0.8 \sim 1.5 \text{ K/W}$ | 셀 중심부에서 냉각 매체까지의 총 열 장벽 저항 |
| **In-plane Cond.** | $k_{xy}$ (Horizontal)| $25 \sim 35 \text{ W/m}\cdot\text{K}$ | 집전체(Cu/Al)를 통한 수평 방향의 고속 열전도도 |
| **Cross-plane Cond.**| $k_z$ (Vertical) | $0.4 \sim 0.9 \text{ W/m}\cdot\text{K}$ | 적층/분리막 방향의 낮은 수직 열전도도 (열 장벽) |
| **Max Temp Grad.** | $\Delta T$ (In-cell) | $< 15.0 \text{ K}$ | 고출력 운용 시 셀 내부 온도 편차의 안전 허용치 |
| **Specific Heat** | $C_p$ (Average) | $1,000 \sim 1,150 \text{ J/kg}\cdot\text{K}$ | 소재 혼합물의 비열 (과도 상태 온도 변화 속도 결정) |
| **Biot Number** | $Bi$ | $> 0.1$ | 내부 열저항이 외부 대류보다 지배적인 대형 셀 특성 |
| **Entropic Coeff.**| $dE_{oc}/dT$ | $-0.5 \sim 0.5 \text{ mV/K}$ | 엔트로피 변화에 따른 가역 열량의 SOC별 계수 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 베르나르디 방정식(Bernardi Equation)과 열역학적 평형
셀 내부의 총 발열량($Q_{gen}$)을 정량화합니다.
- **수식**: $Q_{gen} = I(V_{oc} - V) + I \cdot T \cdot \frac{dE_{oc}}{dT}$
- **로직**: 총 발열은 비가역 열(Overpotential Heat)과 가역 열(Entropic Heat)의 합입니다. 고출력 구간에서는 비가역 열($I^2R_{int}$)이 전체의 $90\%$ 이상을 차지하며 온도를 급격히 높입니다. 반면, 가역 열은 리튬 이온의 삽입/탈리 과정에서의 무질서도 변화에 따라 흡열 또는 발열 반응을 보이며, SOC에 따라 온도 예측에 $5 \sim 10\%$의 변동성을 제공합니다.

### 3.2 열 이방성(Anisotropy)과 냉각 경로 최적화
- **로직**: 배터리 셀은 금속 집전체와 세라믹/고분자 분리막의 적층 구조로 인해 수평 방향($k_{xy}$)과 수직 방향($k_z$)의 열전도도가 수십 배 차이 납니다. 대형 셀의 경우 표면 냉각(Face Cooling)보다는 열전도도가 높은 탭(Tab) 또는 측면 냉각(Side Cooling)을 수행하는 것이 셀 중심부($T_{core}$)의 열을 외부로 효과적으로 배출하고 내부 온도 구배를 완화하는 데 훨씬 유리합니다.

### 3.3 PINN(Physics-Informed Neural Network) 기반 가상 센싱
- **로직**: 셀 내부의 온도를 직접 측정하는 것은 물리적으로 불가능합니다. 열 확산 방정식($\rho C_p \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T) + Q_{gen}$)을 손실 함수(Loss Function)로 포함하는 PINN 모델은, 표면 온도 센서 데이터와 전류/전압 정보만을 가지고 셀 중심부의 온도를 실시간으로 정확하게 추론(Virtual Sensing)해 냅니다.

## 4. [코드 연결 해설 (LargeFormatThermalEngine)]
아래 코드는 베르나르디 방정식을 기반으로 비가역/가역 발열량을 계산하고, 집중 정수 모델(Lumped Parameter Model)을 활용하여 셀 중심부의 온도를 추정하는 열 진단 엔진입니다.

```python
import numpy as np

class LargeFormatThermalEngine:
    """
    HDS-Gold V6.3.7 규격의 대용량 배터리 열 모델링 및 발열 진단 엔진
    """
    def __init__(self, r_int_mohm=1.5, r_th_kw=1.2, cp_jkgk=1100, mass_kg=2.5):
        self.r_int = r_int_mohm / 1000 # Ohm
        self.r_th = r_th_kw
        self.m_cp = mass_kg * cp_jkgk

    def calculate_total_heat(self, current_a, temp_k, entropic_coeff_mvk=0.2):
        """
        Bernardi Equation 기반 발열량(W) 산출
        """
        # q_irrev = I^2 * R
        q_irrev = (current_a ** 2) * self.r_int
        # q_rev = I * T * dS/dT
        q_rev = current_a * temp_k * (entropic_coeff_mvk / 1000)
        
        # Transitional Bridge: 열 모델링은 '셀 내부의 보이지 않는 불꽃'을 
        # 수식으로 그려내는 작업입니다. 고출력 충전 시 
        # 비가역 열이 지배적으로 작용할 때, AI는 가역 열의 
        # 미세한 변동까지 계산하여 폭주 1초 전의 온도 기점을 잡아냅니다.
        return q_irrev + q_rev

    def estimate_core_temp(self, q_gen, t_surface, dt=1.0, t_core_prev=25.0):
        """
        Lumped Parameter Model 기반 중심 온도 추정 (dT/dt)
        """
        # dT = (Q_gen - (T_core - T_surface)/R_th) / (m*Cp) * dt
        dt_core = (q_gen - (t_core_prev - t_surface) / self.r_th) / self.m_cp * dt
        return round(t_core_prev + dt_core, 3)

# Example Usage:
# thermal_ai = LargeFormatThermalEngine(r_int_mohm=1.2, mass_kg=3.0)
# total_q = thermal_ai.calculate_total_heat(current_a=240, temp_k=313.15) # 2C discharge
# core_t = thermal_ai.estimate_core_temp(q_gen=total_q, t_surface=45.0, t_core_prev=50.0)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Bernardi Equation**에서 **Reversible Heat** (가역 열)이 SOC 구간에 따라 흡열(Cooling) 반응을 보일 수 있는 물리적 기전은?
2. **Biot Number** ($Bi$)가 **0.1**보다 큰 대형 셀에서 외부 냉각 팬의 유량을 높이는 것보다 내부 **Thermal Resistance**를 줄이는 것이 효율적인 이유는?
3. **Anisotropy** (열 이방성) 특성상 **Tab Cooling**이 **Face Cooling**보다 셀 내부의 **Temperature Gradient**를 완화하는 데 유리한 공학적 근거는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Intelligence/Battery thermal-runaway-mechanism
- 02_Knowledge/02_Battery/Process/Battery battery-pack-cooling-system-design
- 02_Knowledge/03_AI_Data/General/AI physics-informed-neural-networks-pinn

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
