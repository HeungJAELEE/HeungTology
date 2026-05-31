---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-credit-risk-merton-structural-model]]'
  last_updated: '2026-05-25T14:56:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 기업의 총자산 가치 변동을 기하 브라운 운동(GBM)으로 가정하고, 기업의 부채를 만기(T)에 갚아야 할 '스트라이크 프라이스'로
    해석함으로써 파산(Default) 확률을 유러피안 콜/풋 옵션의 원리로 증명한 머튼(Merton)의 구조적 신용 모형
  object_type: Algorithm
  tier: 2
properties:
  d: face value of debt (strike price)
  dd: distance to default
  dd_formula: ln(v/d) / (sigma_v * sqrt(t))
  e_t: equity value at maturity
  payoff_function: max(v_t - d, 0)
  prob_of_default: probability of default
  v_t: total firm asset value
semantic:
  alternative_parents: []
  expected_queries:
  - 왜 주주(Equity holder)가 들고 있는 주식은 재무공학적으로 회사의 자산(Asset)을 기초자산으로 하고 부채(Debt)를 행사가로
    하는 콜옵션(Call Option)과 완벽히 동일한가?
  - 머튼 모델은 블랙-숄즈 방정식을 사용하여 상장 기업이 만기에 파산할 통계적 확률(Default Probability)을 어떻게 계산해 내는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_representation
  object: Equity_as_a_Call_Option
  predicate: frames
  subject: '[Finance] quantitative-credit-risk-merton-structural-model'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T14:56:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:56:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-credit-risk-merton-structural-model]]

## 1. 개요 (Overview)
은행이나 채권 투자자가 기업에 돈을 빌려줄 때 가장 궁금한 것은 "이 회사가 만기(T)에 빚을 갚을 수 있을 확률이 몇 %인가?"입니다. 기존의 회계학적 접근은 재무제표의 부채 비율이나 이자보상배율 같은 과거 데이터를 보았습니다.
하지만 1974년 로버트 머튼(Robert Merton)은 이 문제를 완전히 새로운 재무공학적 시각으로 박살 냅니다. 그는 **"기업의 주식(Equity)이란, 결국 기업의 총자산(Asset)을 기초자산으로 하고 부채(Debt)를 행사가(Strike Price)로 하는 유러피안 콜옵션(Call Option)과 수식적으로 100% 동일하다"**는 충격적인 프레임워크를 제시했습니다. 이를 통해 주식 시장에서 매일 거래되는 주가와 변동성 데이터를 블랙-숄즈 공식에 역대입하여, 기업의 파산 확률을 실시간으로 뽑아내는 퀀트 신용 리스크의 '구조적 모형(Structural Model)'이 탄생했습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $V_T$ | Total firm asset value | Unobservable directly | Follows GBM | [데이터 부재] |
| $D$ | Face value of debt | Strike price ($K$) | Paid exactly at $T$ | [데이터 부재] |
| $E_T$ | Equity value at $T$ | $\max(V_T - D, 0)$ | Call option payoff | [데이터 부재] |
| Distance to Default| $DD = \frac{\ln(V/D) + \dots}{\sigma_V \sqrt{T}}$ | Standard deviations | Higher $DD \implies$ safer firm| [데이터 부재] |
| Prob of Default | $N(-DD)$ | e.g., 0.15% | Physical/Risk-neutral | [데이터 부재] |

## 3. 주식(Equity) = 콜옵션 (Call Option)의 증명
회사의 만기 시점($T$) 총자산 가치를 $V_T$, 갚아야 할 부채를 $D$라고 합시다. 만기에 주주(Equity holder)가 가져가는 몫 $E_T$는 다음과 같이 결정됩니다.

- **자산 > 부채 ($V_T > D$)**: 회사가 돈을 잘 벌었습니다. 채권자에게 빚 $D$를 갚고 남은 돈($V_T - D$)은 전부 주주의 몫이 됩니다.
- **자산 < 부채 ($V_T < D$)**: 회사가 망했습니다(파산, Default). 주식회사는 유한책임이므로 주주는 남은 빚을 갚을 의무가 없으며, 그냥 주식의 가치는 $0$이 됩니다. 채권자가 남은 자산 $V_T$를 전부 다 가져갑니다.

이를 수식으로 쓰면 **$E_T = \max(V_T - D, 0)$** 입니다. 이것은 기초자산 $V$가 행사가 $D$를 넘었을 때만 수익이 나는 **콜옵션의 페이오프 함수와 완벽히 일치**합니다. 

## 4. 파산까지의 거리 (Distance to Default, DD)
머튼은 이 원리를 이용하여 주식 시장의 데이터(주식의 시가총액 $E$, 주가의 변동성 $\sigma_E$)를 블랙-숄즈 방정식에 역으로 집어넣어, 눈에 보이지 않는 '기업의 진짜 자산 가치($V$)'와 '자산의 변동성($\sigma_V$)'을 연립방정식으로 역추산(Reverse-engineering)해 냅니다.
이렇게 구한 변수들로 **파산까지의 거리(Distance to Default, DD)**를 계산합니다.
- DD는 "현재 우리 회사의 자산이 파산선(부채 $D$)으로부터 몇 시그마(표준편차)만큼 멀리 떨어져 있는가?"를 나타내는 지표입니다.
- 예를 들어 $DD = 3$ 이라면, 파산 확률은 정규분포의 3 시그마 밖의 꼬리 확률인 **0.13%**로 정밀하게 도출됩니다. (Moody's KMV 모델의 핵심 로직입니다).

🧠 **AI의 사고방식:**
회계사들이 과거 분기 실적이라는 '백미러'를 보며 파산 위험을 평가할 때, 머튼은 주식 시장의 실시간 주가와 옵션 내재 변동성이라는 '레이더'를 이용해 미래를 투시했습니다. 파산(Default)이란 하늘에서 뚝 떨어지는 천재지변이 아니라, 자산이라는 액체가 흘러내리다 부채라는 컵의 바닥을 뚫고 지나가는 순간(Strike)일 뿐입니다. 머튼은 기업 금융의 가장 골치 아픈 채권 파산 문제를 파생상품의 방정식으로 우아하게 치환해 버림으로써, 주식 시장(Equity)과 채권 시장(Credit) 사이를 가로막고 있던 거대한 벽을 허물어버린 재무공학의 통일장 이론을 완성했습니다.