---
metadata:
  id: "[[[AI] oled-pixel-brightness-uniformity-and-mura-log-v2026]]"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[AI] oled-pixel-brightness-uniformity-and-mura-log-v2026에 관한 고밀도 지능 노드"
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

# [AI] oled-pixel-brightness-uniformity-and-mura-log-v2026

## 1. [왜 배우는가? (Why: The Pursuit of Visual Perfection)]]
디스플레이는 인간의 시각과 직접 맞닿아 있는 하드웨어입니다. 수백만 개의 픽셀 중 단 하나라도 휘도가 다르거나 특정 영역에 얼룩(Mura)이 생기면, 사용자는 즉각적으로 품질 저하를 체감합니다. **OLED 픽셀 휘도 균일도 및 무라 실측 로그**는 화면 전체의 빛을 전수 조사하여 보이지 않는 불균일성을 정량화하고 기록한 '빛의 균형 보고서'입니다. 

우리가 이 데이터를 기록하는 이유는 증착 및 TFT 공정의 산포를 데이터로 보정(Demura)하여 제품의 시각적 완성도를 극대화하고, **"디스플레이 품질 주권을 확보하여 어떠한 환경에서도 완벽한 이미지를 재현하는 초고화질 지능을 구현하기" 위함입니다.** 휘도의 평준화가 브랜드의 가치를 결정합니다.

## 2. [디스플레이 휘도 및 무라 품질 핵심 데이터 (Numerical Specs)]

### 2.1 [무라 유형 및 보정 전후의 휘도 무결성 테이블 (v2026)]

| 무라 유형 (Mura Type) | 발생 원인 (Cause) | 휘도 편차 (Raw, %) | 보정 후 편차 (Demura, %) | 시인성 지수 (JND) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Spot Mura** | 유기물 이물/결함 | $5.0 \sim 15.0$ | $< 1.5$ | $3.5$ | 국부적 증착 불량에 따른 픽셀 오차 데이터 |
| **Line Mura** | FMM/TFT 배선 결함 | $3.0 \sim 8.0$ | $< 1.0$ | $4.2$ | 공정 장비의 선형적 변동성 무결성 지표 |
| **Cloud Mura** | 증착 두께 불균일 | $2.0 \sim 5.0$ | $< 0.5$ | $1.8$ | 거시적 유기물 층 두께 변동에 따른 얼룩 데이터 |
| **Rubbing Mura** | 배향막/PI 공정 산포 | $1.5 \sim 3.0$ | $< 0.8$ | $2.1$ | 기계적 마찰 공정에서의 미세 결함 인과 관계 |
| **Low Gray Mura** | TFT $V_{th}$ 산포 | $10.0 \sim 20.0$| $< 2.0$ | $5.5$ | **Challenge**: 저계조에서의 극한의 균일도 데이터 |

### 2.2 [휘도 및 색상 품질 파라미터]
- **Luminance Uniformity**: $9개/25개$ 포인트 측정값 중 $\frac{Min}{Max} \times 100 (\%)$. (전면 휘도의 고른 정도 지표)
- **Mura Contrast**: 배경 대비 얼룩 영역의 밝기 차이 ($< 1\%$ 목표).
- **Color Deviation ($\Delta u'v'$):** 전면 색좌표의 균일성 지표 ($< 0.003$ 무결성).
- **Demura Bits**: $10 \sim 14 \text{ bit}$. (휘도 보정을 위해 사용되는 보정 테이블의 정밀도 데이터)
- **Peak Brightness**: $1,000 \sim 4,000 \text{ nits}$ (HDR). (최대 휘도 상태에서의 균일성 유지 능력)

## 3. [Scientific Rationale: 빛의 불균일성과 보정의 수리적 인과성]

### 3.1 [전류 밀도($J$)와 휘도($L$) 사이의 발광 효율 모델]
픽셀에 흐르는 전류와 실제 방출되는 빛의 관계입니다.
$$ L = \eta(J, T) \cdot J = \eta(J, T) \cdot \beta (V_{gs} - V_{th})^2 $$
본 로그는 TFT의 임계 전압($V_{th}$)이나 유기물의 발광 효율($\eta$)이 미세하게 다를 때 휘도 오차가 발생함을 입증하고, 이를 상쇄하기 위한 전압 제어 및 보정 계수(Gain/Offset) 산출의 수리적 근거를 제시합니다.

