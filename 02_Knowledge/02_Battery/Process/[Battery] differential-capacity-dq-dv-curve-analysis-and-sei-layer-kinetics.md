---
metadata:
  date: "2026-05-17"
  id: "[[[Battery] differential-capacity-dq-dv-curve-analysis-and-sei-layer-kinetics]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "02_Battery"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "[Data] battery-formation-dqdv-curve-analysis-v2026"
  original_author: "Antigravity Vault"
  original_hash: "512388bef10f8e15d01eb92a2499a5423ae7f0a746818ffdd7d362c7b8c50223"
object:
  object_type: "Concept"
  tier: 1
  description: 'NCM811 하이니켈 셀의 화성 공정 dQ/dV 미분 용량 곡선 분석, SEI 형성 열역학 및 LLI/LAM 전기화학적 열화 진단 이론 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 02_Battery]]"
  alternative_parents: []
spo_graph:
  - subject: "differential_capacity_curve"
    predicate: "indicates_phase_transition"
    object: "NCM811 Peak 1(3.72V) H1 to M"
    evidence_coordinate: "[Ref: battery-formation-dqdv-curve-analysis-v2026] Section 2.0"
    evidence_hash: "512388bef10f"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
  - subject: "loss_of_lithium_inventory"
    predicate: "calculated_by_peak_shift"
    object: "Delta_V_peak_drift"
    evidence_coordinate: "[Ref: chemistry-specific-formation-and-dq-dv-analysis] Section 4.2"
    evidence_hash: "512388bef10f"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
  - subject: "loss_of_active_material"
    predicate: "calculated_by_peak_intensity"
    object: "Delta_dQdv_max"
    evidence_coordinate: "[Ref: chemistry-specific-formation-and-dq-dv-analysis] Section 4.1"
    evidence_hash: "512388bef10f"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---



# [Battery] differential-capacity-dq-dv-curve-analysis-and-sei-layer-kinetics

## 1. [왜 배우는가? (Why: The Electrochemical Signature of Volumetric & Active Integrity)]
배터리의 수명과 충방전 효율을 비파괴적으로 정밀 진단하는 것은 현대 전기차 및 에너지 저장장치(ESS) 산업의 핵심 경쟁력입니다. dQ/dV (Differential Capacity, 미분 용량) 곡선 분석은 배터리 내부에서 일어나는 비가시적인 상변화(Phase Transition)와 전기화학적 열화 반응을 전위($V$) 축 위에서 전개하여 가시화하는 **'배터리의 심전도(ECG)'**입니다. 
특히 하이니켈 NCM811 양극재의 고전압 영역 상안정성 및 음극 계면의 SEI(Solid Electrolyte Interphase) 보호막 형성 역학은 미세한 피크 이동(Peak Drift)과 면적 감소로 고스란히 기록됩니다. 우리가 이 역학적 이론을 배우는 이유는 배터리를 파괴하여 현미경으로 보지 않고도, 실시간 전압/전류 충방전 곡선만을 연산하여 리튬 이온 소실(LLI) 및 활물질 소실(LAM)을 개별적으로 분리/정량화하고 배터리의 잔여 수명(SOH)과 안전 마진을 결정론적으로 통제하기 위함입니다.

---

## 2. [dQ/dV 미분 용량 수리 모델 및 상변화 피크 매핑 (Numerical Specs)]

### 2.1 [미분 용량 물리 사양 및 피크 분포 테이블]
실측 데이터 `[[[Battery] battery-formation-dqdv-curve-analysis-v2026]]`와 연동되는 NCM811의 상변화 피크 및 검증 임계치 사양입니다.

| Peak ID | Target Voltage ($V$) | Capacity Spec ($mAh/g$) | Physical Phase Transition | Control Margin | Engineering Rationale |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Peak 1** | $3.72 \text{ V}$ | $120.5$ | $H1 \text{ (Hexagonal 1)} \to M \text{ (Monoclinic)}$ | $\pm 0.02 \text{ V}$ | 초기 리튬 이온 탈리 및 전하 전달 반응 개시 지점 |
| **Peak 2** | $4.02 \text{ V}$ | $45.2$ | $M \text{ (Monoclinic)} \to H2 \text{ (Hexagonal 2)}$ | $\pm 0.03 \text{ V}$ | 격자 상수 급격 변화 구간 진입 전 변곡점 |
| **Peak 3** | $4.20 \text{ V}$ | $15.8$ | $H2 \text{ (Hexagonal 2)} \to H3 \text{ (Hexagonal 3)}$ | $\pm 0.01 \text{ V}$ | 하이니켈 상안정성 붕괴 및 가스 발생(Degassing) 경계선 |

