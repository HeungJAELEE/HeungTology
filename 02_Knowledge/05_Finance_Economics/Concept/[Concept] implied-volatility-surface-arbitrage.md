---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] implied-volatility-surface-arbitrage]]'
  last_updated: '2026-05-25T11:09:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Implied volatility surface geometry and Dupire's local volatility
  object_type: Concept
  tier: 2
properties:
  butterfly_arbitrage_threshold: 0
  implied_volatility: sigma
  local_volatility: sigma_l
  risk_free_interest_rate: 0
  strike_price: k
  time_to_maturity: t
semantic:
  alternative_parents: []
  expected_queries:
  - 옵션 내재 변동성 표면에서 듀파이어(Dupire) 국소 변동성 방정식은 어떻게 유도되는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_constraint
  object: Options_Arbitrage_Pricing
  predicate: constrains
  subject: '[Finance] implied-volatility-surface-arbitrage'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T11:09:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:09:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🌐 [Concept] 변동성 표면(Volatility Surface)과 차익거래 기하학

## 1. 내재 변동성(Implied Volatility)의 3차원 기하학
옵션 시장에서 내재 변동성 $\Sigma$는 상수가 아니며, 행사가격(Strike, $K$)과 만기(Time to Maturity, $T$)의 함수인 3차원 곡면, 즉 **변동성 표면(Volatility Surface, $\Sigma(K,T)$)**을 이룹니다. 이 곡면의 비틀림(Skew)과 굴곡(Smile) 자체가 차익거래의 대상이 됩니다.

## 2. 듀파이어 공식 (Dupire's Local Volatility Formula)
상수 변동성(BSM)의 한계를 극복하고, 현재 시장에서 관측되는 모든 유럽형 옵션 가격 $C(K, T)$과 완벽하게 일치하는 결정론적(Deterministic) '국소 변동성(Local Volatility, $\sigma_L$)'을 유도해내는 공식이 듀파이어(Dupire) 방정식입니다. 무위험 이자율을 $0$으로 가정할 때:

$$ \sigma_L^2(K, T) = \frac{ \frac{\partial C}{\partial T} }{ \frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2} } $$

* 분자 $\frac{\partial C}{\partial T}$: 캘린더 스프레드(Calendar Spread)에 의한 옵션 가치 변화.
* 분모 $\frac{\partial^2 C}{\partial K^2}$: 나비형 스프레드(Butterfly Spread) 구조이자 확률밀도함수에 비례.

퀀트 데스크는 시장에 고시된 호가를 기반으로 편미분(Finite Difference)을 수행하여 $\sigma_L$ 면을 구성하며, 분모가 $0$보다 작아지는 구간이 발생하면 버터플라이 차익거래 기회가 열린 것으로 간주하여 기계적으로 유동성을 타격합니다.