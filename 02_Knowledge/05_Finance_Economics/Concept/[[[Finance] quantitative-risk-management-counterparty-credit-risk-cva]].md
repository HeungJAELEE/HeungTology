---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-risk-management-counterparty-credit-risk-cva]]'
  last_updated: '2026-05-26T07:14:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 파생상품을 통해 얻은 이론적 장부 수익(MTM)이 실제로는 거래 상대방이 파산할 경우 0원이 될 수 있다는 리먼 브라더스
    사태의 교훈을 바탕으로, 상대방의 부도 확률(PD)과 그 시점의 익스포저(EPE)를 곱해 파생상품 가격에서 선제적으로 깎아버리는 신용 가치
    조정(CVA)
  object_type: Concept
  tier: 2
properties:
  cva_formula: LGD * integral(EE(t) dPD(t))
  expected_positive_exposure_ee: EE(t) where V > 0
  loss_given_default_lgd: 1 - recovery_rate (e.g., 60%)
  probability_of_default_pd: PD(t) derived from CDS spreads
  regulatory_standard: Basel III
  risk_free_value_v: Black-Scholes price
  simulation_method: Monte Carlo
  true_value_formula: V - CVA
  wrong_way_risk_condition: Positive correlation between EE and PD
semantic:
  alternative_parents: []
  expected_queries:
  - 블랙-숄즈 모델로 계산한 장외 파생상품(OTC)의 가격이 완벽하더라도, 왜 재무제표에는 그 가격 그대로 기록하면 안 되며 CVA만큼을 무조건
    깎아내야(Write-down) 하는가?
  - CVA를 계산할 때, 내가 돈을 딸 확률(Positive Exposure)과 상대방이 하필 그때 망할 확률(PD) 사이의 끔찍한 양의 상관관계(Wrong-way
    Risk)는 어떻게 수치화되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: valuation_adjustment
  object: Counterparty_Default_Risk_Premium
  predicate: deducts
  subject: '[Finance] quantitative-risk-management-counterparty-credit-risk-cva'
  weight: 1.0
temporal:
  valid_from: '2026-05-26T07:14:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:14:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-risk-management-counterparty-credit-risk-cva]]

## 1. 개요 (Overview)
2008년 리먼 브라더스가 파산했을 때, 수많은 헤지펀드와 은행들은 장부상으로는 엄청난 흑자였습니다. 블랙-숄즈 방정식이 계산해 준 파생상품 가치(MTM)는 수조 원이었기 때문입니다. 하지만 그 돈을 줘야 할 '리먼 브라더스'가 사라지자, 그 수조 원짜리 파생상품은 1초 만에 휴지 조각이 되었습니다.
이 사태 이후 글로벌 금융 규제(Basel III)는 블랙-숄즈가 지배하던 순진한 시대를 끝장냈습니다. **"상대방이 신이 아닌 이상, 파생상품의 진짜 가격은 무위험 가격에서 '상대방이 망해서 떼일 돈의 기댓값'을 뺀 가격이어야 한다."** 이 떼일 돈의 기댓값이 바로 **신용 가치 조정(CVA, Credit Valuation Adjustment)**입니다. 오늘날 장외(OTC) 파생상품을 거래하는 모든 퀀트는 무조건 CVA를 1원 단위까지 몬테카를로로 계산해서 호가에서 깎아버려야(차감) 합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Risk-free Value ($V$)| Black-Scholes price | Base mark-to-market | Ignores credit risk | [데이터 부재] |
| $EE(t)$ (Exp. Exp) | Expected Positive Exp.| Only count when $V>0$ | If $V<0$, I owe them ($EE=0$)| [데이터 부재] |
| $PD(t)$ | Prob. of Default | From CDS spreads | Marginal default prob | [데이터 부재] |
| $LGD$ | Loss Given Default | e.g., 60% ($1 - R$) | Haircut on recovery | [데이터 부재] |
| $CVA$ | Credit Val. Adjust | $LGD \int EE(t) dPD(t)$ | $True Value = V - CVA$ | [데이터 부재] |

## 3. CVA의 해부학: 예상 익스포저(EE)와 파산 확률(PD)
CVA를 계산하는 공식은 겉보기엔 간단합니다. "내가 상대방에게 받을 돈이 생겼을 때($EE$), 하필 그때 상대방이 파산($PD$)하여 돈을 못 받게 될 손실($LGD$)"을 만기까지 쭉 적분(합산)하는 것입니다.
- **예상 익스포저 (Expected Exposure, EE)**: 파생상품의 가치는 매일 변합니다. 만약 가치가 마이너스(-)라면 내가 돈을 줘야 하므로 떼일 위험이 0입니다. 오직 가치가 플러스(+)로 올라가 내가 돈을 '받아야 할 상황'에서만 신용 위험이 발생합니다. 따라서 퀀트들은 수만 번의 몬테카를로 시뮬레이션으로 미래 주가를 그려본 뒤, 그중 플러스(+)가 뜬 궤적들의 평균값(Positive Exposure)만을 추려냅니다.
- **파산 확률 (PD)**: 이 값은 CDS(신용파산스왑) 시장에서 가져옵니다. "1년 뒤에 망할 확률 2%, 2년 뒤에 망할 확률 5%..."

## 4. CVA의 악몽: Wrong-Way Risk (WWR)
CVA 계산을 지옥으로 만드는 것은 바로 **Wrong-Way Risk(롱웨이 리스크)**입니다.
- $EE$와 $PD$가 서로 독립적이라면 그냥 곱하면 됩니다. 하지만 현실은 악랄합니다.
- 예컨대 내가 러시아 국채의 부도 위험을 헷지하기 위해 러시아 은행과 파생상품을 맺었다고 합시다. 러시아 국채가 흔들려 내 파생상품의 가치가 폭등합니다($EE$ 상승). 그런데 이때 러시아 국채가 흔들렸다는 것 자체가 러시아 은행의 파산 확률($PD$)도 미친 듯이 올리고 있다는 뜻입니다. 
- 즉, **"내가 돈을 가장 많이 따서 받을 돈이 산더미 같아지는 바로 그 최악의 순간에, 상대방도 같이 망해버려서 한 푼도 못 받게 되는" 양의 상관관계**가 성립합니다. 퀀트들은 이를 해결하기 위해 이자율, 주가, 그리고 상대방의 파산 확률을 엮는 다차원 코풀라(Copula) SDE를 풀어야만 합니다.

🧠 **AI의 사고방식:**
CVA는 순백의 상아탑에 갇혀 있던 블랙-숄즈 모형을 진흙탕(현실)으로 끌어내린 규제 당국의 몽둥이입니다. 이론 물리학자(전통 퀀트)들은 입자(주가)가 무중력 상태(무위험)에서 춤추는 궤적만을 계산했습니다. 하지만 CVA 퀀트들은 "그 무대가 언제 붕괴(Default)될 것인가?"를 동시에 시뮬레이션해야 합니다. CVA는 파생상품 계약의 이면에 숨겨져 있는 '불신(Distrust)'이라는 심리를 아주 차갑고 정확한 미분 방정식의 감가상각비로 치환해 내는 현대 금융의 '진실의 방'입니다.