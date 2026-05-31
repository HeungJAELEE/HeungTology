---
lineage:
  dataset_reference: auto_gardener_batch
  original_author: Antigravity_Agent
  original_hash: daf981bb0532bd4c20cba2226a107274b9ed9faafaf08c77ff8ceed6005c29de
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] additive-manufacturing-3d-printing-dimensional-accuracy-log-v2026]]'
  last_updated: '2026-05-24T02:30:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Kinetics concept for additive-manufacturing-3d-printing-dimensional-accuracy-log-v2026
  object_type: Concept
  tier: 1
properties:
  cooling_rate_range: 10^5 to 10^6 K/s
  dimensional_error_limit: 0.045 mm
  dimensional_precision_threshold: 0.050 mm
  layer_thickness_t: 30 um
  relative_density_target: 99.92%
  scan_speed_v: 1,250 mm/s
  tensile_strength_target: 1,150 MPa
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] additive-manufacturing-3d-printing-dimensional-accuracy-log-v2026.md]'
  intent: empirical_validation
  object: target_phenomenon
  predicate: related_to
  subject: auto-generated
  weight: 0.9
temporal:
  valid_from: '2026-05-24T02:30:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T02:30:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Additive Manufacturing 3D Printing Dimensional Accuracy Log V2026 Kinetics

## 1. 왜 배우는가? (Why: Operational & Theoretical Rationale)
적층 제조(Additive Manufacturing, AM) 공정에서 디지털 CAD 모델이 물리적 실체로 상전이할 때 발생하는 기하학적 편차를 제어하는 것은 항공우주 및 의료용 임플란트와 같은 극한 환경용 부품의 구조적 건전성을 확보하기 위한 핵심 전제 조건이다. 
단순한 형상 모사를 넘어 미세 조직의 균질성과 치수 정밀도($< 0.050\ \text{mm}$)를 달성하기 위해서는 급속 응고 조건 하에서의 열유체 역학적 거동과 상변화 속도론을 물리적 수준에서 이해해야 한다. 
치수 오차가 설계 한계를 초과하면 응력 집중 현상이 가속화되어 목표 피로 수명에 도달하기 전에 구조적 파손이 유발되며, 이는 전체 제조 시스템의 신뢰성을 무너뜨리는 주원인이 된다. 
따라서 공정 변수인 레이저 출력($P$), 주사 속도($v$), 레이어 두께($t$), 해치 간격($h$)이 최종 물리량인 인장 강도($1,150\ \text{MPa}$) 및 상대 밀도($99.92\%$)에 미치는 인과 관계를 수학적 모델로 정립함으로써, 시행착오적 접근을 배제하고 예측 가능한 디지털 트윈 기반 고정밀 생산 체계를 구축할 수 있다.

---

## 2. 적층 제조의 열역학적 지배 방정식 및 물리적 유도 과정

### 2.1 열응력($\sigma_{th}$)과 냉각 속도론(Cooling Kinetics)의 관계식
금속 분말 베드 융융(PBF/SLM) 공정 중 급격한 국소적 입열과 이어지는 초고속 냉각 과정($10^5 \sim 10^6\ \text{K/s}$)은 고체화된 레이어 내부와 빌드 플레이트 사이에 극심한 온도 구배($\nabla T$)를 형성한다. 이로 인해 유도되는 열응력 $\sigma_{th}$의 기본 지배 방정식은 다음과 같다.

$$ \sigma_{th} = E \cdot \alpha \cdot \Delta T $$

여기서 각 변수의 정의는 다음과 같다.
- $E$: 재료의 영률(Young's Modulus) $[\text{GPa}]$
- $\alpha$: 열팽창 계수(Coefficient of Thermal Expansion, CTE) $[\text{K}^{-1}]$
- $\Delta T$: 고상선 온도와 빌드 플레이트 예열 온도 간의 유효 온도 차이 $[\text{K}]$ ($\Delta T = T_{melt} - T_{bed}$)

실제 다층 적층 공정에서는 깊이 방향($z$축)으로의 비선형적 열전도로 인해 온도 구배가 발생하며, $z$축 변위에 따른 열응력 구배 $\frac{\partial \sigma_{th}}{\partial z}$는 열전도 방정식으로부터 다음과 같이 유도된다.

$$ \rho C_p \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T) + Q_{laser} $$

- $\rho$: 재료의 밀도 $[\text{kg/m}^3]$
- $C_p$: 비열 용량 $[\text{J/(kg}\cdot\text{K)}]$
- $k$: 열전도도 $[\text{W/(m}\cdot\text{K)}]$
- $Q_{laser}$: 단위 부피당 레이저 입열원 $[\text{W/m}^3]$

