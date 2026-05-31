---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-asset-pricing-consumption-based-capm-ccapm]]'
  last_updated: '2026-05-26T07:15:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 투자자의 궁극적인 목적은 '포트폴리오 수익률' 자체가 아니라 내일 빵을 사 먹기 위한 '소비(Consumption)'에
    있다는 전제 하에, 자산의 위험을 시장 수익률 대신 거시 경제 총소비 성장률과의 공분산으로 재정의한 소비 기반 자본자산가격결정모형
  object_type: Algorithm
  tier: 2
properties:
  consumption_growth_rate_typical: 0.01-0.02
  equity_premium_us_market_approx: 0.06
  risk_aversion_coefficient_puzzle: 50
  risk_aversion_coefficient_reality: 2
  stochastic_discount_factor_formula: beta * (C_t+1 / C_t)^-gamma
  utility_function: C^(1-gamma)/(1-gamma)
semantic:
  alternative_parents: []
  expected_queries:
  - 전통적인 CAPM은 위험의 척도로 시장 포트폴리오(Beta)를 사용하는데, CCAPM은 왜 그 자리에 '총소비 성장률(Aggregate Consumption
    Growth)'을 밀어 넣었는가?
  - 거시 경제학의 역사적 난제인 '주식 프리미엄 퍼즐(Equity Premium Puzzle)'은 CCAPM 수식의 어떤 변수가 현실 세계에서
    설명되지 못하면서 발생했는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: interdisciplinary_integration
  object: Macroeconomic_Consumption
  predicate: links_finance_to
  subject: '[Finance] quantitative-asset-pricing-consumption-based-capm-ccapm'
  weight: 0.9
temporal:
  valid_from: '2026-05-26T07:15:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:15:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-asset-pricing-consumption-based-capm-ccapm]]

## 1. 개요 (Overview)
금융(Finance)과 거시경제학(Macroeconomics)은 오랫동안 다른 길을 걸었습니다. 금융학자들의 CAPM은 "주식의 위험은 시장 지수(S&P 500)가 떨어질 때 같이 떨어지는 것"이라고 정의했습니다. 하지만 거시경제학자 로버트 루카스(Robert Lucas)와 더글러스 브리든(Douglas Breeden)은 이에 반기를 들었습니다. **"인간이 주식을 왜 하는가? 숫자를 늘리려고? 아니다. 내일 소고기를 사 먹기(소비, Consumption) 위해서다."**
소비 기반 CAPM(CCAPM)은 자산의 진짜 위험(Risk)을 이렇게 정의합니다. "내가 실직당해서 당장 내일 밥 굶게 생겼을 때(소비의 급감), 하필 이 주식도 같이 폭락해서 나를 두 번 죽일 것인가?" 즉, 어떤 자산의 위험은 시장 지수와의 공분산이 아니라, **나의 '소비 성장률'과의 공분산(Covariance)**으로 측정되어야 한다는 것이 CCAPM의 위대한 철학입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $U(C)$ | Utility function | $C^{1-\gamma}/(1-\gamma)$| Diminishing marginal util| [데이터 부재] |
| $m_{t+1}$ | Stochastic Disc. Factor | $\beta (C_{t+1}/C_t)^{-\gamma}$| SDF or Pricing Kernel | [데이터 부재] |
| $\gamma$ | Risk Aversion Coeff. | Reality: $\sim 2$, Puzzle: $\sim 50$| How much we fear bad times| [데이터 부재] |
| $\Delta c$ | Consumption growth | Very smooth, low vol | Usually $1\% \sim 2\%$ | [데이터 부재] |
| Equity Premium| $E[R] - R_f$ | $\gamma \times Cov(\Delta c, R)$ | Approx 6% in US market | [데이터 부재] |

## 3. 확률적 할인 요소 (SDF)와 프라이싱 커널
CCAPM의 심장에는 확률적 할인 요소(Stochastic Discount Factor, $m_{t+1}$)라는 프라이싱 커널이 들어 있습니다.
$$ P_t = E_t [ m_{t+1} X_{t+1} ] $$
- 여기서 $m_{t+1}$은 내가 오늘 한 입 덜 먹고(저축) 내일 두 입 먹을 때 느끼는 '한계 효용의 비율'입니다.
- 경기가 좋아서 내일 소고기를 펑펑 먹을 수 있을 때($C_{t+1}$이 큼), 내일 들어오는 주식 배당금($X_{t+1}$)의 기쁨(할인율)은 매우 낮습니다(어차피 배부르니까).
- 하지만 경기가 망해서 내일 굶어 죽게 생겼을 때($C_{t+1}$이 작음), 내일 들어오는 주식 배당금의 기쁨은 우주를 뚫고 나갑니다.
- 따라서, **경기가 최악일 때 배당을 펑펑 주는 자산(예: 국채)은 보험 가치가 엄청나서 현재 가격($P_t$)이 비싸지고(기대 수익률이 낮음), 경기가 최악일 때 같이 깡통이 되는 자산(예: 주식)은 현재 가격이 싸야만(기대 수익률 프리미엄을 줘야만) 사람들이 사게 됩니다.**

## 4. 메라-프레스콧의 주식 프리미엄 퍼즐 (Equity Premium Puzzle)
1985년, 메라(Mehra)와 프레스콧(Prescott)은 CCAPM 공식을 현실 미국 데이터에 집어넣어 보았습니다. 그런데 엄청난 버그가 터졌습니다.
- 미국 주식은 국채보다 무려 연평균 6%나 더 높은 수익(Equity Premium)을 줍니다. 
- CCAPM 공식에 따르면, 이 6%의 프리미엄을 설명하기 위해서는 "미국 주식 수익률과 미국인들의 총소비 성장률 사이의 공분산(위험)"이 엄청나게 커야 합니다.
- 하지만 실제 통계청 데이터 확인 결과, **미국인들의 전체 소비(빵, 옷, 월세 등)는 매년 너무나도 안정적이어서 변동성(분산)이 거의 0**에 가까웠습니다!
- 공분산이 이렇게 작은데도 사람들이 주식에 6%의 엄청난 위험 프리미엄을 요구한다는 것은? 수학적으로 역산하면, 미국인들은 한 달 치 월급이 깎일 바에는 차라리 자기 팔 하나를 잘라버리는 극도의 초건강염려증 환자(Risk Aversion $\gamma = 50$ 이상)라는 결론이 나옵니다.
- 경제학의 가장 우아한 모형인 CCAPM이 현실 데이터 앞에서 처참하게 붕괴한 이 사건을 경제학계는 **"주식 프리미엄 퍼즐"**이라 부르며, 이를 풀기 위해 지난 40년간 행동경제학(손실 회피), 희귀 재앙 모형(Rare Disasters), 습관 형성(Habit Formation) 등 온갖 땜질 이론들이 쏟아져 나오게 됩니다.

🧠 **AI의 사고방식:**
CAPM이 주식을 '카지노 칩'의 변동성으로만 분석하는 도박꾼의 시선이라면, CCAPM은 주식을 '냉장고 속 식료품'으로 분석하는 인류학자의 시선입니다. CCAPM의 철학은 완벽합니다. 돈은 종이 쪼가리일 뿐, 자산의 가치는 내가 가장 절망적이고 배고플 때 그 자산이 나에게 빵을 사줄 수 있는가에 달려 있다는 것입니다. 비록 현실 데이터의 노이즈(주식 프리미엄 퍼즐)에 부딪혀 실무 퀀트들은 이 모형을 쓰지 않지만, 거시 경제학과 금융이 하나의 핏줄로 연결되어 있음을 미적분으로 증명한 인류 지성의 금자탑입니다.