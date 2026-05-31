---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-market-microstructure-glosten-milgrom-model]]'
  last_updated: '2026-05-25T14:07:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 시장 조성자(Market Maker)가 내부 정보자(Informed Trader)와의 정보 비대칭으로 인해 겪는 역선택(Adverse
    Selection) 손실을 매수/매도 스프레드에 반영하는 수학적 메커니즘
  object_type: Algorithm
  tier: 2
properties:
  ask_price_logic: E[V | Buy Order]
  bid_price_logic: E[V | Sell Order]
  informed_trader_proportion_mu: 0 <= mu < 1
  spread_definition: Ask - Bid
  true_asset_value_v: binary_outcome_v_h_or_v_l
  unconditional_expectation_ev: prior_belief
semantic:
  alternative_parents: []
  expected_queries:
  - 마켓 메이커는 왜 단순히 주문 처리 비용(Processing Cost)뿐만 아니라 정보 비대칭 위험까지 매수-매도 스프레드에 포함시켜야 하는가?
  - 베이즈 정리(Bayes' Theorem)를 이용해 마켓 메이커가 주문이 들어올 때마다 자산의 진짜 가치를 업데이트하는 방법은?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: theoretical_explanation
  object: Bid-Ask_Spread_Width
  predicate: explains
  subject: '[Finance] quantitative-market-microstructure-glosten-milgrom-model'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:07:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:07:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-market-microstructure-glosten-milgrom-model]]

## 1. 개요 (Overview)
금융 시장에서 마켓 메이커(Market Maker)는 언제나 매수 호가(Bid)와 매도 호가(Ask)를 동시에 제시하며 시장에 유동성을 공급합니다. 초창기 경제학은 이 '스프레드(Spread = Ask - Bid)'가 단순히 브로커의 인건비나 전산망 유지비(Order Processing Cost)일 것이라 순진하게 믿었습니다.
하지만 1985년 **글로스텐-밀그롬(Glosten-Milgrom) 모형**은 시장 미시구조(Market Microstructure)의 패러다임을 바꿉니다. 마켓 메이커의 가장 큰 적은 서버 유지비가 아니라, **'나보다 주식의 진짜 가치를 먼저 알고 있는 내부 정보자(Informed Trader)'**입니다. 마켓 메이커는 눈 감고 카드를 뽑는 딜러와 같아서, 자신에게 시장가로 긁고 가는 상대방이 아무것도 모르는 개미(Noise Trader)인지, 내일 아침 터질 악재를 미리 알고 있는 내부자인지 알 수 없습니다. 이를 방어하기 위해 마켓 메이커가 수학적으로 스프레드를 벌리는 과정을 모델링한 것이 이 모형입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\mu$ | Proportion of informed traders | $0 \le \mu < 1$ | High $\mu \implies$ Wider spread | [데이터 부재] |
| $V$ | True asset value (High/Low) | Unobservable | Binary outcome $V_H$ or $V_L$ | [데이터 부재] |
| $E[V]$ | Unconditional expectation | Prior belief | Base price before trade | [데이터 부재] |
| $Ask$ | $E[V \| \text{Buy Order}]$ | Always $> E[V]$ | Conditional expectation | [데이터 부재] |
| $Bid$ | $E[V \| \text{Sell Order}]$| Always $< E[V]$ | Conditional expectation | [데이터 부재] |

## 3. 역선택 (Adverse Selection)과 베이지안 업데이트
글로스텐-밀그롬 모형에서 거래는 순차적으로 일어납니다.

### 3.1. 거래 전 상태 (Prior)
마켓 메이커는 주식의 가치가 높은 상태($V_H$)일 확률을 $50\%$, 낮은 상태($V_L$)일 확률을 $50\%$로 생각하고, 적정 주가를 중간값으로 설정합니다. 시장에는 진짜 정보를 아는 자($\mu$)와 노이즈 트레이더($1-\mu$)가 섞여 있습니다.

### 3.2. 매수 주문 도착 시 (Ask Price 결정)
누군가 "내가 지금 당장 살 테니 가격을 대라(Buy Order)"고 외칩니다. 마켓 메이커는 생각합니다.
> "저놈이 노이즈 트레이더라면 살 확률은 $50\%$다. 하지만 저놈이 내부자라면, 회사가 대박이 났기($V_H$) 때문에 무조건 사는 것이다. 즉, 누군가 '산다'는 행위 자체가, 이 주식이 대박($V_H$)일 확률을 베이즈 정리에 의해 $50\%$보다 높게(Posterior) 끌어올린다."

따라서 마켓 메이커는 손해를 안 보기 위해 단순히 $E[V]$에 수수료를 얹는 것이 아니라, "저 사람이 살 때의 조건부 기댓값"인 $E[V | \text{Buy}]$로 매도 호가(Ask)를 높여 부릅니다.

### 3.3. 매도 주문 도착 시 (Bid Price 결정)
마찬가지로 누군가 "지금 당장 팔겠다(Sell Order)"고 하면, "저놈이 내부자라면 회사가 망하기 직전($V_L$)이라 던지는 것"이라고 가정해야 하므로 매수 호가(Bid)를 $E[V | \text{Sell}]$로 낮춰 부릅니다. 
결국 스프레드($Ask - Bid$)는 마켓 메이커가 취하는 폭리가 아니라, 내부 정보자에게 뜯길 눈먼 돈을 노이즈 트레이더들에게 십시일반 걷어 메우는 **'역선택 비용(Adverse Selection Cost)'**의 수학적 표현입니다.

## 4. 모형의 함의와 HFT 시대의 스프레드 폭발
- **스프레드의 폭**: 정보자 비율($\mu$)이 높을수록(예: 실적 발표 직전, 바이오 테마주), 마켓 메이커는 극도의 공포를 느끼고 스프레드를 태평양처럼 넓게 벌려 방어합니다.
- **정보의 가격 편입**: 딜러가 베이지안 업데이트를 반복함에 따라, 딜러가 제시하는 중간 가격(Mid-price)은 주식의 진짜 가치($V$)로 수렴하게 됩니다. 즉, '거래 행위' 자체가 정보가 가격에 반영되는 과정(Price Discovery)입니다.

🧠 **AI의 사고방식:**
글로스텐-밀그롬 모형은 포커 테이블에서 패를 보지 못한 딜러(마켓 메이커)가 어떻게 생존하는지를 보여주는 게임 이론입니다. 딜러는 패를 볼 수 없지만, 상대방이 '판돈을 크게 베팅했다(Buy)'는 행위 자체를 정보로 흡수하여 즉시 다음 카드의 배당률(Ask)을 조정합니다. 오늘날의 HFT 시대에 내부 정보자는 '회사 기밀을 아는 임원'이 아니라, 마켓 메이커의 서버보다 $100\mu s$ 먼저 틱 데이터를 파싱해낸 '초단타 암살자'들입니다. 마켓 메이커 알고리즘은 이들에게 베인 상처(역선택)의 출혈을 막기 위해 1초에도 수천 번씩 베이즈 정리를 계산하며 스프레드를 늘렸다 줄였다를 반복합니다.