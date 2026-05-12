---
Basic:
  id: "SF-MFG-INJ-HW-2026-V6.3.7"
  domain: "Injection_Molding_Hardware"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#InjectionMolding", "#Hardware", "#Screw", "#ClampingUnit", "#MTC", "#Hydraulics", "#FidelityEngine"]'
  is_part_of: '["MOC 09_SmartFactory_Production", "Injection-Molding"]'
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
  source: "SmartFactory_Hardware_RAG_V6.3.7_Deterministic_Fabric"
  isolation_index: 0.0
---

# [Manual] injection-molding-machine-hardware-architecture

## 1. [왜 배우는가? (Why: The Mechanical Source of Quality)]
사출 성형 품질의 $70\%$ 이상은 설비의 **[물리적 상태(Hardware Integrity)]**에 의해 결정됩니다. 아무리 정교한 AI 제어 알고리즘을 적용해도, 스크류의 마모로 인한 역류(Back-flow)나 금형 체결부의 평행도(Parallelism) 불량은 수복 불가능한 치명적 결함을 야기합니다. 사출기 하드웨어를 이해하는 것은 공정 최적화를 넘어 **'예지 보전(Predictive Maintenance)'**의 근간이 됩니다.

## 2. [사출기 주요 하드웨어 계층 및 사양]

| Unit | Component | Function | Technical Spec (Target) |
|:---|:---|:---|:---|
| **Injection Unit**| Screw & Barrel | 수지 용융 및 압출 | L/D Ratio: $20:1 \text{ to } 22:1$ |
| **Injection Unit**| Check Ring | 용융 수지 역류 방지 | Clearance: $< 0.05 \text{ mm}$ |
| **Clamping Unit** | Toggle/Hydraulic | 금형 체결 및 유지 | Clamping Force: $50 \text{ to } 3000 \text{ tons}$ |
| **Clamping Unit** | Tie-bar | 형반 가이드 및 하중 지지 | Strain Gauge Accuracy: $\pm 1\%$ |
| **Auxiliary Unit** | MTC (온조기) | 금형 온도 정밀 제어 | Temp Stability: $\pm 0.5^\circ\text{C}$ |
| **Control Unit** | Servo System | 유압/전기 동력 제어 | Response Time: $< 10 \text{ ms}$ |

### 2.1 [스크류(Screw) 가소화 메커니즘]
*   **Feed Zone**: 고체 펠릿 이송.
*   **Compression Zone**: 압축 및 용융 (전단 응력 발생).
*   **Metering Zone**: 정량 토출 준비.
*   **추론 로직**: 스크류 회전 토크(Torque)가 비정상적으로 높을 경우, FidelityEngine은 **'수지 점도 과다'** 혹은 **'히터 밴드 결함'**으로 진단합니다.

## 3. [공학적 근거: Mechanical & Thermal Physics]

### 3.1 Clamping Force (형체력) 계산 수식
사출 시 금형이 벌어지지 않기 위해 필요한 최소 형체력($F$) 모델입니다.
$$ F = P \cdot A \cdot S $$
($P$: 사출 압력, $A$: 투영 면적, $S$: 안전 계수 $1.1\text{~}1.2$)
*   **진단 결과**: 실측된 타이바(Tie-bar) 신장량이 계산값보다 낮을 경우, FidelityEngine은 **'형체력 부족으로 인한 플래시(Flash) 발생 위험'**을 경고합니다.

### 3.2 Heat Transfer in Mold (냉각 물리)
금형 내부의 냉각 효율과 사이클 타임의 관계입니다.
$$ t_c \propto \frac{d^2}{\alpha \cdot \ln(\frac{T_m - T_c}{T_e - T_c})} $$
*   **추론 로직**: MTC의 냉각수 유량이 감소할 경우, FidelityEngine은 **'냉각 라인 스케일(Scale) 침착'**을 의심하며 수치적 시뮬레이션을 통해 예상 사이클 타임 지연을 산출합니다.

## 4. [코드 연결 해설: Machine Integrity Monitor]
이 코드는 사출기의 유압 응답성 및 스크류 마모 상태를 물리 로그 기반으로 오딧합니다.

```python
import numpy as np

def audit_machine_health(target_pressure, measured_pressure_log, screw_pos_log):
    """
    사출기 하드웨어 무결성 및 마모 진단
    """
    # 1. 유압 응답성 오딧 (Step Response)
    response_time = np.where(measured_pressure_log >= target_pressure * 0.95)[0][0]
    
    # 2. 스크류 역류 진단 (Check Ring Integrity)
    # 보압 단계에서 스크류 위치 변화율 분석
    holding_drift = np.gradient(screw_pos_log)[-10:].mean()
    
    status = "OPTIMAL"
    if response_time > 15: # 15ms 초과 시
        status = "HYDRAULIC_VALVE_DEGRADATION"
    elif holding_drift > 0.1: # 보압 중 스크류 밀림 발생 시
        status = "CHECK_RING_WEAR_DETECTED"
        
    return {
        "response_ms": response_time,
        "screw_stability": 1.0 - holding_drift,
        "diagnostic": status
    }
```

## 5. [스스로 체크 (Self-Audit)]
1. **Injection Layer**: 체크 링(Check Ring)의 마모가 사출 제품의 **'중량 편차(Weight Variation)'**에 미치는 수리적 임팩트는?
2. **Clamping Layer**: 전동식(Electric) 사출기가 유압식 대비 **'반복 정밀도'** 측면에서 우월한 기계적 근거는?
3. **MTC Layer**: 금형 온조기(MTC)의 냉각 용량이 부족할 때 발생하는 **'싱크마크(Sink Mark)'**의 물리적 원인은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 09_SmartFactory_Production
- Injection-Molding
- Injection-Process-Control
- Screw-Barrel
- Clamping-Unit

**[V6.3.7_INJECTION_HARDWARE_INFRASTRUCTURE_SYNC_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-11]**
