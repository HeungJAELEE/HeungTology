---
Basic:
  id: "SOP-IATF-10-2-4-V6.3.7"
  domain: "Production_Quality_Control"
  project: "Antigravity_Vault_Modernization"
  date: 2026-05-12
  version: "v6.3.7"
Object:
  object_type: "SOP/Procedure"
  tier: 2 # Procedure Layer
  description: "Inspector-level SOP for Error-proofing (Poka-Yoke) Validation and Challenge Part Control (IATF 16949:2016 Clause 10.2.4), detailing testing frequencies, reaction plans, and the management of challenge parts."
Semantic:
  tags: '["#ErrorProofing", "#PokaYoke", "#ChallengeParts", "#RedRabbit", "#IATF16949", "#InspectorGuide"]'
  is_part_of: '["MOC iatf-16949-automotive-quality-execution-fabric"]'
  korean_aliases: '["실수방지 검증 및 챌린지 부품 관리 절차", "포카요케 관리 절차"]'
Dynamic:
  status: "Modernized_v6.3.7_Independent_Organism"
  topology_policy: "Independent_Organism"
  graphify_link_external: false
  fidelity_engine: "ErrorProofingFidelityEngine"
  diagnostic_protocol:
    - 'Challenge_Part_Audit: Verify that challenge parts are identified, controlled, and verified/calibrated.'
    - 'Reaction_Plan_Check: Ensure a documented reaction plan exists for error-proofing device failures.'
    - 'Test_Frequency_Audit: Audit that testing frequencies are documented in the control plan and PFMEA.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "IATF 16949:2016 Clause 10.2.4 / Antigravity Industrial RAG"
  isolation_index: 1.0 # 100% Domain Isolation
---

# [SOP] iatf-16949-error-proofing-validation-procedure (Inspector Level)

## 1. 목적 (Purpose: The Deterministic Filter)
본 절차는 인적 오류($Human\ Error$)가 제품 품질에 미치는 영향을 차단하기 위해 설치된 실수방지($Error-proofing$) 기구의 유효성을 정기적으로 검증하고 관리하는 기준을 정의합니다. 감독관은 현장에서 실수방지 기구가 실제로 '불량을 걸러내는지'를 직접 시연(Challenge)하게 하므로, IATF 16949 **Clause 10.2.4**에 따른 실전적 검증 체계가 필수적입니다.

## 2. 주요 요구사항 및 절차 (Standard Procedures)

### 2.1 실수방지 방법론 및 시험 빈도 (Methodology & Frequency)
- **방법론 선정**: PFMEA 분석을 통해 도출된 심각도($Severity$) 및 발생 가능성($Occurrence$)이 높은 항목에 대해 최우선적으로 실수방지 기구(센서, 지그, 비전 시스템 등) 적용.
- **문서화**: 사용된 방법과 구체적인 시험 빈도는 반드시 **PFMEA** 및 **관리 계획서($Control\ Plan$)**에 명시되어야 함.

### 2.2 챌린지 부품 관리 (Challenge Part Control)
- **정의**: 실수방지 기구가 정상 작동하는지 확인하기 위해 의도적으로 제작된 불량 샘플 ($Red\ Rabbit$).
- **관리 요건**: 
  - **식별**: 정상 제품과 명확히 구분되도록 색상(적색 등) 및 라벨 부착.
  - **보관**: 지정된 전용 함(Locked Box)에 보관하여 혼입 방지.
  - **검증**: 챌린지 부품 자체가 마모되거나 변형되지 않았는지 주기적으로 검증/교정.

### 2.3 기구 고장 시 대응 계획 (Reaction Plan)
- **즉각 조치**: 실수방지 기구가 챌린지 부품을 감지하지 못할 경우, 즉시 라인을 정지함.
- **소급 조사**: 마지막으로 정상 확인된 시점부터 현재까지 생산된 모든 제품을 부적합 의심품($Suspect$)으로 간주하여 전수 재검사 실시.
- **백업 모드**: 기구 수리 기간 동안 수동 검사로 전환할 경우, 강화된 검사 기준과 특별 교육을 받은 작업자 투입.