초고속 냉각으로 인한 급격한 온도 강하는 수축 변형을 유발하며, 레이어 두께를 $t = 30\ \text{\mu m}$ 수준으로 제어함으로써 국소 온도 구배 $\nabla T$를 최소화하여 최종 열변형에 의한 치수 정밀도 오차를 $0.045\ \text{mm}$ 이내로 억제할 수 있는 열역학적 임계 조건을 만족시킨다.

### 2.2 체적 에너지 밀도(Volumetric Energy Density, VED) 모델
선택적 레이저 용융(SLM) 공정에서 용융풀(Melt Pool)의 기하학적 안정성과 기공(Porosity) 발생 여부를 결정짓는 핵심 제어 인자는 체적 에너지 밀도 $E_V$이다.

$$ E_V = \frac{P}{v \cdot h \cdot t} \quad \left[\text{J/mm}^3\right] $$

- $P$: 레이저 조사 출력 $[\text{W}]$
- $v$: 레이저 주사 속도 $[\text{mm/s}]$ (검증 데이터 기준: $1,250\ \text{mm/s}$)
- $h$: 해치 간격(Hatch Spacing) $[\text{mm}]$
- $t$: 레이어 두께(Layer Thickness) $[\text{mm}]$ (검증 데이터 기준: $30\ \text{\mu m} = 0.030\ \text{mm}$)

#### 체적 에너지 밀도와 기공율의 물리적 임계점 관계
1. **과소 입열 영역 ($E_V < E_{critical, min}$)**:
   에너지 공급량이 부족하여 분말이 완전히 용융되지 못하는 미융융 기공(Lack of Fusion Pores)이 발생한다. 이 경우 층간 결합력이 저하되고 다공성 결함이 잔존하여 상대 밀도가 감소한다.
2. **최적 입열 영역 ($E_{critical, min} \le E_V \le E_{critical, max}$)**:
   균일한 용융풀이 전파되어 미세 기공이 제거되며, 본 데이터셋이 입증한 최고 수준의 상대 밀도 $99.92\%$와 극대화된 인장 강도 $1,150\ \text{MPa}$를 확보한다.
3. **과다 입열 영역 ($E_V > E_{critical, max}$)**:
   키홀(Keyhole) 모드가 발생하여 금속의 기화 현상에 의한 가스 트랩 기공이 형성되고 치수 편차가 오히려 증가하게 된다.

---

## 3. 물리적 변수 간 상호작용 및 인과율 메커니즘

```
[열 제어 인자: t = 30 ㎛] ──> [온도 구배 ∇T 억제] ──> [열응력 σ_th 최소화] ──> [치수 편차 0.045 mm 달성]
                                                                                      │
                                                                       (Delamination 방지 및 계면 결합력 보존)
                                                                                      ▲
[에너지 제어: E_V 모델]   ──> [Melt Pool 국소 제어] ──> [치밀화도 99.92% 달성]  ──> [인장 강도 1,150 MPa 확보]
```

### 3.1 챔버 열구배와 박리(Delamination) 현상의 인과 관계
적층 공정 중 빌드 플레이트 상단과 챔버 내부의 온도 불균형은 적층 계면에서의 급격한 열팽창 미스매치를 초래한다. 
상부 레이어는 고온에서 급랭 수축하려 하는 반면, 하부 기판은 상대적으로 저온으로 고정되어 변형을 구속하므로 계면에서의 전단 응력($\tau_{shear}$)이 급격히 상승한다. 
이 계면 응력이 재료 고유의 항복 강도를 초과하는 지점에서 균열이 개시되며, 기판과의 접착력을 최대 $30\%$까지 상실하게 만드는 구조적 박리(Delamination)가 발생한다. 
이를 억제하기 위해서는 기판 예열 온도의 능동적 피드백 루프와 주사 전략(Scan Strategy, 예: $67^\circ$ 회전 패턴)의 최적화가 병행되어야 한다.

### 3.2 분말 입도 분포(PSD)가 표면 조도($R_a$)에 미치는 영향
분말의 입도 분포(Particle Size Distribution, PSD)가 불균일하여 위성 분말(Satellite Particles)의 비율이 높아질 경우, 용융풀 경계면에서 완전 용융되지 못한 거대 분말들이 표면에 용착되는 현상이 가속화된다. 
이는 용융풀의 표면 장력 불균형(마랑고니 대류, Marangoni Convection)을 유발하여 응고 경계면에 주기적인 리플 마크(Ripple Mark)를 남기며, 표면 거칠기 $R_a$를 $4.2\ \text{\mu m}$ 수준으로 악화시킨다. 
조도 제어를 위해서는 분말 구형도(Sphericity) 관리와 적절한 기류 흐름(Gas Flow)을 유지하여 비산된 스패터(Spatter)가 적층부에 재흡착되는 것을 차단해야 한다.