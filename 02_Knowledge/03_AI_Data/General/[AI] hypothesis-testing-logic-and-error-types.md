---
Basic:
  id: "AI-STAT-HYPO-TEST-2026-V6"
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
  tags: - '#Hypothesis_Testing'
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

# [AI] hypothesis-testing-logic-and-error-types

## 1. [왜 배우는가? (Why)]
"신규 배터리 소재가 기존보다 효율적인가?" 혹은 "공정 온도를 $5^\circ\text{C}$ 낮추는 것이 수율에 영향을 주는가?"와 같은 공학적 주장을 단순한 평균 비교로만 결론 내리는 것은 매우 위험합니다. 데이터의 변동성(Variance)으로 인해 발생한 '우연한 결과'에 속을 수 있기 때문입니다. 가설 검정(Hypothesis Testing)은 데이터라는 증거를 통해 연구자의 주장이 우연이 아님을 수리적으로 입증하는 과정입니다. 이는 인지 편향(Cognitive Bias)과 무작위 노이즈를 제거하고, 신기술 도입의 타당성을 입증하여 자원 낭비를 방지하는 데이터 과학의 최후의 필터입니다.

## 2. [가설 검정 및 오류 관리 핵심 사양 (Stat Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Significance ($\alpha$)**| Type I Error Rate | $0.05$ (Standard) | 귀무가설이 참인데 기각할 확률 (오탐지 임계치) |
| **Statistical Power**| $1 - \beta$ | $> 0.80$ | 대립가설이 참일 때 이를 올바르게 채택할 확률 |
| **Confidence Level**| $1 - \alpha$ | $95\%$ | 실제 파라미터가 신뢰 구간 내에 존재할 확률 |
| **Effect Size** | Cohen's $d$ | $> 0.5$ (Medium) | 통계적 유의성을 넘어선 실질적인 차이의 크기 |
| **P-value** | Prob. of $H_0$ | $\le 0.05$ | $H_0$가 참일 때 현재 데이터가 관찰될 확률 (기각 근거) |
| **Sample Size ($n$)**| Data Volume | Calculated per Power | 목표 검정력을 확보하기 위한 최소 표본 수 |
| **Critical Value** | Z-score / T-score| $> 1.96$ (@95%) | 기각역(Reject Region)을 결정하는 통계적 임계 경계 |
| **Standard Error** | SE | $\sigma / \sqrt{n}$ | 표본 평균의 표준 편차; 추정의 정밀도 지표 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 제1종 오류($\alpha$)와 제2종 오류($\beta$)의 트레이드오프
의사결정의 두 가지 실패 유형입니다.
- **제1종 오류 ($\alpha$)**: 효과가 없는데 있다고 판단하는 '가짜 양성(False Positive)'. (예: 불량인데 양품으로 판정)
- **제2종 오류 ($\beta$)**: 효과가 있는데 없다고 판단하는 '가짜 음성(False Negative)'. (예: 양품인데 불량으로 판정)
- **로직**: $\alpha$를 너무 낮게 설정하면 $\beta$가 커지며 검정력($1-\beta$)이 약화됩니다. 공학자는 산업적 비용(Cost of Failure)을 고려하여 두 오류 사이의 물리적 균형점(Decision Boundary)을 설정해야 합니다.

### 3.2 중심 극한 정리 (Central Limit Theorem)
추론 통계의 수리적 기반입니다.
- **수식**: $\bar{X} \sim N(\mu, \sigma^2/n)$
- **의미**: 원래 데이터의 분포와 상관없이 표본의 크기($n$)가 충분히 크면 표본 평균의 분포는 정규 분포를 따릅니다. 이를 통해 우리는 단일 표본 데이터만으로도 모집단의 성질을 확률적으로 규정할 수 있습니다.

### 3.3 검정 통계량과 P-value의 귀류법적 논리
가설 검정은 "내 주장이 맞다"고 증명하는 것이 아니라 "상대 주장이 틀렸다"고 증명하는 방식입니다.
- **로직**: 귀무가설($H_0$)이 참이라고 가정했을 때, 현재 관찰된 데이터가 나타날 확률(P-value)이 매우 낮다면($< 0.05$), "우연이라고 하기엔 너무 이상하므로 $H_0$가 틀렸다"고 결론 내립니다.

## 4. [코드 연결 해설 (StatisticalTestEngine)]
아래 코드는 두 그룹의 데이터를 입력받아 t-검정을 수행하고, P-value와 효과 크기를 산출하여 가설 채택 여부를 공학적으로 결정하는 엔진입니다.

```python
import numpy as np
from scipy import stats

class StatisticalTestEngine:
    """
    HDS-Gold V6.3.7 규격의 가설 검정 및 의사결정 분석 엔진
    """
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def run_t_test(self, group_a, group_b):
        """
        두 그룹 간의 평균 차이 유의성 검정 (Welch's t-test)
        """
        t_stat, p_val = stats.ttest_ind(group_a, group_b, equal_var=False)
        
        # 효과 크기 (Cohen's d) 계산
        d = (np.mean(group_a) - np.mean(group_b)) / np.sqrt((np.var(group_a) + np.var(group_b)) / 2)
        
        decision = "REJECT_H0 (Significant)" if p_val <= self.alpha else "FAIL_TO_REJECT_H0"
        
        return {
            "p_value": round(p_val, 5),
            "cohen_d": round(abs(d), 3),
            "decision": decision,
            "confidence": f"{(1-self.alpha)*100}%"
        }

# Example Usage:
# engine = StatisticalTestEngine(alpha=0.01) # 엄격한 검정
# result = engine.run_t_test(legacy_yield, new_process_yield)
```

## 5. [스스로 체크 (Self-Audit)]
1. **P-value**가 $0.01$로 매우 낮게 나왔음에도 불구하고, **Effect Size** (Cohen's d)가 $0.1$로 작다면 이를 실제 공정에 적용해야 하는가? (경제적 관점의 답변)
2. **Sample Size ($n$)**가 커질수록 **Standard Error (SE)**가 작아지며 **P-value**가 낮아지는 수리적 원리를 설명할 수 있는가?
3. **제1종 오류**를 범했을 때의 비용이 **제2종 오류**를 범했을 때보다 $100$배 크다면, 유의수준($\alpha$)을 어떻게 조정해야 하는가?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/General/AI machine-learning-evaluation-metrics
- 02_Knowledge/02_Battery/Intelligence/Battery cell-quality-data-clustering
- 02_Knowledge/09_SmartFactory_Production/QualityControl/QC statistical-process-control-spc

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
