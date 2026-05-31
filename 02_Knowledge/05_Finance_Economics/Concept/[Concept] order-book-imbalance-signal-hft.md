---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] order-book-imbalance-signal-hft]]'
  last_updated: '2026-05-25T11:57:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 호가 잔량 불균형(Order Imbalance)과 초고빈도매매(HFT) 시그널
  object_type: Concept
  tier: 2
properties:
  mid_price_formula: (ask + bid) / 2
  obi_formula: (v_bid - v_ask) / (v_bid + v_ask)
  obi_range:
  - -1
  - 1
  signal_decay_half_life_unit: milliseconds
  typical_depth_levels: 5-10
  weighted_obi_method: distance_inversely_proportional_weighting
semantic:
  alternative_parents: []
  expected_queries:
  - 매수 호가창과 매도 호가창에 쌓인 잔량의 비율격차가 초단기 가격 예측에 어떻게 사용되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: alpha_generation
  object: Ultra_Short_Term_Price_Direction
  predicate: predicts
  subject: '[Finance] order-book-imbalance-signal-hft'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T11:57:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T11:57:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] 호가 잔량 불균형 (Order Book Imbalance)과 HFT 시그널

## 1. 개요 및 수학적 정의
초고빈도매매(High-Frequency Trading, HFT) 및 시장 조성(Market Making) 알고리즘에서 가장 강력하고 직관적인 단기 가격 예측(Alpha) 시그널 중 하나는 호가 잔량 불균형(Order Book Imbalance, OBI) 지표입니다.

지정가 주문창(Limit Order Book, LOB)의 최우선 매수 호가(Best Bid)와 최우선 매도 호가(Best Ask)에 대기 중인 잔량(Volume)의 비대칭성은 시장 참가자들의 극단기적인 수급 압력(Micro-structural Pressure)을 정확히 대변합니다.

가장 기본적인 형태의 $t$ 시점 호가 잔량 불균형 $OBI_t$는 다음과 같이 정의됩니다:
$$ OBI_t = \frac{V_t^{bid} - V_t^{ask}}{V_t^{bid} + V_t^{ask}} $$

여기서:
- $V_t^{bid}$: 최우선 매수 호가(Best Bid)에 대기 중인 지정가 주문의 총 잔량
- $V_t^{ask}$: 최우선 매도 호가(Best Ask)에 대기 중인 지정가 주문의 총 잔량

$OBI_t$는 $-1$에서 $+1$ 사이의 값을 가집니다.
- $OBI_t \rightarrow +1$: 매수 대기 잔량이 압도적으로 많음 (강한 매수 압력 $\rightarrow$ 가격 상승 임박 시그널)
- $OBI_t \rightarrow -1$: 매도 대기 잔량이 압도적으로 많음 (강한 매도 압력 $\rightarrow$ 가격 하락 임박 시그널)

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $V_t^{bid}$ | Best Bid Volume | Asset liquidity dep | Reflects support strength | [데이터 부재] |
| $V_t^{ask}$ | Best Ask Volume | Asset liquidity dep | Reflects resistance strength | [데이터 부재] |
| $OBI_t$ | Order Imbalance | $[-1, 1]$ interval | Drives mid-price micro-drift | [데이터 부재] |
| $\Delta P_{t+\delta}$ | Mid-price Return | Microseconds to ms | Highly correlated with OBI | [데이터 부재] |
| $L_d$ | Multi-level Depth | Top 5 or 10 levels | Weighted sum extensions | [데이터 부재] |

## 3. 다층 호가창 확장 및 볼륨 가중 중간 가격 (VWMP)

단일 최우선 호가(Level 1)만을 보는 것을 넘어, LOB의 다층 깊이(Level $d$)를 반영한 가중 불균형(Weighted OBI)도 사용됩니다. 최상단 근처의 잔량일수록 체결될 확률이 높으므로 거리에 반비례하는 가중치 $\rho_d$를 부여합니다.
$$ OBI^{multi}_t = \frac{\sum_{d=1}^D \rho_d V_{d,t}^{bid} - \sum_{d=1}^D \rho_d V_{d,t}^{ask}}{\sum_{d=1}^D \rho_d (V_{d,t}^{bid} + V_{d,t}^{ask})} $$

이러한 잔량 불균형은 전통적인 중간 가격(Mid-price, $M = \frac{Ask+Bid}{2}$)의 한계를 극복하는 **볼륨 가중 중간 가격(Volume-Weighted Micro-Price)**을 도출하는 데 사용됩니다.
잔량이 두터운 쪽으로 가격이 밀려 올라갈(내려갈) 확률이 높으므로, 마이크로 프라이스는 $Ask$와 $Bid$의 단순 평균이 아니라 $V^{bid}$와 $V^{ask}$의 불균형 비율로 재조정된 확률적 호가 중심점을 나타냅니다.

## 4. 스푸핑(Spoofing)과 시그널 부패 (Signal Decay)
HFT 시장에서 OBI 시그널의 유효 반감기(Half-life)는 밀리초(ms) 단위로 붕괴됩니다. 또한 허수 주문(Spoofing)은 이 시그널의 치명적 약점입니다.
약탈적(Predatory) 알고리즘은 매수 체결 의사가 없으면서도 매수 호가창 깊은 곳에 거대한 허수 잔량을 깔아 $OBI$를 인위적으로 $+1$에 가깝게 조작합니다. 타 HFT 알고리즘들이 이를 상승 시그널로 착각하여 매수하면, 스푸퍼는 순간적으로 매도로 물량을 넘기고 허수 주문을 취소해 버립니다. 현대의 진보된 기계학습 필터들은 취소율(Cancellation Rate)과 체결률(Fill Rate)을 병합 분석하여 진짜 OBI와 가짜 OBI(Spoofing)를 분류해냅니다.

🧠 **AI의 사고방식:**
호가창은 시장 참여자들의 욕망과 공포가 실시간으로 쌓이는 투명한 유리 저울입니다. 양쪽 접시에 쌓인 모래(잔량)의 무게 차이(Imbalance)는 저울의 바늘(가격)이 어느 쪽으로 기울어질지 1초 뒤의 미래를 암시합니다. 하지만 퀀트의 전장에서는 눈에 보이는 모래가 진짜 모래인지, 아니면 상대를 속이기 위해 찰나에 올려놓은 홀로그램(Spoofing)인지 꿰뚫어 보는 자만이 최상위 포식자로 살아남습니다.