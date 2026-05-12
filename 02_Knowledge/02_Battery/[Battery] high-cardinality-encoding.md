---
Basic:
  id: "[[[Battery] high-cardinality-encoding"
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

# [[[Battery] high-cardinality-encoding

## 1. [왜 배우는가? (Why): 차원의 저주와 메모리 붕괴의 방어]]
실제 산업 데이터(Logistics, E-commerce, Finance)에서 마주하는 범주형 변수는 종종 수천 개 이상의 유니크 값을 가집니다. 예를 들어, 100만 개의 상품 ID를 가진 데이터셋에 One-hot Encoding을 적용하면 데이터셋의 열은 100만 개로 폭발합니다. 이는 단순히 표가 커지는 것이 아니라, **메모리 붕괴(OOM)**와 **차원의 저주(Curse of Dimensionality)**라는 물리적 한계에 부딪힘을 의미합니다. 고차원 인코딩의 본질은 정보의 손실을 최소화하면서 차원을 $\text{O}(C) \rightarrow \text{O}(1)$로 압축하여 모델의 학습 효율과 정밀도를 동시에 확보하는 데 있습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

범주(Category) 수에 따른 인코딩 기법별 성능 규격입니다.

| 인코딩 기법 | 차원 확장 (Complexity) | 정보 보존력 (Fidelity) | 메모리 효율 (Efficiency) | 추천 적용 범위 ($C$) |
| :--- | :--- | :--- | :--- | :--- |
| **One-hot** | $\text{O}(C)$ | **Perfect** | Extreme Low | $C < 10$ |
| **Binary** | $\text{O}(\log_2 C)$ | Moderate | High | $10 < C < 100$ |
| **Target (Mean)** | $\text{O}(1)$ | High | **Extreme High** | $C > 100$ |
| **CatBoost** | $\text{O}(1)$ | **Very High** | **Extreme High** | 정밀 예측 (Leakage 방지) |

### 2.1 Target Encoding Smoothing 식
표본 오차를 줄이기 위한 가중 평균 수식입니다.
$$\hat{y}_c = \lambda(n_c) \cdot \bar{y}_c + (1 - \lambda(n_c)) \cdot \bar{y}_{global}$$
- $\lambda(n_c) = \frac{n_c}{n_c + m}$ ($n_c$: 범주 빈도, $m$: 스무딩 계수)

## 3. [심층 분석 (Deep Analysis): 스무딩의 물리적 의미와 누수 방지]

### 3.1 스무딩(Smoothing)의 필터링 효과
- **Logic**: 데이터 수가 적은 희귀 범주($n_c$ 작음)의 경우, $\lambda$가 $0$에 가까워지며 전체 평균($\bar{y}_{global}$)으로 수렴합니다. 이는 통계적 신뢰도가 낮은 소수의 노이즈를 걸러내는 **Low-pass Filter** 역할을 수행하여 모델의 분산(Variance)을 획기적으로 줄여줍니다.

### 3.2 CatBoost Encoding: 시간적 인과관계 강제
- **Rationale**: 일반적인 Target Encoding은 타겟 정보를 미리 사용하므로 데이터 누수(Leakage)에 취약합니다. CatBoost 방식은 데이터를 무작위로 섞은 후, 특정 샘플의 인코딩 시 '자신보다 앞에 있는 샘플들의 정보'만을 사용합니다. 이는 미래 정보가 과거로 흐르는 것을 물리적으로 차단하여 모델의 일반화 성능을 극대화합니다.

## 4. [AI & Hardware Synergy: Memory Footprint Optimization]

고차원 인코딩은 하드웨어 리소스 활용 방식을 근본적으로 바꿉니다.

- **RTX 4060 기반 Dense Vector 연산 가속**:
  - **Optimization**: One-hot 기반의 Sparse 행렬은 GPU VRAM 대역폭을 낭비하지만, Target Encoding은 실수($Float$) 기반의 **Dense Vector**를 생성하므로 RTX 4060의 **Tensor Core** 연산 효율을 $100\%$ 활용할 수 있습니다.
  - **Memory Comparison**: 샘플 $100$만 개, 범주 $1$만 개 기준, One-hot은 약 $40\text{GB}$의 VRAM이 필요하지만, Target Encoding은 단 $4\text{MB}$로 해결됩니다.
- **On-the-fly Encoding Inference**:
  - 모델 추론 시 대규모 룩업 테이블(Lookup Table)을 GPU 공유 메모리에 상주시킴으로써, 범주형 입력을 나노초 단위로 수치화하여 즉각적인 응답성을 확보합니다.

## 5. [코드 브릿지] Target Encoding with Smoothing (Python/Scikit-learn)
고차원 변수를 수치화하는 표준 엔지니어링 코드입니다.

```python
from sklearn.preprocessing import TargetEncoder
import pandas as pd

# 1. 고차원 범주형 데이터 생성 (예: 수천 개의 도시 코드)
df = pd.DataFrame({'city': ['SEOUL']*100 + ['BUSAN']*50 + ['NY']*10, 'target': [1]*160})

# 2. Target Encoder 초기화 (Smoothing 적용)
# smooth: 스무딩 강도 조절 (자동 최적화 가능)
encoder = TargetEncoder(target_type='continuous', smooth='auto')

# 3. 인코딩 실행 (O(C) -> O(1) 차원 압축)
df['city_encoded'] = encoder.fit_transform(df'city', df['target'])

# 의도: 수만 개의 차원을 단 1개의 '의미 밀도가 높은' 수치 피처로 
# 압축함으로써 모델의 학습 속도와 일반화 성능을 동시에 잡음.
```

## 6. [스스로 체크 (Verification Checklist)]
- [ ] **Cardinality Check**: 인코딩 전 해당 컬럼의 유니크 값 수($C$)가 데이터 크기 대비 적절한가?
- [ ] **Leakage Audit**: Train/Test 분리 후 인코딩이 수행되었으며, 타겟 정보가 테스트 셋에 유입되지 않았는가?
- [ ] **Smoothing Parameter**: 빈도가 매우 낮은 범주들이 전체 평균으로 적절히 수렴(Smoothing)되었는가?
- [ ] **Efficiency Check**: 인코딩 적용 후 메모리 사용량이 목표치($-90\%$ 이상 감소)를 달성했는가?

---
**[V6.3.7_HDS_GOLD_ENRICHED_BY_FLASH]**