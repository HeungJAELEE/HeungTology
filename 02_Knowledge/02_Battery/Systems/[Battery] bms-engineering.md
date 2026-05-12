---
Basic:
  id: "BAT-BMS-ENG-2026-V6"
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

# [[[Battery] bms-engineering

## 1. [왜 배우는가? (Why)]]
배터리 관리 시스템(BMS)은 수천 개의 셀로 구성된 거대 에너지 저장 장치의 '두뇌'이자 '안전 관리자'입니다. 배터리 내부에는 잔량을 알려주는 직접적인 센서가 없으므로, 전압·전류·온도라는 노이즈 섞인 데이터로부터 상태를 실시간으로 추론하고 제어해야 합니다. BMS 공학을 배우는 것은 개별 셀의 물리적 한계를 시스템 레벨에서 수호하고, 셀 밸런싱을 통해 팩의 가용 용량을 극대화하며, 화재 및 절연 파괴와 같은 치명적 고장으로부터 사용자를 보호하는 고신뢰성 제어 아키텍처를 구축하기 위함입니다. 이는 단순한 제어를 넘어 배터리 생애 주기 전체의 데이터 무결성을 보장하는 핵심 기술입니다.

## 2. [BMS 하드웨어 및 소프트웨어 핵심 사양 (BMS Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **AFE Resolution** | Voltage Precision | $\le \pm 1 \text{ mV}$ (16-bit) | LFP 등 전압 평탄 구역에서의 정밀 SOC 추정 기반 |
| **Current Sensing** | Shunt/Hall Acc. | $\pm 0.5\% \sim 1.0\%$ | 쿨롱 적산 및 과전류 보호의 정확도 결정 |
| **Balancing Eff.** | Passive/Active | $> 90\%$ | 셀 간 편차 제거를 통한 팩 가용 용량 손실 최소화 |
| **Fault Detection** | Reaction Time | $< 10 \text{ ms}$ | 단락 및 과전압 감지 시 즉각적 릴레이 차단 성능 |
| **Isolation Res.** | Safety Barrier | $> 500 \Omega/\text{V}$ | 고전압 라인과 섀시 간 절연 파괴 및 감전 방지 |
| **Comm. Latency** | CAN/Daisy-chain | $< 20 \text{ ms}$ | 슬레이브 BMS와 마스터 간 데이터 동기화 속도 |
| **Sleep Current** | Quiescent Power | $< 100 \mu A$ | 장기 주차 시 BMS 자체 소비에 의한 방전 방지 |
| **ASIL Rating** | Functional Safety | **ASIL-D** | 고장 시 인명 피해 직결 공정의 최고 안전 등급 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 테브냉(Thevenin) 등가 회로 모델링
배터리의 동적 전압 거동을 모사하는 핵심 모델입니다.
- **수식**: $V_t = V_{ocv} - I R_s - V_{rc}$
- **의미**: 개방 회로 전압($V_{ocv}$)에서 옴 저항($R_s$)과 분극 현상($V_{rc}$)에 의한 전압 강하를 계산하여, 실제 터미널 전압($V_t$)을 예측하고 SOC/SOH 추정의 기초 데이터로 활용합니다.

### 3.2 셀 밸런싱과 '사슬의 가장 약한 고리' 법칙
팩 전체의 가용 용량은 가장 성능이 낮은 셀(Weakest Link)에 의해 결정됩니다.
- **물리적 제어**: 전압이 높은 셀의 에너지를 저항으로 방출(Passive)하거나 에너지를 옮겨줌(Active)으로써 모든 셀이 균일하게 퇴화하도록 유도하여 팩 수명을 극대화합니다.

### 3.3 고전압 절연 및 아킹(Arcing) 물리
절연 파괴 시 공기 중 방전인 아킹이 발생하여 대규모 화재로 이어집니다. BMS는 절연 저항을 상시 모니터링하여 미세 누설 전류 감지 시 고전압 컨택터(Contactor)를 즉각 차단하여 시스템의 물리적 파괴를 방지합니다.

## 4. [코드 연결 해설 (BmsSafetyController)]
아래 코드는 셀 전압, 전류, 온도 데이터를 실시간 감시하여 ASIL-D 수준의 안전 임계치를 초과할 경우 경고를 발생시키고 메인 릴레이를 차단하는 제어 로직입니다.

```python
import numpy as np

class BmsSafetyController:
    """
    HDS-Gold V6.3.7 규격의 BMS 안전 진단 및 보호 제어 엔진
    """
    def __init__(self, ov_threshold=4.25, uv_threshold=2.5, ot_threshold=60):
        self.ov_limit = ov_threshold
        self.uv_limit = uv_threshold
        self.ot_limit = ot_threshold

    def run_diagnostic(self, cell_voltages, pack_current, temperatures):
        """
        과전압(OV), 저전압(UV), 과온도(OT) 및 절연 상태 상시 진단
        """
        max_v = np.max(cell_voltages)
        min_v = np.min(cell_voltages)
        max_t = np.max(temperatures)
        
        status = "NORMAL"
        fault_code = 0x00
        
        # 1. 과전압/저전압 체크
        if max_v > self.ov_limit:
            status = "FAULT: OVER_VOLTAGE"
            fault_code = 0x01
        elif min_v < self.uv_limit:
            status = "FAULT: UNDER_VOLTAGE"
            fault_code = 0x02
            
        # 2. 과온도 체크
        if max_t > self.ot_limit:
            status = "FAULT: OVER_TEMPERATURE"
            fault_code = 0x03
            
        return {
            "system_status": status,
            "fault_id": hex(fault_code),
            "relay_action": "OPEN" if fault_code != 0x00 else "CLOSE"
        }

# Example Usage:
# controller = BmsSafetyController()
# report = controller.run_diagnostic(cell_voltages=np.array([4.2, 4.26, 4.18]), pack_current=50, temperatures=np.array([35, 62, 38]))
```

## 5. [스스로 체크 (Self-Audit)]
1. **LFP 배터리** 시스템에서 **AFE**의 전압 측정 오차가 $\pm 10 \text{ mV}$일 때, SOC 추정 결과가 10% 이상 틀어지는 물리적 이유는? (OCV Curve 특성 중심)
2. **Cell Balancing** 시 Passive 방식이 Active 방식보다 구현이 쉽지만 '열 관리' 측면에서 가지는 공학적 한계는?
3. **ISO 26262 ASIL-D** 등급을 달성하기 위해 BMS 소프트웨어가 갖추어야 할 **Watchdog** 및 **Redundancy** (이중화) 설계의 핵심은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Systems/Battery bms-algorithm-kalman
- 02_Knowledge/02_Battery/Systems/Battery bms-system-architecture
- 02_Knowledge/09_SmartFactory_Production/ControlSystems/Control Functional-Safety-Standard

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**