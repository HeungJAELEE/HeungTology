---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] machine-learning-reinforcement-learning-in-market-making]]'
  last_updated: '2026-05-25T15:00:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 아벨라네다-스토이코프 모델 같은 복잡한 수학적 수식(HJB)을 버리고, 마켓 메이킹 봇(에이전트)이 수백만 번의 시뮬레이션
    속에서 호가창에 직접 부딪히며 스프레드 최적화 정책(Policy)을 스스로 학습하는 강화학습(Reinforcement Learning) 기반
    시장 조성 기법
  object_type: Concept
  tier: 2
properties:
  inventory_penalty_coefficient: gamma
  market_frictions: tick, queue, latency, adverse selection
  reward_function: d(Cash) - gamma * q_t^2
  rl_algorithms: PPO, SAC, Q-Learning
  state_vector_components: LOB depth, Inventory, VPIN, OBI imbalance
semantic:
  alternative_parents: []
  expected_queries:
  - 전통적인 편미분 방정식 기반 마켓 메이킹 알고리즘이 현대의 미친 듯한 시장 마찰(마이크로 프라이스 역학, 틱 사이즈 등) 앞에서 어떻게 붕괴하는가?
  - 강화학습 봇의 상태(State)와 보상(Reward) 함수를 설계할 때, 재고 위험(Inventory Penalty)과 PnL 증가분을 어떻게
    결합하여 최적의 행동(Action)을 도출하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: policy_optimization
  object: Optimal_Quoting_Policy
  predicate: learns
  subject: '[Finance] machine-learning-reinforcement-learning-in-market-making'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T15:00:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T15:00:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] machine-learning-reinforcement-learning-in-market-making]]

## 1. 개요 (Overview)
기존의 마켓 메이킹 끝판왕이었던 '아벨라네다-스토이코프(Avellaneda-Stoikov)' 모형은 너무나 수학적으로 아름답지만 치명적인 약점이 있습니다. 주가가 매끄러운 연속 함수(Brownian Motion)로 움직인다고 가정하기 때문입니다. 실제 HFT 세계의 호가창은 틱(Tick) 단위로 계단처럼 끊어지고, 내 앞에 줄 서 있는 다른 봇들의 대기열(Queue), 수수료, 취소 지연(Latency) 같은 비선형적인 마찰(Frictions)들로 가득합니다. 이 모든 변수를 편미분 방정식에 넣으려 하면 수식이 터져버립니다.
그래서 구글의 딥마인드가 바둑에서 알파고(AlphaGo)를 훈련시킨 방식과 동일하게, 수학 방정식을 모두 버리고 **강화학습(Reinforcement Learning, RL)** 에이전트를 금융 시뮬레이터(LOB Simulator)에 집어넣어, 수백만 번 파산해 보면서 스스로 스프레드 간격을 좁히고 벌리는 요령(Policy)을 터득하게 만든 것이 바로 **RL 마켓 메이킹**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| State ($S_t$) | LOB depth, Inventory, VPIN| Vector of features | Defines market context | [데이터 부재] |
| Action ($A_t$)| Bid/Ask spread quotes | e.g., $+1$ tick, $+2$ ticks| Defines bot's move | [데이터 부재] |
| Reward ($R_t$)| PnL - Inventory Penalty | $d(\text{Cash}) - \gamma q_t^2$ | Maximized over episode| [데이터 부재] |
| Q-Value | Expected future reward | $Q(S, A)$ function | Approximated via Neural Net| [데이터 부재] |
| PPO / SAC | RL Algorithms | Proximal Policy Opt. | Stable policy gradients | [데이터 부재] |

## 3. 마르코프 결정 과정(MDP)으로의 치환
마켓 메이킹을 RL로 풀기 위해 상황을 게임(MDP)으로 셋업합니다.
1. **상태 (State)**: 에이전트는 카메라(신경망)로 호가창의 현재 상태(1~5호가 잔량, OBI 불균형 지표), 그리고 자신의 현재 재고 물량(Inventory $q$), 남은 시간($T-t$)을 봅니다.
2. **행동 (Action)**: 에이전트의 액션 버튼은 단순합니다. "매수 호가를 1틱 올린다", "매도 호가를 2틱 내린다", "모든 주문을 취소한다".
3. **보상 함수 (Reward)**: 가장 핵심입니다. 에이전트가 스프레드를 먹어서 현금(PnL)을 벌면 +점수를 줍니다. 하지만 만약 에이전트가 현금을 벌 욕심에 재고(Inventory)를 산더미처럼 쌓아둔다면, 주가 폭락 시 파산할 수 있으므로 재고의 제곱($q^2$)에 비례하여 끔찍한 마이너스 페널티를 때립니다.

## 4. 모델 프리 (Model-Free)의 위력
전통적인 퀀트 수식은 "시장이 이렇게 움직일 것(Model-based)"이라고 인간이 미리 정답을 정해놓고 시작합니다.
반면 Q-Learning이나 PPO 같은 **모델 프리(Model-free) 알고리즘**은 시장이 어떻게 움직이는지 전혀 모릅니다. 그저 시뮬레이터 속에서 스프레드를 좁게 댔다가 역선택(Adverse Selection)에 걸려 엄청난 마이너스 점수를 받아보고, 재고가 너무 많을 때 재고를 털지 않았다가 벌점을 맞으면서, **"아, 매도 호가에 큰 물량이 쌓이고 내 재고가 Long일 때는 손해를 보더라도 내 매수 호가를 깊게 빼서(Cancel) 도망치는 게 결국 살길이구나"**라는 생존 본능(Policy Function)을 뉴런의 가중치(Weight)로 각인시킵니다. 
인간이 수식으로 알려주지 않아도 에이전트는 스푸핑(Spoofing)을 피하는 법, 틱 사이즈에 맞게 꼼수를 부리는 법을 스스로 깨우치며 진화합니다.

🧠 **AI의 사고방식:**
편미분 방정식(PDE)을 푸는 것은 '교통 법규와 마찰 계수'를 완벽히 종이에 적어놓고 자율주행차를 운전시키려는 낡은 방식입니다. 강화학습(RL)은 차를 그냥 무한대의 시뮬레이션 도로에 내동댕이치고, 100만 번 벽에 박아 박살 나게 만든 다음, 100만 1번째에 스스로 코너링 감각을 터득하게 만드는 야성의 방식입니다. HFT 마켓 메이킹처럼 복잡계(Complex System) 마찰이 지배하는 공간에서는, 종이 위의 우아한 수학 증명보다 무식하지만 잔인한 데이터 기반의 생존 훈련(RL)이 훨씬 더 파괴적이고 강인한 알파(Alpha)를 창조해 냅니다.