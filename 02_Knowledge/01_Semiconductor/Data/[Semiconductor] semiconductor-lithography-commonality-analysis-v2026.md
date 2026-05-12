---
Basic:
  id: "[semiconductor]-semiconductor-lithography-commonality-analysis-v2026-v6.3.7"
  domain: "Semiconductor_Yield_Engineering"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Commonality_Analysis'
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
  source: "Yield_Management_System_YMS"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-lithography-commonality-analysis-v2026

## 1. [Why]] 공통성 분석(Commonality Analysis)의 수율 공학적 의의
**공통성 분석**은 수천 개의 공정 경로 중 특정 설비나 챔버가 수율 하락의 범인(Root Cause)인지를 통계적으로 가려내는 기법이다. 수백 명의 노광기(Scanner)와 트랙(Track) 설비가 얽혀 있는 복잡한 팹 환경에서, 불량 롯트(Lot)들이 공통적으로 거쳐간 설비를 신속하게 타격함으로써 불량 유출을 차단하고 복구 시간을 최소화한다.

---

## 2. [Numerical Specs] 분석 통계 파라미터 (Numerical Specs)

| 항목 | 분석 기법 (Standard) | 유의 수준 ($\alpha$) | 비고 |
| :--- | :--- | :--- | :--- |
| **P-value** | Chi-square / ANOVA | $< 0.05$ | 통계적 유의성 판단 기준 |
| **Yield Delta** | Group A vs Group B | $> 2.5\%$ | 설비 간 수율 차이 임계치 |
| **Sample Size** | 분석 대상 롯트 수 | $> 30\,\text{lots}$ | 통계적 신뢰도 확보를 위한 최소량 |
| **Confidence Level** | 신뢰 수준 | $95\%$ | 분석 결과의 확실성 |
| **Analysis Latency** | 결과 도출 속도 | $< 10\,\text{min}$ | 자동화 분석 시스템 목표치 |

---

## 3. [Scientific Rationale] 통계적 가설 검정 모델

### 3.1 Chi-square Test (독립성 검정)
설비($X$)와 불량 여부($Y$) 간의 연관성을 검정한다.
$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
*   **분석**: $\chi^2$ 값이 크고 P-value가 낮을수록 해당 설비가 불량 발생에 결정적인 영향을 미쳤음을 의미한다.

### 3.2 One-way ANOVA (분산 분석)
여러 대의 노광기 간의 수율 평균 차이가 통계적으로 유의미한지 분석한다.

---

## 4. [Real-world Case] 특정 스캐너의 렌즈 오염에 따른 집단 불량 규명 사례

### 4.1 'Bin-3' (파티클 불량) 급증 롯트의 경로 추적
- **현상**: 지난 24시간 동안 생산된 10개 롯트에서 동일한 위치의 파티클 불량 패턴 발생.
- **분석**: **Python FidelityEngine**을 활용한 공통성 분석 결과, 불량 롯트들의 $100\%$가 노광 공정의 'SCANNER_07' 호기를 거쳐갔음을 확인 (P-value $0.0001$). 타 설비를 거친 롯트에서는 해당 현상 없음.
- **조치**: 즉시 SCANNER_07 호기를 공정에서 격리(Down)하고 렌즈 하단부를 검사한 결과, 미세 박리된 파티클 발견.
- **결과**: 돌발 불량 조기 차단으로 약 $300$매의 웨이퍼 손실 방지 (기대 수익 약 $5$억 원 확보).

---

## 5. [FidelityEngine] 단순 Chi-square 공통성 분석 코드
```python
import numpy as np
from scipy.stats import chi2_contingency

def run_commonality_test(pass_a, fail_a, pass_b, fail_b):
    """
    Compare two equipment groups using Chi-square test
    :return: p-value and conclusion
    """
    # Contingency table: Pass, Fail, Pass, Fail
    table = pass_a, fail_a, pass_b, fail_b
    chi2, p, dof, expected = chi2_contingency(table)
    
    status = "SIGNIFICANT_DIFFERENCE" if p < 0.05 else "NO_SIGNIFICANT_DIFFERENCE"
    return p, status

# 설비 A (불량 많음) vs 설비 B (정상) 데이터
p_val, result = run_commonality_test(85, 15, 98, 2)
print(f"P-value: {p_val:.4f} | Conclusion: {result}")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Data Completeness**: 모든 롯트의 설비 통과 이력(History)이 누락 없이 MES와 동기화되어 있는가?
- [ ] **Confounding Variables**: 설비 외에 원재료(Chemical)나 작업자 등 다른 변수가 결과에 왜곡을 주지 않는지 확인하였는가?
- [ ] **Real-time Alert**: 유의미한 설비 편차 포착 시 품질 부서에 자동으로 리포트 및 설비 인터락이 실행되는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
