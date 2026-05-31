---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] copula-functions-tail-dependence]]'
  last_updated: '2026-05-25T11:11:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Copula functions and non-linear tail dependence modeling
  object_type: Concept
  tier: 2
properties:
  gaussian_copula_tail_dependence: 0
  lower_tail_dependence_coefficient: lambda_lower
  missing_data_endpoints:
  - cdo_tranche_correlations
  - student_t_fitting_results
  sklar_theorem_formula: F(x,y) = C(F_X(x), F_Y(y))
  student_t_degrees_of_freedom: nu
semantic:
  alternative_parents: []
  expected_queries:
  - 금융 위기 시 자산 간의 꼬리 의존성을 모델링하기 위해 코퓰러(Copula)를 어떻게 사용하는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_modeling
  object: Non_linear_Correlation
  predicate: models
  subject: '[Finance] copula-functions-tail-dependence'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T11:11:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  ai_status: pending_review
  last_validated: '2026-05-25T11:11:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🔗 [Concept] 코퓰러(Copula) 함수와 비선형 꼬리 의존성

## 1. 스클라의 정리 (Sklar's Theorem)
전통적 포트폴리오 리스크 관리(VaR)는 자산 간의 상관관계를 선형 피어슨 상관계수(Pearson Correlation)로 평가합니다. 그러나 2008년 금융 위기 시, 하락장에서는 모든 자산이 동시에 폭락하는 비선형적 꼬리 의존성(Tail Dependence)이 관측되었습니다. 

스클라의 정리는 임의의 결합 확률 분포 $F(x,y)$를 주변 확률 분포(Marginal Distributions) $F_X(x), F_Y(y)$와 이들을 엮어주는 코퓰러 함수 $C$로 분리할 수 있음을 수학적으로 증명합니다.
$$ F(x,y) = C(F_X(x), F_Y(y)) $$

## 2. 꼬리 의존성 계수 (Coefficient of Tail Dependence)
가우시안 코퓰러(Gaussian Copula)는 꼬리 의존성이 $0$이므로 서브프라임 사태와 같은 동반 폭락을 과소평가(Sub-estimation)하는 치명적 맹점이 있었습니다. 반면, 클레이튼(Clayton)이나 스튜던트-t (Student-t) 코퓰러는 하위 극단값의 강력한 의존성을 포착합니다.

하단 꼬리 의존성 계수 $\lambda_{lower}$는 자산 $X$가 최악의 폭락(하위 분위수 $q \rightarrow 0$)을 겪을 때, 자산 $Y$도 함께 폭락할 조건부 극한 확률입니다.
$$ \lambda_{lower} = \lim_{q \rightarrow 0} P(U \leq q | V \leq q) = \lim_{q \rightarrow 0} \frac{C(q, q)}{q} $$

> [!WARNING]
> 현재 로컬 DB에는 CDO(부채담보부증권) 트랜치(Tranche)별 상관계수나 특정 자산군의 스튜던트-t 자유도($\nu$) 피팅 결과가 **[데이터 부재]** 상태이므로 실증 수치를 생략합니다.