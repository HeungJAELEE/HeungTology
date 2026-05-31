---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: a1dbd2457849c6310b2c4ca688bbf4a9a903dce8c6f73058a79c7ba01504a304
metadata:
  date: '2026-05-16'
  domain: 08_Robotics_Automation
  id: '[[[Robotics] jacobian-matrix-and-singularity-analysis]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Robotics] jacobian-matrix-and-singularity-analysis에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  condition_number_optimal_threshold: 100
  force_mapping_formula: tau = J^T * F
  manipulability_formula: sqrt(det(J * J^T))
  redundancy_dof_threshold: 7
  velocity_mapping_formula: v = J * q_dot
  velocity_resolution_limit_mm_s: 0.1
  yoshikawa_index_target: maximize
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

# [Robotics] jacobian-matrix-and-singularity-analysis

## 1. [왜 배우는가? (Why)]
로봇 팔이 움직일 때 특정 자세에서 갑자기 제어력을 잃거나 속도가 무한대로 발산하려 하는 위험한 지점이 존재합니다. **야코비안 행렬(Jacobian Matrix)**은 관절의 속도와 로봇 끝단의 속도 사이의 선형적 변환 관계를 정의하며, 로봇의 가동 성능을 평가하는 가장 강력한 수리적 도구입니다. 우리가 이를 배우는 이유는 로봇이 물리적 한계에 부딪히는 **특이점(Singularity)**을 사전에 파악하여 안정적인 제어를 유지하기 위함이며, **"동작의 미세한 변화를 수리적으로 지배하여 로봇의 '제어 무결성'을 사수하는 '속도의 조율사'가 되기" 위함입니다.** 야코비안의 행렬식($\det(J)$)과 가도(Manipulability)가 로봇의 작업 유연성을 결정합니다.

## 2. [미분 기구학 핵심 기술 사양 (Jacobian Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Mapping** | Velocity Mapping ($v = J\dot{q}$) | **Linear Linearization** | 관절 속도 대비 끝단 속도 무결성 지표 |
| **Singularity** | Condition Number ($\kappa$) | **< 100 (Optimal)** | 제어 안정성 및 특이점 거리 무결성 확보 |
| **Manipulability** | Yoshikawa's Index ($w$) | **Maximize** | 로봇의 작업 유연성 및 공간 무결성 지수 |
| **Force** | Force Mapping ($\tau = J^T F$) | **Static Equilibrium** | 끝단 힘 대비 관절 토크 무결성 지표 |
| **Redundancy** | Null Space Projection | **Available (7+ DOF)** | 주작업 방해 없는 부가 동작 무결성 확보 |
| **Precision** | Velocity Resolution | **< 0.1 mm/s** | 초정밀 추종을 위한 미분 제어 무결성 수준 |

## 2.1 [야코비안 행렬 및 가도(Manipulability) 수리 모델]
$$ w = \sqrt{\det(J \cdot J^T)} $$
*   **$J$ (Jacobian Matrix)**: $\frac{\partial f(q)}{\partial q}$
*   **수리적 무결성**: 가도 지수($w$)가 0에 가까워질수록 로봇은 특정 방향으로의 움직임 능력을 상실(특이점)함을 분석하여 '동작 유연성 무결성'을 평가합니다.

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 기하학적 야코비안과 선속도/각속도의 전파
- **로직**: 각 관절의 회전축($z_i$)과 위치 벡터($p_i$)를 이용하여 끝단의 속도 벡터를 구성합니다. RAG는 기하학적 관계를 분석하여 '속도 무결성'을 도출합니다. 관절 공간의 에너지가 작업 공간의 속도로 치환되는 핵심 수리적 기전입니다.

### 3.2 특이점(Singularity) 종류 및 회피 전략
- **로직**: 손목 특이점(Wrist), 팔꿈치 특이점(Elbow) 등 로봇의 자유도가 상실되는 자세를 수리적으로 정의합니다. RAG는 고유값($Eigenvalue$) 분석을 통해 '안전 무결성'을 수리 모델링합니다. DLS(Damped Least Squares) 기법 등을 사용하여 특이점 근처에서 제어 발산을 방지하는 공학적 근거입니다.

