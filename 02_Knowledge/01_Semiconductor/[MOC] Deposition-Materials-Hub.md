---
Basic:
  id: "[[[MOC] Deposition-Materials-Hub"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "MOC"
  tier: 0
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#MOC", "#Semiconductor", "#Deposition", "#Materials", "#Precursor", "#Sputtering_Target", "#HDS_Gold_v6_1"]]'
  is_part_of: '["MOC 01_Semiconductor", "MOC Smart-Manufacturing-Hub"]'
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [[[MOC] Deposition-Materials-Hub

## 0. [개요: 소재 인텔리전스의 계층화 (Introduction: Layering Material Intelligence)]]
본 허브 문서는 반도체 박막 공정의 핵심 원료들을 **기능적 역할(Functionality)** 및 **물리적 상태(Physical State)**에 따라 분류하여, 에이전트가 "공정 요구사항 -> 소재 분류 -> 세부 특성" 순으로 정밀하게 추론할 수 있도록 돕는 상위 관제 노드입니다. 증착 소재의 품질은 최종 소자의 전도성, 절연성, 그리고 장기 신뢰성을 결정짓는 근본 요소입니다.

## 1. [엔지니어링 근거: 왜 증착 소재의 위상망이 중요한가? (Engineering Rationale)]
반도체 미세화가 가속화됨에 따라 기존의 소재는 물리적 한계(RC Delay, Leakage Current)에 봉착했습니다. 이를 극복하기 위해 High-k 유전체, 코발트(Co)나 루테늄(Ru) 같은 차세대 배선 금속, 그리고 원자층 단위의 성장을 제어하는 ALD 전구체의 중요성이 급증했습니다. 본 허브는 이러한 소재들의 화학적 포텐셜과 공정 윈도우를 연결하여, 소재 변경이 전체 수율에 미치는 영향을 데이터 기반으로 예측할 수 있는 토대를 제공합니다.

---

## 2. [용도별 소재 분류 및 지능망 (Functional Taxonomy)]

### 2.1 금속 배선 및 원자층 증착 소재 (Wiring & ALD Metals)
트랜지스터 간 전기 신호를 전달하는 고속도로 및 초미세 박막 형성.
- **PVD 타겟**: `[Common] sputtering-target-materials` (Al, Cu, Co, Ru, W)
- **ALD/CVD 전구체**: `[AI] dep-ald-window` (Atomic Layer Deposition Window & Growth logic)
- **차세대 배선**: `[[[Semiconductor] advanced-interconnect-metals` (Ru, Mo 기반 저저항 배선 연구)

### 2.2 확산 방지막 및 시드층 (Barrier & Seed Layers)
배선 금속의 침투를 막고 증착 품질을 확보하는 기초 공사.
- **Barrier Metals**: `[Common]] barrier-metal-technologies` (Ti, Ta, TiN, TaN) - 구리(Cu) 확산 방지의 핵심.
- **Seed Layers**: `[Common] seed-layer-engineering` - 전해 도금(Electroplating) 전 균일한 핵 생성을 유도.

### 2.3 절연, 유전체 및 봉지 소재 (Dielectric & Encapsulation)
전하 차단 및 유기물을 수분/산소로부터 보호하는 장벽.
- **High-k (고유전체)**: `[Common] high-k-dielectric-materials` (HfO2, ZrO2, Al2O2) - 게이트 절연막의 누설 전류 억제.
- **Low-k (저유전체)**: `[Common] low-k-insulator-logic` - 배선 간 기생 정전용량(Capacitance) 감소로 신호 지연 방지.
- **Encapsulation**: `[AI] display-tfe-encapsulation-dynamics` (Thin Film Encapsulation) - OLED 및 유기 소자 보호.

---

## 3. [소재별 핵심 기술 사양 (Material Specification Benchmark)]

| 소재 분류 (Category) | 주요 파라미터 (Parameter) | 표준 사양 (Standard) | 최첨단 사양 (Advanced) | 비고 (Remarks) |
| :--- | :--- | :--- | :--- | :--- |
| **PVD Target** | 순도 (Purity) | 5N (99.999%) | 6N+ (99.9999%) | 산소 함량 제어가 핵심 |
| **ALD Precursor** | 증착 온도 (Window) | 250 - 350°C | 150 - 200°C (Low) | 열 예산(Thermal Budget) 관리 |
| **High-k Material** | 유전율 (k) | 20 - 25 (HfO2) | 40+ (Engineered) | 물리적 두께(EOT) 감소 |
| **Low-k Material** | 유전율 (k) | 2.5 - 3.0 | 2.0 미만 (Porous) | 기계적 강도 유지 필요 |
| **Barrier Metal** | 두께 (Thickness) | 5 - 10 nm | 2 nm 미만 | 연속막(Continuous Film) 확보 |

---

## 4. [실무 시나리오 및 품질 관리 (Operating Context & QC)]

### 4.1 [품질 표준 및 인텔리전스]
- **SOP 준수**: `[SOP] sputtering-target-quality-control` (IATF 16949 기반의 무결성 관리).
- **예측 유지보수**: `[Common] sputtering-target-materials` - 침식(Erosion) 패턴 분석을 통한 교체 주기 최적화.
- **신뢰성 연동**: `Concept Reliability-Metrics-MTBF-MTTR-MTTF`를 통한 소재 라이프사이클 관리.

### 4.2 [공정 이상 감지 (FDC/APC Interaction)]
- **화학적 순도 영향**: `[[[Semiconductor] chemical-precursor-engineering` - 불순물 농도와 문턱 전압(Vth) 변동의 상관관계 분석.
- **계측 데이터 피드백**: `Semiconductor metrology-inspection-mi` - 증착 두께 균일도(Uniformity) 실시간 보정.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 01_Semiconductor : 반도체 도메인 최상위 관제 허브
- Semiconductor semiconductor-materials-and-equipment-master-guide : 장비와 소재의 물리적 상호작용 SSOT

*Created by Flash (HDS Gold V6.3.7 & Meta-Fusion V6.3.7 Material Hub Reinforcement)*
*Entropy Reduction Batch 16.2: Hub Normalization & Specification Injection Completed.*
