---
Basic:
  id: "BAT-MAT-SALT-PRECIP-2026-V6"
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
  tags: - '#Electrolyte'
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

# [[[Battery] electrolyte-salt-precipitation

## 1. [왜 배우는가? (Why)]]
전해질은 리튬염($LiPF_6$)과 유기 용매(EC, DMC 등)의 정밀한 화학적 평형 상태를 유지해야 하는 시스템입니다. 염전출(Salt Precipitation)은 온도 저하나 농도 불균형으로 인해 용액의 화학적 포텐셜($\mu$)이 임계점을 벗어나 고체 결정으로 상전이(Phase Transition)하는 현상입니다. 이는 단순히 이온 전도도를 떨어뜨리는 문제를 넘어, 석출된 결정이 분리막의 기공을 폐쇄하는 '물리적 폐쇄(Clogging)'와 전해질 분해를 통해 치명적인 불산($HF$)을 생성하는 '화학적 부식'을 동시에 유발합니다. 이를 배우는 것은 저온 환경이나 고출력 운전 시 배터리의 내부 안정성을 보장하는 화학적 방어선을 구축하기 위함입니다.

## 2. [전해질 염전출 및 화학적 안정성 핵심 사양 (Stability Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Solubility Limit**| $LiPF_6$ Conc. | $0.4 \sim 1.5 \text{ M}$ | 온도($-40 \sim 25^\circ\text{C}$)에 따른 포화 농도 범위 |
| **Ionic Cond.** | $\sigma$ (Sigma) | $1.0 \sim 12.0 \text{ mS/cm}$ | 염 석출 및 점도 상승에 따른 이온 수송 능력 저하율 |
| **Viscosity** | $\eta$ (Eta) | $1.0 \sim 10.0 \text{ cP}$ | 저온 전출 전조 증상인 용매의 유동성 저하 지표 |
| **Moisture Limit** | $H_2O$ Content | $< 20 \text{ ppm}$ | $LiPF_6$와 반응하여 $HF$를 생성하는 수분 관리 한계 |
| **Acid Content** | $HF$ Conc. | $< 50 \text{ ppm}$ | 양극 전이금속 용출 및 격자 부식을 유발하는 산도 한계 |
| **Transference No.**| $t_+$ (Li-ion) | $0.3 \sim 0.4$ | 염 농도 변화에 따른 리튬 이온의 선택적 기여도 |
| **Oxidation Pot.** | Stability Window| $> 4.5 \text{ V}$ | 고전압 양극 표면에서의 전해질 분해 저항성 |
| **Flash Point** | Flammability | $> 30 ^\circ\text{C}$ (DMC) | 온도 상승 시 전해질 기화 및 화재 리스크 지표 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 깁스 자유 에너지와 상전이 구동력
염전출은 용액의 실제 농도($C$)가 평형 용해도($C_{sat}$)를 초과할 때 발생하는 자발적 반응입니다.
- **수식**: $\Delta G = -RT \ln(C / C_{sat})$
- **로직**: 온도가 낮아지면 $C_{sat}$가 감소하여 $\Delta G$가 음의 값이 되고, 고체 결정 핵생성(Nucleation)이 시작됩니다. 이는 분리막 기공의 굴곡도($\tau$)를 급격히 증가시켜 이온 전도도를 차단합니다.

### 3.2 왈든의 법칙 (Walden's Rule)과 이온 전도도
전해질의 점도와 전도도 사이의 인과관계를 설명합니다.
- **수식**: $\sigma \cdot \eta \approx \text{const.}$
- **의미**: 온도가 낮아지면 점도($\eta$)가 지수적으로 상승하며, 염의 용해도가 한계에 도달하여 전도도($\sigma$)가 급격히 하락합니다. 이는 저온 출력 제한(De-rating)의 물리적 근거가 됩니다.

### 3.3 아레니우스(Arrhenius) 점도 관계식
온도 변화에 따른 전해질 유동성 변화를 예측합니다.
- **수식**: $\ln \eta = \ln \eta_0 + \frac{E_{\eta}}{RT}$
- **로직**: 활성화 에너지($E_{\eta}$)가 큰 용매 시스템일수록 저온에서의 염전출 및 출력 하락 리스크가 높으므로, 저온 특성이 우수한 보조 용매(EMC 등)의 혼합비를 최적화해야 합니다.

## 4. [코드 연결 해설 (ElectrolyteChemistryEngine)]
아래 코드는 현재 온도와 전해질 농도를 기반으로 염전출 발생 가능성(Saturation Index)을 계산하고, 이온 전도도 저하 및 $HF$ 생성 리스크를 예측하는 엔진입니다.

```python
import numpy as np

class ElectrolyteChemistryEngine:
    """
    HDS-Gold V6.3.7 규격의 전해질 염전출 및 화학적 안정성 분석 엔진
    """
    def __init__(self, salt_type="LiPF6"):
        self.salt = salt_type
        self.r = 8.314 # Gas constant

    def calculate_solubility_limit(self, temp_c):
        """
        온도별 LiPF6 평형 용해도 예측 (M)
        """
        temp_k = temp_c + 273.15
        # Van't Hoff 유사 모델 기반 용해도 곡선 (가상 계수)
        solubility = 1.2 * np.exp(-0.02 * (298.15 - temp_k))
        return round(solubility, 3)

    def evaluate_precipitation_risk(self, current_conc, temp_c):
        """
        현재 농도와 온도 기반 전출 리스크(Saturation Index) 산출
        """
        sat_limit = self.calculate_solubility_limit(temp_c)
        si = current_conc / sat_limit # Saturation Index
        
        status = "STABLE"
        if si >= 1.0:
            status = "DANGER: PRECIPITATION_ONGOING"
        elif si >= 0.8:
            status = "WARNING: SUPERSATURATION"
            
        return {
            "saturation_index": round(si, 2),
            "status": status,
            "cond_reduction_est": round(max(0, (si-1.0)*50), 1) # %
        }

# Example Usage:
# engine = ElectrolyteChemistryEngine()
# report = engine.evaluate_precipitation_risk(current_conc=1.2, temp_c=-20)
```

## 5. [스스로 체크 (Self-Audit)]
1. **$LiPF_6$**가 분해되어 생성된 **$PF_5$ (Lewis Acid)**가 전해질 내의 미세 수분과 만나 **$HF$**를 생성하는 화학 양론적 반응식을 기술할 수 있는가?
2. 저온 환경에서 **염전출**에 의한 **Clogging** 효과가 분리막의 **굴곡도 ($\tau$)**를 $2$배 증가시켰을 때, 배터리의 **내부 저항 (DCR)**은 이론적으로 몇 배 상승하는가?
3. **용매의 유전율 ($\epsilon$)**이 낮은 유기 용매를 다량 사용할 때, 염의 **해리도 ($\alpha$)**가 낮아져 전출이 더 쉽게 발생하는 열역학적 이유는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Process/Battery electrolyte-filling-and-wetting
- 02_Knowledge/02_Battery/Intelligence/Battery dcir-acir-correlation-model
- 02_Knowledge/02_Battery/Materials/Battery separator-materials-and-design

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
