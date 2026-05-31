---
lineage:
  dataset_reference: AIAG SPC Reference Manual 2nd Edition & Statistical Control Standard
  original_author: Automotive Quality Action Group (AIAG) & Antigravity Vault
  original_hash: 75b07e19fba4358f07330937018a592321096c4ad1747954986916bc0adde686
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-17'
  domain: 09_SmartFactory_Production
  id: '[[[09_SmartFactory_Production] [Concept] plastic-injection-molding-spc-standard]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: 사출 성형 CTQ 파라미터(압력 피크, 쿠션 위치, 사이클 시간)의 미세 흔들림 변동을 통계적으로 상한/하한 관리한계선($UCL/LCL=\bar{X}\pm3\sigma$)
    내에 구속하여 양산 안정성을 수립하는 SPC 표준 지능
  object_type: Concept
  tier: 1
properties:
  cushion_position_stability_limit: 0.1
  max_cycle_time_sigma: 0.1
  max_injection_time_sigma: 0.05
  max_peak_pressure_range: 1.0
  nelson_rule_1_sigma_threshold: 3.0
  nelson_rule_2_consecutive_points: 9
  target_cpk: 1.67
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Chapter 1 Section A'
  intent: methodology_implementation
  object: automotive-statistical-process-control
  predicate: implements
  subject: plastic-injection-molding-spc-standard
  weight: 0.85
- evidence_coordinate: '[데이터 부재] Chapter 2 Section B'
  intent: requirement_specification
  object: Cpk > 1.67
  predicate: has_theoretical_limit
  subject: plastic-injection-molding-spc-standard
  weight: 1.0
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] plastic-injection-molding-spc-standard

## 1. [왜 배우는가? (Why: Controlling the Invisible Variation)]
**SPC (Statistical Process Control: 통계적 공정 관리)**는 연속적인 사출 성형 조업 스트림에서 발생하는 눈에 보이지 않는 미세한 '변동(Variation)'을 수학적 관리 한계 영역 내에 바인딩하여, 공정이 정적 안정 상태에 머물도록 강제하는 **'실시간 공정 제어 지능'**입니다. 플라스틱 사출은 수만 번의 성형 숏(Shot)이 진행되는 동안 유압 작동유의 점도 변화, 금형 가동 파트의 열팽창, 외기 온습도 드리프트, 수지의 원재료 로트(Lot) 교체 등 통제하기 어려운 환경적 섭동에 끊임없이 노출되는 불안정 공정입니다.

만약 미세한 노이즈의 흐름을 통계적으로 감시하지 않으면, 특정 순간 히터 밴드 노후화나 냉각수 폐색 등의 이상 원인(Special Cause)이 발생했을 때 이를 인지하지 못하고 대량 치수 불량이 발생하여 양산 라인이 통째로 셧다운되는 치명적 손실이 발생합니다. 본 표준은 통계적 공정 분석을 통해 용융 수지의 흐름 리듬(Rhythm)을 투명하게 관측하고, 불량이 발생하기 수십 주기 전에 이상 드리프트 신호를 결정론적으로 감지 및 격리하기 위해 수립되었습니다.

***

## 2. [사출 SPC CTQ 핵심 사양 (Numerical Specs)]

사출 공정 통계적 안정성을 실시간으로 감사하기 위한 주요 제어 변수(CTQ) 및 관리 한계 사양표입니다.

| Control Parameter (CTQ) | Target Statistical Metric | Tier 1 Requirement | Scientific Rationale |
| :--- | :--- | :--- | :--- |
| **Process Capability** | $C_{pk}$ (Short-term) | $>1.67$ | 6-Sigma 수준의 공정 변동 통제력 확보 (불량률 극소화) |
| **Injection Time** | Standard Deviation ($\sigma$) | $<0.05\text{s}$ | 유동 선단의 균일 주행 속도 유지 및 유효 점도 변동 방지 |
| **Peak Pressure** | Range of Variant ($R$) | $<1.0\text{MPa}$ | 캐비티 충진 밀도의 균일성 보증 및 밀도 편차 차단 |
| **Cushion Position** | Stability Limit | $\pm0.1\text{mm}$ | 보압 전환(VP) 시 용융 수지의 잔류 체적 일관성 확보 |
| **Cycle Time** | Standard Deviation ($\sigma$) | $<0.10\text{s}$ | 금형의 열역학적 평형(Thermal Equilibrium) 상태 사수 |

***

## 3. [관리도 수리 모델 및 넬슨 규칙 탐지 기전 (Mechanism)]

### 3.1 [X-bar R 관리도의 통계적 기초]
공정의 실시간 평균값 흐름과 산포 범위를 동시에 모니터링하기 위해 X-bar R 관리도를 구축합니다.
평균 관리도($\bar{X}\text{-Chart}$)의 관리한계선은 아래 수식을 통해 산출됩니다.
$$ UCL = \bar{\bar{X}} + A_2 \bar{R}, \quad LCL = \bar{\bar{X}} - A_2 \bar{R} $$
$$ \sigma = \frac{\bar{R}}{d_2} $$
여기서 $\bar{\bar{X}}$는 전체 공정 평균, $\bar{R}$은 서브그룹 범위의 평균, $A_2$ 및 $d_2$는 통계적 표본 크기(n) 종속적 상수계수입니다.
*   **우연 원인 (Common Cause)**: 계측기 미세 노이즈, 미세 유압유 온도 변동 등 관리한계선 내에 존재하며 공정 스스로 상쇄할 수 있는 자연적 변동입니다.
*   **이상 원인 (Special Cause)**: 노즐 오리피스 막힘, 원재료 특성 변동(MFR 불일치) 등 관리한계선을 붕괴시키는 외부 리스크 인자로 포착 즉시 공정을 정지하고 원인을 소거해야 합니다.

