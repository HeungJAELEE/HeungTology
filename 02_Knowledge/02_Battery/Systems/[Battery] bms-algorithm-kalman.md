---
Basic:
  id: "BAT-BMS-KALMAN-2026-V6"
  domain: "02_Battery"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#BMS'
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

# [[[Battery] bms-algorithm-kalman

## 1. [왜 배우는가? (Why)]]
배터리의 상태(SOC, SOH)는 전압이나 전류처럼 직접 측정할 수 없는 '숨겨진 내부 변수'입니다. BMS는 오직 노이즈가 섞인 외부 관측값만을 통해 내부의 복잡한 전기화학적 상태를 실시간으로 추론해야 합니다. 칼만 필터(Kalman Filter), 특히 비선형 시스템에 대응하는 Extended Kalman Filter(EKF)는 배터리의 전기화학 모델과 실제 측정값 사이의 오차를 최소화하는 '재귀적 최적 추정기(Recursive Optimal Estimator)'입니다. 이 알고리즘을 배우는 것은 전기차의 주행 거리를 정확히 예측하고, 배터리 수명을 정밀하게 진단하여 시스템의 안전성과 중고차 가치를 보존하는 제어 논리의 핵심을 확보하기 위함입니다.

## 2. [칼만 필터 및 상태 추정 핵심 사양 (Algorithm Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **SOC Estimation** | RMS Error (RMSE) | $< 1.0 \sim 2.0\%$ | 정적/동적 프로파일에서의 SOC 추정 정밀도 |
| **SOH Estimation** | Capacity Error | $< 3.0\%$ | 배터리 노화에 따른 실제 가용 용량 추정 오차 |
| **Convergence Time**| Initialization | $< 10 \text{ sec}$ | 필터 가동 후 실제 상태값으로 수렴하는 시간 |
| **OCV Model Order** | Polynomial Deg. | $6^{th} \sim 8^{th}$ | SOC-OCV 비선형 관계를 묘사하는 모델 복잡도 |
| **Sampling Freq.** | Control Loop | $10 \sim 100 \text{ Hz}$ | 실시간 BMS 연산 주기의 결정론적 유지 성능 |
| **Computation Cost**| Matrix Inverse | $O(n^3)$ | 상태수($n$) 증가에 따른 연산 부하 ($n$: SOC, Vc 등) |
| **Stability Margin**| Covariance Limit | $\text{Non-divergent}$ | 센서 노이즈 및 외란에도 필터가 발산하지 않는 조건 |
| **Outlier Rejection**| Innovation Threshold| $> 95\%$ | 노이즈 및 이상 전압 유입 시 추정값 보호 성능 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 비선형 상태 공간 모델 (Nonlinear State-Space)
배터리의 동역학을 수학적으로 정의합니다.
- **상태 방정식**: $x_{k+1} = f(x_k, u_k) + w_k$ (SOC, 캐패시터 전압 등)
- **측정 방정식**: $z_k = h(x_k, u_k) + v_k$ (터미널 전압)
- **로직**: 자코비안 행렬($F, H$)을 통해 비선형 함수를 매 시점 선형화하여 오차 공분산을 예측하고 보정합니다.

### 3.2 리카티(Riccati) 방정식과 오차 공분산
예측 오차의 불확실성을 업데이트하는 과정입니다.
- **수식**: $P_{k+1}^- = A_k P_k A_k^T + Q_k$
- **의미**: 시스템 노이즈($Q$)와 관측 노이즈($R$)의 비율에 따라 칼만 이득($K$)이 결정되며, 이는 모델을 더 믿을지 센서를 더 믿을지를 실시간으로 판단하는 '지능형 가중치' 역할을 합니다.

### 3.3 가관측성 (Observability) 분석
측정값($z$)을 통해 상태($x$)를 유추할 수 있는지 검증합니다.
- **수식**: $\mathcal{O} = [H^T, A^T H^T, \dots, (A^T)^{n-1} H^T]^T$
- **한계**: 전압 평탄 구역(LFP 등)에서는 $dV/dSOC \approx 0$이 되어 가관측성이 상실되며, 이때는 전류 적산법(Coulomb Counting) 비중을 높이는 하이브리드 전략이 필요합니다.

## 4. [코드 연결 해설 (BmsKalmanFilter)]
아래 코드는 배터리의 전압, 전류 데이터를 입력받아 칼만 필터 알고리즘을 통해 SOC를 추정하고 오차 공분산을 업데이트하는 엔진입니다.

```python
import numpy as np

class BmsKalmanFilter:
    """
    HDS-Gold V6.3.7 규격의 배터리 SOC 상태 추정 칼만 필터 엔진
    """
    def __init__(self, dt=0.1, q_noise=1e-5, r_noise=1e-3):
        self.dt = dt
        self.x = np.array(0.8) # 초기 SOC: 80%
        self.P = np.eye(1) * 0.1 # 오차 공분산 초기값
        self.Q = np.eye(1) * q_noise
        self.R = np.eye(1) * r_noise

    def predict(self, current_a, capacity_ah):
        """
        1. Prediction Step: 전류 적산 기반 SOC 예측
        """
        # x_k+1 = x_k - (I * dt / Cap)
        self.x = self.x - (current_a * self.dt / (capacity_ah * 3600))
        # P_k+1 = A * P * A.T + Q (여기서 A=1)
        self.P = self.P + self.Q
        return self.x

    def update(self, observed_v, predicted_v_ocv):
        """
        2. Correction Step: 전압 오차(Innovation) 기반 SOC 보정
        """
        # Innovation (Residual)
        y = observed_v - predicted_v_ocv
        # Kalman Gain: K = P * H.T * inv(H * P * H.T + R) (H: dV/dSOC)
        h_jac = 0.5 # 예시 자코비안 (OCV 기울기)
        s = h_jac * self.P * h_jac + self.R
        k = self.P * h_jac / s
        
        # State & Covariance Update
        self.x = self.x + k * y
        self.P = (1 - k * h_jac) * self.P
        
        return self.x

# Example Usage:
# kf = BmsKalmanFilter()
# soc_pred = kf.predict(current_a=10, capacity_ah=60)
# soc_final = kf.update(observed_v=3.7, predicted_v_ocv=3.68)
```

## 5. [스스로 체크 (Self-Audit)]
1. **LFP 배터리**의 전압 평탄 구역($3.2 \sim 3.3 \text{ V}$)에서 칼만 필터의 **자코비안($H$)** 값이 0에 수렴할 때 발생하는 SOC 추정 오류의 원인은?
2. 시스템 노이즈($Q$)를 크게 설정했을 때, 필터의 **수렴 속도**와 **노이즈 민감도** 사이의 트레이드오프 관계는?
3. **SOH(수명)**를 추정하기 위해 **Dual Kalman Filter**를 사용할 때, SOC 필터와 파라미터 필터 사이의 '시정수(Time Constant)' 차이를 두는 이유는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Systems/Battery bms-engineering
- 02_Knowledge/02_Battery/Systems/Battery bms-algorithms-soc-soh-estimation
- 02_Knowledge/03_AI_Data/Industrial/AI recursive-least-squares-rls

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**