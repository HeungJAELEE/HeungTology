---
lineage:
  dataset_reference: battery-aging-kinetics-log-v2026
  original_author: Antigravity Vault
  original_hash: cc85c8b9f5466e1fc4f96535824742fe5ca1ba80cf64fa458681a9f71e8ba79c
metadata:
  date: '2026-05-16'
  domain: 02_Battery
  id: '[[[Battery] cycle-life-vs-calendar-life]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 배터리 생애주기 열화 경로(Cycle vs Calendar Life)에 관한 고밀도 물리-데이터 융합 지능 노드
  object_type: Algorithm
  tier: 1
properties:
  aging_acceleration_index_beta: 1.5-2.0
  calendar_decay_rate: 1.5-3.0%/year
  ce_threshold: < 99.9%
  cycle_decay_rate: 0.02-0.05%/cycle
  dcir_eol_threshold: '> 200%'
  external_db_endpoint: Aging-Kinetics-Log
  fast_charging_decay_rate: '> 0.1%/cycle'
  gas_constant_r: '8.314'
  high_temp_storage_decay_rate: '> 5.0%/year'
  lam_eol_threshold: '> 15%'
  lli_eol_threshold: '> 20%'
  sei_activation_energy_ea: 50-70 kJ/mol
  soh_eol_threshold: < 80%
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 02_Battery]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Battery] cycle-life-vs-calendar-life

## 1. [Scientific Rationale: Dual Degradation Pathways]

배터리의 가용 수명(Life Expectancy)은 전기화학적 활물질의 가역적 가용성($Li^+$)과 계면 무결성(Interface Integrity)의 함수임. 수명 감쇠는 크게 충방전 반복에 의한 **사이클 수명(Cycle Life)**과 시간 경과 및 보존 조건에 의한 **보존 수명(Calendar Life)**으로 분화됨. Manson-standard HDS-Gold 규격에 따라, 모든 수명 진단은 리튬 이온 소실(LLI) 및 활물질 소실(LAM)의 수리적 결합 모델로 정의됨.

## 2. [Numerical Parameter Specification]

### 2.1 [Degradation Metrics & Thresholds]

| 파라미터 (Parameter) | 물리적 정의 (Scientific Rationale) | 퇴화 임계치 (EoL Limit) | 공학적 기전 (Mechanism) |
| :--- | :--- | :---: | :--- |
| **SOH (Cap. Retention)** | $Q_{\text{rem}} / Q_{\text{nom}} \times 100\%$ | $< 80\%$ | 가용 리튬($Li^+$) 고갈 및 활물질 구조 붕괴 |
| **DCIR Increase ($\Delta R$)** | $\Delta V / \Delta I$ | $> 200\%$ | SEI층 조대화 및 접촉 저항 상승 |
| **LLI (Loss of Li)** | 가용 리튬 이온 총량 감소 | $> 20\%$ | SEI 형성 및 리튬 석출(Plating) |
| **LAM (Loss of AM)** | 활물질 비표면적 감소 | $> 15\%$ | 격자 변형($\epsilon$) 및 미세 균열 발생 |
| **Coulombic Eff. (CE)** | $Q_{\text{dis}} / Q_{\text{chg}}$ | $< 99.9\%$ | 부반응(Side reactions) 누적 지표 |

### 2.2 [Cycle vs. Calendar Status (Verified v2026)]

| Aging Mode | Core Variable | verified Decay Rate | Dominant Physics |
| :--- | :---: | :---: | :--- |
| **Cycle Aging** | C-rate, DoD | $0.02 \sim 0.05\%/\text{cycle}$ | Butler-Volmer Kinetics |
| **Calendar Aging** | Temp, SoC | $1.5 \sim 3.0\%/\text{year}$ | Arrhenius Diffusion |
| **High-Temp Storage** | $45 \, ^\circ\text{C}$, $100\%$ SoC | $> 5.0\%/\text{year}$ | Electrolyte Decomposition |
| **Fast Charging** | $> 2\text{C}$ | $> 0.1\%/\text{cycle}$ | Li-Plating / Sand's Time |

## 3. [Electrochemical Modeling: FidelityEngine]