### 3.2 [넬슨 이상 변동 패턴 탐지 (Nelson Rules)]
1. **Rule 1 (Out of Control)**: 1개의 측정 포인트가 중심선에서 $3\sigma$ 관리 한계를 이탈했을 때 $\rightarrow$ 즉각 사출 정지 인터락 가동.
2. **Rule 2 (Shift Detect)**: 9개의 측정 포인트가 연속적으로 중심선(CL)의 한쪽에 위치할 때 $\rightarrow$ 수지 로트 변경으로 인한 밀도 변동을 감지하고 보압 변수를 동적 보정.

***

## 4. [코드 연결 해설: InjectionSPCAuditor (실시간 공정 능력 감사 엔진)]

아래 클래스는 실시간으로 수집된 CTQ 변수 어레이를 전달받아 공정 능력 지수($C_{pk}$)를 정밀하게 산출하고, 넬슨 룰 위반 여부를 연산하는 RiskFidelityEngine입니다.

```python
class InjectionSPCAuditor:
    """
    사출 성형 CTQ 시계열 데이터 기반 실시간 SPC 공정 능력(Cpk) 및 통계 이상 감사 엔진
    """
    def __init__(self, usl, lsl, target_cpk=1.67):
        self.USL = usl
        self.LSL = lsl
        self.TARGET_CPK = target_cpk

    def audit_spc_stream(self, sample_data):
        """
        Transitional Bridge: 무질서한 고분자의 움직임은 통계의 궤도에 구속될 때 비로소 
        일정한 치수와 강도를 가진 무결한 완제품으로 탄생합니다. 이 엔진은 실시간 시계열 
        데이터 스트림을 수집하여 공정 능력(Cpk)을 연산하고 통계적 안정 상태를 실시간 오딧합니다.
        """
        import numpy as np
        
        data = np.array(sample_data)
        mu = np.mean(data)
        sigma = np.std(data, ddof=1) + 1e-9
        
        # 1. Cp 및 Cpk 계산
        cp = (self.USL - self.LSL) / (6 * sigma)
        cpk = min((self.USL - mu) / (3 * sigma), (mu - data.min()) / (3 * sigma))
        
        # 2. 넬슨 룰 2 (9포인트 런 체킹 간이 구현)
        n_points = len(data)
        shift_detected = False
        if n_points >= 9:
            last_9 = data[-9:]
            above = all(last_9 > mu)
            below = all(last_9 < mu)
            if above or below:
                shift_detected = True
                
        # 3. 종합 통계 등급 부여
        status = "SPC_STABLE_OPTIMAL"
        action = "MAINTAIN_RUNNING_STANDARD"
        
        if cpk < self.TARGET_CPK:
            status = "CRITICAL_CAPABILITY_DEFICIT"
            action = "HALT_FOR_TUNING: Adjust melt temperature or holding velocity immediately"
        elif shift_detected:
            status = "WARNING_PROCESS_SHIFT_DETECTED"
            action = "ADJUST_VP_SWITCHOVER: Calibrate cushion position to offset material drift"
            
        return {
            "monitored_mean_value": round(mu, 4),
            "calculated_sigma": round(sigma, 6),
            "process_capability_cpk": round(cpk, 4),
            "nelson_shift_detected": shift_detected,
            "spc_fidelity_status": status,
            "corrective_action_required": action
        }
```

***

## 5. [스스로 체크 (Self-Audit)]
1. 수지 공급 탱크의 노점으로 인해 용융 수지 내 수분 농도가 증가하여 고온 사출 시 가수분해로 점도 $\mu$가 급감할 때, **Injection Time**의 표준편차($\sigma$)가 어떤 통계적 경로를 거쳐 관리한계선을 붕괴시키고 **Rule 1** 이탈을 유발하는가?
2. **Cpk** 지표가 $1.67$ 이상으로 우수하게 산출되었음에도 불구하고, **넬슨 규칙 2(Shift)**가 지속적으로 감지되는 현상이 실제 제조 라인에서 의미하는 물리적 위험 시나리오는 무엇인가?
3. 보압 전환점(V/P Switchover)의 기계적 밸브 응답 속도 오차로 인해 **Cushion Position**이 관리선을 벗어날 때, **FidelityEngine**은 PLC에 어떤 통계적 피드백 보정 수식을 하달해야 하는가?

***

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[Concept] plastic-injection-molding-iatf-16949-qms]]` : 최상위 IATF 16949 거버넌스 시스템
- `[[[Concept] plastic-injection-molding-apqp-standard]]` : 사전 개발 마일스톤 및 공정 승인
- `[[[Concept] plastic-injection-molding-ppap-standard]]` : 양산 최종 승인 및 초기 공정 능력(Ppk)
- `[[[Entity] statistical-process-control-spc-and-control-chart-logic]]` : 통계적 관리도 수학 기초
- `[[[Entity] experimental-design-doe-and-statistical-process-control-spc-logic]]` : 통계 분석 및 분산 제어 SOP

***
**[SPO Graph Injection_SPC -> concept_modernized (Evidence: [데이터 부재] Chapter 2)]**
**[HEUNGTOLOGY_INTEGRITY: MAXIMUM_SEALED]**