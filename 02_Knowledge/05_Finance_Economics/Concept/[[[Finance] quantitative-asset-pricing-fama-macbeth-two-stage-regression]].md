---
metadata:
  ai_status: pending_review
  version: v7.9_Enterprise_Node
object:
  object_type: Algorithm
properties:
  beta_sensitivity: beta_i_k
  factor_premium: lambda_k_t
  stage_1_regression_type: time-series
  stage_2_regression_type: cross-section
  t_statistic_threshold: 1.96
  typical_rolling_window_months: 60
spo_graph: []
---

# 🧠 [[[Finance] quantitative-asset-pricing-fama-macbeth-two-stage-regression]]

## 1. 개요 (Overview)
수많은 퀀트 리서처들은 매일 새로운 지표를 들고 옵니다. "CEO가 트위터를 많이 할수록 주가가 오른다! 트위터 팩터를 펀드에 넣자!" 하지만 이런 주장의 99%는 과거 데이터에만 우연히 들어맞는 과적합(Data Mining)입니다.
1973년, 유진 파마(Eugene Fama)와 제임스 맥베스(James MacBeth)는 누군가 새로운 팩터를 들고 왔을 때 그것이 **진짜 시장에서 보상(Risk Premium)을 받는 팩터인지 검증하는 가혹한 2단계 통계적 재판소**를 세웠습니다. 파마-맥베스 회귀는 주식 수익률 데이터의 시계열(Time) 특성과 횡단면(Cross-section, 종목 간 차이) 특성을 동시에 찢어 발겨, 시간의 흐름에 따른 변동성(표준 오차)을 완벽하게 교정합니다. 오늘날 전 세계 모든 금융 논문과 퀀트 펀드에서 "새로운 알파를 찾았다"고 선언하려면 반드시 이 파마-맥베스의 관문을 통과해야만 합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Stage 1: Time-Series| Roll regression over time| e.g., 60-month window | Extracts $\beta_{i}$ (Sensitivities)| [데이터 부재] |
| $\beta_{i,k}$ | Sensitivity of asset $i$ to factor $k$| e.g., 1.2 | The X-variables for Stage 2| [데이터 부재] |
| Stage 2: Cross-Section| Regress returns on $\beta$| e.g., $N=500$ stocks every month| Extracts $\lambda_t$ (Premiums) | [데이터 부재] |
| $\lambda_{k,t}$ | Factor $k$'s premium at time $t$| e.g., 0.5% per month | Is the factor rewarded? | [데이터 부재] |
| t-statistic | Significance test | $\bar{\lambda} / (Std(\lambda)/\sqrt{T})$ | Must be $> 1.96$ to pass | [데이터 부재] |

## 3. 파마-맥베스 2단계 (Two-Stage) 알고리즘
### Stage 1: 시계열 회귀 분석 (Time-Series Regression) - "너의 민감도를 밝혀라"
먼저 N개의 개별 주식(또는 포트폴리오) 각각에 대해 과거 3~5년 치 일별/월별 수익률 데이터를 길게 늘어놓고 회귀 분석을 돌립니다.
- 목적: 이 주식이 문제의 '트위터 팩터'에 얼마나 민감하게 반응하는가($\beta$)를 추출합니다.
- 결과물: 주식 500개 각각에 대한 500개의 $\beta$ 값들을 얻어냅니다.

### Stage 2: 횡단면 회귀 분석 (Cross-Sectional Regression) - "민감한 놈이 진짜 돈을 더 벌었는가?"
이제 축을 완전히 돌립니다. 이번 달(단 1개월)의 주식 500개 수익률을 Y축에 놓고, 아까 1단계에서 구한 주식 500개의 $\beta$를 X축에 놓은 뒤 단면 회귀 분석을 돌립니다.
- 목적: "이번 달에 $\beta$가 높았던(트위터 팩터에 민감했던) 주식들이, $\beta$가 낮았던 주식들보다 **실제로 프리미엄($\lambda_t$)을 더 받았는가?**"를 묻습니다.
- 이 횡단면 분석을 1990년 1월부터 2020년 12월까지 **매달(Every single month)** 수백 번 반복하여 수백 개의 $\lambda_1, \lambda_2, \dots, \lambda_T$ (월별 프리미엄 값)를 수집합니다.

## 4. 최종 판결: T-검정 (The T-test)
매달 계산된 수백 개의 $\lambda_t$를 쫙 모아놓고 평균($\bar{\lambda}$)을 냅니다.
- 만약 이 평균이 양수(+)이고 통계적으로 유의미하다면(t-stat > 1.96)? **"축하합니다. 트위터 팩터는 30년 동안 꾸준히 양의 프리미엄을 준 진짜 알파입니다."**
- 만약 $\lambda_t$가 어떤 달은 +10%였다가 어떤 달은 -10%로 미친 듯이 널뛰기해서 평균의 표준오차가 너무 크다면(t-stat < 1.96)? **"기각합니다. 당신의 팩터는 그저 운 좋게 몇 달 맞은 노이즈일 뿐입니다."**

🧠 **AI의 사고방식:**
단순한 패널 회귀 분석(Panel Regression)은 공간과 시간을 한 통에 붓고 믹서기로 갈아버리기 때문에, 주식들 간의 잔차가 서로 끈끈하게 엮여 있는 횡단면 상관관계(Cross-sectional Correlation)를 무시하여 거짓말(P-value 부풀리기)을 합니다. 반면 파마-맥베스는 1단계에서 '각 개체의 성향($\beta$)'을 세로로 썰어내고, 2단계에서 '시간의 흐름에 따른 보상($\lambda$)'을 가로로 썰어내는 '십자(Cross) 해부학'입니다. 시간 단위로 한 번, 공간 단위로 한 번, 도합 두 번을 회귀 분석의 체에 걸러냄으로써, 퀀트들은 모래(노이즈)를 완벽히 털어내고 진짜 황금(Factor Premium)만을 남길 수 있습니다.