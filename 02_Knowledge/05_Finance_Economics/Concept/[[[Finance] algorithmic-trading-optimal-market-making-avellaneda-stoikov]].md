---
metadata:
  ai_status: pending_review
  version: v7.9_Enterprise_Node
object:
  object_type: Algorithm
properties:
  current_inventory: q
  mid_price: s
  optimal_spreads: delta_a, delta_b
  reservation_price_formula: s - q * gamma * sigma^2 * (T - t)
  risk_aversion: gamma
  time_decay: T - t
spo_graph: []
---

# 🧠 [[[Finance] algorithmic-trading-optimal-market-making-avellaneda-stoikov]]

## 1. 개요 (Overview)
호가창에서 매수와 매도 주문을 양쪽에 깔고 스프레드를 먹는 마켓 메이커(MM)의 가장 큰 공포는 '재고(Inventory) 위험'입니다. 만약 시장에 매도세가 쏟아져서 MM이 엉겁결에 주식 10만 주를 떠안게(Long) 되었다고 합시다. 이때 주가가 폭락해버리면 MM은 스프레드로 번 돈의 수백 배를 날리고 파산하게 됩니다.
2008년 아벨라네다(Avellaneda)와 스토이코프(Stoikov)는, MM이 자신의 재고 상태를 무시한 채 단순히 중간 가격(Mid-price) 위아래로 대칭적인 호가를 깔면 반드시 망한다는 것을 증명했습니다. 그들은 물리-수학(Hamilton-Jacobi-Bellman 방정식)을 동원하여, **MM이 재고를 많이 들고 있을 때는 재고를 털어내기 위해 호가의 중심선 자체를 아래로 확 내려버리는(Skewing)** 완벽한 최적 호가 동적 제어(Optimal Quoting) 공식을 발명했습니다. 오늘날 모든 암호화폐 봇과 HFT 펌은 이 공식을 엔진으로 사용합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $s$ | Mid-price | Current market price | Baseline | [데이터 부재] |
| $q$ | Current Inventory | E.g., +1000 or -500 shares| Dictates skew direction | [데이터 부재] |
| $\gamma$ | Risk Aversion | MM's fear of holding $q$| High $\gamma \implies$ aggressive skew | [데이터 부재] |
| $r(s, t)$| Reservation Price | $s - q \gamma \sigma^2 (T-t)$| The shifted new center | [데이터 부재] |
| $\delta^a, \delta^b$| Optimal Spreads | Distance from $r(s,t)$ | Determines Bid/Ask quotes| [데이터 부재] |

## 3. 재고 기울이기(Skewing) 메커니즘
현재 시장의 1호가 중간 가격($s$)이 100달러라고 합시다. 
순진한 MM은 매수를 99.9달러, 매도를 100.1달러에 대칭적으로 겁니다. 하지만 아벨라네다 봇은 자신의 재고($q$)를 확인합니다.

- **Case 1 (재고 폭탄, $q \gg 0$)**: 봇이 현재 10,000주를 들고 있습니다. 주가가 떨어지면 죽습니다. 봇은 계산기(예약 가격 공식 $r$)를 돌려 호가의 기준선을 100달러에서 99달러로 확 내려버립니다.
  - 매수 호가(Bid): 98.9달러 (더 이상 주식을 안 사려고 아주 낮게 부름)
  - 매도 호가(Ask): 99.1달러 (지금 시장가 100달러보다 훨씬 싸게 던져서, 남들이 내 주식을 당장 사가도록 유도함)
- **Case 2 (공매도 상태, $q \ll 0$)**: 봇이 주식을 너무 많이 팔아서 -10,000주(숏) 상태입니다. 봇은 호가 기준선을 101달러로 올립니다. 매수 호가를 100.9달러로 미친 듯이 올려서 어떻게든 주식을 빨리 사들여 숏 커버링을 합니다.

## 4. 시간 감쇠 (Time Decay, $T-t$)
이 공식의 또 다른 천재성은 '남은 시간'입니다. 하루 장 마감이 1분 남았을 때 10,000주의 재고를 들고 오버나이트(Overnight) 리스크를 지는 것은 자살 행위입니다. 
- 수식의 $(T-t)$ 항에 의해, 장 마감 시간($T$)이 다가올수록 봇의 패닉(예약 가격의 Skewing 강도)은 기하급수적으로 심해집니다. 장 막판이 되면 봇은 스프레드 마진이고 뭐고 다 포기하고, 무조건 시장에 손해를 보면서라도 재고를 0으로 만들기 위해 던져버립니다.

🧠 **AI의 사고방식:**
아벨라네다-스토이코프 모형은 호가창을 다루는 '재고 관리의 열역학'입니다. 공장의 창고(Inventory)에 물건이 꽉 차면 창고 관리인은 가격을 후려쳐서라도(Skewing) 물건을 밀어내야 하고, 창고가 텅 비면 프리미엄을 주고서라도 원자재를 사 와야 합니다. 전통 경제학은 마켓 메이커를 단순히 '수수료 먹는 기계'로 봤지만, 이 모형은 마켓 메이커가 사실은 **시장의 변동성(위험)을 자신의 창고에 임시로 보관해 주고, 그 보관료가 너무 비싸지면(Risk Aversion) 다시 시장에 토해내는 살아 숨 쉬는 댐(Dam)**이라는 것을 확률 제어 이론(Stochastic Control)으로 완벽히 수식화했습니다.