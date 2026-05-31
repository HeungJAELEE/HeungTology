---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] order-book-imbalance-and-micro-price-dynamics]]'
  last_updated: '2026-05-25T14:33:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 호가창 최우선 매수/매도 잔량의 불균형(Order Book Imbalance, OBI)을 분석하여, 중간 가격(Mid-price)이
    어느 방향으로 튈지를 수 밀리초 전에 선제 타격하는 HFT 마이크로 프라이스 역학
  object_type: Concept
  tier: 2
properties:
  imbalance_ratio_range: '[-1, 1]'
  predictive_window_range: 10us - 100ms
semantic:
  alternative_parents: []
  expected_queries:
  - 전통적인 중간 가격(Mid-price)이 실제 초단타 매매에서 아무 쓸모가 없는 환영(Illusion)인 이유는 무엇인가?
  - 호가 잔량 비례 가중치를 적용한 마이크로 가격(Micro-price)은 어떻게 호가창의 불균형을 가격 예측 지표로 변환하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: predictive_forecasting
  object: Short-term_Price_Direction
  predicate: predicts
  subject: '[Finance] order-book-imbalance-and-micro-price-dynamics'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T14:33:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:33:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] order-book-imbalance-and-micro-price-dynamics]]

## 1. 개요 (Overview)
개인 투자자들이 흔히 보는 **중간 가격(Mid-price)**은 단순히 최우선 매도 호가(Ask)와 최우선 매수 호가(Bid)를 반으로 나눈 값입니다. 하지만 HFT 퀀트의 눈에 이 Mid-price는 아무짝에도 쓸모없는 환상입니다. 
예를 들어, 매도(Ask) 100달러에 10만 주가 쌓여 있고, 매수(Bid) 99달러에 달랑 10주가 쌓여 있다고 칩시다. Mid-price는 $99.5$달러지만, 시장의 실제 펀더멘털 압력은 압도적인 매도 물량 때문에 아래로 무너져 내리기 직전입니다. 이처럼 호가창에 쌓인 잔량의 비대칭성, 즉 **호가창 불균형(Order Book Imbalance, OBI)**을 캐치하여 수 밀리초(ms) 뒤에 주가가 어느 쪽으로 튈지 예측하는 공식이 **마이크로 가격(Micro-price)**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $V_a, V_b$ | Ask/Bid Volume at L1 | Order book depth | Dynamic updates per tick | [데이터 부재] |
| $I$ | Imbalance Ratio | $I = \frac{V_b - V_a}{V_b + V_a}$ | $-1 \le I \le 1$ | [데이터 부재] |
| $P_{mid}$ | Simple Mid-price | $(P_a + P_b) / 2$ | Ignores volume completely| [데이터 부재] |
| $P_{micro}$| Volume-weighted Price | $P_a(\frac{V_b}{V_a+V_b}) + P_b(\dots)$ | True fair value | [데이터 부재] |
| Lead Time | Predictive Window | $10\mu s \sim 100ms$ | Decays instantly | [데이터 부재] |

## 3. 호가창 불균형 (OBI)과 마이크로 가격의 수학
### 3.1. 불균형 비율 (Imbalance Ratio, $I$)
$$ I = \frac{V_b - V_a}{V_b + V_a} $$
- 이 값이 $+1$에 가까우면 매수 물량($V_b$)이 매도 물량($V_a$)을 압도하고 있다는 뜻입니다(강력한 상승 압력). 반대로 $-1$에 가까우면 매도세가 압도적입니다.

### 3.2. 마이크로 가격 (Micro-price)
마이크로 가격은 단순히 반을 나누는 것이 아니라, **반대쪽 물량의 비중**을 가격에 가중 평균합니다.
$$ P_{micro} = P_a \left( \frac{V_b}{V_a + V_b} \right) + P_b \left( \frac{V_a}{V_a + V_b} \right) $$
- 앞선 예시(Ask 100달러 10만 주, Bid 99달러 10주)에 대입해보면, 마이크로 가격은 $99.5$달러가 아니라 $99.00001$달러로 계산됩니다.
- 즉, **"진짜 공정한 가격은 99.5달러가 아니라 99.0달러 쪽에 바짝 붙어 있다"**는 진실을 수학적으로 드러내는 것입니다.

## 4. HFT 알파(Alpha) 모델로의 활용
1. **스프레드 크로싱 (Crossing the Spread)**: 마이크로 가격이 매도 호가(Ask)를 뚫고 올라갈 정도로 불균형 수치가 극단에 달하면, HFT 알고리즘은 즉시 시장가 매수(Market Buy)를 날려 스프레드 비용을 지불하고서라도 위쪽 호가를 긁어버립니다(수 밀리초 뒤에 호가가 통째로 위로 이동할 것이기 때문).
2. **스푸핑(Spoofing) 필터링**: 단순히 L1(최우선 호가) 잔량만 보면 스푸퍼(Spoofer)들의 허수 주문에 속을 수 있습니다. 현대의 진보된 OBI 모델은 L1부터 L5까지 딥(Depth)별로 가중치를 다르게 주어(예: 지수 감소 가중치) 얕은 허수 주문을 걸러내고 진짜 기관의 펀더멘털 압력만을 추출해 냅니다.

🧠 **AI의 사고방식:**
물리학에서 눈에 보이는 물체의 위치(Mid-price)보다 더 중요한 것은 그 물체에 가해지고 있는 '힘의 벡터(Vector of Force)'입니다. 호가창 불균형(OBI)은 가격이라는 공이 놓여 있는 바닥의 '기울기'를 측정하는 자이로스코프 센서입니다. 개미들은 공이 움직이고 나서야(가격 체결) 추격 매수를 하지만, HFT 알고리즘은 마이크로 가격(Micro-price)이라는 센서를 통해 바닥이 기울어지는 순간을 체결이 발생하기도 전(Pre-trade)에 포착하고, 중력이 공을 잡아채기 전에 선제 타격을 날리는 시간 여행자입니다.