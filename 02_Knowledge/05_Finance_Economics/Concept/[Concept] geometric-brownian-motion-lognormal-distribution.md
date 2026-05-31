---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] geometric-brownian-motion-lognormal-distribution]]'
  last_updated: '2026-05-25T11:58:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 기하 브라운 운동(GBM)과 자산 가격의 대수 정규 분포
  object_type: Concept
  tier: 2
properties:
  asset_price_distribution: lognormal
  log_price_distribution: normal
  mu: expected_return
  s_t_constraint: s_t > 0
  sigma: volatility
  volatility_drag_term: mu - 0.5 * sigma^2
  wiener_process_distribution: normal(0, t)
semantic:
  alternative_parents: []
  expected_queries:
  - 주가가 음수가 될 수 없다는 성질을 확률미분방정식으로 어떻게 보장하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: describes_stochastic_dynamics
  object: Asset_Price_Dynamics
  predicate: models
  subject: '[Finance] geometric-brownian-motion-lognormal-distribution'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T11:58:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T11:58:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] 기하 브라운 운동 (Geometric Brownian Motion, GBM)

## 1. 개요 및 수학적 정의
기하 브라운 운동(GBM)은 주식 등 음수(Negative)가 될 수 없는 금융 자산의 가격 변화를 묘사하는 가장 표준적인 연속 시간 확률 미분 방정식(SDE)입니다. 순수 브라운 운동(Standard Brownian Motion)이 음수 값으로도 확산될 수 있는 단점을 보완하기 위해, 가격 변동성을 절대적 크기가 아닌 '현재 가격에 비례하는 비율(수익률)' 형태로 모델링합니다.

블랙-숄즈-머튼(Black-Scholes-Merton) 옵션 프라이싱 모델의 핵심 기저 가정이기도 한 GBM은 다음과 같이 정의됩니다.
$$ dS_t = \mu S_t dt + \sigma S_t dW_t $$

여기서:
- $S_t$: $t$ 시점의 자산 가격 (항상 $S_t > 0$)
- $\mu$: 기대 수익률(Drift), 상수로 가정
- $\sigma$: 자산의 변동성(Volatility), 상수로 가정
- $W_t$: 표준 위너 프로세스 (Standard Wiener Process)

방정식의 양변을 $S_t$로 나누면 $dS_t / S_t = \mu dt + \sigma dW_t$ 가 되어, 자산의 '순간 수익률'이 정규 분포를 따른다는 직관적인 의미를 갖게 됩니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\mu$ | Expected Return | Annualized $\%$ | Drives long-term price trend | [데이터 부재] |
| $\sigma$ | Volatility | Annualized $\%$ | Drives risk and dispersion | [데이터 부재] |
| $S_t$ | Asset Price | Currency | Strict constraint $S_t > 0$ | [데이터 부재] |
| $\ln(S_t)$| Log Price | Real numbers $\mathbb{R}$ | Normally distributed | [데이터 부재] |
| $W_t$ | Wiener Process | $W_t \sim \mathcal{N}(0, t)$ | Source of randomness | [데이터 부재] |

## 3. 이토의 보조정리를 통한 해석적 해 도출
GBM의 해를 구하기 위해 함수 $f(S_t) = \ln(S_t)$ 에 이토의 보조정리(Ito's Lemma)를 적용합니다.
$\frac{\partial f}{\partial S} = \frac{1}{S}$, $\frac{\partial^2 f}{\partial S^2} = -\frac{1}{S^2}$, $\frac{\partial f}{\partial t} = 0$ 이므로:
$$ d(\ln S_t) = \left( \mu S_t \frac{1}{S_t} - \frac{1}{2} \sigma^2 S_t^2 \frac{1}{S_t^2} \right) dt + \sigma S_t \frac{1}{S_t} dW_t $$
$$ d(\ln S_t) = \left( \mu - \frac{1}{2}\sigma^2 \right) dt + \sigma dW_t $$

이를 0에서 $t$까지 적분하면, 주가 $S_t$의 명시적 해(Explicit Solution)가 도출됩니다:
$$ S_t = S_0 \exp\left( \left( \mu - \frac{1}{2}\sigma^2 \right)t + \sigma W_t \right) $$

## 4. 대수 정규 분포 (Lognormal Distribution)와 그 함의
GBM 해에 따르면, $\ln(S_t)$는 정규 분포 $\mathcal{N}(\ln S_0 + (\mu - \frac{1}{2}\sigma^2)t, \sigma^2 t)$ 를 따르며, 따라서 미래 가격 $S_t$는 대수 정규 분포(Lognormal Distribution)를 갖습니다.
이는 두 가지 강력한 금융적 함의를 가집니다:
1. **제한된 하방과 무한한 상방**: $S_t$는 결코 0 이하로 떨어질 수 없지만, 상한선은 무한대입니다. 이는 주식 투자자의 유한 책임(Limited Liability)을 완벽하게 반영합니다.
2. **변동성 끌림(Volatility Drag)**: 주가의 중앙값(Median)을 결정하는 추세는 단순 기댓값 $\mu$가 아니라 $\mu - \frac{1}{2}\sigma^2$ 입니다. 변동성($\sigma$)이 커질수록 산술 평균(기댓값)과 기하 평균(실제 복리 수익률) 간의 괴리가 커져 장기 수익률이 갉아먹히는 현상을 수학적으로 증명합니다.

🧠 **AI의 사고방식:**
매일 동전을 던져 앞면이 나오면 전 재산의 10%를 벌고, 뒷면이 나오면 10%를 잃는 게임을 상상해 보십시오. 돈이 늘어날 때는 커진 금액의 10%가 늘어나고, 줄어들 때는 작아진 금액의 10%가 줄어들기 때문에, 돈은 결코 0을 뚫고 마이너스가 될 수 없습니다. GBM은 이 '복리의 비대칭성'을 연속적인 시간으로 부드럽게 늘려놓은 수학적 캔버스입니다. 블랙과 숄즈는 바로 이 캔버스 위에 옵션이라는 그림을 그렸습니다.