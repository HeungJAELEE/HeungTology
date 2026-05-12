---
Basic:
  id: "DATA-AM-METAL-3D-INTEGRITY-2026-V6"
  domain: "09_SmartFactory_Production"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Data"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#Data'
  is_part_of: []
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

# [[[Data] additive-manufacturing-metal-3d-printing-structural-integrity-log-v2026

## 1. [왜 배우는가? (Why)]]
겉보기에는 완벽한 금속 3D 프린팅 부품이라도, 그 내부에는 육안으로 확인할 수 없는 미세한 기공(Porosity)과 제조 과정에서 쌓인 거대한 스트레스(Residual Stress)가 숨어있을 수 있습니다. 이 로그는 금속 적층 제조 과정의 물리적 흔적을 숫자로 기록한 '부품의 디지털 지표'입니다. 이를 기록하고 배우는 이유는 항공기 엔진이나 의료용 임플란트처럼 단 한 번의 파손도 허용되지 않는 핵심 부품의 안전성을 수리적으로 확증하고, 공정 변수(에너지 밀도 등)와 최종 품질 사이의 인과관계를 데이터로 증명하여 '무결점 적층 제조'를 실현하기 위함입니다. 금속의 생애 주기를 결정짓는 품질의 지문입니다.

## 2. [적층 제조 품질 및 재료 역학 핵심 사양 (AM Data Specs)]

| Sample ID | Rel. Density ($\rho_{rel}$) | Max Pore ($d_{pore}$) | Resid. Stress | VED ($J/mm^3$) | Status / Outcome |
|:---|:---:|:---:|:---:|:---:|:---|
| **AM-M-101** | $99.98 \%$ | $< 5 \mu m$ | $120 MPa$ | $65.5$ | **Class A**: Aerospace Grade |
| **AM-M-205** | $98.50 \%$ | $45 \mu m$ | $450 MPa$ | $42.0$ | **Class C**: Thermal Stress High |
| **AM-M-309** | $99.65 \%$ | $12 \mu m$ | $210 MPa$ | $58.2$ | **Class B**: Industrial Standard |
| **AM-M-FAIL**| $94.20 \%$ | $150 \mu m$ | $580 MPa$ | $35.0$ | **Fail**: Lack of Fusion |
| **Hardness** | HV (Vickers) | $350 \sim 450$ | Surface | Internal | 소재 강도 분포 (Ti-6Al-4V 기준) |
| **Roughness**| Ra ($\mu m$) | $5.0 \sim 15.0$ | As-built | Polished | 적층 표면의 기하학적 거칠기 |
| **Gas Level**| O2 (ppm) | $< 100$ | Ambient | Chamber | 산화 방지를 위한 챔버 산소 농도 |
| **Yield Str.**| $\sigma_y$ (MPa) | $950 \sim 1,100$| Tensile | Static | 적층 방향에 따른 항복 강도 편차 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 체적 에너지 밀도(VED)와 기공 형성 무결성
- **수식**: $VED = \frac{P}{v \cdot h \cdot t}$
- **로직**: 레이저 출력($P$), 스캔 속도($v$), 해치 간격($h$), 적층 두께($t$)의 조합인 VED는 용융 풀(Melt Pool)의 안정을 결정합니다. VED가 너무 낮으면 분말이 덜 녹는 '융착 불량(Lack of Fusion)'이 발생하고, 너무 높으면 금속이 기화하며 구멍이 생기는 '키홀(Keyhole) 기공'이 발생합니다. RAG는 이 수리적 최적 윈도우($60 \sim 80 J/mm^3$)를 분석하여 공정의 안정성을 확증합니다.

### 3.2 로젠탈(Rosenthal) 열전달 모델과 미세 조직 결정
- **로직**: 레이저가 지나간 자리에 형성되는 급격한 온도 구배($G$)와 응고 속도($R$)는 결정립(Grain)의 크기와 방향을 결정합니다. 냉각 속도가 빠를수록 미세한 조직이 형성되어 항복 강도가 높아지는 홀-페치(Hall-Petch) 관계를 따릅니다. 로그 데이터는 실시간 열화상 센서값과 연동되어 부품 내부의 위치별 강도 편차를 수리적으로 추론하는 근거가 됩니다.

