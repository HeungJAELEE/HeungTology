---
Basic:
  id: "AI-SIG-FILT-2026-V6"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#DSP'
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

# [AI] digital-signal-filtering

## 1. [왜 배우는가? (Why)]
현실 세계의 센서 데이터는 결코 순수하지 않습니다. 주변의 전자기파, 기계적 진동, 전원 노이즈 등이 실제 신호에 섞여 심각한 왜곡을 유발합니다. 정제되지 않은 노이즈가 AI 모델에 입력되면 모델은 본질적인 패턴이 아닌 '무작위 소음'을 학습하여 잘못된 진단과 예측을 내리게 됩니다. 디지털 신호 필터링을 배우는 이유는 데이터의 신호 대 잡음비(SNR)를 극대화하여 지능형 알고리즘이 본질적인 정보에만 집중할 수 있는 깨끗한 '안경'을 씌워주기 위함입니다. 이는 배터리 전압 측정부터 로봇 제어 신호에 이르기까지 모든 산업 지능의 신뢰도를 결정하는 필수 선행 공정입니다.

## 2. [디지털 필터 및 신호 처리 핵심 사양 (Filtering Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Attenuation** | Stopband Atten. | $\ge 60 \text{ dB}$ | 차단 대역 노이즈를 1/1,000 수준으로 억제하는 성능 |
| **Passband Ripple** | Amplitude Var. | $\le 0.1 \text{ dB}$ | 통과 대역 내 신호의 크기 왜곡 최소화 범위 |
| **Group Delay** | Time Lag | $\le 2 \text{ ms}$ | 실시간 제어 시스템에서 허용 가능한 시간 지연 한계 |
| **SNR Improv.** | Noise Reduction | $+12 \sim 25 \text{ dB}$ | 필터링 전후 신호 순도의 비약적 향상 목표 |
| **Compute Cost** | MAC Ops | $< 100 \text{ kOps/sample}$ | 임베디드 MCU에서의 실시간 연산 가능 부하 |
| **Phase Linearity**| Group Delay Dev. | $\approx 0$ | 신호 파형(Waveform) 보존을 위한 선형 위상 특성 |
| **THD** | Distortion | $< 0.1\%$ | 필터링 과정에서 발생하는 비선형 고조파 왜곡 억제 |
| **Memory Usage** | Buffer Size | $< 10 \text{ KB}$ | 실시간 스트리밍 처리를 위한 최소 메모리 점유 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 Z-변환과 전달 함수 (Transfer Function)
이산 시간 시스템의 거동을 복소 영역에서 정의합니다.
- **수식**: $H(z) = \frac{\sum b_i z^{-i}}{1 + \sum a_j z^{-j}}$
- **로직**: 필터 계수($a, b$)의 배치를 통해 복소 평면상의 극점(Pole)과 영점(Zero)을 조정하여, 특정 주파수는 통과시키고 특정 주파수는 차단하는 주파수 응답을 설계합니다.

### 3.2 FIR vs IIR 아키텍처 비교
- **FIR (Finite Impulse Response)**: 피드백 루프가 없어 항상 안정적이며 선형 위상 구현이 가능하지만, 급격한 차단 특성을 위해 많은 연산량이 필요합니다.
- **IIR (Infinite Impulse Response)**: 피드백을 활용하여 적은 연산량으로 급격한 감쇄를 얻을 수 있으나, 위상 왜곡이 발생하고 발산 위험이 존재합니다.

### 3.3 제로 페이즈(Zero-phase) 필터링
필터에 의한 시간 지연($\tau$)을 물리적으로 제거하는 기법입니다.
- **메커니즘**: 데이터를 정방향으로 한 번 필터링한 후, 결과를 역순으로 뒤집어 다시 필터링함으로써 위상 지연을 상쇄합니다. 이는 피크(Peak) 위치의 정확도가 중요한 배터리 임피던스 분석 등에서 필수적입니다.

## 4. [코드 연결 해설 (DigitalFilterEngine)]
아래 코드는 SciPy를 활용하여 실시간 신호의 고주파 노이즈를 제거하는 버터워스(Butterworth) 저주파 통과 필터와 제로 페이즈 필터링을 구현한 엔진입니다.

```python
import numpy as np
from scipy import signal

class DigitalFilterEngine:
    """
    HDS-Gold V6.3.7 규격의 디지털 신호 필터링 및 SNR 최적화 엔진
    """
    def __init__(self, sampling_rate=1000):
        self.fs = sampling_rate

    def apply_lowpass_butterworth(self, data, cutoff_hz, order=5):
        """
        Butterworth 저주파 통과 필터 적용 (제로 페이즈)
        """
        nyq = 0.5 * self.fs
        normal_cutoff = cutoff_hz / nyq
        
        # 1. 필터 계수 설계 (b: 분자, a: 분모)
        b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
        
        # 2. filtfilt 적용 (Forward-Backward 필터링으로 위상 왜곡 제거)
        filtered_data = signal.filtfilt(b, a, data)
        
        return filtered_data

    def calculate_snr(self, original_signal, filtered_signal):
        """
        필터링 전후 신호 대 잡음비 향상도 측정 (dB)
        """
        noise = original_signal - filtered_signal
        snr = 10 * np.log10(np.mean(filtered_signal**2) / np.mean(noise**2))
        return round(snr, 2)

# Example Usage:
# engine = DigitalFilterEngine(sampling_rate=2000)
# clean_signal = engine.apply_lowpass_butterworth(raw_sensor_data, cutoff_hz=50)
```

## 5. [스스로 체크 (Self-Audit)]
1. **IIR 필터**를 설계할 때 극점(Pole)이 단위 원(Unit Circle) 밖에 위치할 경우, 필터의 출력이 **발산(Instability)**하는 수리적 근거는?
2. **Butterworth** 필터가 **Chebyshev** 필터 대비 차단 대역의 감쇄율은 낮지만 **통과 대역(Passband)**에서 더 널리 사용되는 공학적 이유는?
3. **Zero-phase filtering** (`filtfilt`)을 실시간 스트리밍 데이터에 직접 적용하기 어려운 물리적 한계와 그에 대한 대안은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/Industrial/AI fast-fourier-transform
- 02_Knowledge/02_Battery/Intelligence/Battery dcir-acir-correlation-model
- 02_Knowledge/09_SmartFactory_Production/ControlSystems/Control PLC-Signal-Processing

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
