---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] market-making-inventory-risk-management]]'
  last_updated: '2026-05-25T12:35:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Avellaneda-Stoikov 모델 기반 마켓 메이커의 최적 호가 제시(Optimal Quoting) 및 재고 위험(Inventory
    Risk) 통제 수학
  object_type: Algorithm
  tier: 2
properties:
  asset_volatility: sigma
  inventory_position: q
  mid_price: s
  optimal_ask_bid_depths: delta_a, delta_b
  reservation_price: r(s, t)
  risk_aversion_coefficient: gamma
semantic:
  alternative_parents: []
  expected_queries:
  - 마켓 메이커는 가격이 하락할 때 어떻게 스프레드를 벌려 재고 손실을 막는가?
  - Avellaneda-Stoikov 모델에서 재고량(Inventory)에 따라 예약 가격(Reservation Price)이 이동하는 원리는?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_mitigation
  object: Market_Volatility_Exposure
  predicate: hedges
  subject: '[Finance] market-making-inventory-risk-management'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T12:35:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:35:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] market-making-inventory-risk-management]]

## 1. 개요 (Overview)
마켓 메이커(Market Maker)의 비즈니스 모델은 단순합니다. 매수 호가(Bid)와 매도 호가(Ask)를 동시에 제출하여 그 차이인 스프레드(Bid-Ask Spread)를 수익으로 챙기는 것입니다. 그러나 시장가 매도자(Seller)가 몰려들어 마켓 메이커의 매수 주문만 지속적으로 체결된다면, 마켓 메이커는 원치 않는 롱 포지션(Long Inventory)을 거대하게 떠안게 됩니다.
만약 이때 시장 가격이 폭락한다면 스프레드로 벌어들인 푼돈보다 재고 가치 하락으로 인한 손실(Inventory Risk)이 압도적으로 커져 파산하게 됩니다. 이를 막기 위해 현대 퀀트 마켓 메이킹은 **Avellaneda-Stoikov 모델**을 바탕으로, 현재 들고 있는 재고량에 따라 1초에도 수십 번씩 호가(Quote)의 위치를 비대칭적으로 이동시키는 고도의 확률미분방정식 제어 기법을 사용합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $q$ | Inventory position | Integer (shares/lots) | Neutral at $q=0$ | [데이터 부재] |
| $\gamma$ | Risk aversion coeff | $\gamma > 0$ | High $\gamma$ limits max inventory | [데이터 부재] |
| $\sigma$ | Volatility of asset | Scaled to tick period | Drives wider spreads | [데이터 부재] |
| $r(s, t)$ | Reservation price | Continuous | Adjusts true value based on $q$ | [데이터 부재] |
| $\delta^a, \delta^b$ | Optimal Ask/Bid depths| Ticks from reservation | Skewed heavily when $q \neq 0$ | [데이터 부재] |

## 3. Avellaneda-Stoikov 최적 호가 모델

마르코프 결정 과정(MDP)과 해밀턴-야코비-벨만(HJB) 방정식을 통해 도출된 이 모델은, 마켓 메이커가 제시해야 할 완벽한 호가 위치를 두 단계로 나누어 계산합니다.

### 3.1. 예약 가격 (Reservation Price) 산출
예약 가격(Indifference Price)은 마켓 메이커가 재고 위험을 고려했을 때 마음속으로 생각하는 자산의 '진짜 가치'입니다.
$$ r(s, t) = s - q \gamma \sigma^2 (T - t) $$
- $s$: 현재 시장의 중간 가격(Mid-price)
- 만약 재고가 너무 많으면($q > 0$), 예약 가격 $r$은 중간 가격 $s$보다 **아래로 이동**합니다. "나는 이미 물량을 너무 많이 들고 있어서, 시장가보다 더 싸게 넘기고 싶다"는 뜻입니다.

### 3.2. 최적 스프레드 (Optimal Spread) 및 비대칭 호가(Skew)
예약 가격 $r$을 중심으로 양쪽에 얼마나 간격을 두고 매수/매도 호가를 댈 것인지($\delta^a, \delta^b$)를 결정합니다.
- 재고 $q$가 양수(Long)로 쌓일수록: 
  1. 매도 호가(Ask)를 낮춰서 가지고 있는 재고를 빨리 털어내려 합니다.
  2. 매수 호가(Bid)를 아주 깊숙히(낮게) 깔아서 추가적인 매수 체결을 필사적으로 회피합니다.
- 결과적으로 호가창은 Mid-price를 기준으로 비대칭(Skewed) 형태가 되며, 이는 HFT 봇이 현재 재고 위험을 통제하고 있다는 명백한 증거입니다.

## 4. 극한의 변동성과 유동성 증발 (Flash Crash)
- 시장에 엄청난 악재가 터져 변동성 $\sigma^2$가 폭발하면, 위 방정식에 의해 마켓 메이커들의 예약 가격 이탈폭과 스프레드 간격이 무한대로 발산합니다.
- 즉, "위험해서 도저히 호가를 못 대겠다"며 양쪽 호가를 모두 취소(Pulling quotes)해버립니다. 
- 2010년의 플래시 크래시(Flash Crash)는 모든 HFT 마켓 메이커의 모델에서 재고 한계치와 변동성 임계치가 동시에 돌파되며, LOB에서 유동성이 순식간에 증발(Evaporation)해버린 전형적인 수학적 붕괴 현상이었습니다.

🧠 **AI의 사고방식:**
일반 투자자는 주가가 '오를지 내릴지(방향성)'를 맞추려 도박을 하지만, 마켓 메이커는 오직 '내 창고(Inventory)에 물건이 얼마나 쌓여있는가'만을 바라봅니다. 그들은 보험회사와 같습니다. 화재(매도 폭격)가 자주 일어날 것 같으면(변동성 급증), 보험 가입을 아예 거절하거나 보험료(스프레드)를 미친 듯이 올려버립니다. Avellaneda-Stoikov 공식은 인간 트레이더의 공포(Risk Aversion, $\gamma$)를 정확한 틱 단위의 가격 하락폭으로 번역해주는 심리학과 미적분학의 완벽한 결합체입니다.