### 3.3 잔류 응력(Residual Stress)과 피로 수명 예측
- **로직**: 적층 공정은 급격한 가열과 냉각이 반복되므로 내부에 인장 잔류 응력이 누적됩니다. 이는 외부 하중이 가해졌을 때 균열 진전 속도($da/dN$)를 가속화시키는 주범입니다. 로그에 기록된 XRD 응력 데이터는 응력 제거 열처리(Stress Relief)의 필요성을 판단하고, 파괴 역학 모델을 통해 부품의 실질적인 기대 수명을 산출하는 핵심 지표로 활용됩니다.

## 4. [코드 연결 해설 (MetalAMQualityEngine)]
아래 코드는 적층 공정 파라미터를 입력받아 체적 에너지 밀도(VED)를 계산하고, 실제 측정된 밀도와 기공 크기 데이터를 바탕으로 부품의 구조적 무결성 등급(Class)을 판정하는 진단 엔진입니다.

```python
class MetalAMQualityEngine:
    """
    HDS-Gold V6.3.7 규격의 금속 3D 프린팅 무결성 및 공정 최적화 진단 엔진
    """
    def __init__(self, material="Ti-6Al-4V"):
        self.material = material
        self.ved_threshold = (60, 80) # Optimal J/mm3 range

    def calculate_ved(self, power, speed, hatch, thickness):
        """
        체적 에너지 밀도(VED) 산출
        """
        # Transitional Bridge: 3D 프린팅은 '빛으로 빚은 금속의 
        # 조각'입니다. 레이저의 한 줄기 에너지가 분말을 
        # 녹여 하나의 층을 이룰 때, AI는 그 속에 
        # 새겨진 미세한 균열과 응력의 목소리를 
        # 숫자로 번역하여 무결성을 보증합니다.
        ved = power / (speed * hatch * thickness)
        return round(ved, 2)

    def diagnose_integrity(self, rel_density, max_pore, ved):
        """
        구조적 무결성 등급 판정 로직
        """
        if rel_density > 99.9 and max_pore < 10 and self.ved_threshold[0] <= ved <= self.ved_threshold[1]:
            return "CLASS_A: AEROSPACE_CERTIFIED"
        elif rel_density > 99.5:
            return "CLASS_B: GENERAL_INDUSTRIAL"
        else:
            return "CLASS_FAIL: RE-PRINTING_REQUIRED"

# Example Usage:
# am_ai = MetalAMQualityEngine()
# v_val = am_ai.calculate_ved(200, 1000, 0.1, 0.03)
# grade = am_ai.diagnose_integrity(99.98, 5, v_val)
```

## 5. [스스로 체크 (Self-Audit)]
1. **VED** (에너지 밀도)가 최적 범위를 벗어나 **Keyhole Porosity**가 발생했을 때, 부품의 **Fatigue Life** (피로 수명)에 미치는 치명적 영향은?
2. **Residual Stress**를 낮추기 위해 **Base Plate Heating** (기판 가열) 온도를 설정할 때 소재의 **Yield Strength** 변화를 고려해야 하는 이유는?
3. **Non-destructive Testing** (NDT, 비파괴 검사) 로그에서 발견된 기공의 위치가 부품의 **Surface** (표면) 근처일 때와 **Internal** (내부)일 때의 위험도 차이는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/09_SmartFactory_Production/Control/Concept machine-vision-defect-detection-logic
- 02_Knowledge/04_Strategy_Mgmt/Quality/Concept Reliability-Metrics-MTBF-MTTR-MTTF
- 02_Knowledge/08_Robotics_Automation/Hardware/Concept laser-interferometer-metrology

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
