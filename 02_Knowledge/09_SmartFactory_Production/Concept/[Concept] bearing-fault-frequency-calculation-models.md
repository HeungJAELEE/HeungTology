---
lineage:
  dataset_reference: Vibration Diagnostics Handbook (ISO 15242)
  original_author: Antigravity Vault
  original_hash: 625c7a4f3e9d2fadc99342fabb008fb0ea8234c5da783a913fd4087f283aa4d2
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-20'
  domain: 09_SmartFactory_Production
  id: '[[[09_SmartFactory_Production] [Concept] bearing-fault-frequency-calculation-models]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: 회전 기계 베어링의 기하학적 형상과 축 회전 속도를 기반으로 한 베어링 결함 주파수(BPFI, BPFO, BSF, FTF)
    계산 이론 및 수학적 모델링
  object_type: Algorithm
  tier: 1
properties:
  bearing_failure_contribution_percent: 40.0
  contact_angle_degree: 15.0
  number_of_rolling_elements: 9.0
  pitch_diameter_mm: 120.0
  rolling_element_diameter_mm: 22.0
  shaft_rotational_frequency_hz: 30.0
  slip_induced_frequency_shift_percent:
  - 1.0
  - 2.0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Smart-Manufacturing-Hub]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Section 5.3'
  intent: parameter_dependency
  object: pitch_diameter, roller_diameter, contact_angle, roller_number
  predicate: calculated_by_geometric_parameters
  subject: bearing-fault-frequency
  weight: 0.9
- evidence_coordinate: '[데이터 부재] Section 3.1'
  intent: semantic_definition
  object: ball_pass_frequency_outer_race
  predicate: represents
  subject: bpfo
  weight: 1.0
temporal:
  valid_from: '2026-05-20T12:52:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Bearing Fault Frequency Calculation Models (베어링 결함 주파수 계산 모델)

## 1. [왜 배우는가? (Why)]
모터, 송풍기, 펌프 등 회전 기계(Rotating Machinery)에서 발생하는 기계적 고장의 약 $40.0\%$ 이상은 구름 베어링(Rolling Element Bearing)의 손상에서 기인합니다. 베어링의 내륜(Inner Race), 외륜(Outer Race), 전동체(Ball/Roller) 또는 리테이너(Cage)에 미세한 크랙이나 박리(Flaking)가 발생하면, 회전축의 회전에 의해 전동체가 손상 부위와 충돌하면서 주기적인 충격 신호를 발생시킵니다. 
이 충격 신호는 시간 영역에서는 매우 짧은 펄스 형태를 나타내지만, 주파수 영역에서는 고유한 고장 주파수(Fault Frequencies) 성분으로 나타납니다. 
베어링의 기하학적 제원(접촉각, 전동체 직경, 피치 직경, 전동체 수)과 샤프트의 회전 속도를 기반으로 고장 주파수를 수학적으로 예측하는 것은 설비의 예측 보전(Predictive Maintenance, PdM) 시스템에서 고장 상태 및 부위를 정밀하게 진단하기 위한 필수적인 공학적 토대입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
베어링 결함 주파수 계산 모델 설계를 위한 기본 기하학 및 작동 사양은 다음과 같습니다.

| 파라미터명 | 설명 | 기준값 | 제어 한계 | 단위 | 적용 공식 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $f_r$ | 샤프트 회전 속도 (Shaft Rotational Frequency) | $30.0$ | $0.0 \sim 300.0$ | $\text{Hz}$ | - |
| $D$ | 베어링 피치 직경 (Pitch Diameter) | $120.0$ | $10.0 \sim 1000.0$ | $\text{mm}$ | $D = \frac{d_{in} + d_{out}}{2}$ |
| $d$ | 볼/롤러 직경 (Rolling Element Diameter) | $22.0$ | $2.0 \sim 100.0$ | $\text{mm}$ | - |
| $N$ | 전동체의 개수 (Number of Rolling Elements) | $9.0$ | $5.0 \sim 50.0$ | $\text{ea}$ | - |
| $\alpha$ | 베어링 접촉각 (Contact Angle) | $15.0$ | $0.0 \sim 45.0$ | $\text{degree}$ | - |

## 3. [공학적 원리 및 수식 유도 (Scientific Rationale)]

### 3.1 내/외륜 및 전동체 결함 주파수의 수학적 모델링
볼 베어링에서 전동체가 내륜 및 외륜의 한 점을 통과할 때 발생하는 충격 주파수는 단순 기하학적 속도 관계로부터 유도됩니다. 샤프트의 회전 속도를 $f_r$, 전동체가 궤도를 따라 공전하는 평균 속도를 기하학적 비율로 환산하여 다음 4가지 기본 결함 주파수 모델을 도출합니다.

#### 3.1.1 BPFO (Ball Pass Frequency Outer Race)
전동체가 외륜의 결함 부위를 통과하는 주파수입니다. 외륜은 일반적으로 고정되어 있다고 가정합니다.
$$f_{BPFO} = \frac{N}{2}f_r\left(1 - \frac{d}{D}\cos\alpha\right)$$

