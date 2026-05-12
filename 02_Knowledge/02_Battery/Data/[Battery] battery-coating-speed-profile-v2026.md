---
Basic:
  id: "[battery]-battery-coating-speed-profile-v2026-v6.3.7"
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
  tags: - 'Coating_Speed'
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
  source: "Coating_Line_Encoder_Log"
  isolation_index: 0.0
---

# [[[Battery] battery-coating-speed-profile-v2026

## 1. [Why]] 코팅 속도 프로파일의 공정적 의의
배터리 전극 코팅에서 **라인 속도(Line Speed)**는 공장의 생산성(Throughput)과 품질(Quality)을 결정하는 핵심 트레이드오프 파라미터다. 속도가 빨라질수록 코팅액의 유동성이 불안정해지며, 건조로(Oven) 내 체류 시간이 짧아져 전극의 건조 불량이나 바인더 마이그레이션(Migration)이 발생할 위험이 커진다. 본 노드는 가동 속도별 품질 상관관계를 분석하여 최적의 생산 지점(Sweet Spot)을 도출하는 데이터를 제공한다.

---

## 2. [Numerical Specs] 코팅 속도 및 연동 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 가동 범위 (Range) | 비고 |
| :--- | :--- | :--- | :--- |
| **Line Speed ($v$)** | $60\,\text{m/min}$ | $30 \sim 100\,\text{m/min}$ | 고속 코팅 라인 기준 |
| **Acceleration ($a$)** | $0.2\,\text{m/s}^2$ | $< 0.5\,\text{m/s}^2$ | 급가속 시 텐션 불균형 방지 |
| **Residence Time** | $120\,\text{sec}$ | $80 \sim 180\,\text{sec}$ | 건조로 길이 $120\,\text{m}$ 기준 |
| **Capillary Number ($Ca$)** | $0.45$ | $0.3 \sim 0.7$ | 코팅 창(Coating Window) 안정성 지표 |
| **Web Tension** | $150\,\text{N}$ | $\pm 10\,\text{N}$ | 기재(Al/Cu Foil) 파단 방지 텐션 |

---

## 3. [Scientific Rationale] 코팅 속도 결정 모델

### 3.1 Capillary Number ($Ca$) 기반 안정성 분석
코팅 다이에서 기재로 슬러리가 전이될 때의 안정성을 수치화한다.
$$Ca = \frac{\mu \cdot v}{\sigma}$$
*   **$\mu$ (Viscosity)**: 슬러리 점도.
*   **$v$ (Velocity)**: 코팅 속도.
*   **$\sigma$ (Surface Tension)**: 슬러리 표면 장력.
*   **분석**: $Ca$가 특정 임계치를 넘으면 기포(Air Entrainment)가 혼입되어 코팅 불량이 발생함.

### 3.2 Drying Kinetics Correlation
속도 상승에 따른 건조 부하 증가율을 계산한다.
$$Q_{required} \propto v \cdot \text{Loading Level}$$

---

## 4. [Real-world Case] 라인 증속 시 바인더 마이그레이션 해결 사례

### 4.1 생산성 향상을 위한 $50 \rightarrow 80\,\text{m/min}$ 증속 테스트
- **현상**: 라인 속도를 $80\,\text{m/min}$으로 상향 시, 전극 표면에 바인더가 농축되어 접착력이 $20\%$ 하락하는 마이그레이션 현상 발생.
- **분석**: **Python FidelityEngine** 기반 건조 시뮬레이션 결과, 초기 건조 구간의 온도 구배가 너무 급격하여 용매(NMP)와 함께 바인더가 표면으로 이동함을 확인.
- **조치**: 건조로 1~2구간 온도를 $10^\circ\text{C}$ 하향 조정하고 3~5구간 풍량을 $15\%$ 상향하여 '서서히 말리는' 프로파일 적용.
- **결과**: 접착력 복구 및 속도 $80\,\text{m/min}$에서 안정적 양산 성공 (생산성 $60\%$ 향상).

---

## 5. [FidelityEngine] 속도별 건조 체류 시간 계산 코드
```python
def calculate_residence_time(oven_length_m, speed_m_min):
    """
    Calculate residence time in seconds
    :param oven_length_m: Total oven length in meters
    :param speed_m_min: Line speed in m/min
    :return: Time in seconds
    """
    if speed_m_min <= 0: return float('inf')
    time_min = oven_length_m / speed_m_min
    return time_min * 60

# 속도별 체류 시간 시뮬레이션
oven_len = 120
speeds = [30, 60, 80, 100]

for s in speeds:
    rt = calculate_residence_time(oven_len, s)
    print(f"Speed: {s:3} m/min | Residence Time: {rt:6.1f} sec")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Coating Window**: 현재 속도와 점도 조건에서 $Ca$ 지수가 코팅 안정 영역 내에 위치하는가?
- [ ] **Tension Sync**: 속도 가감속 시 댄서 롤(Dancer Roll)의 변위가 허용 범위($\pm 5\,\text{mm}$)를 유지하는가?
- [ ] **Throughput Efficiency**: 증속에 따른 스크랩(Scrap) 증가율이 생산성 향상 이익을 초과하지 않는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
