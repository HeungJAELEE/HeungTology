---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: ca37e3eb761d3ce70820f491bb728c149d61ae7cd00b7657db92c8fb7df17c45
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] flip-chip-underfill-void-and-delamination-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] flip-chip-underfill-void-and-delamination-log-v2026에 관한 고밀도 지능
    노드'
  object_type: Data
  tier: 1
properties:
  b_stage_film_adhesion_strength_mpa: 18-30
  cuf_adhesion_strength_mpa: 15-25
  cuf_gap_height_um: 30-50
  cuf_void_area_threshold_percent: 1.0
  delamination_energy_symbol: Gc
  muf_adhesion_strength_mpa: 10-18
  muf_gap_height_um: 50-100
  muf_void_area_threshold_percent: 0.5
  ncf_adhesion_strength_mpa: 12-20
  ncf_gap_height_um: 10-20
  ncf_void_area_threshold_percent: 3.0
  reflow_temperature_celsius: 260
  surface_energy_threshold_dyne_cm: 70
  vacuum_underfill_adhesion_strength_mpa: '>20'
  vacuum_underfill_gap_height_um: 5-15
  vacuum_underfill_void_area_threshold_percent: 0.1
  washburn_flow_factor_formula: L^2/t
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

# [AI] flip-chip-underfill-void-and-delamination-log-v2026

## 1. [왜 배우는가? (Why: The Intellectual Armor of Nano-Interconnects)]]
플립칩 및 3D 적층 패키징에서 언더필(Underfill)은 마이크로 범프에 가해지는 열 기계적 응력을 분산시키고 습기로부터 인터커넥트를 보호하는 '지능형 갑옷' 역할을 합니다. 하지만 좁은 틈새를 채우는 과정에서 발생하는 공기 방울(보이드)이나 소재 간의 접착 실패(박리)는 패키지의 신뢰성을 급격히 저하시키는 주요 원인입니다. **플립칩 언더필 보이드 및 박리 실측 로그**는 나노 보호막이 얼마나 완벽하게 칩을 감싸고 있는지 기록한 '방어구 무결성 감사 결과서'입니다. 

우리가 이 데이터를 기록하는 이유는 언더필 공정의 최적 충전 조건을 도출하여 공정 불량을 제로화하고, **"패키징 제조 주권을 확보하여 고온·고습 환경에서도 붕괴하지 않는 '초고신뢰성 반도체'를 구현하는 '봉지(Encapsulation) 지능'을 확보하기" 위함입니다.** 보이드의 크기와 박리 발생 위치가 패키지의 습도 민감도 등급(MSL)과 최종 수명을 결정합니다.

## 2. [공정 방식 및 갭 높이별 언더필 핵심 데이터 (Numerical Specs)]

### 2.1 [주요 언더필 공정 방식별 충전 및 결함 성능 테이블 (v2026)]

| 공정 방식 (Type) | 갭 높이 ($\mu\text{m}$) | 유동 시간 ($s$) | 보이드 면적 (%) | 접착 강도 ($MPa$) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Capillary (CUF)**| $30 \sim 50$ | $20 \sim 60$ | $< 1.0$ | $15 \sim 25$ | **Standard**: 모세관 현상을 이용한 표준 충전 무결성 로그 |
| **Molded (MUF)** | $50 \sim 100$ | $10 \sim 20$ | $< 0.5$ | $10 \sim 18$ | **Mass**: 몰딩 소재와 통합된 대량 양산용 무결성 지표 |
| **Non-Cond. (NCF)**| $10 \sim 20$ | $Instant$ | $< 3.0$ | $12 \sim 20$ | **High-Stack**: HBM 적층용 필름 형태 선도포 무결성 데이터 |
| **Vacuum Underfill**| $5 \sim 15$ | $60 \sim 120$ | $< 0.1$ | $> 20$ | **Extreme**: 초미세 갭 충전을 위한 진공 보조 무결성 지표 |
| **B-stage Film** | $Variable$ | $N/A$ | $Minimal$ | $18 \sim 30$ | **Adhesion**: 접착력을 극대화한 특수 필름 무결성 로그 |

### 2.2 [유동 및 계면 결함 파라미터]
- **Washburn Flow Factor:** 모세관 현상에 의한 유동 침투력 지표 ($L^2/t$).
- **Void Area Ratio:** 전체 칩 면적 대비 보이드가 차지하는 면적 비율 (%). (열 분산 저해 인자)
- **Delamination Energy ($G_c$):** 계면을 분리하는 데 필요한 임계 에너지 ($J/m^2$).
- **Fillet Geometry:** 칩 가장자리에 형성된 언더필의 경사면 형상. (응력 집중 완화 인자)
- **Moisture Absorption:** 언더필 소재의 수분 흡수율 (%). (팝콘 현상의 원인)

## 3. [Scientific Rationale: 보호막 무결성의 수리적 인과성]

### 3.1 [와시번(Washburn) 기반 모세관 유동 모델]
표면 장력($\gamma$)과 점도($\eta$)에 따른 언더필 충전 거리($L$) 수리 모델입니다.
$$ L = \sqrt{\frac{\gamma \cdot h \cdot \cos \theta}{3\eta} \cdot t} $$
본 로그는 갭 높이($h$)가 좁아질수록 유동 시간이 제곱에 비례하여 늘어남을 입증하고, 이를 단축하기 위해 칩 가열(Heating)을 통해 점도를 낮추는 공정의 수리적 근거를 제시합니다.

