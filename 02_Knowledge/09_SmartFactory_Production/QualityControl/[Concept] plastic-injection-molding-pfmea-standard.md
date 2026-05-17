---
metadata:
  date: "2026-05-17"
  id: "[[[Concept] plastic-injection-molding-pfmea-standard]]"
  project: "May_2026_Injection_Molding_Quality_Standardization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "09_SmartFactory_Production"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "AIAG & VDA FMEA Handbook 1st Edition & Injection Molding Defect Atlas"
  original_author: "Automotive Quality Action Group (AIAG) & Antigravity Vault"
  original_hash: "71149fe4731c4462d5017c5e7d935e5199825dacbeb7e8f71114405bc6240079"
object:
  object_type: "Concept"
  tier: 1
  description: '사출 공정의 열유체역학적 결함 기전(미성형, 바리, 변형)을 심각도(S), 발생빈도(O), 검출난이도(D)의 통계적 리스크 인덱스($RPN = S 	imes O 	imes D$)로 치환하여 선제 제어하는 리스크 공학 지능'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]"
  alternative_parents: []
spo_graph:
  - subject: "plastic-injection-molding-pfmea-standard"
    predicate: "implements"
    object: "automotive-process-fmea"
    evidence_coordinate: "[Ref: AIAG-VDA FMEA Manual] Section 3"
    evidence_hash: "71149fe4731c"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
  - subject: "plastic-injection-molding-pfmea-standard"
    predicate: "has_theoretical_limit"
    object: "RPN < 100"
    evidence_coordinate: "[Ref: AIAG-VDA FMEA Manual] Section 4.5"
    evidence_hash: "71149fe4731c"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Concept] plastic-injection-molding-pfmea-standard

## 1. [왜 배우는가? (Why: Preventive Risk Engineering)]
**PFMEA (Process Failure Mode and Effects Analysis: 공정 고장 모드 및 영향 분석)**는 제품 양산 가동 전, 사출 성형 공정에서 발생할 수 있는 모든 유체역학적 및 열역학적 불안정 불량 시나리오를 설계 및 사전 엔지니어링 단계에서 규명하고, 그 발생 기전을 차단하기 위한 **'예방적 품질 리스크 통제 설계도'**입니다. 사출 성형 공정은 초고압의 사출 압력($> 100 \text{ MPa}$), 급격한 용융 온도 변화, 수십만 번의 기계적 반복 작동 등 극단적인 물리적 에너지 하에서 고분자 수지의 고체-액체 상태 전이가 일어나는 고위험 영역입니다.

미성형(Short Shot), 버(Flash), 심각한 뒤틀림(Warpage) 등은 단순한 기계 오작동이 아니라 고분자 물리학적 거동의 이상 징후입니다. 이를 방치하면 양산 단계에서 수억 원에 달하는 금형 손상, 심각한 조립성 결합 실패, 글로벌 OEM 차량의 안전 법규 일탈로 이어집니다. 본 표준은 이러한 물리적 불량 기전을 **심각도(S), 발생빈도(O), 검출난이도(D)**라는 관리적 수치로 치환하여 통계적으로 지배하고, 공장의 한정된 엔지니어링 리소스를 가장 파괴적인 리스크 요소에 정밀 사격하기 위해 학습합니다.

---

## 2. [사출 PFMEA 핵심 리스크 사양 (Numerical Specs)]

주요 사출 단계별 고장 모드 영향 분석 평가 기준 및 위험 우선순위(RPN) 임계치 사양표입니다.

