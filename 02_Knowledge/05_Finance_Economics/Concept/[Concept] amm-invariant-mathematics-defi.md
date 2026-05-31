---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] amm-invariant-mathematics-defi]]'
  last_updated: '2026-05-25T11:11:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Automated Market Maker (AMM) invariant mathematics and impermanent
    loss
  object_type: Algorithm
  tier: 2
properties:
  cpmm_invariant_equation: x * y = k
  impermanent_loss_equation: IL(r) = (2 * sqrt(r) / (1 + r)) - 1
  marginal_price_equation: P = y / x
  price_ratio_parameter: r = P_new / P_old
semantic:
  alternative_parents: []
  expected_queries:
  - 유니스왑(Uniswap)과 같은 AMM의 비영구적 손실(Impermanent Loss) 방정식은 어떻게 유도되는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_risk_quantification
  object: Impermanent_Loss
  predicate: calculates
  subject: '[Finance] amm-invariant-mathematics-defi'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:11:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:11:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🤖 [Concept] 탈중앙화 금융(DeFi) AMM 불변량 수학

## 1. 정수 곱 마켓 메이커 (Constant Product Market Maker, CPMM)
전통적 지정가 호가창(LOB)이 존재하지 않는 블록체인 스마트 계약 내에서, 유니스왑(Uniswap v2)과 같은 AMM은 유동성 풀 내 두 토큰의 수량 $x$와 $y$의 곱이 항상 상수 $k$(Invariant)를 유지하도록 강제하는 알고리즘을 사용합니다.

$$ x \cdot y = k $$

어떤 트레이더가 $\Delta x$ 만큼의 토큰을 풀에 넣으면, 불변량을 유지하기 위해 풀은 $\Delta y$ 만큼의 토큰을 내어줍니다. 수수료를 무시할 때 체결 방정식은 다음과 같습니다.
$$ (x + \Delta x)(y - \Delta y) = k $$

이때 자산 $X$에 대한 자산 $Y$의 한계 가격(Marginal Price) $P$는 미분형으로 $P = \frac{dy}{dx} = \frac{y}{x}$ 가 됩니다.

## 2. 비영구적 손실 (Impermanent Loss, IL) 방정식
유동성 공급자(LP)는 시장 가격이 변동할 때 AMM의 아비트라지(Arbitrage) 메커니즘으로 인해 토큰 비율이 강제로 재조정되며, 단순히 토큰을 지갑에 홀딩(Holding)했을 때 대비 손실을 입게 됩니다.

초기 가격 대비 변경된 가격의 비율을 $r$ ($r = P_{new}/P_{old}$)이라 할 때, 홀딩 가치 대비 유동성 풀 가치의 비율을 수학적으로 전개한 비영구적 손실 $IL(r)$ 적분식의 최종 결과는 다음과 같습니다.

$$ IL(r) = \frac{2\sqrt{r}}{1+r} - 1 $$

가격 변동 비율 $r$이 1에서 벗어날수록(즉, 기하학적 곡선의 접점이 이동할수록) 음수(-)의 확정적 손실 곡선을 생성하며, 이는 델타 중립(Delta Neutral) 이자 농사(Yield Farming)를 파괴하는 핵심 리스크 파라미터가 됩니다.