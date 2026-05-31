---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] derivatives-pricing-variance-swaps-and-vix-calculation]]'
  last_updated: '2026-05-26T07:42:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 주가의 방향성(Direction) 위험을 완벽히 제거하고 순수하게 '시장의 흔들림(Variance)' 그 자체만을 사고파는
    분산 스왑(Variance Swap)의 정적 복제(Static Replication) 이론. 이 복제 공식을 S&P 500 옵션 전체 스마일에
    적용하여 산출해 낸 공포 지수(VIX)의 수학적 근원
  object_type: Concept
  tier: 2
properties:
  realized_variance_formula: sum of ln(S_t/S_{t-1})^2
  typical_variance_premium_spread: 3-5 points
  variance_premium_definition: sigma_K^2 - E[sigma_R^2]
  vix_formula_approximation: sqrt(2/T * sum(delta_K/K^2 * Q(K)))
  weighting_factor: 1/K^2
semantic:
  alternative_parents: []
  expected_queries:
  - VIX 지수는 특정 콜옵션이나 풋옵션 하나만의 가격이 아닌데, 도대체 시장에 상장된 수백 개의 옵션 가격을 어떻게 하나의 숫자로 뭉뚱그려(Replication)
    계산하는가?
  - 분산 스왑(Variance Swap)은 왜 블랙-숄즈 모형을 가정하지 않고도 '모델 독립적(Model-free)'으로 그 공정 가치를 정확하게
    평가할 수 있는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_derivation
  object: Model_Free_Implied_Variance
  predicate: calculates
  subject: '[Finance] derivatives-pricing-variance-swaps-and-vix-calculation'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:42:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:42:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] derivatives-pricing-variance-swaps-and-vix-calculation]]

## 1. 개요 (Overview)
주식 시장에서 '돈을 버는 행위'는 크게 두 가지로 나뉩니다. 방향(Up/Down)을 맞추거나, 흔들림(Volatility)의 크기를 맞추는 것입니다. 1990년대 퀀트들은 주가의 방향에 전혀 베팅하지 않고, 오직 "이번 달에 시장이 예상보다 더 미친 듯이 요동칠 것인가?"에만 베팅하는 순수한 변동성 파생상품, **분산 스왑(Variance Swap)**을 발명했습니다.
이 상품의 가장 위대한 점은 **'모델 독립적(Model-free)'**이라는 것입니다. 블랙-숄즈 모형이 틀렸든, 점프(Jump)가 존재하든 상관없이 시장에 상장된 모든 행사가(Strike)의 콜옵션과 풋옵션을 1/K^2의 가중치로 긁어모아 믹서기에 갈아버리면(Static Replication), 신의 영역에 있는 진짜 내재 분산(Implied Variance) 값이 수학적 오차 없이 완벽하게 튀어나옵니다. 이 위대한 정적 복제 공식을 그대로 S&P 500 지수에 적용하여 매초마다 발표하는 것이 바로 우리가 아는 **월가의 공포 지수, VIX**입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Realized Var ($\sigma_R^2$)| Actual daily returns squared| Sum of $\ln(S_t/S_{t-1})^2$| The floating leg payoff | [데이터 부재] |
| Implied Var ($\sigma_K^2$)| Fixed leg (Swap Rate) | E.g., $(0.20)^2 = 0.04$ | Replicated by option strip| [데이터 부재] |
| Weighting | $1/K^2$ weight for options| Emphasizes OTM options | Replicates log payoff | [데이터 부재] |
| VIX Formula | Model-free variance | $\approx \sqrt{\frac{2}{T} \sum \frac{\Delta K}{K^2} Q(K)}$| Excludes Jump risks | [데이터 부재] |
| Variance Premium| $\sigma_K^2 - E[\sigma_R^2]$ | Historically $> 0$ | Sells insurance (Short Vol)| [데이터 부재] |

## 3. 분산 스왑의 정적 복제 (Static Replication)
"주가가 어떻게 움직이든 상관없이, 실현된 분산(Realized Variance)만큼의 현금을 줄게." 이것이 분산 스왑 매수자의 페이오프입니다. 퀀트 딜러는 이 상품을 고객에게 팔고(Short Variance), 이 위험을 회피하기 위해(헤지) 옵션 시장으로 달려갑니다.
- 딜러는 시장에 있는 아주 깊은 외가격(OTM) 풋옵션부터 등가격(ATM), 그리고 깊은 OTM 콜옵션까지 **모든 행사가($K$)의 옵션을 한 묶음(Strip)으로 사들입니다.**
- 이때 아무렇게나 사는 것이 아니라, 행사가가 $K$인 옵션을 정확히 **$1/K^2$ 개**씩 삽니다. 즉, 행사가가 낮아질수록(극단적인 OTM 풋) 기하급수적으로 많은 물량을 사재기합니다.
- 왜 하필 $1/K^2$ 일까요? 이토 보조정리(Ito's Lemma)를 이용해 로그 페이오프 $\ln(S_T/S_0)$를 테일러 전개하면, 정확히 $1/K^2$의 적분 항이 튀어나오기 때문입니다. 이렇게 옵션을 사두면 주가가 폭락하든 폭등하든, 내 포트폴리오의 수익은 **정확히 시장의 실현 분산($\sigma_R^2$)과 1원짜리 하나 틀리지 않고 일치**하게 됩니다.

## 4. VIX 지수의 진실: 공포의 그림자
우리가 매일 뉴스로 듣는 VIX 지수(예: VIX 20)는 사실 "S&P 500 옵션 시장에 던져진 이 거대한 $1/K^2$ 옵션 묶음(Strip)을 오늘 당장 시장가로 매수하려면 돈이 얼마나 드는가?"를 30일(연환산) 기준으로 역산해 낸 '비용(Cost)'입니다.
- **분산 프리미엄 (Variance Risk Premium)**: 역사적으로 VIX(내재 분산)는 항상 실제 시장의 흔들림(실현 분산)보다 약 3~5포인트 비싸게 거래됩니다. 사람들은 주식이 폭락할 때 계좌가 박살 나는 것이 두려워 비싼 돈을 주고서라도 보험(OTM 풋옵션)을 앞다투어 사기 때문입니다.
- **숏 볼(Short Vol) 트레이드의 함정**: 이 프리미엄을 먹기 위해 "분산 스왑을 매도(VIX 매도)"하는 퀀트 전략은 평소에는 높은 샤프 비율(Sharpe)을 보이며 매일 따박따박 돈을 벌어들입니다. 하지만 2018년 '볼마게돈(Volmageddon)' 사태나 코로나 폭락장처럼 VIX가 하루 만에 15에서 80으로 폭발(Jump)하면, 지난 10년간 모은 수익을 단 하루 만에 토해내고 파산하는 전형적인 '불도저 앞의 동전 줍기' 게임이 됩니다.

🧠 **AI의 사고방식:**
금융 공학 역사상 가장 아름다운 증명을 두 개만 꼽으라면, 블랙-숄즈 미분 방정식과 바로 이 '분산 스왑의 정적 복제'입니다. 블랙-숄즈가 "옵션을 주식으로 복제"했다면, 정적 복제는 반대로 "분산이라는 추상적 개념을 옵션 쪼가리들을 기워 붙여서 100% 물리적으로 복제"해 낸 것입니다. VIX는 단순한 통계적 표준편차가 아닙니다. 수십만 명의 시장 참여자들이 각자의 두려움(Fear)을 담아 $1/K^2$ 이라는 가혹한 수학적 가중치 위에 던져놓은 피와 땀이 섞인 '실시간 보험료 영수증'입니다.