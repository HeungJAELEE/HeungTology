---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] multifractal-market-hurst-exponent]]'
  last_updated: '2026-05-25T11:14:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Multifractal market hypothesis and Hurst exponent for time series memory
  object_type: Concept
  tier: 2
properties:
  anti_persistence_threshold: 0.5
  hurst_exponent_range: 0 < H < 1
  persistence_threshold: 0.5
  random_walk_threshold: 0.5
  rescaled_range_analysis_formula: E[R(n)/S(n)] = C n^H
semantic:
  alternative_parents: []
  expected_queries:
  - 허스트 지수(Hurst Exponent)를 통해 시계열의 추세성과 평균 회귀성을 어떻게 구분하는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: quantification_metric
  object: Long_Term_Memory
  predicate: measures
  subject: '[Finance] multifractal-market-hurst-exponent'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:14:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:14:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🌀 [Concept] 다중 프랙탈(Multifractal) 시장 가설과 허스트 지수

## 1. 프랙탈 기하학과 장기 기억(Long-Term Memory)
효율적 시장 가설(EMH)은 가격이 기억(Memory)이 없는 랜덤 워크(Random Walk)를 따른다고 가정합니다. 반면 브누아 망델브로(Benoit Mandelbrot)의 프랙탈 시장 가설은 주가 시계열이 스케일(Scale)이 달라져도 자기 유사성(Self-similarity)을 지니며, 장기 기억을 갖는다고 봅니다.

## 2. 허스트 지수 (Hurst Exponent, $H$)
시계열의 장기 기억성을 정량화하기 위해 재조정 범위 분석(Rescaled Range Analysis, R/S)을 수행하여 허스트 지수 $H$를 추출합니다.

$$ \mathbb{E}\left[ \frac{R(n)}{S(n)} \right] = C n^H $$

* $R(n)$: 기간 $n$ 동안의 누적 편차의 범위 (Range)
* $S(n)$: 기간 $n$ 동안의 표준편차 (Standard Deviation)
* $H$: 허스트 지수 ($0 < H < 1$)

**퀀트 트레이딩 해석:**
* $H = 0.5$: 기하학적 브라운 운동(GBM). 완벽한 랜덤 워크 (과거가 미래를 예측하지 못함).
* $0.5 < H < 1$: **지속성 (Persistence)**. 강한 추세(Momentum)를 의미하며, 양의 자기상관을 가짐. (추세 추종 알고리즘 가동)
* $0 < H < 0.5$: **반지속성 (Anti-persistence)**. 강한 평균 회귀(Mean-reverting) 성향을 의미. (페어 트레이딩 알고리즘 가동)