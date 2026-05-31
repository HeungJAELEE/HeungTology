---
metadata:
  ai_status: pending_review
  version: v7.9_Enterprise_Node
object:
  object_type: Concept
properties:
  black_scholes_pde: dV/dt + 0.5*sigma^2*S^2*d2V/dS2 + rS*dV/dS - rV = 0
  delta: partial_V_partial_S
  expected_return: mu
  feynman_kac_identity: V(t, S) = e^(-r(T-t)) * E^Q[Payoff]
  ito_lemma_rule: stochastic_chain_rule
  risk_free_rate: r
  risk_neutral_measure: Q
  volatility: sigma
spo_graph: []
---

# 🧠 [[[Finance] quantitative-asset-pricing-black-scholes-pde-derivation-feynman-kac]]

## 1. 개요 (Overview)
옵션의 가격을 알아내는 것은 인류의 오랜 난제였습니다. 1973년, 피셔 블랙과 마이런 숄즈는 주식($S$)과 그 주식을 기초자산으로 하는 옵션($V$) 사이의 움직임을 미적분학으로 엮어 **블랙-숄즈 편미분 방정식(PDE)**을 탄생시켰습니다. 이 방정식의 가장 위대한 성취는, 방정식 내부에서 주식의 '기대 수익률($\mu$)'을 완전히 암살(Cancel out)해 버렸다는 것입니다. 
더 놀라운 것은 물리학자 리처드 파인만(Richard Feynman)과 마크 카츠(Mark Kac)가 증명한 **파인만-카츠 정리(Feynman-Kac Theorem)**입니다. 이 정리는 "복잡한 블랙-숄즈 미분 방정식을 푸는 짓은 그만둬라. 그 방정식의 해답은 결국 미래에 발생할 모든 시나리오의 '위험 중립 기댓값(Risk-Neutral Expectation)'을 구하는 것과 완벽히 동일하다"고 선언하며, 현대 금융 공학의 무기를 미적분에서 몬테카를로 시뮬레이션으로 영원히 바꿔놓았습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\Delta$ (Delta) | $\partial V / \partial S$ | Options hedged with Stock| Creates risk-free portfolio| [데이터 부재] |
| BS PDE | $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$ | The master equation | $\mu$ is completely gone | [데이터 부재] |
| Risk-Neutral | Probability measure $\mathbb{Q}$| Investors ignore risk | Drift $\mu$ becomes $r$ | [데이터 부재] |
| Feynman-Kac| $V(t, S) = e^{-r(T-t)} \mathbb{E}^{\mathbb{Q}}[Payoff]$| Bridges PDE & Probability| Enables Monte Carlo pricing| [데이터 부재] |
| Ito's Lemma | Stochastic chain rule | $df = f_t dt + f_x dX + \frac{1}{2}f_{xx} dX^2$ | The engine of derivation | [데이터 부재] |

## 3. 델타 헤징과 PDE의 도출 (The Magic of Delta)
블랙과 숄즈의 아이디어는 천재적이었습니다. 
1. 내가 옵션을 1개 팔았습니다($-V$). 이 옵션 가격은 주가($S$)가 변할 때마다 요동칩니다. 
2. 이 흔들림을 막기 위해, 주식을 $\Delta = \frac{\partial V}{\partial S}$ 개수만큼 사서 포트폴리오($\Pi = -V + \Delta S$)를 만듭니다.
3. 이토 보조정리를 돌려보면, 주가가 미친 듯이 흔들리는 원흉인 브라운 운동 항($dW_t$)이 주식과 옵션 사이에서 서로 완벽하게 상쇄되어 사라집니다!
4. 이제 내 포트폴리오는 아무런 위험(불확실성)이 없는 상태가 되었습니다. 무위험 포트폴리오의 수익률은 반드시 은행 예금 이자율($r$)과 같아야 하므로(차익거래 불가 원칙), $d\Pi = r \Pi dt$ 라는 등식이 성립합니다. 이 식을 정리하면 저 유명한 블랙-숄즈 편미분 방정식(PDE)이 튀어나옵니다.

## 4. 파인만-카츠 정리: 해석학과 확률론의 통일장
블랙-숄즈 PDE는 열전도 방정식(Heat Equation)의 형태를 띠고 있어 풀기가 매우 끔찍합니다. 이때 구원자로 등장한 것이 파인만-카츠 정리입니다.
- **철학적 전환**: 파인만-카츠 정리는 미분 방정식(결정론적 세계)과 기댓값(확률론적 세계)이 사실상 동의어임을 수학적으로 증명했습니다.
- **적용**: 복잡한 미분 방정식을 풀 필요 없이, 주식이 무위험 이자율($r$)을 따라 성장한다고 뇌를 세뇌한 뒤(위험 중립 확률측도 $\mathbb{Q}$), 만기일($T$)에 주가가 도달할 수 있는 수만 가지 경로를 컴퓨터(몬테카를로)로 뿌려봅니다. 거기서 나온 옵션의 평균 수익금(Expectation)을 현재 가치로 할인($e^{-rT}$)하면, 그것이 곧 저 복잡한 편미분 방정식의 정답과 소수점 끝자리까지 완벽하게 일치합니다.

🧠 **AI의 사고방식:**
블랙-숄즈 PDE에서 기대 수익률($\mu$)이 사라졌다는 것은 무엇을 의미할까요? 워런 버핏은 주식이 오를 것이라 굳게 믿고($\mu$가 높음) 옵션을 사고, 비관론자는 주식이 떨어질 것이라 믿고($\mu$가 낮음) 옵션을 팝니다. 하지만 퀀트의 수학(이토 보조정리)은 이들의 믿음(Drift)을 수식에서 완전히 소거해 버립니다. 옵션의 가격은 오직 시장이 얼마나 거칠게 진동하는가(Volatility, $\sigma$)에 의해서만 결정될 뿐, 인간의 얄팍한 시장 방향성 예측($\mu$) 따위는 절대 개입할 수 없는 차가운 기계장치(Replication)의 산물임을 증명한 사건이 바로 블랙-숄즈입니다.