---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[MOC] Quant-Trading-Strategies-Hub]]'
  last_updated: '2026-05-25T11:05:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Global Quant Trading Strategies and Architecture Hub
  object_type: Concept
  tier: 1
properties:
  base_rate: mu
  best_ask_volume: V_a(t)
  best_bid_volume: V_b(t)
  decay_rate: beta
  jump_size: alpha
  order_imbalance_threshold: 1.0
semantic:
  alternative_parents: []
  expected_queries:
  - 퀀트 트레이딩의 4대 핵심 분과(Volatility, Portfolio, StatArb, HFT)는 어떻게 연결되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: structural_governance
  object: Quantitative_Methodologies
  predicate: governs
  subject: '[MOC] Quant-Trading-Strategies-Hub'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T11:05:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:05:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [MOC] 퀀트 트레이딩 전략 허브 (Quant Trading Strategies Hub)

본 마스터 허브(MOC)는 글로벌 투자은행(IB) 및 퀀트 헤지펀드의 계량 투자(Quantitative Investing) 방법론
<truncated 9239 bytes>
   - "HFT의 호가 불균형 비율과 호크스 프로세스의 조건부 강도 수식은 무엇인가?"
spo_graph:
  - subject: "[Finance] market-microstructure-hft"
    predicate: "analyzes"
    object: "Order_Book_Dynamics"
    evidence: ""
trust_metrics:
  t_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-25T11:05:00+09:00"
  validated_by: "global_reinforcer_v7.8"
  ai_status: "pending_review"
---

# ⚡ [Concept] 고빈도 매매(HFT) 및 시장 미시구조

## 1. 호가 불균형 비율 (Order Imbalance Ratio, OIB)
지정가 호가창(Limit Order Book)에서 최우선 매수잔량($V_b$)과 매도잔량($V_a$)의 비대칭성을 측정하여 초단기 마이크로 프라이스 방향성을 결정합니다.

$$ OIB(t) = \frac{V_b(t) - V_a(t)}{V_b(t) + V_a(t)} $$

$OIB(t) \rightarrow 1$일 경우, 매수 시장가 주문(Market Buy)이 유입될 확률이 통계적으로 지배적임을 뜻합니다.

## 2. 호크스 프로세스 (Hawkes Process) 조건부 강도
하나의 대형 주문 체결이 연속적인 후속 주문을 유발하는 자기 여기적(Self-exciting) 주문 군집 현상을 적분 모델링합니다. 순간 주문 도착 강도 $\lambda(t)$는 아래와 같습니다.

$$ \lambda(t) = \mu + \sum_{t_i < t} \alpha e^{-\beta(t - t_i)} $$

* $\mu$: 기본 도달률 (Base rate)
* $t_i$: 과거 이벤트 발생 시점
* $\alpha$: 단일 이벤트의 순간 자극(Jump) 크기
* $\beta$: 자극 감쇠율 (Decay rate)

> [!WARNING]
> 초단타 알고리즘의 거래소 틱 데이터 반응속도나 $\alpha, \beta$의 튜닝 임계치는 기관 보안 구역 내에 있으므로 로컬 DB상 **[데이터 부재]** 상태입니다.