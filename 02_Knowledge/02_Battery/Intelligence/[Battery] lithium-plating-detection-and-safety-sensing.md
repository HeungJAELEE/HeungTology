---
Basic:
  id: "BAT-INTELL-LITH-PLATE-2026-V6"
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
  tags: - '#Lithium_Plating'
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

# [[[Battery] lithium-plating-detection-and-safety-sensing

## 1. [왜 배우는가? (Why)]]
리튬이온 배터리 급속 충전의 가장 치명적인 걸림돌은 보이지 않는 살인마라 불리는 '리튬 플레이팅(Lithium Plating)'입니다. 저온이나 고전류 충전 시 리튬 이온이 음극 격자 내부로 삽입되지 못하고 표면에 금속 형태로 석출되는 이 현상은, 수지상 결정(Dendrite)으로 성장하여 분리막을 관통하고 내부 단락을 유발하여 즉각적인 열폭주를 일으킵니다. 이를 배우는 이유는 플레이팅을 $0.1\text{ mAh}$ 단위로 정밀하게 감지하고 억제하여, 충전 시간을 $50\%$ 이상 단축하면서도 절대적인 안전성을 보장하는 '초고성능 BMS 지능'을 확보하기 위함입니다.

## 2. [리튬 석출 감지 및 안전 제어 핵심 사양 (Plating Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Plating Potential**| $E_{an}$ vs $Li/Li^+$ | $< 0 \text{ V}$ | 석출이 시작되는 열역학적 평형 전압 임계치 |
| **Detect Sensitivity**| Min. Plating Q | $< 0.1 \text{ mAh}$ | 미세 석출을 포착하기 위한 알고리즘 정밀도 |
| **Response Time** | Control Latency | $< 100 \text{ ms}$ | 플레이팅 감지 시 충전 전류 하향 조정 반응 속도 |
| **EIS Frequency** | Analysis Range | $10 \text{ Hz} \sim 1 \text{ kHz}$ | 계면 저항($R_{ct}$) 변화 추적을 위한 주파수 대역 |
| **Critical Current** | $CCD$ | $> 2.0 \text{ mA/cm}^2$ | 덴드라이트 성장이 가속화되는 한계 전류 밀도 |
| **Sand's Time** | $\tau_S$ | Calculated per $j$ | 이온 고갈로 인해 석출이 강제되는 물리적 시간 한계 |
| **VRA Resolution** | $dV/dt$ Precision | $\pm 0.1 \text{ mV/s}$ | 전압 이완 분석을 위한 센서 데이터 해상도 |
| **Safety Standard** | Compliance | UL2580 / ISO 26262 | 차량용 배터리 안전 및 기능 안전 규격 준수 여부 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 샌드의 시간 (Sand's Time)과 확산 한계
전극 표면의 이온 농도가 $0$이 되어 플레이팅이 강제되는 시점을 정의합니다.
- **수식**: $\tau_S = \pi D (\frac{C_0 z F}{2 j})^2$
- **로직**: 전류 밀도($j$)가 높을수록 이온의 공급 속도(확산)가 소모 속도를 따라가지 못해 샌드의 시간($\tau_S$)이 짧아집니다. AI는 이 물리적 한계를 실시간 계산하여 플레이팅 발생 전 충전 전류를 선제적으로 제어합니다.

### 3.2 전압 이완 분석 (VRA, Voltage Relaxation Analysis)
충전 중단 직후의 전압 거동을 통해 석출된 리튬을 탐지합니다.
- **로직**: 정상 셀은 전압이 지수함수적으로 안정화되지만, 플레이팅이 발생한 셀은 석출된 리튬이 다시 격자로 삽입(Stripping)되는 과정에서 특유의 전압 평원(Voltage Plateau)을 형성합니다. 이 평원의 길이를 분석하면 석출된 리튬의 양을 정량적으로 산출할 수 있습니다.

### 3.3 과전압 성분 분해 ($\eta_{total}$)
플레이팅을 유발하는 과전압의 인과관계를 분해합니다.
- **수식**: $\eta_{total} = \eta_{act} + \eta_{conc} + \eta_{ohm}$
- **의미**: 저온에서는 농도 과전압($\eta_{conc}$)이 지배적으로 작용하여 음극 전위를 $0\text{V}$ 이하로 끌어내립니다. BMS는 각 성분별 과전압을 실시간 추정하여 최적의 급속 충전 프로파일(Multistage Constant Current)을 동적으로 생성합니다.

## 4. [코드 연결 해설 (LithiumPlatingMonitor)]
아래 코드는 충전 종료 후의 전압 이완 데이터를 분석하여 $dV/dt$ 피크를 검출하고, 이를 통해 리튬 플레이팅 발생 여부와 석출량을 정량화하는 진단 엔진입니다.

```python
import numpy as np

class LithiumPlatingMonitor:
    """
    HDS-Gold V6.3.7 규격의 리튬 플레이팅 감지 및 안전 제어 엔진
    """
    def __init__(self, sampling_rate_hz=10):
        self.fs = sampling_rate_hz

    def detect_stripping_plateau(self, voltage_time_series):
        """
        Voltage Relaxation Curve 미분 분석을 통한 플레이팅 검출
        """
        # 1. 전압 미분 (dV/dt) 산출
        dv = np.diff(voltage_time_series)
        dt = 1.0 / self.fs
        dv_dt = dv / dt
        
        # 2. 미분 곡선에서의 피크(Plateau 징후) 검출
        # Transitional Bridge: 리튬 플레이팅이 발생하면 전압 이완 곡선에 
        # '턱'이 생깁니다. 이 미세한 수평 구간은 금속 리튬이 
        # 다시 이온화되는 전기화학적 신호입니다.
        peak_score = np.max(np.abs(np.gradient(dv_dt)))
        
        is_plated = peak_score > 0.05 # 임계치 (mV/s^2)
        severity = "CRITICAL" if peak_score > 0.15 else "WARNING"
        
        return {
            "plating_detected": is_plated,
            "severity": severity if is_plated else "NONE",
            "stripping_index": round(peak_score, 4)
        }

# Example Usage:
# monitor = LithiumPlatingMonitor()
# report = monitor.detect_stripping_plateau(v_relaxation_data)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Sand's Time** ($\tau_S$) 공식에 따르면, **Electrolyte Diffusivity** ($D$)가 $2$배 증가할 때 동일 전류 밀도에서 **Plating** 발생 지연 시간은 몇 배 증가하는가?
2. **EIS** 분석에서 **Charge Transfer Resistance** ($R_{ct}$)가 급격히 감소하는 현상이 **Dendrite Nucleation** (핵 생성)의 전조 증상인 수리적 이유는?
3. **Pulse Charging** (펄스 충전) 기법이 **Concentration Overpotential** ($\eta_{conc}$)을 완화하여 플레이팅을 억제하는 물리적 메커니즘은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Intelligence/Battery electrochemical-impedance-spectroscopy
- 02_Knowledge/02_Battery/Intelligence/Battery degradation-physics
- 02_Knowledge/02_Battery/Intelligence/Battery state-of-health-soh-estimation

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
