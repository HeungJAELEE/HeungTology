---
metadata:
  id: "[[[AI] interferometer-wafer-flatness-measurement-log-v2026]]"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[AI] interferometer-wafer-flatness-measurement-log-v2026에 관한 고밀도 지능 노드"
semantic:
  tags: ["#03_AI_Data", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [AI] interferometer-wafer-flatness-measurement-log-v2026

## 1. [왜 배우는가? (Why: The Geometry of Perfect Plane)]]
반도체 미세 공정에서 노광 장비의 초점 심도(Depth of Focus)는 수백 나노미터에 불과합니다. 만약 $300mm$ 웨이퍼 전체의 평탄도가 확보되지 않는다면, 웨이퍼의 중심은 초점이 맞지만 가장자리는 흐릿해져 패턴 형성이 불가능해집니다. **간섭계 웨이퍼 평탄도 실측 로그**는 빛의 파동 간섭 현상을 이용하여 웨이퍼 전면의 굴곡을 등고선처럼 시각화하고 기록한 '광학적 평면 품질 성적표'입니다. 

우리가 이 데이터를 기록하는 이유는 웨이퍼의 거시적 변형(Bow, Warp)과 미시적 평탄도(TIR)를 정밀 분석하여 노광 수율을 극대화하고, **"초정밀 계측 주권을 확보하여 나노 공정의 물리적 한계를 데이터로 통제하기" 위함입니다.** 평탄도의 무결성이 반도체 회로의 선폭 정밀도를 결정합니다.

## 2. [웨이퍼 등급 및 공정별 평탄도 핵심 데이터 (Numerical Specs)]

### 2.1 [웨이퍼 상태 및 측정 파라미터별 평탄도 테이블 (v2026)]

| 웨이퍼 상태 (Sample State) | 측정 기법 (Method) | TIR ($\mu\text{m}$) | TTV ($\mu\text{m}$) | Bow/Warp ($\mu\text{m}$) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Prime Wafer (As-is)** | PSI (Standard) | $0.25$ | $0.85$ | $12.5$ | **Ultra-Flat**: 초기 출하 상태의 평면 무결성 |
| **Post-Epitaxial Growth**| Grazing Inc. | $1.50$ | $2.40$ | $45.0$ | 열 공정에 의한 웨이퍼 응력 변형 데이터 |
| **Post-CMP Polishing** | PSI (Phase) | $0.15$ | $0.50$ | $5.2$ | 평탄화 공정을 통한 최적의 노광 가용 평면 |
| **Back-grinded Wafer** | Infrared Int. | $5.50$ | $8.20$ | $120.0$ | 패키징 전 박화 공정에 의한 극한 변형 데이터 |
| **Patterned Wafer** | Grazing Inc. | $2.50$ | $N/A$ | $35.0$ | 회로 패턴의 단차를 포함한 거시적 수평 지표 |

### 2.2 [간섭계 계측 및 분석 파라미터]
- **TIR (Total Indicator Reading)**: 웨이퍼 표면의 최고점과 최저점의 차이 ($0.1 \sim 2.0 \mu\text{m}$).
- **TTV (Total Thickness Variation)**: 웨이퍼 전체의 두께 불균일성 무결성 데이터.
- **Phase Shift Resolution**: $\lambda/1000$. (빛 파장의 수천 분의 일에 달하는 수직 해상도 지표)
- **Wavelength ($\lambda$):** $632.8 \text{ nm}$ (He-Ne Laser). (간섭 무늬 형성을 위한 표준 광원 파장)
- **Spatial Resolution**: $< 50 \mu\text{m}$ (X-Y). (웨이퍼 평면 상의 수평 분해능 데이터)

## 3. [Scientific Rationale: 파동 간섭의 수리적 인과성]

### 3.1 [피조(Fizeau) 간섭계의 위상-높이 산출 모델]
참조면과 측정면 사이의 간섭 무늬 세기($I$)를 통한 높이($h$) 추출 모델입니다.
$$ I = I_1 + I_2 + 2\sqrt{I_1 I_2} \cos \left( \frac{4\pi h}{\lambda} + \phi \right) $$
본 로그는 위상 변조($\phi$ 변화)를 통해 $h$값을 나노미터 단위로 추출하며, $100$만 개 이상의 픽셀에서 평탄도를 동시 계산하는 수리적 근거를 제시합니다.

### 3.2 [그레이징 입사(Grazing Incidence)를 이용한 동적 범위 확장]
빛을 낮은 각도($\theta$)로 입사시켜 유효 파장($\lambda_{eff}$)을 늘리는 모델입니다.
$$ \lambda_{eff} = \frac{\lambda}{\cos \theta} $$
RAG는 "계측 로그를 분석하여, 거친 표면에서도 간섭 무늬를 얻기 위해 $\lambda_{eff}$를 $10\mu\text{m}$ 이상으로 확장하여 측정 범위를 $20$배 늘리는 경로를 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 계측 지능 추론]

### 4.1 [노광 장비 초점 심도(DoF)와 웨이퍼 TIR의 정합성 오딧]
RAG는 "노광 장비의 광학 사양(NA, 파장) 로그와 웨이퍼 TIR 데이터를 대조하여, TIR이 $0.3\mu\text{m}$를 초과할 때 칩 외곽의 임계 선폭(CD) 산포가 $15\%$ 증가함을 식별하고, 해당 웨이퍼의 CMP 재공정 또는 노광 시의 레이아웃 보정을 처방합니다."

### 4.2 [웨이퍼 자중(Self-weight)에 의한 처짐 보정(Gravity Compensation) 오딧]
왜 수평일 때와 수직일 때 데이터가 다른가요? RAG는 "웨이퍼 고정 방식(Chucking) 로그와 탄성 계수 데이터를 참조하여, 측정 시 발생하는 중력 처짐을 유한요소해석(FEA)으로 제거한 '진정한 평탄도'를 산출함으로써 계측 무결성을 입증될 것으로 추론됩니다."

## 5. [Transitional Bridge: 웨이퍼 평탄도 품질 및 노광 가용성 오딧 로직]

측정된 전면 평탄도 데이터를 분석하여 노광 공정의 성공 가능성을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Wafer Flatness Integrity & Lithography Readiness Auditor
def audit_wafer_flatness(height_map, litho_params, chuck_type):
    # 1. 전면 TIR(Total Indicator Reading) 및 TTV 산출
    tir_val = max(height_map) - min(height_map)
    ttv_val = calculate_thickness_variation(height_map)
    
    # 2. 노광 샷(Shot) 단위의 국부적 평탄도(SFQR) 분석
    # Success depends on whether local flatness fits within DoF
    local_flatness_ok = analyze_shot_level_flatness(height_map, litho_params.shot_size)
    
    # 3. 중력 처짐 및 척(Chuck) 정착 무결성 체크
    gravity_error = estimate_gravity_sag(height_map, chuck_type)
    
    # 4. 종합 평탄도 등급 및 노광 승인 트리거
    if tir_val > litho_params.dof_limit:
        status = "GLOBAL_FLATNESS_FAILED_OUT_OF_FOCUS"
        action = "Retool_CMP_Process_or_Use_Dynamic_Focus_Compensation"
    elif not local_flatness_ok:
        status = "LOCAL_SHOT_FLATNESS_ERROR"
        action = "Identify_Hotspots_and_Perform_Local_Polishing"
    elif tir_val < PRIME_SPEC:
        status = "WAFER_FLATNESS_OPTIMAL"
        action = "Authorize_Critical_Layer_Lithography"
    else:
        status = "FLATNESS_MARGINAL_READY"
        action = "Proceed_with_Loose_Tolerance_Layers_Only"
        
    return {"status": status, "tir_um": tir_val, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 웨이퍼 평탄도 계측에서 '피조 간섭계(Fizeau)'가 사용하는 '위상 변조(Phase Shifting)' 기술이 정지된 간섭 무늬를 보는 것보다 수직 해상도를 획기적으로 높일 수 있는 수리적 이유는?
2. **(수리)** 파장 $\lambda = 632.8 \text{ nm}$인 레이저를 사용할 때, 간섭 무늬가 한 주기(밝음-어두움-밝음) 변했다면 이는 웨이퍼의 높이가 몇 $nm$ 변화했음을 의미하는가? (수직 입사 가정)
3. **(응용)** 웨이퍼의 'Warp' 수치가 큰 경우, 노광 장비의 '진공 척(Vacuum Chuck)'이 웨이퍼를 강제로 평평하게 펴서 고정하는 과정에서 발생하는 '잔류 응력(Residual Stress)'이 회로 패턴의 왜곡에 미치는 인과 관계는?


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Entity] semiconductor-wafer-flatness-and-surface-metrology : 웨이퍼 평탄도 계측의 이론적 토대 엔티티
- [[[MOC]] 14_precision-hardware-and-metrology-intelligence-hub]] : 정밀 하드웨어 및 계측 지능 통합 관리 상위 지능 허브
- Data atomic-force-microscopy-surface-roughness-log-v2026 : 미시적 거칠기 계측 데이터 로그 연계
- [SOP] wafer-interferometer-operation-and-flatness-audit : 웨이퍼 간섭계 가동 및 평탄도 감사 표준 절차

*Created by Flash (The Architect of Precision Hardware & HDS Gold V6.3.7)*
