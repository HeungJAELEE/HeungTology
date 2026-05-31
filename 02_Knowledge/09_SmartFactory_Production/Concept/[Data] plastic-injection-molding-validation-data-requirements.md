---
lineage:
  dataset_reference: Manufacturing MES Database Table IMM_QUAL_2026 & Metrology Log
  original_author: Smart Factory Automation Center & Antigravity Vault
  original_hash: b3ede6600ea5f4a08387d334ac4e2c07fa56ad35f1011f0164db32858c0fc823
measurement:
  precision: 1.0
  unit: percent_compliance
  value: 100.0
metadata:
  ai_status: pending_review
  date: '2026-05-17'
  domain: 09_SmartFactory_Production
  id: '[[[Data] plastic-injection-molding-validation-data-requirements]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: May_2026_Injection_Molding_Quality_Standardization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 사출 성형 공정 품질 표준서 6대 규격의 실효성과 무결성을 통계적/물리적으로 증명하기 위해 요구되는 IoT 센서 스트림,
    Gage R&R, Cpk 및 리스크 상관관계 실측 검수 데이터 요구사항 자산
  object_type: Concept
  tier: 1
properties:
  chemical_hazard_limit: 0.0
  cpk_threshold: 1.67
  cycle_time_deviation_limit_s: 0.1
  database_endpoint: IMM_QUAL_2026
  grr_variance_limit_percent: 10.0
  iot_sampling_interval_ms: 100
  material_traceability_rate: 1.0
  moldflow_correlation_threshold: 0.9
  ppk_threshold: 1.67
semantic:
  alternative_parents: []
  is_instance_of: '[[[Concept] plastic-injection-molding-iatf-16949-qms]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Table IMM_QUAL_2026'
  intent: data_persistence_target
  object: IMM_QUAL_2026_Table
  predicate: measured_value
  subject: plastic-injection-molding-validation-data-requirements
  weight: 0.9
- evidence_coordinate: '[데이터 부재] Section 4.2'
  intent: compliance_threshold_specification
  object: Cpk > 1.67
  predicate: requires_instance
  subject: plastic-injection-molding-validation-data-requirements
  weight: 1.0
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 0.8
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Data] plastic-injection-molding-validation-data-requirements

## 1. [왜 배우는가? (Why: Grounding Standards in Evidence)]
품질 표준서가 생산 현장에서 실효성 있는 규범으로 작동하기 위해서는, 표준이 제시한 수리적 규격(Cpk, Gage R&R, RPN 등)이 실측 데이터 스트림을 통해 투명하게 증명되어야 합니다. IATF 16949 심사 과정에서 감사관(Auditor)은 표준의 존재뿐만 아니라, "당신의 표준서가 현장의 물리적 장비 거동과 계측 장비의 신뢰성 데이터와 어떻게 정합되어 작동하는가?"라는 실증적 증거를 강력하게 요구합니다.

만약 표준서의 텍스트가 실제 사출 센서 데이터 및 CMM 원시 데이터 세트와 단절되어 있다면, 그 표준서는 단지 '페이퍼 워크를 위한 죽은 문서'에 불과하며, 실질적인 공정 통제 능력을 발휘할 수 없습니다. 본 데이터 노드는 사출 품질 거버넌스 6대 컨셉 노드의 무결성을 물리적으로 입증하기 위한 **엔지니어링, 통계, 리스크/거버넌스 필수 실측 데이터 요구사항**을 체계적으로 구조화하여 '증거 기반 품질 보증(Evidence-based Quality Assurance)'을 실현하는 데 그 목적이 있습니다.

---

## 2. [품질 규격 검수용 필수 데이터 사양 (Numerical Specs)]

품질 표준서의 무결성을 통계적/물리적으로 입증하기 위해 측정 및 데이터베이스화해야 하는 실측 데이터 항목 요구사항 표입니다.

