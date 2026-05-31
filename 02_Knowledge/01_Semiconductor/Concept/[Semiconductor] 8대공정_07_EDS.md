---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 8887160e9a2804dfcd78b02a208112749e2906033065ea556f7976fcb0a0c2b0
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] 8대공정_07_EDS]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] 8대공정_07_EDS에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  critical_failure_mode: false_fail
  high_parallel_test_threshold: 512 units/cycle
  min_testing_throughput: 512 units/cycle
  quality_standard: known_good_die
  theoretical_contact_resistance: 0 Ohm
  theoretical_yield_recovery: 100%
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 반도체_백서_통합_지휘소]]'
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

# [Semiconductor] 8대공정_07_EDS

## 1. Functional Definition & Economic Impact
EDS(Electrical Die Sorting)는 웨이퍼 내 개별 Die의 전기적 특성 검증을 통한 양품 선별 공정임 [Ref: EDS Economic Model]. 불량 Die 조기 식별을 통해 후속 패키징 공정의 비용 손실을 차단하며, 수율(Yield) 데이터를 전 공정(Front-end)으로 피드백하여 공정 안정성을 제어하는 'Yield Gatekeeper' 역할을 수행함 [Ref: EDS Economic Model].

## 2. Technical Mechanism
### 2.1 Wafer Probing
Probe Card의 Micro-needle을 Die Pad에 접촉시켜 전기적 신호를 인가/수집함 [Ref: Contact Protocol].
- **Parametric Test**: 트랜지스터 전기적 특성($V, I$ 등)의 설계 사양(Design Specification) 준수 여부 검증.
- **Functional Test**: 설계 로직 패턴 입력을 통한 회로의 논리적 동작 무결성 확인.
- **Binning**: 테스트 결과 기반 Die 성능 등급 분류 및 불량 Die의 Repair/폐기 할당.

## 3. Comparative Analysis: Theoretical vs. Verified
| Parameter | Theoretical (Ideal) | Verified (Actual/Empirical) |
| :--- | :--- | :--- |
| Yield Recovery | $100\%$ | $\Delta\text{Yield}$ via Redundancy/Repair [Ref: Repair Tech] |
| Contact Resistance ($R_{\text{c}}$) | $0\ \Omega$ | Controlled via Probe Force [Ref: Contact Protocol] |
| Testing Throughput | $\infty$ | $\ge 512\ \text{units/cycle}$ [Ref: High-Parallel Trend] |

## 4. Critical Engineering Challenges
### 4.1 Redundancy-based Repair
메모리 수율 극대화를 위한 핵심 기술임. 불량 셀(Cell) 발생 시, 설계된 여분 회로(Redundancy)로 경로를 재구성하여 기능을 복원함 [Ref: Repair Tech]. 레이저 또는 전기적 퓨즈를 통한 배선 재연결로 폐기 대상 Die를 양품화함 [Ref: Repair Tech].

### 4.2 Contact Resistance ($R_{\text{c}}$) Management
Probe Tip과 Die Pad 간 접촉 저항($R_{\text{c}}$) 제어는 테스트 신뢰성의 임계 요소임 [Ref: Contact Protocol]. $R_{\text{c}}$가 설계 임계치를 초과하여 불안정할 경우, 신호 감쇄에 의한 'False Fail'이 발생하여 수율 지표를 왜곡함 [Ref: Contact Protocol]. 정기적인 Probe Tip 세정 및 Probe Force 제어가 필수적임 [Ref: Contact Protocol].

### 4.3 HBM & KGD (Known Good Die) Requirement
HBM(High Bandwidth Memory) 적층 구조에서 EDS 신뢰성은 공정 성패를 결정함 [Ref: HBM Quality Standard]. 적층 후 단일 Die 불량은 전체 패키지의 폐기로 직결되므로, 적층 전 단계에서 개별 Die의 무결성을 검증하는 KGD(Known Good Die) 확보가 필수적임 [Ref: HBM Quality Standard].

## 5. 2026 Technology Roadmap
- **High-Parallel Test**: 단일 사이클당 $\ge 512\ \text{units/cycle}$ 이상의 Die를 동시 검증하는 병렬화 기술 고도화 [Ref: High-Parallel Trend].
- **AI-driven Yield Inference**: EDS 빅데이터 기반 머신러닝 모델을 활용하여 전 공정(Photo, Etch 등)의 결함 발생 지점을 실시간 추론하는 지능형 수율 관리 시스템 도입 [Ref: AI Yield Prediction].