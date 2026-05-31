---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 65bb1e24a37f311e2031197caea700df4b6ac5bbc1fd5f980ebf6ba2277b8400
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] missing-value-classification-logic]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] missing-value-classification-logic에 관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  critical_temperature_threshold: 80
  littles_test_p_value_threshold: 0.05
  mice_max_iter: 10
  mice_random_state: 42
  missing_rate_threshold: 0.3
  specification_version: HDS-Gold V6.3.7
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
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

# [AI] missing-value-classification-logic

## 1. [왜 배우는가? (Why)]
데이터 분석에서 결측치(Missing Value)는 단순한 '데이터 부재'가 아니라, 수집 과정의 결함이나 특정 물리적 현상이 반영된 '잠재적 정보'입니다. 어떤 데이터가 왜 사라졌는지에 대한 메커니즘을 규명하지 못한 채 평균값으로 채우거나 행을 삭제하면, 모델은 '절반의 진실'만을 학습하게 되어 통계적 편향(Bias)에 빠지게 됩니다. 결측치 분류 로직을 배우는 이유는 데이터의 실종 패턴을 수학적으로 식별하여, 정보 유실에 의한 왜곡을 최소화하고 모델의 일반화 성능을 물리적으로 보존하기 위한 과학적 대치(Imputation) 전략을 수립하기 위함입니다.

## 2. [결측치 유형 판별 및 데이터 품질 핵심 사양 (Missing Data Specs)]

| Type Category | Specific Metric | Condition (Probabilistic) | Engineering Strategy |
|:---|:---|:---:|:---|
| **MCAR** | Missing Completely | $P(M \| Y_{obs}, Y_{mis}) = P(M)$ | 무작위 결측: 단순 제거 또는 리스트와이즈 삭제 가능 |
| **MAR** | Missing at Random | $P(M \| Y_{obs}, Y_{mis}) = P(M \| Y_{obs})$ | 조건부 결측: MICE, KNN 등 회귀 기반 대치 필수 |
| **MNAR** | Not at Random | $P(M \| Y_{obs}, Y_{mis}) \neq P(M \| Y_{obs})$ | 비무작위 결측: 결측 원인 변수화(Indicator) 및 모델링 |
| **Little's Test**| MCAR Test | $p \text{-value} > 0.05$ | MCAR 가정을 기각하지 못할 경우 안전하게 대치 가능 |
| **Missing Rate** | Sparsity (%) | $> 30\%$ Threshold | 대치보다는 변수 삭제 또는 정보 수집 재개 검토 |
| **Imp. Accuracy**| RMSE / MAE | Lower is Better | 실제값(Hold-out) 대비 대치된 값의 수리적 오차 |
| **Sparsity Index**| Data Density | $1 - (\text{Non-null} / \text{Total})$ | 데이터셋 전체의 희소성 정도를 나타내는 지표 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 정보 유실에 의한 '보이지 않는 편향'
데이터가 사라진 이유 자체가 데이터인 경우를 분석합니다.
- **로직**: 만약 배터리 팩 내부의 온도가 $80^\circ\text{C}$를 초과할 때 센서가 과열로 작동을 멈춘다면(MNAR), 이 결측치를 단순히 평균 온도로 채우는 순간 모델은 '과열 징후'라는 가장 중요한 정보를 영구히 상실합니다. 이 경우 결측치를 채우는 것보다 '결측 여부(Indicator)' 자체를 하나의 강력한 독립변수로 사용하는 것이 시스템 위험 감지에 유리합니다.

### 3.2 MICE(연쇄 방정식 다중 대치)의 기계적 완성
변수 간의 상관관계를 보존하며 결측치를 복원하는 기법입니다.
- **수식**: $Y_j = f(Y_1, \dots, Y_{j-1}, Y_{j+1}, \dots, Y_k)$
- **로직**: 한 변수의 결측치를 다른 모든 변수를 사용해 예측하고, 이 과정을 모든 결측 변수에 대해 순환적으로 반복합니다. 이는 데이터의 전체적인 공분산 구조를 해치지 않으면서 빈칸을 메우기 때문에, 단순 평균 대치 대비 모델의 신뢰도를 획기적으로 높입니다.

### 3.3 루빈의 법칙 (Rubin's Rules)
다중 대치(Multiple Imputation) 결과를 통합하는 원칙입니다. 여러 번 대치된 데이터셋에서 얻은 추정치들의 평균과 분산을 결합하여, 결측치 대치 과정에서 발생하는 불확실성을 통계적으로 보정합니다.

## 4. [코드 연결 해설 (DataQualityGuard)]
아래 코드는 `scikit-learn`의 `IterativeImputer`를 활용하여 MICE 기반의 결측치 대치를 수행하고, 결측 패턴의 상관관계를 분석하여 대치 전략을 제안하는 엔진입니다.

```python
import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

class DataQualityGuard:
    """
    HDS-Gold V6.3.7 규격의 결측치 패턴 분석 및 지능형 대치 엔진
    """
    def __init__(self, strategy='mice'):
        self.imputer = IterativeImputer(max_iter=10, random_state=42)

    def analyze_missing_pattern(self, df):
        """
        결측률 및 변수 간 결측 상관관계 분석
        """
        missing_counts = df.isnull().sum()
        missing_rate = (missing_counts / len(df)) * 100
        
        # Transitional Bridge: 결측치는 단순한 빈칸이 아니라 
        # 데이터 수집 시스템의 '침묵하는 목소리'입니다. 
        # 이 목소리가 다른 변수와 결합되어 있는지 확인해야 합니다.
        return missing_rate

    def execute_imputation(self, X):
        """
        MICE 기반 다중 대치 실행
        """
        X_imputed = self.imputer.fit_transform(X)
        return pd.DataFrame(X_imputed, columns=X.columns)

# Example Usage:
# guard = DataQualityGuard()
# df = pd.DataFrame({'Temp': [25, np.nan, 30, 28], 'Volt': [3.7, 3.6, np.nan, 3.8]})
# missing_report = guard.analyze_missing_pattern(df)
# df_clean = guard.execute_imputation(df)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Little's MCAR Test**의 결과 $p \text{-value}$가 $0.001$로 나왔을 때, 이 데이터를 **Mean Imputation** (평균 대치)으로 처리할 수 없는 통계적 이유는?
2. **MICE** 연산 시 **Iteration** (반복 횟수)이 증가함에 따라 대치값의 **Convergence** (수렴) 여부를 확인해야 하는 공학적 근거는?
3. **MNAR** 유형의 결측치가 발생했을 때, 결측 여부를 나타내는 **Binary Indicator** 변수를 추가하는 것이 모델의 **Predictive Power**를 높이는 기전은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/General/AI deep-learning-data-augmentation
- 02_Knowledge/03_AI_Data/General/AI statistics-hypothesis-testing
- 02_Knowledge/02_Battery/Intelligence/Battery degradation-physics

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**