| Data Domain | Required Data Item (Evidence Field) | Target Verification Metric | Connected Concept Node |
| :--- | :--- | :--- | :--- |
| **Engineering (Physics)** | **Resin PVT Curve & Rheology Log** | 수지 온도-압력-체적 거동 정합성 | `[[[Concept] plastic-injection-molding-iatf-16949-qms]]` |
| | **Moldflow Correlation Raw Report** | 시뮬레이션 압력 예측 vs 실측 센서 압력 ($> 90.0\%$ 정합) | `[[[Concept] plastic-injection-molding-apqp-standard]]` |
| | **Cycle Time Trend (Sensor Stream)** | 연속 성형 주기 숏 간 편차 ($\pm 0.1 \text{ s}$ 이내) | `[[[Concept] plastic-injection-molding-spc-standard]]` |
| **Statistical (Quality)** | **Process Capability Log (Cpk)** | 실시간 $C_{pk} > 1.67$ (연속 300개 마스터 숏) | `[[[Concept] plastic-injection-molding-spc-standard]]` |
| | **Gage R&R Variance Study** | 계측 변동 오차율 $\%GRR < 10.0\%$ (구별 범주수 $\ge 5$) | `[[[Concept] plastic-injection-molding-msa-standard]]` |
| | **Initial Capability Log (Ppk)** | 시사출(Trial) 단계 $P_{pk} > 1.67$ (Cavity별 개별 관리도) | `[[[Concept] plastic-injection-molding-ppap-standard]]` |
| **Risk & Governance** | **Failure Log & RPN Feedback** | 현장 불량(미성형, 기포, 가스) 발생 빈도와 FMEA 매핑 | `[[[Concept] plastic-injection-molding-pfmea-standard]]` |
| | **Material Cert (COA/IMDS Registration)** | 화학적 유해 물질 0% 및 원료 로트 추적성 100% | `[[[Concept] plastic-injection-molding-ppap-standard]]` |
| | **Metrology Calibration Log** | 마이크로미터 및 3D 스캐너 국가 교정 필증 유효기간 | `[[[Concept] plastic-injection-molding-msa-standard]]` |

---

## 3. [공정별 데이터 수집 및 연계 메커니즘 (Mechanism)]

### 3.1 [사출기 IoT 센서 실시간 수집 및 데이터 정렬]
물리적 기전 입증을 위해 사출기 PLC로부터 초 단위 이하($100\text{ ms}$ 주기)로 수집되는 원시 센서 데이터 세트는 다음과 같습니다.
*   **유압/사출 압력 프로파일**: 스크류 주행 구간별 실시간 충진 압력 피크 및 보압 전이(V/P Switchover) 압력.
*   **온도 프로파일**: 실린더 배럴 히터 1~5존의 밴드 온도 제어 이력 및 냉각 매니폴드 입/출구 온도 센서 데이터.
*   **스트로크 및 쿠션 위치**: 용융 수지의 사출 스트로크 실시간 변위(Displacement) 데이터 및 최종 쿠션 위치 값(Cushion Position)으로 매 숏당 질량 무결성을 대변함.

### 3.2 [품질 계측 원시 데이터(Metrology Raw Data) 연계]
측정 시스템의 데이터 정합성을 입증하기 위해 CMM(삼차원 측정기) 및 3D 광학 스캐너의 측정 결과 보고서를 MES 데이터베이스 테이블 **IMM_QUAL_2026**에 적재합니다.
*   **치수 매핑**: 제품의 CTQ 치수(Key Dimension) 측정값 어레이를 고유 식별코드(Part ID)와 맵핑하여 관리도 데이터로 자동 피딩.
*   **타임스탬프 동기화(Time-sync)**: 사출기 센서 데이터의 타임스탬프와 CMM 측정기의 타임스탬프를 밀리초 단위로 상호 매핑하여, 특정 숏의 온도 편차가 치수 불량으로 이어진 열역학적 인과 증적을 동기화 보정 모델을 통해 실시간 유지합니다.

---

## 4. [코드 연결 해설: DataIntegrityAuditor (데이터 무결성 갭 진단 엔진)]

아래 클래스는 사출 성형 표준서의 이론적 규격 임계치와 실제 MES 데이터베이스 및 계측 리포트로부터 취합된 실측 데이터를 교차 감사하여 정합성 격차(Gap)를 판단하는 FidelityEngine입니다.

