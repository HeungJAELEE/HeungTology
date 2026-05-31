---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-risk-management-value-at-risk-var-and-expected-shortfall-es]]'
  last_updated: '2026-05-26T07:56:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 은행장이 '우리가 내일 재수 없으면 최대 얼마까지 까먹을 수 있는가?'를 물을 때 대답하기 위해 JP모건이 발명한 VaR(Value
    at Risk)의 한계와, VaR 임계점을 넘어선 끔찍한 꼬리 구간(Tail)의 실제 평균 손실액을 측정하여 바젤 위원회의 새로운 표준이 된
    예상 부족액(Expected Shortfall, ES)
  object_type: Concept
  tier: 2
properties:
  confidence_level_es_standard: 97.5%
  confidence_level_var_typical: 99%
  es_mathematical_definition: E[Loss | Loss > VaR]
  regulatory_standard: Basel III (FRTB)
  sub_additivity_property: true_for_es_false_for_var
  va_r_coherence_status: non_coherent
  va_r_mathematical_flaw: tail_risk_neglect
semantic:
  alternative_parents: []
  expected_queries:
  - JP모건이 발명한 VaR(Value at Risk) 모형은 왜 2008년 금융위기 때 은행들의 천문학적 파산을 전혀 경고하지 못했는가?
  - 바젤(Basel) 은행 감독 위원회는 왜 리스크 측정의 글로벌 표준을 99% VaR에서 97.5% Expected Shortfall(ES)로
    강제 변경했는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_quantification
  object: Tail_Risk_and_Maximum_Loss
  predicate: measures
  subject: '[Finance] quantitative-risk-management-value-at-risk-var-and-expected-shortfall-es'
  weight: 0.9
temporal:
  valid_from: '2026-05-26T07:56:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:56:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-risk-management-value-at-risk-var-and-expected-shortfall-es]]

## 1. 개요 (Overview)
1980년대 후반, JP모건의 데니스 웨더스톤 회장은 매일 오후 4시 15분마다 거대한 보고서(4:15 Report)를 받았습니다. 그 보고서에는 전 세계 모든 트레이딩 데스크의 수만 가지 파생상품 포지션이 내포한 위험이 단 하나의 달러 숫자로 요약되어 있었습니다. "내일 하루 동안 99% 확률로 우리의 최대 손실액은 100억 원을 넘지 않습니다." 이것이 금융 리스크 관리의 혁명이자 재앙의 씨앗이 된 **VaR(Value at Risk)**의 탄생입니다.
하지만 VaR는 "1%의 확률로 재수 없는 일이 터지면 도대체 얼마나 더 크게 망하는가?"에 대해서는 침묵했습니다. 2008년 금융위기 때 이 1%의 문이 열리자 은행들은 100억 원이 아니라 1조 원을 날리고 파산했습니다. 이 참사를 겪은 퀀트들은 VaR의 눈가림을 박살 내고, 1% 꼬리 구간(Tail)에 숨어있는 악몽의 '평균' 크기를 정직하게 계산해 내는 **예상 부족액(Expected Shortfall, ES)**, 일명 조건부 VaR(CVaR)를 리스크의 새로운 글로벌 표준으로 세웠습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Confidence Level| e.g., 99% or 95% | Probability of "normal" days | $\alpha$ percentile of loss dist.| [데이터 부재] |
| VaR (99%) | Loss threshold at 99% | e.g., -\$10M | Ignores losses beyond this | [데이터 부재] |
| ES (97.5%) | Expected Shortfall | $E[L \mid L > VaR_{97.5\%}]$ | Averages the worst 2.5% | [데이터 부재] |
| Sub-additivity | $Risk(A+B) \le Risk(A) + Risk(B)$| True for ES, False for VaR | VaR penalizes diversification| [데이터 부재] |
| Historical Sim | Revaluing with past returns | No normal distribution needed | Captures fat tails in past | [데이터 부재] |

## 3. VaR의 치명적 결함 (비일관적 위험 척도)
VaR는 수학적으로 심각한 결함을 두 개 가지고 있습니다.
1. **꼬리 리스크(Tail Risk)의 방치**: A 펀드는 최대 손실이 110억 원이고, B 펀드는 최대 손실이 파산(1조 원)이라도, 상위 99% 컷오프(Cut-off) 지점의 손실액이 둘 다 100억 원이라면 VaR 엔진은 "A와 B의 리스크는 똑같다"고 평가합니다. 트레이더들은 이 맹점을 이용해 꼬리 구간에 거대한 폭탄(OTM 풋옵션 매도)을 숨겨놓고 평소에 보너스를 챙기는 '규제 차익거래'를 일삼았습니다.
2. **분산 투자(Sub-additivity)의 파괴**: 상식적으로 주식과 채권을 섞으면 리스크가 줄어들어야 합니다. 하지만 VaR 모형 하에서는 주식과 채권을 섞었을 때 전체 VaR가 각각의 VaR 합보다 오히려 커지는 미친 수학적 오류가 가끔 발생합니다. 이는 VaR가 '일관적 위험 척도(Coherent Risk Measure)'의 수학적 공리를 충족하지 못하기 때문입니다.

## 4. Expected Shortfall (ES): 바젤 III의 심판
스위스 바젤(Basel) 은행 감독 위원회는 이 사기극을 끝내기 위해 글로벌 은행 자본 규제 표준(FRTB)을 99% VaR에서 **97.5% ES (Expected Shortfall)**로 전면 교체했습니다.
- ES의 공식은 $E[Loss \mid Loss > VaR]$ 입니다. 
- 즉, "100일 중 재수가 가장 없는 최악의 2~3일(Tail)이 발생했을 때, 그 2~3일 동안 잃는 금액의 '평균값'은 얼마인가?"를 계산합니다.
- 파산(1조 원) 폭탄을 숨겨놓았던 B 펀드는, ES 검사기를 통과하는 순간 그 폭탄 값이 평균에 반영되어 리스크 수치가 수천억 원으로 폭발하게 됩니다. 더 이상 꼬리에 폭탄을 숨길 수 없게 된 것입니다.

🧠 **AI의 사고방식:**
리스크 관리 엔진은 단순히 '숫자를 재는 자(Ruler)'가 아닙니다. 그것은 트레이더들의 행동을 조종하는 '법전'입니다. VaR라는 자(Ruler)가 99% 길이까지만 잴 수 있었기 때문에, 트레이더들은 99.1%의 어둠 속에 온갖 레버리지와 파생상품 쓰레기를 은닉했습니다. ES(Expected Shortfall)로의 전환은 수학적 진보라기보다는, "네가 아무리 깊은 꼬리(Tail)에 위험을 숨기더라도 적분(Integral) 기호로 그 꼬리 끝자락까지 샅샅이 훑어서 끄집어내겠다"는 규제 당국과 퀀트들의 처절한 술래잡기(Cat and Mouse Game)의 산물입니다.