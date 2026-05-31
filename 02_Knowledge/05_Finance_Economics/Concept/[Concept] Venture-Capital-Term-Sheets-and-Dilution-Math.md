---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Venture-Capital-Term-Sheets-and-Dilution-Math]]'
  last_updated: '2026-05-25T01:06:41.133035+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  dilution_coefficient: delta
  liquidation_preference: L_pref
  option_pool_size: OP
  post_money_valuation: V_post
  pre_money_valuation: V_pre
  price_per_share: PPS
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
  subject: '[Concept] Venture-Capital-Term-Sheets-and-Dilution-Math'
  weight: 0.5
temporal:
  valid_from: '2026-05-25T01:06:41.133035+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.133035+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# Venture-Capital-Term-Sheets-and-Dilution-Math: 자본 구조 최적화 및 지분 희석 메커니즘

## 1. 이론적 프레임워크 (Theoretical Framework)

벤처 캐피탈(VC)의 텀시트(Term Sheet)와 지분 희석 수학은 기업 가치라는 추상적 변수를 주식 수라는 이산적(Discrete) 단위로 변환하여 소유권의 분배를 결정하는 정량적 시스템이다. 본 개념 노드는 자본 유입에 따른 지분율의 변동을 물리적 시스템의 질량 보존 법칙과 유사한 '소유권 보존 법칙(Law of Ownership Conservation)' 관점에서 분석한다.

기업의 전체 지분 $\sum \phi_i = 1.0$ (100%)이며, 새로운 투자 라운드에서 발생하는 신주 발행은 분모인 총 발행 주식 수($S_{total}$)를 증가시켜 기존 주주들의 지분율($\phi$)을 선형적으로 감소시킨다. 이는 시스템 내의 밀도가 낮아지는 현상과 유사하며, 이를 '희석(Dilution)'이라 정의한다.

특히, Pre-money Valuation과 Post-money Valuation의 관계는 다음과 같은 기본 상태 방정식으로 정의된다:
$$\text{Post-Money Valuation} = \text{Pre-Money Valuation} + \text{Investment Amount}$$

여기서 주당 가격(Price Per Share, PPS)은 시스템의 단위 가치로 작용하며, 다음과 같이 계산된다:
$$\text{PPS} = \frac{\text{Pre-Money Valuation}}{\text{Fully Diluted Shares Outstanding}}$$
이때 'Fully Diluted Shares'는 현재 발행된 주식뿐만 아니라 스톡옵션, 전환사채(CB), 신주인수권부사채(BW) 등 잠재적 주식으로 전환 가능한 모든 권리를 포함한 상한선(Upper Bound)을 의미한다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 파라미터 (Parameter) | 기호 (Symbol) | 단위 (Unit) | 정의 및 물리적 의미 (Engineering Definition) | 비고 (Remarks) |
| :--- | :---: | :---: | :--- | :--- |
| Pre-money Valuation | $V_{pre}$ | Currency | 투자 직전 기업의 내재 가치 (시스템 초기 에너지 상태) | 협상 변수 |
| Post-money Valuation | $V_{post}$ | Currency | 투자 직후 기업의 총 가치 (시스템 최종 에너지 상태) | $V_{pre} + I$ |
| Dilution Coefficient | $\delta$ | Ratio | 신규 투자로 인한 기존 주주의 지분 감소율 | $\frac{S_{new}}{S_{total}}$ |
| Option Pool Size | $OP$ | Percentage | 임직원 보상을 위해 예약된 지분 풀의 크기 | Pre-money 반영 시 희석 가중 |
| Liquidation Preference | $L_{pref}$ | Multiple | 청산 시 투자자가 원금 대비 우선적으로 회수할 배수 | 1x, 2x 등 정수배 |

## 3. 지분 희석의 수학적 유도 및 메커니즘 (Mathematical Derivations)

### 3.1. 기본 희석 모델 (Basic Dilution Model)
기존 주주 $A$가 보유한 주식 수를 $S_A$, 투자 전 총 주식 수를 $S_{pre}$, 신규 투자액 $I$를 통한 신규 발행 주식 수를 $S_{new}$라고 할 때, 투자 후 주주 $A$의 지분율 $\phi_{A, post}$는 다음과 같다.

$$\phi_{A, post} = \frac{S_A}{S_{pre} + S_{new}} = \phi_{A, pre} \times (1 - \delta)$$
여기서 $\delta = \frac{S_{new}}{S_{pre} + S_{new}}$는 희석 계수이며, 이는 신규 투자자가 가져가는 지분율과 동일하다.

