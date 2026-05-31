---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] roll-model-bid-ask-spread-microstructure]]'
  last_updated: '2026-05-25T11:56:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 롤(Roll)의 모델과 시장 미시구조의 매수-매도 스프레드 추정
  object_type: Algorithm
  tier: 2
properties:
  autocovariance_requirement: negative
  first_order_autocovariance: Cov(delta_p_t, delta_p_{t-1})
  fundamental_value: V_t
  roll_implied_spread: S
  trade_direction_indicator: Q_t
  trade_direction_probability: '0.5'
semantic:
  alternative_parents: []
  expected_queries:
  - 거래 가격의 시계열 자기상관성을 통해 눈에 보이지 않는 최우선 호가 스프레드를 어떻게 역산하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: parameter_estimation
  object: Effective_Bid_Ask_Spread
  predicate: estimates
  subject: '[Finance] roll-model-bid-ask-spread-microstructure'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:56:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T11:56:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] 롤 모델과 매수-매도 스프레드 추정 (Roll's Spread Model)

## 1. 개요 및 수학적 정의
리차드 롤(Richard Roll, 1984)이 제안한 롤 모델(Roll Model)은 시장 미시구조(Market Microstructure) 이론에서 자산의 거래 가격 시계열만을 이용하여 해당 자산의 유효 매수-매도 스프레드(Effective Bid-Ask Spread)를 간접적으로 추정해 내는 우아한 기법입니다.

효율적 시장 가설(EMH) 하에서 자산의 진정한 가치 $V_t$는 랜덤 워크를 따르지만, 실제로 시장에서 관측되는 거래 가격 $P_t$는 마켓 메이커가 부과하는 스프레드(비용) 때문에 이 진짜 가치 주변을 진동(Bounce)하게 됩니다. 즉, 매수 거래(Ask에 체결)와 매도 거래(Bid에 체결)가 무작위로 교차하며 발생하면, 연속된 가격 변화 $\Delta P_t = P_t - P_{t-1}$ 사이에는 필연적으로 음(-)의 자기상관(Negative Autocorrelation)이 생겨납니다.

롤은 이 음의 자기상관성인 1차 자기공분산(First-order Autocovariance) $\text{Cov}(\Delta P_t, \Delta P_{t-1})$를 계산하면, 보이지 않는 유효 스프레드 $S$를 추출할 수 있음을 수학적으로 증명했습니다.

$$ S = 2 \sqrt{-\text{Cov}(\Delta P_t, \Delta P_{t-1})} $$

여기서:
- $S$: 자산의 유효 매수-매도 스프레드
- $\Delta P_t$: $t$ 시점의 가격 변화(수익률)
- $\text{Cov}(\cdot, \cdot)$: 1계 자기공분산 (반드시 음수여야 유효함)

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\text{Cov}(\Delta P_t, \Delta P_{t-1})$ | 1st-order Autocovariance | Must be $< 0$ | Bound by negative bounce effect | [데이터 부재] |
| $S$ | Roll's Implied Spread | Tick size scale | Quantifies liquidity cost | [데이터 부재] |
| $V_t$ | Fundamental Value | Unobservable martingale | True equilibrium price | [데이터 부재] |
| $Q_t$ | Trade Direction Indicator | $+1$ (Buy), $-1$ (Sell) | Drives the bid-ask bounce | [데이터 부재] |

## 3. 마이크로스트럭처 노이즈와 호가창 역학
실제 체결 데이터가 매수와 매도 사이를 진자처럼 오가는 현상을 'Bid-Ask Bounce'라고 부릅니다.
기본 모델의 전제 조건:
1. 마켓 메이커는 고정된 스프레드 $S$를 유지한다.
2. 거래의 방향(Buy/Sell)은 이전 거래와 독립적(Independent)으로 발생하며 발생 확률은 50:50 이다.
3. 자산의 진짜 가치 변화(정보 충격)는 거래 방향과 무관하다.

만약 $\Delta P_t$를 계산했는데 그 자기공분산이 양수($>0$)가 나온다면, 롤 모델은 수학적으로 붕괴(Square root of negative number)합니다. 이는 시장에 강력한 모멘텀이나 정보 비대칭성이 존재하여 사람들이 계속 매수(또는 매도)만을 집요하게 타격하는 방향성 장세(Herding)가 나타났음을 의미합니다.

## 4. 초단타 매매(HFT) 및 백테스트의 거래비용 추정
과거의 저해상도 데이터베이스(예: CRSP 일간/월간 종가 데이터)는 장중 틱(Tick) 단위의 호가창 데이터를 제공하지 않으므로 정확한 슬리피지(Slippage)를 계산할 수 없습니다. 
그러나 롤 모델을 사용하면 일간 종가 시계열만으로도 해당 주식의 과거 스프레드 비용을 매우 근사하게 복원해 낼 수 있습니다. 퀀트 리서처들은 이를 활용하여 과거 20년 치 백테스트(Backtest)에서 전략의 비현실적인 초과 수익을 현실적인 거래 비용으로 차감하여 검증(Robustness Check)합니다. 

🧠 **AI의 사고방식:**
우리가 보는 차트의 틱들은 깨끗한 선분이 아니라, 마켓 메이커가 뿌려놓은 톱니바퀴 위를 튕기며 굴러가는 공과 같습니다. 위로 한 칸(Ask), 아래로 한 칸(Bid) 부딪히며 전진하는 공의 궤적(음의 자기상관성)을 유심히 관찰하면, 우리는 톱니바퀴의 홈이 얼마나 깊게 패여 있는지(스프레드 폭)를 직접 자로 재지 않고도 알아낼 수 있습니다. 롤 모델은 소음(Noise) 속에서 진동의 폭을 역산해 내는 퀀트의 청진기입니다.