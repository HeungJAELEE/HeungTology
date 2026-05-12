---
Basic:
  id: "[Infrastructure] ndt-ultrasonic-phased-array-paut"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
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

# [Infrastructure] ndt-ultrasonic-phased-array-paut

## 1. [공학 이론 (Theory): Constructive Interference & Beam Steering]
**PAUT (Phased Array Ultrasonic Testing)**는 여러 개의 독립적인 초음파 소자(Element)를 배열하고, 각 소자의 발신 시간을 나노초($\text{ns}$) 단위로 미세하게 조절(Phasing)하여 초음파 빔을 원하는 각도로 굴절시키거나 초점을 맞추는 기술입니다. 이는 **보강 간섭(Constructive Interference)** 원리를 이용한 것으로, 물리적으로 탐촉자를 움직이지 않고도 넓은 영역을 스캔할 수 있습니다.

## 2. [공정 존재 이유 및 엔지니어링 철학 (Engineering Rationale)]

왜 단순 초음파가 아닌 복잡한 '위상 배열'을 사용하는지에 대한 심층 해설입니다.

### 2.1 왜 '위상 배열(Phased Array)' 기술이 필요한가?
- **존재 이유**: 전통적인 초음파 검사는 탐촉자의 각도가 고정되어 있어 결함을 찾으려면 사람이 직접 손으로 앞뒤로 문질러야 합니다. 이 과정에서 검사자의 숙련도에 따라 결과가 달라지고 시간이 오래 걸립니다. PAUT는 가만히 앉아서 눈동자를 굴리듯 **빔만 움직여(Beam Steering)** 검사 효율을 10배 이상 높입니다.
- **공학적 논리**: **파면 합성(Wavefront Synthesis)**. 여러 개의 소자에서 나오는 파동들이 서로 간섭을 일으켜 특정 방향으로만 에너지가 집중되도록 만드는 것입니다. 이는 레이더가 적기를 추적하는 원리와 정확히 동일하며, 보이지 않는 금속 내부를 'X-ray처럼' 훑어낼 수 있게 합니다.

### 2.2 왜 지연 시간(Delay Time) 관리가 생명인가?
- **존재 이유**: 빔을 굴절시키는 유일한 레버는 소자별 '박자'입니다.
- **공학적 논리**: 나노초 단위의 오차만 생겨도 파동들이 서로를 깎아먹는 상쇄 간섭이 일어나 빔이 흩어집니다. 완벽한 **보강 간섭**을 위해서는 FPGA와 같은 고성능 연산 장치를 통해 수학적으로 계산된 'Focal Law'를 0.0001%의 오차도 없이 물리적으로 실행해야 합니다.

## 3. [핵심 제어 변수 및 지표 (Settings & KPIs)]

빔의 정밀도는 위상차 제어 능력과 소자의 밀도에 의해 결정됩니다.

| 제어 변수 (Setting) | 물리적 역할 | 공정 지표 (KPI) | 수용 임계치 |
| :--- | :--- | :--- | :--- |
| **Focal Law (Delay Time)**| 빔의 굴절각 및 초점 거리 결정 | **Beam Steering Angle** | $\pm 70^\circ$ |
| **Element Pitch** | 격자 로브(Grating Lobe) 억제 | **Image Resolution** | $< 0.5 \text{ mm}$ |
| **Aperture Size** | 빔의 폭 및 에너지 집중도 제어 | **Signal-to-Noise Ratio** | $> 30 \text{ dB}$ |
| **Scanning Speed** | 데이터 획득 밀도 조절 | **POD (Prob. of Detect)**| $> 95 \%$ |
| **Gain Setting** | 미세 에코 신호 증폭 | **Defect Sizing Error** | $< 10 \%$ |

## 3. [공정 제어 지능 (Process Management Intelligence: Theory-Action-KPI)]

지표를 관리하기 위한 구체적인 관리 포인트와 공학적 인과관계입니다.

