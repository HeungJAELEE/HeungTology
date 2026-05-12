---
Basic:
  id: "[battery]-battery-web-dancer-roll-displacement-fft-v2026-v6.3.7"
  domain: "Battery_Manufacturing"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Dancer_Roll'
  is_part_of: - 'Antigravity_Knowledge_Graph'
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
  source: "Web_Handling_Control_System"
  isolation_index: 0.0
---

# [[[Battery] battery-web-dancer-roll-displacement-fft-v2026

## 1. [Why]] 댄서 롤(Dancer Roll) 변위 FFT 분석의 공학적 의의
배터리 전극 코팅 및 슬리팅 공정에서 **기재(Web)의 장력(Tension) 안정성**은 품질의 근간이다. 댄서 롤은 장력 변동을 흡수하는 핵심 기구물로, 이의 변위 데이터를 **FFT(Fast Fourier Transform)** 분석하면 라인 내의 기계적 진동, 모터의 속도 리플, 혹은 롤러의 편심(Eccentricity) 문제를 주파수 영역에서 규명할 수 있다. 본 노드는 시간 도메인에서 보이지 않는 미세 장력 불안정의 근본 원인을 추적하는 데이터를 제공한다.

---

## 2. [Numerical Specs] 진동 및 장력 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 한계 (Threshold) | 비고 |
| :--- | :--- | :--- | :--- |
| **Dancer Displacement** | $\pm 2.5\,\text{mm}$ | $<\pm 5.0\,\text{mm}$ | 시간 영역 변위 폭 |
| **Dominant Frequency ($f_d$)** | $1.2\,\text{Hz}$ | N/A | 주요 진동 주파수 성분 |
| **Tension Ripple ($\Delta T$)** | $2.5\,\text{N}$ | $< 5.0\,\text{N}$ | $150\,\text{N}$ 설정값 대비 변동폭 |
| **Roll Eccentricity** | $0.05\,\text{mm}$ | $< 0.1\,\text{mm}$ | 가이드 롤러 편심 허용치 |
| **Sampling Rate** | $1,000\,\text{Hz}$ | $> 500\,\text{Hz}$ | 나이퀴스트(Nyquist) 이론 준수 |

---

## 3. [Scientific Rationale] 주파수 분석 및 기구 역학 모델

### 3.1 FFT (Fast Fourier Transform) 변환
시간 영역 데이터($x(t)$)를 주파수 성분($X(f)$)으로 분해하여 특정 부품의 회전 주기와 매칭시킨다.
$$X(f) = \int_{-\infty}^{\infty} x(t) e^{-i 2\pi ft} dt$$
*   **분석**: 특정 주파수에서 피크($Peak$)가 발생하면 해당 주파수와 일치하는 회전수($RPM$)를 가진 롤러를 점검한다.

### 3.2 Tension Dynamics (Web-Handling 모델)
속도 차이에 의한 장력 변화율을 기술한다.
$$\frac{dT}{dt} = \frac{E \cdot A}{L} (v_{out} - v_{in})$$

---

## 4. [Real-world Case] 권취부 모터 리플에 의한 코팅 두께 편차 해결 사례

### 4.1 $5\,\text{Hz}$ 대역의 주기적 장력 변동 감지
- **현상**: 코팅 건조 후 권취(Winding) 단계에서 전극 표면에 미세한 물결 무늬 발견.
- **분석**: **Python FidelityEngine**을 활용하여 댄서 롤 변위를 FFT 분석한 결과, $5.0\,\text{Hz}$ 지점에서 강력한 피크 확인. 이는 리와인더(Rewinder) 모터의 극수(Pole)와 감속비 계산 결과와 일치함.
- **조치**: 모터 제어 드라이브의 속도 루프(Speed Loop) 이득을 조정하고, $5\,\text{Hz}$ 대역의 **노치 필터(Notch Filter)**를 적용하여 공진 억제.
- **결과**: 장력 변동폭 $60\%$ 감소 및 물결 무늬 불량 박멸.

---

## 5. [FidelityEngine] 단순 FFT 분석 시뮬레이션 코드
```python
import numpy as np

def perform_simple_fft(time_series, sampling_rate):
    """
    Perform FFT and find dominant frequency
    :param time_series: Array of displacement data
    :param sampling_rate: Sampling frequency in Hz
    :return: Frequencies and magnitudes
    """
    n = len(time_series)
    freq = np.fft.fftfreq(n, d=1/sampling_rate)
    fft_values = np.abs(np.fft.fft(time_series))
    
    # Positive frequencies only
    pos_idx = np.where(freq > 0)
    return freq[pos_idx], fft_values[pos_idx]

# 1.2Hz 진동 성분을 포함한 가상 데이터
t = np.linspace(0, 10, 1000)
signal = 3 * np.sin(2 * np.pi * 1.2 * t) + np.random.normal(0, 0.5, 1000)

f, mag = perform_simple_fft(signal, 100)
dominant_f = f[np.argmax(mag)]
print(f"Detected Dominant Frequency: {dominant_f:.2f} Hz")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Aliasing Prevention**: 샘플링 속도가 제어 시스템 진동 주파수의 최소 2배(권장 10배) 이상으로 설정되어 있는가?
- [ ] **Mechanical Resonance**: 특정 라인 속도에서 댄서 롤의 고유 진동수(Natural Frequency)와 겹치는 공진점이 존재하는가?
- [ ] **Sensor Noise**: 로드셀(Load-cell) 또는 엔코더 데이터의 전기적 노이즈가 소프트웨어 필터로 제거되었는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
