---
Basic:
  date: '2026-05-12'
  domain: Semiconductor_Yield_Engineering
  id: '[moc]-yield-intelligence-v6.3.7'
  project: Vault_Modernization
  version: v6.3.7
Dynamic:
  diagnostic_protocol:
  - 'Standard_Verification: Verify baseline parameters.'
  - 'Context_Audit: Ensure topological integrity.'
  fidelity_engine: DomainFidelityEngine
  graphify_link_external: true
  status: Ratified_v6.3.7_Migration
  topology_policy: Interconnected_Cluster
Object:
  description: Standard Industrial Node
  object_type: MOC
  physical_model: N/A
  tier: 0
Semantic:
  expected_queries:
  - Assistant to an Antigravity Industrial Process Engineer.
  - A technical document titled "[moc]-yield-intelligence-v6.3.7".
  - Create 5 "Expected Queries" that would be used to search for this document later.
  - Queries must be specific and practical.
  - Must end with '?'.
  is_part_of:
  - Antigravity_Knowledge_Graph
  related_to: []
  tags:
  - Yield_Intelligence
Trust Metrics:
  T_dynamic: 1.0
  T_init: 1.0
  T_static: 1.0
  isolation_index: 0.0
  source: Yield_Management_Framework
---

# [[[MOC] Yield-Intelligence

## 1. [Why]] 수율 지능(Yield Intelligence)의 반도체 경영적 의의
**수율(Yield)**은 반도체 비즈니스의 수익성과 직결되는 최상위 지표다. **수율 지능**은 팹(Fab) 전반의 빅데이터(계측, 센서, 물류, 환경 등)를 융합하여 수율 하락의 근본 원인을 실시간으로 규명하는 '중추 지능'이다. 단순히 결과를 모니터링하는 것을 넘어, 머신러닝 기반의 상관관계 분석을 통해 잠재적 위험을 사전에 차단하고 학습 곡선(Learning Curve)을 가속화하여 시장 우위를 점하는 전략적 도구다.

---

## 2. [Numerical Specs] 수율 관리 및 분석 지표 (Numerical Specs)

| 항목 | 핵심 지표 (KPI) | 목표 수준 (Target) | 비고 |
| :--- | :--- | :--- | :--- |
| **Line Yield** | 공정 진행 성공률 | $> 98.5\%$ | 웨이퍼 파손 및 폐기 방지 |
| **Die Yield** | 웨이퍼 내 넷다이 비율 | $> 92.0\%$ | 설계 수율 (mature node) |
| **Ramp-up Speed** | 수율 목표 도달 기간 | $< 6\,\text{months}$ | 신제품 양산 가속도 |
| **Analysis Latency** | 원인 규명 소요 시간 | $< 2\,\text{hr}$ | 돌발 수율 저하 대응 속도 |
| **Data Correlation** | 팩트 연계 신뢰도 | $> 85\%$ | 결함-수율 상관관계 계수 |

---

## 3. [Scientific Rationale] 수율 모델링 및 상관 분석

### 3.1 Murphy's Yield Model (수율 예측 모델)
웨이퍼 면적($A$), 결함 밀도($D_0$), 공정 복잡도(Critical Layers)를 기반으로 수율($Y$)을 예측한다.
$$Y = \left( \frac{1 - \exp(-AD_0)}{AD_0} \right)^2$$
*   **분석**: 결함 밀도가 낮아질수록 수율은 지수함수적으로 상승하며, 대면적 칩일수록 결함에 민감하다.

### 3.2 Commonality Analysis (공통성 분석)
불량 웨이퍼들이 공통적으로 거쳐간 설비나 챔버를 통계적(Chi-square 등)으로 추출하여 문제 설비를 타격(Targeting)한다.

---

## 4. [Real-world Case] 비정상 Bin-Fail 패턴 분석을 통한 챔버 이상 감지 사례

### 4.1 웨이퍼 에지(Edge) 영역의 특정 테스트 항목 집단 불량
- **현상**: EDS(Electrical Die Sorting) 테스트 결과, 특정 주간 생산된 웨이퍼들의 에지 영역에서 'Bin-7' (저전압 누설) 불량이 평소 대비 $15\%$ 증가.
- **분석**: **Python FidelityEngine**을 활용한 공통성 분석 결과, 에칭(Etching) 공정의 5번 설비 B-챔버를 통과한 롯트에서만 현상이 발생함을 $30\,\text{min}$ 만에 규명.
- **조치**: 해당 챔버의 정전 척(ESC) 상태 확인 결과, 냉각 불균형 발견 및 교체 실시.
- **결과**: 수율 $5\%$ 즉시 복구 및 $200$매 이상의 웨이퍼 손실 방지.

---

## 5. [FidelityEngine] 수율 예측(Murphy 모델) 계산 코드
```python
import numpy as np

def predict_yield_murphy(area_cm2, defect_density_cm2):
    """
    Predict yield using Murphy's Model
    :param area_cm2: Die area in cm^2
    :param defect_density_cm2: Average defect density per cm^2
    :return: Yield fraction (0.0 to 1.0)
    """
    ad = area_cm2 * defect_density_cm2
    if ad == 0: return 1.0
    y = ((1 - np.exp(-ad)) / ad) ** 2
    return y

# 칩 크기 2.0 cm^2, 결함 밀도 0.05 개/cm^2 시뮬레이션
predicted_y = predict_yield_murphy(2.0, 0.05)
print(f"Predicted Yield: {predicted_y*100:.2f}%")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Data Integrity**: 수율 분석 시스템(YMS)에 입력되는 센서 및 계측 데이터의 누락률이 $0.1\%$ 이하인가?
- [ ] **Feedback Loop**: 분석된 결과가 실제 공정 제어 시스템(APC)이나 설비 유지보수 오더(EAM)와 자동으로 연동되는가?
- [ ] **Baseline Management**: 모델의 기준 수율(Baseline)이 공정 변경(Change) 시마다 즉시 업데이트되는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**