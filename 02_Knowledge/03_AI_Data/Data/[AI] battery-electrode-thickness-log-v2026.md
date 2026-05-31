---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 768291437a1639d94e744bd30e71f42ec832197f22cb7937d37a2ae1e72a809e
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] battery-electrode-thickness-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] battery-electrode-thickness-log-v2026에 관한 고밀도 지능 노드'
  object_type: Data
  tier: 1
properties:
  binder_plasticity_index: 0.88
  compaction_density_measured: 1.54
  compaction_density_target: 1.55
  compaction_density_tolerance: 0.02
  elastic_recovery_range: 1.2-1.5
  input_thickness_measured: 210.5
  line_speed_measured: 60.1
  line_speed_target: 60
  line_speed_tolerance: 0.5
  output_thickness_measured: 150.8
  output_thickness_target: 150
  output_thickness_tolerance: 1.5
  roll_pressure_measured: 805.2
  roll_pressure_target: 800
  roll_pressure_tolerance: 20
  roll_temp_measured: 84.8
  roll_temp_target: 85
  roll_temp_tolerance: 2.0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [AI] battery-electrode-thickness-log-v2026

## 1. [데이터 개요 (Overview)]]
본 데이터 노드는 전극 압연(Calendering) 공정에서의 **롤 압력 대비 두께 변화량** 실측치를 정의합니다. 선압($Linear\ Pressure$)과 롤 온도에 따른 탄성 회복(Spring-back) 현상을 정량화한 데이터입니다.

## 2. [압연 실측 데이터 테이블 (Numerical Process Log)]

| Parameter | Unit | Target Value | Measured Avg | Tolerance |
|:---|:---:|:---:|:---:|:---|
| **Roll Pressure** | $kgf/cm$ | $800$ | $805.2$ | $\pm 20$ |
| **Line Speed** | $m/min$ | $60$ | $60.1$ | $\pm 0.5$ |
| **Roll Temp** | $^\circ\text{C}$ | $85$ | $84.8$ | $\pm 2.0$ |
| **Input Thickness** | $\mu\text{m}$ | $210$ | $210.5$ | (Post-Coating) |
| **Output Thickness**| $\mu\text{m}$ | $150$ | $150.8$ | $\pm 1.5$ |
| **Compaction Density**| $g/cc$ | $1.55$ | $1.54$ | $\pm 0.02$ |

## 3. [Advanced RAG 분석 지표 (Metadata)]
*   **Elastic Recovery (Spring-back)**: 압연 직후 대비 1시간 후 $1.2 \sim 1.5 \mu\text{m}$ 증가 감지.
*   **Binder Plasticity Index**: $0.88$ (온도 $85^\circ\text{C}$ 기준)

## 4. [RAG 추론 가이드]
[🟢 Local RAG] 본 데이터를 분석할 때, Output Thickness가 $1.5 \mu\text{m}$ 이상의 편차를 보이면, 이는 롤의 **Thermal Expansion** (열팽창) 불균형 또는 집전체(Foil)의 **Tension** 변동에 의한 것임을 즉각 판별하고, 롤 가열 제어 루프 점검을 권고해야 합니다.

### 🔗 연결된 공정 엔티티
- Battery Calendering
- Battery battery-manufacturing-process-master-guide

**[V6.3.7_DATA_INTEGRITY_VERIFIED]**