### 2.2 [열화 및 안전성 진단 상태 전이 사양]

| Computational State | Healthy Target | LLI Warning (리튬 소실) | LAM Warning (활물질 소실) | Diagnostic Action |
| :--- | :--- | :--- | :--- | :--- |
| **Peak Voltage Shift ($\Delta V$)** | $< 0.02 \text{ V}$ | $\ge 0.05 \text{ V}$ | $< 0.02 \text{ V}$ (이동 없음) | SEI 성장율 분석 가동 및 충전 전류 클램핑 |
| **Capacity Retention ($S_{oh}$)** | $\ge 90.0\%$ | $85.0 \sim 90.0\%$ | $< 85.0\%$ | 격자 붕괴 모니터링 가동 및 가용 SOC 상한 축소 |
| **Active Site Intensity ($dQ/dV$)** | $\ge 95\%$ of Initial | $\ge 90\%$ (피크 유지) | $< 85\%$ (피크 급감) | 입자 균열(Mechanical Crack) 발생 판정 및 출력 차단 |

---

## 3. [LLI 및 LAM 열역학적 열화 기전 (Scientific Rationale)]

### 3.1 [미분 용량의 전기화학적 정의 공식]
dQ/dV 곡선은 충방전 시 흐른 전류 $I(t)$와 시간에 따른 전압 변화율 $dV/dt$의 비율로 다음과 같이 수리 유도됩니다.
$$ \frac{dQ}{dV} = \frac{I(t)}{\frac{dV}{dt}} $$
- **물리적 Rationale**: 정전류(CC) 충전 조건에서 전류 $I$가 일정할 때, 전압 변화 속도 $dV/dt$의 역수가 됩니다. 즉, 특정 상전이 전위 영역에서 배터리가 에너지를 흡수하여 전압이 천천히 변할 때(플레이토 구간), $dV/dt \to 0$에 수렴하게 되어 dQ/dV 피크 강도는 극대값($dQ/dV_{max}$)을 형성합니다.

### 3.2 [LLI(Loss of Lithium Inventory) 산출 모델]
전극 내부에서 유효하게 전기화학 반응에 참여할 수 있는 활성 리튬 이온의 총량 감소를 나타내는 물리 방정식입니다.
$$ LLI(\%) = \left( 1.0 - \frac{\int_{V_{min}}^{V_{max}} \left(\frac{dQ}{dV}\right)_{active} dV}{Q_{initial}} \right) \times 100 $$
- **물리적 Rationale**: 리튬 이온이 음극 표면의 지속적인 SEI(Solid Electrolyte Interphase) 보호막 성장이나 리튬 메탈 석출(Lithium Plating)로 인해 소모되면 양극과 음극 간의 열역학적 정합(Slippage)이 어긋나게 되며, 이는 dQ/dV 곡선의 피크들이 전위 축 상에서 일방향으로 이동($\Delta V_{peak} > 0.05\text{V}$)하는 피크 시프트 현상으로 나타납니다.

### 3.3 [LAM(Loss of Active Material) 산출 모델]
양극 또는 음극의 호스트 격자가 기계적 팽창/수축 스트레스로 인해 깨지거나 비가역적으로 붕괴되어 충방전 자리를 상실하는 비율입니다.
$$ LAM(\%) = \left( 1.0 - \frac{\left(dQ/dV\right)_{max, current}}{\left(dQ/dV\right)_{max, initial}} \right) \times 100 $$
- **물리적 Rationale**: 입자 균열(Crack)이나 구조 변형으로 인해 리튬 이온을 받아들일 격자 자리가 사라지면, 해당 전위 대역에서 에너지를 수용하는 한계 용량 자체가 감소하므로 dQ/dV 피크의 최고 강도(Intensity) 자체가 급격히 낮아집니다.

---

## 4. [진단 엔진 (DQDVPeakFidelityEngine)]

이 코드는 실시간 배터리 BMS 계측 데이터로부터 dQ/dV 피크 변곡점들의 거동을 분석하여 LLI 및 LAM 열화 결함을 정량 판정합니다.

