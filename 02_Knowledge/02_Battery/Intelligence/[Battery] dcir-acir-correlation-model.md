---
Basic:
  id: "BAT-RES-CORR-2026-V6"
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
  tags: - '#DCIR'
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

# [[[Battery] dcir-acir-correlation-model

## 1. [왜 배우는가? (Why)]]
배터리의 내부 저항은 단일 상수가 아니라, 반응 속도에 따른 시상수(Time Constant)의 집합입니다. DCIR(Direct Current Internal Resistance)은 거시적인 시간 도메인(Time Domain) 데이터이며, ACIR(Alternating Current Internal Resistance)은 주파수 도메인(Frequency Domain)의 미시적 데이터입니다. 이 두 세계를 연결하는 상관관계 모델을 구축하는 것은, 고가의 EIS(Electrochemical Impedance Spectroscopy) 장비 없이도 주행 중 발생하는 전류 펄스(DCIR)만으로 배터리의 계면 저항과 내부 건강 상태를 마이크로초 단위로 정밀 추론하기 위함입니다. 이는 '가상 EIS(Virtual EIS)' 기술의 핵심 물리 기반입니다.

## 2. [DCIR 및 ACIR 상관관계 핵심 사양 (Correlation Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Mapping Accuracy**| Mean Absolute Error | $< 5\%$ | DCIR 펄스 데이터로부터 추정된 ACIR 성분의 정확도 |
| **Correlation Coeff.**| Pearson's $r$ | $> 0.98$ | 시간 도메인 $R_{ohmic}$과 주파수 도메인 $R_0$의 일치성 |
| **Sampling Freq.** | Real-time Sensing | $\ge 10 \text{ kHz}$ | DCIR 펄스에서 Ohmic/CT 성분을 분리하기 위한 최소 주기 |
| **Response Domain** | Frequency Range | $0.1 \text{ Hz} \sim 1 \text{ kHz}$ | Ohmic, 전하 이동, 확산 영역을 모두 포괄하는 상관 범위 |
| **Temp. Sensitivity**| Resistance Shift | $\pm 5\% / ^\circ\text{C}$ | 온도 변화에 따른 저항 성분별(R_ohmic, R_ct) 보정 계수 |
| **Compute Latency** | Inference Speed | $< 100 \text{ ms}$ | BMS 엣지 기기에서 실시간 상태 진단을 위한 연산 속도 |
| **SOC Applicability**| Valid Range | $10 \sim 90\%$ | SOC 변화에 따른 비선형 저항 거동 반영 및 유효 범위 |
| **Pulse Duration** | HPPC Standard | $1, 10, 30 \text{ sec}$ | DCIR 측정 시 과도 응답 분석을 위한 표준 펄스 기간 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 등가 회로 모델 (Equivalent Circuit Model, ECM)
배터리의 물리적 거동을 저항(R)과 커패시터(C)의 조합으로 묘사합니다.
- **수식**: $Z(\omega) = R_0 + \sum \frac{R_i}{1 + j\omega R_i C_i}$
- **로직**: DCIR의 즉각적인 전압 강하는 $R_0$(Ohmic)와 일치하며, 지수적 회복 곡선은 $R_i C_i$ 병렬 루프(Charge Transfer)의 시상수와 주파수 도메인의 반원(Nyquist arc) 지름에 대응합니다.

### 3.2 콜-콜(Cole-Cole) 모델과 완화 시간 (Relaxation Time)
비이전압 분포를 고려한 저항 모델입니다.
- **수식**: $Z(\omega) = R_{\infty} + \frac{R_0 - R_{\infty}}{1 + (j\omega\tau)^{\alpha}}$
- **의미**: 배터리 내부의 복잡한 물리적 층(SEI 등)에 의한 불균일한 시상수를 분산 지수($\alpha$)를 통해 표현하며, 이를 통해 DCIR의 전압 완화(Relaxation) 속도를 주파수 영역의 임피던스로 변환합니다.

### 3.3 타임-프리퀀시 브릿지 (DRT 분석)
이완 시간 분포(Distribution of Relaxation Times) 분석을 통해, DCIR의 시계열 데이터를 주파수 성분별 기여도로 분해합니다. 이를 통해 각 저항 성분이 리튬 플레이팅(Plating)이나 SEI 성장 중 어느 현상에 기인하는지 정량적으로 분리합니다.

## 4. [코드 연결 해설 (BatteryResistanceModel)]
아래 코드는 전류 펄스(DCIR) 데이터로부터 Ohmic 저항과 전하 이동(Charge Transfer) 저항을 분리하여 산출하고, 이를 주파수 도메인의 ACIR과 매핑하는 분석 엔진입니다.

```python
import numpy as np

class BatteryResistanceModel:
    """
    HDS-Gold V6.3.7 규격의 DCIR-ACIR 상관관계 및 저항 진단 엔진
    """
    def __init__(self, sampling_rate_hz=10000):
        self.fs = sampling_rate_hz

    def extract_resistances(self, voltage_trace, current_pulse_a):
        """
        DCIR 펄스 응답으로부터 Ohmic 및 CT 저항 분리 추출
        """
        dv = np.diff(voltage_trace)
        di = current_pulse_a
        
        # 1. Ohmic Resistance (즉각 강하: t < 1ms)
        # 고속 샘플링(10kHz) 시 첫 번째 데이터 포인트가 Ohmic 성분 반영
        r_ohmic = abs(dv[0] / di)
        
        # 2. Total Resistance (t = 10s 시점)
        r_total = abs((voltage_trace[-1] - voltage_trace[0]) / di)
        
        # 3. Polarization (Charge Transfer + Diffusion)
        r_pol = r_total - r_ohmic
        
        return {
            "R_ohmic_ohm": round(r_ohmic, 6),
            "R_total_ohm": round(r_total, 6),
            "R_polarization_ohm": round(r_pol, 6),
            "R_ct_estimate": round(r_pol * 0.7, 6) # 단순화된 CT 추정 비율
        }

    def correlate_with_acir(self, r_ohmic_dc, r_acir_1khz):
        """
        DCIR Ohmic 저항과 ACIR 1kHz 측정값의 상관계수 산출
        """
        error = abs(r_ohmic_dc - r_acir_1khz) / r_acir_1khz
        return 1.0 - error

# Example Usage:
# model = BatteryResistanceModel()
# v_data = np.array([3.7, 3.65, 3.64, 3.635, 3.63]) # 펄스 인가 시 전압 변화
# results = model.extract_resistances(v_data, current_pulse_a=50)
```

## 5. [스스로 체크 (Self-Audit)]
1. **LFP 배터리**의 전압 평탄 구역에서 **DCIR**을 측정할 때, 전압 강하량($\Delta V$)이 작아 발생하는 측정 노이즈가 **Virtual EIS** 정확도에 미치는 영향은?
2. **ACIR 1kHz** 저항과 **DCIR 0.1s** 저항 중 배터리 내부의 **전해액 전도도(Electrolyte Conductivity)** 변화를 더 민감하게 반영하는 지표는?
3. **Cole-Cole 모델**의 분산 지수($\alpha$)가 1에서 멀어질수록(0.6~0.8) 배터리 내부의 **계면 상태(Heterogeneity)**가 어떻게 변했음을 의미하는가?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Intelligence/Battery eis-impedance-spectroscopy-analysis
- 02_Knowledge/02_Battery/Systems/Battery bms-algorithm-kalman
- 02_Knowledge/03_AI_Data/Industrial/AI time-series-forecasting-diagnostics

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
