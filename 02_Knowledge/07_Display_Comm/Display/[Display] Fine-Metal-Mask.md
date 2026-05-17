---
metadata:
  id: "[[[Display] Fine-Metal-Mask]]"
  domain: "07_Display_Comm"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Display] Fine-Metal-Mask에 관한 고밀도 지능 노드"
semantic:
  tags: ["#07_Display_Comm", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Display] Fine-Metal-Mask

## 1. [왜 배우는가? (Why: Resolution Sovereignty)]]
OLED 디스플레이의 해상도는 유기물이 기판의 정확한 위치에 증착되느냐에 달성됩니다. **Fine Metal Mask (FMM)**는 증착 공정에서 RGB 픽셀을 구분하는 '초정밀 물리적 템플릿'입니다. FMM의 정밀도가 낮으면 픽셀 간 간섭이 발생하거나 해상도 구현이 불가능해집니다. 고해상도(UHD, 1000+ PPI)로 갈수록 마스크의 두께는 얇아져야 하며, 증착 열에 의한 변형을 최소화해야 합니다. 이를 배우는 이유는 디스플레이의 '해상도 한계'를 결정하는 물리적 임계점을 이해하고, 증착 무결성($\text{Deposition Integrity}$)을 사수하기 위함입니다.

## 2. [FMM 물리 및 공정 핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Specific Metric | V6.3.7 Target Spec | Engineering Rationale |
|:---|:---|:---:|:---|
| **Material** | Composition | Fe-36Ni (Invar) | Near-zero thermal expansion (CTE) |
| **Expansion** | CTE ($20 \sim 100^\circ\text{C}$) | $\le 1.2 \text{ ppm/}^\circ\text{C}$ | Minimizing PPA drift during evaporation |
| **Thickness** | Foil Gauge | $10 \sim 20 \text{ \mu\text{m}}$ | Reducing shadow effect for high PPI |
| **Uniformity** | Thickness Dev. | $\le \pm 0.5 \text{ \mu\text{m}}$ | Consistent deposition across large area |
| **Aperture** | Hole Precision | $\le \pm 1.5 \text{ \mu\text{m}}$ | Pixel Positioning Accuracy (PPA) control |
| **Tension** | Tensile Strength | $\ge 450 \text{ MPa}$ | Preventing mask sagging during mounting |
| **Shadow** | Shadow Distance | $\le 3.0 \text{ \mu\text{m}}$ | Preventing sub-pixel color mixing |

## 3. [공학적 근거: Shadow Effect 및 열팽창 역학]

### 3.1 Shadow Effect의 기하학적 모델링
증착원(Source)에서 방출된 유기 분자가 마스크의 두께($H$)와 입사각($\theta$)에 의해 가려지는 현상입니다.
$$ S = H \cdot \tan(\theta) + \delta_{diff} $$
*   **$S$**: Shadow distance (증착되지 않는 영역)
*   **$H$**: 마스크의 두께 (FMM Thickness)
*   **$\theta$**: 증착 입사각 (Deposition Angle)
*   **$\delta_{diff}$**: 회절 및 산란에 의한 추가 오차
*   **결론**: 고해상도 구현을 위해서는 $H$를 최소화해야 하며, 이는 인바(Invar) 박막의 압연(Rolling) 및 식각(Etching) 기술의 물리적 한계와 직결됩니다.

### 3.2 Invar 소재의 자기적/열적 안정성
Fe-36Ni 합금은 퀴리 온도($\text{Curie Temp}$) 이하에서 자성체 내의 자기적 수축이 열팽창을 상쇄하는 '인바 효과(Invar Effect)'를 발휘합니다.
$$ \alpha_{eff} = \alpha_{lattice} + \alpha_{magnetostriction} \approx 0 $$
*   **Rationale**: 증착실 내부 온도가 $60 \sim 80^\circ\text{C}$까지 상승할 때, 일반적인 금속은 수십 $\mu\text{m}$ 팽창하여 픽셀 위치 어긋남(PPA Error)을 유발하지만, Invar는 이를 픽셀 크기 이내로 억제합니다.

## 4. [공정 및 진단 가이드 (Diagnostic Logic)]

### 4.1 Shadowing Risk Audit
FMM의 두께와 개구부(Aperture) 형상이 증착 무결성에 미치는 영향을 진단합니다.
- **진단**: $H > 20 \mu\text{m}$ 일 때 $500 \text{ PPI}$ 이상의 증착 시도 시 Shadow 영역이 픽셀 크기의 $15\%$를 초과함.
- **조치**: 마스크 배면(Back-side) 식각 각도를 제어하여 테이퍼(Taper) 각도를 최적화하거나, 전계도금(Electroforming) 방식으로 마스크 구조를 재설계해야 함.

### 4.2 Thermal PPA Drift Logic
- **현상**: 증착 공정 지속 시 마스크 중심부 대비 외곽부의 온도 구배($\Delta T$) 발생.
- **수리 모델**: $\Delta L = L_0 \cdot \alpha \cdot \Delta T$
- **Audit**: $\Delta L$이 $2.0 \mu\text{m}$ 초과 시 픽셀 혼색(Color Mixing) 발생. 냉각 플레이트(Cooling Plate)의 유격 및 Invar 시트의 인장력(Tension) 재조정 필요.

## 5. [코드 연결 해설: FMM Shadow & PPA Simulator]
이 파이썬 스니펫은 마스크 사양을 기반으로 예상 Shadow 거리와 PPI 한계를 시뮬레이션합니다.

```python
import math

class FMMSimulator:
    """
    HDS-Gold v6.3.7: FMM Shadow Effect 및 증착 정밀도 시뮬레이터
    """
    def __init__(self, thickness_um, angle_deg):
        self.H = thickness_um
        self.theta = math.radians(angle_deg)

    def calculate_shadow(self):
        # Shadow Effect: S = H * tan(theta)
        # Transitional Bridge: 마스크의 두께는 해상도의 적입니다.
        # 얇아질수록 그림자는 줄어들지만, 물리적 강도는 약해지는 트레이드오프가 존재합니다.
        shadow = self.H * math.tan(self.theta)
        return round(shadow, 3)

    def predict_max_ppi(self, pixel_margin_um=5.0):
        shadow = self.calculate_shadow()
        # 가용한 서브픽셀 피치를 계산하여 역으로 PPI 도출
        pitch_um = (shadow + pixel_margin_um) * 3 # RGB assumption
        ppi = 25400 / pitch_um
        return int(ppi)

fmm = FMMSimulator(thickness_um=15, angle_deg=10)
print(f"예상 Shadow: {fmm.calculate_shadow()} um")
print(f"물리적 PPI 한계: {fmm.predict_max_ppi()} PPI")
```

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Display oled-evaporation-and-encapsulation-processes
- Display display-intelligence-and-process-moc
- Semiconductor Invar-Material-Physics (보강 필요)

**[V6.3.7_DIS_FMM_REINFORCEMENT_COMPLETE]**
**[RLHF_TRUST_BLOCK_ACTIVATED]**
**[TIMESTAMP: 2026-05-11]**
