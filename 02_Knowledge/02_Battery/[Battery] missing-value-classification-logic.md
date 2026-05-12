---
Basic:
  id: "[[[Battery] missing-value-classification-logic"
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

# [[[Battery] missing-value-classification-logic

## 1. [왜 배우는가? (Why): 단순한 빈칸 그 이상의 의미]]
데이터 분석에서 결측치(Missing Value)는 단순한 '데이터 부재'가 아닙니다. 어떤 데이터가 왜 사라졌는지에 대한 메커니즘을 규명하지 못한 채 임의로 평균을 채우거나 행을 삭제하면, 모델은 '절반의 진실'만 배우게 됩니다. **결측치 분류 로직**은 데이터의 실종 패턴을 수학적으로 식별하여, 정보 유실에 의한 통계적 왜곡을 최소화하고 모델의 일반화 성능을 물리적으로 보전하기 위한 과학적 대치(Imputation) 전략의 출발점입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

결측치 유형 판별을 위한 통계적 수치와 의사결정 임계치입니다.

| 유형 (Type) | 수식적 식별 조건 (Condition) | 대치 적합성 (Appropriateness) | 공학적 권고 (Recommendation) |
| :--- | :--- | :--- | :--- |
| **MCAR** | $P(M \| Y_{obs}, Y_{mis}) = P(M)$ | **가장 안전함** | 단순 제거 또는 무작위 대치 |
| **MAR** | $P(M \| Y_{obs}, Y_{mis}) = P(M \| Y_{obs})$ | **분석 가능함** | **MICE / 회귀 기반 대치** |
| **MNAR** | $P(M \| Y_{obs}, Y_{mis}) \neq P(M \| Y_{obs})$ | **매우 위험함** | 결측 사유를 변수로 포함 (Indicator) |

### 2.1 리틀의 MCAR 검정 (Little's MCAR Test)
- **Logic**: 결측치가 있는 집단과 없는 집단 간의 특성 차이가 우연인지(MCAR), 아니면 체계적인지(MAR/MNAR)를 카이제곱 분포를 통해 검정합니다.
- **Threshold**: $p < 0.05$ 이면 MCAR 가정을 기각하며, 이는 결측치에 '의미'가 있음을 시사합니다.

## 3. [심층 분석 (Deep Analysis): 편향의 발생과 인과적 사슬]

### 3.1 정보 유실에 의한 '보이지 않는 편향'
- **Rationale**: 만약 장비의 특정 부품이 과열될 때 센서가 작동을 멈춘다면(MNAR), 그 결측치를 평균 온도로 채우는 순간 우리 모델은 '과열 징후'를 영구히 놓치게 됩니다. 
- **Causality**: 이 경우 결측치를 채우는 것보다, '결측 여부($1$ 또는 $0$)' 자체를 하나의 강력한 독립변수로 사용하는 것이 시스템의 위험을 감지하는 데 훨씬 유리합니다.

### 3.2 MICE(연쇄 방정식 다중 대치)의 기계적 완성
- **Logic**: 한 변수의 결측치를 다른 모든 변수를 사용해 예측하고, 이 과정을 모든 결측 변수에 대해 순환적으로 반복합니다.
- **Physics**: 이 과정은 데이터의 전체적인 상관관계를 보존하며 결측치를 메우기 때문에, 단순 평균 대치보다 모델의 신뢰도를 획기적으로 높입니다.

## 4. [AI & Hardware Synergy: Iterative Imputation Acceleration]

수백 개의 변수가 얽힌 대규모 데이터셋에서 MICE 연산을 수행하는 것은 엄청난 반복 회귀 연산을 요구합니다.

- **RTX 4060 GPU 가속 (cuML LinearRegression)**:
  - **Optimization**: MICE의 각 단계에서 수행되는 선형/로지스틱 회귀 예측을 GPU 코어에서 병렬로 처리합니다.
  - **Result**: 수십만 행의 테이블에 대한 다중 대치 시간을 $5$분 이내로 단축하여 분석 사이클을 가속합니다.
- **Intel oneDAL Vectorization**:
  - CPU 기반 환경에서는 oneDAL 라이브러리를 통해 결측치 마스킹(Masking) 및 집계 연산을 벡터화하여 처리 성능을 극대화합니다.

## 5. [코드 브릿지] Little's MCAR Test & MICE Strategy (Python)
결측 유형을 판별하고 정교하게 대치하는 표준 로직입니다.

```python
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from statsmodels.stats.diagnostic import lilliefors # 예시적 검정

# 1. 결측치 패턴 시각화 (Missingno 등 활용 권장)
# 2. 다중 대치(MICE) 전략 실행
# estimator를 통해 결측치를 무엇으로 예측할지 결정
mice_imputer = IterativeImputer(estimator=RandomForestRegressor(), 
                                max_iter=10, 
                                random_state=0)

X_filled = mice_imputer.fit_transform(X_missing)

# 의도: 데이터의 '빈칸'을 단순한 수치가 아닌, 
# 다른 변수들과의 '상관적 흐름' 속에서 복원하여 정보 왜곡을 차단함.
```

## 6. [스스로 체크 (Verification Checklist)]
- [ ] **Null Correlation**: 결측 여부와 다른 변수 간의 상관 계수가 높은가? (높다면 MAR로 판단하고 MICE 적용)
- [ ] **Range Integrity**: 대치된 값이 변수의 물리적/논리적 범위(예: 나이는 0 이상)를 준수하는가?
- [ ] **Imputation Variance**: 다중 대치 시 각 세션별로 생성된 대치값들이 일관성 있는 범위를 유지하는가?
- [ ] **Indicator Variable**: 결측률이 $30\%$ 이상인 중요 변수의 경우, 결측 여부를 나타내는 바이너리 변수를 추가했는가?

---
**[V6.3.7_HDS_GOLD_ENRICHED_BY_FLASH]**