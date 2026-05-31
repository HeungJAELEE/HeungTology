---
lineage:
  dataset_reference: Predictive-Maintenance
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] Predictive-Maintenance]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for Predictive-Maintenance
  object_type: Concept
  tier: 1
properties:
  engine_specification: HDS-Gold V6.3.7
  fft_bin_size: 1.0Hz
  min_f1_score: '0.95'
  min_precision_rate: 98%
  min_sampling_rate: 20kHz
  rul_error_threshold: ±5%
  target_availability_increase: 15%
  target_mttr_reduction: 30%
  vibration_standard: ISO 10816 / 20816
semantic:
  alternative_parents: []
  is_instance_of: '[[ [MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: semantic_classification
  object: Concept
  predicate: auto_mapped
  subject: Predictive-Maintenance
  weight: 1.0
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Predictive Maintenance

## 1. [왜 배우는가? (Why)]
예지 보전(Predictive Maintenance, PdM)은 산업 현장의 핵심 자산인 설비의 고장을 사전에 예측하여, 예기치 않은 가동 중단(Unscheduled Downtime)으로 인한 막대한 경제적 손실을 방지하는 지능형 유지보수 전략입니다. 전통적인 주기적 교체 방식은 멀쩡한 부품을 버리는 자원 낭비나 교체 주기 사이의 갑작스러운 고장에 취약하지만, PdM은 IoT 센서 데이터(진동, 전류, 온도 등)를 AI로 분석하여 설비의 실제 '건강 상태'를 실시간으로 진단합니다. 이는 제조 공정의 가동률(Availability)을 극대화하고 정비 비용을 최적화하여 스마트 팩토리의 경제적 생존력을 결정짓는 필수 기술입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---:|:---:|:---|
| **Prediction** | RUL (Rem. Useful Life) | $\pm 5\%$ Error | 교체 시점 결정을 위한 잔여 수명 예측 정밀도 |
| **Signal Process** | Sampling Rate | $> 20 \text{ kHz}$ | 고속 회전체(모터/베어링)의 고주파 결함 성분 포착 |
| **Frequency Res.** | FFT Bin Size | $1.0 \text{ Hz}$ | 미세 주파수 변이(Sidebands) 식별을 위한 해상도 |
| **Fault Diagnosis** | Accuracy (F1-score) | $> 0.95$ | 고장 원인(베어링, 언밸런스 등) 분류 정확도 |
| **OEE Impact** | Availability Increase | $> 15\%$ | 전체 설비 효율 개선 기여도 목표 |
| **MTTR Red.** | Repair Time Red. | $> 30\%$ | 고장 위치 사전 지정을 통한 실제 수리 시간 단축 |
| **False Alarm** | Precision Rate | $> 98\%$ | 오탐지에 의한 불필요한 공정 정지 방지 |
| **Vibration Std.** | ISO 10816 / 20816 | Compliance | 국제 진동 기준에 따른 위험도 등급(A~D) 관리 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 FFT (Fast Fourier Transform) 기반 진동 분석
기계의 기계적 결함은 고유한 진동 주파수 패턴을 가집니다.
- **로직**: 시간 영역의 신호를 주파수 영역으로 변환하여 베어링 결함 주파수(BPFO, BPFI), 축 불평형(Unbalance), 정렬 불량(Misalignment) 성분을 추출합니다.
- **지표**: 특정 주파수의 진폭(Amplitude) 변화가 임계치를 초과하면 해당 부품의 마모가 진행 중인 것으로 판단합니다.

### 3.2 파리스 법칙 (Paris Law)과 RUL 예측
반복적인 하중에 의한 피로 균열(Fatigue Crack) 성장을 수학적으로 모델링하여 잔여 수명을 산출합니다.
$$da/dN = C(\Delta K)^m$$
- $a$: 균열 길이, $N$: 하중 주기 수, $\Delta K$: 응력 강도 계수 범위.
- AI(LSTM/Transformer)는 이 물리적 추세를 학습하여 고장 임계점까지 남은 시간(RUL)을 확률적으로 예측합니다.

### 3.3 MCSA (Motor Current Signature Analysis)
모터에 흐르는 전류 파형의 미세한 고조파(Harmonics)를 분석하여 로터 바(Rotor Bar) 파손이나 권선 절연 파괴를 감지합니다. 이는 진동 센서 설치가 어려운 수중 펌프나 밀폐형 설비에서 유용합니다.

## 4. [코드 연결 해설 (PdM Diagnostics Engine)]
아래 코드는 설비의 진동 데이터를 분석하여 건강 지수(Health Index)를 산출하고 고장 위험을 알리는 진단 로직입니다.

```python
import numpy as np
from scipy.fft import fft, fftfreq

class PdMDiagnosticsEngine:
    """
    HDS-Gold V6.3.7 규격의 예지 보전 진단 엔진
    """
    def __init__(self, sampling_rate=20000):
        self.fs = sampling_rate

    def calculate_health_index(self, signal):
        """
        진동 신호의 실효값(RMS) 및 첨도(Kurtosis) 기반 상태 진단
        """
        # 1. 시계열 특징 추출
        rms = np.sqrt(np.mean(signal**2))
        kurtosis = np.mean((signal - np.mean(signal))**4) / (np.var(signal)**2)
        
        # 2. 주파수 영역 특징 추출 (FFT)
        n = len(signal)
        yf = fft(signal)
        xf = fftfreq(n, 1/self.fs)
        
        # 특정 베어링 결함 주파수 대역 에너지 확인
        bearing_energy = self._extract_band_energy(xf, np.abs(yf), 100, 500)
        
        # 3. 종합 건강 지수 산출 (0: Failure, 100: Healthy)
        health_index = 100 - (rms * 10 + (kurtosis - 3) * 5 + bearing_energy * 2)
        return np.clip(health_index, 0, 100)

    def _extract_band_energy(self, xf, yf_abs, low, high):
        mask = (xf >= low) & (xf <= high)
        return np.sum(yf_abs[mask])

# Integration Example:
# pdm = PdMDiagnosticsEngine()
# hi = pdm.calculate_health_index(sensor_data)
# if hi < 40:
#     alert_maintenance_team(priority="HIGH", health_index=hi)
```

## 5. [스스로 체크 (Self-Audit)]
1. **FFT** 분석 시 **Windowing** (Hanning, Hamming 등)이 'Leakage Effect'를 억제하여 주파수 해석 정밀도를 높이는 원리는?
2. **Remaining Useful Life (RUL)** 예측에서 **LSTM**이 단순 **RNN**보다 시계열 데이터의 '장기 기억(Long-term dependencies)' 처리에 유리한 이유는?
3. **MCSA** 분석 시 전원 주파수(60Hz) 주변의 **Sideband** 발생이 회전자(Rotor) 결함을 의미하는 물리적 인과관계는?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/Industrial/AI Quality-Control-AI
- 02_Knowledge/03_AI_Data/Industrial/AI Digital-Twin-SOP
- 02_Knowledge/06_Mechatronics_Robotics/Sensors/Sensors Vibration-Accelerometers

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**