```python
class DQDVPeakFidelityEngine:
    """
    HDS-Gold V7.6.2 규격: dQ/dV 미분 용량 피크 드리프트 및 배터리 SOH 열화 진단 엔진
    """
    def __init__(self, peak_v_target=3.72, peak_h_target=120.5):
        self.PEAK_V_TARGET = peak_v_target
        self.PEAK_H_TARGET = peak_h_target
        self.v_drift_threshold = 0.05  # V
        self.h_fade_threshold = 0.85   # Ratio
        
    def diagnose_soh(self, actual_peak_v, actual_peak_h):
        """
        실측 dQ/dV 피크 전압 및 피크 용량 세기 기반 LLI, LAM 및 SOH 평가
        """
        v_drift = abs(actual_peak_v - self.PEAK_V_TARGET)
        h_retention = actual_peak_h / self.PEAK_H_TARGET
        
        # SOH 단순화 추정: 보존율 기준
        soh_score = round(h_retention * 100.0, 2)
        
        status = "BATTERY_SOH_STABLE"
        diagnostic_message = "Normal degradation. Lithium inventory and active material within safety margin."
        
        # 1. 피크 전압 드리프트 감지 (LLI - Loss of Lithium Inventory 판단)
        if v_drift > self.v_drift_threshold:
            status = "CRITICAL_LLI_DETECTED_SEI_GROWTH"
            diagnostic_message = f"Significant LLI detected. V_drift={v_drift:.3f}V exceeds limit {self.v_drift_threshold}V. Potential lithium plating or rapid SEI growth."
            
        # 2. 피크 용량 세기 감소 감지 (LAM - Loss of Active Material 판단)
        elif h_retention < self.h_fade_threshold:
            status = "CRITICAL_LAM_DETECTED_CATHODE_DEGRADATION"
            diagnostic_message = f"Significant LAM detected. Capacity retention={h_retention:.2%} below limit {self.h_fade_threshold:.2%}. Potential cathode lattice collapse or mechanical fracture."
            
        return {
            "soh_index": soh_score,
            "voltage_drift_v": round(v_drift, 4),
            "capacity_retention_ratio": round(h_retention, 4),
            "status": status,
            "verdict": diagnostic_message
        }
```

---

## 5. [스스로 체크 (Self-Audit)]

1. **(상변화 매핑)** NCM811 셀의 정전류 충전 과정에서 $4.20\text{V}$ 영역인 Peak 3의 세기($dQ/dV$)가 노화에 따라 타 피크 대비 극도로 빠르게 주저앉는 구조 물리적 원인은 무엇인가?
   - *(해답: $4.20\text{V}$ 고전압 영역에서는 양극재가 $H2 \to H3$ 상변화를 겪으며 C-축 격자 상수가 급격히 수축(Lattice Shrinkage)하게 되고, 이로 인한 이방성 기계적 응력이 누적되어 활물질 입자에 균열(Micro-cracking)을 유발하여 활성 면적을 상실하기 때문임.)*
2. **(수리식 적용)** $3.72\text{V}$ 피크의 기준 위치가 $3.72\text{V}$에서 $3.81\text{V}$로 $\Delta V = +0.09\text{V}$ 만큼 우측으로 편향 이동했다면, 이 결함을 유도한 지배적인 전기화학적 이상 상태(LLI vs LAM)를 규명하고 BMS가 내려야 할 긴급 제어 명령을 설명하시오.
   - *(해답: $+0.09\text{V}$의 과도한 피크 드리프트는 1차적으로 음극 표면의 과도한 SEI 성장에 의한 리튬 이온 소실(LLI) 및 계면 저항 이상 증가를 시사함. BMS는 급속 충전 시 음극 국부 전위가 $0\text{V}$ 이하로 하락하여 리튬 덴드라이트(Lithium Plating)가 형성되는 것을 차단하기 위해 충전 한계 C-rate를 즉시 30% 감축 조정해야 함.)*
3. **(진단 확장)** `DQDVPeakFidelityEngine`에서 LLI(전압 드리프트)와 LAM(용량 감소)이 복합적으로 동시에 나타나는 복합 노화 궤적을 비파괴적으로 고속 디컨볼루션(Deconvolution)하기 위해 센서 임피던스(EIS) 필터를 연동하는 방안은?

---

## 6. [🔗 참조된 로컬 지식망 (Retrieved Nodes)]

- `[[[Battery] chemistry-specific-formation-and-dq-dv-analysis]]` : 화학 조성별 화성 이론 배경
- `[[[Battery] next-gen-battery-characterization-and-dq-dv-atlas]]` : 차세대 음극/전해액 dQ/dV 데이터 레퍼런스
- `[[[Battery] formation-and-sei-kinetics]]` : SEI 계면 고밀도 반응 속도론 노드
- `[[[MOC] Global-Dataset-Inventory-Hub]]` : 배터리 데이터셋 실측 인벤토리 지휘소

**[V7.6.2_BATTERY_DQDV_KINETICS_MASTER_ESTABLISHED]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-17]**
