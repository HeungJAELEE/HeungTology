---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] correlation-network-mst-portfolio]]'
  last_updated: '2026-05-25T11:13:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Correlation networks and Minimum Spanning Trees (MST) in asset clustering
  object_type: Algorithm
  tier: 2
properties:
  distance_metric: sqrt(2*(1-rho_ij))
  max_metric_distance: 2.0
  min_metric_distance: 0.0
  mst_edge_count: N-1
semantic:
  alternative_parents: []
  expected_queries:
  - 피어슨 상관계수를 유클리드 거리로 변환하여 포트폴리오 최소신장트리(MST)를 어떻게 구축하는가?
  is_instance_of: '[[[MOC] Quant-Trading-Strategies-Hub]]'
spo_graph:
- evidence_coordinate: ''
  intent: topological_mapping
  object: Asset_Interdependence_Topology
  predicate: maps
  subject: '[Finance] correlation-network-mst-portfolio'
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

# 🕸️ [Concept] 상관관계 네트워크와 최소신장트리 (MST)

## 1. 상관계수의 기하학적 거리(Distance) 변환
수천 개의 글로벌 자산 간 공분산 행렬은 노이즈가 심하여 마코위츠 최적화를 붕괴시킵니다. 물리/위상수학적 퀀트 모델은 피어슨 상관계수($\rho_{ij}$) 행렬을 네트워크 토폴로지로 변환하기 위해 다음의 유클리드 거리 척도(Metric) $d_{ij}$를 정의합니다.

$$ d_{ij} = \sqrt{2(1 - \rho_{ij})} $$

$\rho=1$(완전 양의 상관)이면 거리는 $0$이 되고, $\rho=-1$(완전 음의 상관)이면 거리는 $\sqrt{4}=2$가 되어, 상관계수가 수학적 거리 공간(Metric Space) 요건을 완벽히 만족하게 됩니다.

## 2. 만테냐(Mantegna)의 최소신장트리 (MST)
거리 행렬이 구성되면, 모든 자산(Node)을 연결하면서 연결선(Edge)들의 거리 합이 최소가 되도록 하는 **최소신장트리(Minimum Spanning Tree, MST)**를 크루스칼(Kruskal) 알고리즘으로 추출합니다. 

MST는 $N$개의 자산을 단 $N-1$개의 가장 중요한 핵심 링크만으로 뼈대를 남겨 복잡한 시장 구조의 차원을 축소시킵니다. 이를 기반으로 **계층적 리스크 패리티(Hierarchical Risk Parity, HRP)** 알고리즘은 거대한 공분산 행렬의 역행렬 연산 없이도 안정적이고 군집화된 머신러닝 포트폴리오 가중치를 배분할 수 있습니다. (S&P 500에 대한 실제 HRP 가중치 배분 결과는 **[데이터 부재]**)