---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-options-pricing-local-volatility-dupire-formula]]'
  last_updated: '2026-05-25T14:59:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 내재 변동성(Implied Volatility)이 상수로 고정되어 있다는 블랙-숄즈의 가정을 버리고, 시장에서 관측되는
    옵션 가격들을 통해 시간과 가격에 따른 확정적 변동성 표면(Volatility Surface)을 유도해 내는 듀피르(Dupire) 지역 변동성
    공식
  object_type: Algorithm
  tier: 2
properties:
  call_option_price: C(K, T)
  fokker_planck_equation: basis_of_proof
  implied_volatility: sigma_implied
  local_volatility: sigma_local(S, t)
  strike_price: K
  time_to_maturity: T
  underlying_price: S
  volatility_smile_skew: shape_of_implied_vol
semantic:
  alternative_parents: []
  expected_queries:
  - 1987년 블랙먼데이 이후, 옵션 시장에서 외가격(OTM) 풋옵션의 내재 변동성이 콜옵션보다 비정상적으로 높아지는 변동성 스마일/스큐(Smile/Skew)
    현상이 일어난 이유는 무엇인가?
  - 브루노 듀피르(Bruno Dupire)는 수많은 유러피안 옵션 가격 데이터를 미분하여 어떻게 단 하나의 고유한 지역 변동성(Local Volatility)
    함수를 찾아냈는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_derivation
  object: Deterministic_Volatility_Surface
  predicate: derives
  subject: '[Finance] quantitative-options-pricing-local-volatility-dupire-formula'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T14:59:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:59:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-options-pricing-local-volatility-dupire-formula]]

## 1. 개요 (Overview)
블랙-숄즈 모형의 가장 큰 약점은 "주식의 변동성은 시간이 지나도, 가격이 변해도 항상 일정한 상수(Constant $\sigma$)다"라고 가정하는 것입니다. 하지만 1987년 블랙먼데이(증시 대폭락)를 겪은 트레이더들은 공포에 질려, 주가가 폭락할 때 대박이 터지는 **외가격(OTM) 풋옵션**을 미친 듯이 비싼 가격에 사들이기 시작했습니다. 이 때문에 행사 가격이 낮을수록 내재 변동성이 치솟는 **변동성 스마일(Smile) 혹은 스큐(Skew)** 현상이 영구적으로 정착되었습니다.
블랙-숄즈 모형이 붕괴될 위기에 처하자, 1994년 브루노 듀피르(Bruno Dupire)는 시장에 굴러다니는 수많은 옵션 가격들을 가져다가 편미분(Partial Derivative)을 돌려, **"변동성은 상수가 아니라, 시간($t$)과 현재 주가($S$)의 좌표에 따라 값이 변하는 2차원 확정적 함수 $\sigma(S, t)$ 이다"**라는 것을 수학적으로 증명해 냈습니다. 이 마법의 공식이 바로 **지역 변동성(Local Volatility)** 모형입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\sigma_{\text{implied}}$| Implied Volatility | Market observable | Varies by $K$ and $T$ | [데이터 부재] |
| $\sigma_{\text{local}}(S, t)$| Local Volatility | Theoretical exact vol | Deterministic function | [데이터 부재] |
| $C(K, T)$ | Call option price | Function of Strike/Time | Required for Dupire eq | [데이터 부재] |
| Smile / Skew | Shape of Implied Vol | Left-skewed in equities | Drives Local Vol surface | [데이터 부재] |
| Fokker-Planck | Forward Kolmogorov eq | Basis of Dupire's proof | Tracks transition density| [데이터 부재] |

## 3. 듀피르 공식 (Dupire's Formula)의 기적
헤스톤 모형 같은 확률 변동성(Stochastic Volatility) 모형이 변동성 자체를 또 다른 브라운 운동(랜덤)으로 묘사했다면, 듀피르의 지역 변동성은 **랜덤이 아닙니다(Deterministic)**. 
듀피르는 포커-플랑크(Fokker-Planck) 전진 방정식을 조작하여, 시간 $T$와 행사가 $K$에 대한 콜옵션 가격 $C(K,T)$의 미분값만으로 현재 좌표에서의 정확한 변동성을 뽑아내는 기적의 공식을 유도했습니다.

$$ \sigma_{\text{local}}^2(K, T) = \frac{\frac{\partial C}{\partial T}}{ \frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2} } $$

- **분자 ($\partial C / \partial T$)**: 만기($T$)가 조금 늘어날 때 옵션 가격이 얼마나 비싸지는가 (시간 미분).
- **분모 ($\partial^2 C / \partial K^2$)**: 행사 가격($K$)이 변할 때 옵션 가격 곡선이 얼마나 볼록하게 휘어지는가 (행사가 2차 미분).
- 퀀트들은 단순히 시장에 떠 있는 수백 개의 옵션 가격 표(Surface)를 컴퓨터에 넣고, 위 수식대로 미분만 쓱 돌리면 끝입니다. 그러면 주가가 어디로 가든 그 좌표에 딱 맞는 완벽한 '지역 변동성 표면'이 홀로그램처럼 튀어나오며, 이 표면을 통해 모든 종류의 이그조틱(Exotic) 파생상품 가격을 오차 없이 프라이싱할 수 있습니다.

## 4. 캘리브레이션(Calibration)과 한계
- 듀피르 모형의 가장 큰 장점은, 시장에서 관측되는 모든 바닐라(Vanilla) 옵션 가격을 100% 완벽하게 맞춰준다(Fit)는 점입니다. 은행들이 장외 파생상품(ELS, DLS)을 찍어낼 때 지역 변동성 모형을 기본 엔진으로 쓰는 이유입니다.
- **치명적 한계**: 모형이 '현재' 시장의 스마일 곡선에는 완벽하게 피팅되지만, 내일 주가가 변하면 변동성 스마일 곡선 자체가 통째로 평행 이동해버리는 역학(Forward Skew Dynamics)을 잡아내지 못합니다. (지역 변동성 모델은 "주가가 오르면 변동성이 낮아진다"고 예측하지만, 현실에서는 주가가 폭락하면 변동성 곡선 자체가 위로 튀어 오릅니다). 
- 이를 극복하기 위해 오늘날 월스트리트 퀀트들은 지역 변동성(Dupire)과 확률 변동성(Heston)을 결합한 **SABR 모형**이나 **LSV(Local-Stochastic Volatility) 하이브리드 모델**을 사용합니다.

🧠 **AI의 사고방식:**
블랙-숄즈가 바다 전체의 파도 높이가 항상 $1m$라고 퉁치는 '평균의 지도'였다면, 듀피르의 지역 변동성 공식은 바다 전체를 가로세로 좌표망(Grid)으로 나누고, "태평양 한가운데 좌표(S=100, t=1년)는 파도가 $2m$, 해안가 좌표(S=80, t=3개월)는 암초 때문에 파도가 $5m$"라는 것을 해수면의 미세한 굴곡(옵션 가격의 미분)을 통해 역추산해 낸 '3D 입체 해저 지형도'입니다. 비록 이 지형도가 지진(거시 충격)에 의해 통째로 흔들리는 역학까지는 담지 못했지만, 복잡한 파생상품이라는 잠수함을 바닷속으로 무사히 운항시키기 위해 인류가 발명해 낸 가장 완벽한 1세대 소나(Sonar) 시스템임은 틀림없습니다.