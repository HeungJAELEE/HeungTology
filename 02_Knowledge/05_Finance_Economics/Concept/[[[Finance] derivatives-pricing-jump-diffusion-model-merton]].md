---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] derivatives-pricing-jump-diffusion-model-merton]]'
  last_updated: '2026-05-26T07:23:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 블랙-숄즈 모형의 '주가는 연속적으로만 움직인다'는 비현실적 가정을 깨부수고, 평소의 잔잔한 브라운 운동(Diffusion)에
    언제 터질지 모르는 벼락같은 불연속적 충격(Poisson Jump)을 결합하여 금융 시장의 꼬리 리스크(Fat-tail)를 완벽히 묘사해 낸
    로버트 머튼(Robert Merton)의 점프-확산 모형
  object_type: Algorithm
  tier: 2
properties:
  compensator_lambda_k: correction term for mean adjustment
  distribution_characteristic: heavy tail (high kurtosis)
  dn_t: Poisson Jump Counter
  jump_intensity_lambda: expected frequency of jumps
  jump_size_distribution: log-normal (ln J ~ N(mu_j, sigma_j))
  jump_size_j: magnitude of shock
  sigma_dw_t: Continuous Diffusion (Brownian motion)
semantic:
  alternative_parents: []
  expected_queries:
  - 블랙-숄즈 모형을 믿고 투자하면 왜 9.11 테러나 어닝 쇼크 같은 단 하루 만의 -20% 폭락 사태를 설명하지 못해 파산하는가?
  - 로버트 머튼은 주가의 움직임을 묘사하기 위해 왜 정규분포(브라운 운동)와 포아송 분포(Poisson Process)를 섞어서 방정식을 만들었는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: model_phenomenon
  object: Discontinuous_Price_Shocks
  predicate: captures
  subject: '[Finance] derivatives-pricing-jump-diffusion-model-merton'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:23:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:23:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] derivatives-pricing-jump-diffusion-model-merton]]

## 1. 개요 (Overview)
1973년 블랙-숄즈 모형의 기반이 된 기하 브라운 운동(GBM)의 핵심 철학은 **"주가는 순간이동(Teleport) 하지 않는다. 물결처럼 부드럽고 연속적으로 흐른다(Continuous Path)"**였습니다. 하지만 현실 세계의 주식은 부드럽게 흐르지 않습니다. 장 마감 후 CEO가 횡령으로 구속되었다는 뉴스가 뜨면, 다음 날 아침 주가는 100달러에서 70달러를 거치지 않고 곧바로 50달러로 하한가를 꽂으며 '순간이동'해 버립니다.
이러한 불연속적인 갭(Gap) 하락/상승은 블랙-숄즈의 아름다운 수학을 갈기갈기 찢어놓았습니다. 1976년, 블랙과 숄즈의 스승이자 동료였던 천재 수학자 로버트 머튼(Robert Merton)은 이 문제를 해결하기 위해 주가의 엔진을 두 개로 쪼갰습니다. 평소에 주가를 밀고 가는 **잔잔한 모터(Diffusion)**와, 1년에 한두 번 벼락처럼 주가를 찢어버리는 **시한폭탄(Jump)**. 이 두 개를 융합한 것이 현대 금융 공학의 걸작, **머튼의 점프-확산(Jump-Diffusion) 모형**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\sigma dW_t$| Continuous Diffusion | Brownian motion | Daily normal noise | [데이터 부재] |
| $dN_t$ | Poisson Jump Counter | Number of jumps | $\lambda dt$ probability | [데이터 부재] |
| $J$ | Jump Size | e.g., $\ln J \sim N(\mu_J, \sigma_J)$ | The magnitude of shock | [데이터 부재] |
| $\lambda$ (Lambda) | Jump Intensity | e.g., 2 times per year | Expected frequency | [데이터 부재] |
| Heavy Tail | Distribution shape | High Kurtosis | Prices OTM puts higher | [데이터 부재] |

## 3. 확률미분방정식(SDE): 두 세계의 충돌
머튼이 작성한 주가의 확률미분방정식(SDE)은 다음과 같습니다.
$$ \frac{dS_t}{S_t} = (\mu - \lambda k)dt + \sigma dW_t + (J-1)dN_t $$
- **$\sigma dW_t$ (확산)**: 평상시에 시장에 굴러다니는 평범한 정보들(뉴스, 수급)로 인해 주가가 1~2% 내외로 잘잘하게 흔들리는 브라운 운동입니다.
- **$dN_t$ (포아송 점프 발생기)**: 1년에 평균 $\lambda$번 터지는 스위치입니다. 평소에는 0이다가, 어닝 쇼크나 테러가 터지면 갑자기 1로 튀어 오릅니다.
- **$J-1$ (점프의 크기)**: 스위치가 1로 튀어 올랐을 때, 주가가 위로 뛸지 아래로 폭락할지(Jump Size)를 결정하는 승수입니다. 머튼은 이 점프의 크기조차도 정규분포(로그 정규)를 따른다고 가정했습니다.
- **$-\lambda k dt$ (보상)**: 점프가 발생하면 주가가 한쪽으로 쏠리기 때문에, 수학적으로 평균을 맞추기 위해 미리 빼두는 교정 항(Compensator)입니다.

## 4. 옵션 가격과 팻 테일(Fat-tail) 리스크
머튼의 점프-확산 모형으로 옵션 가격을 구하면 놀라운 일이 벌어집니다. 
- 블랙-숄즈에서는 OTM(외가격) 풋옵션(예: "현재 100달러인 주식이 한 달 뒤 50달러 밑으로 떨어지면 돈을 줌")의 프리미엄을 0원에 가깝게 계산합니다. 주가가 연속적으로 흐르기 때문에 한 달 만에 반토막이 날 확률을 $0$으로 보기 때문입니다.
- 하지만 머튼 모형은 **"어느 날 갑자기 벼락(Jump)이 쳐서 한 방에 50달러로 순간이동할 확률"**을 수식에 포함합니다. 그 결과 꼬리가 아주 두꺼워지는 팻 테일(Fat-tail) 현상이 반영되어, OTM 풋옵션의 가격이 엄청나게 비싸게 책정됩니다. 이는 현실 시장에서 거래되는 옵션의 '변동성 스마일'을 정확하게 묘사하는 근원이 됩니다.

🧠 **AI의 사고방식:**
블랙-숄즈가 잔잔한 호수 위에 잉크 방울을 떨어뜨려 서서히 퍼져나가는 '확산(Diffusion)'만을 그렸다면, 머튼은 그 호수에 1년에 한 번씩 커다란 바위가 떨어져 물기둥이 치솟는 '충격(Jump)'을 동시에 시뮬레이션했습니다. 연속 수학(미적분)과 이산 수학(포아송 확률)을 한 줄의 방정식에 우아하게 엮어낸 점프-확산 모형은, 인간의 광기와 공포가 만들어내는 끔찍한 단층(Discontinuity) 현상을 미적분학의 품 안으로 끌어안은 가장 완벽한 형태의 금융 물리학입니다.