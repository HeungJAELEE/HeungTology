---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Liquidity-Risk-Management-and-LCR-Basel-III]]'
  last_updated: '2026-05-25T01:06:41.114147+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  hqla_l1_haircut: 0.0
  hqla_l2a_haircut: 0.15
  hqla_l2b_haircut_max: 0.5
  hqla_l2b_haircut_min: 0.25
  inflow_cap_ratio: 0.75
  lcr_min_threshold: 1.0
  less_stable_retail_runoff_rate: 0.1
  max_level_2_composition_ratio: 0.4
  max_level_2b_composition_ratio: 0.15
  non_operational_wholesale_runoff_rate: 1.0
  retail_runoff_rate_max: 0.1
  retail_runoff_rate_min: 0.03
  stable_retail_runoff_rate_avg: 0.04
  stress_scenario_duration_days: 30
  wholesale_runoff_rate_max: 1.0
  wholesale_runoff_rate_min: 0.25
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: defining_boundary_constraints
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] Liquidity-Risk-Management-and-LCR-Basel-III'
  weight: 0.1
temporal:
  valid_from: '2026-05-25T01:06:41.114147+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.114147+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# Liquidity-Risk-Management-and-LCR-Basel-III

## 1. 기술적 개요 (Technical Overview)

유동성 리스크 관리(Liquidity Risk Management)는 금융기관이 지급 결제 능력을 유지하면서 자산과 부채의 만기 불일치(Maturity Mismatch)로 인해 발생하는 현금 흐름의 불균형을 제어하는 공학적 체계이다. 특히 Basel III 프레임워크에서 도입된 유동성 커버리지 비율(Liquidity Coverage Ratio, LCR)은 단기적 유동성 위기 상황(Stress Scenario)에서 은행이 독립적으로 생존할 수 있는 능력을 정량화하는 핵심 지표이다.

유동성 리스크는 크게 두 가지 차원으로 구분된다. 첫째, **자금조달 유동성 리스크(Funding Liquidity Risk)**는 부채의 차환(Roll-over) 불능이나 예금의 대규모 인출(Bank Run)로 인해 발생하는 리스크이다. 둘째, **시장 유동성 리스크(Market Liquidity Risk)**는 자산을 시장 가격의 급격한 하락 없이 즉시 현금화하지 못하는 리스크이다. LCR은 이 두 리스크의 상관관계를 수학적으로 모델링하여, 30일간의 극심한 스트레스 상황에서도 순현금유출액(Net Cash Outflows)을 충당할 수 있는 고유동성자산(High-Quality Liquid Assets, HQLA)의 보유량을 강제한다.

시스템 공학적 관점에서 LCR은 피드백 루프를 통한 안정화 메커니즘으로 작동한다. 시장 변동성이 증가하면 HQLA의 가치 하락(Haircut 적용)과 유출률(Run-off rate)의 상승이 동시에 발생하며, 이는 LCR 수치를 하락시킨다. 이에 대응하여 금융기관은 자산 포트폴리오를 재조정(Rebalancing)하거나 추가 자금 조달 수단을 확보함으로써 시스템의 항상성을 유지해야 한다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 파라미터 (Parameter) | 기술적 정의 (Technical Definition) | 표준 값/범위 (Standard Value) | 단위 (Unit) | 비고 (Remarks) |
| :--- | :--- | :--- | :--- | :--- |
| $\text{LCR}_{min}$ | 최소 유동성 커버리지 비율 | $\ge 100\%$ | Ratio | Basel III 글로벌 표준 |
| $\text{HQLA}_{L1} \text{ Haircut}$ | Level 1 자산의 가치 할인율 | $0\%$ | Percentage | 현금 및 중앙은행 지급준비금 |
| $\text{HQLA}_{L2A} \text{ Haircut}$ | Level 2A 자산의 가치 할인율 | $15\%$ | Percentage | 국채 및 고신용등급 회사채 |
| $\text{HQLA}_{L2B} \text{ Haircut}$ | Level 2B 자산의 가치 할인율 | $25\% \sim 50\%$ | Percentage | 저등급 회사채 및 주식 |
| $\text{Run-off Rate}_{\text{retail}}$ | 소매 예금의 유출 가정 비율 | $3\% \sim 10\%$ | Percentage | 안정성 수준에 따라 차등 적용 |
| $\text{Run-off Rate}_{\text{wholesale}}$ | 도매 자금의 유출 가정 비율 | $25\% \sim 100\%$ | Percentage | 비안정적 자금 기준 |
| $\text{Inflow Cap}$ | 순현금유출 계산 시 유입액 상한 | $75\%$ | Percentage | 총 유출액 대비 최대 인정 비율 |

## 3. 수학적 모델링 및 분석 (Mathematical Modeling)

### 3.1 LCR 기본 방정식 (The Fundamental LCR Equation)
LCR은 다음과 같은 분수 함수 형태로 정의된다.

