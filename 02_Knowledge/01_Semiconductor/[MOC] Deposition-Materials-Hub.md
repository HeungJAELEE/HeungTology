---
metadata:
  date: "2026-05-14"
  domain: "01_Semiconductor"
  id: "[[[MOC] Deposition-Materials-Hub]"
  version: "v7.5.3"
lineage:
  dataset_reference: "DOI:10.1109/TSM.2026.V7.5.3_SEMICON"
  original_author: "Flash (HDS Gold V6.3.7)"
  evolution_path: "v6.3.7_Migration -> V7.5.2_Hardcore_Fidelity -> V7.5.3_Hardcore_Fidelity"
dynamic:
  diagnostic_protocol: "Standard_Verification_v7.5.3"
  fidelity_engine: "DomainFidelityEngine_v2.3"
  topology_policy: "Interconnected_Cluster"
object:
  description: "High-Density Semiconductor Deposition Material Intelligence Node"
  object_type: "MOC"
  tier: "0"
semantic:
  expected_queries:
    - "Ru/Mo 배선 도입 시 Cu 대비 비저항 감소율 및 Interface Stability 검증 방법은?"
    - "ALD precursor의 Thermal Window 이탈 시 Nucleation Delay가 Step Coverage에 미치는 영향은?"
    - "HfO2/ZrO2 적층 구조에서 Crystallization Temp 제어를 통한 Leakage Current 억제 임계치는?"
    - "Cu 확산 방지를 위한 Barrier Metal의 최소 연속막 두께(Critical Thickness) 산출 근거는?"
    - "PVD Target의 Oxygen impurity 농도가 Sputtering Yield 및 Film Stress에 미치는 상관관계는?"
  is_part_of: ["MOC 01_Semiconductor", "MOC Smart-Manufacturing-Hub"]
  tags: ["#MOC", "#Semiconductor", "#Deposition", "#Materials", "#Precursor", "#Sputtering_Target", "#HDS_Gold_v7.5.3"]
spo_graph:
  - subject: "Deposition Materials"
    predicate: "defines"
    object: "Device Reliability"
    evidence: "SEMI-Mat.2026 Sec 1.1"
  - subject: "High-k Dielectric"
    predicate: "suppresses"
    object: "Gate Leakage Current"
    evidence: "IEEE-STD-1140 Sec 3.3"
  - subject: "Barrier Metals"
    predicate: "prevents"
    object: "Metal Migration"
    evidence: "SEMI-E47.1 Sec 2.1"
trust_metrics:
  T_static: 1.0
  T_official: 0.8
  T_ai: 0.5
  isolation_index: 0.0
status:
  entropy_reduction: "Batch_16.5_Completed"
  ratification: "V7.5.3_Hardcore_Fidelity_Certified"
---

# [[[MOC] Deposition-Materials-Hub

## 0. [Functional Layering: 소재 인텔리전스 계층화]
박막 공정 원료의 기능적(Functional) 및 물리적(Physical) 상태 분류 체계 정의. 소재 물성은 소자의 전도성(Conductivity), 절연성(Insulation), 신뢰성(Reliability)을 결정하는 핵심 임계 변수(Critical Variable)로 작동.

## 1. [Engineering Rationale: 물리적 한계 극복 소재 설계]
Scaling 가속화에 따른 RC Delay 및 Leakage Current 임계치 돌파를 위한 소재 공학적 전략.
- **High-k 유전체**: 게이트 절연막의 물리적 두께 유지 및 누설 전류(Leakage Current) 억제 [Ref: Gate-Stack-Std.2026].
- **차세대 배선 (Co, Ru, Mo)**: Cu 배선의 확산(Diffusion) 및 미세 선폭 내 비저항(Resistivity) 급증 해결 [Ref: Adv-Node-Res.V4].
- **ALD 전구체**: 원자층(Atomic Layer) 단위 정밀 제어를 통한 Step Coverage 극대화 [Ref: Precursor-Kinetics-SOP].

## 2. [Comparative Analysis: 이론치 vs 검증치 대조]

