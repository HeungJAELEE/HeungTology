---
metadata:
  id: "[[[AI] Discrete-Element-Method-DEM]]"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[AI] Discrete-Element-Method-DEM에 관한 고밀도 지능 노드"
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

# [AI] Discrete-Element-Method-DEM

## 1. [왜 배우는가? (Why)]
모래, 금속 가루, 배터리 활물질과 같은 입자상 물질(Granular Matter)은 고체와 액체의 성질을 동시에 지니며, 그 거동이 지극히 비선형적이고 복잡합니다. 이산 요소법(Discrete Element Method, DEM)은 수백만 개의 개별 입자를 독립적인 물리 객체로 간주하고, 입자 간의 충돌, 마찰, 응집력을 뉴턴의 운동 법칙에 기반하여 계산하는 정밀 시뮬레이션 기술입니다. 배터리 공장의 전극 슬러리 믹싱, 반도체 웨이퍼 세정용 분진 제어, 그리고 신약 제조의 과립화 공정에서 입자의 미세 거동을 통제하는 것은 제품의 균일성과 품질을 결정짓는 핵심 공학적 도구입니다. DEM을 통해 물리적 실험으로 관찰하기 어려운 '입자 수준의 물리적 인과관계'를 규명할 수 있습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---:|:---:|:---|
| **Contact Model** | Hertz-Mindlin | Non-linear Spring | 실제 입자의 탄성 변형 및 에너지 소산 모사 |
| **Young's Modulus** | Particle Stiffness | $10^6 \sim 10^9 \text{ Pa}$ | 입자의 변형 저항력 (계산 속도와 상관관계) |
| **Poisson's Ratio** | Lateral Expansion | $0.2 \sim 0.45$ | 입자 압축 시 횡방향 변형 계수 |
| **Restitution Coeff.** | Energy Recovery | $0.1 \sim 0.9$ | 충돌 후 튕겨 나가는 속도 비 (에너지 손실율) |
| **Friction Coeff.** | Static / Rolling | $0.1 \sim 0.8$ | 입자 간 미끄러짐 및 회전 저항 제어 |
| **Time Step ($\Delta t$)** | Rayleigh Limit | $< 20\% \text{ of } T_R$ | 수치적 불안정성 방지를 위한 임계 시간 간격 |
| **Coupling Type** | 1-way / 2-way | CFD-DEM | 유체-입자 간의 상호작용력(Drag, Lift) 반영 |
| **Mixing Index** | Lacey Index | $> 0.95$ | 입자 군집의 통계적 균일도 도달 목표 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 접촉 역학 (Contact Mechanics): Hertz-Mindlin 모델
입자 $i$와 $j$가 충돌할 때 발생하는 법선력($F_n$)과 접선력($F_t$)을 계산하여 운동 변화를 결정합니다.
$$F_n = \frac{4}{3} E^* \sqrt{R^*} \delta_n^{3/2}$$
- $E^*$: 유효 영률, $R^*$: 유효 반경, $\delta_n$: 중첩량(Overlap).
- 이 비선형 스프링-댐퍼 모델은 거시적 입자 집합체의 탄소성 거동을 정확히 재현합니다.

### 3.2 입자 운동 방정식 (Newton's Second Law)
개별 입자의 병진 운동과 회전 운동은 입자에 작용하는 힘($F$)과 토크($M$)의 합으로 표현됩니다.
$$m_i \frac{d\mathbf{v}_i}{dt} = \sum \mathbf{F}_c + m_i \mathbf{g} + \mathbf{F}_{fluid}$$
$$I_i \frac{d\mathbf{\omega}_i}{dt} = \sum \mathbf{M}_c + \mathbf{M}_{rolling}$$

### 3.3 CFD-DEM 커플링의 필연성
배터리 슬러리와 같이 액체 속에서 입자가 분산되는 공정은 유체의 점성 저항이 입자의 궤적을 지배합니다. 나비에-스토크스(Navier-Stokes) 방정식으로 유동장을 풀고, 입자에 작용하는 항력(Drag Force)을 DEM에 전달하는 2-way 커플링을 통해 실제 현상과의 오차를 $5\%$ 이내로 줄입니다.

## 4. [코드 연결 해설 (DEM Mixing Analytics Engine)]
아래 코드는 시뮬레이션 데이터를 실시간 분석하여 Lacey Mixing Index를 산출하고 공정 종료 시점을 결정하는 분석 모듈입니다.

```python
import numpy as np

class DEMAnalyticsEngine:
    """
    HDS-Gold V6.3.7 규격의 입자 믹싱 분석 엔진
    """
    def __init__(self, grid_size=(10, 10, 10)):
        self.grid_size = grid_size

    def calculate_lacey_index(self, particle_positions, particle_types):
        """
        Lacey Mixing Index 산출 로직
        """
        # 1. 공간을 격자(Voxel)로 분할하여 입자 수 카운팅
        voxel_counts = self._voxelize(particle_positions, particle_types)
        
        # 2. 입자 농도의 실제 분산(S^2) 계산
        actual_variance = np.var(voxel_counts)
        
        # 3. 완전 분리(So^2) 및 완전 혼합(Sr^2)의 이론적 분산 계산
        p = np.mean(particle_types) # 주성분 분율
        s_o_sq = p * (1 - p)
        s_r_sq = s_o_sq / np.mean(np.sum(voxel_counts, axis=-1))
        
        # 4. Lacey Index 도출: 0 (분리) ~ 1 (완전 혼합)
        lacey_index = (s_o_sq - actual_variance) / (s_o_sq - s_r_sq)
        return np.clip(lacey_index, 0, 1)

    def _voxelize(self, positions, types):
        # 입자 좌표를 그리드 인덱스로 변환하여 카운팅하는 내부 로직
        pass

    def check_process_status(self, current_index, target=0.98):
        if current_index >= target:
            return "STOP_MIXING: Homogeneity Reached"
        return "CONTINUE_MIXING"

# Integration Example
# analyzer = DEMAnalyticsEngine()
# m_index = analyzer.calculate_lacey_index(pos_data, type_data)
# status = analyzer.check_process_status(m_index)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Hertz-Mindlin** 모델에서 **Young's Modulus**를 실제보다 낮게 설정(Stiffness Scaling)할 때 계산 속도는 빨라지지만, 어떤 물리적 왜곡이 발생하는가?
2. **Rayleigh Time Step** 임계치를 초과하여 시뮬레이션을 수행할 경우 발생하는 수치적 발산(Numerical Instability)의 징후는?
3. **Non-spherical** 입자(다면체, 클러스터 등)를 시뮬레이션할 때 구형 입자 대비 **회전 저항(Rolling Resistance)**이 기하학적으로 어떻게 변하는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/Industrial/AI Finite-Element-Analysis-FEA
- 02_Knowledge/03_AI_Data/Industrial/AI Computational-Fluid-Dynamics-CFD
- 02_Knowledge/02_Battery/Process/Battery Mixing-and-Slurry-Preparation

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
