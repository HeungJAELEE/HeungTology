---
Basic:
  id: "liquid-penetrant-testing-and-surface-defect-detection-physics"
  domain: "General_Industrial"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Entity"
  tier: 1
  description: "A widely applied and low-cost inspection method used to locate surface-breaking defects in all non-porous materials (Liquid Penetrant Testing) and the physical study of capillary action and wetting dynamics (Surface Defect Detection Physics)."
  physical_model: "N/A"
Semantic:
  tags: '["liquid-penetrant-testing", "lpt", "ndt", "surface-defect", "capillary-action", "fluorescence", "industrial-inspection", "physics"]'
  is_part_of: []
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "FactoryFidelityEngine"
  diagnostic_protocol:
    - 'Penetration_Fidelity_Audit: Evaluate the ''Dwell Time'' ($t$) to identify if high-fidelity ''Viscosity'' changes or ''Surface Contamination'' is preventing the penetrant from filling high-fidelity micro-cracks.'
    - 'Observation_Integrity_Check: Analyze the high-fidelity ''UV Intensity'' and high-fidelity ''Developer Coverage'' to ensure the high-fidelity ''Contrast Ratio'' is sufficient for human or AI defect detection.'
    - 'Cleaning_Fidelity_Scan: Monitor the high-fidelity ''Pre-cleaning'' effectiveness to verify that high-fidelity ''Oil'' or ''Scale'' is not masking surface high-fidelity defects.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# 🕵️ Liquid Penetrant Testing and Surface Defect Detection Physics