#### 3.1.2 BPFI (Ball Pass Frequency Inner Race)
전동체가 회전하는 내륜의 결함 부위를 통과하는 주파수입니다. 샤프트와 내륜이 동기화되어 회전하므로 상대 주파수가 적용되어 외륜보다 높은 주파수 값을 가집니다.
$$f_{BPFI} = \frac{N}{2}f_r\left(1 + \frac{d}{D}\cos\alpha\right)$$

#### 3.1.3 BSF (Ball Spin Frequency)
볼 또는 롤러 자체의 결함 부위가 내/외륜 궤도면과 충돌하는 자전 주파수입니다.
$$f_{BSF} = \frac{D}{2d}f_r\left(1 - \left(\frac{d}{D}\cos\alpha\right)^2\right)$$

#### 3.1.4 FTF (Fundamental Train Frequency)
리테이너(Cage)가 회전하는 공전 주파수입니다.
$$f_{FTF} = \frac{1}{2}f_r\left(1 - \frac{d}{D}\cos\alpha\right)$$

### 3.2 접촉각 ($\alpha$) 및 미끄러짐(Slip) 효과에 의한 수리적 변동성
위 공식들은 전동체와 레이스 사이에 순수한 구름 접촉(Pure Rolling Contact)만 존재한다고 가정하여 도출된 이상적인 주파수입니다. 
그러나 실제 현장에서는 고부하, 불충분한 예압(Preload) 또는 윤활 상태 불량으로 인해 미세한 슬립(Slip)이 발생합니다. 
이로 인해 실측 주파수는 이론 주파수 대비 일반적으로 약 $1.0\% \sim 2.0\%$ 정도의 주파수 천이(Frequency Shift)를 나타내며, 신호 처리 장치에서는 이를 보정하기 위해 엔벨로프(Envelope) 분석 및 복조(Demodulation) 기법을 사용합니다.

## 4. [진단 코드 (Diagnostic Code)]
베어링 기하학적 변수와 축 속도를 입력받아 이상적인 결함 주파수 4종을 계산하고 슬립 마진을 포함한 탐색 윈도우 범위를 출력하는 Python 모듈입니다.

```python
import numpy as np

class BearingFaultFrequencyCalculator:
    def __init__(self, pitch_diam, roller_diam, num_rollers, contact_angle_deg):
        self.D = float(pitch_diam)
        self.d = float(roller_diam)
        self.N = float(num_rollers)
        self.alpha = np.radians(float(contact_angle_deg))

    def calculate_frequencies(self, shaft_speed_hz):
        fr = float(shaft_speed_hz)
        cos_alpha = np.cos(self.alpha)
        d_over_D_cos = (self.d / self.D) * cos_alpha

        # Defect frequencies calculation
        bpfo = (self.N / 2.0) * fr * (1.0 - d_over_D_cos)
        bpfi = (self.N / 2.0) * fr * (1.0 + d_over_D_cos)
        bsf = (self.D / (2.0 * self.d)) * fr * (1.0 - (d_over_D_cos ** 2))
        ftf = 0.5 * fr * (1.0 - d_over_D_cos)

        # Apply 1.5% slip margin window for real-world detection
        margin = 0.015
        return {
            'BPFO': {'theoretical': bpfo, 'range': (bpfo * (1 - margin), bpfo * (1 + margin))},
            'BPFI': {'theoretical': bpfi, 'range': (bpfi * (1 - margin), bpfi * (1 + margin))},
            'BSF': {'theoretical': bsf, 'range': (bsf * (1 - margin), bsf * (1 + margin))},
            'FTF': {'theoretical': ftf, 'range': (ftf * (1 - margin), ftf * (1 + margin))}
        }

if __name__ == "__main__":
    # Test for standard deep groove ball bearing 6205 at 1800 RPM (30 Hz)
    calculator = BearingFaultFrequencyCalculator(D=39.0, d=7.94, num_rollers=9.0, contact_angle_deg=0.0)
    report = calculator.calculate_frequencies(shaft_speed_hz=30.0)
    for fault_type, values in report.items():
        print(f"{fault_type}: Theoretical = {values['theoretical']:.2f} Hz | Search Window = [{values['range'][0]:.2f}, {values['range'][1]:.2f}] Hz")
```

## 5. [스스로 체크 (Self-Audit)]
1. **베어링 슬립(Slip)**이 주파수 도메인에서 결함 주파수 피크의 선폭을 넓히는 현상(Spectral Leakage 또는 Peak Smearing)의 물리적 메커니즘은 무엇인가?
2. 축방향 과도 부하(Axial Load)가 작용하여 실제 접촉각 $\alpha$가 이상적인 설계 값보다 증가할 경우, $f_{BPFI}$와 $f_{BPFO}$ 값의 변화 경향을 수학적으로 비교 설명하시오.
3. 베어링의 각 진동 신호를 획득할 때, 고주파 대역통과 필터와 복조(Demodulation) 처리를 수행하는 **Envelope Analysis** 기법이 저주파 배경 노이즈가 강한 환경에서 초기 결함 충격 성분을 검출하는 데 유리한 공학적 이유는 무엇인가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[MOC] Smart-Manufacturing-Hub]]`
- `[[[Entity] control-systems-and-signal-processing-engineering]]`
- `[[[Entity] predictive-maintenance-and-industrial-iot-iiot-analytics]]`
- `[[[Data] manufacturing-iiot-high-speed-vibration-data-v2026]]`