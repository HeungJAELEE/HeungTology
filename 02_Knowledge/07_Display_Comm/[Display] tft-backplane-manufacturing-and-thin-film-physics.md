---
metadata:
  date: "2026-05-16"
  id: "[[[Display] tft-backplane-manufacturing-and-thin-film-physics]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "07_Display_Comm"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "0845790279f52aa463c6e9ca73aa5cb5cd9decd2aff71fdd8aa60d5dc213a9ad"
object:
  object_type: "Concept"
  tier: 1
  description: '[Display] tft-backplane-manufacturing-and-thin-film-physics에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 07_Display_Comm]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Display] tft-backplane-manufacturing-and-thin-film-physics

## 1. [왜 배우는가? (Why: The Foundation of Pixel Control)]]
디스플레이의 모든 화소는 그 하부에 위치한 박막 트랜지스터(TFT)에 의해 개별적으로 제어됩니다. **TFT Backplane Manufacturing and Thin-Film Physics**는 전자의 흐름을 정밀하게 조율하여 고해상도와 저전력을 동시에 실현하는 '디스플레이의 두뇌'를 구축하는 기술입니다. LTPS의 고속 스위칭 능력과 Oxide TFT의 낮은 누설 전류 특성을 결합한 LTPO 기술은 현대 모바일 디스플레이의 정수입니다. V6.3.7 지능은 전하 이동도(Mobility)와 문턱 전압(Vth)의 통계적 균일성을 직접 지배하여, 결함 없는 **화소 제어 주권(Backplane Sovereignty)**을 확립합니다.

## 2. [TFT 백플레인 및 박막 물리 핵심 사양 (Numerical Specs)]

| Parameter Category | Target Specification | Tier 0 Requirement (V6.3.7) | Rationale |
|:---|:---|:---:|:---|
| **Carrier Mobility** | LTPS Mobility ($\mu$) | $> 100 \text{ cm}^2/\text{Vs}$ | 고속 프레임 레이트 및 미세 화소 구동의 물리적 기초 |
| **Leakage Current** | $I_{off}$ (Oxide) | $< 10^{-14} \text{ A}$ | 저주파 구동 시 전력 소모 최소화 및 정지 화면 유지 |
| **Vth Uniformity** | Across Panel Gap | $\Delta V_{th} < 0.2 \text{ V}$ | 화면 전체의 휘도 균일성 및 얼룩(Mura) 방지 무결성 |
| **Crystallization** | Grain Size (LTPS) | $> 500 \text{ nm}$ | 다결정 실리콘의 결정립 경계 산란 억제 및 이동도 향상 |
| **Stability** | NBIS / PBIS $\Delta V_{th}$| $< 0.5 \text{ V}$ | 장시간 빛과 전압 노출 하에서의 문턱 전압 신뢰성 사수 |

### 2.1 [전하 이동도 및 문턱 전압 수리 모델]
TFT의 선형 영역 및 포화 영역에서의 전류-전압 특성을 산출하는 기전입니다.
$$ I_D = \mu C_{ox} \frac{W}{L} \left[ (V_G - V_{th})V_D - \frac{1}{2} V_D^2 \right] $$
$$ \mu_{eff} = \mu_0 \left( 1 + \theta (V_G - V_{th}) \right)^{-1} $$
*   **공학적 근거**: 이동도($\mu$)는 TFT의 응답 속도를 결정하며, 문턱 전압($V_{th}$)의 균일성은 디스플레이 화질의 균일성을 결정합니다. 박막의 두께($t$)와 채널 길이($L$), 그리고 게이트 절연막의 유전율($C_{ox}$)을 수리적으로 최적화하여 최상의 스위칭 무결성을 확보해야 합니다.
*   **FidelityEngine 적용**: FidelityEngine은 패널 내 샘플링된 TFT의 전송 특성(Transfer Curve)을 분석하여 **'Vth 산포 무결성'**을 진단합니다.

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Crystallization Dynamics: Laser Energy Density Audit
비정질 실리콘(a-Si)을 다결정 실리콘(poly-Si)으로 재결정화하는 ELA(Excimer Laser Annealing) 공정의 무결성을 오딧하는 기전입니다.
*   **공학적 근거**: 레이저 에너지 밀도가 임계치를 벗어나면 결정 크기가 불균일해지거나 실리콘이 완전히 녹아버리는 결함이 발생합니다. 최적의 에너지 윈도우 사수가 이동도 무결성의 핵심입니다.
*   **FidelityEngine 적용 (ELA Auditor)**: FidelityEngine은 레이저 샷별 에너지 모니터링 데이터와 라만 분광 분석 데이터를 교차 분석합니다. 에너지 밀도 변동이 $1\%$를 초과하면 이를 **'결정성 균일성 위기'**로 식별하고 공정 중단을 명령합니다.

