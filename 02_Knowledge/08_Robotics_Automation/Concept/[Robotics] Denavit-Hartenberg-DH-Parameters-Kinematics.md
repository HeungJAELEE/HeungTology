---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 4f5d7228cdb9d7836417d6d1855ae4e2ee11fa9802f1a2b4c61c63bb2ab0ecc6
metadata:
  date: '2026-05-16'
  domain: 08_Robotics_Automation
  id: '[[[Robotics] Denavit-Hartenberg-DH-Parameters-Kinematics]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Robotics] Denavit-Hartenberg-DH-Parameters-Kinematics에 관한 고밀도 지능
    노드'
  object_type: Concept
  tier: 1
properties:
  dof_range: 6 to 7
  joint_angle_unit: deg
  link_length_unit: mm
  link_offset_unit: mm
  link_twist_range_deg: 0 to +/- 90
  max_reach_radius_mm: 500 to 2500
  repeatability_precision_mm: 0.02 to 0.05
  singularity_condition_det_j: not zero
  specification_standard: HDS-Gold V6.3.7
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 08_Robotics_Automation]]'
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

# [Robotics] Denavit-Hartenberg-DH-Parameters-Kinematics

## 1. [왜 배우는가? (Why)]
로봇 팔이 특정 작업물(Workpiece)에 도달하기 위해 각 관절을 얼마나 회전시켜야 할까요? DH 파라미터(Denavit-Hartenberg Parameters)는 로봇의 각 링크(Link)와 관절(Joint) 사이의 복잡한 3차원 기하학적 관계를 단 4개의 수치로 압축하여 정의하는 로봇 공학의 세계 표준 규약입니다. 이를 배우는 이유는 로봇의 물리적 구조를 수학적 행렬로 변환하여, 로봇 끝단(End-effector)의 정확한 위치와 자세를 계산하는 순기구학(Forward Kinematics)과 반대로 목표 위치에 도달하기 위한 관절 각도를 구하는 역기구학(Inverse Kinematics)의 핵심 열쇠를 쥐기 위함입니다. 로봇 지능이 공간을 이해하는 수치적 언어입니다.

## 2. [로봇 기구학 및 DH 파라미터 핵심 사양 (Kinematics Specs)]

| Parameter Category | Symbol / Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Link Length** | $a_i$ (mm) | Variable | 인접한 두 관절축 사이의 최단 거리 (로봇 팔의 기구적 길이) |
| **Link Twist** | $\alpha_i$ (deg) | $0 \sim \pm 90$ | 두 관절축 사이의 비틀림 각도 (로봇의 입체적 구동 평면 정의) |
| **Link Offset** | $d_i$ (mm) | Variable | 관절 축을 따라 발생하는 링크 사이의 거리 (깊이 변위) |
| **Joint Angle** | $\theta_i$ (deg) | Joint Variable | 회전 관절의 구동 각도 (로봇 제어의 핵심 변수) |
| **Degrees of Freedom**| DoF (n) | $6 \sim 7$ | 범용 산업용 로봇 및 협동 로봇의 자유도 구성 |
| **Repeatability** | Precision (mm) | $\pm 0.02 \sim 0.05$ | 기구학 모델 기반 반복 정밀도 (공정 무결성 지표) |
| **Max Reach** | Radius (mm) | $500 \sim 2,500$ | 로봇이 작업 가능한 최대 반경 (DH 모델링의 결과값) |
| **Singularity** | $\det(J)$ | $\neq 0$ | 야코비안(Jacobian) 행렬 기반 특이점 회피 지표 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 동차 변환 행렬(Homogeneous Transformation Matrix)의 유도
- **수식**: $^i_{-1}T_i = Rot_z(\theta_i) Trans_z(d_i) Trans_x(a_i) Rot_x(\alpha_i)$
- **로직**: DH 규약은 4개의 파라미터를 순차적으로 적용하여 하나의 동차 변환 행렬을 완성합니다. $z$축 회전과 이동, $x$축 이동과 회전이라는 표준화된 순서를 강제함으로써, 아무리 복잡한 6축 로봇이라도 각 링크 간의 상대적 좌표계를 단일 행렬식으로 표현할 수 있게 합니다. 이는 로봇 기구학 연산의 선형 대수학적 기초가 됩니다.