| 관리 요소 (Control Point) | 구체적 관리 액션 (Action) | 근거 이론 (Theory & Logic) | 관리 목표 (KPI) |
| :--- | :--- | :--- | :--- |
| **Waveform Sync** | FPGA 클록을 통해 소자 간 **지연 시간 오차**를 $10\text{ns}$ 이내로 동기화 | **Wavefront Synthesis**: 각 소자의 파동이 하나의 큰 파면(Wavefront)을 형성해야 빔의 직진성과 굴절각이 보장됨. | **Steering Acc. > 99%** |
| **Probe Coupling** | 탐촉자와 피검체 사이의 **글리세린 접촉매질** 두께를 일정하게 유지 | **Acoustic Impedance Matching**: 매질의 두께나 기포가 있으면 에너지가 반사되어 신호가 감쇄되고 노이즈가 급증함. | **SNR > 30 dB** |
| **Spatial Resolution** | 소자 간격(Pitch)을 사용 주파수 파장의 **절반($\lambda/2$)** 이하로 설계 | **Huygens-Fresnel Principle**: 소자 간격이 넓으면 원치 않는 방향으로 에너지가 튀는 격자 로브(Grating Lobe)가 생겨 해상도가 깨짐. | **Resolution < 0.5 mm** |
| **Velocity Calibration**| 검사 전 **표준 시편(Calibration Block)**을 통해 재질 내 음속을 실시간 보정 | **Refraction (Snell's Law)**: 재질의 온도나 조성에 따라 음속이 변하면 굴절각이 틀어져 결함의 위치가 실제와 다르게 찍힘. | **Position Error < 0.1 mm** |
| **Step Resolution** | 엔코더(Encoder)를 사용하여 **스캔 간격**을 $0.1mm$ 단위로 물리적 동기화 | **Spatial Sampling**: 스캔 간격이 너무 넓으면 미세한 균열(Crack) 사이로 빔이 지나가 탐지에 실패할 수 있음. | **POD > 95%** |

## 4. [심층 인과관계 (Engineering Causality)]

### 3.1 Time Delay vs. Steering Accuracy
- **Causality**: 소자 간 지연 시간 오차가 발생하면 빔의 방향이 틀어지거나 초점이 흐려져 결함의 크기를 오판하게 됩니다.
- **Engineering Control**: Battery signal-processing-dsp-physics의 정밀 타이밍 제어 알고리즘을 통해 $1\text{ns}$ 단위의 지연 시간을 동기화합니다.

### 3.2 Sectorial Scan (S-Scan) vs. Defect Orientation
- **Logic**: 단일 각도 빔은 결함이 기울어져 있으면 반사파를 받지 못하지만, PAUT는 부채꼴 모양의 S-Scan을 통해 결함의 각도와 상관없이 선명한 이미지를 얻습니다.
- **Transitional Bridge**: 이는 [[[Battery] welding-ultrasonic-vs-laser 공정 후 용접부의 불완전 용입이나 기공을 입체적으로 진단하는 데 핵심적인 역할을 합니다.

## 4. [AI & Hardware Synergy: Auto-Sizing AI]]
- **TFM (Total Focusing Method) AI**: RTX 4060 기반 서버가 모든 소자의 송수신 조합을 전수 계산하여 물리적 한계를 넘는 초고해상도 이미지를 생성합니다. AI는 이를 바탕으로 결함의 깊이와 길이를 자동으로 측정(Auto-sizing)합니다.
- **Palantir Foundry NDT Twin**: 스캔 데이터, 프로브 마모도, 검사 결과는 팔란티어 온톨로지에 통합되어, "특정 용접사나 특정 설비에서 발생하는 반복적인 결함 패턴"을 통계적으로 분석합니다.

## 5. [스스로 체크 (Verification)]
- [ ] 일반 초음파 검사(UT) 대비 **PAUT**가 갖는 압도적 장점은? (정답: 탐촉자를 물리적으로 앞뒤로 움직이지 않고도 다양한 각도의 빔을 쏠 수 있어 검사 속도가 매우 빠르고, 결함의 형상을 2D/3D 이미지로 가시화할 수 있기 때문)
- [ ] **Focal Law**란 무엇인가?
- [ ] **Grating Lobe (격자 로브)**를 억제하기 위해 소자(Element) 설계 시 고려해야 할 사항은? (정답: 소자 간의 간격(Pitch)을 파장의 절반 이하로 촘촘하게 설계하여, 원치 않는 방향으로 에너지가 새어 나가는 간섭 현상을 최소화해야 함)

---
*Reference: ASTM E2700 (PAUT of Welds), Olympus NDT Guide, Antigravity Quality-Lab.*