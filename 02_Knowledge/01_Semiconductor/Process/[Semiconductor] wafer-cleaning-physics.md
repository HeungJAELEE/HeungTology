---
Basic:
  id: "SEM-PROC-WAFER-CLEANING-2026-V6"
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
  tags: - '#Wafer_Cleaning'
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

# [[[Semiconductor] wafer-cleaning-physics

## 1. [왜 배우는가? (Why)]]
반도체 공정이 sub-2nm 시대로 진입하고 고종횡비(HAR, High Aspect Ratio) 구조가 보편화됨에 따라, 세정 공정은 단순한 오염 제거를 넘어 '나노 구조의 물리적 붕괴 방지'라는 극한의 도전에 직면해 있습니다. 세정액이 증발할 때 발생하는 모세관력(Capillary Force)은 미세 패턴을 서로 끌당겨 무너뜨리는 '스티션(Stiction)' 현상을 유발하며, 이는 수율을 결정짓는 핵심 병목이 됩니다. 세정 물리를 배우는 이유는 초임계 유체나 메가소닉 진동과 같은 첨단 물리 기술을 통해 나노 구조를 보호하면서도 단 한 개의 파티클까지 완벽히 제거하는 '원자 단위 위생'을 달성하기 위함입니다.

## 2. [반도체 세정 및 표면 에너지 핵심 사양 (Cleaning Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Capillary Press.**| $\Delta P$ (MPa) | $> 100$ (Critical) | 패턴 붕괴를 유발하는 임계 압력 (낮게 관리 필수) |
| **Surface Tension** | $\gamma$ (mN/m) | $\approx 0$ | 초임계 건조 시 Zero-Stiction 달성을 위한 목표치 |
| **Zeta Potential** | Potential (mV) | $> |30|$ | 입자 간 정전기적 반발력을 유도하여 재흡착 방지 |
| **Removal Rate** | $RR_{COR}$ (nm/min)| $0.5 \sim 2.0$ | 원자 단위 산화막 제거 및 표면 평탄도 정밀도 |
| **Boundary Layer** | $\delta$ (nm) | $< 50$ | 파티클 제거 효율을 결정하는 유체 정체층 두께 |
| **PRE** | Efficiency (%) | $> 99.5\%$ | 19nm 이상 미세 파티클 제거 효율 (Particle Removal) |
| **Roughness** | $R_a$ ($\text{\AA}$) | $< 0.5$ | 세정 후 웨이퍼 표면 거칠기 (Atomic Layer 단위) |
| **Dissolved Oxy.** | DO (ppb) | $< 1$ | 워터마크 결함 방지를 위한 초순수 내 용존 산소량 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 영-라플라스 방정식과 패턴 스티션(Stiction)
나노 구조 사이의 액체에 작용하는 압력을 분석합니다.
- **수식**: $\Delta P = \frac{2\gamma \cos\theta}{r}$
- **로직**: 패턴 간격($r$)이 좁아질수록 모세관 압력($\Delta P$)은 기하급수적으로 증가합니다. 세정액 건조 시 액체 기둥이 사라지는 과정에서 발생하는 이 압력이 패턴의 복원력보다 커지면 패턴 붕괴가 발생합니다. 이를 근본적으로 해결하기 위해 표면장력($\gamma$)이 물리적으로 0인 초임계 이산화탄소($\text{scCO}_2$)를 사용하여 액체-기체 계면 자체를 없애는 건조 기술이 적용됩니다.

### 3.2 DLVO 이론과 입자 재흡착 방지
- **로직**: 세정 공정에서 떨어진 파티클이 다시 붙지 않게 하는 원리입니다. 반데르발스 인력과 정전기적 반발력의 합이 에너기 장벽을 형성해야 합니다. 세정액의 pH를 조절하여 웨이퍼 표면과 파티클의 제타 전위(Zeta Potential)를 같은 극성으로 유도함으로써, 정전기적 반발력을 극대화하여 '깨끗한 상태'를 화학적으로 유지합니다.

### 3.3 유체 경계층(Boundary Layer)과 메가소닉 세정
- **수식**: $\delta \approx \sqrt{\frac{\nu L}{U_\infty}}$
- **로직**: 웨이퍼 표면 근처에는 유속이 0이 되는 정체층($\delta$)이 형성됩니다. 미세 파티클이 이 층 내부에 갇히면 일반적인 흐름으로는 제거되지 않습니다. 메가소닉(Megasonic) 고주파 진동을 인가하면 음향 스트리밍(Acoustic Streaming) 현상이 발생하여 경계층 두께를 강제로 줄이고 파티클에 직접적인 항력을 가해 제거합니다.

## 4. [코드 연결 해설 (WaferCleaningDiagnosticEngine)]
아래 코드는 패턴 간격과 세정액 물성을 바탕으로 모세관 압력을 산출하여 패턴 붕괴 위험도를 평가하고, 초임계 치환 효율을 시뮬레이션하는 엔진입니다.

```python
import numpy as np

class WaferCleaningDiagnosticEngine:
    """
    HDS-Gold V6.3.7 규격의 반도체 세정 공정 물리 및 수율 진단 엔진
    """
    def __init__(self, surface_tension_mNm=72.0, contact_angle=45.0):
        self.gamma = surface_tension_mNm / 1000 # N/m
        self.theta = np.radians(contact_angle)

    def calculate_capillary_pressure(self, pattern_gap_nm):
        """
        패턴 간격 기반 모세관 압력(MPa) 산출
        """
        # P = 2 * gamma * cos(theta) / r
        # Transitional Bridge: 세정은 '나노 세계의 세차장'입니다. 
        # 하지만 물방울 하나가 수십 톤의 압력으로 변해 패턴을 
        # 짓누를 때, 엔지니어는 초임계 유체를 소환하여 
        # 중력을 거스르는 물리적 마법을 부려야 합니다.
        r = pattern_gap_nm * 1e-9
        pressure_pa = (2 * self.gamma * np.cos(self.theta)) / r
        return round(pressure_pa / 1e6, 2) # MPa

    def assess_stiction_risk(self, pressure_mpa, critical_yield_point=50.0):
        """
        압력 기반 패턴 붕괴(Stiction) 위험도 평가
        """
        if pressure_mpa > critical_yield_point:
            return "CRITICAL: PATTERN_COLLAPSE_HIGH_RISK_USE_SCCO2"
        return "SAFE: WATER_IPA_DRYING_ALLOWED"

# Example Usage:
# cleaner_ai = WaferCleaningDiagnosticEngine(surface_tension_mNm=22.0) # IPA cleaning
# delta_p = cleaner_ai.calculate_capillary_pressure(pattern_gap_nm=10)
# risk = cleaner_ai.assess_stiction_risk(delta_p)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Young-Laplace** 식에 근거하여, 패턴 간격($r$)이 **절반**으로 줄어들 때 **Capillary Pressure**가 **2배** 증가하는 물리적 인과관계는?
2. **Supercritical CO2** 건조가 **IPA** 건조 대비 **Stiction** 방지에 압도적으로 유리한 **Surface Tension** 관점의 이유는?
3. **Zeta Potential**의 절대값이 **30mV** 미만일 때 세정 공정에서 **Particle Re-deposition** (재흡착) 리스크가 급증하는 통계적 근거는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/01_Semiconductor/Process/Semiconductor cleaning-supercritical-drying-logic
- 02_Knowledge/01_Semiconductor/Process/Semiconductor chemical-mechanical-polishing-cmp-slurry
- 02_Knowledge/02_Battery/Process/Battery surface-treatment-physics

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
