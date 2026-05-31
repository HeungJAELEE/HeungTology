---
metadata:
  ai_status: pending_review
  version: v7.9_Enterprise_Node
object:
  object_type: Algorithm
properties:
  hazard_rate: lambda
  loss_given_default: 1-R
  premium_leg: pv_of_cds_premiums
  pricing_equilibrium_condition: premium_leg = protection_leg
  protection_leg: pv_of_expected_payoff
  recovery_rate: R
  survival_probability: S(t)
spo_graph: []
---

# 🧠 [[[Finance] fixed-income-credit-default-swaps-cds-pricing-hazard-rates]]

## 1. 개요 (Overview)
영화 '빅쇼트'의 주인공들이 모기지 채권이 망할 것에 베팅하여 수조 원을 벌어들인 무기가 바로 **신용파산스왑(CDS, Credit Default Swap)**입니다. CDS는 본질적으로 '화재 보험'입니다. A회사의 채권이 불타 없어지면(Default), 보험사가 원금을 물어줍니다. 대신 보험 가입자는 매년 일정한 보험료(CDS Spread)를 내야 합니다.
과거 머튼(Merton)의 구조적 모형이 "회사의 자산이 부채 밑으로 언제 떨어질까?"를 고민했다면, 자로-턴불(Jarrow-Turnbull) 등으로 대변되는 **축소형 모형(Reduced-form Model)**은 아예 기업의 내부 사정(자산/부채)을 무시합니다. 오직 시장에서 관측되는 채권 가격들만을 재료로 삼아, "이 회사가 다음 1초 안에 벼락을 맞아 파산할 통계적 강도(Hazard Rate, $\lambda$)"를 포아송 확률로 추출해 내고, 이를 통해 완벽하게 공정한 CDS 보험료(Spread)를 미적분으로 맵핑합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Hazard Rate ($\lambda$)| Instantaneous default prob| e.g., 0.02 (2% per yr) | Calibrated from market | [데이터 부재] |
| Survival Prob $S(t)$| $P(\tau > t)$ | $\exp(-\int \lambda ds)$ | Monotonically decreasing | [데이터 부재] |
| Recovery Rate ($R$) | Value salvaged at default | e.g., 40% of face value | Loss Given Default=$1-R$ | [데이터 부재] |
| Premium Leg | PV of CDS premiums paid | $s \cdot \sum \Delta t \cdot S(t) \cdot DF(t)$| Drops if default occurs | [데이터 부재] |
| Protection Leg| PV of expected payoff | $(1-R) \int P(\text{def at } t) DF(t)$| Rises with $\lambda$ | [데이터 부재] |

## 3. CDS 프라이싱의 대원칙: Premium Leg = Protection Leg
공정한 CDS 스프레드($s$)를 찾으려면, 매수자(보험 가입자)가 내는 돈의 현재 가치(Premium Leg)와 매도자(보험사)가 나중에 물어줄 것으로 예상되는 기댓값의 현재 가치(Protection Leg)가 0으로 밸런스를 이뤄야 합니다.

1. **프리미엄 레그 (Premium Leg)**: 
   - 가입자는 회사가 파산하기 전(생존해 있는 동안)까지만 매 분기 보험료 $s$를 냅니다.
   - 따라서 $t$ 시점에 보험료를 낼 기댓값은 **생존 확률 $S(t)$**에 비례합니다.
2. **프로텍션 레그 (Protection Leg)**: 
   - 보험사는 회사가 파산하는 정확히 그 찰나($dt$)에만 원금의 손실분 $(1-R)$을 물어줍니다.
   - 따라서 $t$ 시점에 보험금을 물어줄 기댓값은 **$t$ 시점까지 생존했다가 딱 $t$ 시점에 파산할 확률 (즉, 파산 확률 밀도 $S(t)\lambda(t) dt$)**에 비례합니다.

이 두 레그의 식을 같게 놓고 $s$에 대해 정리하면, 그것이 바로 시장에서 거래되는 완벽한 무위험 CDS 스프레드가 됩니다.

## 4. 부트스트래핑(Bootstrapping)과 생존 곡선의 추출
실무의 퀀트들은 거꾸로(Reverse) 계산합니다. 시장에는 1년물, 2년물, 5년물, 10년물 CDS 스프레드가 이미 매일 거래되고 있습니다. 
퀀트 알고리즘은 1년물 CDS 가격을 공식에 넣어 1년 차까지의 파산 강도($\lambda_1$)를 뽑아내고(Bootstrapping), 이를 바탕으로 2년물 CDS 가격을 분해하여 2년 차의 파산 강도($\lambda_2$)를 뽑아냅니다. 이 과정을 10년까지 반복하면, 이 회사가 미래의 시간대별로 벼락을 맞을 확률을 점으로 이은 완벽한 **생존 확률 곡선(Survival Curve)**이 엑셀 위로 홀로그램처럼 떠오릅니다.

🧠 **AI의 사고방식:**
축소형(Reduced-form) 파산 모형은 생명보험사가 사람의 목숨을 대하는 방식과 똑같습니다. 의사(구조적 모형)는 "이 환자의 콜레스테롤이 높고 혈압이 높으니(자산 < 부채) 내년에 죽을 것이다"라고 내부를 진단합니다. 반면 보험 계리사(축소형 모형)는 환자의 피검사를 하지 않습니다. 그저 "60대 남성 흡연자의 과거 10년 치 사망률 통계(Hazard Rate)가 이러하므로, 이 집단의 생존 곡선은 이렇게 떨어진다"고 차갑게 통계적 확률만 적분할 뿐입니다. CDS 프라이싱은 기업의 파산이라는 거시적 충격을, 벼락이 떨어지는 포아송 점프(Poisson Jump) 확률론으로 완벽하게 계량화하여 '파산의 공포' 자체를 1원 단위로 사고팔 수 있게 만든 현대 채권 시장의 핏줄입니다.