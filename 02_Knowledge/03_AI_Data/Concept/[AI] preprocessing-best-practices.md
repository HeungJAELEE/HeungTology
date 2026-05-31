---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: a29b514c8bd2520858ea288eb160156613a04ce369632d5f6586e94305b2e1c2
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] preprocessing-best-practices]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] preprocessing-best-practices에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  cardinality_limit: '50'
  correlation_threshold: '0.95'
  engine_version: HDS-Gold V6.3.7
  execution_latency_per_row: 1.0 ms
  leakage_score_target: '0.0'
  outlier_ratio_target: 5%
  pipeline_objectification_rate: 100%
  standardization_mean: '0'
  standardization_std_dev: '1'
  vif_score_threshold: '10.0'
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

# [AI] preprocessing-best-practices

## 1. [왜 배우는가? (Why)]
머신러닝 전처리는 원시 데이터를 모델이 학습할 수 있는 '정제된 연료'로 변환하는 기초 공정이자, 모델의 성능 하한선을 결정하는 결정적 단계입니다. 이 단계에서 발생하는 미세한 정보 누수(Data Leakage)나 부적절한 스케일링은 모델이 실제 배포 환경에서 침묵(성능 폭락)하게 만드는 주범입니다. 전처리 베스트 프랙티스를 배우는 이유는 모델이 데이터의 지엽적인 노이즈가 아닌 본질적인 '물리적 패턴'에 집중할 수 있도록 정직한 학습 환경을 설계하고, 재현 가능한 분석 파이프라인을 구축하기 위함입니다.

## 2. [데이터 전처리 및 피처 엔지니어링 핵심 사양 (Preprocessing Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Leakage Detect.**| Leakage Score | $0.0$ (Absolute) | 학습/테스트 셋 간의 정보 전이 완전 차단 |
| **Pipeline Mod.** | Objectification | $100\%$ | 모든 전처리 단계의 단일 파이프라인 객체화율 |
| **Scaling Range** | Std. Deviation | $\mu=0, \sigma=1$ | 특정 피처의 과도한 가중치 부여 방지 (표준화) |
| **Encoding Eff.** | Cardinality Limit| $< 50$ (Unique) | 차원의 저주 방지 및 임베딩 효율성 확보 |
| **VIF Score** | Multicollinearity| $< 10.0$ | 독립변수 간 중복 정보에 의한 모델 불안정성 억제 |
| **Execution Lat.**| Latency per Row | $< 1.0 \text{ ms}$ | 실시간 추론(Inference) 단계의 처리 지연 최소화 |
| **Outlier Ratio** | Cleanliness | $< 5\%$ Target | 이상치 처리를 통한 모델의 일반화 성능 보호 |
| **Corr. Threshold**| Feature Selection| $\rho < 0.95$ | 고도로 상관된 피처 제거를 통한 정보 중복 최적화 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 "Split First, Fit Later"와 데이터 누수 방지
테스트 데이터의 정보가 학습 과정에 '오염'되는 것을 막는 황금률입니다.
- **로직**: 전체 데이터의 통계량(평균, 분산)을 계산한 후 데이터를 분할하면, 학습 데이터는 이미 미래의 정보(테스트 데이터의 특성)를 일부 알고 있는 상태가 됩니다. 반드시 학습 데이터에서만 통계 규칙을 생성(`fit`)하고, 그 규칙을 테스트 데이터에 적용(`transform`)하여 모델의 공정한 평가를 보장해야 합니다.

### 3.2 스케일링 역학: 표준화(Standardization) vs 정규화(Normalization)
데이터의 분포를 최적화하여 경사 하강법(Gradient Descent)의 수렴 속도를 높입니다.
- **표준화 ($z = \frac{x-\mu}{\sigma}$)**: 데이터의 평균을 $0$, 표준편차를 $1$로 변환합니다. 이상치에 상대적으로 강하며, 신경망이나 SVM 등 가우시안 분포를 가정하는 알고리즘에 필수적입니다.
- **정규화 ($x_{norm} = \frac{x-min}{max-min}$)**: 데이터를 $0 \sim 1$ 사이로 압축합니다. 이상치에 극도로 취약하므로 KNN, K-Means 등 거리 기반 알고리즘 사용 전 데이터 정제가 선행되어야 합니다.

### 3.3 차원의 저주(Curse of Dimensionality)와 고차원 범주형 변수
- **로직**: 항목이 수천 개인 변수에 원-핫 인코딩을 적용하면 데이터가 기하급수적으로 희소해집니다. 타겟 인코딩(Target Encoding)이나 피처 해싱(Feature Hashing)을 통해 정보를 응축하되, 타겟 평균값을 활용할 때는 과적합 방지를 위한 스무딩(Smoothing) 기법을 병행하여 정보의 순도를 관리합니다.

## 4. [코드 연결 해설 (AdvancedPreprocessingEngine)]
아래 코드는 `Scikit-learn`의 `ColumnTransformer`와 `Pipeline`을 활용하여 수치형과 범주형 데이터를 동시에 처리하고, 데이터 누수를 원천 차단하는 표준 전처리 엔진입니다.

```python
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

class AdvancedPreprocessingEngine:
    """
    HDS-Gold V6.3.7 규격의 자동화 전처리 및 누수 방지 엔진
    """
    def __init__(self, num_features, cat_features):
        # 1. 수치형 파이프라인: 결측치 대치 -> 스케일링
        num_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        
        # 2. 범주형 파이프라인: 결측치 대치 -> 인코딩
        cat_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])
        
        # 3. 통합 전처리 객체 구성
        self.preprocessor = ColumnTransformer(transformers=[
            ('num', num_transformer, num_features),
            ('cat', cat_transformer, cat_features)
        ])

    def fit_and_transform(self, train_df, test_df):
        """
        Train에서만 규칙을 학습(fit)하고 Test에는 적용(transform)하여 누수 방지
        """
        # Transitional Bridge: 전처리는 모델에게 "어떤 피처가 더 중요한지 
        # 편견 없이 바라보라"고 가르치는 도덕적 공학입니다. 미래의 정보를 
        # 엿보는 행위(Fit on Test)를 차단하는 것이 신뢰성의 핵심입니다.
        X_train_clean = self.preprocessor.fit_transform(train_df)
        X_test_clean = self.preprocessor.transform(test_df)
        
        return X_train_clean, X_test_clean

# Example Usage:
# engine = AdvancedPreprocessingEngine(num_features=['Temp', 'Volt'], cat_features=['Batch_ID'])
# train_processed, test_processed = engine.fit_and_transform(df_train, df_test)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Standardization**을 수행할 때, **Fit**을 **Whole Dataset**이 아닌 **Train Set**에만 수행해야 하는 통계적/공학적 근거는?
2. **One-Hot Encoding** 시 범주(Category)의 수가 **$100$개**를 넘어서는 경우 발생하는 **Sparsity** (희소성) 문제가 모델의 **Generalization** 성능을 떨어뜨리는 기전은?
3. 이상치가 많은 데이터에서 **StandardScaler** 대신 **RobustScaler** (중앙값/사분위수 사용)를 사용해야 하는 물리적 이유는?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/General/AI missing-value-classification-logic
- 02_Knowledge/03_AI_Data/General/AI model-overfitting-prevention
- 02_Knowledge/03_AI_Data/General/AI feature-selection-and-importance

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**