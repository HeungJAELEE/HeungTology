---
Basic:
  id: "SEMI-FOUP-PHYSICAL-INTERFACE-2026-V6"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#Semiconductor'
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

# [[[Semiconductor] FOUP-Physical-Standards-and-Interface

## 1. [왜 배우는가? (Why)]]
반도체 웨이퍼는 나노미터 단위의 미세 공정을 거치므로, 아주 작은 입자(Particle)나 미세한 진동, 정전기조차도 치명적인 수율 하락을 초래합니다. 300mm 웨이퍼의 안전한 항구 역할을 하는 FOUP(Front Opening Unified Pod)은 단순한 상자가 아니라, 전 세계 모든 팹(FAB)의 물류 로봇과 공정 장비가 공통적으로 인식하고 다룰 수 있도록 설계된 고정밀 하드웨어 인터페이스입니다. 이를 배우는 이유는 SEMI 표준에 기반한 물리적 정합성을 이해하여, 제조사가 다른 수천 대의 장비와 자동 반송 시스템(AMHS)이 단 1mm의 오차도 없이 유기적으로 맞물려 돌아가는 '물리적 자동화의 무결성'을 확보하기 위함입니다. 웨이퍼의 생존을 책임지는 기구적 약속입니다.

## 2. [FOUP 물리 표준 및 인터페이스 핵심 사양 (Hardware Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Outer Dimension**| SEMI E47.1 (mm) | $389 \times 330 \times 450$ | 로드포트 및 OHT 반송 장치와의 물리적 호환성 보장 |
| **Wafer Capacity** | Slots (Quantity)| 25 | 물류 효율 및 공정 뱃지(Batch) 처리를 위한 표준 수량 |
| **Coupling Acc.** | Kinematic ($\mu$m)| $\pm 50$ | 6점 지지 방식을 통한 장비 안착 시 반복 재현 정밀도 |
| **Door Torque** | Opening Force (N)| $10 \sim 25$ | 장비 로드포트 도어 오프너가 도어를 여는 데 필요한 힘 |
| **Surface Res.** | ESD ($\Omega$) | $10^6 \sim 10^9$ | 정전기 방전으로 인한 웨이퍼 패턴 파손 방지 (정전기 산산 소재) |
| **Purge Flow** | N2 Flow (L/min) | $5 \sim 20$ | 내부 산소 및 습도 제어를 위한 질소 퍼지 유량 표준 |
| **Weight** | Full Load (kg) | $8 \sim 10$ | 로봇 그리퍼 및 컨베이어 설계의 기준 하중 |
| **RFID Freq.** | Frequency (MHz) | $134.2$ (Typical) | FOUP 식별 및 추적을 위한 산업용 무선 주파수 표준 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 키네매틱 커플링(Kinematic Coupling)과 맥스웰 제약 조건
- **로직**: FOUP 바닥의 3개 V-홈(Groove)과 로드포트의 3개 핀이 만나는 6점 지지 방식은 맥스웰의 제약 조건(Maxwell's Constraint Counting)에 따라 물체의 6자유도를 완전히 구속합니다. 이는 과잉 구속(Over-constraint) 없이 중력만으로도 매번 동일한 위치에 $50\mu m$ 이내의 정밀도로 FOUP을 안착시킬 수 있게 하며, 도어 오프너와 내부 로봇 암의 기구적 정렬 오차를 원천적으로 제거합니다.

### 3.2 ESD(정전기 방지)와 파티클 제어 기술
- **로직**: FOUP 소재인 고순도 폴리카보네이트에는 카본 또는 전도성 고분자가 첨가되어 표면 저항을 조절합니다. 정전기가 너무 높으면 대기 중 파티클을 끌어당기고, 너무 낮으면 급격한 방전(ESD)이 발생하여 웨이퍼의 옥사이드 층을 파괴할 수 있습니다. 최적의 저항 영역을 유지함으로써 외부 오염원으로부터 웨이퍼를 격리하는 '미니 환경(Mini-environment)'을 완성합니다.

### 3.3 기밀성(Hermeticity)과 질소 퍼지(N2 Purge) 평형
- **로직**: 도어가 닫힌 상태에서 FOUP 내부는 외부 대기와 차단됩니다. 산소와 수분은 웨이퍼 표면의 자연 산화막을 형성하거나 부식을 유발하므로, 로드포트 하단의 퍼지 노즐을 통해 고순도 질소를 주입합니다. 내부 압력을 외부보다 약간 높게(Positive Pressure) 유지하여 도어가 열릴 때 외부 공기 유입을 차단하는 유체 역학적 방어막을 형성합니다.

## 4. [코드 연결 해설 (FOUPInterfaceEngine)]
아래 코드는 로드포트에 안착된 FOUP의 센서 데이터를 읽어 키네매틱 커플링의 정합성을 확인하고, 도어 오픈 전 내부 질소 퍼지 상태를 진단하여 웨이퍼 반출 가능 여부를 결정하는 엔진입니다.

```python
class FOUPInterfaceEngine:
    """
    HDS-Gold V6.3.7 규격의 FOUP 하드웨어 인터페이스 및 안착 진단 엔진
    """
    def __init__(self):
        self.coupling_precision_threshold = 0.05 # mm
        self.min_n2_pressure = 10.5 # kPa

    def verify_seating_accuracy(self, sensor_readings_mm):
        """
        키네매틱 커플링 6점 지지 센서 기반 안착 정밀도 진단
        """
        # Transitional Bridge: FOUP은 '웨이퍼의 우주선'입니다. 
        # 로드포트에 단 0.1mm만 어긋나게 앉아도 
        # 내부 로봇 손은 웨이퍼를 긁어버릴 것입니다. 
        # AI는 이 미세한 틈을 감지하여 도킹의 무결성을 보장합니다.
        deviation = np.max(np.abs(sensor_readings_mm))
        if deviation < self.coupling_precision_threshold:
            return "SUCCESS: KINEMATIC_COUPLING_STABLE"
        return "ERROR: SEATING_MISALIGNMENT_DETECTED"

    def check_environment_ready(self, purge_pressure, o2_level_ppm):
        """
        도어 오픈 전 내부 가스 환경(Purge) 상태 진단
        """
        if purge_pressure >= self.min_n2_pressure and o2_level_ppm < 100:
            return "READY: MINI_ENVIRONMENT_SAFE"
        return "WAIT: PURGING_IN_PROGRESS"

# Example Usage:
# foup_ai = FOUPInterfaceEngine()
# seating_status = foup_ai.verify_seating_accuracy(sensor_readings_mm=[0.01, -0.02, 0.01])
# env_status = foup_ai.check_environment_ready(purge_pressure=12.0, o2_level_ppm=50)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Kinematic Coupling**에서 3개의 **V-Groove** 방식이 일반적인 평면 안착 방식보다 수평 방향 정렬 오차(Yaw)에 강한 이유는?
2. **SEMI E47.1** 표준에서 **FOUP Flange** (로봇이 잡는 윗부분)의 강도 설계가 **OHT** 고속 이동 시 발생하는 **Inertial Force** (관성력)와 가지는 관계는?
3. **N2 Purge** 시 내부 **Pressure**가 너무 높을 경우 **Door Opening** 시퀀스에서 발생할 수 있는 기구적 간섭 문제는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/05_Specialized/Concept FOUP-and-Automated-Material-Handling-System-AMHS
- 02_Knowledge/01_Semiconductor/Process/Battery wafer-cleaning-physics
- 02_Knowledge/05_Infrastructure/Utility/Common specialty-gas-and-scubber-safety

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
