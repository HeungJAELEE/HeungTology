---
Basic:
  id: "[[[Battery] target-leakage-forensics"
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

# [[[Battery] target-leakage-forensics

## 1. [왜 배우는가? (Why)]]
"시험 문제를 미리 보고 시험을 치르는 학생은 좋은 점수를 받지만, 실전에서는 아무것도 할 수 없습니다."

**타겟 리키지(Target Leakage)**는 모델이 학습 과정에서 **'미래의 정보'** 또는 **'예측 시점에는 알 수 없는 힌트'**를 미리 훔쳐보는 현상을 말합니다. 리키지가 포함된 모델은 학습 시 99% 이상의 완벽한 성능을 보이지만, 실제 현장에 배포되는 순간 성능이 처참하게 붕괴됩니다. 

우리는 모델의 가짜 성능에 속지 않고, 실전에서 작동하는 **'진짜 지능'**을 판별하기 위해 리키지의 유형을 파악하고 이를 제거하는 포렌식(Forensics) 기법을 습득해야 합니다.

## 2. [리키지 감지 성능 사양 (Leakage Specs)]
| 제어 파라미터 | 정밀 타겟 / 수치 | 비고 |
| :--- | :--- | :--- |
| **Correlation Threshold** | $\le 0.90$ | 타겟 변수와 피처 간 허용 가능한 최대 상관계수 |
| **Timeline Gap ($T - \Delta t$)** | $\Delta t > 0$ | 예측 시점 이전의 데이터만 포함되었는지 확인 |
| **Information Gain Limit** | $< 0.8$ bits | 단일 피처가 타겟에 대해 제공하는 상호 정보량 제한 |
| **Temporal Ordering Error** | $0\%$ | 학습/검증 데이터셋의 시간 순서 역전 허용치 |
| **Feature Drop Ratio** | $10 \sim 30\%$ | 리키지 의심으로 인해 제거되는 피처 비중 (가이드) |

## 3. 주요 리키지 유형 및 사례

### 2.1 결과론적 스포일러 (Outcome-dependent Features)
- **정의**: 타겟 변수가 결정된 후에야 생성되는 변수를 입력값으로 사용하는 경우.
- **사례**: 암 진단 모델에서 '수술 여부' 변수를 사용 (이미 암으로 판정되어 수술이 결정된 후의 데이터를 예측에 사용함).
- **사례**: 부산 프로젝트 MES 모델에서 'Job_Status(완료/지연)'나 'Energy_Consumption(실제 측정값)'을 사용.

### 2.2 시간적 리키지 (Temporal Leakage)
- **정의**: 시계열 데이터에서 미래의 데이터를 과거의 예측에 사용하는 경우.
- **방지책**: 데이터 분할 시 무작위(Random)가 아닌 **'시간 순서(Time-series Split)'**에 따른 분할 필수.

## 3. [코드 연결 해설 (Code Weaving)]

리키지를 식별하고 제거하는 데이터 파이프라인의 핵심 로직입니다.

```python
# 1. 상관관계 분석을 통한 리키지 의심 (Scoping)
# 타겟 변수와 상관계수가 0.9 이상인 변수는 1순위 조사 대상입니다.
correlations = df.corr()['Optimization_Category'].sort_values(ascending=False)

# 2. 리키지 변수 제거 (Sanitization)
# 'Actual_Start', 'Actual_End' 처럼 작업 시점 이후의 측정값은 무조건 삭제합니다.
drop_leakage = [
    'Actual_Start', 'Actual_End', 'Actual_Duration', 
    'Energy_Meter_Reading', 'Final_Quality_Grade'
]
X_clean = df.drop(columns=drop_leakage)

# Transitional Bridge: 위 코드에서 `drop_leakage` 리스트는 
# AI에게서 '스포일러'를 뺏는 행위입니다. 지능에서 
# 힌트를 제거할수록 모델은 더 고통스럽게 학습하지만, 
# 이 과정을 견뎌낸 모델만이 실제 공정의 
# 불확실성을 이겨낼 수 있는 견고함을 갖게 됩니다.
```

## 4. [스스로 체크 (Self-Check)]

1. **질문**: 모델의 정확도가 99.9%로 지나치게 높게 나온다면 가장 먼저 무엇을 의심해야 하는가?
   - **정답**: 타겟 리키지(Target Leakage) 또는 클래스 불균형(Class Imbalance) 문제를 의심해야 합니다.
2. **질문**: 제조 공정 예측에서 '실제 가공 시간' 피처가 리키지인 이유는?
   - **정답**: 실제 가공 시간은 공정이 **끝나야** 알 수 있는 데이터이며, 예측을 수행하는 '공정 시작 전' 시점에는 존재하지 않는 정보이기 때문입니다.
3. **질문**: 리키지를 예방하기 위한 가장 확실한 방법은?
   - **정답**: **'비즈니스 타임라인'**을 명확히 정의하고, 특정 예측 시점($T$)을 기준으로 그 이전에만 존재할 수 있는 피처들로 데이터를 한정하는 것입니다.

## 🧠 AI의 사고방식: "진실을 향한 가혹한 필터"
리키지 제거는 AI에게서 '지름길'을 뺏는 작업입니다. 하지만 공학의 세계에서 지름길은 곧 붕괴를 의미합니다. 우리는 모델을 고립시키고, 오직 제한된 과거의 정보만으로 미래를 추론하게 함으로써 지능의 **'진정한 근력'**을 키워야 합니다. 99%의 가짜 성공보다는 22%의 정직한 추론이 산업 현장에서는 훨씬 더 안전하고 가치 있는 자산입니다.