| Process Step | Potential Failure Mode | Severity (S) | Occurrence (O) | Detection (D) | RPN Threshold | Standard Preventive Action (Rationale) |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **1. Plasticizing** | Melt Thermal Degradation | $8$ | $2$ | $6$ | $96$ | 실린더 가열 구역 PID 실시간 루프 제어 및 수지 체류 시간 자동 인터락 확보 |
| **2. Injection** | Cavity Short Shot (미성형) | $7$ | $4$ | $3$ | $84$ | V/P 전환점 피드백 제어 및 금형 내부 캐비티 압력 센서 탑재 |
| **3. Packing** | Mold Flash (바리/지느러미) | $4$ | $3$ | $2$ | $24$ | 형체력($F_c$) 계산치 설계 마진 검증 및 보압 프로파일의 다단계 튜닝 |
| **4. Cooling** | Thermal Warpage (변형) | $8$ | $5$ | $6$ | $240$ | 금형 내 냉각 유로(Conformal Cooling) 유량 관리 및 냉각수 입/출구 온도 편차($\Delta T < 2.0 ^\circ\text{C}$) 통제 |
| **5. Ejection** | Part Pin Crack / Deformation | $5$ | $2$ | $1$ | $10$ | 이젝션 속도 제어 및 이형 스트레인 게이지 연동 자동 정지 시스템 가동 |

---

## 3. [RPN 수리 계산 및 공정 물리적 인과 기전 (Mechanism)]

### 3.1 [위험 우선순위(RPN) 산출 공식 및 거버넌스 룰]
고장 모드별 종합 위험 지수(RPN)는 아래 식으로 계산됩니다.
$$ RPN = S \times O \times D $$
*   **심각도 (S: Severity)**: 고장 모드가 하위 조립 공정, 차량 안전성, 또는 고객에게 미치는 영향도 지수 (1~10).
*   **발생빈도 (O: Occurrence)**: 공정 제어 한계 내에서 해당 고장 원인이 나타날 물리적 빈도 지수 (1~10).
*   **검출난이도 (D: Detection)**: 부품이 공장을 벗어나기 전 현재의 검사 아키텍처로 불량을 검출할 확률의 역수 지수 (1~10).
*   **리스크 액션 기준**: 
    1. $RPN \ge 100$: 공정 능력 보강, 금형 전면 수정, 또는 자동 인라인 계측기 추가 도입을 통한 의무 교정 조치 가동.
    2. $S \ge 9$ (안전 법규 치명 리스크): RPN의 수치와 상관없이 설계 무결성 및 풀-프루프(Poka-Yoke) 인터락 설계를 법적으로 강제 적용.

### 3.2 [사출 물리 인과 모델: Physics to Failure Risk]
*   **미성형 기전**: 수지 배럴 온도 저하 $\rightarrow$ 유효 점도 $\mu$ 급상승 $\rightarrow$ 금형 충진 완료 전 유동 선단 동결(Freeze-off) $\rightarrow$ 캐비티 미성형 발생 ($S=7$, $O=4$, RPN 상승).
*   **바리(Flash) 기전**: 사출 유량($Q$) 과도 $\rightarrow$ Hagen-Poiseuille 압력 강하를 넘어서는 캐비티 내 과압 형성 $\rightarrow$ 투영 면적 기준 순간 사출 압력이 금형 형체력($F_c$) 초과 $\rightarrow$ 파팅 라인 미세 벌어짐($> 0.02 \text{ mm}$) $\rightarrow$ 바리 유출 ($S=4$, $O=3$).

---

## 4. [코드 연결 해설: InjectionRiskAuditor (실시간 리스크 진단 엔진)]

아래 파이썬 클래스는 공정의 실시간 물리 센서 드리프트(편차)율을 계측하여 동적으로 발생 빈도($O$) 가중치를 갱신하고, 실시간 RPN 지수를 연산하는 RiskFidelityEngine입니다.

