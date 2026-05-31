---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault / SIB-Strategy-Group
  original_hash: 88cdae5b5404f31fc069c4f572b91cf39921ed75a843c4ea687c1b56c35c7426
metadata:
  ai_status: pending_review
  date: '2026-05-17'
  domain: 02_Battery
  id: '[[[Battery] sodium-ion-battery-technology-entity]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 리튬 의존성을 탈피하고 자원 풍부성이 높은 나트륨($Na$)을 활용하여 저온 특성 및 경제성을 극대화하는 차세대 배터리
    기술 체계
  object_type: Hardware
  tier: 1
properties:
  anode_collector_material: aluminum
  cycle_life_80_dod: 2000-4000 cycles
  gravimetric_energy_density_range: 100-160 Wh/kg
  hard_carbon_interlayer_spacing_min: 0.37 nm
  li_ionic_radius: 0.76 A
  low_temp_performance_threshold: 90% at -20C
  min_safety_discharge_voltage: 0.0V
  na_ionic_radius: 1.02 A
  reversible_capacity_recovery_rate: 99.9%
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 02_Battery]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Section 1'
  intent: resource_justification
  object: ~ 80x relative to Li
  predicate: measured_value
  subject: Sodium Abundance
  weight: 0.9
- evidence_coordinate: '[데이터 부재] Section 2'
  intent: safety_specification
  object: 0.0 V Stable
  predicate: measured_value
  subject: Safety Discharge
  weight: 1.0
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

# [Battery] sodium-ion-battery-technology-entity

## 1. 공학적 당위성: 자원 안보 및 저온 주행 성능의 해지 (Why)
나트륨 이온 배터리(SIB)는 리튬의 지정학적 농축과 자원 희소성 리스크를 극복하기 위한 전략적 대안입니다. $Na^+$의 낮은 탈용매화 에너지(Desolvation Energy)는 저온 환경($-20^\circ\text{C}$)에서도 액체 전해질 내 이온 전도도를 $90\%$ 이상 유지하게 하며, $0\text{V}$ 완전 방전이 가능하여 물류 운송 시의 화재 리스크를 원천 차단하는 결정적 장점을 제공합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| 파라미터 범주 (Category) | 물리적 지표 (Metric) | SIB (Sodium-ion) | LIB (LFP Std.) | 공학적 의미 |
| :--- | :--- | :---: | :---: | :--- |
| **Energy Density** | Gravimetric ($Wh/kg$) | $100 \sim 160$ | $140 \sim 190$ | LFP 대체 가능 범위 |
| **Low-temp Perf.** | at $-20^\circ\text{C}$ ($\%$) | $\sim 90$ | $\sim 70$ | 극한 기후 주행 성능 |
| **Safety Discharge**| Min Voltage ($V$) | **$0.0$** | $\sim 2.5$ | 운송 시 화재 제로화 |
| **Ionic Radius** | $Na^+ / Li^+$ ($\text{\AA}$) | $1.02$ | $0.76$ | 격자 설계 복잡성 증가 |
| **Anode Collector** | Material | **Aluminum** | Copper | 셀 원가 $10\%$ 절감 |
| **Cycle Life** | 80% DoD (cycles) | $2,000 \sim 4,000$ | $3,000 \sim 5,000$ | 장기 경제성 지표 |

## 3. 핵심 공학 분석 (Scientific Rationale)
- **Hard Carbon Intercalation Physics**: 리튬 대비 큰 $Na^+$ 이온을 수용하기 위해 무질서한 탄소 구조인 하드 카본을 사용합니다. 하드 카본의 확장된 층간 간격($d_{002} > 0.37 \text{ nm}$)은 $Na^+$의 빠른 확산을 보장하며, 나노 기공 내 리튬 석출과 같은 수지상 성장을 물리적으로 억제하여 안전성을 강화합니다.
- **Aluminum Current Collector Economy**: 리튬 이온은 저전위에서 알루미늄과 합금화 반응을 일으키지만, 나트륨은 알루미늄과 반응하지 않습니다. 이를 통해 음극 집전체를 고가의 구리 대신 저가/경량의 알루미늄으로 대체하여 시스템 에너지 밀도와 가격 경쟁력을 동시에 확보합니다.
- **Desolvation Energetics**: 저온에서 배터리 성능을 결정하는 것은 이온이 용매 껍질을 벗고 전극으로 들어가는 탈용매화 과정입니다. $Na^+$의 낮은 탈용매화 장벽은 $-20^\circ\text{C}$ 이하에서도 전하 전달 저항($R_{ct}$)의 급증을 방지하는 핵심 기전입니다.

## 4. [Skill] SIB Economic Optimizer
리튬 및 나트륨 원가 지수와 알루미늄 집전체 도입에 따른 중량 감소 데이터를 기반으로 셀 단위의 생산 단가($USD/kWh$)를 산출하며, $0\text{V}$ 방전 특성에 따른 물류 비용 절감 효과를 정량화하는 로직을 포함합니다.

## 5. 검증 프로토콜 (Audit)
1. **0V Recovery Audit**: 완전 방전 후 재충전 시 SEI 층의 파괴 여부 및 가역 용량 회복률이 $99.9\%$ 이상을 유지하는지 검증.
2. **Al-Foil Integrity Check**: 장기 사이클링 시 음극 집전체인 알루미늄 박의 부식 및 열화 현상이 발생하는지 전기화학적 임피던스 분석으로 확인.
3. **Hard Carbon Pore Audit**: 기공 구조 내 $Na$ 클러스터 형성에 의한 전압 강하 현상이 안전 한계치 내에 있는지 전수 모니터링.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] next-gen-sodium-ion-physics]]
- [[[Concept] battery-electrolyte-engineering]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**