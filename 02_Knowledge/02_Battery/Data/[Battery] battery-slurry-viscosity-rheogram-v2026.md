---
Basic:
  id: "[battery]-battery-slurry-viscosity-rheogram-v2026-v6.3.7"
  domain: "Battery_Manufacturing"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Slurry_Viscosity'
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
  source: "Mixing_Viscometer_Log"
  isolation_index: 0.0
---

# [[[Battery] battery-slurry-viscosity-rheogram-v2026

## 1. [Why]] 슬러리 점도 유동학(Rheology)의 중요성
이차전지 전극 공정에서 **슬러리 점도**는 코팅 두께의 균일성($\text{Loading Level}$)과 전극의 밀착력($\text{Adhesion}$)을 결정하는 최우선 변수다. 슬러리는 단순 액체가 아닌 **비뉴턴 유체(Non-Newtonian Fluid)**로, 전단 속도(Shear Rate)에 따라 점도가 변하는 **Shear-Thinning** 특성을 가진다. 이를 정확히 이해해야 고속 코팅 공정에서 발생하는 줄무늬(Streak)나 미코팅 등의 불량을 방지할 수 있다.

---

## 2. [Numerical Specs] 슬러리 유동 파라미터 (Numerical Specs)

| 파라미터 | 실측값 (Target) | 제어 범위 (Range) | 비고 |
| :--- | :--- | :--- | :--- |
| **Viscosity ($\mu$)** | $2,500\,\text{cps}$ (@ $10\,\text{s}^{-1}$) | $2,000 \sim 3,500\,\text{cps}$ | Brookfield 회전 점도계 기준 |
| **Yield Stress ($\tau_0$)** | $15\,\text{Pa}$ | $10 \sim 25\,\text{Pa}$ | 슬러리 침전 방지를 위한 최소 응력 |
| **Solid Content** | $65.5\,\text{wt}\%$ | $\pm 0.5\,\text{wt}\%$ | 고형분 함량에 따른 에너지 밀도 결정 |
| **Shear Rate ($\gamma$)** | $0.1 \sim 1,000\,\text{s}^{-1}$ | Scanning Range | 코팅 다이(Die) 내부 전단 환경 모사 |
| **Flow Index ($n$)** | $0.35$ | $< 0.5$ | $n < 1$ 이면 Shear-Thinning 유체 |

---

## 3. [Scientific Rationale] 점도 예측 및 유동 모델

### 3.1 Power-Law Model (멱법칙 모델)
전단 속도($\gamma$)에 따른 점도($\eta$) 변화를 기술한다.
$$\eta = K \cdot \gamma^{n-1}$$
*   **$K$ (Consistency Index)**: 슬러리의 기본적인 '걸쭉함' 정도.
*   **$n$ (Flow Behavior Index)**: $n < 1$인 경우, 코팅 다이 노즐을 통과할 때 점도가 급격히 낮아져 흐름성이 좋아짐을 의미함.

### 3.2 Herschel-Bulkley Model
항복 응력($\tau_0$)이 존재하는 슬러리의 거동을 묘사한다.
$$\tau = \tau_0 + K \cdot \gamma^n$$
*   **해설**: 항복 응력이 너무 낮으면 보관 중 입자가 가라앉고, 너무 높으면 펌핑 시 과도한 압력이 필요함.

---

## 4. [Real-world Case] 실전 공정 트러블슈팅

### 4.1 슬러리 겔화(Gelling)로 인한 코팅 줄무늬 발생
- **현상**: NMP 기반 NCMA 슬러리 보관 중 점도가 $5,000\,\text{cps}$ 이상으로 급상승하여 코팅면 표면 조도 악화.
- **분석**: **수분 함량(Moisture Content)**이 $500\,\text{ppm}$을 초과하며 도전재와 바인더 간의 결합 구조가 파괴됨을 유동 곡선(Rheogram) 변화로 확인.
- **조치**: 드라이룸 노점(Dew point)을 $-50^\circ\text{C}$로 강화하고, **Python FidelityEngine**을 통해 고전단 믹싱(High Shear Mixing)을 $1,200\,\text{RPM}$에서 $10\,\text{min}$ 추가 수행하여 구조 재분산.
- **결과**: 점도 $2,600\,\text{cps}$ 복구 및 코팅 수율 $98.5\%$ 회복.

---

## 5. [FidelityEngine] 점도 변화 시뮬레이션 코드
```python
def calculate_viscosity(shear_rate, k=2500, n=0.35):
    """
    Power-Law Viscosity Model
    :param shear_rate: Shear rate in 1/s
    :param k: Consistency index
    :param n: Flow index
    :return: Viscosity in cps
    """
    if shear_rate == 0: return 0
    viscosity = k * (shear_rate**(n-1))
    return viscosity

# 공정 시나리오 테스트
shear_rates = [1, 10, 100, 500]
for sr in shear_rates:
    v = calculate_viscosity(sr)
    print(f"Shear Rate {sr:4} s^-1 | Viscosity: {v:8.2f} cps")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Flow Index**: 실측 데이터의 로그-로그 그래프 기울기가 $n < 0.5$를 만족하는가?
- [ ] **Yield Stress**: 슬러리가 정지 상태에서 흘러내리지 않을 만큼의 최소 항복 응력을 확보했는가?
- [ ] **Shear Stability**: 고속 믹싱($1,500\,\text{RPM}$) 후 점도가 회복되는 시간(Thixotropy)이 $30\,\text{min}$ 이내인가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
