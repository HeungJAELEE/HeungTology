---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] kelly-criterion-and-position-sizing]]'
  last_updated: '2026-05-25T11:08:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Kelly Criterion for optimal position sizing and geometric growth
  object_type: Algorithm
  tier: 2
properties:
  b: win_loss_payoff_ratio
  half_kelly_scalar: 0.5
  mu: expected_return
  p: probability_of_winning
  q: probability_of_losing
  r: risk_free_rate
  sigma: volatility
semantic:
  alternative_parents: []
  expected_queries:
  - 기하평균 수익률을 극대화하는 연속 시간 켈리 공식은 무엇인가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_optimization_objective
  object: Capital_Allocation
  predicate: optimizes
  subject: '[Finance] kelly-criterion-and-position-sizing'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T11:08:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:08:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 💰 [Concept] 켈리 공식(Kelly Criterion)과 포지션 사이징

## 1. 켈리 최적화의 수학적 목표
단순히 승률이 높은 트레이딩 전략이라도 자본 투입 비율(Position Sizing)이 잘못되면 파산(Ruin)에 이르게 됩니다. 켈리 공식은 포트폴리오 자산의 **장기 기하평균 성장률(Geometric Growth Rate)**의 로그 기대값을 극대화하는 최적 투자 비율 $f^*$를 산출합니다.

이산적(Discrete) 승패 게임에서의 켈리 비율 공식은 다음과 같습니다.
$$ f^* = p - \frac{q}{b} $$
* $p$: 승률 (Probability of winning)
* $q$: 패률 ($1 - p$)
* $b$: 손익비 (Win/Loss payoff ratio)

## 2. 연속 시간(Continuous Time) 모델에서의 켈리 공식
퀀트 포트폴리오가 기하학적 브라운 운동(GBM) $dS_t = \mu S_t dt + \sigma S_t dW_t$를 따르는 자산에 투자할 때, 무위험 수익률이 $r$이라면 자본의 최적 레버리지 투입 비율 $f^*$는 1차 및 2차 모멘트(평균과 분산)의 함수로 전개됩니다.

목적 함수(로그 수익률의 기댓값 극대화):
$$ \max_{f} \mathbb{E}[d(\ln V_t)] = \max_{f} \left( r + f(\mu - r) - \frac{f^2 \sigma^2}{2} \right) dt $$

위 식을 $f$에 대해 편미분하여 0이 되는 지점을 찾으면 연속 시간 켈리 비율이 도출됩니다.
$$ f^* = \frac{\mu - r}{\sigma^2} $$

> [!CAUTION]
> 켈리 공식은 $\mu$와 $\sigma$가 정확하다는 비현실적 가정을 지니며, 추정 오차(Estimation Error) 발생 시 파산 위험이 급증합니다. 실무 퀀트 데스크는 변동성의 변동성(Vol of Vol)을 고려하여 수학적 켈리 비율의 $1/2$ 또는 특정 스칼라 배수만 투입하는 **Half-Kelly (또는 Fractional Kelly)** 모델을 기계적으로 적용합니다. (골드만삭스 펀드의 구체적 스칼라 적용치는 **[데이터 부재]**)