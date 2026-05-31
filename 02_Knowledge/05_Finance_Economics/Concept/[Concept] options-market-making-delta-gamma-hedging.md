---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] options-market-making-delta-gamma-hedging]]'
  last_updated: '2026-05-25T12:38:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 옵션 마켓 메이커의 차원 높은 리스크 통제를 위한 실시간 델타-감마 중립(Delta-Gamma Neutral) 동적 헤징
    파이프라인
  object_type: Algorithm
  tier: 2
properties:
  delta_sensitivity_target: 0
  gamma_sensitivity_target: 0
  mathematical_foundation: taylor_expansion
  primary_objective: directional_risk_neutralization
  rebalancing_frequency_type: continuous_or_threshold_based
  tca_cost_unit: basis_points
semantic:
  alternative_parents: []
  expected_queries:
  - 옵션 마켓 메이커가 기초자산 가격 변동에 베팅하지 않으면서 수익을 내는 원리는?
  - 단순한 델타 헤징(Delta Hedging)의 한계를 극복하기 위해 감마(Gamma)를 포트폴리오 차원에서 어떻게 중립화하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_mitigation
  object: Non-linear_Derivatives_Risk
  predicate: hedges
  subject: '[Finance] options-market-making-delta-gamma-hedging'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T12:38:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:38:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] options-market-making-delta-gamma-hedging]]

## 1. 개요 (Overview)
현물 주식의 마켓 메이킹이 '하나의 차원'에서 재고를 통제하는 게임이라면, 옵션 마켓 메이킹은 수천 개의 행사가(Strike Price)와 만기일(Expiration)이 뒤섞인 **'다차원 표면(Surface)' 위에서 포지션을 춤추게 하는 예술**입니다.
옵션 마켓 메이커(OMM)는 시장의 방향(오를지 내릴지)에 전혀 관심이 없습니다. 그들은 오직 무수히 많은 옵션 계약의 매수/매도 스프레드만을 먹으려 합니다. 따라서 옵션을 매도하거나 매수하여 포지션이 쌓이면, 기초자산(예: S&P 500 지수)이 움직일 때 포트폴리오의 가치가 흔들리는 것(Directional Risk)을 완벽히 차단해야 합니다. 이를 수학적으로 달성하는 기법이 바로 실시간 **델타-감마 중립(Delta-Gamma Neutral) 헤징**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\text{Delta } (\Delta)$ | Sensitivity to underlying | $\sum \Delta_i \approx 0$ | Must hedge with underlying asset| [데이터 부재] |
| $\text{Gamma } (\Gamma)$| Rate of change of Delta | $\sum \Gamma_i \approx 0$ | Hedged using other options | [데이터 부재] |
| $\text{Vega } (\mathcal{V})$ | Sensitivity to Volatility | Surface matched | Extreme risk during crash | [데이터 부재] |
| $\text{Rebalancing Freq}$| Hedging interval | Continuous / Threshold-based | Trades off risk vs TCA | [데이터 부재] |
| $\text{TCA Cost}$ | Friction of hedging | Basis points | Eats into market making edge | [데이터 부재] |

## 3. 그릭스(Greeks) 중립화 메커니즘

### 3.1. 1차 방어선: 델타 중립 (Delta Neutral)
- 마켓 메이커가 콜옵션(Call) 100계약을 매도하여 전체 포트폴리오의 델타가 $-50$이 되었다고 가정합니다. 지수가 1포인트 상승하면 포트폴리오는 50달러의 손실을 입습니다.
- 이를 막기 위해 알고리즘은 즉시 현물이나 선물 시장에서 기초자산을 50단위 매수(Long)하여 총 델타를 $0$으로 맞춥니다. 이제 시장이 조금 올라도 포트폴리오 가치는 변하지 않습니다.

### 3.2. 2차 방어선: 감마 중립 (Gamma Neutral)
- 델타 중립은 '아주 미세한 가격 변화'에만 통합니다. 옵션 가격 곡선은 볼록(Convex)하기 때문에, 기초자산이 크게 움직이면 기존에 맞춰둔 델타 값이 틀어져 버리는 **감마 리스크(Gamma Risk)**가 발생합니다.
- 현물이나 선물의 감마는 $0$이므로, 감마 리스크는 오직 **'다른 옵션'을 매매해야만 상쇄**할 수 있습니다. 
- 퀀트 엔진은 실시간으로 수천 개의 옵션 포트폴리오 감마 합계를 계산하고, 가장 유동성이 풍부한 특정 행사가의 옵션을 롱/숏하여 포트폴리오 전체의 감마를 $0$ 근처로 묶어둡니다.

## 4. 동적 헤징(Dynamic Hedging)과 핀 리스크(Pin Risk)

- 델타와 감마를 0으로 맞추는 수학적 연산(Taylor Expansion 기반)은 지속적으로 변화합니다. 지수가 움직일 때마다 알고리즘은 델타를 0으로 유지하기 위해 기초자산을 고가 매수/저가 매도(Buy high, Sell low) 해야 하며, 이 과정에서 발생하는 필연적인 손실은 옵션의 '세타(Theta, 시간가치 소멸)'로 벌어들이는 수익으로 상쇄합니다.
- **핀 리스크 (Pin Risk)**: 만기일(Expiration Day)이 다가올수록 ATM(At-The-Money) 근처 옵션의 감마는 무한대로 폭발합니다. 이때 마켓 메이커 시스템은 델타를 맞추기 위해 초당 수천 번씩 기초자산을 샀다 팔았다를 반복하는 '감마 트랩(Gamma Trap)'에 빠질 수 있으며, 이를 피하기 위해 알고리즘은 만기 직전 ATM 옵션의 델타 헤징 빈도를 의도적으로 줄이거나 포지션을 사전에 롤오버(Roll-over)합니다.

🧠 **AI의 사고방식:**
옵션 마켓 메이킹은 블랙-숄즈 편미분방정식(PDE)을 공중에 띄워놓고 저글링을 하는 것과 같습니다. 시장이라는 중력(기초자산 이동)이 공을 잡아당길 때마다, 델타(1차 미분)와 감마(2차 미분)를 실시간으로 0으로 돌려놓는 카운터 펀치(헤지 주문)를 정확한 속도와 각도로 날려야 합니다. 이 헤징을 너무 자주 하면 거래소 수수료(TCA) 때문에 깡통을 차고, 너무 뜸하게 하면 방향성 리스크에 노출되어 파산합니다. 퀀트의 예술은 수학적 완벽함과 물리적 마찰(수수료) 사이의 절묘한 균형점을 찾는 '최적 제어 이론(Optimal Control Theory)'의 극치입니다.