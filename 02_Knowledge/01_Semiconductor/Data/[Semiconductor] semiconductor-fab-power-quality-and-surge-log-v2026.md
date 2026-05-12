---
Basic:
  id: "[semiconductor]-semiconductor-fab-power-quality-and-surge-log-v2026-v6.3.7"
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
  source: "Fab_Electrical_Substation_and_UPS_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-fab-power-quality-and-surge-log-v2026

## 1. [Why]] 반도체 팹 전력 품질 및 서지 로그의 시스템 안정성 의의
반도체 생산 장비는 전력 품질에 극도로 민감하다. 밀리초(ms) 단위의 짧은 전압 하락(Voltage Sag)이나 서지(Surge)조차도 노광기(Stepper)의 위상 제어를 뒤흔들거나 로봇 팔의 오동작을 유발하여 수천억 원 상당의 웨이퍼 손실을 야기할 수 있다. **전력 품질 및 서지 로그**는 전압, 주류, 고조파 왜곡률(THD)을 실시간 기록하여, 전력망의 건강 상태를 감시하고 UPS(무정전 전원 장치)의 가동 시점을 최적화하여 팹의 가용성을 극대화한다.

---

## 2. [Numerical Specs] 전력 품질 및 안전 지표 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 한계 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Voltage Stability** | $22,900\,\text{V}$ | $\pm 5\%$ | 인입 전압 변동 허용치 |
| **Voltage Sag (ITIC)** | $0.5\,\text{cycle}$ | $< 0.1\,\text{sec}$ | 장비 정지 유발 하한선 |
| **Total Harmonic (THD)**| $2.5\%$ | $< 5.0\%$ | 전력 고조파 왜곡 |
| **UPS Switch Time** | $0\,\text{ms}$ | $< 2\,\text{ms}$ | 전력 전환 소요 시간 (Static) |
| **Surge Counter** | $0\,\text{events}$ | N/A | 누적 서지 발생 횟수 |

---

## 3. [Scientific Rationale] 전력망 안정성 및 왜곡 모델

### 3.1 ITIC (CBEMA) Curve Analysis
전압 변동의 크기와 지속 시간을 분석하여, 산업용 장비가 고장 없이 견딜 수 있는 영역(Safe Zone)에 있는지 판별한다.
*   **분석**: 순간적인 전압 강하가 발생하더라도 UPS의 에너지가 보충될 수 있는 시간 동안만 지속된다면 생산 공정은 멈추지 않고 유지된다.

### 3.2 Total Harmonic Distortion (THD)
비선형 부하(인버터, 정류기 등)에 의해 발생하는 전류 파형의 왜곡 정도를 계산하여 변압기 가열이나 통신 장애를 사전에 경고한다.

---

## 4. [Real-world Case] 낙뢰에 의한 순간 전압 강하 시 UPS 무중단 대응 사례

### 4.1 인근 변전소 낙뢰 발생으로 인한 팹 인입 전압 $30\%$ 순간 하락
- **현상**: 외부 전력망의 전압이 $0.05$초간 $20\%$ 이상 강하하는 'Sag' 현상 발생. 팹 내부의 수천 대 설비가 정지 위기에 처함.
- **분석**: **Python FidelityEngine** 기반의 전력 로그 분석 결과, STS(Static Transfer Switch)가 $1\,\text{ms}$ 내에 응답하여 UPS 배터리 전원으로 즉시 전환했음을 확인.
- **조치**: 외부 전력망 복구 후 위상 동기화(Sync) 과정을 거쳐 다시 한전 전원으로 안정적으로 복귀.
- **결과**: 생산 중인 웨이퍼 $10,000$매 손실 방지 및 가동률 $100\%$ 유지.

---

## 5. [FidelityEngine] 전압 강하(Voltage Sag) 위험도 분석 코드
```python
def analyze_voltage_sag(remaining_voltage_percent, duration_ms):
    """
    Classify voltage sag according to SEMI F47 / ITIC standards
    :param remaining_voltage_percent: Percentage of normal voltage remaining
    :param duration_ms: Duration of the sag event
    :return: dict with risk classification
    """
    if remaining_voltage_percent < 50 and duration_ms > 20:
        risk = "CRITICAL_EQUIPMENT_TRIP_EXPECTED"
    elif remaining_voltage_percent < 70 and duration_ms > 200:
        risk = "MODERATE_INTERRUPT_RISK"
    else:
        risk = "SAFE_WITHIN_STANDARDS"
        
    return {"Voltage_Level": remaining_voltage_percent, "Duration": duration_ms, "Risk": risk}

# 실측 데이터: 60% 전압 유지, 100ms 지속
res = analyze_voltage_sag(60, 100)
print(f"Power Event Class: {res['Risk']} (Level: {res['Voltage_Level']}%, Duration: {res['Duration']}ms)")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **UPS Battery Health**: UPS 배터리의 기대 수명과 실제 방전 테스트(Load Bank Test) 결과가 최신화되어 있는가?
- [ ] **Surge Arrester**: 팹 외부 노출 구간에 서지 보호 장치(SPD)가 정상 설치되어 있으며, 서지 카운터가 동작 중인가?
- [ ] **Grounding Impedance**: 공장 접지 시스템의 저항값이 규정치($< 1\,\Omega$)를 유지하여 대규모 서지 발생 시 에너지를 신속히 배출할 수 있는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
