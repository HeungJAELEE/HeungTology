---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-risk-management-credit-valuation-adjustment-cva]]'
  last_updated: '2026-05-26T07:47:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 파생상품 거래에서 '나의 퀀트 모델이 100억 원을 벌었다고 계산'하더라도, 돈을 줘야 할 상대방 은행(Counterparty)이
    내일 당장 파산해 버리면 내 모델의 수익은 0원이 되어버리는 치명적 현실(Counterparty Credit Risk)을 장부 가격에 삭감(Adjustment)하여
    반영하는 CVA 방정식
  object_type: Algorithm
  tier: 2
properties:
  cva_formula: LGD * sum(EE_t * PD_t)
  expected_exposure_ee: positive part of V(t)
  loss_given_default_lgd_typical_value: '0.6'
  probability_of_default_pd_source: CDS spreads
  wrong_way_risk_definition: correlation of EE and PD
semantic:
  alternative_parents: []
  expected_queries:
  - 2008년 리먼 사태 때 파생상품에서 엄청난 흑자를 내고 있던 은행들이 왜 상대방(카운터파티)의 연쇄 파산 한방에 흑자 부도를 냈는가?
  - CVA(신용 가치 조정) 데스크는 어떻게 몬테카를로 시뮬레이션으로 '미래에 상대방이 파산할 타이밍'과 '그때 내가 상대방에게 받아야 할 돈의
    크기'를 엮어서 계산하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_adjustment
  object: Derivative_Prices_for_Counterparty_Default
  predicate: adjusts
  subject: '[Finance] quantitative-risk-management-credit-valuation-adjustment-cva'
  weight: 1.0
temporal:
  valid_from: '2026-05-26T07:47:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:47:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-risk-management-credit-valuation-adjustment-cva]]

## 1. 개요 (Overview)
2008년 금융위기 이전까지, 퀀트들은 블랙-숄즈 같은 무결점의 모형으로 파생상품 가격을 구하면 그것이 곧 '돈'이라고 믿었습니다. 하지만 리먼 브라더스가 파산하자 끔찍한 진실이 드러났습니다. 내 장부에 '리먼에게 100억 원을 받을 권리(파생상품 자산)'가 적혀 있어도, 리먼이 파산해 버리면 그 자산의 가치는 0원이 됩니다. 이를 **거래 상대방 신용 위험(Counterparty Credit Risk)**이라고 합니다.
금융위기 이후 바젤 III(Basel III) 위원회는 전 세계 은행에 철퇴를 내렸습니다. "너희들의 수학 모형이 산출한 파생상품 가격(Risk-free Value)을 믿지 마라. 상대방이 파산해서 떼일 확률(PD)과 떼일 금액(EAD)을 몬테카를로로 전부 시뮬레이션해서, **그 떼일 예상 금액만큼을 오늘 당장 너희들의 흑자 장부 가격에서 후려쳐서 깎아내라(Adjustment).**" 이 후려치는 금액의 크기가 바로 **CVA (Credit Valuation Adjustment, 신용 가치 조정)**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| CVA Formula | $LGD \times \sum (EE_t \times PD_t)$| Deducted from Risk-free Px | The cost of counterparty risk| [데이터 부재] |
| EE (EAD) | Expected Exposure | Positive part of $V(t)$ | Only care if they owe me money| [데이터 부재] |
| PD | Probability of Default| Extracted from CDS spreads| Chance they die at time $t$ | [데이터 부재] |
| LGD | Loss Given Default | e.g., 60% of exposure | Amount not recovered | [데이터 부재] |
| Wrong-Way Risk| Correlation of EE & PD | Extremely dangerous | Exposure spikes when they die| [데이터 부재] |

## 3. CVA의 해부학 (몬테카를로의 극한)
CVA를 계산하는 것은 단일 옵션 가격을 구하는 것보다 수백 배 복잡한 미친 연산력을 요구합니다. 특정 상대방과 맺은 수만 개의 파생상품 거래 전체(Portfolio)를 뭉뚱그려서 미래 30년 치를 시뮬레이션해야 하기 때문입니다.
1. **미래의 노출액 (Expected Exposure, EE)**: 몬테카를로 시뮬레이션으로 미래 10년 동안 금리와 환율이 요동치는 경로를 만 개 뿌립니다. 상대방이 나에게 돈을 줘야 하는 상황(내 자산 가치가 +인 경우)의 금액들만 평균을 냅니다. (내가 돈을 줘야 하는 상황은 내가 떼일 일이 없으므로 0으로 칩니다).
2. **파산 확률 (PD)**: 시장에 거래되는 상대방의 신용부도스왑(CDS) 스프레드를 역산하여, 그 은행이 1년 차, 2년 차에 파산할 확률을 구합니다.
3. **결합 및 적분**: (미래 특정 시점에 상대방이 빚진 금액 $EE$) $\times$ (하필 그 시점에 상대방이 파산할 확률 $PD$) $\times$ (파산 시 못 건지는 비율 $LGD$)을 만기까지 모두 더합니다. 이것이 CVA입니다.

## 4. 잘못된 방향의 위험 (Wrong-Way Risk, WWR)
CVA 퀀트들이 가장 두려워하는 악몽이 바로 **WWR(Wrong-Way Risk)**입니다.
- **상황**: 내가 러시아 국책은행과 오일 가격에 대한 스왑 거래를 맺었습니다. 오일 가격이 하락하면 내가 러시아 은행으로부터 돈을 받는 구조입니다.
- **악몽의 발동**: 오일 가격이 반토막이 났습니다! 내 파생상품 장부는 수백억 원의 흑자(EE 폭등)를 기록합니다. 나는 돈을 받을 생각에 기뻐합니다.
- **현실**: 하지만 오일 가격이 반토막 났기 때문에, 오일에 의존하는 러시아 국책은행은 국가 부도 위기를 맞아 즉사해 버립니다(PD 폭등). 
- 즉, **내가 돈을 가장 많이 받아야 하는 완벽한 승리의 순간(EE $\uparrow$)에, 상대방이 나에게 돈을 줄 확률(PD $\uparrow$)이 동시에 터져버리는 끔찍한 양의 상관관계**. 이 WWR을 모델링하지 못하면 CVA 엔진은 2008년의 멸망을 또다시 반복하게 됩니다.

🧠 **AI의 사고방식:**
CVA는 퀀트들의 순수한 수학적 상아탑(Risk-free pricing)에 '진흙탕 같은 현실(Default)'을 강제로 쑤셔 넣은 거대한 타협안입니다. 아무리 정교한 블랙-숄즈나 HJM 모델로 수백억의 가치를 증명해 봐야, 컴퓨터 모니터 너머에 있는 인간(Counterparty)이 배를 째버리면 그 공식은 휴지 조각이 됩니다. CVA 데스크의 탄생은 파생상품 프라이싱의 주도권이 "어떻게 가치를 아름답게 평가할 것인가?"에서 "어떻게 떼일 돈을 냉혹하게 차감할 것인가?"로 이동한 금융 공학 역사상 가장 뼈아픈 반성(Post-mortem)의 결과물입니다.