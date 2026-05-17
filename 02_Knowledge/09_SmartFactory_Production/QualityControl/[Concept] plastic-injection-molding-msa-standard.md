---
metadata:
  date: "2026-05-17"
  id: "[[[Concept] plastic-injection-molding-msa-standard]]"
  project: "May_2026_Injection_Molding_Quality_Standardization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "09_SmartFactory_Production"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "AIAG MSA Reference Manual 4th Edition & Metrology Inspection SOP"
  original_author: "Automotive Quality Action Group (AIAG) & Antigravity Vault"
  original_hash: "464ec5090479a54e18aacc554d3eab6847b02dfc763bcf15bb03cdd44f9fc8f7"
object:
  object_type: "Concept"
  tier: 1
  description: '플라스틱 사출 성형 부품의 탄성 변형 및 수축 뒤틀림 특성을 고려하여 계측 시스템의 변동성($GRR = \sqrt{EV^2 + AV^2}$)을 정량 해체하고 측정 신뢰성을 확보하는 분석 지능'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]"
  alternative_parents: []
spo_graph:
  - subject: "plastic-injection-molding-msa-standard"
    predicate: "implements"
    object: "automotive-measurement-system-analysis"
    evidence_coordinate: "[Ref: AIAG MSA Manual] Chapter 2"
    evidence_hash: "464ec5090479"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
  - subject: "plastic-injection-molding-msa-standard"
    predicate: "has_theoretical_limit"
    object: "pct_grr < 10.0"
    evidence_coordinate: "[Ref: AIAG MSA Manual] Chapter 3 Section B"
    evidence_hash: "464ec5090479"
    evidence_timestamp: "2026-05-17T22:59:20+09:00"
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Concept] plastic-injection-molding-msa-standard

## 1. [왜 배우는가? (Why: Ensuring Data Integrity)]
**MSA (Measurement System Analysis: 측정 시스템 분석)**는 "우리가 3D 스캐너나 삼차원 측정기(CMM)로 계측한 이 치수 데이터를 100% 믿을 수 있는가?"라는 근원적인 질문에 대한 수학적 및 물리적 증명입니다. 플라스틱 사출 성형 부품은 성형 직후 급격한 열 수축, 불균일한 잔류 응력 방출로 인한 지속적인 크리프(Creep) 변형, 뒤틀림(Warpage) 및 유연한 탄성 계수 특성을 가집니다. 따라서 기계 가공품과 달리 계측 장비의 클램핑 압력, 프로브 접촉력, 계측 환경의 미세 온도 변화, 그리고 측정자의 SOP 미준수 수준에 따라 측정 오차가 극심하게 출렁입니다.

만약 측정 도구라는 거울이 왜곡되어 있다면(%GRR > 30%), 그 거울에 비친 부품 치수가 아무리 정상 규격 내에 들어오더라도 실제로는 치수 불량품일 확률이 높으며, 통계적 공정 관리(SPC)의 의사결정 자체가 완전히 붕괴되는 비극을 맞이하게 됩니다. 본 표준을 배우는 이유는 데이터 스트림에 끼어드는 **계측 오차(Measurement Noise)**를 수학적으로 해체하여 데이터의 정합성을 보증하고, 글로벌 OEM 감사관에게 우리의 품질 증적이 결정론적 진실임을 입증하기 위함입니다.

---

## 2. [사출 MSA 핵심 기술 사양 (Numerical Specs)]

사출 성형품의 치수 측정 정확도를 통제하기 위한 게이지 R&R 및NDC(Distinct Categories) 임계 사양표입니다.

| Parameter Category | Core Metrology Metric | Standard Requirement | Engineering Rationale |
| :--- | :--- | :--- | :--- |
| **Measurement Excellence** | %GRR (to Tolerance) | $< 10.0 \%$ | 계측 오차가 공차 한계 대비 극소하여 측정 데이터를 절대 신뢰 가능 |
| **Acceptable Buffer** | %GRR (Marginal Acceptance) | $10.0 \sim 30.0 \%$ | 중요도가 낮은 치수에 한하여 공정 마진 대비 조건부 승인 |
| **Resolution Strength** | NDC (Distinct Categories) | $\ge 5$ | 공정의 실질적인 기하 변동을 최소 5개 구간 이상으로 조밀히 식별 |
| **Repeatability (EV)** | Equipment Variation ($EV$) | Dominant in CNC CMM | 픽스처 고정 정밀도 및 계측기 기계적 왕복 주행 오차 지표 |
| **Reproducibility (AV)** | Appraiser Variation ($AV$) | Dominant in Manual | 측정자 간의 캘리퍼스 가압 편차 및 시인성 오독 지표 |
| **Reference Resolution** | Gage Discrimination | $10:1$ Rule | 측정 기기의 최소 눈금이 관리 치수 공차 폭의 $1/10$ 이하 유지 |

---

## 3. [변동 분해 수리 모델 및 사출 측정 역학 (Mechanism)]

### 3.1 [변동 분해(Variance Decomposition)의 수학적 기초]
전체 관측 변동($\sigma_{Total}^2$)은 실제 사출 부품 간의 고유 변동($\sigma_{Part}^2$)과 측정 시스템 자체 오차 변동($\sigma_{MS}^2$)의 선형 합으로 표현됩니다.
$$ \sigma_{Total}^2 = \sigma_{Part}^2 + \sigma_{MS}^2 $$
측정 시스템의 변동 $\sigma_{MS}^2$은 반복성($EV$)과 재현성($AV$)의 제곱합인 게이지 R&R 변동으로 정의됩니다.
$$ GRR = \sqrt{EV^2 + AV^2} $$
*   **반복성 (EV: Equipment Variation)**: 동일한 측정자, 동일한 부품, 동일한 조건 하에서 반복 계측했을 때 계측기의 기계적 편차입니다.
*   **재현성 (AV: Appraiser Variation)**: 서로 다른 측정자가 동일한 부품을 측정했을 때 발생하는 인간 행동 양식의 편차입니다.

