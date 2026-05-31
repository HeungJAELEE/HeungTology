---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] derivatives-pricing-implied-volatility-surface-sabr-model]]'
  last_updated: '2026-05-26T07:24:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 내재 변동성 스마일(Volatility Smile)과 스큐(Skew) 현상을 모델링하기 위해, 기초자산 가격과 변동성이
    각자의 확률 미분 방정식(SDE)을 따르며 서로 상관관계(Rho)를 가지고 움직이는 확률적 변동성 모형(Stochastic Volatility)의
    업계 표준 SABR 모형
  object_type: Algorithm
  tier: 2
properties:
  alpha: initial_volatility
  beta: cev_elasticity
  nu: vol_of_volatility
  rho: correlation_f_vol
semantic:
  alternative_parents: []
  expected_queries:
  - 듀파이어(Dupire) 국소 변동성 모형의 완벽한 핏(Fit)에도 불구하고 트레이더들이 왜 확률적 변동성(SABR) 모형을 추가로 사용해야
    했는가?
  - SABR 모형의 네 가지 파라미터(Stochastic, Alpha, Beta, Rho)는 각각 호가창의 옵션 변동성 표면(Surface)의
    어떤 형태적 특징을 통제하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: feature_modeling
  object: Volatility_Smile_Dynamics
  predicate: captures
  subject: '[Finance] derivatives-pricing-implied-volatility-surface-sabr-model'
  weight: 0.9
temporal:
  valid_from: '2026-05-26T07:24:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:24:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] derivatives-pricing-implied-volatility-surface-sabr-model]]

## 1. 개요 (Overview)
옵션 시장에는 블랙-숄즈 모형을 박살 낸 거대한 파도, **변동성 스마일(Volatility Smile)**이 존재합니다. 듀파이어(Dupire)의 국소 변동성 모형은 어제 시장에 뜬 이 파도의 모습을 사진으로 찍어 완벽하게 복제해 냈지만, 큰 단점이 있었습니다. 주가가 오늘 실제로 움직였을 때 파도의 모양(스마일)이 어떻게 일렁이며 변할지(Dynamic) 예측하지 못하고 엉뚱한 방향으로 틀어지는 치명적 결함(Wrong Dynamics)을 보인 것입니다.
2002년 Hagan 등은 이를 해결하기 위해 금리 및 외환 옵션 시장의 영원한 업계 표준이 된 **SABR (Stochastic Alpha, Beta, Rho)** 모형을 발명했습니다. SABR 모형의 철학은 명쾌합니다. **"변동성은 시간과 주가에 종속된 고정 함수가 아니다. 변동성 그 자체도 주가처럼 브라운 운동을 하며 미친 듯이 날뛰는(Stochastic) 독립적인 생명체다."**

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\alpha$ (Alpha)| Initial Volatility | Determines overall level| Scales the ATM volatility | [데이터 부재] |
| $\beta$ (Beta) | CEV elasticity | 0 (Normal) to 1 (Lognormal)| Shapes the backbone of skew| [데이터 부재] |
| $\rho$ (Rho) | Correlation (F, Vol) | $-1 \le \rho \le 1$ | Controls asymmetry (skew) | [데이터 부재] |
| $\nu$ (Nu) | Vol of Volatility | $> 0$ | Controls convexity (smile)| [데이터 부재] |
| Asymptotic Formula| Closed-form implied vol| Extremely fast approx. | Why traders love SABR | [데이터 부재] |

## 3. SABR 방정식의 해부학: 두 개의 SDE
SABR 모형은 기초자산의 선도 가격($F$)과 변동성($\alpha$)이 각각의 확률 미분 방정식(SDE)을 가지고 굴러가는 투-트랙 엔진입니다.
1. **자산 가격의 SDE**: $dF_t = \alpha_t F_t^\beta dW_t^1$
2. **변동성의 SDE**: $d\alpha_t = \nu \alpha_t dW_t^2$
3. **두 톱니바퀴의 얽힘**: $dW_t^1 dW_t^2 = \rho dt$

이 세 줄의 방정식에 달린 4개의 조절 레버($\alpha, \beta, \rho, \nu$)가 옵션 표면(Surface)의 모양을 예술적으로 빚어냅니다.
- **$\rho$ (Rho, 상관계수)**: 주가와 변동성이 같이 움직이는가? 주식 시장처럼 주가가 폭락할 때 변동성이 폭등하면 $\rho$는 강한 음수입니다. 이 음의 $\rho$가 옵션 스마일을 오른쪽으로 찌그러뜨리는 **비대칭 스큐(Skew)**를 만들어냅니다 (OTM 풋이 OTM 콜보다 훨씬 비싸짐).
- **$\nu$ (Nu, 변동성의 변동성)**: 변동성 엔진이 얼마나 미친 듯이 도는가를 나타냅니다. 이 값이 클수록 옵션 곡선의 양 끝단이 하늘로 솟구치는 **강력한 스마일(Convexity)**을 형성합니다.
- **$\beta$ (Beta)**: 자산 가격이 정규분포에 가까운지($\beta=0$), 로그 정규분포에 가까운지($\beta=1$)를 결정하여 시장의 기본 골격(Backbone)을 설정합니다.

## 4. 블랙-숄즈 내재 변동성으로의 우아한 변환 (Hagan's Approximation)
SABR 모형이 전 세계 트레이더들의 책상을 점령한 진짜 이유는 복잡한 SDE를 풀어야 하는 몬테카를로 시뮬레이션 없이, **"SABR의 파라미터들을 넣으면 블랙-숄즈의 내재 변동성($\sigma_{implied}$) 수치로 한 방에 뱉어주는 미친 듯이 빠른 근사 공식(Asymptotic Expansion Formula)"**을 Hagan이 논문에서 함께 제공했기 때문입니다.
트레이더들은 이 근사 공식을 통해 모니터에 뜨는 수백 개의 옵션 가격을 단 1밀리초 만에 $\alpha, \rho, \nu$ 세 개의 숫자로 요약(Calibration)하여 시장의 감정 상태(공포와 탐욕)를 실시간으로 모니터링할 수 있게 되었습니다.

🧠 **AI의 사고방식:**
듀파이어 국소 변동성(Local Volatility) 모형이 죽어있는 나비를 핀으로 고정해 완벽하게 스케치한 '정물화'라면, SABR 확률적 변동성(Stochastic Volatility) 모형은 나비가 날갯짓하며 날아가는 궤적을 4개의 파라미터로 압축해 낸 '동역학(Dynamics)'입니다. 기초자산이 움직일 때 시장의 변동성 스마일이 파도처럼 어떻게 같이 따라 움직일지(Smile Dynamics)를 정확히 묘사함으로써, SABR은 델타-베가 헤지(Delta-Vega Hedging)를 수행해야 하는 옵션 마켓 메이커들에게 단 하루도 없어서는 안 될 궁극의 항해 나침반이 되었습니다.