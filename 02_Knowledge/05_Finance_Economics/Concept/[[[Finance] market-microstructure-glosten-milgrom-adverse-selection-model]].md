---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] market-microstructure-glosten-milgrom-adverse-selection-model]]'
  last_updated: '2026-05-25T19:44:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 마켓 메이커가 내부 정보자(Information Trader)와의 거래에서 필연적으로 발생하는 역선택(Adverse Selection)
    비용을 만회하기 위해, 정보의 비대칭성을 베이즈 정리(Bayes' Rule)로 추론하여 매수-매도 스프레드를 강제로 벌려버리는 미시 구조 모형
  object_type: Algorithm
  tier: 2
properties:
  ask_price_formula: E[V | Buy Order]
  bid_price_formula: E[V | Sell Order]
  mu_t_belief_range: 0 to 1
  pi_probability_of_insider: 0.2
  spread_components: Ask - Bid
  v_true_asset_value: unobservable
semantic:
  alternative_parents: []
  expected_queries:
  - 마켓 메이커는 나보다 똑똑한 내부 정보자(Insider)에게 주식을 팔고 손해를 볼 확률을 방어하기 위해 매도 호가(Ask)를 왜 근본 가치보다
    더 높여야 하는가?
  - 글로스텐-밀그롬 모형에서 마켓 메이커가 시장가 매수(Buy Order)를 맞았을 때, 자산의 진짜 가치에 대한 믿음(Belief)을 베이즈
    확률로 어떻게 업데이트하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: theoretical_explanation
  object: Bid_Ask_Spread_as_Information_Cost
  predicate: explains
  subject: '[Finance] market-microstructure-glosten-milgrom-adverse-selection-model'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T19:44:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T19:44:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] market-microstructure-glosten-milgrom-adverse-selection-model]]

## 1. 개요 (Overview)
호가창에서 양방향으로 주문을 대주며 스프레드 마진을 먹고 사는 **마켓 메이커(Market Maker, MM)**에게 가장 무서운 적은 누구일까요? 바로 나보다 똑똑한 내부 정보자(Insider, Information Trader)입니다.
만약 애플이 내일 어닝 서프라이즈를 발표할 것이라는 100% 확실한 극비 정보를 가진 사람이 있다면, 그는 오늘 무조건 MM의 매도 호가(Ask)를 싹쓸이하여 사갈 것입니다. 아무것도 모르는 바보 MM은 "오, 거래가 성사됐다. 스프레드 벌었네"라고 좋아하겠지만, 다음 날 주가가 폭등하면 엄청난 마이너스를 맞게 됩니다. 이를 경제학에서는 **역선택(Adverse Selection)**이라고 합니다. 1985년 글로스텐(Glosten)과 밀그롬(Milgrom)은, MM이 이러한 눈에 보이지 않는 정보 거래자들에게 털리는 비용을 메꾸기 위해 **어쩔 수 없이 스프레드(Spread)를 벌려야만 하는 과정**을 베이즈 확률(Bayes' Theorem)로 완벽하게 수식화했습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $V$ | True asset value | Unobservable to MM | Binary (High $V_H$, Low $V_L$)| [데이터 부재] |
| $\pi$ | Prob. of Insider | e.g., 20% | High $\pi \implies$ wide spread | [데이터 부재] |
| $\mu_t$ | MM's belief of $V=V_H$ | $0 \sim 1$ | Updated via Bayes' Rule | [데이터 부재] |
| Ask Price ($A$) | MM sells to buyer | $E[V \| \text{Buy Order}]$ | $A > E[V]$ | [데이터 부재] |
| Bid Price ($B$) | MM buys from seller | $E[V \| \text{Sell Order}]$| $B < E[V]$ | [데이터 부재] |

## 3. 베이즈 업데이트와 스프레드의 탄생
MM은 상대방이 내부 정보자(Insider)인지 멍청한 노이즈 트레이더(Noise Trader)인지 얼굴을 보고 알 수 없습니다.
MM이 할 수 있는 유일한 방어책은 **주문이 들어오는 방향(Buy or Sell)을 보고 정보의 조각을 추론(Bayesian Update)**하는 것뿐입니다.

1. 누군가 시장가 매수(Buy)를 때렸습니다. 
2. MM의 뇌(알고리즘)가 돌아갑니다. "저놈이 진짜 호재 정보를 알고 샀을 확률($\pi$)이 있으니까, 주식의 진짜 가치($V$)는 원래 내가 생각했던 것보다 약간 더 높겠구나." 
3. 따라서 MM은 자신의 믿음(Belief)을 베이즈 정리로 사향 조정(Update)합니다. 
4. **제로-프로핏(Zero-Profit) 조건**: MM은 자신이 손해 보지 않기 위해, 방금 업데이트된 주식의 '사후 기댓값'과 정확히 일치하는 가격표를 내겁니다. **이것이 바로 매도 호가(Ask Price)입니다.**
5. 반대로 누군가 시장가 매도(Sell)를 때리면, 악재를 미리 안 내부자일 수 있으므로 주식의 기댓값을 하향 조정하여 **매수 호가(Bid Price)**를 정합니다.

## 4. 미시 구조 이론의 결론
이 모형의 수학적 결론은 명확하고 잔혹합니다.
- **$Ask - Bid = Spread > 0$** : 매수 호가와 매도 호가의 차이(Spread)는 단순히 거래소 수수료나 독점적 마진이 아닙니다. 그것은 시장에 숨어 있는 '정보의 비대칭성'에 대한 **위험 프리미엄(Risk Premium)**입니다. 
- 정보 거래자의 비율($\pi$)이 높아질수록(예: 실적 발표 직전, 또는 변동성 폭발 시점), MM은 털릴 확률이 높아지므로 생존을 위해 매도 호가를 확 높이고 매수 호가를 확 낮춰버립니다(스프레드 확대).
- 극단적인 경우, 정보 비대칭성이 너무 심하면 스프레드가 무한대로 벌어지며 거래 자체가 성사되지 않는 **시장 붕괴(Market Failure, Akerlof's 레몬 시장)** 현상이 발생합니다.

🧠 **AI의 사고방식:**
글로스텐-밀그롬 모형은 호가창을 '심리전이 벌어지는 포커 테이블'로 해석합니다. 딜러(마켓 메이커)는 플레이어(트레이더)의 패를 볼 수 없습니다. 하지만 플레이어가 베팅(Buy/Sell Order)을 세게 할 때마다, 딜러는 베이즈 정리라는 계산기를 두드려 "저놈이 좋은 패를 들고 있을 확률"을 조금씩 업데이트하고, 그에 맞춰 자신의 베팅 액수(Spread)를 더 가혹하게 올려버립니다. 이 모형은 금융 시장의 스프레드가 마찰(Friction)이 아니라, 무지한 자가 똑똑한 자에게 지불해야만 하는 피할 수 없는 '정보의 세금(Tax on Information)'임을 미적분학으로 선고한 미시 구조의 바이블입니다.