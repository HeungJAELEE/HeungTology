---
Basic:
  id: "[[[Battery] preprocessing-best-practices"
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

# [[[Battery] preprocessing-best-practices

## 1. [왜 배우는가? (Why)]]
머신러닝 전처리는 데이터를 모델이 이해할 수 있는 형태로 변환하는 과정입니다. 이 단계에서 발생하는 미세한 실수는 모델이 학습 데이터에만 과적합되거나, 실제 배포 시 성능이 폭락하는 결과로 이어집니다.

## 2. [전처리 가이드라인 사양 (Best Practice Specs)]
| 제어 파라미터 | 정밀 타겟 / 수치 | 비고 |
| :--- | :--- | :--- |
| **Leakage Detection Score** | $0.0$ | 학습/테스트 간 정보 누수 발생 건수 |
| **Pipeline Modularity** | $100\%$ | 모든 전처리 단계의 단일 파이프라인 객체화율 |
| **Transformation Reproducibility** | $\Delta < 10^{-10}$ | 재실행 시 결과값의 수치적 불일치 오차 |
| **Encoding Efficiency** | $< 50$ dims | 임베딩/인코딩을 통한 차원 수 제어 가이드 |
| **Execution Speed** | $< 1\text{ms/row}$ | 추론 단계(Inference)에서의 전처리 처리 지연 시간 |

## 2. 절대 금기 사항: 데이터 누수 (Data Leakage)

데이터 누수는 테스트 데이터의 정보가 학습 과정에 '몰래' 들어가는 현상입니다. 이를 방지하기 위한 황금률은 다음과 같습니다.

### 1.1 "Split First, Fit Later"
- **잘못된 예**: 전체 데이터의 평균으로 결측치를 채운 후 Train/Test 분할 (테스트 데이터의 평균 정보가 학습 데이터에 스며듦).
- **올바른 예**: Train 데이터에서만 평균을 계산(`fit`)하고, 그 값을 Test 데이터에 적용(`transform`)합니다.

## 2. 수치형 피처 스케일링 (Scaling)

데이터의 범위가 다르면 특정 피처가 모델에 과도한 영향력을 행사할 수 있습니다.

| 방식 | 수식 | 특징 및 용도 |
| :--- | :--- | :--- |
| **Standardization (표준화)** | $z = \frac{x - \mu}{\sigma}$ | 평균 0, 표준편차 1. **이상치에 상대적으로 강함**. 신경망, SVM에 권장. |
| **Normalization (정규화)** | $\frac{x - min}{max - min}$ | 0~1 사이로 압축. **이상치에 매우 취약**. KNN, K-Means 등 거리 기반 알고리즘에 권장. |
| **Robust Scaling** | $\frac{x - Q2}{IQR}$ | 중앙값과 사분위수 사용. **이상치가 많은 데이터**에 최적. |

## 3. 고차원 범주형 변수 처리 (High-cardinality)

항목(Unique values)이 수천 개인 범주형 변수에 원-핫 인코딩을 적용하면 차원이 폭증(Curse of Dimensionality)합니다.

- **Target Encoding**: 각 카테고리를 해당 카테고리의 타겟(정답) 평균값으로 치환합니다. 정보 보존력이 높지만 과적합 위험이 크므로 **Smoothing** 기법과 함께 사용해야 합니다.
- **Feature Hashing**: 해시 함수를 통해 고정된 크기의 벡터로 매핑합니다. 메모리 효율이 극도로 높지만 해석력이 떨어집니다.

## 4. 전처리 파이프라인 자동화

실수를 줄이기 위해 전처리 과정을 코드 뭉치가 아닌 **Pipeline 객체**로 관리해야 합니다.
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# 전처리 과정을 하나의 흐름으로 묶음
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# 학습 데이터로만 규칙을 생성
pipeline.fit(X_train)

# 동일한 규칙을 모든 데이터에 적용 (누수 방지)
X_train_clean = pipeline.transform(X_train)
X_test_clean = pipeline.transform(X_test)
```

## 🧠 AI의 사고방식: '공정한 비교'를 위한 환경 조성
전처리는 모델에게 "어떤 피처가 더 중요한지 편견 없이 바라보라"고 가르치는 과정입니다. 특정 피처의 숫자가 크다고 해서 그것을 더 중요하게 생각하지 않도록 스케일을 맞추고, 미래의 정보(테스트 데이터)를 엿보지 못하도록 눈을 가려주는(Leakage 방지) 이 모든 과정은, 모델이 데이터의 본질적인 '패턴'에만 집중할 수 있는 정직한 학습 환경을 설계하는 고도의 도덕적 공학입니다.

---
**관련 노드:**
- [AI] data-quality-audit (전처리 전 검사)
- [AI] feast-feature-store (전처리된 피처의 체계적 관리 및 서빙)
- [[[Battery] standardization-vs-normalization (상세 비교)
- [AI]] high-cardinality-encoding (범주형 처리 심화)
- [AI] colorspaces-and-channels (색 공간 전처리)