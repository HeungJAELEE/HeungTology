---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault / Display-Engineering-Group
  original_hash: 3d20335eba8520b08d3df9ae1ebe842a192679c3dcc454b320bde299b99ab762
metadata:
  ai_status: pending_review
  date: '2026-05-17'
  domain: 02_Battery
  id: '[[[Battery] W14_display-oled-evolution-tandem-oled-and-blue-phosphorescence]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: OLED의 수명 및 휘도 한계를 극복하기 위한 탠덤(Tandem) 구조 및 청색 인광(Blue PHOLED), 중수소 치환
    기술 명세
  object_type: Hardware
  tier: 1
properties:
  blue_pholed_eqe: '> 25%'
  single_driving_voltage: 3-5 V
  single_eqe: 20-30%
  single_peak_luminance: ~ 1,000 nits
  tandem_driving_voltage: 6-10 V
  tandem_eqe: 40-60%
  tandem_lifespan_multiplier: '> 4x'
  tandem_peak_luminance: '> 2,000 nits'
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 02_Battery]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Section 2.1'
  intent: empirical_validation
  object: '> 4x (vs Single-stack)'
  predicate: has_theoretical_limit
  subject: Tandem OLED Lifespan
  weight: 0.9
- evidence_coordinate: '[데이터 부재] Page 1'
  intent: technical_specification
  object: '> 25%'
  predicate: measured_value
  subject: Blue PHOLED EQE
  weight: 0.9
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

# [Battery] W14_display-oled-evolution-tandem-oled-and-blue-phosphorescence

## 1. 공학적 당위성 (Engineering Rationale)
OLED 엔지니어링의 핵심 과제는 전류 밀도($J$)와 수명($T_{50}$) 간의 비선형적 역상관 관계 제어입니다. 휘도($L$) 증폭을 위해 전류 밀도를 증가시킬 경우, 엑시톤 밀도 급증에 따른 열화(Burn-in)가 가속화됩니다. 이를 해결하기 위해 발광층을 수직 적층하여 전류 부하를 분산하는 **탠덤(Tandem) 구조**와 에너지 손실을 최소화하는 **청색 인광(Blue PHOLED)** 기술이 채택되었습니다.

## 2. 디스플레이 사양 및 비교 (Specifications)

| 항목 | 싱글 스택 (Single) | 탠덤 (2-Stack) | 청색 인광 (PHOLED) | 공학적 당위성 |
|:---|:---:|:---:|:---:|:---|
| **피크 휘도** | $\sim 1,000 \text{ nits}$ | **$> 2,000 \text{ nits}$** | High Efficiency | 스택 적층을 통한 선형적 증가 |
| **외부 양자 효율** | $20 \sim 30\%$ | **$40 \sim 60\%$** | **$> 25\%$ (Blue)** | 내부 양자 효율의 극대화 |
| **수명 ($T_{95}$)** | Base (1x) | **$> 4 \text{x}$** | Improved | 전류 분산에 의한 열화 억제 |
| **구동 전압** | $3 \sim 5 \text{ V}$ | **$6 \sim 10 \text{ V}$** | Moderate | CGL에 의한 전압 강하 포함 |

## 3. 핵심 메커니즘 분석
- **탠덤 구조 및 CGL**: 탠덤 구조의 핵심인 CGL은 전하를 생성하여 인접 발광층으로 주입합니다. 동일 전류 구동 시 발광층이 $n$개일 경우 전류 밀도는 $1/n$로 감소하여 유기물 결합 파괴를 지연시킵니다.
- **중수소(Deuterium) 치환**: 청색 광자의 고에너지는 C-H 결합 해리를 유발합니다. 수소를 중수소로 치환 시 결합 에너지 변화로 인해 번인(Burn-in)을 물리적으로 억제합니다.

## 4. [Skill] OLED Health Guardian
누적 사용량 맵을 기반으로 지수 열화 모델을 적용하여 번인을 예측하고, 적응형 감마 보정을 통해 휘도 균일도를 유지하는 최적화 로직을 포함합니다.

## 5. 검증 프로토콜 (Audit)
1. **CGL 계면 저항**: 저항($R_{CGL}$) 급증 시 구동 전압 상승 및 발열량 증가로 인한 열적 열화 가속 여부 확인.
2. **청색 인광 한계**: 높은 엑시톤 에너지에 의한 유기 결합 파괴를 중수소 치환으로 어느 정도 방어하는지 실측.
3. **고휘도 유지 근거**: 싱글 스택 대비 낮은 전류 밀도($J$) 사용으로 $T_{50}$ 수명을 확보하는 물리적 근거 검증.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] advanced-packaging-hbm4-hybrid-bonding]]
- [[[Concept] W12_thermal-management-in-ai-chips]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**