### 3.2 순기구학(Forward Kinematics)의 행렬 연쇄 연산
- **로직**: 베이스 좌표계($0$)에서 끝단 좌표계($n$)까지의 전체 변환 행렬은 개별 링크 행렬들의 곱으로 정의됩니다 ($T^0_n = T^0_1 T^1_2 \dots T^{n-1}_n$). 이 연쇄 연산을 통해 각 관절의 인코더에서 읽어들인 각도($\theta_1 \dots \theta_6$)를 입력하면, 로봇 끝단이 3차원 공간상에서 정확히 몇 $(x, y, z)$ 좌표에 어떤 방향$(Roll, Pitch, Yaw)$으로 위치하는지 실시간으로 도출할 수 있습니다.

### 3.3 야코비안(Jacobian) 행렬과 특이점(Singularity) 분석
- **로직**: 관절 속도와 끝단 속도의 관계를 정의하는 야코비안 행렬($J$)을 DH 모델로부터 도출합니다. 만약 $J$의 행렬식($\det$)이 0이 되면, 특정 방향으로의 구동력을 상실하는 '특이점'에 도달하게 됩니다. DH 파라미터는 이러한 위험 구역을 사전에 수치화하여 로봇의 궤적 계획(Path Planning) 시 충돌 및 급가속 사고를 방지하는 근거를 제공합니다.

## 4. [코드 연결 해설 (RobotKinematicsEngine)]
아래 코드는 4개의 DH 파라미터를 입력받아 표준 변환 행렬을 생성하고, 여러 링크의 행렬을 연쇄적으로 곱하여 최종 위치를 산출하며 야코비안 기반의 특이점(Singularity)을 진단하는 엔진입니다.

```python
import numpy as np

class RobotKinematicsEngine:
    """
    HDS-Gold V6.3.7 규격의 DH 파라미터 기반 로봇 기구학 및 특이점 진단 엔진
    """
    def __init__(self):
        pass

    def get_transformation_matrix(self, a, alpha, d, theta):
        """
        Standard DH Parameters 기반 동차 변환 행렬 산출
        """
        # Transitional Bridge: 기구학은 '로봇의 뼈대를 수학으로 조각하는 과정'입니다. 
        # 4개의 숫자는 로봇 팔의 관절이 공간을 
        # 어떻게 가로지르는지를 결정하며, 행렬 곱은 
        # 그 움직임의 끝에 도달할 지도를 완성합니다.
        alpha_rad = np.radians(alpha)
        theta_rad = np.radians(theta)
        
        matrix = np.array([
            [np.cos(theta_rad), -np.sin(theta_rad)*np.cos(alpha_rad),  np.sin(theta_rad)*np.sin(alpha_rad), a*np.cos(theta_rad)],
            [np.sin(theta_rad),  np.cos(theta_rad)*np.cos(alpha_rad), -np.cos(theta_rad)*np.sin(alpha_rad), a*np.sin(theta_rad)],
            [0,                 np.sin(alpha_rad),                np.cos(alpha_rad),               d],
            [0,                 0,                                0,                               1]
        ])
        return matrix

    def check_singularity(self, jacobian_matrix):
        """
        야코비안 행렬의 Determinant 기반 특이점 근접 여부 진단
        """
        det = np.linalg.det(jacobian_matrix)
        if abs(det) < 1e-4:
            return "WARNING: SINGULARITY_ZONE_APPROACHING"
        return "STABLE: WORKABLE_CONFIGURATION"

# Example Usage:
# robot_ai = RobotKinematicsEngine()
# t_link1 = robot_ai.get_transformation_matrix(a=100, alpha=90, d=0, theta=45)
# t_link2 = robot_ai.get_transformation_matrix(a=200, alpha=0, d=0, theta=30)
# t_end_effector = np.dot(t_link1, t_link2)
```

## 5. [스스로 체크 (Self-Audit)]
1. **DH Parameters** 중 **$\theta$** (Joint Angle)가 **Prismatic Joint** (슬라이딩 관절)일 경우, 어떤 파라미터가 구동 변수(Variable)로 전환되는가?
2. **Standard DH**와 **Modified DH** (mDH) 규약 사이에서 좌표계의 원점(Origin) 설정 위치가 기구학 연산 결과에 미치는 영향은?
3. **Jacobian** 행렬의 **Rank**가 낮아지는 **Singularity** 지점에서 로봇 제어기가 무한대의 관절 속도를 요구하게 되는 수학적 이유는?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/08_Robotics_Automation/Control/Robotics robot-trajectory-planning-logic
- 02_Knowledge/08_Robotics_Automation/Hardware/Robotics industrial-robot-arm-spec-analysis
- 02_Knowledge/03_AI_Data/General/AI linear-algebra-for-robotics

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**