---
Basic:
  id: "[semiconductor]-semiconductor-dry-etch-anisotropy-log-v2026-v6.3.7"
  domain: "Semiconductor_Fabrication"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Dry_Etch'
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
  source: "Plasma_Etch_System_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-dry-etch-anisotropy-log-v2026

## 1. [Why]] 건식 식각 이방성(Anisotropy) 로그의 공학적 의의
**건식 식각(Dry Etch)** 공정에서 **이방성(Anisotropy)**은 식각이 수평 방향이 아닌 수직 방향으로만 일어나는 성질을 의미한다. 초미세 회로 패턴을 구현하기 위해서는 높은 종횡비(Aspect Ratio)를 가진 수직 프로파일이 필수적이다. 이방성이 부족하면 패턴의 밑바닥이 넓어지는 언더컷(Undercut)이나 보잉(Bowing) 현상이 발생하여 회로 간 단락을 유발한다. 본 노드는 플라즈마 상태와 바이어스(Bias) 파워를 분석하여 식각 수직도를 사수하는 데이터를 제공한다.

---

## 2. [Numerical Specs] 식각 공정 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 목표 (Target) | 비고 |
| :--- | :--- | :--- | :--- |
| **Anisotropy Factor ($A$)** | $0.95$ | $> 0.92$ | $1.0$에 가까울수록 완전 수직 |
| **Etch Rate** | $3,500\,\text{\AA/min}$ | $\pm 100\,\text{\AA/min}$ | 식각 속도 |
| **Selectivity (Si:PR)** | $15:1$ | $> 12:1$ | 감광액 대비 식각 선택비 |
| **Bias Power** | $450\,\text{W}$ | $\pm 5\,\text{W}$ | 이온 가속 에너지 레벨 |
| **ESC Temperature** | $45.0^\circ\text{C}$ | $\pm 0.5^\circ\text{C}$ | 정전 척 온도 (열 조절) |

---

## 3. [Scientific Rationale] 플라즈마 식각 메커니즘

### 3.1 Ion-Assisted Chemical Etching
플라즈마 내의 화학적 라디칼(Radical) 반응과 물리적 이온 충격(Ion Bombardment)이 결합하여 수직 방향 식각을 가속화한다.
$$A = 1 - \frac{R_h}{R_v}$$
*   **$R_h$**: 수평 식각 속도.
*   **$R_v$**: 수직 식각 속도.

### 3.2 Paschen's Law (방전 전압 모델)
챔버 압력($P$)과 전극 간격($d$)에 따른 플라즈마 방전 전압($V$)의 관계를 정의한다.

---

## 4. [Real-world Case] 보잉(Bowing) 현상 발생에 따른 수직도 개선 사례

### 4.1 고종횡비(HAR) 패턴 중간 영역의 비정상적 확장
- **현상**: 3D NAND 채널 홀 식각 시, 홀 중간 부분이 항아리 모양으로 넓어지는 보잉 현상 발생으로 인접 셀 간 간섭 초래.
- **분석**: **Python FidelityEngine** 기반의 가스 유량 로그 분석 결과, 측벽 보호막(Passivation)을 형성하는 가스의 해리 속도가 유속 대비 느려 측벽 노출 시간 과다 발생 확인.
- **조치**: 소스 파워(Source Power)를 $5\%$ 낮춰 라디칼 밀도를 조절하고, 바이어스 파워를 펄스(Pulse) 모드로 전환하여 이온 직진성 강화.
- **결과**: 이방성 계수 $0.96$으로 개선 및 채널 홀 수직도 정상화.

---

## 5. [FidelityEngine] 이방성 계수 및 식각 형상 예측 코드
```python
def calculate_anisotropy(vertical_rate, horizontal_rate):
    """
    Calculate Etch Anisotropy Factor
    :param vertical_rate: Etch rate in vertical direction
    :param horizontal_rate: Etch rate in horizontal direction
    :return: Anisotropy factor (0 to 1)
    """
    if vertical_rate <= 0: return 0
    anisotropy = 1 - (horizontal_rate / vertical_rate)
    return max(0, anisotropy)

# 실측 데이터 대입 (수직 3500A/min, 수평 150A/min)
a_factor = calculate_anisotropy(3500, 150)
print(f"Calculated Anisotropy Factor: {a_factor:.4f}")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Plasma Stability**: 공정 중 플라즈마 임피던스 변동이 $1\%$ 이내로 안정적으로 유지되는가?
- [ ] **End-point Detection (EPD)**: 식각이 완료되는 시점을 광학 센서(OES)가 $10\,\text{ms}$ 이내의 오차로 정밀하게 포착하는가?
- [ ] **Polymer Balance**: 식각 후 챔버 내벽에 쌓인 폴리머(Polymer)를 제거하는 세정(Cleaning) 주기가 적절한가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