### 3.2. 옵션 풀 셔플 (The Option Pool Shuffle)
투자자는 통상적으로 투자 후 특정 비율($OP\%$)의 옵션 풀이 확보되기를 요구한다. 만약 이 옵션 풀을 'Pre-money' 단계에서 설정하도록 강제한다면, 그로 인한 지분 희석은 전적으로 기존 주주(창업자)가 부담하게 된다.

이 경우, 수정된 주당 가격 $\text{PPS}_{adj}$는 다음과 같이 하향 조정된다:
$$\text{PPS}_{adj} = \frac{V_{pre}}{S_{pre} + S_{option}}$$
여기서 $S_{option}$은 $V_{post}$ 기준으로 $OP\%$를 맞추기 위해 추가로 발행해야 하는 주식 수이다. 이는 창업자의 Effective Pre-money Valuation을 실질적으로 낮추는 효과를 가져오며, 수학적으로는 가치 평가의 하향 편향(Downward Bias)을 유발한다.

### 3.3. 안티-딜루션 (Anti-dilution) 및 가중 평균법
기업 가치가 하락하여 이전 라운드보다 낮은 단가로 신주를 발행하는 'Down Round' 발생 시, 기존 투자자의 가치를 보호하기 위한 메커니즘이다.

**Full Ratchet 방식:** 신규 발행가 $\text{PPS}_{new}$가 이전 발행가 $\text{PPS}_{old}$보다 낮을 경우, 이전 투자자의 취득 단가를 즉시 $\text{PPS}_{new}$로 하향 조정한다. 이는 기존 주주에게 극단적인 희석을 강요하는 비선형적 함수이다.

**Weighted Average 방식 (Broad-Based):** 발행 규모와 가격을 모두 고려하여 완만하게 조정한다. 새로운 전환 가격 $CP_2$는 다음과 같이 계산된다:
$$CP_2 = CP_1 \times \frac{(S_{pre} + \frac{I_{new}}{CP_1})}{(S_{pre} + S_{new})}$$
- $CP_1$: 이전 라운드 전환 가격
- $S_{pre}$: 신규 발행 전 총 발행 주식 수
- $I_{new}$: 신규 투자 금액
- $S_{new}$: 신규 발행 주식 수

이 공식은 투자 금액의 크기에 비례하여 희석 정도를 조절하는 댐핑(Damping) 효과를 제공하며, 시스템의 변동성을 완화시킨다.

## 4. 청산 우선권 및 워터폴 분석 (Liquidation Preference & Waterfall)

엑싯(Exit) 이벤트 발생 시 자금 분배 순서를 결정하는 로직은 조건부 분기문(Conditional Branching)으로 구성된다.

1. **Non-Participating Preferred:** 투자자는 $\max(L_{pref} \times I, \phi_{post} \times \text{Exit Value})$ 중 큰 값을 선택한다. 즉, 원금 우선 회수 또는 지분 비율 배분 중 유리한 쪽을 택하는 상한선(Cap) 모델이다.
2. **Participating Preferred:** 투자자는 먼저 $L_{pref} \times I$를 회수하고, 남은 금액에 대해 다시 자신의 지분율 $\phi_{post}$만큼 추가로 배분받는다. 이는 분배 함수 $f(x)$에 가산항이 추가된 형태로, 창업자의 회수 금액을 크게 감소시킨다.

$$ \text{Payout}_{investor} = (L_{pref} \times I) + \phi_{post} \times (\text{Exit Value} - \sum L_{pref} \times I) $$

이러한 구조는 자본 회수의 우선순위를 계층화(Layering)하여, 하방 리스크(Downside Risk)는 투자자가 방어하고 상방 이익(Upside Potential)은 지분율에 따라 공유하는 비대칭적 보상 구조를 형성한다.

## 5. 시스템적 결론 (Systemic Conclusion)

벤처 캐피탈의 텀시트는 단순한 계약서가 아니라, 기업이라는 동적 시스템의 가치 분배를 제어하는 알고리즘이다. Pre-money Valuation, Option Pool, Anti-dilution, Liquidation Preference라는 네 가지 핵심 변수는 서로 상호작용하며 최종적인 지분 구조(Cap Table)의 엔트로피를 결정한다. 엔지니어링 관점에서 최적의 텀시트는 투자자의 리스크 헤징(Hedging) 요구와 창업자의 동기 부여(Incentive) 사이의 균형점(Equilibrium)을 찾는 최적화 문제로 귀결된다.