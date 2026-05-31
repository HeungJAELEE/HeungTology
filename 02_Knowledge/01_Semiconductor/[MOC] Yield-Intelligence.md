---
lineage:
  dataset_reference: global-core-log-v2026
  original_author: Antigravity Vault Core Team
  original_hash: ac1596073d79179e4080cad52d8b668796dc2e43e9938339a18bb674f2f5a1de
metadata:
  date: '2026-05-17'
  domain: 01_Semiconductor
  id: '[[[Concept] [MOC] Yield-Intelligence]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 'High-fidelity engineering node: [MOC] Yield-Intelligence.md'
  object_type: Concept
  tier: 1
properties:
  bin_7_voltage_leakage_rate: 15.0%
  commonality_analysis_time: 30.0 min
  murphy_yield_formula: Y = ((1 - exp(-A*D_0)) / (A*D_0))^2
  recovered_yield_rate: 5.0%
  sensor_data_missing_rate_limit: <= 0.1%
  target_analysis_latency_limit: < 2.0 hr
  target_data_correlation: '> 85.0%'
  target_die_yield: '> 92.0%'
  target_line_yield: '> 98.5%'
  target_ramp_up_speed_limit: < 6.0 months
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 반도체_백서_통합_지휘소]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# Yield-Intelligence

## 1. [Definition] 수율 지능(Yield Intelligence) 공학적 정의
수율(Yield): 반도체 제조 공정 경제성 결정 최상위 핵심 지표 [Ref: Yield_Mgmt_SOP Section 1].
수율 지능(YI): Fab 내 Metrology, Sensor, Logistics, Environment 데이터 통합 분석을 통한 Root Cause 실시간 규명 및 Learning Curve 가속화 전략 계층 [Ref: Yield_Mgmt_SOP Section 1.1]. ML 기반 상관관계 분석을 통해 잠재 리스크를 선제 차단하고 제조 경쟁력을 확보하는 고밀도 인텔리전스 시스템 [Ref: Yield_Management_Framework Section 2].

---

## 2. [Quantitative Specs] 수율 관리 정량 지표

### 2.1 이론치 vs 검증치 대조 (Theoretical vs. Verified)

| Parameter | Theoretical (Ideal) | Verified (Target KPI) | [Ref] |
| :--- | :--- | :--- | :--- |
| **Line Yield** | 100.0% | $> 98.5\%$ | [Ref: Yield_Mgmt_SOP Section 2.1] |
| **Die Yield** | 100.0% | $> 92.0\%$ | [Ref: Yield_Mgmt_SOP Section 2.2] |
| **Ramp-up Speed** | $\infty$ (Instant) | $< 6.0\,\text{months}$ | [Ref: Fab_Ops_Standard Section 1.4] |
| **Analysis Latency** | $0.0\,\text{min}$ | $< 2.0\,\text{hr}$ | [Ref: Fab_Ops_Standard Section 1.5] |
| **Data Correlation** | 1.0 | $> 85.0\%$ | [Ref: Yield_Analysis_Protocol Section 3] |

---

## 3. [Scientific Rationale] 수율 모델링 및 상관 분석

### 3.1 Murphy's Yield Model (수율 예측 모델)
웨이퍼 면적($A$), 결함 밀도($D_0$), 공정 복잡도 기반 수율($Y$) 산출 식 [Ref: Murphy_1968 Section 3.1].
$$Y = \left( \frac{1 - \exp(-AD_0)}{AD_0} \right)^2$$
- **공학적 해석**: $D_0$ 감소 시 $Y$는 지수함수적으로 상승하며, Die Area 증가 시 결함 민감도는 비선형적으로 증가함 [Ref: Yield_Modeling_Manual Section 4.2].

### 3.2 Commonality Analysis (공통성 분석)
불량 웨이퍼 공유 설비(Tool) 및 챔버(Chamber)를 Chi-square $\chi^2$ 통계량 기반으로 추출하여 문제 국소화(Localization) 수행 [Ref: SPC_Std Section 3.2].

---

## 4. [Case Study] Bin-Fail 패턴 기반 챔버 이상 감지

### 4.1 Edge 영역 특정 테스트 항목 불량 분석
- **현상**: EDS 결과, 특정 주간 에지 영역 'Bin-7'(Low Voltage Leakage) 불량률 $15.0\%$ [Ref: EDS_Log Section 4.1] 증가.
- **분석**: FidelityEngine 공통성 분석을 통해 에칭(Etching) 5번 설비 B-챔버 경유 Lot 연관성 $30.0\,\text{min}$ [Ref: Analysis_Log Section 1.2] 내 규명.
- **조치**: 정전 척(ESC) 냉각 불균형(Cooling Imbalance) 확인 및 부품 교체.
- **결과**: 수율 $5.0\%$ [Ref: Yield_Report Section 2.1] 즉시 복구 및 200매 이상의 Wafer Loss 방지.

---

## 5. [FidelityEngine] 수율 예측(Murphy 모델) 구현 코드

```python
import numpy as np

def predict_yield_murphy(area_cm2: float, defect_density_cm2: float) -> float:
    """
    Murphy's Model 기반 수율 예측 함수
    :param area_cm2: Die area (cm^2)
    :param defect_density_cm2: Average defect density (cm^-2)
    :return: Yield fraction (0.0 ~ 1.0)
    """
    ad = area_cm2 * defect_density_cm2
    if ad == 0:
        return 1.0
    y = ((1 - np.exp(-ad)) / ad) ** 2
    return y

# Simulation: Die size 2.0 cm^2, Defect density 0.05 cm^-2
predicted_y = predict_yield_murphy(2.0, 0.05)
print(f"Predicted Yield: {predicted_y*100:.2f}%")
```

---

## 6. [Verification] 시스템 무결성 체크리스트

- [ ] **Data Integrity**: YMS 내 센서/계측 데이터 누락률 $\le 0.1\%$ [Ref: Data_Quality_Standard Section 1.1] 여부.
- [ ] **Feedback Loop**: 분석 결과의 APC(Advanced Process Control) 및 EAM(Enterprise Asset Management) 실시간 연동 여부.
- [ ] **Baseline Management**: 공정 변동 발생 시 모델 기준 수율(Baseline) 즉시 업데이트 여부.

**[V7.5.3_HDS_GOLD_REINFORCED_BY_FIDELITY]**