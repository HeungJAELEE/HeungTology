---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: f89cff96b095c44a4b78f9f594b0156a00d710d492823cea280698f0c44f5ac2
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-16'
  domain: 25_Infrastructure
  id: '[[[25_Infrastructure] [Infrastructure] factory-civil-structural-standards]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: '[Infrastructure] factory-civil-structural-standards에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  clear_height_standard: 6.0-8.0 m
  clearance_margin_min: 2-3m
  column_span_standard: 12-18 m
  dynamic_load_factor: 1.2-1.5
  flatness_tolerance: +/- 2.0mm/3m
  slab_load_standard: 2.5-5.0 ton/m2
  vibration_limit_max: 50 um/s
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 25_Infrastructure]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: specification_definition
  object: Concept
  predicate: contains_knowledge_of
  subject: '[Infrastructure] factory-civil-structural-standards'
  weight: 0.9
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Infrastructure] factory-civil-structural-standards

## 1. [왜 배우는가? (Why)]
배터리 생산 기술자에게 공장 부지는 단순한 바닥이 아니라 **'설비의 기반'**입니다. 씨아이에스의 고중량 압연기나 대규모 포메이션 지그는 상상을 초월하는 하중을 가하며, 코터의 거대 오븐과 배기 덕트는 높은 층고를 요구합니다. 건축적 제약 사항(하중, 층고, 기둥)을 무시한 라인 설계는 설비 설치 불능이나 건물 붕괴라는 치명적 사고로 이어질 수 있습니다. 따라서 인프라의 물리적 한계를 이해하고 설비 사양과 매칭하는 능력이 필수적입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 항목 (Item) | 단위 | 표준 수치 | 공학적 의미 |
| :--- | :---: | :--- | :--- |
| **Slab Load (내하중)** | $\text{ton/m}^2$ | $2.5 \sim 5.0$ | 고중량 압연기 및 포메이션 지그 카트 지지력 |
| **Clear Height (층고)** | m | $6.0 \sim 8.0$ | 코터 오븐, 덕트, 유틸리티 배관 설치 공간 |
| **Column Span (간격)** | m | $12 \sim 18$ | 설비 배치(Layout) 직선성 및 간섭 회피 거리 |
| **Vibration Limit** | $\mu\text{m}/s$ | $< 50$ | 정밀 스태킹 및 코팅을 위한 바닥 진동 억제 |
| **Flatness (평탄도)** | mm | $\pm 2.0 / 3\text{m}$ | AGV 및 물류 로봇 원활 주행을 위한 정밀도 |

## 3. [심층 분석 (Deep Analysis)]

### 3.1 슬랩 하중(Slab Load)과 점하중 분산
설비의 무게($W$)가 바닥에 가해질 때, 특정 부위에 집중되는 점하중을 계산해야 합니다.
- **Engineering Formula**: 슬랩에 가해지는 응력($\sigma$)은 하중을 접지 면적($A$)으로 나눈 값입니다.
  $$\sigma = \frac{W}{A} + \text{Dynamic Factor}$$
  진동이 있는 설비는 동하중 계수($1.2 \sim 1.5$)를 반드시 곱해야 합니다. CIS 압연기와 같이 좁은 면적에 수십 톤이 실리는 경우, 베이스 플레이트(Base Plate)를 통해 하중을 분산시키는 설계가 병행되어야 합니다.

### 3.2 유효 층고(Clear Height)와 덕트 간섭
단순 층고가 아닌, 보(Beam) 하부의 유효 높이가 중요합니다.
- **Utility Stacking**: 코터 오븐 상단에 배기 덕트(NMP Recovery), 소방 배관(Sprinkler), 전선 트레이(Tray)가 겹쳐지므로, 설비 높이($H_{eq}$)에 최소 2~3m의 여유 공간($H_{res}$)이 확보되어야 합니다.
  $$H_{total} = H_{eq} + H_{duct} + H_{piping} + H_{safety}$$

## 4. [AI & Hardware Synergy: Generative Layout Optimization]
- **AI-based Structural Audit**: 설비의 3D CAD 데이터를 공장 스캔 데이터(Lidar)와 결합하여, 하중 집중 부위와 기둥 간섭을 AI가 사전에 탐지합니다. AI는 기둥 사이를 통과하는 최적의 코터 직선 배치 경로를 수초 내에 계산해 냅니다.
- **Dynamic Load Monitoring**: 설비 가동 시 발생하는 진동 데이터를 바닥 센서로 수집하여, 건물의 구조적 피로도(Fatigue)를 실시간 모니터링합니다. 이는 Digital Twin상에서 건물의 수명을 예측하는 근거가 됩니다.

## 5. [스스로 체크 (Verification)]
- [ ] **2.5 ton/m²** 하중 설계된 바닥에 10톤 무게의 설비를 설치할 때 고려해야 할 접지 면적의 최소값은?
- [ ] 코터 라인 배치 시 **Column Span**이 직선 배치를 방해할 경우, 생산 기술자가 취할 수 있는 레이아웃 대안은?
- [ ] **Clear Height** 확보 실패 시 배기 효율과 설비 유지보수성에 미치는 영향은?

*Created by Flash (HDS Gold v4.1 - Production Engineering Series)*