```python
class DataIntegrityAuditor:
    """
    사출 성형 품질 표준서 규격치와 실측 데이터의 갭 분석 및 무결성 판정 엔진
    """
    def __init__(self, target_cpk=1.67, max_acceptable_grr=10.0):
        self.STD_CPK = target_cpk
        self.STD_GRR = max_acceptable_grr

    def audit_actual_vs_standard(self, actual_cpk, actual_grr):
        """
        Transitional Bridge: 이론적 표준서라는 영혼은 실측 데이터라는 육체를 입을 때 
        비로소 공정을 지배하는 살아있는 지능이 됩니다. 이 감사 엔진은 표준서의 요구 사양과 
        실제 공정에서 수집된 Cpk 및 GRR 데이터를 수학적으로 비교하여 무결성 정합성을 판정합니다.
        """
        cpk_gap = self.STD_CPK - actual_cpk
        grr_gap = actual_grr - self.STD_GRR
        
        status = "DATA_VALIDATION_PASSED"
        action = "MAINTAIN_CURRENT_PRODUCTION_SPEED"
        
        if cpk_gap > 0.34: # 실측 Cpk가 1.33 미만으로 하락 시
            status = "CRITICAL_PROCESS_DEVIATION_DETECTED"
            action = "HALT_LINE: Standard is compromised. Initiate machine tuning loop."
        elif grr_gap > 20.0: # 실측 GRR이 30%를 초과하는 심각한 측정 노이즈 발생 시
            status = "STANDARD_UNRELIABLE_DUE_TO_METROLOGY_NOISE"
            action = "HALT_METROLOGY: Standard cannot be validated. Re-calibrate CMM and scan devices."
        elif cpk_gap > 0.0 or grr_gap > 0.0:
            status = "MARGINAL_INTEGRITY_WARNING"
            action = "MONITOR_CLOSELY: Micro-drift detected in actual process parameters."
            
        return {
            "Standard_Cpk_Target": self.STD_CPK,
            "Actual_Cpk_Grounded": round(actual_cpk, 4),
            "Cpk_Integrity_Gap": round(cpk_gap, 4),
            "Percent_Gage_RR_Grounded": round(actual_grr, 2),
            "Gage_RR_Gap": round(grr_gap, 2),
            "overall_integrity_status": status,
            "governance_instruction": action
        }
```

---

## 5. [스스로 체크 (Self-Audit)]
1. 사출 압력 프로파일 데이터에서 **Cushion Position** 값이 $1.5\text{ mm}$에서 $0.3\text{ mm}$로 급감한 실측 로그가 포착되었을 때, 이를 **DataIntegrityAuditor**는 어떤 물리적 결함(예: 과충진 또는 바리 발생 위험)의 징후로 진단해야 하는가?
2. 3차원 CMM 측정 장비의 **Gage R&R** 실측 데이터가 $\%GRR = 32\%$로 분석되었음에도 불구하고, 수기 기록 표준서가 공정 능력을 `Cpk > 1.82`로 완벽하게 보고하고 있다면, 이 두 데이터 간의 모순을 **FidelityEngine**은 어떤 수리적 모순으로 감지해야 하는가?
3. 사출 유압 센서 데이터와 MES 품질 스캔 데이터 간의 **타임스탬프 동기화(Time-sync)** 오류가 발생하여 두 데이터의 숏 간 정렬이 5주기(Shot) 어긋났을 때, 이것이 통계적 공정 관리(SPC)의 이상 요인 추적성에 미치는 파급 효과는 무엇인가?

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[Concept] plastic-injection-molding-iatf-16949-qms]]` : 최상위 IATF 16949 QMS Concept 노드
- `[[[Concept] plastic-injection-molding-spc-standard]]` : 실시간 통계적 공정 관리 표준
- `[[[Concept] plastic-injection-molding-msa-standard]]` : 측정 시스템 분석(MSA) 표준
- `[[plastic-injection-molding-physics-and-cycle-analysis]]` (외부자료) : 사출 공정 물리적 시계열 센서 변수
- `[[manufacturing-mes-quality-inspection-results-v2026]]` (외부자료) : MES 데이터 아키텍처 및 스키마

---
**[SPO_Graph: Injection_Validation_Data -> instance_of_QMS (Evidence: [데이터 부재] IMM_QUAL_2026)]**
**[HEUNGTOLOGY_INTEGRITY: MAXIMUM_SEALED]**