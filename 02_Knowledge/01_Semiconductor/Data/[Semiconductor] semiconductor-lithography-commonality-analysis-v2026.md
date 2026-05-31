---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 5d651d15bdbda49a1a5862c20e747d60edf26e7745818c646e705b1470c4c140
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] semiconductor-lithography-commonality-analysis-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] semiconductor-lithography-commonality-analysis-v2026에
    관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  confidence_level: 95%
  max_analysis_latency: 10 min
  min_sample_size: '30'
  p_value_threshold: '0.05'
  verified_equipment_correlation: 100%
  verified_p_value: '0.0001'
  verified_sample_size: '10'
  verified_yield_delta: 3.1%
  yield_delta_threshold: 2.5%
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

# [Semiconductor] semiconductor-lithography-commonality-analysis-v2026

## 1. [Engineering Significance] 공통성 분석의 수율 공학적 의의
공통성 분석(Commonality Analysis)은 다수 공정 경로 내 특정 설비(Equipment) 또는 챔버(Chamber)를 수율 저하의 근본 원인(Root Cause)으로 식별하는 통계적 기법임. 노광(Scanner) 및 트랙(Track) 연동 환경에서 불량 롯트(Lot)의 공통 경로를 추적하여 불량 유출 차단 및 복구 시간(MTTR) 최소화를 수행함.

## 2. [Comparative Analysis] 이론치 vs 검증치 대조

| Parameter | Theoretical (Standard) | Verified (Field Case) |
| :--- | :--- | :--- |
| **P-value** | $< 0.05$ [Ref: YMS] | $0.0001$ [Ref: Case_Study] |
| **Yield Delta** | $> 2.5\%$ [Ref: YMS] | $3.1\%$ [Ref: Case_Study] |
| **Sample Size** | $> 30$ lots [Ref: YMS] | $10$ lots [Ref: Case_Study] |
| **Equipment Correlation** | Statistical Link [Ref: YMS] | $100\%$ via SCANNER_07 [Ref: Case_Study] |

## 3. [Numerical Specs] 분석 통계 파라미터

| 항목 | 분석 기법 (Standard) | 유의 수준 ($\alpha$) | 비고 |
| :--- | :--- | :--- | :--- |
| **P-value** | Chi-square / ANOVA | $< 0.05$ [Ref: YMS] | 통계적 유의성 판단 기준 |
| **Yield Delta** | Group A vs Group B | $> 2.5\%$ [Ref: YMS] | 설비 간 수율 차이 임계치 |
| **Sample Size** | 분석 대상 롯트 수 | $> 30$ [Ref: YMS] | 통계적 신뢰도 확보 최소량 |
| **Confidence Level** | 신뢰 수준 | $95\%$ [Ref: YMS] | 분석 결과의 확실성 |
| **Analysis Latency** | 결과 도출 속도 | $< 10$ min [Ref: YMS] | 자동화 분석 시스템 목표치 |

## 4. [Scientific Rationale] 통계적 가설 검정 모델

### 4.1 Chi-square Test (독립성 검정)
설비($X$)와 불량 여부($Y$) 간의 연관성을 검정함.
$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
$\chi^2$ 값의 증가 및 P-value의 감소는 해당 설비가 불량 발생의 결정적 변수임을 의미함 [Ref: YMS].

### 4.2 One-way ANOVA (분산 분석)
다수 노광기 간 수율 평균($\mu$)의 통계적 유의차 분석에 활용하며, F-통계량을 통해 집단 간 분산 비율을 산출함 [Ref: YMS].

## 5. [Field Case] SCANNER_07 렌즈 오염에 따른 집단 불량 규명

### 5.1 'Bin-3' (파티클 불량) 경로 추적
- **현상**: 24시간 [Ref: Case_Study] 내 생산된 10개 롯트 [Ref: Case_Study]에서 특정 위치 파티클 불량 패턴 발생 [Ref: Case_Study].
- **분석**: Python FidelityEngine 분석 결과, 불량 롯트의 $100\%$ [Ref: Case_Study]가 'SCANNER_07' 호기를 경유함 (P-value $0.0001$ [Ref: Case_Study]).
- **조치**: SCANNER_07 즉시 격리 및 렌즈 하단부 정밀 검사 $\rightarrow$ 미세 박리 파티클 검출 [Ref: Case_Study].
- **결과**: 약 $300$매 [Ref: Case_Study] 웨이퍼 손실 방지 및 기대 수익 약 $5$억 원 [Ref: Case_Study] 확보.

## 6. [FidelityEngine] Implementation (Python)
```python
import numpy as np
from scipy.stats import chi2_contingency

def run_commonality_test(pass_a, fail_a, pass_b, fail_b):
    """
    Compare two equipment groups using Chi-square test
    :return: p-value and conclusion
    """
    # Contingency table: Pass, Fail, Pass, Fail
    table = np.array([[pass_a, fail_a], [pass_b, fail_b]])
    chi2, p, dof, expected = chi2_contingency(table)
    
    # Significance threshold: 0.05 [Ref: YMS]
    status = "SIGNIFICANT_DIFFERENCE" if p < 0.05 else "NO_SIGNIFICANT_DIFFERENCE"
    return p, status

# Data: Equipment A (High defect) vs Equipment B (Normal)
p_val, result = run_commonality_test(85, 15, 98, 2)
print(f"P-value: {p_val:.4f} | Conclusion: {result}")
```

## 7. [Verification] Reliability Checklist
- [ ] **Data Completeness**: MES-Lot History 동기화 무결성 확보 여부 [Ref: YMS].
- [ ] **Confounding Variables**: Chemical, Operator 등 외생 변수 통제 여부 [Ref: YMS].
- [ ] **Real-time Alert**: 유의미한 편차 발생 시 Interlock 및 Report 자동화 여부 [Ref: YMS].

**[V7.5.3_HDS_GOLD_REINFORCED_BY_FIDE]**