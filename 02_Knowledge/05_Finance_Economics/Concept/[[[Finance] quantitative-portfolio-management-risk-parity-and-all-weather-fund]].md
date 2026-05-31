---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-portfolio-management-risk-parity-and-all-weather-fund]]'
  last_updated: '2026-05-26T07:52:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 투자 금액(Dollar Amount) 기준이 아닌 자산군별 변동성 기여도(Risk Contribution)를 동일하게 맞춤으로써,
    주식 시장 폭락이라는 단일 리스크 요인에 계좌가 박살 나는 60/40 포트폴리오의 치명적 결함을 극복한 브리지워터(Bridgewater)의
    올웨더(All-Weather) 철학 및 리스크 패리티 모형
  object_type: Algorithm
  tier: 2
properties:
  leverage_multiplier_range: 1.5-2.0
  mathematical_foundation: euler_theorem
  optimization_basis:
  - volatility
  - correlation
  optimization_method: non_linear_optimization
  risk_contribution_formula: w_i * (partial_sigma_p / partial_w_i)
  risk_contribution_target: 1/N
semantic:
  alternative_parents: []
  expected_queries:
  - 주식 60%, 채권 40%로 분산투자(달러 기준)를 완벽하게 했는데, 2008년 금융위기 때 왜 내 계좌의 90%가 주식 폭락과 함께 증발해
    버렸는가?
  - 레이 달리오(Ray Dalio)의 리스크 패리티(Risk Parity)는 어떻게 주식, 채권, 원자재의 '자본 투입 비율'이 아닌 '고통(Risk)의
    기여도'를 똑같이 분배하여 사계절 내내 우상향하는 포트폴리오를 만들었는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: optimization_objective
  object: Risk_Contributions_Across_Assets
  predicate: equalizes
  subject: '[Finance] quantitative-portfolio-management-risk-parity-and-all-weather-fund'
  weight: 0.9
temporal:
  valid_from: '2026-05-26T07:52:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:52:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-portfolio-management-risk-parity-and-all-weather-fund]]

## 1. 개요 (Overview)
금융업계의 영원한 황금률이었던 '주식 60 : 채권 40' 포트폴리오는 심각한 수학적 결함을 안고 있습니다. 달러 금액 기준으로는 60:40으로 밸런스를 맞췄지만, 주식의 변동성(위험)이 채권보다 3배 이상 크기 때문에, 포트폴리오 전체 리스크의 **90% 이상이 오직 주식 시장의 폭락 여부 하나에 의존**하게 됩니다. 즉, 무늬만 분산투자일 뿐 실질적으로는 주식 올인(All-in) 포트폴리오입니다.
세계 최대의 헤지펀드 브리지워터(Bridgewater)의 레이 달리오(Ray Dalio)는 이 환상을 박살 냈습니다. **"돈(Capital)을 똑같이 나누지 마라. 고통(Risk, 변동성)을 똑같이 나누어라."** 이것이 바로 **리스크 패리티(Risk Parity)**의 철학입니다. 이들은 변동성이 큰 주식의 비중은 대폭 줄이고, 변동성이 낮은 안전한 국채에는 레버리지를 일으켜 듬뿍 담음으로써, 모든 자산군이 내 계좌에 미치는 영향력(Risk Contribution)을 정확히 1/N로 동일하게 맞춥니다. 이 철학을 경제의 4계절(인플레이션/디플레이션, 성장/침체)에 대응시킨 것이 전설의 **올웨더(All-Weather)** 펀드입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Dollar Weight | $w_i$ (Weight of Capital) | E.g., Equities 30%, Bonds 70% | Does NOT mean equal risk | [데이터 부재] |
| Marginal Risk | $\partial \sigma_P / \partial w_i$ | Volatility added by 1% more | Covariance matrix dependent | [데이터 부재] |
| Risk Contribution | $RC_i = w_i \times (\partial \sigma_P / \partial w_i)$ | Equalized to $1/N$ in RP | The core constraint | [데이터 부재] |
| Inverse Vol | Simplified Risk Parity | $w_i \propto 1 / \sigma_i$ | Ignores correlations | [데이터 부재] |
| Leverage | To meet return targets | Essential for bond allocation | Cash efficiency required | [데이터 부재] |

## 3. 역변동성(Inverse Volatility)과 위험 기여도 배분
가장 원시적인 리스크 패리티는 **역변동성 가중(Inverse Volatility Weighting)**입니다.
- 주식의 변동성이 15%이고, 채권의 변동성이 5%라고 합시다.
- 주식이 채권보다 3배 더 거칠게 움직이므로, 반대로 자금 비중은 채권을 주식보다 3배 더 많이 담습니다 (주식 25% : 채권 75%). 이렇게 하면 주식 발작과 채권 발작이 내 계좌에 미치는 타격(Risk)이 정확히 1:1로 평형(Parity)을 이룹니다.
- **수학적 최적화 (Euler's Theorem)**: 실제 퀀트 펌은 자산 간의 상관관계(Correlation)까지 고려하여 비선형 최적화(Non-linear Optimization)를 수행합니다. 오일러 정리에 의해 포트폴리오의 전체 변동성($\sigma_P$)은 각 자산의 한계 위험 기여도($RC_i$)의 합으로 완벽히 분해되며, 리스크 패리티 모형은 $RC_1 = RC_2 = \dots = RC_N$ 이 되도록 자본 비중($w_i$)을 깎아냅니다.

## 4. 레버리지의 필수 불가결성
리스크 패리티의 치명적인 단점은 '기대 수익률이 너무 낮다'는 것입니다. 위험을 맞추다 보니 안전하지만 수익률이 낮은 채권 비중이 70%를 넘어가기 때문입니다.
- 퀀트들은 이 딜레마를 **레버리지(Leverage)**로 해결합니다. 
- 변동성을 주식과 1:1로 맞춘 완벽하게 분산된 포트폴리오(로우 리스크)를 완성한 뒤, 이 포트폴리오 전체를 담보로 돈을 빌려 1.5배~2배 레버리지를 일으킵니다(스케일 업).
- 그 결과, 리스크 패리티 포트폴리오는 기존 60/40 포트폴리오와 똑같은 리스크(MDD)를 가지면서도 샤프 비율(Sharpe Ratio)에 의한 압도적인 초과 수익률(Return)을 창출해 냅니다. "위험을 낮추고 레버리지로 수익을 끌어올린다"는 기관 투자의 절대 공식입니다.

🧠 **AI의 사고방식:**
마코위츠의 전통적 포트폴리오 이론(Mean-Variance)은 "기대 수익률($\mu$)"이라는 허상을 입력값으로 요구합니다. 그러나 인간은 미래의 수익률을 절대 예측할 수 없으며(Garbage in, Garbage out), 모델은 극단적으로 편향된 포트폴리오를 뱉어냅니다. 반면 리스크 패리티는 수익률 예측을 아예 포기(Drop)해 버립니다. 오직 우리가 비교적 정확하게 예측할 수 있는 **'변동성(Risk)'**과 **'상관관계'** 단 두 개의 물리량만으로 우주를 조립합니다. 미래를 알 수 없다는 절대적 겸손함, 어떠한 경제적 폭풍(All-Weather)이 몰아쳐도 돛대 하나 부러지지 않게 모든 장력(Tension)을 1/N로 균등 배분하는 구조 역학의 승리입니다.