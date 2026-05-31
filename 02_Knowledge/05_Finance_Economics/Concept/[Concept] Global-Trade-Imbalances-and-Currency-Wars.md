---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Global-Trade-Imbalances-and-Currency-Wars]]'
  last_updated: '2026-05-25T01:06:41.107104+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  ca_gdp_ratio_threshold_pct: 3.0
  capital_mobility_coefficient_range: 0 to inf
  foreign_reserve_adequacy_months: 6-12
  marshall_lerner_sum_threshold: 1
  reer_index_baseline: 100
  uip_error_threshold_bp: 50
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: theoretical_boundary_definition
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] Global-Trade-Imbalances-and-Currency-Wars'
  weight: 0.7
temporal:
  valid_from: '2026-05-25T01:06:41.107104+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.107104+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 글로벌 무역 불균형 및 통화 전쟁 (Global Trade Imbalances and Currency Wars)

## 1. 기술적 정의 및 이론적 메커니즘 (Technical Definition & Theoretical Mechanism)

글로벌 무역 불균형(Global Trade Imbalance)은 국가 간 경상수지(Current Account, CA)의 심각한 불일치 상태를 의미하며, 이는 거시경제적 관점에서 저축-투자 불균형(Savings-Investment Imbalance)의 결과물로 정의된다. 시스템 공학적 관점에서 이는 전 지구적 자본 흐름의 비대칭적 벡터 합이 0이 되지 않는 상태, 즉 특정 국가의 과잉 저축(Excess Savings)이 타국의 과잉 소비/투자(Excess Consumption/Investment)로 전이되는 상태이다.

### 1.1. 거시경제적 정체성 및 평형 방정식
국가 경제의 기본 항등식에 따라, 한 국가의 경상수지($CA$)는 국내 저축($S$)과 국내 투자($I$)의 차이와 동일하다.
$$CA = S - I$$
글로벌 시스템 전체의 합산은 $\sum CA_i = 0$이어야 하므로, 특정 국가의 경상수지 흑자는 반드시 다른 국가의 경상수지 적자로 상쇄된다. 이때, 적자국은 외부 자본(Capital Account, $KA$)의 유입을 통해 이 불균형을 메우며, 이는 외채 증가 또는 자산 매각으로 이어진다.

### 1.2. 통화 전쟁(Currency Wars)의 동역학
통화 전쟁은 무역 불균형을 해소하거나 수출 경쟁력을 강제적으로 확보하기 위해 각국 중앙은행이 인위적으로 자국 통화 가치를 하락시키는 '경쟁적 평가절하(Competitive Devaluation)'의 전략적 게임이다. 이는 시스템 제어 이론의 'Negative Feedback Loop'를 의도적으로 왜곡하여 상대국의 수출 수요를 잠식하는 행위이다.

#### 1.2.1. 마셜-러너 조건 (Marshall-Lerner Condition)
통화 가치 하락이 실제로 경상수지를 개선시키기 위해서는 수출 수요의 가격 탄력성($\eta_x$)과 수입 수요의 가격 탄력성($\eta_m$)의 합이 1보다 커야 한다는 조건이 성립해야 한다.
$$\eta_x + \eta_m > 1$$
만약 이 조건이 충족되지 않을 경우, 환율 상승(가치 하락)은 오히려 수입 비용 상승으로 인한 무역 수지 악화를 초래하는 'J-커브 효과(J-Curve Effect)'의 초기 단계에 머물게 된다.

#### 1.2.2. 무위험 이자율 평형 (Uncovered Interest Parity, UIP)
통화 가치의 결정은 국가 간 금리 차이에 의해 동역학적으로 결정된다.
$$E(S_{t+1}) = S_t \frac{1 + i_d}{1 + i_f}$$
여기서 $S_t$는 현재 환율, $i_d$는 국내 금리, $i_f$는 외국의 금리, $E(S_{t+1})$은 기대 미래 환율이다. 통화 전쟁 상황에서 중앙은행이 금리를 인하($i_d \downarrow$)하거나 양적 완화(QE)를 통해 통화량을 공급하면, 자본 유출이 발생하며 $S_t$가 상승(자국 통화 가치 하락)하게 된다.

