---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 29645dc08e839c40d6593c822eb5753b6c8d1343029abcd0e19f32f68f813dca
metadata:
  date: '2026-05-16'
  domain: 02_Battery
  id: '[[[Battery] sodium-ion-chemistry]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Battery] sodium-ion-chemistry에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  anode_collector_material: aluminum
  anode_material: hard_carbon
  cathode_structures: prussian_blue, layered_oxides
  cost_reduction_target_vs_lib: 30%
  external_performance_log: Battery-SIB-Material-and-Cost-Performance-Log_2026-05-16
  lithium_ion_radius: 0.76 Å
  safe_overdischarge_voltage: 0V
  sodium_ion_radius: 1.02 Å
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 02_Battery]]'
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

# [Battery] sodium-ion-chemistry

## 1. 개요: 자원 주권과 경제적 배터리 (Operational Objective)
나트륨 이온 배터리(SIB)는 리튬($Li$) 자원의 희소성과 가격 변동성 리스크를 해결하기 위한 핵심 대안입니다. 지각 내 매장량이 풍부한 나트륨($Na$)을 활용하여 시스템 비용을 리튬 이온 배터리(LIB) 대비 30% 이상 절감하면서도, 대규모 에너지 저장 장치(ESS) 및 저가형 마이크로 모빌리티 시장에 최적화된 출력과 저온 성능을 제공하는 것을 목적으로 합니다.

## 2. SIB 전기화학 및 소재 물성 표준 (Technical Specs)

| 분석 항목 | 수리적/물리적 기전 (Mechanism) | 공학적 특징 및 이점 | 기술적 근거 |
| :--- | :--- | :--- | :--- |
| **이온 반경** | $Na^+ (1.02 \text{\AA}) > Li^+ (0.76 \text{\AA})$ | 확산 속도가 느리나 저온 저항이 낮음 | 확산 동역학 모델 |
| **음극 집전체** | $Na$와 $Al$의 비합금화(Non-alloying) | 음극에 고가 구리(Cu) 대신 알루미늄(Al) 사용 | 원가 절감의 핵심 기전 |
| **음극 소재** | 하드 카본 (Hard Carbon) | 불규칙한 층간 간격으로 큰 나트륨 삽입 | 흡착-삽입 복합 메커니즘 |
| **양극 구조** | 프러시안 블루 / 층상 산화물 | 개방형 프레임워크로 이온 경로 최적화 | 결정 격자 안정성 확보 |

## 3. 핵심 공학 메커니즘 (Engineering Mechanisms)

### 3.1 하드 카본(Hard Carbon)의 'Adsorption-Intercalation' 물리
규칙적인 흑연 구조는 나트륨 이온의 삽입에 한계가 있습니다. 비정질 구조의 하드 카본은 기공 내 흡착(Adsorption)과 확장된 층간 삽입(Intercalation)을 동시에 활용하여 높은 가역 용량을 확보합니다.

### 3.2 알루미늄 집전체 채택의 전기화학적 근거
리튬은 저전위에서 알루미늄과 합금을 형성하여 집전체를 파괴하지만, 나트륨은 알루미늄과 합금을 형성하지 않습니다. 이 특성 덕분에 SIB는 음극 집전체로 알루미늄 박을 사용할 수 있으며, 이는 배터리 팩 수준의 에너지 밀도당 비용을 획기적으로 낮춥니다.

### 3.3 저온 및 안전성 우위
나트륨 이온은 액체 전해질 내에서 리튬보다 탈용매화(Desolvation) 에너지가 낮아 저온에서의 이온 전도도 유지에 유리합니다. 또한 과방전 시(0V) 집전체 용출 리스크가 적어 운송 및 보관 안정성이 우수합니다.

## 4. 진단 및 운영 프로토콜
- **Rate Fidelity Audit**: 입자 크기와 확산 계수를 연동하여 고출력 구동 시의 전압 강하를 수리적으로 예지.
- **Cycle Life Prediction**: 하드 카본의 층간 확장 스트레스를 분석하여 장기 사이클링 중의 용량 퇴화 기전 모델링.

## 5. 결론 (Deterministic Standard)
본 노드는 SIB의 소재 화학적 차별성과 경제성을 극대화하기 위한 물리적 기준을 제공합니다. 실제 에너지 밀도 및 원가 절감 지표 데이터는 인스턴스 로그에서 관리됩니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] Battery-Materials-and-Chemistry-Master-Guide]]
- [[[Concept] Battery-Storage-and-Grid-Intelligence-Hub]]
- [[[Data] Battery-SIB-Material-and-Cost-Performance-Log_2026-05-16]]