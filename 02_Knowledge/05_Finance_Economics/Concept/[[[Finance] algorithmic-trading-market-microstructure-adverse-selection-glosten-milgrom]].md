---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-market-microstructure-adverse-selection-glosten-milgrom]]'
  last_updated: '2026-05-26T07:48:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 호가창(LOB)에 유동성을 공급하는 마켓 메이커(MM)가 왜 무조건 수익(스프레드 차익)을 내지 못하고 파산하는지에 대한
    해답. 나보다 정보가 많은 내부자(Informed Trader)와의 거래에서 기계적으로 손해를 볼 수밖에 없는 역선택(Adverse Selection)의
    공포와 이를 수학적으로 증명한 Glosten-Milgrom 모형
  object_type: Concept
  tier: 2
properties:
  ask_price_expectation: E[V|Buy]
  bid_price_expectation: E[V|Sell]
  informed_probability_mu: 0.1-0.2
  spread_calculation: ask_price - bid_price
semantic:
  alternative_parents: []
  expected_queries:
  - 아무 생각 없이 매수 호가와 매도 호가를 동시에 걸어두고 스프레드만 챙기는 마켓 메이커(MM) 봇은 왜 한 달도 안 되어 계좌가 녹아내리는가?
  - Glosten-Milgrom 모형에서 '내부자(Informed Trader)'의 존재 확률이 높아질수록 왜 시장의 매수-매도 스프레드가 기하급수적으로
    넓어지는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: theoretical_explanation
  object: Market_Maker_Losses_due_to_Informed_Trading
  predicate: explains
  subject: '[Finance] algorithmic-trading-market-microstructure-adverse-selection-glosten-milgrom'
  weight: 0.9
temporal:
  valid_from: '2026-05-26T07:48:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:48:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-market-microstructure-adverse-selection-glosten-milgrom]]

## 1. 개요 (Overview)
많은 초보 퀀트들이 범하는 가장 큰 착각 중 하나는 "마켓 메이킹(Market Making)은 무위험 돈복사기"라는 것입니다. 100달러에 매수 호가(Bid)를 깔고 101달러에 매도 호가(Ask)를 깔아두면, 개미들이 샀다 팔았다 하면서 나에게 1달러의 스프레드(Spread)를 계속 공짜로 떠먹여 줄 것이라 믿습니다.
하지만 시장에는 아무 정보 없이 샀다 파는 '노이즈 트레이더(Noise Trader)'만 있는 것이 아닙니다. 내일 애플이 부도난다는 사실을 미리 알고 있는 **'정보 거래자(Informed Trader)'**가 존재합니다. 마켓 메이커는 호가를 깔아두었기 때문에(수동적), 저 내부자가 100달러짜리 매수 호가에 애플 주식 100만 주를 폭탄처럼 던지고 도망갈 때 기계적으로 그 주식을 다 사줘야 합니다. 다음 날 주가는 50달러가 되고 마켓 메이커는 파산합니다. 이것이 시장 미시구조론의 뼈대인 **역선택(Adverse Selection)**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\mu$ (Informed) | Prob of facing insider | e.g., 10-20% | Higher $\mu \to$ Wider Spread | [데이터 부재] |
| $V$ (True Value) | The fundamental value | Hidden from MM | Known only to Insider | [데이터 부재] |
| Bid Price | Expectation given Sell | $E[V \mid \text{Sell Order}]$ | Always $< E[V]$ | [데이터 부재] |
| Ask Price | Expectation given Buy | $E[V \mid \text{Buy Order}]$ | Always $> E[V]$ | [데이터 부재] |
| Spread | Ask - Bid | Drives liquidity cost | Compensates for Adverse Sel.| [데이터 부재] |

## 3. Glosten-Milgrom 모형의 수학 (베이즈 추론)
1985년 Glosten과 Milgrom은 마켓 메이커가 이 '정보의 비대칭성' 속에서 살아남기 위해 어떻게 호가를 벌려야 하는지(Spread)를 베이즈 정리(Bayes' Theorem)로 증명했습니다.
- 시장에 누군가 '시장가 매수(Buy)' 주문을 쏘며 내 Ask 호가를 쳤습니다.
- 멍청한 MM은 "앗싸, 스프레드 먹었다"라고 좋아합니다. 하지만 깐깐한 Glosten-Milgrom MM은 의심합니다. **"저 놈이 나보다 정보가 많은 내부자라면? 내일 주가가 오를 걸 알고 내 물량을 털어간 거라면?"**
- 따라서 MM은 누군가 사겠다고 달려들면(Buy Order), 주식의 진짜 가치($V$)가 현재 예상치보다 더 높을 것이라고 베이지안 업데이트(Bayesian Update)를 돌립니다. $E[V \mid \text{Buy}]$.
- MM이 파산하지 않으려면, 자신이 부르는 매도 호가(Ask)를 정확히 이 사후 기댓값 $E[V \mid \text{Buy}]$ 수준까지 방어적으로 끌어올려야 합니다.
- 반대로 누군가 팔겠다고 달려들면(Sell Order), 주가가 쓰레기가 될 확률이 높으므로 매수 호가(Bid)를 $E[V \mid \text{Sell}]$ 수준으로 확 낮춥니다.

## 4. 유동성의 붕괴와 폭락장
이 모델은 왜 금융 위기나 중요 실적 발표 직전에 시장 호가창(LOB)이 텅텅 비고 스프레드가 미친 듯이 벌어지는지를 완벽히 설명합니다.
- 시장에 불확실성(정보의 크기)이 커지면, MM은 "지금 나에게 주문을 던지는 놈은 무조건 나보다 똑똑한 내부자($\mu \approx 1$)다"라고 극도의 공포에 질립니다.
- 역선택을 피하기 위해 MM은 Bid를 지하 10층으로 내리고 Ask를 지상 10층으로 올려버립니다. (스프레드 무한대 확장).
- 스프레드가 너무 벌어지니 아무도 거래를 할 수 없게 되고, 시장의 유동성(Liquidity)은 완전히 증발합니다. 

🧠 **AI의 사고방식:**
전통 경제학은 수요와 공급이 만나면 '하나의 균형 가격'이 생긴다고 가르치지만, Glosten-Milgrom 모형은 이를 박살 냅니다. 시장에는 결코 하나의 가격이 존재하지 않으며, 오직 '살 때의 가격(Ask)'과 '팔 때의 가격(Bid)'이라는 두 개의 가격만이 존재합니다. 그리고 이 두 가격 사이의 틈(Spread)은 거래소의 수수료도, 딜러의 얄팍한 마진도 아닙니다. 그것은 '나보다 똑똑한 누군가에게 합법적으로 사기를 당할 확률'에 대비하여 마켓 메이커가 치러야만 하는 순수한 **정보 비대칭의 보험료(Information Premium)**입니다.