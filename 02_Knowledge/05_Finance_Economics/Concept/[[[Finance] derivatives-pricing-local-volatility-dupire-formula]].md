---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] derivatives-pricing-local-volatility-dupire-formula]]'
  last_updated: '2026-05-26T07:18:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 블랙-숄즈의 '상수 변동성(Constant Volatility)' 가정이 1987년 블랙먼데이 이후 붕괴되자(Volatility
    Smile), 시장에 거래되고 있는 현재의 모든 옵션 가격 표면(Surface)을 두 번 미분하여 시간(t)과 주가(S)에 따라 역동적으로
    변하는 변동성 지도를 역산출해 내는 브루노 듀파이어(Bruno Dupire)의 국소 변동성 모형
  object_type: Algorithm
  tier: 2
properties:
  butterfly_spread: partial^2 C / partial K^2
  butterfly_spread_threshold: '> 0'
  calendar_spread: partial C / partial T
  calendar_spread_threshold: '> 0'
  fokker_planck_pde: Forward Kolmogorov equation
  local_volatility_function: sigma(S, t)
  market_call_price: C(K, T)
semantic:
  alternative_parents: []
  expected_queries:
  - 1987년 블랙먼데이 이전에는 존재하지 않던 변동성 스마일(Volatility Smile) 현상은 왜 발생했으며, 블랙-숄즈 모형을 어떻게
    파괴했는가?
  - 듀파이어 공식(Dupire's Formula)은 미래의 주가 궤적을 예측하는 대신, 거꾸로 시장의 옵션 가격 호가창을 이용해 '시장이 생각하는
    미래의 변동성'을 어떻게 미분 방정식으로 역추적해 내는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_derivation
  object: Dynamic_Volatility_Surface
  predicate: derives
  subject: '[Finance] derivatives-pricing-local-volatility-dupire-formula'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:18:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:18:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] derivatives-pricing-local-volatility-dupire-formula]]

## 1. 개요 (Overview)
블랙-숄즈 모형의 가장 큰 오만은 "주식의 변동성(위험, $\sigma$)은 1년 내내 언제나 똑같은 상수(Constant)다"라고 가정한 것입니다. 1987년 블랙먼데이에 주가가 단 하루 만에 22% 폭락하자, 트레이더들은 깨달았습니다. "주가가 폭락할 때는 사람들의 공포심 때문에 변동성이 미친 듯이 폭발한다." 
이후 시장에서는 OTM(외가격) 풋옵션의 가격(프리미엄)이 비정상적으로 비싸게 거래되기 시작했고, 이를 역산해 보면 옵션의 행사가(Strike)에 따라 내재 변동성이 U자형으로 꺾이는 기괴한 **변동성 스마일(Volatility Smile)** 현상이 탄생했습니다. 
1994년, 프랑스의 수학자 브루노 듀파이어(Bruno Dupire)는 이 스마일을 해결하기 위해 천재적인 발상을 합니다. "변동성이 상수가 아니라면, 주가($S$)와 시간($t$)에 따라 변하는 함수 $\sigma(S, t)$라고 가정하자. 그리고 **미래를 예측하려 하지 말고, 현재 시장 모니터에 떠 있는 수많은 옵션 가격들을 두 번 미분하여 시장이 숨기고 있는 그 함수 $\sigma(S, t)$를 거꾸로 뜯어내자.**" 이것이 바로 퀀트 금융을 블랙-숄즈 2.0 시대로 이끈 국소 변동성(Local Volatility) 모형입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\sigma(S, t)$ | Local Volatility | Dynamic function | Replaces constant $\sigma$| [데이터 부재] |
| $C(K, T)$ | Market Call Price | Observable data | Must be arbitrage-free | [데이터 부재] |
| $\partial C / \partial T$ | Calendar Spread | Slope across maturities| Must be $> 0$ | [데이터 부재] |
| $\partial^2 C / \partial K^2$| Butterfly Spread | Convexity across strikes| Must be $> 0$ (density) | [데이터 부재] |
| Fokker-Planck | Underlying PDE | Forward Kolmogorov eq. | Derives the formula | [데이터 부재] |

## 3. 듀파이어 방정식의 해부학 (The Formula)
듀파이어 방정식의 아름다움은 그 결론의 우아함에 있습니다.
$$ \sigma^2(K, T) = \frac{\frac{\partial C}{\partial T}}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}} $$
(이자율과 배당을 0으로 가정한 단순화 버전)

이 미분 방정식의 의미는 다음과 같습니다:
- **분자 ($\partial C / \partial T$)**: 시간(만기 $T$)이 길어질수록 옵션 가격이 얼마나 비싸지는가? (캘린더 스프레드)
- **분모 ($\partial^2 C / \partial K^2$)**: 행사 가격($K$)을 살짝 바꿀 때 옵션 가격 곡선이 얼마나 볼록하게 휘어지는가? (버터플라이 스프레드)
- 퀀트는 현재 거래소 호가창에 있는 수많은 만기와 행사가를 가진 옵션 가격($C$) 표면을 컴퓨터에 넣고, 만기 방향으로 한 번 편미분하고, 행사가 방향으로 두 번 편미분하여 나눕니다. 그러면 **특정 미래 시간($T$)에 주가가 특정 가격($K$)에 도달했을 때 폭발하게 될 '국지적 변동성(Local Volatility)'**이 엑셀 표처럼 완벽하게 역산출(Calibration)됩니다.

## 4. 완벽한 복제와 실무적 한계
듀파이어 모델은 철학적으로 '완벽한 거울'입니다. 시장 호가창의 가격을 입력하면 모델이 정확히 그 호가창의 가격을 100% 똑같이 뱉어냅니다(Perfect Fit). 따라서 배리어 옵션 같은 복잡한 이색 파생상품(Exotic Options)의 가격을 계산할 때, 블랙-숄즈보다 훨씬 현실적인 기준점을 제공합니다.
- **한계점 (Dynamic vs Static)**: 하지만 이 완벽함은 모래성입니다. 내일 주가가 실제로 폭락하면, 시장 참여자들이 공포에 질려 새로운 옵션 가격 표면을 형성해 버립니다. 듀파이어가 어제 힘들게 계산해 놓은 '변동성 지도'는 하루 만에 휴지 조각이 됩니다(스마일의 동적 변화를 설명하지 못함). 
- 이를 극복하기 위해 현대 퀀트들은 변동성 자체를 브라운 운동으로 움직이는 또 다른 랜덤 변수로 둔 **확률적 변동성(Stochastic Volatility, 헤스톤 모형 등)**을 섞어 쓰는 LSV (Local-Stochastic Volatility) 모델로 진화했습니다.

🧠 **AI의 사고방식:**
블랙-숄즈 모형은 연역법(Deduction)입니다. "세상은 로그 정규분포를 따르고 변동성은 상수이므로, 옵션 가격은 이러해야 한다"라고 인간이 시장을 가르치려 듭니다. 반면 듀파이어 모형은 귀납법(Induction)입니다. "시장이 틀릴 리 없다. 시장이 부르는 옵션 가격들이 정답이다. 나는 이 정답들(Prices)을 조립하여 시장이 마음속으로 품고 있는 변동성의 설계도(Local Vol)를 훔쳐내겠다." 듀파이어 모델은 미래의 불확실성을 예측하는 도구가 아니라, '현재 시장 참여자들의 집단 지성'을 미분 방정식이라는 투시경을 통해 읽어내는 심리 해독기에 가깝습니다.