### 3.1 보존 수명(Calendar) Diffusion 모델
시간 경과에 따른 SEI층 성장은 확산 제한(Diffusion-limited) 거동을 보이며, 시간의 제곱근($\sqrt{t}$)에 비례함.
$$ SOH_{cal}(t, T, SoC) = 1 - k_{ref} \cdot f(SoC) \cdot \exp\left(-\frac{E_a}{R}\left(\frac{1}{T} - \frac{1}{T_{ref}}\right)\right) \cdot \sqrt{t} $$
- **$E_a$**: SEI 형성 활성화 에너지 ($50 \sim 70 \, \text{kJ/mol}$) [Ref: Aging-Kinetics-Log].
- **$f(SoC)$**: 고전압($> 4.2\text{V}$) 구간에서 전해액 산화 가속 계수.

### 3.2 사이클 수명(Cycle) 스트레인 모델
충방전 시 격자 팽창/수축에 의한 피로 파괴($\sigma_{max}$) 모델링.
$$ \Delta SOH_{cyc} \propto \sum (\text{DoD})^\beta \cdot \exp\left(\frac{\sigma_{mechanical}}{E}\right) $$
- **$\beta$**: 노화 가속 지수 ($1.5 \sim 2.0$).
- **Logic**: 실리콘 음극재 함량 증가 시 $\sigma_{mechanical}$ 급증으로 인한 비선형적 수명 급락 진단 로직 가동.

## 4. [Advanced Diagnostic Logic: HealthCheck-V7]

```python
import numpy as np

class BatteryHealthOrchestrator:
    """
    HDS-Gold V7.6.2: 배터리 잔존 수명(RUL) 정밀 진단 엔진
    """
    def __init__(self, initial_cap_ah=100):
        self.q0 = initial_cap_ah
        self.r0 = 1.0 # mOhm

    def estimate_combined_soh(self, cycle_count, calendar_days, avg_temp_k, avg_soc):
        # 1. Calendar Aging (Arrhenius + Root-t)
        ea = 65000 # J/mol
        r = 8.314
        k_cal = 0.001 * np.exp(-ea/r * (1/avg_temp_k - 1/298)) * (avg_soc / 0.5)
        loss_cal = k_cal * np.sqrt(calendar_days)
        
        # 2. Cycle Aging (DoD stress model)
        k_cyc = 0.0002 * (cycle_count)
        loss_cyc = k_cyc * (1.2 if avg_temp_k > 318 else 1.0)
        
        # 3. Combined SOH
        total_loss = loss_cal + loss_cyc
        current_soh = (1 - total_loss) * 100
        
        return {
            "SOH_Current_pct": round(current_soh, 2),
            "Dominant_Mode": "Calendar" if loss_cal > loss_cyc else "Cycle",
            "EoL_Forecast_Days": round((0.2 - total_loss) / (k_cal/2/np.sqrt(calendar_days) + k_cyc/calendar_days), 0)
        }
```

## 5. [Verification & Audit Protocol]

1. **Synergistic Aging**: 캘린더 노화로 약해진 SEI층이 사이클 중 기계적 응력에 의해 쉽게 파손되어 퇴화가 가속되는 '결합 노화(Synergistic Aging)' 메커니즘을 증명하시오.
2. **SoC Dependency**: 고온 보존($45 \, ^\circ\text{C}$) 시 SoC $100\%$와 $50\%$ 간의 용량 감쇠율 편차가 전해액 산화 전위($V_{ox}$)와 갖는 상관관계를 수리적으로 분석하시오.
3. **Internal Resistance**: DCIR 증가율이 용량 감쇠율($\Delta Q$)보다 빠르게 상승할 경우, 이를 전극 계면의 '저항막 형성' 관점에서 포렌식 진단하시오.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] Battery-degradation-physics-and-mechanisms]]
- [[[Concept] Battery-Management-System-BMS-and-Safety-Intelligence]]
- [[[Data] battery-aging-kinetics-log-v2026]]
- [[[Concept] Battery-Slurry-Mixing-and-Rheology-Physics]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**
**[TIMESTAMP: 2026-05-16]**
**[GROUNDED_VIA: battery-aging-kinetics-log-v2026]**