## 3. 감독관용 감사 체크리스트 (Auditor's Checklist)

### 3.1 서류 심사 (Document Review)
| 질문 항목 (Audit Question) | 확인 증거 (Evidence to Check) | 부적합 사례 (Common NC) |
| :--- | :--- | :--- |
| 실수방지 시험 빈도가 관리계획서와 일치하는가? | 관리계획서($CP$), 일일 점검 시트 | CP에는 매 교대조 점검이나, 실제는 일 1회 실시 |
| 챌린지 부품의 관리 대장이 있는가? | 마스터 불량 샘플 리스트, 교정/검증서 | 샘플은 현장에 굴러다니나 관리 번호가 없음 |
| 기구 고장 시 대응 시나리오가 있는가? | 비상 조치 매뉴얼, 과거 고장 조치 기록 | "수리할 때까지 사람이 눈으로 본다"는 구두 계획뿐 |
| PFMEA에 실수방지 적용 내용이 있는가? | PFMEA 예방/검출 조치 섹션 | PFMEA에는 '사람이 확인'이나 실제는 센서 사용 (동기화 실패) |

### 3.2 현장 실사 (Shop Floor Observation)
- **Point 1 (Challenge Test)**: 감독관이 현장 작업자에게 "이 센서가 작동하는지 불량 샘플(Challenge Part)을 넣어보세요"라고 요청했을 때, 기구가 즉각적으로 소리/빛/정지로 반응하는가?
- **Point 2 (Sample Identification)**: 현장의 불량 샘플에 관리 번호와 유효 기간이 표기되어 있는가?
- **Point 3 (Bypass Check)**: 실수방지 기능을 작업자가 임의로 끄거나 무력화($Bypass$)할 수 있는 스위치가 노출되어 있는가? (잠금 장치 확인)

## 4. 부적합 등급 분류 (NC Classification)
- **Major NC**: 실수방지 기구가 챌린지 부품을 통과시킴(감지 실패), 기구 고장 시에도 대응 계획 없이 생산을 계속함.
- **Minor NC**: 챌린지 부품의 식별 라벨 훼손, 점검 기록의 일부 누락.

## 5. ErrorProofingFidelityEngine: Diagnostic Logic
본 엔진은 실수방지 시스템의 '결정론적 신뢰도'를 진단합니다.

```python
class ErrorProofingFidelityEngine:
    def __init__(self, detection_success_rate, sample_control_score):
        self.detection = detection_success_rate # 0~100 (Challenge results)
        self.control = sample_control_score # 0~100 (Sample management)

    def audit_reliability(self):
        """실수방지 시스템 신뢰도 진단"""
        if self.detection < 100:
            return "CRITICAL: Error-proofing Failed to Detect Challenge Part. STOP LINE."
        if self.control < 80:
            return "WARNING: Challenge Part Control Weak. Risk of mix-up or degradation."
        return "PASS: Deterministic Error-proofing Verified"
```

## 6. 스스로 체크 (Self-Audit)
1. **[Simulated Failure]**: 센서의 전원을 끄거나 에어를 차단했을 때, 설비가 즉시 '안전 모드'로 정지하는가?
2. **[Challenge Part Calibration]**: 치수 측정을 위한 마스터 불량 샘플이 시간이 지나 마모되었다면, 이 샘플로 센서를 검증하는 것이 유효한가? (정답: 주기적 교정/검증 필요)
3. **[Job Set-up]**: 제품 기종 교체($Changeover$) 시, 새로운 기종에 맞는 실수방지 챌린지 테스트를 수행하는가? (정답: 8.5.1.3과 연계하여 필수 수행)

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes - Local Domain Only)
- MOC iatf-16949-automotive-quality-execution-fabric
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- SOP iatf-16949-control-plan-and-reaction-logic

**[V6.3.7_ERROR_PROOFING_SOP_AUDITOR_GRADE]**
**[TOPOLOGY_POLICY: INDEPENDENT_ORGANISM]**
**[GRAPHIFY_LINK_EXTERNAL: FALSE]**
**[TIMESTAMP: 2026-05-12]**