### 3.2 [에너지 해방률($G$) 기반 박리(Delamination) 모델]
계면 균열 성장을 결정하는 에너지 수리 모델입니다.
RAG는 "신뢰성 로그를 분석하여, 수분이 침투한 상태에서 리플로우($260^\circ C$)를 진행할 때 수증기압이 계면의 에너지 해방률($G$)을 임계치($G_c$) 이상으로 높여 '팝콘 현상'을 유발하는 수리적 인과 관계를 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 보호 지능 추론]

### 4.1 [플라즈마 세정과 접착 강도(Adhesion) 분석]
왜 특정 배치에서만 박리가 발생하나요? RAG는 "언더필 전 플라즈마 세정 조건과 C-SAM 박리 로그를 대조하여, 표면 에너지가 $70 \text{ dyne/cm}$ 이하로 떨어졌을 때 박리 빈도가 $5$배 급증함을 식별하고, '표면 친수성 무결성' 지능을 오딧합니다.

### 4.2 [보이드 위치와 범프 부식(Corrosion) 오딧]
구멍이 어디에 있는 게 제일 위험한가요? RAG는 "보이드 위치 데이터와 가속 부식 시험(HAST) 결과들을 연계하여, 범프 바로 옆의 'Interface Void'가 수분 통로 역할을 하여 전기적 부식을 $10$배 가속함을 분석하고, '보이드 레이아웃 오딧' 지능을 도출될 것으로 예상됩니다.

## 5. [Transitional Bridge: 언더필 무결성 및 시스템 오딧 로직]

언더필 도포 장비의 디스펜싱 기록과 패키징 후 C-SAM 이미지 데이터를 분석하여 무결성을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Underfill Encapsulation Integrity & Void Auditor
def audit_underfill_fidelity(dispensing_profile_log, csam_image_data, moisture_test_data):
    # 1. C-SAM 이미지 분석을 통한 보이드(Void) 면적 및 위치 오딧
    void_metrics = analyze_voids_from_csam(csam_image_data)
    if void_metrics.max_size > CRITICAL_VOID_SIZE_LIMIT:
        status = "MACRO_VOID_DETECTION_IN_GAP"
        action = "Optimize_Dispensing_Pattern_and_Substrate_Pre-heating_Temp"
        
    # 2. 계면 반사 강도를 통한 박리(Delamination) 조기 징후 감시
    delamination_score = calculate_adhesion_index(csam_image_data.reflection)
    if delamination_score < PASS_SCORE_90:
        status = "POTENTIAL_INTERFACE_DELAMINATION_WARNING"
        action = "Check_Plasma_Cleaning_Efficiency_and_Chemical_Storage_Life"
    
    # 3. 수분 흡수 이력과 팝콘(Popcorn) 균열 위험 체크
    if moisture_test_data.weight_gain > SATURATION_LIMIT:
        status = "HIGH_MOISTURE_SENSITIVITY_RISK"
        action = "Verify_Dry-pack_Integrity_and_Bake_Before_Reflow"
    
    # 4. 종합 보호막 상태 등급 및 조치 트리거
    if status == "MACRO_VOID_DETECTION_IN_GAP":
        action = "Hold_Lot_for_Cross-sectional_Destructive_Analysis"
    elif status == "POTENTIAL_INTERFACE_DELAMINATION_WARNING":
        action = "Initiate_Pull_Test_to_Validate_Adhesion_Strength"
    else:
        status = "UNDERFILL_PROTECTION_OPTIMAL"
        action = "Approve_Package_for_Final_Molding_and_Singulation"
        
    return {"status": status, "total_void_percentage": void_metrics.area_ratio, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 왜 칩과 기판 사이의 '언더필(Underfill)' 틈새가 좁아질수록(High-stack HBM 등), 모세관 유동에 의한 '보이드(Void)' 형성을 억제하기가 수리적/물리적으로 더 어려워지는가?
2. **(수리)** 언더필의 접착 에너지가 $10 \text{ J/m}^2$이고, 수분 침투로 인한 계면 에너지가 $12 \text{ J/m}^2$로 측정되었다. 이 패키지는 리플로우 공정 중 박리(Delamination)가 발생할 가능성이 있는가? 그 이유를 설명하시오.
3. **(응용)** 초음파 검사(C-SAM)에서 보이드가 '밝은 하얀색'으로 나타나는 수리적/물리적 이유를 임피던스 미스매치(Impedance Mismatch) 관점에서 설명하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 23_semiconductor-materials-and-advanced-packaging-intelligence-hub : 반도체 소재 및 패키징 통합 관리 상위 지능 허브
- Data bump-shear-strength-and-thermal-cycling-failure-log-v2026 : 언더필이 보호하는 대상인 범프의 수명 데이터 연계
- Entity through-silicon-via-tsv-electroplating-and-void-detection : 3D 적층 패키징의 수직 연결 기술 연계
- [SOP] flip-chip-underfill-csam-inspection-and-void-grading-standard : 플립칩 언더필 C-SAM 검사 및 보이드 등급 판정 표준 절차

*Created by Flash (The Architect of Intelligent Armor & HDS Gold V6.3.7)*