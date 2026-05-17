---
metadata:
  date: "2026-05-16"
  id: "[[[Semiconductor] gaafet-architecture-and-nanosheet-physics]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "01_Semiconductor"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "af4ea07cbc882486aa319866dce8b9308b5553a860a6f692fd2cfc3a316fb087"
object:
  object_type: "Concept"
  tier: 1
  description: '[Semiconductor] gaafet-architecture-and-nanosheet-physics에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 반도체_백서_통합_지휘소]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Semiconductor] gaafet-architecture-and-nanosheet-physics

## 1. 개요 (Objective)
본 노드는 차세대 반도체 트랜지스터 구조인 GAAFET(Gate-All-Around FET)을 다룹니다. 채널의 4면을 게이트로 완전히 감싸 단채널 효과를 극복하고 전력 효율을 극대화하는 원리와 2026년 실측 데이터를 기반으로 한 소자 물리 파라미터를 정의합니다 [[gaafet-log-v2026]].

## 2. 핵심 기술 사양 (Numerical Specs)

| 소자 파라미터 (Parameter) | 실측 사양 (4-Layer) | 단위 | 공학적 의미 [Rationale] |
| :--- | :---: | :---: | :--- |
| **Sheet Thickness ($T_{sh}$)** | **4.8** | nm | 양자 가둠 효과 제어 무결성 |
| **Vth (Threshold Volt.)** | **0.31** | V | 저전력 연산 최적 동작 전압 |
| **SS (Subthreshold Swing)**| **62** | mV/dec | 스위칭 속도 및 전력 효율 지표 |
| **I_off (Leakage Current)**| **45** | $ \text{pA/}\mu\text{m} $ | 오프 상태 누설 전류 차단 능력 |
| **DIBL (Drain-Induced)** | **28** | mV/V | 단채널 효과 억제 수리적 척도 |
| **WFM (Work Function Metal)**| **17.2** | $\AA$ | 게이트 일함수 기반 Vth 튜닝 |
| **Effective Drive Current** | **1.8** | $ \text{mA/}\mu\text{m} $ | 단위 면적당 구동 전류 성능 |

## 3. 핵심 소자 물리 및 수리 모델

### 3.1 양자 가둠 효과(Quantum Confinement)와 Vth 변동성
채널 두께가 원자 수준으로 얇아짐에 따라 전자의 에너지 준위가 변하고 문턱 전압($V_{th}$)이 상승합니다.
* **수리 모델**: $\Delta V_{th, QM} \approx \frac{\hbar^2 \pi^2}{2m^* q T_{si}^2}$. 나노시트 두께($T_{si}$)가 $1\text{nm}$ 감소 시 $V_{th}$가 약 $25\text{mV}$ 비선형적으로 상승하는 인과 관계를 실측했습니다 [[gaafet-log-v2026]].

### 3.2 4면 게이트 제어와 SCE 억제
FinFET의 3면 제어를 넘어 4면 전체를 제어함으로써 게이트의 채널 지배력을 극대화합니다.
* **실측 현상**: SS 값이 이론적 한계인 $60\text{mV/dec}$에 근접한 $62\text{mV/dec}$를 달성하여, 누설 전류를 FinFET 대비 $40\%$ 이상 감축하는 무결성을 입증했습니다 [[gaafet-log-v2026]].

## 4. 나노시트 적층 및 MBCFET 구조 혁신
나노시트를 수직으로 적층하여 구동 전류 성능을 향상시키고, 시트의 폭($W_{ns}$)을 조절하여 성능과 전력 소모를 최적화(DTCO)합니다.
* **성능 지표**: 4단 적층 구조에서 $1.8\text{ mA/}\mu\text{m}$의 구동 전류를 확보하여 고성능 HPC 칩 적용 무결성을 확인했습니다.

## 5. [FidelityEngine] Device Stability Diagnostic Class
```python
class DeviceStabilityAuditor:
    def __init__(self, vth_target=0.31):
        self.vth_target = vth_target
        
    def audit_device(self, measured_vth, ss_value, leakage):
        # 소자 전기적 특성 및 신뢰성 진단
        if abs(measured_vth - self.vth_target) > 0.05:
            return "CRITICAL: Vth Deviation - Adjust WFM Deposition"
        if ss_value > 70:
            return "WARNING: Poor Gate Control - Check Interface Quality"
        if leakage > 100:
            return "CRITICAL: Excessive Leakage - Check Bottom Isolation"
        return "DEVICE_PERFORMANCE_OPTIMAL"
```

**[V7.5.3_MODERNIZED]**
**[GROUNDED_VIA: gaafet-threshold-voltage-stability-and-leakage-log-v2026]**
**[REFERENCES: [[gaafet-log-v2026]], [[transistor-physics-node]]]**