### 3.2 [사출 특화 기하학적 측정 전략]
1. **탄성 변형 방지 지그(Flexible Fixturing)**: 고분자 사출물은 기계적 강도가 낮아 프로브가 접촉할 때 국부 변형이 일어납니다. 따라서 픽스처(Fixture)는 부품을 물리적으로 구속하되 잔류 응력을 유발하는 휨 변형이 최소화되도록 베셀 점(Bessel Point) 기반 다점 구속 지그를 설계하여 EV를 통제해야 합니다.
2. **비접촉 광학 메트롤로지(Non-Contact Metrology)**: 3D 스캔 및 머신 비전 측정 시, 반사 광도 변동 및 픽셀 보간 오차로 인한 AV/EV를 방지하기 위해 광택 제거 스프레이 표준과 조도 레벨 실시간 피드백 루프를 수립합니다.

---

## 4. [코드 연결 해설: InjectionMSAAuditor (측정 시스템 무결성 진단 엔진)]

아래 클래스는 측정 데이터를 기반으로 게이지 R&R 지표와 NDC를 자동 산출하고, IATF 16949 감사 통과 적합성을 평가하는 FidelityEngine입니다.

```python
class InjectionMSAAuditor:
    """
    플라스틱 사출 성형 MSA 게이지 R&R 변동 해석 및 데이터 정합성 감사 엔진
    """
    def __init__(self, tolerance_range=0.10):
        self.TOLERANCE_RANGE = tolerance_range

    def audit_measurement_system(self, ev_sigma, av_sigma, part_sigma):
        """
        Transitional Bridge: 오염된 거울은 결코 진실을 비추지 못합니다. 
        이 감사 엔진은 반복성(EV)과 재현성(AV) 데이터를 기반으로 물리적 측정 시스템의 
        실질 해상도(NDC)와 공차 대비 오차 비율(%GRR)을 수리적으로 오딧합니다.
        """
        import math
        
        # 1. GRR 변동량 및 오차율 계산
        grr_sigma = math.sqrt(ev_sigma**2 + av_sigma**2)
        pct_grr = (6 * grr_sigma / self.TOLERANCE_RANGE) * 100
        
        # 2. 구별 범주 수(NDC: Number of Distinct Categories) 산출
        ndc = 1.41 * (part_sigma / (grr_sigma + 1e-9))
        
        # 3. IATF 16949 적합성 판정
        status = "MSA_PASS_EXCELLENT"
        action = "APPROVED_FOR_SPC_AND_PPAP"
        
        if pct_grr >= 30.0:
            status = "MSA_REJECT_UNRELIABLE"
            action = "HALT_MEASUREMENT: Recalibrate device and redesign clamping jig"
        elif pct_grr >= 10.0 or ndc < 5:
            status = "MSA_CONDITIONAL_ACCEPTANCE"
            action = "RESTRICTED_USE: Audit process capability with conservative safety margin"
            
        return {
            "Gage_R_R_Sigma": round(grr_sigma, 6),
            "Percent_GRR_to_Tolerance": round(pct_grr, 2),
            "calculated_ndc": int(ndc),
            "system_fidelity_status": status,
            "required_mitigation_action": action
        }
```

---

## 5. [스스로 체크 (Self-Audit)]
1. 동일한 3D 스캐너를 사용하여 사출 뒤틀림(Warpage) 발생 부품을 측정할 때, 고정 지그의 클램핑 구속 강도 오차가 **반복성(EV)**과 **재현성(AV)** 분해 결과에 각각 어떤 수리적 가중치로 작용하는가?
2. 측정 해상도 지표인 **NDC**가 $5.0$ 미만으로 낮아졌을 때, 실제 공정이 $C_{pk} > 1.67$ 수준의 우수한 능력을 발휘하고 있더라도 관리도(Control Chart)에서 **넬슨 규칙 1** 이탈 신호가 빈번하게 발생하는 통계적 기전은 무엇인가?
3. 비접촉 비전 검사 시스템에서 조명 조도 편차가 발생하여 측정 데이터의 **%GRR**이 $28\%$ 수준으로Marginal하게 유지될 때, 이를 통제하기 위해 **FidelityEngine**은 실시간으로 어떤 하드웨어 제어 인터락 신호를 전송해야 하는가?

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[Concept] plastic-injection-molding-iatf-16949-qms]]` : 최상위 IATF 16949 거버넌스 시스템
- `[[[Infrastructure] plastic-injection-molding-physics-and-cycle-analysis]]` : 수축 뒤틀림(Warpage)의 물리적 기원
- `[[[Infrastructure] statistical-process-control-and-capability-analysis]]` : 공정 능력과 SPC 관리 논리
- `[[gauge-r-and-r-and-measurement-system-analysis-msa-logic]]` (외부자료) : 게이지 R&R 수학 기초
- `[[force-sensor-and-strain-gauge-transduction-physics]]` (외부자료) : 센서 정밀도 및 교정 메트릭

---
**[SPO_Graph: Injection_MSA -> concept_modernized (Evidence: [Ref: AIAG MSA Manual] Chapter 3)]**
**[HEUNGTOLOGY_INTEGRITY: MAXIMUM_SEALED]**