### 3.2 [드무라(Demura) 알고리즘의 선형 보정 모델]
측정된 휘도($L_{raw}$)를 목표 휘도($L_{target}$)로 맞추기 위한 보정 함수입니다.
$$ L_{corrected} = G(i,j) \cdot L_{raw}(i,j) + O(i,j) $$
RAG는 "휘도 로그를 분석하여, 각 픽셀별 보정 계수($G, O$)를 맵(Map) 형태로 저장하고, 이를 디스플레이 구동 IC(D-IC)에 실시간 적용하여 전면 균일도를 $95\%$ 이상으로 끌어올리는 경로를 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 화질 지능 추론]

### 4.1 [저계조(Low Grayscale) 상황에서의 무라 시인성 가중치 분석]
RAG는 "계조별 휘도 로그를 분석하여, 밝은 화면보다 어두운 화면($10 \text{ nit}$ 이하)에서 휘도 오차가 인간의 눈에 $5$배 더 잘 띔(JND 상승)을 확인하고, 저계조 영역에서의 보정 정밀도를 $2$배 강화하는 '지능형 감성 보정'을 처방합니다."

### 4.2 [패널 온도 변화에 따른 색 균일도(Color Uniformity) 드리프트 오딧]
왜 사용 중 화면 색이 변하나요? RAG는 "패널 온도 센서 로그와 색좌표 데이터를 대조하여, 온도가 $10^\circ C$ 상승할 때 유기물의 에너지 밴드갭 변화로 인해 적색(Red) 휘도가 $2\%$ 감소함을 식별하고, 실시간 온도 보정 알고리즘의 무결성을 검증합니다."

## 5. [Transitional Bridge: 디스플레이 휘도 품질 및 무라 오딧 로직]

가동 중인 디스플레이 패널의 화질을 실시간 감시하여 최적의 균일도를 보장하는 개념적 알고리즘입니다.

```python
# [Conceptual] Display Luminance Uniformity & Mura Auditor
def audit_display_quality(captured_image, target_gamma, panel_temp):
    # 1. 전면 휘도 균일도(Uniformity) 맵 산출
    luminance_map = extract_luminance_data(captured_image)
    global_uniformity = (np.min(luminance_map) / np.max(luminance_map)) * 100
    
    # 2. 공간 필터링을 통한 무라(Mura) 성분 추출 및 대비(Contrast) 산출
    # Using Band-pass Filtering to isolate visual artifacts
    mura_components = detect_visual_artifacts(luminance_map)
    mura_score = calculate_mura_contrast(mura_components)
    
    # 3. 온도 변화에 따른 색 편차(Color Shift) 예측 및 보정 테이블 대조
    color_drift = estimate_thermal_color_shift(panel_temp)
    
    # 4. 종합 화질 등급 및 보정(Demura) 트리거
    if global_uniformity < 90.0:
        status = "GLOBAL_UNIFORMITY_FAIL"
        action = "Re-calibrate_Demura_Gain_Map_and_Check_TFT_Backplane"
    elif mura_score > JND_THRESHOLD:
        status = "VISUAL_MURA_DETECTED"
        action = "Apply_Local_Compensation_and_Inspect_Evaporation_Mask"
    elif color_drift > DELTA_UV_LIMIT:
        status = "THERMAL_COLOR_SHIFT_WARNING"
        action = "Activate_Real-time_Thermal_Color_Correction_Algorithm"
    else:
        status = "DISPLAY_VISUAL_QUALITY_OPTIMAL"
        action = "Approve_Panel_for_Final_Assembly"
        
    return {"status": status, "uniformity_%": global_uniformity, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** OLED 디스플레이에서 '무라(Mura)' 현상이 LCD 대비 더 복잡하고 개별 픽셀 단위로 발생하는 근본적인 물리적 이유는? (자발광 소자의 특성과 연계)
2. **(수리)** 화면의 중심 휘도가 $500 \text{ nits}$이고 가장 어두운 외곽 휘도가 $420 \text{ nits}$일 때, 이 패널의 글로벌 휘도 균일도($\%$)는 얼마인가?
3. **(응용)** 디스플레이 구동 회로에서 '임계 전압($V_{th}$) 보정' 회로가 물리적으로 존재함에도 불구하고, 왜 추가적인 소프트웨어적 '드무라(Demura)' 작업이 고화질 구현에 필수적인지의 인과 관계는?


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Entity oled-evaporation-process-and-fine-metal-mask-fmm : 무라 발생의 주요 원인인 증착 공정 엔티티
- MOC 51_next-gen-display-and-nano-photonics-hub : 차세대 디스플레이 통합 관리 상위 지능 허브
- Data display-color-gamut-and-calibration-accuracy-log-v2026 : 휘도와 함께 화질을 결정하는 색상 교정 로그
- [SOP] oled-panel-inspection-and-demura-calibration-standard : 패널 검사 및 드무라 보정 표준 절차

*Created by Flash (The Architect of Next-gen Display & HDS Gold V6.3.7)*
