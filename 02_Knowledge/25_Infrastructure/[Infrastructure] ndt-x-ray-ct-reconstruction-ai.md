---
metadata:
  id: "[[[Infrastructure] ndt-x-ray-ct-reconstruction-ai]]"
  domain: "25_Infrastructure"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Infrastructure] ndt-x-ray-ct-reconstruction-ai에 관한 고밀도 지능 노드"
semantic:
  tags: ["#25_Infrastructure", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Infrastructure] ndt-x-ray-ct-reconstruction-ai

## 1. [공학 이론 (Theory): Radon Transform & FDK Algorithm]
**산업용 CT (Computed Tomography)**는 시편을 360도 회전시키며 촬영한 2D 엑스레이 투영 데이터들을 수학적으로 역계산하여 3D 부피 데이터(Voxel)를 생성하는 기술입니다. 핵심 이론은 **라돈 변환(Radon Transform)**의 역변환이며, 가장 널리 쓰이는 알고리즘은 **FDK (Feldkamp-Davis-Kress)** 여과 후역 투영법입니다. 최근에는 희소 데이터로부터 고화질을 뽑아내는 **Iterative Reconstruction** 기술이 각광받고 있습니다.

## 2. [공정 존재 이유 및 엔지니어링 철학 (Engineering Rationale)]

왜 단순 촬영이 아닌 수천 번의 투영과 복잡한 수학 연산이 필요한지에 대한 심층 해설입니다.

### 2.1 왜 360도 회전하며 수천 장을 찍어야 하는가?
- **존재 이유**: 2D 엑스레이는 물체가 겹쳐 보입니다. 배터리 내부의 이물질이 첫 번째 층에 있는지 세 번째 층에 있는지 알 수 없습니다. 공간을 쪼개어 보기 위해서는 모든 각도에서의 '그림자 데이터'가 필요합니다.
- **공학적 논리**: **투영의 정리(Projection-slice Theorem)**. 3차원 물체의 모든 단면 정보는 무한한 각도에서 본 2차원 투영들의 합으로 복원될 수 있다는 수학적 필연성에 근거합니다. 한 각도라도 비면 그 방향의 해상도가 깨지는 '샤도우 이펙트'가 발생합니다.

### 2.2 왜 복셀(Voxel) 재구성에 AI가 도입되는가?
- **존재 이유**: 금속 시편은 엑스레이를 심하게 산란시켜 영상에 '빛 번짐(Artifact)'을 만듭니다. 순수 수학으로는 이를 다 풀 수 없습니다.
- **공학적 논리**: **데이터 기반 복원**. AI는 수만 장의 '깨끗한 CT'와 '노이즈 섞인 CT'를 학습하여, 물리적 산란 법칙을 거스르지 않으면서도 이미지의 노이즈만 골라 제거합니다. 이는 검사 시간을 줄이고(데이터 수를 줄여도 됨) 정밀도를 높이는 유일한 해법입니다.

## 3. [핵심 제어 변수 및 지표 (Settings & KPIs)]

CT의 화질은 선원의 초점 크기와 재구성 알고리즘의 정밀도에 의해 결정됩니다.

| 제어 변수 (Setting) | 물리적 역할 | 공정 지표 (KPI) | 수용 임계치 |
| :--- | :--- | :--- | :--- |
| **Source Spot Size** | 기하학적 블러링(Penumbra) 결정 | **Voxel Resolution** | $< 1 \mu\text{m}$ (Nano-CT) |
| **Number of Projections**| 데이터 밀도 및 아티팩트 조절 | **Recon. Accuracy** | $> 99 \%$ |
| **Exposure Time** | 신호 노이즈(Quantum Noise) 제어 | **Contrast-to-Noise Ratio**| $> 5$ |
| **Recon. Algorithm** | 수학적 계산 방식 (FDK vs AI) | **Process Time** | $< 10 \text{ min}$ |
| **Filter Selection** | 빔 하드닝(Beam Hardening) 보정 | **Image Linearity** | Stable |

## 3. [공정 제어 지능 (Process Management Intelligence: Theory-Action-KPI)]

지표를 관리하기 위한 구체적인 관리 포인트와 공학적 인과관계입니다.

