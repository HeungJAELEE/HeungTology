---
metadata:
  date: "2026-05-17"
  id: "[[[Battery] conductive-additives-carbon-black-cnt-graphene]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "02_Battery"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault / Additive-Science-Group"
  original_hash: "2195d6e5c6fcce4055b4fcc611262ee2b69a729b362dea859cb86801f438658b"
object:
  object_type: "Concept"
  tier: 1
  description: '활물질의 저전도성을 보완하기 위한 전자 전송 네트워크(ETN) 구축 및 퍼콜레이션 임계점 최적화 설계'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 02_Battery]]"
  alternative_parents: []
spo_graph:
  - subject: "CNT Percolation"
    predicate: "measured_value"
    object: "0.1 ~ 1.5 wt%"
    evidence_coordinate: "[Ref: CNT_Res_2024] Section 1"
    evidence_hash: "2195d6e5c6fc"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
  - subject: "SWCNT Strain"
    predicate: "measured_value"
    object: "300 %"
    evidence_coordinate: "[Ref: Si_Anode_Spec] Section 2"
    evidence_hash: "2195d6e5c6fc"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---



# [Battery] conductive-additives-carbon-black-cnt-graphene

## 1. 공학적 당위성: 전자 전송 네트워크 (Why)
활물질의 저전도성(Low Conductivity) 보완을 위한 전자 전송 네트워크(ETN) 구축이 주 목적입니다. 도전재 최적화는 투입량 최소화를 통해 활물질 점유 부피를 극대화하고 셀 에너지 밀도(Energy Density)를 제고하는 데 핵심적입니다. 특히 실리콘(Si) 음극의 부피 팽창(Volume Expansion) 환경에서 전기적 연속성(Electrical Continuity)을 유지하는 기술적 신뢰성 확보가 설계의 핵심 요구사항입니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| 도전재 유형 (Type) | 차원 (Dim) | 종횡비 (Aspect Ratio) | 질량 분율 (wt%) | 공학적 의미 (Rationale) |
| :--- | :---: | :---: | :---: | :--- |
| **0D (Carbon Black)** | Point | 1 : 1 | $5 \sim 10\%$ | 국부 접촉, 저비용 |
| **1D (CNT)** | Line | $> 1000 : 1$ | $0.1 \sim 2\%$ | 장거리 네트워크, Si-anode 지지 |
| **2D (Graphene)** | Plane | High Surface Area | $1 \sim 3\%$ | 평면 접촉, 고출력 최적화 |

## 3. 핵심 공학 분석 (Scientific Rationale)
- **Percolation Threshold Model**: 전도성 네트워크 형성 임계점은 $\sigma = \sigma_0 (\phi - \phi_c)^t$ 수리 모델을 따릅니다. CNT는 1D 고종횡비 특성으로 인해 Carbon Black 대비 현저히 낮은 농도($< 1\%$)에서 임계점($\phi_c$)에 도달하여 활물질 로딩 공간을 확보합니다.
- **Mechanical Bridge Logic**: SWCNT(Single-Walled CNT)는 극대화된 인장 강도를 기반으로 실리콘 음극이 팽창할 때 전기적 경로를 유지하는 교량 역할을 수행합니다. 약 $300\%$의 변형률(Strain) 환경에서도 전기적 연속성을 사수합니다.

## 4. [Skill] Additive Fidelity Engine
바인더 시스템 내 슬러리의 유변학적 데이터를 분석하여 도전재의 분산 무결성(Dispersion Integrity)을 평가하며, 응집(Agglomeration) 감지 시 국부 저항 상승 리스크를 예지하는 진단 로직을 포함합니다.

## 5. 검증 프로토콜 (Audit)
1. **Percolation Verification**: 도전재 함량 변화에 따른 시트 저항($\Omega/\text{sq}$) 매핑을 통해 이론적 임계점과 실측치의 정합성 확인.
2. **Dispersion Stability**: 제타 전위 및 입도 분포(DLS) 데이터를 근거로 CNT 분산액의 장기 저장 안정성 검증.
3. **C-rate Impact**: 고출력 방전 조건에서 0D/1D 하이브리드 도전재 시스템이 리튬 이온 수송 속도에 미치는 가속 효과 실측.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] battery-binder-intelligence-and-slurry-rheology]]
- [[[Concept] material-anode-synthesis]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**
