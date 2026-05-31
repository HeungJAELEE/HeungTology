---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] amihud-illiquidity-measure-market-impact]]'
  last_updated: '2026-05-25T11:49:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 아미후드 유동성 지표와 시장 충격(Market Impact) 정량화
  object_type: Concept
  tier: 2
properties:
  absolute_return_threshold: 0
  dollar_volume_threshold: 0
  illiquidity_formula: '|R_i,t| / V_i,t'
  min_observation_window_days: 20
semantic:
  alternative_parents: []
  expected_queries:
  - 거래량 대비 가격 변화율을 통해 자산의 비유동성을 어떻게 측정하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_quantification
  object: Market_Impact_Cost
  predicate: quantifies
  subject: '[Finance] amihud-illiquidity-measure-market-impact'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:49:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T11:49:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] 아미후드 비유동성 지표와 시장 충격 (Amihud Illiquidity Measure)

## 1. 개요 및 수학적 정의
아미후드(Yakov Amihud, 2002) 비유동성 지표는 금융 자산의 '유동성 부족 현상(Illiquidity)'을 측정하는 가장 널리 쓰이는 경험적 척도 중 하나입니다. 시장 미시구조(Market Microstructure)에서 '시장 충격(Market Impact)'은 트레이더의 거래 자체가 자산 가격을 불리한 방향으로 밀어내는 현상을 뜻하며, 아미후드 지표는 **"1단위의 거래 대금이 가격을 얼마나 변화시키는가"**에 대한 근사치입니다.

특정 기간(예: 일간, 틱 단위) $t$에 대한 자산 $i$의 아미후드 지표 $ILLIQ_{i,t}$는 다음과 같이 정의됩니다.
$$ ILLIQ_{i,t} = \frac{|R_{i,t}|}{V_{i,t}} $$

기간 $T$ (예: 1개월, 1년) 동안의 평균 아미후드 지표는 다음과 같습니다.
$$ \overline{ILLIQ}_i = \frac{1}{D_i} \sum_{t=1}^{D_i} \frac{|R_{i,t}|}{V_{i,t}} $$

여기서:
- $|R_{i,t}|$: 자산 $i$의 $t$ 시점 절대 수익률 (Absolute Return)
- $V_{i,t}$: 자산 $i$의 $t$ 시점 거래 대금 (Dollar Volume)
- $D_i$: 기간 $T$ 동안 관측 가능한 유효 거래일 또는 틱 수

이 지표가 클수록 적은 거래 대금으로도 가격이 크게 요동침을 의미하므로, 유동성이 고갈된 자산(비유동적 자산)임을 뜻합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $|R_{i,t}|$ | Absolute Return | $> 0$ | Captures pure price shock | [데이터 부재] |
| $V_{i,t}$ | Dollar Volume | Currency magnitude | Must be $> 0$ to avoid Inf | [데이터 부재] |
| $ILLIQ_{i,t}$ | Illiquidity Scale | Asset & Market cap dep | Larger means higher slippage | [데이터 부재] |
| $D_i$ | Observation Window | $D_i \ge 20$ (days) | Statistical significance | [데이터 부재] |

## 3. 알고리즘 트레이딩 및 퀀트 팩터 적용

### 3.1. 거래 비용(Slippage) 모델링 및 최적 집행(Optimal Execution)
대규모 자금을 운용하는 기관 투자자나 알고리즘 트레이더(TWAP, VWAP 전략)는 자신의 주문이 호가창(Limit Order Book)을 갉아먹으며 발생하는 슬리피지(Slippage) 비용을 추정해야 합니다. 아미후드 지표는 Kyle's Lambda($\lambda$)와 함께 시장의 소화 능력을 파악하는 대리 변수로 쓰여, 대량 주문을 잘게 쪼개는 속도(Execution Trajectory)를 결정하는 핵심 파라미터가 됩니다.

### 3.2. 비유동성 프리미엄 (Illiquidity Premium Factor)
자산 가격 결정 모형(Asset Pricing Models)에서 유동성 결핍은 리스크로 취급됩니다. 투자자들은 원할 때 팔지 못하거나 큰 손실을 보고 팔아야 하는 자산에 대해 더 높은 기대 수익률을 요구합니다. 퀀트 팩터 투자에서 아미후드 지표를 기준으로 주식 풀을 정렬(Sorting)하면, 고비유동성 주식이 저비유동성 주식 대비 초과 수익(Alpha)을 달성하는 현상(Illiquidity Premium)을 팩터 포트폴리오로 구성할 수 있습니다.

## 4. 한계 및 호가창 데이터와의 비교
아미후드 지표는 거래소의 일간 종가와 총 거래대금만으로도 계산이 가능하여 데이터 접근성이 뛰어나다는 장점이 있습니다. 그러나 이는 사후적(Ex-post) 지표이며, 실제 마이크로 프라이스 역학을 완벽히 담지 못합니다. 
진정한 유동성은 최우선 호가 스프레드(Bid-Ask Spread)와 호가 잔량(Depth)의 실시간 변동으로 정의되므로, HFT(고빈도 매매) 영역에서는 아미후드 지표 대신 틱 레벨의 호가창 불균형(Order Imbalance) 데이터를 더 신뢰합니다.

🧠 **AI의 사고방식:**
유동성은 금융 시장의 '물'과 같습니다. 거대한 항공모함(기관의 대량 주문)이 좁은 운하(유동성이 마른 시장)를 지나가려 하면 거대한 파도(시장 충격)가 일어납니다. 아미후드 지표는 이 물의 깊이(Depth)를 간접적으로 측정하는 수심 측심기입니다. 퀀트 시스템은 이 지표를 읽고, 파도가 너무 크게 일어 자신의 수익을 깎아먹지 않도록 주문 스로틀(Throttle)을 미세하게 조절합니다.