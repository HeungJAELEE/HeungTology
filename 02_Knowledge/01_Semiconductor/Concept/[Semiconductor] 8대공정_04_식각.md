---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: e448395ad9d9bca10f069ea302c50e62d9bb0102c87e4946592bb8cb452a434c
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] 8대공정_04_식각]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] 8대공정_04_식각에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  ale_node_threshold: 2nm
  industrial_ale_precision: 0.2~0.5nm
  industrial_anisotropy: 0.95~0.99
  industrial_cryogenic_temp: <-100C
  industrial_selectivity: 50:1~100:1
  theoretical_ale_precision: 0.1nm
  theoretical_anisotropy: '1.0'
  theoretical_cryogenic_temp: -150C
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

# [Semiconductor] 8대공정_04_식각

## 1. Functional Overview: Structural Pattern Formation
식각(Etching)은 포토패턴(Photo-pattern)된 PR을 마스크로 활용하여 하부 박막의 불요 영역을 제거함으로써 회로 기하 구조(Circuit Topology)를 확정하는 공정임 [Ref: Etch_Process_Standard]. 미세 공정화에 따른 소자 간 단락(Short) 방지 및 임계 치수(CD, Critical Dimension) 제어가 핵심 공정 목표임 [Ref: CD_Control_Protocol]. 특히 고적층 V-NAND 구조 내 채널 홀(Channel Hole)의 종횡비(Aspect Ratio) 확보가 수율(Yield)의 임계 요소임 [Ref: V-NAND_Yield_Report].

## 2. Mechanism Analysis: Reactive Ion Etching (RIE)
RIE는 화학적 반응성과 물리적 타격력을 결합하여 식각 효율을 최적화함 [Ref: RIE_Mechanism_Manual].

### 2.1 Component Synergy
* **Chemical Etching (Radical-based)**: 고반응성 라디칼(Radical)에 의한 등방성(Isotropic) 식각임 [Ref: Chemical_Etch_Theory]. 특정 물질과의 선택적 반응을 통해 휘발성 생성물을 형성하여 우수한 선택비(Selectivity)를 구현함 [Ref: Chemical_Etch_Theory].
* **Physical Etching (Ion-based)**: 가속된 이온(Ion) 충돌에 의한 이방성(Anisotropic) 식각임 [Ref: Physical_Etch_Theory]. 높은 방향성(Directionality)을 통해 수직 프로파일(Vertical Profile) 형성을 제어함 [Ref: Physical_Etch_Theory].
* **Synergistic Effect**: 수직 가속 이온이 표면 에너지를 활성화하여 라디칼 반응 속도를 국소적으로 증폭시킴으로써 고이방성 프로파일을 유지함 [Ref: RIE_Synergy_Report].

## 3. Technical Parameter Comparison

| Parameter | Theoretical (Ideal) | Verified (Industrial) | Reference |
| :--- | :--- | :--- | :--- |
| **Anisotropy ($A_{\text{f}}$)** | $1.0$ [Ref: Etch_Profile_Standard] | $0.95 \sim 0.99$ [Ref: Etch_Profile_Standard] | [Ref: Etch_Profile_Standard] |
| **Selectivity ($S$)** | $\infty$ [Ref: Material_Selectivity_Log] | $50:1 \sim 100:1$ [Ref: Material_Selectivity_Log] | [Ref: Material_Selectivity_Log] |
| **Cryogenic Temp** | $-150^{\circ}\text{C}$ [Ref: Cryo_Etch_Protocol] | $< -100^{\circ}\text{C}$ [Ref: Cryo_Etch_Protocol] | [Ref: Cryo_Etch_Protocol] |
| **ALE Precision** | $0.1\text{ nm}$ [Ref: ALE_Node_Spec] | $0.2 \sim 0.5\text{ nm}$ [Ref: ALE_Node_Spec] | [Ref: ALE_Node_Spec] |

## 4. Critical Phenomena & Mitigation

### 4.1 Loading Effect (Pattern Density Dependency)
패턴 밀도(Pattern Density) 편차에 따른 식각 속도 불균일(Non-uniformity) 현상임 [Ref: Loading_Effect_Control].
* **Macro-loading**: 웨이퍼 전체 패턴 밀도 변동에 따른 반응 가스(Etchant) 총 소모량의 변화임 [Ref: Loading_Effect_Control].
* **Micro-loading**: 미세 패턴 내부의 가스 유입 및 부산물(By-product) 배출 제한에 따른 국소적 식각 속도 저하임 [Ref: Loading_Effect_Control].
* **Mitigation**: 가스 유량 및 압력 정밀 제어, ESC(Electrostatic Chuck) 기반 온도 구배(Temperature Gradient) 보정 적용 [Ref: Loading_Effect_Control].

### 4.2 ARDE (Aspect Ratio Dependent Etch)
V-NAND 고적층화에 따른 종횡비(Aspect Ratio) 증가로 인한 식각 병목(Bottleneck) 현상임 [Ref: V-NAND_Yield_Report]. 종횡비 증가 시 이온 도달 확률 및 부산물 확산 속도 감소로 식각 속도가 저하됨 [Ref: ARDE_Physics_Log].
* **Solution: Cryogenic Etching**: $-100^{\circ}\text{C}$ [Ref: Cryo_Etch_Protocol] 이하의 극저온 환경에서 측벽 보호막(Passivation layer)을 강화하고 이온 직진성을 확보하여 고종횡비 구조를 식각함 [Ref: Cryo_Etch_Protocol].

## 5. Next-Generation Technology: ALE (Atomic Layer Etch)
$2\text{ nm}$ [Ref: ALE_Node_Spec] 이하 초미세 공정용 표준 기술로, 원자층 단위의 순차 식각을 수행함 [Ref: ALE_Standard_Procedure].
1. **Adsorption**: 표면 반응 가스 흡착을 통한 화학적 결합 형성 [Ref: ALE_Standard_Procedure].
2. **Desorption**: 에너지(Ion 등) 인가를 통한 흡착 원자층의 선택적 제거 [Ref: ALE_Standard_Procedure].
이를 통해 CD 손실(Loss)을 최소화하고 극도의 식각 균일도(Uniformity)를 달성함 [Ref: ALE_Node_Spec].