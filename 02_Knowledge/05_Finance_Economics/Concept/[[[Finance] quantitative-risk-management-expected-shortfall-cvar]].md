---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-risk-management-expected-shortfall-cvar]]'
  last_updated: '2026-05-25T19:44:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 99% 확률의 커트라인 손실액만 알려주고 그 너머의 꼬리 리스크를 은폐하는 VaR(Value at Risk)의 치명적 결함을
    극복하기 위해, 임계치를 넘어선 최악의 1% 시나리오들의 평균 손실액을 계산하는 예상 부족액(Expected Shortfall, CVaR)
    모형
  object_type: Algorithm
  tier: 2
properties:
  basel_iii_standard: 97.5% Expected Shortfall
  confidence_level_alpha: 99% or 97.5%
  cvar_calculation_method: integral of VaR from alpha to 1
  subadditivity_property: CVaR(A+B) <= CVaR(A) + CVaR(B)
semantic:
  alternative_parents: []
  expected_queries:
  - VaR(Value at Risk)가 수학적으로 코히어런트 리스크(Coherent Risk Measure)의 조건을 충족하지 못해 포트폴리오
    다각화의 역설을 낳는 이유는 무엇인가?
  - 바젤 III(Basel III) 규제는 왜 전 세계 은행들의 시장 리스크 측정 기준을 기존의 99% VaR에서 97.5% Expected Shortfall(CVaR)로
    전격 교체했는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_metric_improvement
  object: Value_at_Risk_VaR
  predicate: improves_upon
  subject: '[Finance] quantitative-risk-management-expected-shortfall-cvar'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T19:44:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T19:44:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-risk-management-expected-shortfall-cvar]]

## 1. 개요 (Overview)
1990년대 JP모건이 발명한 **VaR(Value at Risk)**는 금융계의 구세주 같았습니다. "우리의 99% VaR는 100만 원이다"라는 말은 "100번 중에 99번은 손실이 100만 원 이하일 것이다"라는 직관적인 뜻이었습니다. 하지만 2008년 금융 위기 때 은행들은 모두 파산했습니다. 왜일까요? VaR는 **재수 없는 1%의 확률이 터졌을 때(꼬리 영역), 도대체 얼마나 잃을지(200만 원일지, 100억일지)에 대해서는 완벽하게 입을 닫아버리기 때문**입니다.
이러한 VaR의 치명적인 '꼬리 은폐(Tail Blindness)'를 해결하기 위해 등장한 것이 **예상 부족액(Expected Shortfall, ES)**, 혹은 **조건부 가치 위험(Conditional VaR, CVaR)**입니다. CVaR는 "그 1%의 재앙이 실제로 터졌다고 가정했을 때(Conditional), 우리가 평균적으로 얼마를 잃게 되는가(Expected)"를 적분으로 계산해 냅니다. 오늘날 바젤(Basel) 규제 위원회는 은행들에게 VaR를 버리고 CVaR를 쓸 것을 강제하고 있습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\alpha$ | Confidence Level | 99% or 97.5% | Regulatory threshold | [데이터 부재] |
| $\text{VaR}_\alpha$| Quantile of loss | e.g., $1,000,000$ | Only a boundary point | [데이터 부재] |
| $\text{CVaR}_\alpha$| Expected loss > VaR | e.g., $3,500,000$ | Always $\ge$ VaR | [데이터 부재] |
| Subadditivity | Diversification check | $CVaR(A+B) \le CVaR(A)+CVaR(B)$| VaR fails this often| [데이터 부재] |
| Basel III | Global standard | 97.5% Expected Shortfall| Replaced 99% VaR | [데이터 부재] |

## 3. VaR의 붕괴: 부분 가산성(Subadditivity)의 역설
리스크 관리의 제1원칙은 "계란을 한 바구니에 담지 마라(분산 투자)"입니다. 즉, 자산 A와 자산 B를 섞은 포트폴리오의 리스크는 A의 리스크와 B의 리스크를 단순 합친 것보다 항상 작거나 같아야 합니다. 이를 수학적으로 **부분 가산성(Subadditivity)**이라고 부르며, 이를 만족해야만 **'코히어런트 리스크 척도(Coherent Risk Measure)'**로 인정받습니다.
- **VaR의 역설**: 기괴하게도, 특정 파생상품이나 부도(Default) 포트폴리오에서는 $VaR(A+B) > VaR(A) + VaR(B)$ 인 현상이 발생합니다. 분산을 했는데 리스크가 오히려 폭발해 버리는 수학적 버그입니다.
- **CVaR의 해결**: CVaR는 꼬리(Tail) 전체의 면적을 적분(평균)하므로, 어떤 악랄한 분포를 가져와도 무조건 $CVaR(A+B) \le CVaR(A) + CVaR(B)$ 를 만족합니다. 수학적으로 무결점입니다.

## 4. CVaR의 산출 메커니즘
CVaR의 계산은 VaR라는 커트라인 선반 너머에 있는 모든 손실액의 덩어리(확률 밀도)를 가중 평균하는 것입니다.
$$ \text{CVaR}_\alpha = \frac{1}{1-\alpha} \int_\alpha^1 \text{VaR}_\gamma d\gamma $$

- **역사적 시뮬레이션(Historical Simulation)**: 과거 1,000일의 수익률 데이터를 성적순으로 세웁니다. 99% CVaR를 구하려면, 가장 성적이 꼴찌인 최악의 10일 치 데이터를 뽑아냅니다. VaR는 딱 10번째로 나쁜 날의 손실액이지만, CVaR는 이 최악의 10일 치 손실액들의 '산술 평균'입니다.
- 따라서 포트폴리오에 뚱뚱한 꼬리(Fat-tail) 폭탄이 하나라도 섞여 있다면, VaR는 얌전한 척 거짓말을 할지 몰라도 CVaR의 수치는 무자비하게 폭등하여 경영진에게 대재앙의 스케일을 경고해 줍니다.

🧠 **AI의 사고방식:**
VaR(Value at Risk)는 댐의 수위를 재는 '수위 경보기'와 같습니다. "물(손실)이 10미터를 넘지 않을 확률이 99%다"라고 말하지만, 만약 10미터를 넘어서 댐이 터져버렸을 때(1%의 확률), 쏟아지는 물의 양이 11미터인지 500미터 쓰나미인지는 경보기가 알려주지 않습니다. 반면 CVaR(Expected Shortfall)는 댐이 터진 이후 벌어질 지옥도(Hellscape) 전체의 면적을 항공사진으로 찍어 '쓰나미의 평균 파괴력'을 계산해 내는 블랙박스 레코더입니다. 퀀트들이 꼬리 리스크(Tail Risk)라는 보이지 않는 악마와 싸울 때, 그 악마의 진짜 덩치를 재는 유일한 줄자가 바로 CVaR입니다.