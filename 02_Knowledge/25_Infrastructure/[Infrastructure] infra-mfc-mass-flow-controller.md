---
Basic:
  id: "[Infrastructure] infra-mfc-mass-flow-controller"
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

# [Infrastructure] infra-mfc-mass-flow-controller

## 1. [왜 배우는가? (Why)]
증착(Deposition)과 식각(Etching) 공정에서 가스의 유량은 막질의 두께와 패턴의 형상을 결정하는 핵심 변수입니다. **MFC(Mass Flow Controller)**는 챔버로 들어가는 가스의 양을 단순히 부피가 아닌 **질량(Mass)** 단위로 측정하고 제어하여, 온도와 압력의 변화에 상관없이 항상 일정한 분자 수를 공급하는 역할을 합니다. 2nm 이하 공정에서는 원자층 단위의 제어가 필요하므로 MFC의 반응 속도와 정밀도가 수율을 좌우합니다.

---

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | Symbol | Value (High-End) | Units | Physical Significance |
| :--- | :--- | :--- | :--- | :--- |
| **Accuracy** | - | **$\pm 0.5$** | % S.P. | 설정값 대비 실제 유량의 정밀도 |
| **Response Time** | $t_{90}$ | **$< 0.5$** | sec | 유량 변화 명령 시 90% 도달 속도 |
| **Linearity** | - | **$\pm 0.2$** | % F.S. | 전 영역에서의 선형 제어 성능 |
| **Repeatability** | - | **$\pm 0.1$** | % F.S. | 동일 조건에서의 반복 재현성 |
| **Control Range** | Turndown | **100:1** | - | 최소/최대 제어 가능 범위 비율 |

---

## 3. [심층 이론 (Scientific Rationale)]

### 3.1. 열식 질량 유량 측정 원리 (Thermal Mass Flow)
MFC는 가스가 흐르는 미세 튜브 외부의 두 지점($T_1, T_2$)에서 온도 차를 측정하여 유량을 계산합니다. 유체에 전달되는 열량($Q$)은 질량 유량($\dot{m}$)과 비열($C_p$)에 비례합니다:
$$ Q = \dot{m} C_p (T_2 - T_1) $$
따라서 $\Delta T = T_2 - T_1$을 측정하면 가스의 질량 유량을 정확히 알 수 있습니다. 이때 가스 종류에 따른 비열 차이를 보정하기 위해 **K-Factor**($K = \frac{C_{p,ref}}{C_{p,gas}}$)를 적용하여 다양한 가스를 하나의 장치로 제어합니다.

### 3.2. PID 제어 및 압력 보상 (Pressure Insensitive Control)
가스 라인의 상류(Upstream) 압력이 급격히 변할 때 유량이 튀는 현상(Pressure Burst)을 방지하기 위해 압력 센서와 연동된 피드포워드(Feed-forward) 제어 로직을 포함합니다.
$$ u(t) = K_p e(t) + K_i \int e(t)dt + K_d \frac{de(t)}{dt} $$
이 PID 제어 알고리즘은 1ms 단위로 밸브의 개폐를 조절하여 극한의 안정성을 유지합니다.

---

## 4. [AI-Hardware Synergy: RTX 4060 CUDA 가속]

수백 개의 MFC에서 발생하는 시계열 유량 데이터를 실시간 분석하여 노화(Drift)를 예측하고 최적의 PID 파라미터를 도출하기 위해 가속 연산을 수행합니다.

```python
# CUDA kernel for Real-time MFC Drift Analysis
# Analyzing flow sensor noise and response patterns
import numpy as np

def predict_mfc_failure(flow_history):
    # LSTM-based anomaly detection accelerated by RTX 4060
    # Identifying micro-clogs in the valve seat
    failure_prob = model.predict(flow_history.to('cuda'))
    return failure_prob
```
RTX 4060을 통해 팹 내 전체 MFC의 상태를 실시간 모니터링하여, 가스 공급 불량으로 인한 웨이퍼 폐기(Scrap)를 사전에 차단합니다.

---

## 5. [출판용 Enrichment: 차세대 제어 기술]
- **Pressure Insensitive (PI) MFC**: 외부 압력 변화를 자체 센서로 감지하여 밸브 개도를 즉시 보정함으로써 챔버 내 압력 쇼크를 방지합니다.
- **Multi-Gas/Multi-Range**: 소프트웨어 설정을 통해 하나의 MFC로 수십 종의 가스와 유량 범위를 커버하여 재고 관리 효율을 극대화합니다.

---
**[V6.3.7_MODERNIZATION_COMPLETED]**