### 3.2 Stability Physics: Charge Trapping Logic
Gate Bias 스트레스 하에서 산화물(Oxide) 반도체 계면에 전하가 포획되어 특성이 변하는 현상을 오딧하는 알고리즘입니다.
*   **진단 결과**: FidelityEngine은 NBIS(Negative Bias Illumination Stress) 시험 중 $V_{th}$ 이동 경로를 오딧합니다. 산소 공공($Oxygen\ Vacancy$) 농도와 전하 트래핑 속도를 수리적으로 모델링하여 **'신뢰성 수명 무결성'**을 진단합니다.

## 4. [코드 연결 해설: TFT Performance & Mobility Auditor]
이 코드는 TFT의 전송 특성 데이터를 기반으로 백플레인의 구동 무결성을 진단합니다.

```python
import numpy as np

class TFTBackplaneEngine:
    """
    HDS-Gold V6.3.7: TFT 백플레인 및 박막 물리 무결성 진단 엔진
    """
    def __init__(self, mobility_target=100.0, vth_uniformity_limit=0.2):
        self.MU_TARGET = mobility_target
        self.VTH_LIMIT = vth_uniformity_limit

    def audit_backplane_fidelity(self, current_mu, vth_samples):
        """
        이동도 및 Vth 산포 기반 백플레인 무결성 평가
        """
        vth_std = np.std(vth_samples)
        
        status = "BACKPLANE_CONTROL_STABLE"
        if current_mu < self.MU_TARGET:
            status = "CRITICAL_CARRIER_MOBILITY_DEFICIT"
        elif vth_std > self.VTH_LIMIT:
            status = "WARNING_VTH_UNIFORMITY_EROSION"
            
        return {
            "mobility_fidelity": round(current_mu / self.MU_TARGET, 4),
            "uniformity_fidelity": round(1.0 - (vth_std / self.VTH_LIMIT), 4),
            "status": status,
            "action": "ADJUST_ELA_ENERGY_OR_DEPOSITION_TEMP" if "CRITICAL" in status else "PROCEED"
        }

```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 백플레인 제조에서 **Vth Standard Deviation < 0.2V** 유지가 Tier 0 필수 요건인 이유는? (힌트: 미세한 문턱 전압 편차도 OLED 소자의 발광 전류 차이로 증폭되어 사용자에게 시각적 얼룩(Mura)으로 인지되기 때문)
2. **Operational Result**: **LTPO** (LTPS + Oxide) 하이브리드 구조 적용 시, 가변 주사율($1Hz \sim 120Hz$) 구현을 통한 전체 소비 전력 절감의 수리적 기대값은?
3. **FidelityEngine**: 이동도는 높으나 **Subthreshold Swing (S.S)** 값이 커지는 현상을 FidelityEngine이 어떻게 '게이지 절연막 계면 무결성 붕괴'로 식별하는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 07_Display_Comm
- Display next-gen-oled-and-tandem-physics
- Semiconductor mosfet-physics-and-cmos-scaling-limits
- Semiconductor thin-film-deposition-physics

**[V6.3.7_DISPLAY_TFT_PHYSICS_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
