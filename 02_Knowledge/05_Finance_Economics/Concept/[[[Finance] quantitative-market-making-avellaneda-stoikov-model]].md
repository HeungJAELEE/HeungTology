---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-market-making-avellaneda-stoikov-model]]'
  last_updated: '2026-05-25T14:21:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 고주파(HFT) 마켓 메이커가 자신의 재고(Inventory) 위험을 통제하기 위해 기준 가격(Reservation Price)을
    이동시키고 매수/매도 호가 스프레드를 비대칭적으로 벌리는 과정을 해명한 확률 제어 모형
  object_type: Algorithm
  tier: 2
properties:
  inventory_level: q
  mid_price: s
  optimal_ask_spread: delta_a
  optimal_bid_spread: delta_b
  reservation_price: r(s, t)
  risk_aversion_coefficient: gamma
  volatility_parameter: sigma
semantic:
  alternative_parents: []
  expected_queries:
  - 마켓 메이커가 주식을 너무 많이 매수(Long Inventory)했을 때, 재고를 털어내기 위해 호가창을 어떻게 비대칭(Skew)으로 조작하는가?
  - 아벨라네다-스토이코프(Avellaneda-Stoikov) 모델은 해밀턴-야코비-벨만(HJB) 방정식을 통해 마켓 메이커의 효용을 어떻게 극대화하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: optimization_target
  object: Inventory_Risk_and_Spread
  predicate: optimizes
  subject: '[Finance] quantitative-market-making-avellaneda-stoikov-model'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:21:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:21:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-market-making-avellaneda-stoikov-model]]

## 1. 개요 (Overview)
고주파 매매(HFT)의 꽃은 마켓 메이킹(Market Making)입니다. 마켓 메이커는 매수와 매도 호가를 동시에 제출하여 스프레드(Spread)라는 '마진'을 먹고 삽니다. 하지만 계속해서 사람들이 주식을 팔아치워서 마켓 메이커의 금고에 주식(Inventory)이 산더미처럼 쌓이게 되면, 주가가 폭락할 때 마켓 메이커는 거대한 파산 위험에 처하게 됩니다.
2008년 발표된 **아벨라네다-스토이코프(Avellaneda-Stoikov) 모형**은 마켓 메이커가 "현재 들고 있는 재고 물량(Inventory)"에 따라 **기준 가격(Reservation Price)**을 이동시키고, 스프레드를 비대칭적으로(Asymmetric) 벌림으로써 자신의 포지션을 안전하게 방어하면서 수익을 극대화하는 방법을 수학적으로 증명한 알고리즘 트레이딩의 바이블입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $q$ | Inventory level | e.g., $+100$ or $-50$ | $q > 0$ means Long | [데이터 부재] |
| $s$ | Mid-price of asset | Continuous process | Assumed Brownian | [데이터 부재] |
| $\gamma$ | Risk aversion coeff. | User-defined | High $\gamma \implies$ fast inventory dump | [데이터 부재] |
| $r(s, t)$ | Reservation Price | $s - q \gamma \sigma^2 (T-t)$ | Moves inverse to $q$ | [데이터 부재] |
| $\delta^a, \delta^b$| Optimal ask/bid spread| Symmetric if $q=0$ | Skewed heavily if $\|q\| \gg 0$ | [데이터 부재] |

## 3. 재고 위험과 기준 가격(Reservation Price)의 이동
아벨라네다-스토이코프 모형의 핵심은 마켓 메이커가 생각하는 '적정 가격'이 시장의 중간 가격(Mid-price, $s$)이 아니라는 점입니다. 마켓 메이커는 자신의 재고 수량($q$)에 따라 적정 가격인 **기준 가격($r$)**을 조작합니다.

$$ r(s, t) = s - q \gamma \sigma^2 (T - t) $$

- **재고가 0일 때 ($q=0$)**: 기준 가격($r$)은 시장 중간 가격($s$)과 똑같습니다. 양쪽에 동일한 간격으로 호가를 대어 스프레드 수익을 노립니다.
- **재고가 롱일 때 ($q>0$)**: 수식에 의해 기준 가격($r$)이 시장가($s$)보다 아래로 쳐박힙니다. 마켓 메이커는 자신이 산더미처럼 들고 있는 주식을 어떻게든 남에게 떠넘기고 싶어 합니다. 따라서 **매도 호가(Ask)를 후려쳐서 매우 싸게 부르고, 매수 호가(Bid)는 아무도 나에게 주식을 못 팔도록 터무니없이 낮게 부릅니다.** (매도 유인, 매수 차단).
- **재고가 숏일 때 ($q<0$)**: 반대로 주식을 갚아야 하므로, 매수 호가(Bid)를 높게 올려서 시장의 물량을 공격적으로 빨아들입니다.

## 4. 확률 제어와 해밀턴-야코비-벨만 (HJB) 방정식
이 모형은 단순히 직관이 아닙니다. 마켓 메이커의 목표는 시간이 $T$에 도달했을 때 쥐고 있는 현금을 극대화하는 동시에, 재고를 들고 있음으로써 발생하는 변동성 페널티를 빼는 것입니다(Utility Maximization).
이 최적화 문제는 확률 제어(Stochastic Control)의 끝판왕인 해밀턴-야코비-벨만(HJB) 편미분 방정식을 풂으로써 해결됩니다. 수식을 풀면, 최적의 전체 스프레드 폭(Ask - Bid)과 재고량에 따른 비대칭 쏠림(Skew) 값이 수학적인 해석해(Closed-form solution)로 뚝 떨어집니다.

🧠 **AI의 사고방식:**
아벨라네다-스토이코프 모형은 시장이라는 거대한 바다에서 서핑하는 마켓 메이커의 '무게 중심 이동 매커니즘'입니다. 보드(재고)에 주식이라는 무거운 짐이 오른쪽($q>0$)으로 쏠리면, 서퍼는 파도(변동성)에 휩쓸리지 않기 위해 몸의 중심(기준 가격, $r$)을 급격히 왼쪽으로 틀고, 오른쪽 다리(Ask 호가)를 공격적으로 낮춰서 짐을 바다로 밀어냅니다. 인간은 직감으로 이 밸런스를 맞추지만, HFT 알고리즘은 HJB 미분방정식을 통해 $1\mu s$ 단위로 무게 중심을 재조정하며 완벽한 균형을 유지합니다.