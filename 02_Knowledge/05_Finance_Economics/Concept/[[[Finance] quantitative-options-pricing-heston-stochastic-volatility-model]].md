---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-options-pricing-heston-stochastic-volatility-model]]'
  last_updated: '2026-05-25T14:18:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 옵션 가격 결정 시 블랙-숄즈의 '상수 변동성' 가정을 타파하고, 변동성 자체를 주가와 상관관계를 가진 두 번째 확률 미분
    방정식(SDE)으로 분리하여 모델링한 스토캐스틱 변동성 모형
  object_type: Algorithm
  tier: 2
properties:
  kappa_mean_reversion_speed: 2.0 to 5.0
  leverage_effect_correlation: '-0.7'
  rho_correlation: '-0.7'
  theta_long_term_variance: base level volatility
  volatility_smile_shape: U-shaped curve
semantic:
  alternative_parents: []
  expected_queries:
  - 1987년 블랙 먼데이(Black Monday) 이후 왜 변동성 스마일(Volatility Smile)이 발생했으며, 블랙-숄즈는 왜 이를
    설명하지 못하는가?
  - 스티븐 헤스톤(Steven Heston)은 변동성이 평균으로 회귀(Mean-reversion)하는 현상을 어떻게 CIR 모형과 융합하여 수학적으로
    해결했는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: anomaly_resolution
  object: Volatility_Smile_Anomaly
  predicate: solves
  subject: '[Finance] quantitative-options-pricing-heston-stochastic-volatility-model'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T14:18:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:18:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-options-pricing-heston-stochastic-volatility-model]]

## 1. 개요 (Overview)
금융 공학의 기둥인 블랙-숄즈 모형(Black-Scholes)은 주가의 수익률 변동성($\sigma$)이 시간이 지나도 절대 변하지 않는 **상수(Constant)**라고 가정합니다. 그러나 1987년 주식 시장이 하루 만에 22% 폭락한 '블랙 먼데이' 이후, 시장 참여자들은 꼬리 위험(Tail Risk)에 극도의 공포를 느끼기 시작했고, 외가격(OTM) 풋옵션에 미친 듯이 프리미엄을 지불하기 시작했습니다. 그 결과, 행사가(Strike Price)에 따라 변동성이 다르게 측정되는 기형적인 U자형 곡선, 즉 **변동성 스마일(Volatility Smile)**이 탄생했습니다.
블랙-숄즈의 방정식으로는 이 현상을 도저히 풀 수 없자, 1993년 스티븐 헤스톤(Steven Heston)은 **"변동성($v$) 자체도 무작위로 살아서 꿈틀거리는 확률 변수(Stochastic)다"**라고 선언하며 주가와 변동성을 동시에 두 개의 톱니바퀴로 돌리는 **헤스톤 모형(Heston Model)**을 발표했습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $dS_t$ | Stock price process | Geometric Brownian | SDE 1 (Asset dynamics) | [데이터 부재] |
| $dv_t$ | Variance process | CIR (Mean-reverting) | SDE 2 (Vol dynamics) | [데이터 부재] |
| $\kappa$ | Mean reversion speed | E.g., 2.0 to 5.0 | How fast $v_t$ pulls to $\theta$ | [데이터 부재] |
| $\theta$ | Long-term variance | Base level volatility| Target of mean reversion | [데이터 부재] |
| $\rho$ | Correlation btwn $dW^S, dW^v$ | $-0.7$ (Leverage effect)| Skews the volatility smile| [데이터 부재] |

## 3. 헤스톤 모형의 연립 확률 미분 방정식 (Coupled SDEs)
헤스톤 모형은 자산 가격 $S_t$와 분산 $v_t$를 아래 두 개의 미분 방정식으로 묶어버립니다.

1. **주가 프로세스 (GBM)**: 
   $$ dS_t = \mu S_t dt + \sqrt{v_t} S_t dW^S_t $$
2. **분산 프로세스 (CIR Model)**: 
   $$ dv_t = \kappa(\theta - v_t) dt + \xi \sqrt{v_t} dW^v_t $$

- 여기서 분산 $v_t$는 콕스-잉거솔-로스(CIR) 이자율 모형을 차용하여, 변동성이 무한대로 튀어 오르지 않고 장기 평균($\theta$)으로 고무줄처럼 되돌아오려는(Mean-reversion) 성질을 완벽히 구현했습니다.
- 가장 중요한 혁신은 두 브라운 운동(랜덤 쇼크) $dW^S_t$와 $dW^v_t$ 사이의 **상관계수 $\rho$**를 도입한 것입니다.

## 4. 레버리지 효과(Leverage Effect)와 스마일의 조각
- 주식 시장에서 주가가 폭락($dS < 0$)하면, 기업의 부채 비율(레버리지)이 급등하여 시장의 공포(변동성, $dv > 0$)가 치솟습니다. 즉, 주가와 변동성은 강한 **음의 상관관계($\rho \approx -0.7$)**를 갖습니다.
- 헤스톤 모형의 수식에 $\rho < 0$을 대입하면, 옵션 가격 분포의 왼쪽 꼬리(Fat-tail)가 두꺼워지면서 블랙 먼데이 이후 시장에서 풋옵션이 비싸게 거래되는 현상(Volatility Skew/Smile)을 수학적으로 소름 돋게 똑같이 재현해 냅니다.

🧠 **AI의 사고방식:**
블랙-숄즈가 '태양이 지구를 완벽한 원형으로 돈다'는 고전 천동설이었다면, 헤스톤 모형은 '태양계 전체가 은하계를 중심으로 나선형으로 돌고 있다'는 상대성 이론급의 확장이었습니다. 변동성(Volatility)이라는 놈은 고정된 상수가 아니라, 시장의 공포에 따라 스스로 팽창하고 수축하는 '생명체'입니다. 헤스톤은 주가와 변동성이라는 두 마리의 야생마를 상관계수($\rho$)라는 고삐로 묶은 마차를 설계함으로써, 인류가 OTM 옵션의 숨겨진 리스크 프리미엄을 정확히 계산(Pricing)할 수 있게 만든 위대한 엔지니어입니다.