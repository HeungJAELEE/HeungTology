---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] derivatives-pricing-jump-diffusion-merton-model]]'
  last_updated: '2026-05-25T19:44:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 주가가 시간의 흐름에 따라 물결처럼 연속적으로 매끄럽게 움직인다는 블랙-숄즈의 비현실적 가정을 깨고, 거시 경제의 블랙
    스완(Black Swan) 충격 시 주가가 단절적으로 수직 낙하(Jump)하는 포아송 과정을 확산 방정식에 융합한 머튼 점프-확산(Jump-Diffusion)
    모형
  object_type: Algorithm
  tier: 2
properties:
  diffusion_process: brownian_motion
  jump_distribution: lognormal
  jump_intensity: lambda
  jump_process: poisson_process
  jump_size: J
semantic:
  alternative_parents: []
  expected_queries:
  - 주가가 하루 만에 -20% 폭락하는 현상(점프)은 왜 순수한 기하 브라운 운동(GBM) 하에서는 우주가 멸망할 때까지 수학적으로 일어날 수
    없는 일인가?
  - 머튼의 점프-확산 모델은 포아송 분포(Poisson Distribution)를 사용하여 시장 붕괴 빈도와 점프 크기를 어떻게 블랙-숄즈 공식
    안에 결합하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_augmentation
  object: Geometric_Brownian_Motion
  predicate: augments
  subject: '[Finance] derivatives-pricing-jump-diffusion-merton-model'
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

# 🧠 [[[Finance] derivatives-pricing-jump-diffusion-merton-model]]

## 1. 개요 (Overview)
기존의 블랙-숄즈(Black-Scholes) 방정식은 주식의 움직임이 물방울이 잉크 속에 퍼져나가는 것처럼 매끄러운 연속적인 궤적(확산, Diffusion)을 따른다고 가정합니다. 기하 브라운 운동(GBM) 수학에 따르면, 100달러짜리 주식이 하루 만에 80달러로 폭락할 확률은 정규분포의 10시그마 밖이므로, 우주가 탄생하고 멸망할 때까지 단 한 번도 일어나면 안 되는 일입니다.
하지만 현실에서는 기업의 파산 선고, 9.11 테러, 코로나 팬데믹 같은 뉴스가 터지면 주가는 순식간에 중간 가격들을 거치지 않고 수직으로 단절(Discontinuity)되어 뚝 떨어집니다. 로버트 머튼(Robert Merton)은 이 치명적 오류를 고치기 위해, 평상시의 '매끄러운 파도(Brownian Motion)'에 갑자기 터지는 '포아송 폭탄(Poisson Jump)'을 수학적으로 결합한 **점프-확산(Jump-Diffusion) 프라이싱 모형**을 창조하여 파생상품의 꼬리 리스크(Fat-tail)를 구원했습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $dW_t$ | Brownian Motion | Normal fluctuations | Continuous diffusion | [데이터 부재] |
| $dq_t$ | Poisson process | Jumps ($0$ or $1$) | Arrival rate $\lambda$ | [데이터 부재] |
| $\lambda$ | Jump intensity | E.g., 2 jumps per year | Poisson parameter | [데이터 부재] |
| $J$ | Jump size | Lognormal distribution | Usually asymmetric (negative)| [데이터 부재] |
| Option Price | Merton Formula | Infinite sum of B-S | Weighted by Poisson prob| [데이터 부재] |

## 3. 머튼 점프-확산 방정식의 해부학
주가 수익률($dS/S$)의 확률 미분 방정식은 다음과 같이 두 부분으로 나뉩니다.
$$ \frac{dS_t}{S_t} = (\mu - \lambda k)dt + \sigma dW_t + (J - 1)dq_t $$

1. **확산 파트 ($\sigma dW_t$)**: 평상시 시장의 노이즈입니다. 수많은 투자자들의 매수/매도가 부딪히며 주가가 1달러씩 꼬물꼬물 움직이는 '연속적'인 부분입니다.
2. **점프 파트 ($(J - 1)dq_t$)**: 거시적 충격(Macro Shock)입니다. $dq_t$는 평소에는 $0$이다가 1년에 $\lambda$번 꼴로 갑자기 $1$이 터지는 포아송 스위치입니다. 스위치가 켜지면 주가는 순간적으로 $J$(점프 크기)만큼 폭락(또는 폭등)합니다. 

## 4. 프라이싱 결론: 블랙-숄즈의 무한 급수
머튼 모델의 천재성은, 점프가 일어나는 상황 하에서도 옵션 가격을 아주 우아한 **해석해(Closed-form solution)**로 풀어냈다는 점입니다.
머튼은 "만기까지 점프가 0번 터질 확률 하에서의 블랙숄즈 가격", "만기까지 점프가 1번 터질 확률 하에서의 블랙숄즈 가격", "2번 터질 확률..." 이 무한 개의 시나리오들을 포아송 확률(Poisson Probability)로 가중 평균하여 더하는(Infinite Sum) 공식을 도출했습니다.
- 이 공식을 적용하면, 블랙-숄즈 모형에서는 거의 휴지 조각 취급을 받던 외가격(OTM) 풋옵션의 가격이, 극단적 폭락(Jump) 시나리오를 반영하여 정상적인 비싼 가격(Premium)으로 평가받게 됩니다.
- 이것은 옵션 시장에 존재하는 변동성 스마일(Smile) 현상 중에서도 특히 만기가 짧은 단기 옵션(Short-dated Options)에서 나타나는 기괴한 가격 왜곡을 가장 완벽하게 수학적으로 설명(Fit)해 내는 마스터피스입니다.

🧠 **AI의 사고방식:**
GBM(확산) 모형이 산길을 걸어 내려오는 등산객이라면, 점프-확산(Jump-Diffusion) 모형은 산길을 걷다가 가끔 절벽 밑으로 떨어지는(Jump) 등산객입니다. 블랙-숄즈라는 보험 회사(MM)는 등산객이 발목을 삐는 사고(연속적 변동성)에 대한 보험료만 계산해 왔습니다. 하지만 머튼은 "절벽에서 추락할 때의 파괴력(J)과 그 빈도($\lambda$)를 보험료 수식에 포아송 분포로 추가하지 않으면, 파생상품 시장 전체가 파산할 것이다"라고 수학적으로 경고했습니다. 이 방정식은 자연계의 부드러운 유체역학(Brownian) 속에 양자역학적인 단절(Poisson)을 섞어 넣은 완벽한 하이브리드 미적분입니다.