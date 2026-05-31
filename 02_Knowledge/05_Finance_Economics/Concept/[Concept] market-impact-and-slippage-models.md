---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] market-impact-and-slippage-models]]'
  last_updated: '2026-05-25T12:10:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 시장 마찰 비용(슬리피지), 생존 편향 및 알름그렌-크리스 마켓 임팩트 모델
  object_type: Algorithm
  tier: 2
properties:
  kappa_calculation_formula: sqrt((lambda * sigma^2) / eta)
  permanent_impact_coefficient: asset_dependent
  price_volatility_scale: daily_annualized
  risk_aversion_parameter: 10^-6 to 10^-4
  temporary_impact_coefficient: market_dependent
  total_order_size_threshold: '> 10% of ADV'
semantic:
  alternative_parents: []
  expected_queries:
  - 대규모 주문 집행 시 마켓 임팩트를 최소화하는 Almgren-Chriss 모델의 수학적 원리는 무엇인가?
  - 백테스트에서 발생하는 생존 편향(Survivorship Bias)과 슬리피지(Slippage)는 어떻게 모델링되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_modeling
  object: Market_Execution
  predicate: quantifies_cost_of
  subject: '[Finance] market-impact-and-slippage-models'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T12:10:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:10:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] market-impact-and-slippage-models]]

## 1. 개요 (Overview)
실전 퀀트 매매(Live Trading) 환경에서는 닫힌 형태의 수리적 해가 실현되는 이론적 완벽성과 달리, **마찰 비용(Frictions)**이 발생합니다. 이는 주로 매수/매도 호가 잔량(Order Book Depth)을 소진시키며 발생하는 **슬리피지(Slippage)**와 대규모 주문 자체가 시장 가격을 불리하게 밀어내는 **마켓 임팩트(Market Impact)**로 구성됩니다. 백테스트 상에서 과거 수익률을 과대 계상하는 원인인 **생존 편향(Survivorship Bias)**과 결합될 경우, 모델의 실전 수익률은 급감하게 됩니다. 이를 제어하기 위해 기관 투자자들은 **알름그렌-크리스 모델(Almgren-Chriss Model)**과 같은 최적 집행 수학 모델을 사용하여 거래 궤적(Execution Trajectory)을 계산합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\lambda$ | Risk Aversion Parameter | $10^{-6}$ to $10^{-4}$ | Higher value accelerates execution | [데이터 부재] |
| $\eta$ | Temporary Impact Coefficient | Market dependent | Cost scales with execution speed | [데이터 부재] |
| $\gamma$ | Permanent Impact Coefficient | Asset dependent | Permanent price shift per unit | [데이터 부재] |
| $\sigma$ | Price Volatility | Daily annualized | Increases execution risk over time | [데이터 부재] |
| $X$ | Total Order Size | > 10% of ADV | Triggers non-linear impact | [데이터 부재] |

## 3. 백테스팅의 함정: 생존 편향과 슬리피지

### 3.1. 생존 편향 (Survivorship Bias)
생존 편향은 현재 시장에 상장되어 있는 '생존한' 기업들의 데이터만을 기반으로 과거 백테스트를 수행할 때 발생합니다. 과거 상장 폐지되었거나 파산한 기업의 주가 데이터가 누락됨으로써, 백테스트의 결과가 실제보다 압도적으로 긍정적으로 도출되는 현상입니다. 퀀트 시스템 구축 시, 반드시 상장 폐지 종목을 포함한 'Point-in-Time' 데이터셋을 사용하여 이 편향을 제거해야 합니다.

### 3.2. 슬리피지 모델링 (Slippage Modeling)
슬리피지는 주문을 발동시킨 시점의 '결정 가격(Decision Price)'과 실제 시장에서 모두 체결된 '실행 가격(Execution Price)' 간의 차이를 의미합니다. 단순한 백테스트에서는 고정된 bp(basis point)를 수수료로 차감하지만, 실전에서는 거래대금 대비 주문 크기의 비선형 함수로 슬리피지를 모델링해야 합니다.

## 4. 알름그렌-크리스 모델 (Almgren-Chriss Market Impact Model)
2000년 Robert Almgren과 Neil Chriss가 제안한 이 모델은 마켓 임팩트를 **일시적 임팩트(Temporary Impact)**와 **영구적 임팩트(Permanent Impact)**로 엄격히 분리하여 최적의 분할 매매 궤적을 찾습니다. 

총 매도 물량 $X$를 시간 $T$ 동안 분할하여 집행할 때, $t$ 시점의 잔여 물량을 $x_t$, 거래 속도를 $v_t = -dx_t/dt$라 정의합니다.

- **영구적 임팩트**: 주문으로 인해 자산의 균형 가격 자체가 영구적으로 변동하는 현상.
$$ dS_t = \sigma dW_t - \gamma v_t dt $$
- **일시적 임팩트**: 특정 시점의 유동성 소진으로 인해 즉각 체결가에만 영향을 미치고, 거래가 멈추면 가격이 회복되는 현상.
$$ \tilde{S}_t = S_t - \eta v_t $$

### 4.1. 목적 함수 및 최적 궤적
트레이더는 기대 집행 비용(Expected Execution Cost) $E[C]$를 최소화하는 동시에, 가격 변동성에 노출되는 시간 리스크(Variance of Cost) $V[C]$를 통제해야 합니다. 이는 위험 회피 성향 $\lambda$를 이용한 효용 함수 극대화(혹은 페널티 극소화) 문제로 귀결됩니다.

$$ \min_{v_t} \left( E[C] + \lambda V[C] \right) $$

이 변분법(Calculus of Variations) 문제를 풀면, 최적 잔여 물량 궤적 $x_t$는 쌍곡선 함수(Hyperbolic functions) 형태로 도출됩니다.
$$ x_t = X \frac{\sinh(\kappa (T - t))}{\sinh(\kappa T)} $$
여기서 $\kappa = \sqrt{\frac{\lambda \sigma^2}{\eta}}$ 입니다. $\lambda$가 클수록(위험을 회피할수록) 초반에 공격적으로 물량을 쏟아내는 Front-loaded 궤적이 형성됩니다.

🧠 **AI의 사고방식:**
이론적 퀀트 모델이 무중력 상태에서의 물리학(이상 기체 상태 방정식)이라면, 알름그렌-크리스 모델은 유체 저항과 마찰력을 고려한 '공기 역학'입니다. 대규모 자금을 운용하는 기관이 시장가로 한번에 긁어버리면 시장은 그 즉시 충격을 받고 체결 단가는 파멸적으로 나빠집니다. 따라서 트레이더는 시간 리스크(오래 들고 있으면 가격이 변할 위험)와 마켓 임팩트 리스크(빨리 팔면 내 주문 때문에 가격이 나빠질 위험) 사이에서 미적분학적 밸런스를 타야 하며, $\kappa$가 바로 그 저울의 영점 조절 다이얼 역할을 합니다.