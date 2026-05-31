---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] automated-market-maker-uniswap-v3-concentrated-liquidity]]'
  last_updated: '2026-05-25T14:24:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Uniswap v2의 자본 비효율성을 극복하기 위해, 사용자가 특정 가격 구간(Tick)에만 유동성을 집중적으로 공급(Concentrated
    Liquidity)하도록 설계한 탈중앙화 거래소의 차세대 수학적 구조
  object_type: Algorithm
  tier: 2
properties:
  current_price: P
  liquidity_depth: L
  lp_token_standard: ERC-721
  max_capital_efficiency_increase_multiplier: 4000
  price_range_bounds: '[p_a, p_b]'
  virtual_liquidity_formula: (x + L/sqrt(p_b)) * (y + L*sqrt(p_a)) = L^2
semantic:
  alternative_parents: []
  expected_queries:
  - "유니스왑 v2의 $x \times y = k$ 공식이 왜 자본의 99%를 아무도 거래하지 않는 가격대(0원 ~ 무한대)에 낭비하게 만드는가?"
  - 집중화된 유동성(Concentrated Liquidity)은 전통 거래소의 호가창(Limit Order Book)과 AMM을 어떻게 결합한
    것인가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: optimization_target
  object: Capital_Efficiency_in_DeFi
  predicate: maximizes
  subject: '[Finance] automated-market-maker-uniswap-v3-concentrated-liquidity'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:24:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:24:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] automated-market-maker-uniswap-v3-concentrated-liquidity]]

## 1. 개요 (Overview)
초창기 DeFi를 폭발시킨 유니스왑(Uniswap v2)은 두 자산의 교환비를 $x \times y = k$ 곡선을 따라 결정했습니다. 이 곡선의 가장 큰 특징은 **가격이 $0$원부터 무한대($\infty$)까지 모든 구간을 커버**한다는 점입니다. 
언뜻 들으면 좋아 보이지만, USDC/USDT 같은 스테이블코인 쌍은 가격이 항상 $0.99 \sim 1.01$ 사이에서만 움직입니다. 그런데 유니스왑 v2에 유동성을 공급하면, 내 자본의 99%가 "1 USDC가 1,000,000 USDT가 될 때"를 대비해 곡선 저 끝에 묶여 있게 됩니다. 수천억 원이 예치되어 있어도 정작 $1.0$ 근처에서 거래에 쓰이는 돈은 1%도 안 되는 극악의 **자본 비효율성(Capital Inefficiency)**이 발생한 것입니다.
이를 타파하기 위해 2021년 출시된 **유니스왑 v3**는 유동성 공급자(LP)가 "나는 딱 $0.99$ 달러에서 $1.01$ 달러 구간(Tick)에만 내 돈을 넣겠다"고 지정할 수 있는 **집중화된 유동성(Concentrated Liquidity)** 개념을 수학적으로 구현했습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $[p_a, p_b]$ | Price range | User-defined ticks | Outside range: 0 fees earned | [데이터 부재] |
| $L$ | Liquidity | $\sqrt{x \cdot y}$ | Constant within a tick | [데이터 부재] |
| $P$ | Current price | $\sqrt{y/x}$ | Moves as trades occur | [데이터 부재] |
| Virtual Liquidity| Translated $k$ curve | $L^2 = (x + \dots)(y + \dots)$ | Shifts $x,y$ axes | [데이터 부재] |
| NFT (ERC-721)| LP Token Format | Non-fungible | Each LP has unique range | [데이터 부재] |

## 3. 유니스왑 v3의 가상 유동성 (Virtual Liquidity) 수학
유니스왑 v3의 핵심 아이디어는 기존의 $x \times y = k$ 곡선을 $x$축과 $y$축 방향으로 잡아당겨, 내가 설정한 가격 구간 $[p_a, p_b]$ 바깥에 배정될 잉여 유동성을 잘라내고, 오직 해당 구간 안에서만 곡선이 작동하도록 **원점(Origin)을 이동시키는 기하학적 평행 이동**입니다.

$$ (x + \frac{L}{\sqrt{p_b}}) (y + L\sqrt{p_a}) = L^2 $$

- 여기서 $L$은 유동성의 깊이(Depth)입니다.
- 평행 이동된 이 수식 덕분에, v2에서 100만 달러를 넣어야 만들 수 있었던 호가창의 두께를 v3에서는 단 2,000달러만 내가 지정한 구간에 집중해서 넣으면 똑같은 두께(슬리피지 방어력)를 만들어 낼 수 있습니다. (자본 효율성 최대 4,000배 증가).
- **부작용 (Impermanent Loss 폭발)**: 범위가 좁을수록 수수료를 엄청나게 많이 먹지만, 가격이 그 범위를 살짝이라도 벗어나는 순간 내 자산이 전부 값싼 코인으로 강제 환전(100% 매도)되어 버리는 엄청난 비영구적 손실(IL) 위험을 짊어져야 합니다.

## 4. AMM과 호가창(Limit Order Book)의 수렴
유니스왑 v3의 '틱(Tick)' 시스템은 사실상 전통 금융 시장의 **호가창(Limit Order Book)을 온체인(On-chain)으로 복원한 것**입니다. 
- LP가 현재 시장가보다 높은 가격 범위 $[1.1, 1.2]$에 유동성을 집중해 놓으면, 가격이 올라가면서 그 범위에 도달할 때 자산이 점진적으로 분할 매도됩니다. 이는 전통 거래소에서 미리 깔아 놓은 '지정가 매도 주문(Limit Sell Order)'과 수학적으로 완벽히 동일합니다.
- v3의 등장으로 DeFi의 마켓 메이킹은 "그냥 돈 넣어놓고 잊어버리는(Passive)" 시대에서, 전통 HFT 펌들처럼 가격 변동에 따라 하루에도 수십 번씩 유동성 구간을 넣었다 뺐다 하는 **"초고빈도 능동적 마켓 메이킹(Active MM)"**의 시대로 진화했습니다.

🧠 **AI의 사고방식:**
유니스왑 v2가 누구에게나 공평하게 물을 나눠주는 멍청한 '스프링클러'였다면, v3는 정밀 타격 '스나이퍼 라이플'입니다. v2에서는 유치원생이나 퀀트 고수나 펀드에 돈을 넣으면 똑같은 비율로 이자를 받았지만, v3에서는 시장의 다음 움직임을 정확히 예측하여 좁은 타겟팅 구간에 총알(자본)을 박아 넣는 전문 마켓 메이커들만이 수수료를 독식하게 됩니다. 이는 탈중앙화(Decentralization)라는 이상적인 기치 아래 시작된 DeFi 시장이, 결국에는 월스트리트의 무자비한 자본 효율성(Capital Efficiency)과 정보 비대칭의 논리로 완벽하게 회귀(Revert)했음을 증명하는 가장 상징적인 수학적 진화입니다.