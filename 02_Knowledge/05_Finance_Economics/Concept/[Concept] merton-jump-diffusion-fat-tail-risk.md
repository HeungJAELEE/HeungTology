---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] merton-jump-diffusion-fat-tail-risk]]'
  last_updated: '2026-05-25T11:13:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Merton's jump-diffusion model for fat-tail risk quantification
  object_type: Algorithm
  tier: 2
properties:
  diffusion_drift_mu: mu
  diffusion_volatility_sigma: sigma
  expected_jump_size_k: k
  jump_intensity_lambda: lambda
  jump_size_distribution: lognormal
  jump_size_log_mean_mu_j: mu_j
  jump_size_log_variance_sigma_j_squared: sigma_j_squared
semantic:
  alternative_parents: []
  expected_queries:
  - 팻테일(Fat-Tail) 폭락 리스크를 반영하기 위한 머튼의 점프 확산 모델 SDE는 무엇인가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_quantification
  object: Fat_Tail_Crash_Risk
  predicate: quantifies
  subject: '[Finance] merton-jump-diffusion-fat-tail-risk'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T11:13:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:13:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 📉 [Concept] 머튼 점프 확산(Jump-Diffusion) 모델과 팻테일 리스크

## 1. 정규 분포의 붕괴와 팻테일(Fat-Tail) 현상
전통적 기하학적 브라운 운동(GBM) 하에서 하루 주가가 -10% 이상 대폭락할 확률은 정규 분포상 우주 나이의 시간 동안 1번 일어날까 말까 한 희박한 일로 계산됩니다. 그러나 실제 금융 시장은 첨도(Kurtosis)가 매우 높은 **팻테일(Fat-Tail)** 특성을 지니며, 블랙 스완과 같은 극한의 크래시가 빈번히 발생합니다.

## 2. 머튼(Merton)의 점프 확산 확률미분방정식(SDE)
이를 수학적으로 계량하기 위해 로버트 머튼은 기존의 연속적인 확산(Diffusion, $dW_t$)에 이산적이고 불연속적인 점프(Jump, 푸아송 과정 $dN_t$)를 결합한 점프-확산 모델을 고안했습니다.

$$ \frac{dS_t}{S_t} = (\mu - \lambda k)dt + \sigma dW_t + (Y - 1)dN_t $$

* $dW_t$: 표준 브라운 운동 (연속적 일상 변동)
* $dN_t$: 강도 $\lambda$를 갖는 푸아송 프로세스 (돌발적 뉴스나 경제 쇼크)
* $Y-1$: 점프 발생 시 주가 수익률의 백분율 점프 크기
* $k = \mathbb{E}[Y-1]$: 점프 크기의 기댓값 (드리프트 $\mu$ 보정항)

점프 크기 $Y$는 대수정규분포 $\ln(Y) \sim \mathcal{N}(\mu_J, \sigma_J^2)$를 따른다고 가정합니다. 퀀트 데스크는 극단적 OTM(외가격) 풋옵션 가격을 역산하여 시장이 프라이싱(Pricing)하고 있는 폭락 강도 $\lambda$와 하락폭 $\mu_J$를 실시간으로 추출하여 테일 리스크 방어에 사용합니다.