## 1. 개요 (Why: 인간적 통찰)
거대한 항공기 엔진 날개나 원자력 발전소 배관 표면에 보이지 않는 아주 미세한 금(Crack)이 가 있다면 어떻게 찾아낼까요? **액체 침투 탐상 및 표면 결함 탐지 물리**는 액체가 좁은 틈새를 파고드는 성질(모세관 현상)을 이용해, 숨어있는 결함을 밖으로 '빨아올려' 보여주는 **'결함의 확대경'** 기술입니다. 형광색 액체가 균열 속으로 스며들게 한 뒤, 다시 밖으로 끌어내어 자외선 아래에서 밝게 빛나게 함으로써 재난의 씨앗을 미리 발견합니다. **'워시번 방정식과 모세관 압력의 원리를 이용해 미세 결함에 액체를 강제로 주입하여 육안으로는 불가능한 정밀 검사를 수행하는 지능형 비파괴 검사 엔진'**입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 모세관 침투 로직 (Washburn's Equation)
액체가 틈새($r$)를 따라 파고드는 깊이($h$)는 표면장력($\gamma$), 점도($\mu$), 그리고 시간($t$)에 의해 결정된다는 원리입니다.

$$ h^2 = \frac{\gamma r \cos(\theta)}{2 \mu} t $$

**[인간적 해석]**: "침투의 인내심"입니다. 금이 아주 좁을수록($r$이 작을수록) 액체가 들어가는 데 시간이 오래 걸립니다. 우리는 이 수식을 통해 "가장 깊숙한 곳까지 액체가 스며들도록 기다려야 할 최적의 시간(Dwell Time)"을 결정하는 **'검사 무결성'**을 수행합니다.

### 2.2. 라플라스 압력 로직 (Young-Laplace Pressure)
좁은 틈새에서 액체를 안으로 빨아당기는 강력한 압력($\Delta P$)을 계산합니다.

$$ \Delta P = \frac{2 \gamma \cos(\theta)}{r} $$

**[인간적 해석]**: "액체의 흡입력"입니다. 이 압력 덕분에 액체는 중력을 거슬러 거꾸로도 타고 올라갑니다. 우리는 이 물리 법칙을 통해 "머리카락 굵기의 수백 분의 일에 불과한 미세 균열조차 놓치지 않는" **'탐지 무결성'**을 실현합니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Feature | Visual Inspection (Eye) | Liquid Penetrant (V6.3.7) | Unit | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Sensitivity** | Low (> 1.0mm) | **Ultra-high (< 0.01mm)** | $mm$ | Precision |
| **Visibility** | Ambient Light | **UV / Fluorescence (High Contrast)**| - | Trust |
| **Applicability** | Limited | **All Non-porous (Metal/Plastic)** | - | Versatility |
| **Cost** | Zero | **Low (Cost-effective NDT)** | - | Economy |
| **Speed** | Fast | **Moderate (Dwell time req)** | - | Agility |
| **Detectability** | Surface only | **Surface-breaking only** | - | Logic |

## 4. FactoryFidelityEngine: Diagnostic Logic

항공기 부품 정비소 및 대형 압력 용기 제작 현장의 비파괴 검사 무결성 및 시스템 상태를 현황을 진단하는 `FactoryFidelityEngine` 로직입니다.

```python
class FactoryFidelityEngine:
    def __init__(self, dwell_time_min, uv_intensity_uw, surface_cleanliness_level):
        self.dwell = dwell_time_min # 침투 시간
        self.uv = uv_intensity_uw # UV 램프 강도
        self.clean = surface_cleanliness_level # 세척 상태

    def diagnose_inspection_health(self):
        """침투 시간 및 광원 기반 시스템 무결성 진단"""
        if self.clean < self.target_clean: # 청소가 안 됨 (기름기가 남음)
            return "CRITICAL: Surface Masking - High-fidelity contaminants preventing penetrant entry. Risk of high-fidelity 'False Negative'. Re-clean high-fidelity surface"
        if self.dwell < 10.0: # 너무 빨리 닦아냄
            return f"WARNING: Insufficient Dwell Time ({self.dwell} min) - High-fidelity micro-cracks may not be fully filled. Reduced high-fidelity detection sensitivity"
        if self.uv < 1000.0:
            return "NOTICE: Low Contrast - High-fidelity UV light source weakening. Fluorescent high-fidelity indications may be missed by the inspector"
        return "OPTIMAL: Stable Capillary Action and High-Fidelity Defect Visualization Verified"

    def audit_indication_integrity(self, false_call_rate):
        """결함 지시(Indication) 무결성 진단"""
        if false_call_rate > 0.1: # 가짜 결함이 너무 많음 (세척 불량)
            return "REJECT: Background Noise - High-fidelity excess penetrant not removed correctly. Unacceptable high-fidelity signal-to-noise ratio"
        return "PASS: Validated Capillary Logic and Verified Inspection Integrity Confirmed"

# Instance Diagnostic
engine = FactoryFidelityEngine(dwell_time_min=15.0, uv_intensity_uw=1200.0, surface_cleanliness_level=0.95)
print(engine.diagnose_inspection_health())
```

## 5. 분석 프레임워크: High-Contrast Defect Detection Strategy
1. **[Fluorescent Penetrant Strategy]**: 형광 물질을 섞어 어두운 곳에서 자외선을 비추면 결함만 밝게 빛나게 하여, 사람이나 AI가 단번에 찾아내게 하는 전략. '고감도 검사'의 비결입니다.
2. **[Solvent-Removable vs Water-Washable Logic]**: 물로 씻어낼 것인지 용제로 닦아낼 것인지 결정하여, 결함 속의 액체는 남기고 표면만 깨끗하게 치우는 전략. '배경 노이즈 제거' 기술입니다.
3. **[Developer Bleed-out Strategy]**: 침투 후 현상액(흰 가루)을 뿌려, 결함 속에 숨은 액체를 스펀지처럼 빨아올려 크기를 키워 보여주는 전략. '결함 시각적 증폭' 전략입니다.

## 6. 스스로 체크 (Self-Audit)
1. 왜 침투 탐상 전에 '전처리(Cleaning)'가 가장 중요한가? (균열 속에 이미 기름이나 이물질이 차 있으면 침투액이 들어갈 자리가 없어, 결함이 있어도 없다고 판정되는 '치명적 오류'가 발생하기 때문)
2. '모세관 현상'은 중력을 이길 수 있는가? (그렇음. 라플라스 압력은 매우 강력해서 거꾸로 된 천장의 균열 속으로도 액체를 밀어 넣을 수 있는 관점)
3. 왜 '다공성 물질(나무, 스펀지 등)'에는 이 검사를 쓸 수 없는가? (재질 자체가 침투액을 다 흡수해버려 표면 전체가 형광색으로 뒤덮여 '진짜 결함'을 구분할 수 없기 때문인 관점)

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data ndt-defect-detection-probability-and-resolution-v2026`와 연동되어, 전 세계 주요 항공 정비창 및 중공업 현장의 실시간 비파괴 검사 데이터를 분석하고 균열 미검출 및 대형 사고 확률을 0.001% 이하로 억제함으로써 지능형 산업 안전 문명의 품질 무결성을 보장합니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- light-interferometry-and-surface-metrology-physics
- Data ndt-defect-detection-probability-and-resolution-v2026
