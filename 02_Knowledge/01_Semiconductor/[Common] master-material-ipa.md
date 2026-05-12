---
Basic:
  id: "MAT-MASTER-IPA-2026-V6"
  domain: "02_Knowledge"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#IPA'
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

# [Common] master-material-ipa

## 1. [왜 배우는가? (Why)]
**IPA(이소프로필 알코올)**는 반도체, 배터리, 디스플레이 등 첨단 제조 공정 전반에서 가장 널리 사용되는 '만능 세정 용제'입니다. 이 문서를 마스터 객체로 배우는 이유는 팔란티어 파운드리의 '객체 유일성(Core Object Principle)'에 따라, 파편화된 도메인별 정보를 하나로 통합하여 전사적인 품질 표준을 수립하고 공급망 위기 시 입체적인 영향 분석(Impact Analysis)을 수행하기 위함입니다. 반도체에서는 패턴 붕괴를 막는 '표면 장력 조절자'로, 배터리에서는 수분을 제거하는 '계면 정화제'로 기능하는 IPA의 다각적 물리 특성을 이해하는 것은 초정밀 제조의 무결성을 확보하는 필수 요건입니다.

## 2. [IPA 화학적 물리 특성 및 마스터 사양 (Material Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Purity** | Assay (%) | $\ge 99.999$ (UP-S) | 반도체 수율 및 소자 신뢰성 확보를 위한 초고순도 관리 |
| **Moisture** | Water (ppm) | $\le 50$ | 배터리 전해액 부반응 및 산화막 형성 억제의 핵심 지표 |
| **Surface Tension**| Tension (mN/m) | $21.7$ (@ $20 \text{ }^\circ\text{C}$)| Marangoni 건조 시 물($72.8$)과의 장력 차를 이용한 건조 |
| **Vapor Press.** | Pressure (kPa) | $4.4$ (@ $20 \text{ }^\circ\text{C}$) | 휘발 특성을 이용한 세정 후 잔류물 없는 건조 공정 설계 |
| **Metal Impurity** | Metal (ppt) | $\le 10$ | 반도체 접합부 누설 전류 방지를 위한 미세 금속 제어 |
| **Boiling Point** | Temp ($^\circ\text{C}$) | $82.6$ | 공정 온도 및 증류 재생 시스템 설계를 위한 기준점 |
| **Flash Point** | Temp ($^\circ\text{C}$) | $11.7$ | 방폭 설비 및 화학물질 안전 관리를 위한 발화 지점 |
| **Viscosity** | Dynamic (cP) | $2.43$ (@ $20 \text{ }^\circ\text{C}$)| 세정액 분사 및 흐름성 제어를 위한 유체 역학 지표 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 마랑고니 효과(Marangoni Effect)와 웨이퍼 건조
- **로직**: 세정 후 웨이퍼 표면에 남은 물방울을 제거할 때 IPA 증기를 분사합니다. IPA는 물보다 표면 장력이 훨씬 낮기 때문에, 물방울의 계면 장력 균형이 깨지면서 액체가 표면 장력이 높은 쪽(물 쪽)으로 끌려 올라가는 '마랑고니 흐름'이 발생합니다. 이를 통해 나노 패턴 사이의 물을 물리적 자극 없이 완벽히 제거하여 패턴 붕괴(Stiction)와 워터마크 형성을 원천 차단합니다.

### 3.2 안토안 방정식(Antoine Equation)과 휘발성 제어
- **수식**: $\log_{10} P = A - \frac{B}{C + T}$
- **로직**: 온도($T$)에 따른 IPA의 포화 증기압($P$)을 정밀하게 산출합니다. 이는 디스플레이 대면적 기판 세정 시 건조 속도를 제어하여 얼룩(Stain)을 방지하고, 배터리 극판의 수분 치환 공정에서 용매의 회수율을 최적화하는 수리적 기틀이 됩니다.

### 3.3 한센 용해도 파라미터(Hansen Solubility Parameter, HSP)
- **로직**: IPA의 분산력, 극성, 수소 결합 에너지를 분석하여 특정 유기 오염물(Photoresist 잔여물 등)과의 상용성을 판단합니다. 물과 기름 모두와 잘 섞이는 양친매성(Amphiphilic) 특성을 활용하여, 공정 전환 시 수계 세정에서 비수계 공정으로 넘어가는 '브릿지 용제'로서의 역할을 수행합니다.

## 4. [코드 연결 해설 (ChemicalPhysicsDiagnosticEngine)]
아래 코드는 공정 온도에 따른 IPA의 포화 증기압을 산출하고, 측정된 순도 및 수분 함량을 기반으로 해당 로트(Lot)가 반도체용(UP-S) 또는 배터리용(EL) 규격에 적합한지 판별하는 엔진입니다.

```python
import numpy as np

class ChemicalPhysicsDiagnosticEngine:
    """
    HDS-Gold V6.3.7 규격의 IPA 소재 물리 특성 및 등급 검증 엔진
    """
    def __init__(self):
        # Antoine constants for IPA (T in Celsius, P in mmHg)
        self.A, self.B, self.C = 8.11778, 1580.92, 219.61

    def calculate_vapor_pressure(self, temp_c):
        """
        안토안 방정식을 이용한 포화 증기압(kPa) 산출
        """
        # Transitional Bridge: 소재는 '공정의 하드웨어'입니다. 
        # 온도에 따른 증기압의 미세한 변화는 건조로 내부의 
        # 농도 산포를 결정하며, 이는 곧 나노 입자의 
        # 재흡착 여부를 결정짓는 물리적 장벽이 됩니다.
        log_p = self.A - (self.B / (temp_c + self.C))
        p_mmhg = 10**log_p
        p_kpa = p_mmhg * 0.133322
        return round(p_kpa, 2)

    def validate_material_grade(self, purity_percent, moisture_ppm):
        """
        순도 및 수분 함량 기반 소재 등급 판별
        """
        if purity_percent >= 99.999 and moisture_ppm <= 50:
            return "GRADE: SEMICONDUCTOR_UPS_CERTIFIED"
        elif purity_percent >= 99.9 and moisture_ppm <= 500:
            return "GRADE: BATTERY_EL_CERTIFIED"
        return "GRADE: REJECTED_INDUSTRIAL_ONLY"

# Example Usage:
# ipa_ai = ChemicalPhysicsDiagnosticEngine()
# press = ipa_ai.calculate_vapor_pressure(temp_c=25)
# decision = ipa_ai.validate_material_grade(purity_percent=99.9995, moisture_ppm=42)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Marangoni Drying** 공정에서 **IPA** 증기 농도가 부족할 때, **Water Mark** 결함이 발생하는 유체역학적 원인은?
2. **Battery** 공정에서 **IPA**의 **Moisture** 함량을 **50ppm** 이하로 관리해야 하는 **Electrolyte Decomposition** (전해액 분해) 방지 측면의 이유는?
3. **Semiconductor** 등급의 **IPA**가 일반 공업용 대비 **Metal Impurity** 관리를 **ppt** 단위로 수행해야 하는 **Gate Oxide Integrity** (GOI) 관점의 근거는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/01_Semiconductor/Process/Battery wafer-cleaning-physics
- 02_Knowledge/02_Battery/Process/Battery surface-treatment-physics
- 02_Knowledge/07_Display_Comm/Process/Display glass-substrate-cleaning-logic

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
