---
Basic:
  id: "[data]-display-roll-to-roll-flexible-electronics-alignment-accuracy-log-v2026-v6.3.7"
  domain: "Display_Manufacturing"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Data"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Roll-to-Roll'
  is_part_of: - 'Antigravity_Knowledge_Graph'
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
  source: "R2R_Web_Alignment_Sensor_Log"
  isolation_index: 0.0
---

# [[[Data] display-roll-to-roll-flexible-electronics-alignment-accuracy-log-v2026

## 1. [Why]] 롤투롤(R2R) 정렬 정밀도 로그의 기계 시스템적 의의
**롤투롤(Roll-to-Roll, R2R)** 공정은 유연 기판(Flexible Substrate) 위에 디스플레이나 전자 회로를 대량으로 인쇄하거나 증착하는 기술이다. 기판이 롤 사이를 이동하며 연신(Stretching)되거나 사행(Meandering)하기 때문에, 여러 공정을 거칠 때 패턴 간의 정렬(Register)을 맞추는 것이 극도로 어렵다. **정렬 정밀도 로그**는 웹(Web)의 이동 속도, 장력, 좌우 편차 데이터를 실시간 기록하여, $10\,\mu\text{m}$ 이하의 초정밀 적층 품질을 구현하는 근거를 제공한다.

---

## 2. [Numerical Specs] R2R 웹 핸들링 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 허용 오차 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Lateral Alignment** | $\pm 8\,\mu\text{m}$ | $<\pm 15\,\mu\text{m}$ | 좌우 사행 오차 |
| **Machine Direction (MD)**| $\pm 5\,\mu\text{m}$ | $<\pm 10\,\mu\text{m}$ | 흐름 방향 정렬 오차 |
| **Web Tension** | $80\,\text{N}$ | $\pm 5\,\text{N}$ | 기재 연신 제어 장력 |
| **Line Speed** | $20\,\text{m/min}$ | Max $50\,\text{m/min}$ | 생산 가동 속도 |
| **Web Width** | $500\,\text{mm}$ | $\pm 0.1\,\text{mm}$ | 기재 폭 변화량 (수축/팽창) |

---

## 3. [Scientific Rationale] 웹 역학 및 정렬 제어 모델

### 3.1 Web Dynamics and Meandering
웹이 롤러를 통과할 때 발생하는 횡방향 거동을 모델링한다.
*   **분석**: 롤러의 평행도 오차나 장력 불균형은 웹의 비틀림(Wrinkle)을 유발하고 정렬 정밀도를 파괴한다.

### 3.2 Register Control Strategy
사전에 인쇄된 마크(Register Mark)를 비전 센서로 감지하여, 다음 공정의 롤러 속도나 위치를 미세 조정하는 피드백 제어 알고리즘을 적용한다.

---

## 4. [Real-world Case] 열 건조 공정 후 기판 수축에 의한 정렬 불량 해결 사례

### 4.1 다층 인쇄 회로 적층 중 상하 패턴 어긋남 현상 포착
- **현상**: 유연 디스플레이용 TFT 인쇄 공정 중, 건조로(Oven)를 통과한 후 두 번째 패턴 적층 시 MD 방향으로 $50\,\mu\text{m}$ 이상의 오차 발생.
- **분석**: **Python FidelityEngine** 기반의 장력-연신 상관성 분석 결과, 고온 건조 과정에서 PET 기판이 $0.02\%$ 열 수축했음을 확인.
- **조치**: 건조 후 냉각 롤러(Chill Roll) 구간의 장력을 미세하게 높여 기판을 인위적으로 늘려(Compensate) 수축분을 상쇄하는 'Pre-stretch' 로직 적용.
- **결과**: 적층 정렬 오차 $10\,\mu\text{m}$ 이내로 복구 및 불량률 제로화.

---

## 5. [FidelityEngine] 웹 사행(Meandering) 및 보정 시뮬레이션 코드
```python
import numpy as np

def simulate_web_alignment(time_steps, noise_level, correction_gain):
    """
    Simulate web lateral alignment and active correction
    :return: List of residual errors
    """
    current_pos = 0
    errors = []
    
    for _ in range(time_steps):
        # Random wandering (Disturbance)
        drift = np.random.normal(0, noise_level)
        current_pos += drift
        
        # Active correction (Feedback)
        correction = -current_pos * correction_gain
        current_pos += correction
        
        errors.append(current_pos)
        
    return errors

# 시뮬레이션: 100단계, 소음 2um, 게인 0.8
residual_errors = simulate_web_alignment(100, 2.0, 0.8)
avg_residue = np.mean(np.abs(residual_errors))

print(f"Average Residual Alignment Error: {avg_residue:.3f} um")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Sensor Cleaning**: 웹의 위치를 읽는 초음파/광학 센서 렌즈에 분진이나 잉크가 튀어 측정 오류를 유발하지 않는가?
- [ ] **Roller Parallelism**: 모든 롤러의 수평/평행도가 $0.01\,\text{mm/m}$ 이내로 켈리브레이션되어 있는가?
- [ ] **Tension Profile**: 웹의 가감속 구간에서 장력 변화가 설정 임계치($\pm 5\%$) 내에서 안정적으로 유지되는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