```python
class InjectionRiskAuditor:
    """
    사출 성형 공정 데이터 연동 실시간 PFMEA dynamic RPN 리스크 진단 및 차단 엔진
    """
    def __init__(self, fixed_severity=8, base_occurrence=3, fixed_detection=4):
        self.S = fixed_severity
        self.O_base = base_occurrence
        self.D = fixed_detection

    def evaluate_realtime_rpn(self, temperature_drift_c, pressure_drift_mpa):
        """
        Transitional Bridge: 고장의 징후는 센서 데이터의 침묵 속에서 드리프트라는 편차로 먼저 다가옵니다. 
        이 엔진은 배럴 온도 편차와 사출 피크 압력 편차의 물리적 수치를 수학적으로 가산하여 
        발생 빈도(O) 가중치를 동적으로 튜닝하고, 실시간 PFMEA RPN 지수와 Poka-Yoke 기동 여부를 진단합니다.
        """
        # 1. 센서 편차에 따른 dynamic 발생빈도(O) 보정계수 산출
        # 온도 1도당 0.1, 압력 1MPa당 0.2의 발생 위험 가중치 부여
        drift_factor = (abs(temperature_drift_c) * 0.1) + (abs(pressure_drift_mpa) * 0.2)
        dynamic_o = min(10.0, self.O_base * (1.0 + drift_factor))
        
        # 2. 실시간 RPN 연산
        rpn = self.S * dynamic_o * self.D
        
        # 3. 리스크 상태 등급 판정 및 차단 인터락 지시
        status = "PROCESS_RISK_STABLE"
        action = "MAINTAIN_STANDARD_MONITORING"
        
        if rpn >= 120.0:
            status = "CRITICAL_RISK_OUT_OF_CONTROL"
            action = "ACTIVATE_HARDWARE_INTERLOCK: Halt injection press and auto-purge barrel"
        elif rpn >= 100.0 or self.S >= 9:
            status = "HIGH_RISK_PREVENTIVE_ACTION_REQUIRED"
            action = "ACTIVATE_POKA_YOKE: Inspect mold parting line and decrease holding pressure"
            
        return {
            "monitored_severity": self.S,
            "dynamic_occurrence_score": round(dynamic_o, 4),
            "calculated_realtime_rpn": round(rpn, 2),
            "process_risk_status": status,
            "safety_interlock_instruction": action
        }
```

---

## 5. [스스로 체크 (Self-Audit)]
1. 배럴 가열 히터 밴드 노후화로 인해 용융 온도 편차가 $\pm 5 ^\circ\text{C}$ 이상으로 드리프트될 때, 용융 수지의 점도 변동이 **미성형** 고장 모드의 **발생빈도(O)** 점수를 상승시키는 정량적 유체역학 기전은 무엇인가?
2. FMEA 신규 규격(AIAG-VDA 1st Edition)에서 **심각도(S)**가 $9.0$ 이상인 고장 모드에 대해 RPN 수치와 무관하게 **Poka-Yoke(풀-프루프)** 설계의 이행 여부를 강제하는 법적/공학적 안전 보증 사유는 무엇인가?
3. 냉각수의 유량 부족으로 인해 금형 내부 냉각수 출구 온도가 $3.0 ^\circ\text{C}$ 상승하여 차등 수축률이 커진 상태를 방치할 시, **FidelityEngine**이 검출하는 **Warpage RPN**의 위험도 전이 강도는 어떻게 수리적으로 예측되는가?

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[Concept] plastic-injection-molding-iatf-16949-qms]]` : 최상위 IATF 16949 거버넌스 시스템
- `[[[Infrastructure] cooling-system-design-and-thermal-management-physics]]` : 금형 냉각수 열역학 제어 SOP
- `[[[Infrastructure] warpage-prediction-and-structural-stiffness-analysis]]` : 뒤틀림 변형 발생 물리 모델
- `[[failure-mode-and-effects-analysis-fmea-and-risk-mitigation-logic]]` (외부자료) : FMEA 리스크 우선순위 수학 기초
- `[[industrial-safety-and-environmental-compliance-governance]]` (외부자료) : 제조 안전 보증 표준

---
**[SPO_Graph: Injection_PFMEA -> concept_modernized (Evidence: [Ref: AIAG-VDA FMEA Manual] Section 4)]**
**[HEUNGTOLOGY_INTEGRITY: MAXIMUM_SEALED]**