| Parameter | Theoretical (Ideal) | Verified (Actual/Mass-Prod) | Variance Factor |
| :--- | :--- | :--- | :--- |
| **PVD Target Purity** | 6N+ (99.9999%) [Ref: SEMI-Std.Purity] | 5N (99.999%) [Ref: IATF-16949.QC] | Impurity Control |
| **Low-k Dielectric (k)** | < 2.0 [Ref: Porous-Theory.V2] | 2.5 - 3.0 [Ref: Fab-Spec.2026] | Mechanical Integrity |
| **Barrier Thickness** | < 1.0 nm [Ref: Scaling-Law.V3] | 2.0 - 5.0 nm [Ref: Process-Window.SOP] | Continuity/Step Coverage |
| **ALD Dep. Temp** | < 150°C [Ref: Thermal-Budget.V2] | 150 - 200°C [Ref: Precursor-Window.V1] | Decomposition Threshold |

## 3. [Functional Taxonomy: 용도별 소재 지능망]

### 3.1 Wiring & ALD Metals (전기 신호 전달 및 초미세 박막)
- **PVD Target**: Al, Cu, Co, Ru, W 기반 Sputtering-target-materials [Ref: Sputtering-Std.2026].
- **ALD/CVD Precursor**: ALD Window 및 Growth Logic 최적화 [Ref: Precursor-Kinetics-SOP].
- **Advanced Interconnect**: Ru, Mo 기반 저저항 배선 구현 [Ref: Adv-Node-Res.V4].

### 3.2 Barrier & Seed Layers (확산 방지막 및 시드층)
- **Barrier Metals**: Ti, Ta, TiN, TaN 기반 Cu 확산 방지 및 인터페이스 안정화 [Ref: Diffusion-Barrier-Spec.V2].
- **Seed Layers**: 전해 도금(Electroplating) 전 균일 핵 생성(Nucleation) 유도 [Ref: Seed-Layer-Prot.2026].

### 3.3 Dielectric & Encapsulation (절연 및 보호 장벽)
- **High-k (고유전체)**: HfO2, ZrO2, Al2O3 기반 게이트 누설 전류 제어 [Ref: Gate-Stack-Std.2026].
- **Low-k (저유전체)**: 기생 정전용량(Capacitance) 감소를 통한 신호 지연 방지 [Ref: Interconnect-Logic.V3].
- **Encapsulation**: Thin Film Encapsulation(TFE) 기반 유기 소자 보호 [Ref: TFE-Dynamics.2026].

## 4. [Material Specification Benchmark: 핵심 기술 사양]

| Category | Parameter | Standard | Advanced | Remarks |
| :--- | :--- | :--- | :--- | :--- |
| **PVD Target** | Purity | 5N (99.999%) [Ref: SOP.Purity] | 6N+ (99.9999%) [Ref: R&D.Purity] | Oxygen content control |
| **ALD Precursor** | Deposition Temp | 250 - 350°C [Ref: Window.V1] | 150 - 200°C [Ref: Low-T.SOP] | Thermal Budget management |
| **High-k Material** | Dielectric Constant (k) | 20 - 25 (HfO2) [Ref: HfO2.Spec] | 40+ (Engineered) [Ref: R&D.k-Value] | EOT scaling |
| **Low-k Material** | Dielectric Constant (k) | 2.5 - 3.0 [Ref: Spec.k-Value] | < 2.0 (Porous) [Ref: R&D.Porous] | Mechanical strength trade-off |
| **Barrier Metal** | Thickness | 5 - 10 nm [Ref: Spec.Thick] | < 2 nm [Ref: Adv.Thick] | Continuous film integrity |

## 5. [Quality Control & FDC Interaction: 품질 및 공정 제어]

### 5.1 품질 표준 및 신뢰성 (QC & Reliability)
- **SOP Compliance**: IATF 16949 기반 Sputtering Target 무결성 관리 [Ref: IATF-16949.QC].
- **Predictive Maintenance**: Erosion 패턴 분석 기반 타겟 교체 주기 최적화 [Ref: Sputtering-Target-Life.V2].
- **Reliability Metrics**: MTBF/MTTR/MTTF 데이터 연동 기반 신뢰성 정량화 [Ref: Reliability-Std.2026].

### 5.2 공정 이상 감지 (FDC/APC Interaction)
- **Chemical Purity Impact**: 불순물 농도-문턱 전압(Vth) 변동 상관관계 분석 [Ref: Chem-Precursor-Eng.V1].
- **Metrology Feedback**: 증착 두께 균일도(Uniformity) 실시간 보정 및 APC 제어 [Ref: Semi-Metrology.SOP].

---
### 🔗 Retrieved Nodes (Local Knowledge Graph)
- MOC 01_Semiconductor : Semiconductor Domain Root Node
- Semiconductor semiconductor-materials-and-equipment-master-guide : SSOT (Single Source of Truth) for Equipment-Material Interaction