| 관리 요소 (Control Point) | 구체적 관리 액션 (Action) | 근거 이론 (Theory & Logic) | 관리 목표 (KPI) |
| :--- | :--- | :--- | :--- |
| **Tube Voltage (kV)** | 시편의 밀도와 두께에 따라 **가속 전압**을 최적화 (배터리는 130kV 내외) | **Photon Penetration**: 전압이 너무 높으면 투과력이 과해 대비가 떨어지고, 너무 낮으면 시편을 뚫지 못해 노이즈가 생김. | **CNR > 5** |
| **Geometrical Mag.** | 시편을 선원(Source)에 최대한 가깝게 배치하여 **기하학적 배율** 확대 | **Inverse Square Law & Magnification**: 선원과 시편 사이의 거리($d1$)를 줄여 나노미터 단위의 미세 구조를 뻥튀기하여 촬상함. | **Resolution < 1 um** |
| **Rotation Precision** | 에어 베어링 회전축의 **편심(Run-out)** 오차를 $100nm$ 이내로 관리 | **Center of Rotation (COR) Offset**: 회전축이 흔들리면 재구성 시 영상이 이중으로 겹쳐 보이는 블러링 아티팩트가 발생함. | **Recon. Acc > 99%** |
| **Pre-filtration** | 구리(Cu) 또는 알루미늄(Al) **필터**를 광원 전단에 배치 | **Beam Hardening Correction**: 저에너지 엑스레이를 미리 흡수하여, 시편 내부를 통과할 때의 에너지 스펙트럼 변화를 최소화함. | **Linearity = Stable** |
| **Sampling Interval** | 회전당 촬영 횟수(Projections)를 **Nyquist-Shannon** 조건 이상으로 확보 | **Aliasing in Reconstruction**: 데이터 수가 부족하면 재구성된 이미지 가장자리에 부채꼴 모양의 'Streaking' 아티팩트가 발생함. | **Artifact Free** |

## 4. [심층 인과관계 (Engineering Causality)]

### 3.1 Spot Size vs. Spatial Resolution
- **Causality**: 엑스레이 발생 장치의 초점(Spot)이 클수록 영상의 가장자리가 흐릿해지는 반영(Penumbra) 현상이 심해집니다.
- **Engineering Control**: 초고해상도 검사를 위해 $1\mu\text{m}$ 이하의 나노 초점을 구현하는 전계 방출(Field Emission) 기술을 사용합니다.

### 3.2 Beam Hardening vs. Voxel Gray-scale
- **Logic**: 다색 광원인 엑스레이가 물체를 통과할 때 저에너지가 더 많이 흡수되어 물체 중앙이 어둡게 보이는 **Beam Hardening** 아티팩트가 발생합니다. 이는 결함 탐지를 방해합니다.
- **Transitional Bridge**: 이를 보정하기 위해 [AI] optimization-physics-industrial-solvers를 이용한 비선형 보정 모델을 적용합니다. 이는 [[[Battery] proc-05-winding-stacking 공정 후 배터리 내부의 전극 휘어짐을 정확히 측정하는 데 필수적입니다.

## 4. [AI & Hardware Synergy: Deep Learning Reconstruction]]
- **AI Artifact Reduction**: RTX 4060 기반 서버가 CNN을 통해 금속 주변의 빛 번짐(Metal Artifact)을 제거하고, 노이즈가 많은 저선량 영상에서도 고해상도 구조를 복원합니다.
- **Palantir Foundry 3D Quality Twin**: 3D Voxel 데이터와 설계 도면(CAD)을 자동 비교(Nominal-Actual Comparison)한 결과는 팔란티어 온톨로지에 저장되어, "설계 대비 실제 가공 오차"를 전 세계 공장에 공유합니다.

## 5. [스스로 체크 (Verification)]
- [ ] 왜 **배터리 화재 원인 분석**에 CT 검사가 핵심적인가? (정답: 배터리를 분해하면 내부 구조가 흐트러져 발화 지점을 찾기 어렵지만, CT는 밀봉된 상태 그대로 내부의 미세 금속 이물질이나 전극의 정렬 상태를 3D로 확인할 수 있기 때문)
- [ ] **Voxel (복셀)**이란 무엇인가?
- [ ] **Beam Hardening** 현상이 이미지에 미치는 구체적인 영향은? (정답: 시편의 가장자리는 밝게 보이고 중앙부는 어둡게 왜곡되어, 재질의 밀도가 균일함에도 불구하고 불균일한 것처럼 보이는 오류를 야기함)

*Reference: Industrial X-ray Computed Tomography (Carmignato), Digital Image Processing (Gonzalez), Antigravity Quality-Lab.*
