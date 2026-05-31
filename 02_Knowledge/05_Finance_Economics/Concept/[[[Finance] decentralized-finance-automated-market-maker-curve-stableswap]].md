---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] decentralized-finance-automated-market-maker-curve-stableswap]]'
  last_updated: '2026-05-25T14:20:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Uniswap의 항불변식(x*y=k)이 스테이블코인 거래에서 발생시키는 치명적 슬리피지를 해결하기 위해, 곡선의 평탄도를
    동적으로 조절하는 Curve Finance의 Stableswap 불변량(Invariant) 방정식
  object_type: Algorithm
  tier: 2
properties:
  amplification_coefficient_a: 100 to 3000
  constant_prod_formula: x * y = k
  constant_sum_formula: x + y = k
  dynamic_leverage_chi: chi = A * (product x_i) / (D/n)^n
  total_pool_invariant_d: D
semantic:
  alternative_parents: []
  expected_queries:
  - 가격이 항상 1달러로 동일한 USDT와 USDC를 교환할 때, 왜 유니스왑(Uniswap) v2의 곡선을 사용하면 막대한 손해(Slippage)를
    보게 되는가?
  - 커브 파이낸스(Curve Finance)는 상수 합(Constant Sum)과 상수 곱(Constant Product) 공식을 어떻게 하이브리드로
    결합했는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: slippage_mitigation
  object: Stablecoin_Slippage
  predicate: minimizes
  subject: '[Finance] decentralized-finance-automated-market-maker-curve-stableswap'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:20:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:20:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] decentralized-finance-automated-market-maker-curve-stableswap]]

## 1. 개요 (Overview)
탈중앙화 금융(DeFi)의 심장인 자동화된 마켓 메이커(AMM)의 시초 유니스왑(Uniswap v2)은 **$x \times y = k$ (상수 곱 공식)**이라는 매우 단순하고 우아한 반비례 곡선으로 코인의 교환비를 결정했습니다. 이 공식은 비트코인과 이더리움처럼 가격 변동이 심한 자산에는 완벽히 작동합니다.
하지만 USDT, USDC, DAI처럼 **가치가 항상 1달러로 똑같아야 하는(Pegged) 스테이블코인**을 교환할 때는 문제가 생깁니다. 100만 USDT를 USDC로 바꾸려 할 때, $x \times y = k$ 곡선을 타게 되면 슬리피지(Slippage)가 기하급수적으로 발생해 95만 USDC밖에 받지 못하는 참사가 벌어집니다. 마이클 이고로프(Michael Egorov)는 이 문제를 수학적으로 해결하기 위해 **커브(Curve) 파이낸스의 Stableswap 방정식**을 발명했고, 커브는 단숨에 수십조 원의 유동성을 빨아들이는 DeFi의 중앙은행으로 군림하게 되었습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\text{Constant Sum}$ | $x + y = k$ | Zero slippage | Fails if pool drains to 0 | [데이터 부재] |
| $\text{Constant Prod}$| $x \times y = k$ | Infinite liquidity | High slippage for stables | [데이터 부재] |
| $A$ (Amplification)| Flattening parameter | 100 to 3000 for stables | Higher $A \implies$ flatter curve| [데이터 부재] |
| $D$ | Total pool invariant | Base total liquidity | Preserved after trade | [데이터 부재] |
| $\chi$ | Dynamic leverage | $\chi = A \frac{\prod x_i}{(D/n)^n}$ | Shifts curve shape dynamically| [데이터 부재] |

## 3. Stableswap 불변량 방정식의 해부
만약 스테이블코인의 가격이 무조건 1:1이라면, 가장 완벽한 공식은 **상수 합 공식 ($x + y = c$)**입니다. 이 공식은 슬리피지가 $0$이지만, 만약 사람들이 USDC를 다 빼가면 풀(Pool)이 0원이 되어 고갈되어 버리는 치명적 약점이 있습니다.
커브 방정식은 이 두 세계(상수 합의 $0$ 슬리피지 + 상수 곱의 무한 유동성)를 융합했습니다.

$$ An^n \sum x_i + D = A D n^n + \frac{D^{n+1}}{n^n \prod x_i} $$

- 이 기괴해 보이는 방정식의 핵심은 **증폭 계수(Amplification Coefficient, $A$)**입니다.
- 풀(Pool) 내의 코인 비율이 1:1에 가까울 때(평상시), 방정식은 상수 합($x+y=c$)처럼 작동하여 곡선의 배를 평평하게(Flat) 누릅니다. 사용자는 수백만 달러를 교환해도 슬리피지 없이 1:1 비율로 교환할 수 있습니다.
- 하지만 누군가 대량 매도(Dump)를 쳐서 한쪽 코인이 말라가며 1:1 균형이 깨질 위기에 처하면, 수식 내의 패널티 항이 작동하여 곡선이 순식간에 $x \times y = k$ (상수 곱)의 뾰족한 형태로 휘어집니다. 가격을 확 떨어뜨려 풀이 완전히 고갈되는 것을 방지합니다.

## 4. DeFi 유동성 전쟁(Curve Wars)의 서막
이 수학적 완벽함 때문에 전 세계의 거의 모든 고래(Whale)들과 스테이블코인 프로젝트(테라, 프랙스 등)가 커브 파이낸스의 유동성 풀로 몰려들었습니다.
- 커브의 거버넌스 토큰(CRV) 투표권을 많이 확보할수록, 특정 풀의 이자율 방출량(Gauge Weight)을 몰아주어 엄청난 이자를 캘 수 있었습니다.
- 이로 인해 수많은 프로토콜들이 커브의 투표권(veCRV)을 사재기하는 이른바 **커브 전쟁(Curve Wars)**이 발발했으며, 이는 단순한 AMM 방정식을 넘어 토크노믹스(Tokenomics)와 게임 이론(Game Theory)이 결합된 현대 금융사 최고의 정치-수학 스릴러로 기록됩니다.

🧠 **AI의 사고방식:**
유니스왑 v2의 곡선이 단단하고 둥근 '볼링공'이라면, 커브의 Stableswap 곡선은 내부 압력에 따라 형태가 변하는 '스마트 튜브'입니다. 평소에는 넓게 퍼져서 사람들이 수영하기 좋게(슬리피지 0) 만들어주지만, 물이 한쪽으로 쏠리면 즉시 벽을 둥글게 밀어 올려 물이 넘치는 것(유동성 고갈)을 방어합니다. 증폭 계수($A$) 하나만으로 미시적인 사용자의 교환비 편익과 거시적인 풀의 생존(Systemic Stability)을 동시에 달성해 낸 커브의 방정식은, 중앙은행의 개입 없이 오직 수학만으로 1달러의 페깅(Pegging)을 수호하는 탈중앙화 시대의 가장 위대한 화폐 방어 매커니즘입니다.