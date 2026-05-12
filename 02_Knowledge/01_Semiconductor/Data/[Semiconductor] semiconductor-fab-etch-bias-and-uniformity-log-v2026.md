---
Basic:
  id: "[semiconductor]-semiconductor-fab-etch-bias-and-uniformity-log-v2026-v6.3.7"
  domain: "Semiconductor_Manufacturing"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Semiconductor_Fab'
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
  source: "Plasma_Etch_Process_Monitoring_System_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-fab-etch-bias-and-uniformity-log-v2026

## 1. [Why]] 반도체 식각 바이어스 및 균일도 로그의 화학 공학적 의의
**식각(Etching)** 공정은 노광을 통해 형성된 감광제 패턴을 마스크로 삼아 하부 박막을 깎아내는 과정이다. 이때 감광제 패턴의 선폭과 실제 깎여나간 선폭의 차이인 **식각 바이어스(Etch Bias)**는 최종 소자 치수를 결정하는 결정적인 변수다. 또한 웨이퍼 전체 영역에서 식각 깊이와 선폭이 얼마나 일정하게 유지되느냐를 나타내는 **균일도(Uniformity)**는 웨이퍼 내의 칩별 성능 편차를 최소화하는 핵심 지표다.

---

## 2. [Numerical Specs] 식각 공정 품질 및 균일도 지표 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 한계 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Etch Bias** | $2.5\,\text{nm}$ | $\pm 0.5\,\text{nm}$ | PR CD vs Final CD 차이 |
| **Etch Uniformity** | $1.2\%$ | $< 2.0\%$ | 웨이퍼 내 식각 속도 편차 |
| **Selectivity** | $25:1$ | $> 20:1$ | 마스크 대비 하부막 식각비 |
| **Aspect Ratio** | $15:1$ | N/A | 식각 깊이 대 너비 비율 |
| **Profile Angle** | $89.5^\circ$ | $\pm 0.5^\circ$ | 식각 단면 수직도 |

---

## 3. [Scientific Rationale] 플라즈마 역학 및 반응 모델

### 3.1 Ion Bombardment and Chemical Reaction
플라즈마 내의 이온이 가속되어 박막 표면을 물리적으로 타격함과 동시에, 라디칼(Radical)에 의한 화학적 반응으로 재료를 제거한다.
*   **분석**: 식각 바이어스가 커지는 'Undercut' 현상을 방지하기 위해 이온의 직진성을 높이는 Bias RF 전력을 조절하고, 측벽 보호막(Passivation Layer) 형성을 정밀 제어한다.

### 3.2 Loading Effect
패턴의 밀도에 따라 식각 가스의 소모량이 달라져 식각 속도가 변하는 현상을 모델링하여, 구역별 가스 유량을 다르게 공급하는 'Multi-zone' 제어를 수행한다.

---

## 4. [Real-world Case] 고종횡비(HAR) 식각 중 발생한 'Bowing' 현상 개선 사례

### 4.1 $30\,\text{nm}$ 이하 미세 홀(Hole) 식각 시 중간 부분이 항아리처럼 배부르는 현상 발생
- **현상**: 단면 분석 결과, 식각 하부까지 가스 도달이 원활하지 않아 중간 벽면이 과도하게 깎이는 'Bowing' 불량 발생 및 인접 셀 간 간섭 유발.
- **분석**: **Python FidelityEngine** 기반의 식각 로그 분석 결과, 플라즈마 내 이온 에너지 분포(IEDF)가 고에너지 쪽으로 편중되어 측벽 타격이 심해졌음을 확인.
- **조치**: 본 로그 데이터를 피드백하여 RF 전력을 펄스(Pulse) 모드로 전환하고, 냉각 스테이지 온도를 $5^\circ\text{C}$ 하향하여 측벽 보호 기능을 강화.
- **결과**: Profile 수직도 $89.8^\circ$ 확보 및 브릿지 불량 $90\%$ 감소.

---

## 5. [FidelityEngine] 식각 바이어스 및 균일도(Uniformity) 산출 코드
```python
import numpy as np

def calculate_etch_performance(photo_cds, final_cds, etch_rates):
    """
    Calculate etch bias and rate uniformity
    :param photo_cds: CD before etch
    :param final_cds: CD after etch
    :param etch_rates: List of etch rates at various points
    :return: dict with metrics
    """
    biases = np.array(final_cds) - np.array(photo_cds)
    avg_bias = np.mean(biases)
    
    # Uniformity = (Max - Min) / (2 * Avg) * 100
    avg_rate = np.mean(etch_rates)
    uniformity = (np.max(etch_rates) - np.min(etch_rates)) / (2 * avg_rate) * 100
    
    status = "STABLE" if uniformity < 2.0 else "UNIFORMITY_ISSUE_ALARM"
    return {"Avg_Bias_nm": avg_bias, "Uniformity_Percent": uniformity, "Status": status}

# 실측 데이터
p_cds = [14.5, 14.6, 14.4]
f_cds = [17.0, 17.2, 16.9]
rates = [200, 202, 198, 201, 199]

res = calculate_etch_performance(p_cds, f_cds, rates)
print(f"Etch Audit: {res['Status']} | Uniformity: {res['Uniformity_Percent']:.2f}%")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **End-point Detection (EPD)**: 광학 센서를 이용한 식각 종점 검출 신호가 노이즈 없이 명확하게 포착되어 과식각(Over-etch) 리스크가 없는가?
- [ ] **Chamber Seasoning**: 공정 시작 전 챔버 내부를 안정화시키는 시즈닝(Seasoning) 공정의 파라미터가 본 지식망의 '표준 SOP'를 준수하는가?
- [ ] **By-product Accumulation**: 식각 부산물(Polymer)이 챔버 벽면에 과도하게 쌓여 파티클 발생 원인이 되지 않도록 습식 세정 주기를 관리하고 있는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