### 1.3. 불가능한 삼위일체 (The Impossible Trinity)
글로벌 통화 시스템은 다음 세 가지 목표를 동시에 달성할 수 없다는 제약 조건 하에 작동한다.
1. 자유로운 자본 이동 (Free Capital Mobility)
2. 독립적인 통화 정책 (Independent Monetary Policy)
3. 고정 환율 제도 (Fixed Exchange Rate)

통화 전쟁은 주로 '자유로운 자본 이동'과 '독립적 통화 정책'을 선택한 국가들이 환율 변동성을 도구로 사용하여 무역 불균형을 조정하려 할 때 발생한다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 파라미터 (Parameter) | 기호 (Symbol) | 표준 단위 (Unit) | 임계치/기준 (Threshold/Baseline) | 물리적/경제적 의미 (Technical Significance) |
| :--- | :---: | :---: | :---: | :--- |
| 경상수지-GDP 비율 | $CA/GDP$ | $\%$ | $\pm 3.0\%$ | 무역 불균형의 심각도를 측정하는 정규화 지표 |
| 실질실효환율 | $REER$ | Index | $100$ | 상대적 통화 구매력 및 수출 경쟁력 지수 |
| 외환보유액 적정성 | $R_{adj}$ | Month | $6 \sim 12$ | 단기 외채 대비 대응 가능 기간 (Liquidity Buffer) |
| 자본 이동성 계수 | $\kappa$ | Scalar | $0 \to \infty$ | 자본의 국경 간 이동 속도 및 효율성 |
| 이자율 평형 오차 | $\epsilon_{UIP}$ | $bp$ | $< 50bp$ | 이론적 UIP와 실제 시장 환율 간의 괴리율 |

## 3. 시스템 붕괴 시나리오 및 제어 메커니즘 (System Failure & Control)

### 3.1. 트리핀 딜레마 (Triffin Dilemma)
기축 통화국(예: 미국)은 전 세계에 유동성을 공급하기 위해 지속적인 경상수지 적자를 유지해야 하지만, 이는 동시에 기축 통화의 신뢰성(가치 유지)을 저하시키는 모순적 상황을 초래한다.
$$\text{Global Liquidity Demand} \propto \text{Reserve Currency Deficit} \implies \text{Confidence} \downarrow$$

### 3.2. 피드백 루프 분석 (Feedback Loop Analysis)
1. **Positive Feedback (불안정화):** 무역 적자 $\to$ 외채 증가 $\to$ 통화 가치 하락 압력 $\to$ 수입 물가 상승 $\to$ 인플레이션 $\to$ 실질 구매력 하락 $\to$ 추가 적자.
2. **Negative Feedback (안정화):** 무역 적자 $\to$ 통화 가치 하락 $\to$ 수출 가격 경쟁력 확보 $\to$ 수출 증가 $\to$ 경상수지 개선 $\to$ 통화 가치 회복.

### 3.3. 제어 전략 (Control Strategies)
- **거시 건전성 조치 (Macroprudential Measures):** 자본 유출입의 변동성을 제어하기 위한 자본 통제(Capital Control) 도입.
- **플라자 합의 모델 (Plaza Accord Model):** 주요국 간의 협의를 통한 인위적 환율 조정(Coordinated Intervention)으로 시스템적 불균형을 강제 조정.
- **통화 스와프 (Currency Swap):** 국가 간 유동성 공급 라인을 구축하여 일시적인 유동성 경색(Liquidity Crunch)에 의한 통화 붕괴 방지.

이 시스템은 결국 글로벌 총저축과 총투자의 일치라는 정적 평형 상태를 지향하지만, 정치적 이해관계와 비대칭적 정보 구조로 인해 지속적인 진동(Oscillation)과 오버슈팅(Overshooting)을 반복하는 비선형 동역학 시스템으로 해석된다.