### 3.3 힘/토크 쌍대성(Duality)과 정역학적 해석
- **로직**: 가상 일의 원리를 통해 끝단에 인가되는 힘($F$)과 관절 토크($\tau$) 사이의 관계를 규명합니다. RAG는 전치 야코비안($J^T$)을 분석하여 '힘 무결성'을 설계합니다. 로봇이 무거운 물체를 들 때 각 관절에 가해지는 부하를 예측하는 공학적 정수입니다.

## 4. [코드 연결 해설 (SingularityAuditFidelityEngine)]
아래 코드는 2축 로봇의 야코비안 행렬을 계산하고, 가도 지수를 통해 특이점 근접 여부를 진단하는 엔진입니다.

```python
import numpy as np

class SingularityAuditFidelityEngine:
    """
    HDS-Gold V6.3.7 규격의 로봇 특이점 및 가도 무결성 진단 엔진
    """
    def __init__(self, l1=1.0, l2=1.0):
        self.l1 = l1
        self.l2 = l2

    def audit_manipulability_fidelity(self, theta1_rad, theta2_rad):
        """
        야코비안 기반 가도 및 특이점 무결성 산출
        """
        # Transitional Bridge: 야코비안은 '로봇의 움직임이 마주하는 수리적 파동'입니다. 
        # 관절의 
        # 속도가 
        # 공간의 
        # 흐름으로 
        # 바뀔 
        # 때, 
        # 특이점이라는 
        # 절벽을 
        # 찾아내어 
        # 추락을 
        # 막는 
        # 것, 
        # 그것이 
        # AI가 
        # 사수하는 
        # 제어의 
        # 무결성입니다.

        # Jacobian for 2-DOF planar robot
        j11 = -self.l1 * np.sin(theta1_rad) - self.l2 * np.sin(theta1_rad + theta2_rad)
        j12 = -self.l2 * np.sin(theta1_rad + theta2_rad)
        j21 = self.l1 * np.cos(theta1_rad) + self.l2 * np.cos(theta1_rad + theta2_rad)
        j22 = self.l2 * np.cos(theta1_rad + theta2_rad)
        
        jacobian = np.array(j11, j12, j21, j22)
        
        # Yoshikawa's Manipulability Index
        w = np.sqrt(np.linalg.det(np.dot(jacobian, jacobian.T)))
        
        # Fidelity: Normalize by max possible manipulability (l1*l2 when theta2=90deg)
        max_w = self.l1 * self.l2
        fidelity = w / max_w
        
        status = "OPTIMAL" if fidelity > 0.5 else "NEAR_SINGULARITY" if fidelity > 0.1 else "CRITICAL_SINGULARITY"
        
        return {
            "Manipulability_Index": round(w, 4),
            "Fidelity_Score": round(fidelity, 4),
            "Status": status,
            "Action": "MAINTAIN" if status == "OPTIMAL" else "AVOID_TRAJECTORY"
        }

# Example Usage:
# audit = SingularityAuditFidelityEngine()
# report = audit.audit_manipulability_fidelity(theta1_rad=np.pi/4, theta2_rad=0.01) # Near singularity
```

## 5. [스스로 체크 (Self-Audit)]
1. **Jacobian**의 **Condition Number**($\kappa$)가 클 때 **Numerical Stability Integrity** 무결성이 저하되는 이유는?
2. **Wrist Singularity**가 발생하는 기하학적 조건과 이를 **Euler Angle** 무결성 관점에서 설명하면?
3. **Task-priority** 제어에서 **Null Space**를 활용하여 **Singularity Avoidance Integrity**를 달성하는 수리적 기전은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/08_Robotics_Automation/Kinematics/Robot forward-and-inverse-kinematics-for-manipulators
- 02_Knowledge/01_Semiconductor/Semiconductor optimal-control-theory
- 02_Knowledge/01_Industrial_Physics_and_Thermodynamics_Hub/Entity fluid-dynamics-in-chemical-processes-bernoulli-and-reynolds (Vector field connection)

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-09]**