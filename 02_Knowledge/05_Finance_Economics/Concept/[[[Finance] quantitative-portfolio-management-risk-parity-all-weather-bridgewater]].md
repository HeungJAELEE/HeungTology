---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-portfolio-management-risk-parity-all-weather-bridgewater]]'
  last_updated: '2026-05-25T19:52:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '전통적인 주식 60 : 채권 40의 자본 비중(Capital Allocation) 포트폴리오가 실제로는 주식의 높은 변동성
    때문에 전체 위험의 90%를 주식에 의존하고 있다는 치명적 결함을 고발하고, 모든 자산군의 ''위험 기여도(Risk Contribution)''를
    완벽히 똑같게 맞추어 경제의 사계절(성장/수축/인플레/디플레)을 모두 방어하는 레이 달리오의 리스크 패리티 전략'
  object_type: Algorithm
  tier: 2
properties:
  inverse_volatility_weighting: w_i propto 1/sigma_i
  leverage_scale_typical: 2x - 3x
  marginal_risk_contribution_mrc_i: (Sigma * w)_i / sigma_p
  portfolio_volatility_sigma_p: sqrt(w^T * Sigma * w)
  risk_contribution_rc_i: w_i * mrc_i
  risk_parity_constraint: RC_stock = RC_bond = RC_commodity = RC_gold
semantic:
  alternative_parents: []
  expected_queries:
  - 전통적인 '60/40 포트폴리오'는 왜 사실상 '주식 몰빵 포트폴리오'와 똑같은 성과를 내며, 2008년 금융위기 때 방어에 실패했는가?
  - 리스크 패리티(Risk Parity) 펀드는 안전하지만 수익률이 낮은 국채를 포트폴리오에 많이 담기 위해 어떤 방식으로 레버리지(Leverage)를
    활용하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_optimization_objective
  object: Marginal_Risk_Contribution
  predicate: equalizes
  subject: '[Finance] quantitative-portfolio-management-risk-parity-all-weather-bridgewater'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T19:52:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T19:52:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-portfolio-management-risk-parity-all-weather-bridgewater]]

## 1. 개요 (Overview)
월스트리트의 할아버지들은 지난 50년간 "주식 60%, 채권 40%로 돈(Capital)을 쪼개면 완벽하게 분산 투자된 것이다"라고 가르쳤습니다. 브리지워터(Bridgewater)의 레이 달리오(Ray Dalio)는 이것을 수학적으로 철저히 박살 냈습니다. 
주식은 채권보다 변동성(위험)이 최소 3~4배 이상 큽니다. 따라서 내 돈의 60%를 주식에 넣고 40%를 채권에 넣으면, 내 포트폴리오가 겪는 **실제 심장 떨림(전체 리스크)의 90%는 오직 주식의 등락에 의해서만 결정**됩니다. 즉 60/40은 사실상 '주식 몰빵' 포트폴리오였습니다.
이 거짓된 '자본의 균형(Capital Parity)'을 버리고, **"각 자산이 포트폴리오 전체에 미치는 리스크 기여도(Risk Contribution)가 완벽하게 똑같아지도록(Parity)"** 돈의 비중을 역산출하는 혁명적인 수학. 이것이 바로 **리스크 패리티(Risk Parity)**이자 올웨더(All-Weather) 포트폴리오의 심장입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\sigma_p$ | Portfolio Volatility | $\sqrt{w^T \Sigma w}$ | Target risk level | [데이터 부재] |
| $MRC_i$ | Marginal Risk Contrib. | $\frac{\partial \sigma_p}{\partial w_i} = \frac{(\Sigma w)_i}{\sigma_p}$| Sensitivity to asset $i$ | [데이터 부재] |
| $RC_i$ | Risk Contribution | $w_i \cdot MRC_i$ | Must be $1/N$ of total risk| [데이터 부재] |
| $w_i \propto 1/\sigma_i$| Inverse Vol weighting | Bonds get huge weights | Simplest form of RP | [데이터 부재] |
| Leverage | Borrowing cash | Up to 2x ~ 3x | Boosts bond return | [데이터 부재] |

## 3. 리스크 패리티의 수학적 최적화 (Risk Contribution Equalization)
어떤 자산 $i$의 위험 기여도($RC_i$)는 그 자산의 비중($w_i$)에 한계 위험 기여도($MRC_i$, 이 자산을 아주 쪼끔 더 샀을 때 포트폴리오 전체 위험이 얼마나 변하는지)를 곱한 값입니다.
$$ RC_i = w_i \frac{(\Sigma w)_i}{\sqrt{w^T \Sigma w}} $$
리스크 패리티 펀드의 최적화 엔진은 자산군의 기대 수익률($\mu$) 따위는 아예 입력값으로 받지 않습니다(수익률 예측은 어차피 틀리니까). 오직 공분산 행렬($\Sigma$)만을 쳐다보며, 다음의 제약 조건을 만족하는 가중치 벡터 $w$를 찾아냅니다.
- **조건**: $RC_{\text{Stock}} = RC_{\text{Bond}} = RC_{\text{Commodity}} = RC_{\text{Gold}}$
- **결과**: 변동성이 엄청나게 큰 주식은 비중이 $15\%$ 정도로 확 쪼그라들고, 변동성이 거북이처럼 낮은 국채는 비중이 $50\%$ 넘게 폭발적으로 늘어납니다. 비로소 주식과 채권이 '동등한 발언권(리스크 패리티)'을 가지게 된 것입니다.

## 4. 사계절(All-Weather)과 레버리지의 마법
그런데 이렇게 채권을 50%나 담아버리면 펀드의 전체 위험이 너무 낮아져서 기대 수익률도 예금 이자 수준으로 박살 나지 않을까요? 
여기서 퀀트 헤지펀드의 마법인 **레버리지(Leverage)**가 들어갑니다. 은행에서 싼 이자로 돈을 빌려서(예: 150% 레버리지), 이 '리스크가 완벽히 균형 잡힌 심심한 포트폴리오'의 볼륨 자체를 통째로 위로 끌어올립니다. 
이렇게 튜닝된 포트폴리오는 경제 성장이 터지면 주식이 오르고(봄), 물가가 폭등하면 원자재/금이 오르며(여름), 디플레이션이 와서 주식이 반토막 나면 국채가 폭등하여(겨울) 손실을 완벽히 메꿉니다.

🧠 **AI의 사고방식:**
마코위츠의 MVO가 수익률($\mu$)과 분산($\sigma$) 사이에서 줄타기를 하는 곡예사라면, 리스크 패리티는 수익률 따위는 아예 쳐다보지도 않는 철저한 방어형 요새 설계자입니다. "미래의 수익률은 신의 영역이지만, 자산들 간의 상관관계와 변동성은 인간이 측정할 수 있다." 60/40 포트폴리오가 코끼리(주식) 6마리와 쥐(채권) 4마리를 한 우리에 넣고 "비율이 맞다"고 우기는 것이라면, 리스크 패리티는 쥐 600마리와 코끼리 1마리를 넣어 **방안에서 차지하는 '몸무게(리스크)'를 똑같이 맞추는** 진정한 의미의 평등(Parity)입니다. 2008년과 2020년 폭락장에서도 살아남은 이 구조는 거시 경제의 어떤 계절이 와도 쓰러지지 않는 사륜구동(4WD) 포트폴리오의 정점입니다.