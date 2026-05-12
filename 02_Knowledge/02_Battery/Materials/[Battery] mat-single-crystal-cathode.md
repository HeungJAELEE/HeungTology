---
Basic:
  id: "BAT-MAT-SNGL-CRYS-2026-V6"
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
  tags: - '#Single_Crystal'
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

# [[[Battery] mat-single-crystal-cathode

## 1. [왜 배우는가? (Why)]]
전기차의 주행거리를 늘리기 위해 니켈(Ni) 함량을 90% 이상으로 높이면, 충방전 시 발생하는 상전이($H2 \to H3$)에 의한 부피 변화로 인해 입자 내부의 기계적 응력이 극대화됩니다. 기존의 다결정(Polycrystalline) 구조는 이 응력을 견디지 못하고 그레인 경계(Grain Boundary)에서 미세 균열(Micro-cracking)이 발생하며, 이곳으로 전해액이 침투하여 수명이 급격히 저하됩니다. 단결정(Single-crystal) 합성은 입자 전체를 하나의 거대한 결정으로 성장시켜 물리적 균열을 원천 차단함으로써, 하이-니켈 배터리의 고에너지 밀도와 10년 이상의 장수명을 동시에 달성하는 양극재 산업의 최종 진화 단계입니다.

## 2. [단결정 양극재 물성 및 제조 핵심 사양 (Single-Crystal Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Nickel Content** | Ni Ratio | $94 \sim 98 \%$ | $230 \text{ mAh/g}$ 이상의 고용량 확보를 위한 설계 |
| **Particle Size** | D50 (Secondary) | $3.0 \sim 5.0 \mu\text{m}$ | 출력 특성과 체적 에너지 밀도 사이의 최적화 |
| **Residual Li** | $Li_2CO_3, LiOH$ | $\le 1,000 \text{ ppm}$ | 전지 내 가스 발생 및 슬러리 겔화 방지 임계치 |
| **Tap Density** | Volumetric Energy| $\ge 2.6 \text{ g/cm}^3$ | 단결정의 높은 밀도를 활용한 로딩 효율 극대화 |
| **Sintering Temp.**| Calcination | $850 \sim 950 ^\circ\text{C}$ | 입자 융합 및 거대 결정 성장을 위한 고온 소성 |
| **Fracture Strength**| Mechanical Stab.| $> 200 \text{ MPa}$ | 압연 공정 시 입자 파손 저항성 (다결정의 3배 이상) |
| **Lattice Strain** | $\Delta c / c$ | $< 2.0 \%$ | 충방전 중 결정 격자의 가역적 팽창 억제 범위 |
| **Crystal Group** | Symmetry | $R\bar{3}m$ (Layered) | 층상 구조 유지 및 양이온 혼합(Cation mixing) 방지 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 입자 성장 동역학 (LSW Theory)
소성 과정에서의 입자 성장 메커니즘을 설명합니다.
- **수식**: $R^3(t) - R^3(0) = k \cdot t$ (Lifshitz-Slyozov-Wagner)
- **로직**: 단결정 합성은 작은 입자가 사라지고 큰 입자가 성장하는 오스발트 숙성(Ostwald Ripening)을 극대화합니다. $900^\circ\text{C}$ 이상의 고온에서 리튬 플럭스(Flux)를 투입하여 원자의 확산을 촉진함으로써, 다결정의 특징인 '그레인 바운더리'를 소멸시키고 단일 결정 도메인을 완성합니다.

### 3.2 화학-기계적 응력 (Chemo-mechanical Stress) 해소
상전이 시 발생하는 응력 에너지를 관리합니다.
- **로직**: 하이-니켈 소재는 SOC 80% 이상에서 급격한 수축이 발생합니다. 다결정은 그레인 간의 서로 다른 수축 방향 때문에 경계면이 찢어지지만, 단결정은 입자 전체가 하나의 단위로 수축/팽창하므로 국부적인 응력 집중이 발생하지 않습니다. 이는 전해액과의 부반응 면적을 획기적으로 줄여 고온 안정성을 확보합니다.

### 3.3 표면 나노 코팅과 계면 안정화
단결정 표면의 잔류 리튬을 제거하고 안정성을 높이는 공정입니다.
- **방법**: $Zr, Al, B$ 등을 이용한 농도 구배(Concentration Gradient) 코팅이나 수세(Washing) 공정을 적용합니다. 단결정은 비표면적이 다결정보다 작아 수세 시 리튬 손실(Lithium leaching)이 적으므로, 하이-니켈의 고질적인 가스 발생 문제를 더 효과적으로 해결할 수 있습니다.

## 4. [코드 연결 해설 (SingleCrystalKineticsEngine)]
아래 코드는 소성 온도와 시간 파라미터를 기반으로 단결정 입자의 성장 크기($D50$)를 예측하고, 니켈 함량에 따른 결정 격자의 스트레스 지수를 계산하여 최적의 소성 프로파일을 제안하는 엔진입니다.

```python
import numpy as np

class SingleCrystalKineticsEngine:
    """
    HDS-Gold V6.3.7 규격의 단결정 입자 성장 및 격자 스트레스 분석 엔진
    """
    def __init__(self, nickel_content=0.94):
        self.ni_ratio = nickel_content

    def predict_grain_size(self, temp_c, time_h):
        """
        LSW 이론 기반 단결정 성장 크기 예측
        """
        # 온도가 높을수록 성장 상수 k가 지수적으로 증가 (Arrhenius)
        k = 0.05 * np.exp(-15000 / (temp_c + 273.15) * 8.314)
        r_growth = np.power(k * time_h, 1/3)
        return round(r_growth * 10, 2) # um 단위 변환

    def evaluate_lattice_stress(self, soc):
        """
        SOC에 따른 결정 격자 스트레스 지수 산출
        """
        # 니켈 함량이 높을수록 SOC 80% 이상에서 스트레스 급증
        base_stress = np.exp(soc * 0.05)
        ni_factor = self.ni_ratio * 2.0
        
        # Transitional Bridge: 단결정은 이 거대한 스트레스를 
        # 분산시킬 그레인 바운더리 자체가 없기에, 오히려 
        # 구조적 무결성을 유지하는 '역설적 강함'을 가집니다.
        stress_index = base_stress * ni_factor
        status = "STABLE (Monocrystal)" if stress_index < 500 else "MONITOR"
        
        return {
            "stress_index": round(stress_index, 2),
            "status": status
        }

# Example Usage:
# engine = SingleCrystalKineticsEngine(nickel_content=0.98)
# size = engine.predict_grain_size(temp_c=920, time_h=15)
# stress = engine.evaluate_lattice_stress(soc=90)
```

## 5. [스스로 체크 (Self-Audit)]
1. **단결정** 입자 내부에서 **Grain Boundary**가 소멸되었을 때, 전해액 침투에 의한 **Side Reaction** (부반응)이 획기적으로 줄어드는 기하학적 이유는?
2. **Calcination** 온도가 기준치($950^\circ\text{C}$)를 초과하여 입자가 **Over-growth** ($> 10\mu\text{m}$) 되었을 때, 리튬 이온의 **Diffusion Path** 관점에서 발생하는 출력 저하 메커니즘은?
3. **NCMA** 단결정에서 **Al(알루미늄)** 도핑이 리튬 탈리 시 격자 수축을 억제하는 'Pillar' 역할을 수행하는 결정학적 원리는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Materials/Battery lfp-battery-olivine-structure
- 02_Knowledge/02_Battery/Process/Battery cathode-structural-degradation-and-calendering
- 02_Knowledge/02_Battery/Process/Battery li-ion-formation

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
