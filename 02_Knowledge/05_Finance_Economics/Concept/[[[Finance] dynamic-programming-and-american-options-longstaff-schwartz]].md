---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] dynamic-programming-and-american-options-longstaff-schwartz]]'
  last_updated: '2026-05-25T14:57:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 만기 전 언제든 행사할 수 있는 미국형(American) 옵션의 가치를 계산하기 위해, 몬테카를로 시뮬레이션(정방향)과
    최소자승법(OLS) 회귀 분석을 결합하여 동적 계획법(역방향)으로 최적 행사 경계(Optimal Exercise Boundary)를 찾아내는
    롱스태프-슈워츠(Longstaff-Schwartz) 모형
  object_type: Algorithm
  tier: 2
properties:
  algorithm_name: Least Squares Monte Carlo (LSM)
  continuation_value_formula: E[e^{-r} V_{t+1} | S_t]
  decision_rule: If EV_t > CV_t, Exercise
  exercise_value_formula: max(K-S_t, 0)
  mc_path_count_range: 100,000 ~ 1,000,000
  polynomial_basis_features: S_t, S_t^2, S_t^3
  regression_method: Ordinary Least Squares (OLS)
  simulation_model: Geometric Brownian Motion (GBM)
semantic:
  alternative_parents: []
  expected_queries:
  - 유럽형 옵션과 달리 미국형 옵션은 왜 블랙-숄즈 공식처럼 깔끔한 해석해(Closed-form Solution)를 가질 수 없는가?
  - 롱스태프-슈워츠(LSM) 모델은 몬테카를로 시뮬레이션이 끝난 후, 왜 만기(T)에서 현재(0) 시점으로 거꾸로(Backward) 역산하며 회귀
    분석을 돌리는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: solves_computational_problem
  object: American_Option_Pricing
  predicate: solves
  subject: '[Finance] dynamic-programming-and-american-options-longstaff-schwartz'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:57:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:57:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] dynamic-programming-and-american-options-longstaff-schwartz]]

## 1. 개요 (Overview)
만기일(T) 딱 하루에만 행사할 수 있는 유럽형(European) 옵션은 블랙-숄즈 방정식에 숫자를 넣으면 정답이 바로 나옵니다. 하지만 만기 전 아무 때나 마음대로 행사할 수 있는 **미국형(American) 옵션**은 퀀트들에게 지옥과 같습니다. 매 초, 매 순간마다 "지금 당장 행사해서 현금을 챙길까(Immediate Exercise)?" 아니면 "옵션을 들고 내일까지 더 버텨볼까(Continuation Value)?"를 끊임없이 비교하며 최적의 타이밍을 찾아야 하는 '최적 정지 문제(Optimal Stopping Problem)'이기 때문입니다.
2001년 프란시스 롱스태프와 에두아르도 슈워츠는 몬테카를로 시뮬레이션으로 수십만 개의 주가 경로를 무작위로 뿌린 뒤, 만기에서부터 거꾸로(Backward) 역산하면서 **최소자승법(OLS) 회귀 분석을 통해 '더 버텼을 때의 기대 가치(Continuation Value)'를 추정해 내는 LSM(Least Squares Monte Carlo) 알고리즘**을 발명했습니다. 이로써 이자율 옵션과 같은 복잡한 경로 의존형(Path-dependent) 미국형 파생상품의 프라이싱이 마침내 정복되었습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $N$ | Number of MC paths | $100,000 \sim 1,000,000$| Forward simulation | [데이터 부재] |
| $EV_t$ | Exercise Value | $\max(K-S_t, 0)$ for Put| Known exactly at $t$ | [데이터 부재] |
| $CV_t$ | Continuation Value | $E[e^{-r} V_{t+1} \| S_t]$ | Estimated via OLS | [데이터 부재] |
| Polynomial Basis| Features for OLS | $S_t, S_t^2, S_t^3 \dots$| Captures non-linearity| [데이터 부재] |
| Decision Rule | Maximize payoff | If $EV_t > CV_t$, Exercise| Dynamic programming | [데이터 부재] |

## 3. 롱스태프-슈워츠 (LSM) 알고리즘의 3단계
### Phase 1: 정방향 몬테카를로 (Forward Simulation)
먼저 현재 시점(0)부터 만기 시점(T)까지 수십만 개의 가상 주가 경로를 기하 브라운 운동(GBM)으로 시뮬레이션하여 미래의 거대한 거미줄을 만듭니다.

### Phase 2: 역방향 동적 계획법 (Backward Induction)
만기(T) 시점의 옵션 가치는 명확합니다. 여기서부터 시간을 하루씩 과거($t$)로 되돌리며 매 노드마다 두 가지 가치를 비교합니다.
1. **당장 행사할 가치 (EV)**: 풋옵션이라면 $K - S_t$. 이건 주가만 알면 초등학생도 계산할 수 있습니다.
2. **들고 버틸 가치 (CV)**: 내일 이후에 받게 될 현금 흐름들의 현재가치입니다. 미래는 불확실하므로, 우리는 이 값을 "현재 주가($S_t$)가 주어졌을 때의 조건부 기댓값"으로 추정해야 합니다.

### Phase 3: 회귀 분석(OLS)을 통한 조건부 기댓값 추정의 천재성
롱스태프와 슈워츠의 천재성은 바로 이 '버틸 가치(CV)'를 구하기 위해 **회귀 분석(Cross-sectional Regression)**을 썼다는 점입니다.
특정 시점($t$)에서 옵션이 내가격(ITM) 상태인 경로들만 모아서, "현재 주가($S_t$)"를 X축으로 삼고 "미래에 실제로 실현된 현금 흐름 할인값"을 Y축으로 삼아 다항식 회귀($Y = a + bX + cX^2$) 곡선을 그립니다. 
이 곡선(회귀식)이 바로 '현재 주가가 얼마일 때 더 버티면 얼마를 벌 수 있는지'를 알려주는 **기대 가치 함수**가 됩니다. 이제 곡선에서 계산된 $CV_t$와 당장 행사할 가치 $EV_t$를 비교하여, $EV_t > CV_t$인 지점에서는 옵션을 행사(Exercise)한다고 표시하고 과거로 계속 넘어가면 됩니다.

🧠 **AI의 사고방식:**
미국형 옵션을 행사하는 것은 체스 게임의 '수읽기'와 같습니다. 당장 눈앞의 폰(Pawn)을 잡아먹는 게 이득인지($EV$), 아니면 안 먹고 3턴 뒤에 상대방의 퀸(Queen)을 잡을 확률에 베팅하는 게 이득인지($CV$)를 판단해야 합니다. 전통적 트리(Tree) 모델은 이 경우의 수를 전부 계산하려다 차원의 저주에 빠져 붕괴했습니다. LSM 모델은 머신러닝의 뼈대인 회귀 분석(Regression)을 도입하여, 수십만 번의 시뮬레이션 경험을 뭉뚱그려 "대충 현재 판이 이 모양($S_t$)이면, 퀸을 잡을 기대 가치는 이 정도($CV$) 곡선이 나온다"는 패턴(근사치)을 학습시킵니다. 정밀한 전수조사를 포기하는 대신, 통계적 통찰력을 통해 무한대에 가까운 차원의 저주를 가뿐히 베어버린 동적 계획법(Dynamic Programming)의 예술입니다.