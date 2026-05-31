---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] glosten-milgrom-asymmetric-information]]'
  last_updated: '2026-05-25T11:08:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Glosten-Milgrom model for asymmetric information and bid-ask spread
  object_type: Concept
  tier: 2
properties:
  ask_price: A
  bid_ask_spread: S
  bid_price: B
  informed_trader_ratio: alpha
  noise_trader_ratio: 1-alpha
  prior_probability_high: pi
  v_high: V_H
  v_low: V_L
semantic:
  alternative_parents: []
  expected_queries:
  - 시장 조성자의 매수-매도 스프레드는 정보 비대칭성에 의해 어떻게 산출되는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: theoretical_modeling
  object: Bid_Ask_Spread
  predicate: explains
  subject: '[Finance] glosten-milgrom-asymmetric-information'
  weight: 0.95
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

# 🕵️ [Concept] 정보 비대칭성과 글로스텐-밀그롬(Glosten-Milgrom) 모델

## 1. 시장 조성자(Market Maker)의 역선택 딜레마
HFT(고빈도 매매) 및 유동성 공급 관점에서, 시장 조성자(MM)는 자신과 거래하려는 상대방이 단기적 노이즈 트레이더(Noise Trader)인지, 자산의 진짜 가치를 아는 정보 거래자(Informed Trader)인지 알 수 없는 **역선택(Adverse Selection)**의 위험에 직면합니다. 

글로스텐-밀그롬(1985) 모델은 이 정보 비대칭성 비용을 상쇄하기 위해 시장 조성자가 매수 호가(Bid)와 매도 호가(Ask) 사이에 넓은 스프레드(Spread)를 벌려야만 수학적으로 파산을 면할 수 있음을 증명합니다.

## 2. 베이즈 업데이트(Bayesian Updating) 매커니즘
자산의 진정한 펀더멘털 가치가 $V \in \{V_L, V_H\}$ 중 하나라고 가정합니다. 시장 조성자는 사전에 $P(V = V_H) = \pi$의 믿음을 가집니다.
시장에 참여하는 트레이더 중 정보 거래자의 비율을 $\alpha$, 무작위 매매를 하는 노이즈 거래자의 비율을 $1-\alpha$라고 정의합니다.

시장 조성자는 '누군가 매수(Buy) 주문을 던졌다는 사실' 자체에서 시장의 숨겨진 가치를 베이즈 정리로 사후 업데이트(Posterior)합니다.
$$ P(V_H | Buy) = \frac{P(Buy | V_H) P(V_H)}{P(Buy)} = \frac{(\alpha + (1-\alpha) \cdot 0.5) \pi}{\pi(\alpha + (1-\alpha) \cdot 0.5) + (1-\pi)((1-\alpha) \cdot 0.5)} $$

## 3. 제로 이윤 스프레드 (Zero-Profit Spread) 균형
완전 경쟁 하에서 시장 조성자는 기대 이윤이 0이 되는 지점에 호가를 설정합니다. 즉, 매수 호가(Bid)는 매도 주문이 들어왔을 때의 자산 기대 가치로, 매도 호가(Ask)는 매수 주문이 들어왔을 때의 기대 가치로 셋팅됩니다.

* 매도 호가 (Ask): $A = \mathbb{E}[V | Buy]$
* 매수 호가 (Bid): $B = \mathbb{E}[V | Sell]$

스프레드 $S = A - B$ 는 오직 정보 거래자의 비율 $\alpha$에 비례하여 팽창합니다. 퀀트 알고리즘이 순간적으로 스프레드가 팽창하는 것을 감지하면, 시장에 거대한 비대칭 정보(실적 발표 등)가 유출되었음을 역산하고 $OIB$(호가 불균형 비율)와 연계하여 모멘텀에 올라탈지(Liquidity Taking) 유동성을 거둘지 결정합니다.