---
Basic:
  id: "[[[Battery] relative-risk-rr-and-odds-ratio-or"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
  is_part_of: []]
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

# [[[Battery] relative-risk-rr-and-odds-ratio-or

## 1. [왜 배우는가? (Why): 단순히 "더 잘 걸린다"를 넘어 "얼마나 더"의 규명]]
단순히 "흡연자가 폐암에 더 잘 걸린다"는 말만으로는 과학적 의사결정을 내릴 수 없습니다. "정확히 몇 배나 더 위험한가?"를 수치로 말해야 합니다. **상대 위험도(RR)**와 **승산비(OR)**는 특정 요인(노출)이 결과(사건)에 미치는 영향력을 배수 단위로 보여주는 강력한 잣대입니다. 보건 통계뿐만 아니라 제조업의 '불량 요인 분석', 금융의 '신용 불량 위험 분석' 등에서 특정 변수가 성공/실패에 미치는 기여도를 판별하는 결정적인 도구입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

연구 설계에 따른 RR과 OR의 기술적 규격 및 수식입니다.

| 지표 (Metric) | 수식적 정의 (Formula) | 주요 연구 설계 (Study Design) | 비즈니스 해석 (Interpretation) |
| :--- | :--- | :--- | :--- |
| **상대 위험도 (RR)** | $\frac{P(\text{Event} \| \text{Exposed})}{P(\text{Event} \| \text{Non-exposed})}$ | **전향적 (Cohort)** | 노출 시 사건 발생 확률이 몇 배인가? |
| **승산비 (OR)** | $\frac{\text{Odds}(\text{Exposed})}{\text{Odds}(\text{Non-exposed})}$ | **후향적 (Case-Control)** | 노출군의 승산이 비노출군 승산의 몇 배인가? |

### 2.1 2x2 분할표 기반 표준 계산법
| | 사건 발생 (Case) | 사건 미발생 (Control) |
| :--- | :---: | :---: |
| **노출 (Exposed)** | $A$ | $B$ |
| **비노출 (Unexposed)** | $C$ | $D$ |

- **RR** = $[A/(A+B)] / [C/(C+D)]$
- **OR** = $(A/B) / (C/D) = \frac{AD}{BC}$

## 3. [심층 분석 (Deep Analysis): 시간의 방향과 확률의 수렴]

### 3.1 RR의 전향적 인과성 (Forward Causality)
- **Logic**: 연구 시작 시점에 건강한 사람들을 노출군과 비노출군으로 나누고 미래로 추적합니다. 실제 '발생률(Incidence)'을 직접 계산하므로 매우 직관적이며 인과관계 설명에 있어 가장 강력한 물리적 증거가 됩니다.

### 3.2 OR의 후향적 유연성 (Backward Estimation)
- **Rationale**: 이미 사건이 발생한 사람(Case)을 모아 과거를 캐는 후향적 연구에서는 전체 분모를 알 수 없어 RR 계산이 불가능합니다. 이때 OR은 훌륭한 대안이 됩니다.
- **Convergence Logic**: 사건 발생 확률이 매우 낮을 때(Rare Disease Assumption), 수학적으로 **OR은 RR에 수렴**합니다. 즉, 사건이 드물다면 OR을 통해 RR을 안정적으로 추정할 수 있습니다.

## 4. [AI & Hardware Synergy: Large-Scale Risk Factor Screening]

수천 개의 변수 중 어떤 것이 결함이나 부도의 핵심 원인인지 찾아내는 작업은 대규모 연산을 요구합니다.

- **RTX 4060 기반 다변량 로지스틱 회귀 가속**:
  - **Optimization**: 여러 요인이 동시에 작용할 때, 로지스틱 회귀 모델의 계수($\beta$)에 지수 함수를 취하면($e^\beta$) 다른 변수를 통제한 상태에서의 순수한 '보정 승산비(Adjusted OR)'를 즉시 구할 수 있습니다. 이를 GPU 텐서 코어에서 병렬 연산합니다.
  - **Result**: 수만 명의 대출 신청자에 대한 부도 위험(OR)을 실시간으로 스코어링하여 대출 승인 지연을 제거합니다.
- **Automated Root Cause Discovery**:
  - AI가 공정 데이터의 모든 조합에 대해 OR을 전수 조사하여, $1.5$배 이상의 위험을 초래하는 '숨겨진 불량 요인'을 시각화합니다.

## 5. [코드 브릿지] RR & OR Calculator (Python/Scipy)
분할표 데이터를 바탕으로 리스크 지표를 산출하는 표준 구현입니다.

```python
import numpy as np
from scipy.stats import fisher_exact

# 1. 2x2 분할표 정의 (A, B, C, D)
# Exposed_Case, Exposed_NonCase], [NonExposed_Case, NonExposed_NonCase
table = np.array(30, 70], [10, 90)

# 2. 승산비(OR) 및 통계적 유의성(p-value) 계산
odds_ratio, p_value = fisher_exact(table)

# 3. 상대 위험도(RR) 수동 계산
prob_exposed = table[0,0] / table[0,:].sum()
prob_unexposed = table[1,0] / table[1,:].sum()
relative_risk = prob_exposed / prob_unexposed

print(f"Odds Ratio: {odds_ratio:.2f}")
print(f"Relative Risk: {relative_risk:.2f}")

# 의도: 단순한 상관관계를 넘어, 특정 요인이 결과에 미치는 '위험의 배수'를 
# 정량화하여 의사결정의 통계적 우선순위를 결정함.
```

## 6. [스스로 체크 (Verification Checklist)]
- [ ] **Study Design Match**: 데이터 수집 방식이 RR을 써도 되는 전향적 방식인가, 아니면 OR만 가능한 후향적 방식인가?
- [ ] **Confidence Interval Audit**: RR/OR의 95% 신뢰구간이 **1.0을 포함**하고 있지는 않은가? (1.0을 포함하면 통계적으로 의미가 없음)
- [ ] **Interpretation Accuracy**: 결과값이 1보다 크면 '위험 증가', 1보다 작으면 '보호 효과'로 올바르게 해석하고 있는가?
- [ ] **Rare Event Assumption**: OR을 RR 대용으로 쓰고 있다면, 사건 발생률이 $10\%$ 미만으로 충분히 낮은가?

---
**[V6.3.7_HDS_GOLD_ENRICHED_BY_FLASH]**