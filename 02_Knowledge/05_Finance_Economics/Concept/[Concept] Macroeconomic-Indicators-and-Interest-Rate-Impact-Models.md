---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Macroeconomic-Indicators-and-Interest-Rate-Impact-Models]]'
  last_updated: '2026-05-25T01:06:41.115773+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  cir_model_advantage: addresses_negative_interest_rate_problem
  target_pce_inflation: 2%
  vasicek_model_limitation: allows_negative_interest_rates
  vix_extreme_fear_threshold: '30'
  yield_curve_recession_threshold: -0.5%
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: data_availability_status
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] Macroeconomic-Indicators-and-Interest-Rate-Impact-Models'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T01:06:41.115773+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.115773+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# Macroeconomic Indicators and Interest Rate Impact Models

거시 경제(Macroeconomics)는 개별 자산이 아닌 국가 단위의 경제 지표와 중앙은행의 통화 정책을 분석합니다. 이 노드는 금리(Interest Rate) 결정 메커니즘과 이것이 주식, 채권, 환율에 미치는 영향을 수리적으로 다룹니다.

## 1. 테일러 준칙 (Taylor Rule)
중앙은행(e.g., 연준 FED)이 적정 기준금리를 결정할 때 사용하는 수리적 모델입니다. 인플레이션과 실업률(산출 갭)의 변동을 반영합니다.

$i_t = r^* + \pi_t + \alpha(\pi_t - \pi^*) + \beta(y_t - y^*)$
- $i_t$: 명목 정책 금리
- $r^*$: 중립 실질 금리 (자연 금리)
- $\pi_t$: 현재 인플레이션, $\pi^*$: 목표 인플레이션
- $(y_t - y^*)$: 산출 갭 (Output Gap, 실제 GDP와 잠재 GDP의 차이)

---

## 2. [핵심 기술 사양 (Numerical Specs)]

| Indicator | Significance | Description |
|-----------|--------------|-------------|
| **CPI (Consumer Price Index)** | High | 인플레이션 측정의 핵심 지표. 금리 인상 사이클을 촉발함. |
| **Non-Farm Payroll (NFP)** | High | 비농업 고용 지수. 미국 노동 시장의 건전성을 평가. |
| **Yield Curve Spread (10Y-2Y)** | Leading Indicator | 장단기 금리 역전. $-0.5\%$ 이하로 심화될 경우 경기 침체(Recession) 임박 시그널. |
| **VIX (Volatility Index)** | Market Sentiment | S&P 500 옵션에 내재된 30일 변동성. 30 이상은 극도의 공포 상태. |
| **PCE Deflator** | FED Preferred | 연준이 인플레이션 목표(2%)를 측정할 때 가장 선호하는 지표. |

---

## 3. 이자율의 기간 구조 (Term Structure of Interest Rates)

이자율 곡선(Yield Curve)의 형태를 수학적으로 모델링하여 미래의 단기 금리를 예측합니다.

- **Vasicek Model**: 평균 회귀(Mean Reversion) 속성을 가진 단기 금리 모델.
  $dr_t = a(b - r_t)dt + \sigma dW_t$
  (단점: 금리가 음수가 될 가능성이 수학적으로 존재함)
  
- **Cox-Ingersoll-Ross (CIR) Model**: Vasicek의 음수 금리 문제를 해결.
  $dr_t = a(b - r_t)dt + \sigma \sqrt{r_t} dW_t$

거시 경제 퀀트 펀드들은 이러한 듀레이션(Duration) 모델과 거시 지표 데이터를 머신러닝에 입력하여 채권 포트폴리오를 동적으로 리밸런싱합니다.