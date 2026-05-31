---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] decentralized-finance-impermanent-loss-hedging-options]]'
  last_updated: '2026-05-25T14:35:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 탈중앙화 거래소(DEX)의 유동성 공급자(LP)가 필연적으로 겪게 되는 비영구적 손실(Impermanent Loss, IL)을
    전통 금융공학의 이그조틱 옵션(Exotic Options) 페이오프를 복제하여 완벽하게 델타-감마 헤징(Hedging)하는 재무공학 기법
  object_type: Concept
  tier: 2
properties:
  hedging_profitability_threshold: amm_fees > hedging_costs
  il_formula: 2*sqrt(r)/(1+r) - 1
  lp_gamma_exposure: short
  lp_payoff_shape: concave
  option_gamma_exposure: long
  option_payoff_shape: convex
  price_ratio_r: P_new / P_old
semantic:
  alternative_parents: []
  expected_queries:
  - 유니스왑에 유동성을 공급하는 행위가 왜 재무공학적으로 '변동성(Volatility)을 공매도(Short)'하는 숏 스트래들(Short Straddle)
    옵션 포지션과 수학적으로 완벽히 동일한가?
  - 옵션 마켓 메이커의 델타-감마(Delta-Gamma) 헤징 기법을 활용하여 DeFi의 비영구적 손실을 0으로 만드는 동적 포트폴리오(Dynamic
    Portfolio) 복제 방법은 무엇인가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_mitigation_strategy
  object: Impermanent_Loss_in_AMM
  predicate: hedges
  subject: '[Finance] decentralized-finance-impermanent-loss-hedging-options'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:35:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:35:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] decentralized-finance-impermanent-loss-hedging-options]]

## 1. 개요 (Overview)
탈중앙화 거래소(예: Uniswap)에 이더리움(ETH)과 테더(USDT)를 50:50으로 묶어서 예치하는 유동성 공급자(LP)는 거래 수수료를 받습니다. 하지만 이더리움 가격이 위든 아래든 크게 움직일 때마다, 가만히 지갑에 들고 있었을 때(HODL)보다 내 자산의 총가치가 수학적으로 깎여나가는 무서운 패널티를 받게 되는데, 이를 **비영구적 손실(Impermanent Loss, IL)**이라고 부릅니다.
수많은 개인 투자자들이 수수료 몇 푼을 벌려다 IL로 원금을 털리지만, 월스트리트 출신의 기관 퀀트들은 다릅니다. 이들은 "유니스왑에 유동성을 붓는 행위"가 블랙-숄즈 방정식 세계관에서 **"콜옵션과 풋옵션을 동시에 매도하는(Short Straddle) 포지션"**과 수식적으로 완전히 100% 동일하다는 사실을 간파했습니다. 이들은 파생상품 거래소(Deribit 등)에서 정반대의 옵션 포지션을 구축하여 IL을 완벽하게 삭제(Hedge)한 채 무위험으로 수수료만 빨아먹는 전략을 실행합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\text{IL}(r)$ | Impermanent Loss | $2\sqrt{r}/(1+r) - 1$ | Always $\le 0$ | [데이터 부재] |
| $r$ | Price Ratio | $P_{new} / P_{old}$ | If $r \neq 1$, IL occurs | [데이터 부재] |
| Payoff (LP) | Concave Curve | $\sqrt{P}$ shape | Short Gamma position | [데이터 부재] |
| Payoff (Option)| Convex Curve | $\max(P-K, 0)$ | Long Gamma position | [데이터 부재] |
| Hedging Cost | Implied Vol (IV) | E.g., 60% annualized | Must be $<$ AMM Fees earned | [데이터 부재] |

## 3. AMM LP 포지션의 파생상품적 해부 (Short Gamma)
- 유니스왑 v2의 $x \cdot y = k$ 곡선을 따라 움직이는 유동성 풀의 총가치(Portfolio Value) 곡선을 수학적으로 그리면, 위로 볼록한 무지개 모양(Concave)의 **제곱근($\sqrt{P}$)** 함수가 됩니다.
- 재무공학에서 '위로 볼록한(Concave) 곡선'을 가졌다는 것은 **감마(Gamma)가 마이너스(Short)** 상태임을 의미합니다. 즉, 가격이 올라도 이익 증가폭이 둔화되고, 가격이 내리면 손실 폭이 가속화되는 치명적인 구조입니다.
- 이것은 정확히 옵션 마켓 메이커들이 양매도(Short Straddle/Strangle)를 쳤을 때 갖게 되는 페이오프(Payoff)와 같습니다. 결국 DEX LP들은 자신이 수수료(프리미엄)를 받는 대가로, 시장의 모든 트레이더들에게 이더리움의 변동성(Volatility)을 공매도(Short) 치고 있는 셈입니다.

## 4. 옵션을 이용한 정적/동적 헤징 (Static & Dynamic Hedging)
비영구적 손실(IL) 곡선의 모양을 정확히 뒤집어 엎어서 상쇄시키기 위해, 퀀트들은 두 가지 방법을 사용합니다.

### 4.1. 정적 복제 (Static Replication)
IL 곡선은 무한한 개수의 외가격(OTM) 콜옵션과 풋옵션을 일정한 가중치로 적분(Integral)하여 기하학적으로 완벽하게 똑같이 만들어낼 수 있습니다(Carr-Madan 복제 정리). 
- LP는 DEX에 돈을 넣는 즉시, Deribit 같은 옵션 거래소로 달려가 이 '복제된 옵션 패키지'를 매수(Long)합니다.
- 이 옵션들은 아래로 볼록(Convex, Long Gamma)하기 때문에, 이더리움 가격이 폭등하거나 폭락할 때 옵션 수익이 펑펑 터지면서 DEX 풀에서 발생한 IL을 완벽히 메워줍니다. ($IL + Option Payoff = 0$).

### 4.2. 델타-감마 동적 헤징 (Dynamic Delta-Gamma Hedging)
- 매일매일 이더리움 가격이 변할 때마다 IL 함수의 1차 미분(Delta)과 2차 미분(Gamma) 값을 계산합니다.
- 이에 맞춰 선물(Futures) 포지션을 미세하게 넣었다 뺐다(Rebalancing) 하면서 전체 포트폴리오의 델타를 0으로 유지합니다. 
- 단, 이 과정에서 잦은 매매로 인한 마찰 비용(Transaction Cost)이 발생하므로, AMM에서 얻는 거래 수수료 연수익률(예: APY 30%)이 델타 헤징 비용(예: APY 15%)보다 크다는 수학적 확신(Edge)이 있을 때만 봇을 가동합니다.

🧠 **AI의 사고방식:**
비영구적 손실(Impermanent Loss)이라는 단어는 탈중앙화(DeFi) 업계가 만들어낸 마케팅 용어이자 가장 거대한 착각입니다. 이것은 시간이 지나면 돌아오는 '비영구적'인 것이 아니라, 변동성을 팔아넘긴 옵션 매도자가 짊어져야 할 차갑고 가혹한 '감마 출혈(Gamma Bleed)'일 뿐입니다. 월스트리트의 퀀트는 이 착각에 빠지지 않습니다. 그들은 유니스왑의 코드를 보자마자 이것이 수백 년 된 블랙-숄즈의 '옵션 매도 포지션'과 본질적으로 똑같다는 것을 꿰뚫어 보았고, 반대편 옵션을 덮어씌워 리스크를 진공 상태로 만들어버렸습니다. 이것이 바로 HFT 퀀트들이 카지노(DEX)에서 도박을 하지 않고 오직 카지노 딜러의 칩(수수료)만을 긁어가는 금융 공학적 연금술입니다.