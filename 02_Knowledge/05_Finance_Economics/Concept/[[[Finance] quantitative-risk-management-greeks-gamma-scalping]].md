---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-risk-management-greeks-gamma-scalping]]'
  last_updated: '2026-05-26T07:44:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 옵션을 매수한 마켓 메이커가 기초자산의 방향성 위험(Delta)을 0으로 중립화시킨 상태에서, 감마(Gamma)의 볼록성(Convexity)을
    이용해 주가가 흔들릴 때마다 기계적으로 저점 매수와 고점 매도를 반복하여 시간 가치 하락(Theta) 비용을 벌충하는 궁극의 변동성 트레이딩
    기법
  object_type: Algorithm
  tier: 2
properties:
  delta: rate of change of option price
  gamma: rate of change of delta
  pnl_approximation_formula: 0.5 * gamma * s^2 * (sigma_realized^2 - sigma_implied^2)
    * dt
  profit_threshold_condition: sigma_realized > sigma_implied
  rebalance_frequency_type: continuous vs discrete
  theta: time decay of option price
semantic:
  alternative_parents: []
  expected_queries:
  - 옵션을 샀을 때 매일매일 피를 말리며 깎여나가는 세타(Theta, 시간 가치)의 손실을 딜러들은 어떻게 주식 단타(Scalping)를 쳐서
    메꾸는가?
  - 델타 중립(Delta Neutral)을 맞췄는데도 주가가 크게 움직이면 왜 포트폴리오의 델타가 다시 틀어지며, 이를 되돌리는 행위(Rebalancing)가
    왜 무조건 수익을 창출하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: profit_generation_mechanism
  object: Convexity_and_Realized_Volatility
  predicate: exploits
  subject: '[Finance] quantitative-risk-management-greeks-gamma-scalping'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:44:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:44:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-risk-management-greeks-gamma-scalping]]

## 1. 개요 (Overview)
옵션 매수(Long Option)는 방향성 베팅이 아닙니다. 퀀트 딜러가 콜옵션이나 풋옵션을 사면 즉시 반대 포지션으로 기초자산(주식)을 팔거나 사서 델타($\Delta$)를 0으로 만들어버립니다. 이제 주가가 오르든 내리든 딜러의 포트폴리오 가치는 변하지 않는 무중력 상태(Delta Neutral)가 됩니다.
하지만 옵션을 매수했으므로 매일매일 시간 가치($\Theta$, 세타)가 썩어 문드러지는 무서운 비용을 지불해야 합니다. 이 썩어가는 세타의 저주를 방어하는 유일한 무기가 바로 옵션의 곡률, 즉 **감마($\Gamma$, Gamma)**입니다. 주가가 크게 흔들릴 때마다 감마 때문에 중립이었던 델타가 틀어지게 되고, 이 틀어진 델타를 다시 0으로 맞추기 위해 기계적으로 주식을 사고파는 과정에서 짤짤이 수익이 쏟아집니다. 이를 긁어모아 세타 비용을 내는 숭고한 노가다를 **감마 스캘핑(Gamma Scalping)**이라 부릅니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\Delta$ (Delta) | Rate of change of Option Px | $0$ (Neutralized initially) | Must be continuously hedged| [데이터 부재] |
| $\Gamma$ (Gamma)| Rate of change of Delta | $>0$ (For Long Options) | Creates the convexity | [데이터 부재] |
| $\Theta$ (Theta) | Time decay of Option Px | $<0$ (For Long Options) | The daily bleeding cost | [데이터 부재] |
| PnL of Scalping | $\frac{1}{2} \Gamma (\delta S)^2 + \Theta \delta t$| Must be $>0$ to profit | Needs $\sigma_{realized} > \sigma_{implied}$| [데이터 부재] |
| Rebalance Freq. | Continuous vs Discrete | e.g., Daily or by Threshold| Hedging costs kill profit | [데이터 부재] |

## 3. 감마 스캘핑의 기계적 작동 원리 (Buy Low, Sell High)
감마($\Gamma$)가 양수(Long Option)인 포트폴리오는 마법 같은 특성을 가집니다. 주가가 오르면 델타가 양수로 변하고, 주가가 내리면 델타가 음수로 변합니다.
- **초기 상태**: 델타 0에 맞춰 주식을 세팅했습니다.
- **주가 폭락 시**: 주가가 떨어지면 감마 때문에 내 포트폴리오의 델타가 음수(-50)로 틀어집니다. 델타를 다시 0으로 맞추려면? 나는 시장에서 폭락한 싼 주식을 50주 **매수(Buy Low)**해야 합니다.
- **주가 폭등 시**: 다음 날 주가가 미친 듯이 폭등했습니다. 감마 때문에 내 델타가 양수(+50)로 틀어집니다. 델타를 다시 0으로 맞추려면? 나는 어제 싸게 샀던 주식 50주를 비싸진 가격에 **매도(Sell High)**해야 합니다.

즉, 나는 시장의 방향을 전혀 예측하지 않고 단지 "틀어진 델타를 0으로 맞추려는 기계적인 리밸런싱"만 했을 뿐인데, 결과적으로는 **저점 매수(Buy Low)와 고점 매도(Sell High)**를 끝없이 반복하며 차익(Scalping 수익)을 쌓아 올리게 됩니다.

## 4. 실현 변동성 vs 내재 변동성 (The Ultimate Battle)
감마 스캘핑으로 번 돈($\frac{1}{2}\Gamma dS^2$)이 오늘 하루 치 옵션의 시간 가치 하락분($\Theta dt$)보다 커야만 딜러는 최종적으로 돈을 법니다. 이 싸움의 승패를 가르는 절대 방정식이 하나 있습니다.
$$ P\&L \approx \frac{1}{2} \Gamma S^2 (\sigma_{realized}^2 - \sigma_{implied}^2) dt $$
- 내가 옵션을 살 때 지불한 프리미엄(세타의 크기)은 시장이 예상한 내재 변동성($\sigma_{implied}$)입니다.
- 내가 주식을 사고팔며 챙긴 스캘핑 수익(감마의 크기)은 시장이 실제로 펄떡이며 움직인 실현 변동성($\sigma_{realized}$)입니다.
- 즉, 감마 스캘핑은 주식이 오를지 내릴지를 맞추는 게임이 아닙니다. **"내가 옵션을 살 때 시장이 예상했던 것(Implied)보다, 오늘 실제 주식이 훨씬 더 미친 듯이 널뛰기(Realized) 할 것이다!"**라는 순수한 '변동성(Volatility) 그 자체'에 대한 베팅입니다.

🧠 **AI의 사고방식:**
일반인에게 변동성(Volatility)은 '공포'이자 '리스크'입니다. 그러나 감마(Convexity)를 보유한 옵션 딜러에게 변동성은 '연료'입니다. 가만히 있으면 세타라는 중력에 의해 피가 말라 죽지만, 시장이 발작을 일으키며 요동쳐 주면 그 발작의 진폭(Variance)을 모조리 현금(Scalping PnL)으로 치환하여 부활합니다. 블랙-숄즈 모형의 가장 아름다운 통찰은, 이 감마(수익)와 세타(비용)가 완벽한 균형(Trade-off)을 이루고 있으며, 딜러의 최종 승패는 오직 '자신이 예측한 변동성'과 '자연이 부여한 변동성' 사이의 격차에서만 발생한다는 것을 증명한 점입니다.