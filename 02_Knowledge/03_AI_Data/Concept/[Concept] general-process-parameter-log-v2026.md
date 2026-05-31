---
lineage:
  dataset_reference: general-process-parameter-log-v2026
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] general-process-parameter-log-v2026]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for general-process-parameter-log-v2026
  object_type: Data
  tier: 1
properties:
  analysis_engine: Python FidelityEngine
  flow_rate_resolution: 0.05L/min
  flow_rate_sampling_period: 0.5s
  normalization_range: 0-1
  power_consumption_resolution: 0.1kW
  power_consumption_sampling_period: 5s
  pressure_resolution: 0.01bar
  pressure_sampling_period: 0.1s
  temp_resolution: 0.1C
  temp_sampling_period: 1s
  time_sync_protocol: NTP
  vibration_resolution: 0.01g
  vibration_sampling_period: 0.001s
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: semantic_classification
  object: Concept
  predicate: auto_mapped
  subject: general-process-parameter-log-v2026
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

# [Concept] General Process Parameter Log V2026

## 1. [Why]] 범용 공정 파라미터 로그의 통합적 의의
산업 현장의 수많은 설비는 각기 다른 물리적 단위(온도, 압력, 유량, 진동 등)의 데이터를 쏟아낸다. **범용 공정 파라미터 로그**는 이질적인 센서 데이터들을 통합하고 정규화(Normalization)하여, 특정 도메인에 국한되지 않는 거시적인 공정 추세와 상관관계를 분석할 수 있는 기반을 제공한다. 이는 다학제적(Multi-disciplinary) 문제 해결과 공장 전체의 최적화를 위한 필수 원천 데이터다.


## 2. [Numerical Specs] 공정 센서 통합 파라미터 (Numerical Specs)

| 데이터 유형 | 표준 단위 (SI) | 샘플링 주기 (Avg) | 정밀도 (Resolution) | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| **Temperature** | $^\circ\text{C}$ (Celsius) | $1\,\text{sec}$ | $0.1^\circ\text{C}$ | RTD/Thermocouple |
| **Pressure** | $\text{bar}$ | $0.1\,\text{sec}$ | $0.01\,\text{bar}$ | 압력 트랜스듀서 |
| **Flow Rate** | $\text{L/min}$ | $0.5\,\text{sec}$ | $0.05\,\text{L/min}$ | 질량/부피 유량계 |
| **Vibration** | $\text{mm/s}^2$ | $0.001\,\text{sec}$ | $0.01\,\text{g}$ | 가속도계 (High freq) |
| **Power Consumption** | $\text{kW}$ | $5\,\text{sec}$ | $0.1\,\text{kW}$ | 전력량계 |


## 3. [Scientific Rationale] 데이터 정규화 및 상관 분석 모델

### 3.1 Min-Max Normalization (데이터 정규화)
서로 다른 스케일을 가진 데이터들을 $0 \sim 1$ 사이의 값으로 변환하여 비교 분석을 용이하게 한다.
$$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$

### 3.2 Cross-Correlation Analysis (상관관계 분석)
두 신호($X, Y$) 간의 시간 지연($\tau$)에 따른 유사성을 분석하여 인과관계를 파악한다.
$$R_{xy}(\tau) = \int_{-\infty}^{\infty} X(t) Y(t+\tau) dt$$
*   **분석**: 압력 급증($X$) 후 5초 뒤 온도 상승($Y$)이 나타난다면, 압력 변화가 온도의 주요 변수임을 도출할 수 있다.


## 4. [Real-world Case] 이기종 센서 데이터 융합을 통한 원인 불명 불량 규명 사례

### 4.1 압력과 진동의 상관관계 분석을 통한 펌프 파손 예방
- **현상**: 화학 용액 이송 라인에서 토출 압력이 주기적으로 미세하게 요동치나(Hunting), 에러 알람은 발생하지 않음.
- **분석**: **Python FidelityEngine**을 활용하여 압력 로그와 펌프 베이스의 진동 로그를 **Cross-correlation** 분석한 결과, 진동 주파수가 압력 변동보다 $0.2\,\text{sec}$ 앞서 발생함을 포착.
- **조치**: 펌프 임펠러(Impeller)에 이물질이 끼어 균형이 깨진 것으로 진단하고 즉시 세척 실시.
- **결과**: 펌프 축 파손 및 대규모 누출 사고 사전 방지.


## 5. [FidelityEngine] 데이터 정규화 및 상관도 계산 코드
```python
import numpy as np

def normalize_and_correlate(signal_a, signal_b):
    """
    Normalize two signals and calculate correlation
    :return: Normalized signals and max correlation index
    """
    s_a = np.array(signal_a)
    s_b = np.array(signal_b)
    
    # Normalize
    n_a = (s_a - np.min(s_a)) / (np.max(s_a) - np.min(s_a))
    n_b = (s_b - np.min(s_b)) / (np.max(s_b) - np.min(s_b))
    
    # Simple correlation
    correlation = np.correlate(n_a, n_b, mode='full')
    return n_a, n_b, np.argmax(correlation)

# 가상 데이터 (신호 B가 신호 A보다 2 스텝 지연)
a = [1, 2, 3, 4, 5, 4, 3]
b = [0, 0, 1, 2, 3, 4, 5]

na, nb, peak_idx = normalize_and_correlate(a, b)
print(f"Max Correlation Peak Index: {peak_idx}")
```


## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Unit Consistency**: 모든 데이터가 시스템 전반의 표준 단위(SI)로 변환되어 기록되는가?
- [ ] **Time Sync**: 서로 다른 설비에서 올라오는 데이터의 타임스탬프가 NTP(Network Time Protocol)를 통해 동기화되어 있는가?
- [ ] **Outlier Handling**: 센서 노이즈나 통신 오류에 의한 튀는 값(Outlier)이 필터링된 후 분석에 사용되는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**