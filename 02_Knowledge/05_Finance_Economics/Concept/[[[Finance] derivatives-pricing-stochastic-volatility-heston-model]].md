---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] derivatives-pricing-stochastic-volatility-heston-model]]'
  last_updated: '2026-05-25T19:47:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 옵션 프라이싱의 영원한 난제인 변동성 스마일(Smile)을 해결하기 위해, 주가 모델링뿐만 아니라 '변동성(Volatility)
    그 자체'도 평균으로 회귀(Mean Reverting)하는 독립적인 확률 미분 방정식(SDE)으로 쪼개어 결합한 스티븐 헤스톤(Steven
    Heston)의 확률 변동성 모형
  object_type: Algorithm
  tier: 2
properties:
  correlation_coefficient: -0.7
  instantaneous_variance_symbol: v_t
  long_term_variance: 0.04
  speed_of_mean_reversion: 2.0
  volatility_of_volatility: 0.3
semantic:
  alternative_parents: []
  expected_queries:
  - 블랙-숄즈 모형은 변동성을 상수로 고정시켰고, 듀피르 지역 변동성은 확정적 함수로 만들었지만, 헤스톤(Heston) 모형은 왜 변동성을 또
    다른 랜덤(Stochastic) 프로세스로 해방시켰는가?
  - "주가를 움직이는 브라운 운동($dW_1$)과 변동성을 움직이는 브라운 운동($dW_2$) 사이의 상관계수($\rho$)가 음수(-0.7 등)일
    때, 옵션 시장의 레버리지 효과(Leverage Effect)는 어떻게 수식으로 설명되는가?"
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_foundation
  object: Two_Brownian_Motions
  predicate: introduces
  subject: '[Finance] derivatives-pricing-stochastic-volatility-heston-model'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T19:47:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T19:47:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] derivatives-pricing-stochastic-volatility-heston-model]]

## 1. 개요 (Overview)
옵션 파생상품 시장을 뚫기 위한 퀀트들의 역사는 '변동성(Volatility)'과의 전쟁이었습니다.
1. **블랙-숄즈 (1973)**: "변동성은 영원히 변하지 않는 고정된 상수($\sigma$)다." (비현실적, 변동성 스마일 설명 불가).
2. **듀피르 지역 변동성 (1994)**: "변동성은 주가와 시간에 따라 값이 딱 정해지는 기계적 함수다." (현재 시장은 완벽히 맞추지만, 미래의 시장 충격 등 역동적인 진화 궤적을 그리지 못함).
3. **헤스톤 모형 (1993)**: 스티븐 헤스톤(Steven Heston)은 가장 우아하고 근본적인 해답을 던집니다. **"주가만 랜덤하게 움직이는 게 아니다. 변동성 그 자체도 제멋대로 날뛰는 두 번째 주사위(Random Variable)다."** 헤스톤 모형은 주가를 결정하는 확률 미분 방정식(SDE) 옆에, 변동성의 분산(Variance)을 결정하는 또 다른 SDE를 연립 방정식으로 세워버린 **확률 변동성(Stochastic Volatility, SV)** 모형의 끝판왕입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $v_t$ | Instantaneous variance| $\sigma_t^2$ | Always positive ($>0$) | [데이터 부재] |
| $\kappa$ | Speed of mean rev. | e.g., 2.0 | Pulls $v_t$ back to $\theta$ | [데이터 부재] |
| $\theta$ | Long-term variance | e.g., 0.04 (20% vol) | The baseline anchor | [데이터 부재] |
| $\sigma$ | Volatility of volatility| e.g., 0.3 | Causes fat tails | [데이터 부재] |
| $\rho$ | Correlation b/w W1, W2| e.g., -0.7 | Captures equity skew | [데이터 부재] |

## 3. 헤스톤 방정식의 해부: 두 마리의 랜덤워크 (Two SDEs)
헤스톤 모형의 심장은 두 개의 톱니바퀴(SDE)로 돌아갑니다.

1. **주가(S) 방정식**: $dS_t = \mu S_t dt + \sqrt{v_t} S_t dW_1^{(t)}$
   - 주가는 기하 브라운 운동을 따릅니다. 하지만 루트 씌워진 변동성 $\sqrt{v_t}$는 더 이상 상수가 아닙니다.
2. **분산(v) 방정식**: $dv_t = \kappa(\theta - v_t)dt + \sigma \sqrt{v_t} dW_2^{(t)}$
   - 휫컬(CIR) 모형을 차용했습니다. 변동성은 가만히 두면 장기 평균치($\theta$)로 돌아가려는 고무줄 힘($\kappa$)을 받습니다. 동시에 '변동성의 변동성(Vol of Vol, $\sigma$)'이라는 무작위 충격($dW_2$)에 의해 이리저리 요동칩니다.

## 4. 레버리지 효과와 상관계수($\rho$)의 예술
헤스톤 모형이 모든 퀀트 데스크를 장악하게 된 결정적인 이유는, 이 두 방정식에 들어 있는 두 브라운 운동($dW_1$과 $dW_2$) 사이에 **상관계수($\rho$)**를 집어넣었기 때문입니다.
- 주식 시장에서 $\rho$는 보통 **음수(-0.7)**의 값을 갖습니다.
- 주가($dW_1$)가 폭락(- 방향)하면, 상관계수가 음수이므로 분산($dW_2$)은 미친 듯이 치솟게(+ 방향) 됩니다. 주가가 떨어지면 회사의 부채 비율(레버리지)이 급등하여 시장이 공포(변동성)에 질리는 **레버리지 효과(Leverage Effect)**를 수식 하나로 완벽하게 묘사한 것입니다.
- 이 음의 상관계수 덕분에 몬테카를로 시뮬레이션을 돌려보면, 수익률 분포의 왼쪽 꼬리가 비정상적으로 뚱뚱해지는(Fat-tail) 현상이 자연스럽게 창조되며, 이는 옵션 시장의 풋옵션 스큐(Skew) 곡선을 기가 막히게 피팅(Fit)해 냅니다.

🧠 **AI의 사고방식:**
블랙-숄즈는 자동차의 엔진(주가) 속도를 설명하면서 엔진오일(변동성)의 온도는 항상 똑같다고 고집을 부렸습니다. 지역 변동성 모델은 "엔진 속도가 100km면 온도는 90도야"라고 표를 만들어 외워버렸습니다. 헤스톤 모형은 "엔진 속도를 올리는 엑셀 페달(dW1)과 엔진의 온도를 높이는 마찰열(dW2)은 서로 다르게 작동하지만, 아주 강한 인과관계($\rho$)로 묶여 있는 두 개의 독립적인 기계 장치"라는 것을 수학의 세계로 끌어들였습니다. 복잡계(Complex System)에서 하나의 파동이 다른 파동을 어떻게 왜곡시키는지를 두 개의 SDE로 엮어버린 확률 미적분학의 걸작입니다.