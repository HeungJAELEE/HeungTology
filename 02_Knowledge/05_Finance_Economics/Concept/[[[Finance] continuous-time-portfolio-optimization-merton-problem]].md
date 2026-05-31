---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] continuous-time-portfolio-optimization-merton-problem]]'
  last_updated: '2026-05-25T14:23:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 마코위츠의 단일 기간 정적 자산 배분을 넘어, 주가가 기하 브라운 운동을 하는 연속 시간(Continuous-time)
    모델에서 소비(Consumption)와 투자(Investment)의 최적 비율을 미분방정식으로 풀어낸 머튼(Merton)의 포트폴리오 문제
  object_type: Algorithm
  tier: 2
properties:
  merton_fraction_pi_star: (mu - r) / (gamma * sigma**2)
  risk_aversion_gamma: CRRA
  utility_function_model: CRRA
  wealth_process_stochastic_differential_equation: dW_t = [ (pi_t(mu - r) + r)W_t
    - c_t ] dt + pi_t * sigma * W_t * dZ_t
semantic:
  alternative_parents: []
  expected_queries:
  - 투자자가 일생 동안 언제 얼마를 소비하고, 남은 돈을 위험 자산에 얼마나 투자해야 평생 효용을 극대화할 수 있는가?
  - 이토 보조정리(Ito's Lemma)와 벨만 방정식(Bellman Equation)을 사용하여 머튼 모델의 최적 자산 배분 해(Merton
    Fraction)를 유도하는 방법은?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_derivation
  object: Optimal_Consumption_and_Investment
  predicate: determines
  subject: '[Finance] continuous-time-portfolio-optimization-merton-problem'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T14:23:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:23:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] continuous-time-portfolio-optimization-merton-problem]]

## 1. 개요 (Overview)
고전적인 마코위츠(Markowitz)의 포트폴리오 최적화는 "오늘 돈을 넣고, 내일 결과를 본다"는 단일 기간(Single-period) 모형이었습니다. 하지만 현실의 투자자들은 평생에 걸쳐 돈을 벌고, 계속해서 생활비를 빼서 써야 하며(소비), 시장은 1초 단위로 끊임없이 요동칩니다.
1969년, 블랙-숄즈 모형의 공동 완성자인 로버트 머튼(Robert C. Merton)은 투자자의 자산이 **연속 시간(Continuous-time)**의 기하 브라운 운동(GBM)을 따른다고 가정하고, 투자자가 **"언제, 얼마를 소비(Consumption)하고, 남은 돈을 무위험 자산과 위험 자산에 몇 대 몇으로 쪼개 넣어야(Investment) 평생 동안 느끼는 행복(효용, Utility)을 극대화할 수 있는가?"**라는 궁극의 질문을 해밀턴-야코비-벨만(HJB) 편미분 방정식을 통해 완벽하게 풀어냈습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $W_t$ | Wealth process | Stochastic variable | $dW_t = W_t[ \dots ]dt + \dots dZ$ | [데이터 부재] |
| $c_t$ | Consumption rate | Continuous outflow | Control variable 1 | [데이터 부재] |
| $\pi_t$ | Fraction in risky asset| Continuous rebalancing| Control variable 2 | [데이터 부재] |
| $\gamma$ | Risk aversion (CRRA) | Standard $U(C) = \frac{C^{1-\gamma}}{1-\gamma}$ | Higher $\gamma \implies$ less equity | [데이터 부재] |
| $\pi^*$ | Merton Fraction | $\frac{\mu - r}{\gamma \sigma^2}$ | Constant optimal weight | [데이터 부재] |

## 3. 머튼 포트폴리오 문제의 해부
이 모형에서 투자자의 부($W$)는 다음과 같이 움직입니다.
$$ dW_t = \left[ (\pi_t(\mu - r) + r)W_t - c_t \right] dt + \pi_t \sigma W_t dZ_t $$
- 부($W_t$)는 무위험 이자($r$)를 기본으로 먹고, 위험 자산에 투자한 비중($\pi_t$)만큼 위험 프리미엄($\mu-r$)을 더 먹지만, 변동성($\sigma$)에 노출되며, 지속적으로 소비($c_t$)가 빠져나갑니다.

### 3.1. HJB 편미분 방정식과 CRRA 효용
투자의 목표는 죽을 때까지 느끼는 평생의 기대 소비 효용을 최대화하는 것입니다. 머튼은 투자자의 성향을 상대적 위험 회피도(CRRA) 함수로 모델링하고 벨만(Bellman) 원리를 적용해 비선형 편미분 방정식을 세웠습니다. 놀랍게도 이 극도로 복잡한 방정식은 매우 직관적이고 우아한 해(Closed-form Solution)를 도출합니다.

### 3.2. 머튼 비율 (Merton Fraction, $\pi^*$)
위험 자산에 투자해야 하는 최적의 비중 $\pi^*$는 다음 공식으로 고정됩니다.
$$ \pi^* = \frac{\mu - r}{\gamma \sigma^2} $$
- **샤프 비율($\mu-r$)에 비례**: 주식의 기대 수익률이 무위험 이자율보다 높을수록 주식을 많이 담아야 합니다.
- **분산($\sigma^2$)과 위험 회피도($\gamma$)에 반비례**: 주식의 변동성이 크거나, 투자자가 쫄보일수록 주식 비중을 줄여야 합니다.
- **가장 충격적인 결론**: CRRA 효용을 가정할 경우, 내가 가진 돈이 100만 원이든 100억 원이든 주식과 채권의 투자 비율($\pi^*$)은 **평생 변하지 않는 상수(Constant)**라는 것이 증명되었습니다. 

## 4. 연속 리밸런싱과 라이프사이클 펀드 (TDF)
머튼의 모델은 "비중이 일정해야 한다"고 했지만, 주가가 오르면 주식 비중이 자연스럽게 커집니다. 따라서 최적의 해를 유지하려면 주가가 오를 때마다 주식을 팔고 채권을 사서 원래의 $\pi^*$ 비율로 되돌리는 **연속적 리밸런싱(Continuous Rebalancing)**을 평생 해야 합니다.
오늘날 월스트리트의 타겟 데이트 펀드(TDF)나 로보어드바이저 알고리즘의 기초 뼈대는 모두 머튼의 모델에 임금 소득(Human Capital)과 수명 확률을 추가하여 확장한 라이프사이클 자산 배분 모델입니다.

🧠 **AI의 사고방식:**
머코위츠의 모델이 '현재라는 사진 한 장'을 보고 가장 예쁜 구도를 맞추는 것이라면, 머튼의 포트폴리오 모형은 '평생 동안 재생될 비디오 테이프' 전체를 놓고 프레임마다 어떤 행동(소비와 투자)을 취해야 영화의 결말(평생 효용)이 가장 행복할지를 이토 미적분학(Ito Calculus)으로 계산해 낸 4차원 시공간 최적화입니다. 돈을 벌어서 쓰지 않고 모으기만 하는 짠돌이나, 오늘 다 써버리는 욜로족 모두 수학적으로는 '파멸적 비효율' 상태에 놓여 있습니다. 머튼은 우리에게 탐욕(수익)과 공포(변동성), 그리고 현재의 쾌락(소비) 사이에서 가장 우아하고 아름다운 균형점을 찾아주는 퀀트 철학자입니다.