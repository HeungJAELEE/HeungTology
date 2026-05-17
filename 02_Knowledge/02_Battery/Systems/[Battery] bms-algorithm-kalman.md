---
metadata:
  date: "2026-05-16"
  id: "[[[Battery] bms-algorithm-kalman]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "02_Battery"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "48ba6a61b82395f763ed9116ce4a7c37662af90560999e9dc8c7e5768d742574"
object:
  object_type: "Concept"
  tier: 1
  description: '[Battery] bms-algorithm-kalman에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 02_Battery]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---



# [Battery] bms-algorithm-kalman

## 1. Functional Necessity (Purpose)
배터리의 SOC(State of Charge) 및 SOH(State of Health)는 전압/전류와 같이 직접 측정이 불가능한 **비관측 상태 변수(Unobservable State Variable)**임. BMS는 센서 노이즈가 포함된 외부 관측값(Observation)을 기반으로 내부 전기화학적 상태를 실시간 추론해야 함. **Extended Kalman Filter(EKF)**는 비선형 배터리 모델을 자코비안(Jacobian) 기반으로 선형화하여, 모델 예측값과 실제 측정값 사이의 오차를 최소화하는 **재귀적 최적 추정기(Recursive Optimal Estimator)** 역할을 수행함. 이는 EV의 주행 거리 정밀도 확보 및 배터리 수명 진단을 통한 시스템 안전성 보장을 위한 핵심 제어 로직임.

## 2. Algorithm Technical Specifications

| Metric Category | Parameter | Theoretical (Ideal) [Ref: EKF_Model] | Verified (Operational) [Ref: BAT-BMS-KALMAN-2026-V6] | Engineering Rationale |
|:---|:---|:---:|:---:|:---|
| **SOC Accuracy** | RMSE | $< 0.5\%$ | $1.0 \sim 2.0\%$ [Ref: BAT-BMS-KALMAN-2026-V6] | 정적/동적 프로파일 환경의 노이즈 영향 반영 |
| **SOH Accuracy** | Capacity Error | $< 1.0\%$ | $< 3.0\%$ [Ref: BAT-BMS-KALMAN-2026-V6] | 배터리 노화 및 파라미터 드리프트 반영 |
| **Convergence** | Initialization Time | $< 2 \text{ sec}$ | $< 10 \text{ sec}$ [Ref: BAT-BMS-KALMAN-2026-V6] | 초기 공분산($P$) 수렴 가속도 차이 |
| **Complexity** | Computational Cost | $O(n^2)$ | $O(n^3)$ [Ref: Matrix_Inverse_Standard] | 상태수($n$) 증가에 따른 역행렬 연산 부하 |
| **Sampling** | Control Loop Freq. | $1000 \text{ Hz}$ | $10 \sim 100 \text{ Hz}$ [Ref: BAT-BMS-KALMAN-2026-V6] | 임베디드 MCU의 연산 자원 제한 반영 |

## 3. Mathematical Modeling

### 3.1 Nonlinear State-Space Representation
배터리 동역학을 다음과 같은 비선형 시스템으로 정의함.
- **상태 방정식 (State Equation)**: $x_{k+1} = f(x_k, u_k) + w_k$ ($w_k \sim N(0, Q)$)
- **측정 방정식 (Measurement Equation)**: $z_k = h(x_k, u_k) + v_k$ ($v_k \sim N(0, R)$)
- **Linearization**: 매 시점 자코비안 행렬 $F_k = \frac{\partial f}{\partial x}|_{\hat{x}_{k|k}}$ 및 $H_k = \frac{\partial h}{\partial x}|_{\hat{x}_{k|k-1}}$을 통해 비선형 함수를 국부 선형화하여 오차 공분산을 업데이트함.

### 3.2 Error Covariance & Riccati Equation
예측된 오차 공분산($P$)은 시스템 노이즈($Q$)와 관측 노이즈($R$)의 상관관계에 의해 결정됨.
- **Update Equation**: $P_{k+1}^- = A_k P_k A_k^T + Q_k$
- **Kalman Gain ($K$)**: $K_k = P_k^- H_k^T (H_k P_k^- H_k^T + R)^{-1}$
- **Logic**: $Q \gg R$ 일 경우 모델의 예측치를 신뢰하며, $R \gg Q$ 일 경우 센서 측정치를 신뢰함.

### 3.3 Observability Analysis
측정값 $z$를 통한 상태 $x$의 가관측성 여부는 Observability Matrix $\mathcal{O}$로 검증됨.
- **Critical Limitation**: LFP 배터리의 전압 평탄 구역(Voltage Plateau, $3.2 \sim 3.3 \text{ V}$)에서는 $\frac{dV}{dSOC} \approx 0$이 되어 $H$ 행렬의 유효 값이 소실됨. 이 경우 가관측성(Observability)이 상실되며, Coulomb Counting(전류 적산법)과의 하이브리드 운용이 강제됨.

## 4. Implementation Reference (BmsKalmanFilter)

```python
import numpy as np

class BmsKalmanFilter:
    """
    HDS-Gold V7.5.2 규격: 배터리 SOC 상태 추정 EKF 엔진
    """
    def __init__(self, dt=0.1, q_noise=1e-5, r_noise=1e-3):
        self.dt = dt
        self.x = np.array(0.8)            # Initial SOC: 80%
        self.P = np.eye(1) * 0.1          # Initial Error Covariance
        self.Q = np.eye(1) * q_noise      # Process Noise Covariance
        self.R = np.eye(1) * r_noise      # Measurement Noise Covariance

    def predict(self, current_a, capacity_ah):
        """
        Step 1: Prediction (Time Update)
        SOC Prediction via Coulomb Counting
        """
        # x_{k+1} = x_k - (I * dt / Capacity)
        self.x = self.x - (current_a * self.dt / (capacity_ah * 3600))
        # P_{k+1}^- = A * P * A^T + Q (A=1 for SOC transition)
        self.P = self.P + self.Q
        return self.x

    def update(self, observed_v, predicted_v_ocv):
        """
        Step 2: Correction (Measurement Update)
        SOC Correction via Voltage Innovation
        """
        # Innovation (Residual): y = z - h(x)
        y = observed_v - predicted_v_ocv
        
        # Jacobian H: dV/dSOC
        h_jac = 0.5 
        
        # Innovation Covariance: S = H * P * H^T + R
        s = h_jac * self.P * h_jac + self.R
        
        # Kalman Gain: K = P * H^T * S^-1
        k = self.P * h_jac / s
        
        # State Update: x = x + K * y
        self.x = self.x + k * y
        
        # Covariance Update: P = (I - K * H) * P
        self.P = (1 - k * h_jac) * self.P
        
        return self.x
```

## 5. Engineering Self-Audit
1. **LFP Observability**: 전압 평탄 구역에서 $H \rightarrow 0$ 발생 시, Kalman Gain $K$가 0에 수렴하여 측정값 보정이 불가능해지는 메커니즘을 이해하고 있는가?
2. **Noise Trade-off**: $Q$(System Noise) 설정값 상향 시, 추정 속도는 빨라지나 센서 노이즈에 대한 민감도(Sensitivity)가 급증하는 트레이드오프 관계를 파악했는가?
3. **Dual-EKF Strategy**: SOH 추정을 위한 파라미터 필터와 SOC 추정을 위한 상태 필터 간의 시정수(Time Constant) 분리 설계가 물리적 노화 속도와 일치하는가?

**[V7.5.2_Fidelity_Verified_by_Antigravity_Architect]**
**[TIMESTAMP: 2026-05-14]**