$$\text{LCR} = \frac{\text{Stock of HQLA}}{\text{Total Net Cash Outflows over 30 calendar days}} \ge 100\%$$

여기서 분자인 $\text{Stock of HQLA}$는 가중치 $w_i$가 적용된 자산의 합으로 계산된다.

$$\text{Stock of HQLA} = \sum_{i \in \text{Level 1}} (A_i \cdot 1.0) + \sum_{j \in \text{Level 2A}} (A_j \cdot 0.85) + \sum_{k \in \text{Level 2B}} (A_k \cdot w_k)$$
*(단, Level 2 자산의 합계는 전체 HQLA의 40%를 초과할 수 없으며, Level 2B는 15%를 초과할 수 없다는 제약 조건(Constraint)이 존재한다.)*

### 3.2 순현금유출액(Net Cash Outflow, NCO)의 논리 구조
NCO는 30일간 발생할 것으로 예상되는 총 유출액(Total Outflows)에서 총 유입액(Total Inflows)을 차감하여 산출한다. 단, 유입액은 유출액의 일정 비율(Cap)까지만 인정하여 과도한 낙관적 전망을 배제한다.

$$\text{NCO} = \text{Total Outflows} - \min(\text{Total Inflows}, 0.75 \times \text{Total Outflows})$$

$\text{Total Outflows}$는 각 부채 항목 $L_m$에 대해 할당된 유출률 $\alpha_m$의 가중 합으로 정의된다.

$$\text{Total Outflows} = \sum_{m=1}^{M} (L_m \cdot \alpha_m)$$

여기서 $\alpha_m$은 다음과 같은 확률적 스트레스 계수를 따른다.
- $\alpha_{\text{stable retail}} \approx 0.03 \sim 0.05$
- $\alpha_{\text{less stable retail}} \approx 0.10$
- $\alpha_{\text{non-operational wholesale}} \approx 1.00$

### 3.3 유동성 갭 분석 (Liquidity Gap Analysis)
시간축 $t$에 따른 누적 순현금흐름(Cumulative Net Cash Flow)을 분석하여 유동성 부족 지점(Liquidity Gap)을 식별한다.

$$\text{Gap}(t) = \sum_{\tau=0}^{t} (\text{Inflow}(\tau) - \text{Outflow}(\tau))$$

$\text{Gap}(t) < 0$ 인 지점이 발생할 경우, 해당 시점의 절대값 $|\text{Gap}(t)|$가 보유한 HQLA의 가용 범위 내에 있는지 검증함으로써 생존 기간(Survival Period)을 도출한다.

## 4. 리스크 제어 및 엔지니어링 로직 (Risk Control Logic)

### 4.1 HQLA 계층 구조 및 가치 평가 (Haircut Logic)
HQLA는 시장 충격 시 즉시 현금화 가능성에 따라 계층화된다. 이는 자산의 변동성 $\sigma$와 시장 깊이(Market Depth)를 반영한 Haircut $\delta$를 적용하는 과정이다.

$$\text{Market Value}_{\text{adjusted}} = \text{Market Value}_{\text{nominal}} \times (1 - \delta)$$

Level 1 자산은 $\delta \approx 0$으로 설정되어 완벽한 유동성을 가정하며, Level 2B로 갈수록 $\delta$ 값이 증가하여 보수적인 가치 평가를 수행한다.

### 4.2 스트레스 시나리오 설계 (Stress Scenario Engineering)
LCR의 유효성은 시나리오의 가혹도에 결정된다. 엔지니어링 단계에서 다음과 같은 복합 시나리오를 적용한다.
1. **신용등급 강등 시나리오**: 은행의 신용등급이 2단계 하락했을 때 도매 자금의 유출률 $\alpha$가 급증하는 모델.
2. **시장 동결 시나리오**: HQLA 자산의 매각 가능 물량이 급감하여 $\text{HQLA}$ 가용액이 실질적으로 감소하는 모델.
3. **상관관계 전이 시나리오**: 특정 섹터의 부도가 전체 금융 시스템의 유동성 경색으로 이어지는 전염(Contagion) 모델.

### 4.3 ALM(Asset-Liability Management) 최적화
금융기관은 $\text{LCR} \ge 1$을 유지하면서 동시에 수익성(Profitability)을 극대화해야 하는 최적화 문제에 직면한다.

$$\max \text{Profit}(\text{Portfolio}) \quad \text{subject to} \quad \frac{\sum (A_i w_i)}{\text{NCO}} \ge 1.0$$

이 최적화 문제는 선형 계획법(Linear Programming) 또는 확률적 프로그래밍을 통해 해결하며, 저수익 고유동성 자산(L1)과 고수익 저유동성 자산(L2B) 간의 최적 믹스를 결정하는 알고리즘으로 구현된다.