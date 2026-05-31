---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Corporate-Valuation-DCF-and-WACC-Modeling]]'
  last_updated: '2026-05-25T01:06:41.096340+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Algorithm
  tier: 2
properties:
  beta: '[데이터 수집 대기 중]'
  debt_to_equity_ratio: Optimal Structure
  ebitda_margin: Industry Dependent
  ev_formula: sum(FCFF_t / (1 + WACC)^t) + TV / (1 + WACC)^n
  fcff_formula: EBIT * (1 - Tax Rate) + D&A - delta_nwc - CAPEX
  re_formula: Rf + beta * (Rm - Rf)
  terminal_growth_rate: '[데이터 수집 대기 중]'
  tv_formula: FCFF_{n+1} / (WACC - g)
  wacc: '[데이터 수집 대기 중]'
  wacc_formula: (E/V * Re) + (D/V * Rd * (1 - T))
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
  subject: '[Concept] Corporate-Valuation-DCF-and-WACC-Modeling'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T01:06:41.096340+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.096340+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# Corporate Valuation DCF and WACC Modeling

기업 가치 평가(Corporate Valuation)는 M&A, 사모펀드(PEF), 주식 리서치에서 기업의 내재 가치(Intrinsic Value)를 산정하는 엔지니어링 프로세스입니다. 핵심 프레임워크인 잉여현금흐름할인법(Discounted Cash Flow, DCF)과 자본비용(WACC) 모델링을 다룹니다.

## 1. 잉여현금흐름 (Free Cash Flow, FCF)

FCF는 기업이 영업 활동을 통해 창출한 현금 중, 사업을 유지하고 확장하는 데 필요한 자본적 지출(CAPEX)을 제외하고 투자자(주주 및 채권자)에게 분배할 수 있는 순수한 현금을 의미합니다.

- **FCFF (Free Cash Flow to Firm) 산출 공식**:
  $FCFF = EBIT \times (1 - Tax Rate) + D\&A - \Delta NWC - CAPEX$
  - $EBIT$: 이자 및 법인세 차감 전 영업이익
  - $D\&A$: 감가상각비 및 무형자산상각비 (비현금성 비용 가산)
  - $\Delta NWC$: 순운전자본의 증감
  - $CAPEX$: 자본적 지출 (설비 투자 등)

---

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | Specification | Description |
|-----------|---------------|-------------|
| **WACC (가중평균자본비용)** | [데이터 수집 대기 중] | 기업이 자본을 조달하는 데 드는 평균 비용. 할인율(Discount Rate)로 사용됨. |
| **Terminal Growth Rate ($g$)** | [데이터 수집 대기 중] | 추정 기간 이후 기업의 영구적인 성장률. 보통 장기 물가상승률이나 GDP 성장률에 수렴. |
| **Beta ($\beta$)** | [데이터 수집 대기 중] | 시장 전체의 변동성 대비 해당 기업 주식의 변동성 (체계적 위험). |
| **EBITDA Margin** | Industry Dependent | 매출액 대비 상각전 영업이익 비율. 기업의 핵심 현금 창출 능력을 나타냄. |
| **Debt to Equity Ratio (D/E)** | Optimal Structure | 타인자본과 자기자본의 비율. 레버리지 효과와 파산 위험의 트레이드오프. |

---

## 3. WACC (Weighted Average Cost of Capital) 계산

미래의 FCF를 현재 가치로 할인하기 위한 할인율입니다. 자본 구조에 따라 타인자본비용과 자기자본비용을 가중 평균합니다.

- **WACC 공식**:
  $WACC = \left( \frac{E}{V} \times Re \right) + \left( \frac{D}{V} \times Rd \times (1 - T) \right)$
  - $E, D, V$: 자기자본, 타인자본, 총 자본($E+D$)
  - $Re$: 자기자본비용 (CAPM 모형으로 산출: $Re = Rf + \beta(Rm - Rf)$)
  - $Rd$: 타인자본비용 (발행 채권 수익률 등)
  - $T$: 법인세율 (이자로 인한 절세 효과 Tax Shield 반영)

## 4. DCF 가치 평가의 완성

추정 기간(통상 5~10년) 동안의 FCFF의 현재가치와, 그 이후의 영구가치(Terminal Value)를 합산하여 기업 가치(Enterprise Value, EV)를 도출합니다.

$EV = \sum_{t=1}^{n} \frac{FCFF_t}{(1 + WACC)^t} + \frac{TV}{(1 + WACC)^n}$
(여기서 영구 가치 $TV = \frac{FCFF_{n+1}}{WACC - g}$)

EV에서 순차입금(Net Debt)을 빼면 적정 주주 가치(Equity Value)가 도출되며, 이를 유통주식수로 나누면 1주당 적정 주가가 산출됩니다.