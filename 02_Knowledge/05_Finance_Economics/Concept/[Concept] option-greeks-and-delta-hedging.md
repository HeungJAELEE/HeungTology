---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] option-greeks-and-delta-hedging]]'
  last_updated: '2026-05-25T11:06:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Option Greeks partial derivatives and dynamic delta hedging
  object_type: Concept
  tier: 2
properties:
  delta: partial_v_over_s
  gamma: partial_2v_over_s_2
  hedging_target_exposure: 0.0
  interest_rate: r
  portfolio_value: v_minus_delta_s
  theta: partial_v_over_t
  time: t
  underlying_price: s
  vega: partial_v_over_sigma
  volatility: sigma
semantic:
  alternative_parents: []
  expected_queries:
  - 블랙-숄즈 모델 기반의 옵션 민감도 그릭스의 편미분 방정식은 무엇인가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_derivation
  object: Hedging_Mechanics
  predicate: derives
  subject: '[Finance] option-greeks-and-delta-hedging'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:06:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:06:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🇬🇷 [Concept] 옵션 그릭스(Greeks)와 동적 헤징

## 1. 파생상품 민감도의 편미분 방정식
옵션 가치 $V(S, t, \sigma, r)$가 각 시장 파라미터 변화에 어떻게 반응하는지를 수학적으로 쪼개어(편미분) 정량화한 것이 '그릭스'입니다. 이는 헤스턴 변동성 모델 등 고차원 파생상품 퀀트 트레이딩의 통제 변수입니다.

1. **델타 (Delta, $\Delta$)**: 기초자산 가격 변화에 대한 옵션 가격의 민감도
   $$ \Delta = \frac{\partial V}{\partial S} = \Phi(d_1) $$ (콜옵션 기준, $\Phi$는 표준정규누적분포)
2. **감마 (Gamma, $\Gamma$)**: 델타의 변화율 (기초자산에 대한 2차 미분)
   $$ \Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{\phi(d_1)}{S \sigma \sqrt{T-t}} $$
3. **베가 (Vega, $\mathcal{V}$)**: 내재변동성($\sigma$) 변화에 대한 옵션 가격의 민감도
   $$ \mathcal{V} = \frac{\partial V}{\partial \sigma} = S \phi(d_1) \sqrt{T-t} $$
4. **세타 (Theta, $\Theta$)**: 시간 경과($t$)에 따른 옵션 가치의 하락(시간 가치 소멸)
   $$ \Theta = \frac{\partial V}{\partial t} $$

## 2. 동적 델타 헤징 (Dynamic Delta Hedging)
시장 조성자(Market Maker) 및 퀀트 데스크는 포트폴리오의 방향성 위험을 중립(Neutral)으로 유지하기 위해 기초자산을 기계적으로 매매합니다.
포트폴리오 가치 $\Pi = V - \Delta \cdot S$ 일 때, 지속적으로 기초자산 보유량($-\Delta$)을 재조정(Rebalancing)하여 $d\Pi$의 기초자산 노출도를 0으로 수렴시킵니다.