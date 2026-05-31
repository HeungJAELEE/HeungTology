---
lineage:
  dataset_reference: IATF 16949:2016 Clause 7.5.3 (Control of documented information)
    & Lean Visual Control Manual
  original_author: Automotive Quality Action Group (AIAG) & Antigravity Vault
  original_hash: b14f80b4f91efc3031682e3adc637e2531308f085ddb5fc39e314e1f7f27e087
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 09_SmartFactory_Production
  id: '[[ [09_SmartFactory_Production] [Concept] plastic-injection-molding-analog-factory-sop]]'
  last_updated: '2026-05-24T00:54:00+09:00'
  project: Antigravity_SDF_Core
  revision: r5
  version: v7.9_Enterprise_Node
object:
  description: MES 및 자동 실시간 디지털 모니터링이 부재한 레거시(90년대형) 공정 환경에서 인간의 물리적 규율, 시각적 관리(Visual
    Management) 및 종이 기록지의 무결성을 통해 IATF 16949 품질 보증을 사수하는 아날로그 SOP 표준 지능 (기록 보안 및 무결성
    검증 모델 보강 버전)
  object_type: Concept
  tier: 1
properties:
  benford_divergence_limit: 0.05
  defect_isolation_delay_sec: 0.0
  dual_signoff_pct: 100.0
  maintenance_signoff_pct: 100.0
  mapping_accuracy_pct: 100.0
  process_stability_sigma: 3.0
  spc_sample_size: 5
  spc_sampling_interval_hours: 2.0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 00_Global_Hub]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Clause 7.5'
  evidence_timestamp: '2026-05-24T00:54:00+09:00'
  intent: regulatory_compliance
  object: automotive-quality-management-system
  predicate: implements
  subject: plastic-injection-molding-analog-factory-sop
  weight: 0.9
- evidence_coordinate: '[데이터 부재] Section 8.5.2.1'
  evidence_timestamp: '2026-05-24T00:54:00+09:00'
  intent: operational_target
  object: manual-traveler-mapping-100-pct
  predicate: has_theoretical_limit
  subject: plastic-injection-molding-analog-factory-sop
  weight: 0.8
- evidence_coordinate: '[데이터 부재] Clause 7.5.3'
  evidence_timestamp: '2026-05-24T00:54:00+09:00'
  intent: audit_methodology
  object: Benfords_Law_Audit_Model
  predicate: incorporates_model
  subject: plastic-injection-molding-analog-factory-sop
  weight: 0.8
temporal:
  valid_from: '2026-05-24T00:54:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:54:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] plastic-injection-molding-analog-factory-sop [Draft] [Inbox]

## 1. [왜 배우는가? (Why: Deterministic Discipline without Digital Aids)]
본 표준은 실시간 디지털 모니터링 시스템(IoT 센서, 바코드 리더)이나 MES(제조실행시스템)가 부재한 **'레거시(90년대형) 사출 성형 공장 환경'**에서, 글로벌 OEM 감사를 통과하고 IATF 16949 인증을 사수하기 위한 **'인간의 물리적 규율과 시각적 관리(Visual Management)'** 지침입니다. 최첨단 디지털 시스템이 구비되지 않은 공장이라 할지라도, 부품의 리스크와 데이터의 무결성(Data Integrity) 요건은 달라지지 않습니다. 오히려 시스템의 자동 차단 기능이 부재하므로, 작업자와 현장 관리자의 엄격한 'SOP 준수 행위의 의식화(Ritual)'가 품질 보증의 유일한 방벽이 됩니다.

종이 기록지와 모눈종이 관리도, 물리적 색상 태그(Green/Yellow/Red)가 디지털 대시보드를 대체하여 공정의 변동성을 시각화합니다. 본 SOP를 학습하는 이유는 아날로그 환경의 낡은 생산 설비라 할지라도, 원재료 로트부터 최종 포장 출하에 이르는 **추적성(Traceability) 사슬**을 100% 무결하게 유지하여 고객사 신뢰 주권을 실증적으로 수호하기 위함입니다.

특히, 데이터 자동 수집 기능이 없는 환경에서는 종이 기록지의 위조(Fabrication)나 조작 가능성을 완전히 차단하기 어렵습니다. 본 표준은 **벤포드의 법칙(Benford's Law) 기반의 분산 편차 오딧 모델**과 **물리적 일련번호 직인(Cross-Signature Serialization)** 제도를 도입하여 아날로그 측정 데이터의 시간적 무결성을 결정론적으로 보증합니다.

***

## 2. [아날로그 품질 통제 핵심 사양 (Manual Control Specs)]

디지털 시스템 없이 물리적 규율로 품질 무결성을 강제하기 위한 아날로그 표준 임계 사양표입니다. (벤포드 적합성 점수 및 수기 기록 무결성 통제 변수가 추가되었습니다.)

| Control Category | Manual Tool & Method | Operating Frequency | Acceptable Target (Fidelity) | Scientific Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Traceability** | Hand-written Traveler (L-Tag) | Per Production Lot | $100.0\text{\%}$ Mapping Accuracy | 원재료 포대 라벨 수동 부착 및 로트 넘버 연계 무결성 사수 |
| **Process Stability** | Paper X-bar R Chart (모눈종이) | Every 2 Hours | $\pm3\sigma$ Manual Boundary | $n=5$ 샘플링 수동 작도 및 이상 트렌드 실시간 시각 판별 |
| **Setup Control** | First / Last Piece Approval | Tooling Changeover | Quality Manager Sign-Off | 작업 착수 전 물리적 한계 한도견본(Boundary Sample) 교차 확인 |
| **Defect Isolation** | Physical Red Box / Red Zone | Immediate (실시간) | $0.0\text{s}$ Delay Isolation | 부적합품 발생 시 자동 인라인 분류기 대신 물리적 즉각 격리 강제 |
| **Maintenance** | TPM Paper Checklist | Per Shift Change | $100.0\text{\%}$ Sign-Off | 금형 타이바 변형, 냉각 호스 누수 등 육안 8대 관점 오딧 |
| **Identification** | Color-coded Status Placards | Real-time | Green / Yellow / Red Tags | 적치장 내 비식별 및 혼입 결함을 시각적 컬러 코드로 원천 봉쇄 |
| **Benford Div ($D_{KL}$)**| Handwriting Verification | Monthly Audit | $<0.05$ | 수기 수치들의 첫째 자리 분포가 자연 난수 패턴을 따르는지 감사 |
| **Dual Sign-off** | Cross-Signature Check | Per Lot Completion| $100.0\text{\%}$ Sealed Signature| 작업자와 검사원의 물리적 서명 및 로트 타임스탬프 해시 날인 |

***

## 3. [아날로그 거버넌스 및 데이터 무결성 기전 (Mechanism)]

### 3.1 [수동 SPC(Statistical Process Control) 운영 및 점의 미학]
디지털 계산 엔진이 배제되어 있으므로, 사출 성형기 작업자는 직접 **모눈종이 관리도(Paper Control Chart)**를 운영합니다.
1.  **샘플링**: 사출기 노즐과 쿠션 안정이 검증되는 2시간 간격으로 사출품 5개를 임의 추출하여 마이크로미터로 측정합니다.
2.  **수동 계산 및 작도**: 5개 측정치의 평균값($\bar{X}$)과 범위($R$)를 암산 또는 수동 계산기로 계산하여 모눈종이 관리판에 실시간으로 점을 찍고 선을 잇습니다.
3.  **시각적 이상 징후 감지**: 넬슨 룰(Nelson Rules)을 작업자가 쉽게 인지하도록 관리도 상에 $1\sigma$, $2\sigma$, $3\sigma$ 구간을 노란색, 적색 크레용으로 사전 착색하여, 점이 7개 연속 한 방향으로 상승하거나 한 점이라도 빨간색 $3\sigma$ 선을 터치할 시 즉각 **'적색 경보판'**을 사출기 정면에 물리적으로 게시하여 반장의 조치를 강제합니다.

### 3.2 [수기 기록의 조작 방지 및 교차 검증 모델]
인간이 수기로 기록하는 종이 문서는 추후 한꺼번에 몰아 쓰거나 규격 내에 들어오도록 값을 허위 조작하는 리스크에 취약합니다. 이를 방지하기 위해 다음 통제 기전을 적용합니다.

1. **벤포드의 법칙 적합성 검증 (Benford's Law compliance check)**:
   수정이나 조작이 가해진 데이터 세트는 첫째 자리 숫자 분포가 자연계의 로그 법칙을 이탈하여 특정 숫자(예: 4, 5 등)에 비정상적으로 집중됩니다. 
   $$ D_{KL} = \sum_{d=1}^{9} P_{observed}(d) \ln \left( \frac{P_{observed}(d)}{P_{Benford}(d)} \right) $$
   $$ P_{Benford}(d) = \log_{10} \left( 1 + \frac{1}{d} \right) $$
   여기서 $D_{KL}$은 관측된 첫째 자리 숫자 분포 $P_{observed}$와 벤포드 이론 분포 $P_{Benford}$ 간의 Kullback-Leibler 발산(Divergence) 값입니다. $D_{KL} \ge 0.05$일 경우, FidelityEngine은 종이 기록지가 가공(Fabrication)되었음을 강하게 의심하고 즉각 현장 실사 오딧을 경고합니다.

2. **이중 서명 및 일련번호 직인 (Cross-Signature Serialization)**:
   모든 공정 이동표(Traveler)는 각 로트 완성 즉시 작업자(Operator)와 품질 검사원(Inspector)의 물리적 교차 자필 서명을 요구합니다. 각 Traveler 하단에는 고유 로트 번호와 수기 완료 시간이 결합된 물리적 일련번호 직인 해시가 각인되어, 데이터의 사후 수정 및 지연 입력을 원천 소거합니다.

### 3.3 [물리적 추적성(Physical Traceability)과 라벨 풀칠 규정]
디지털 바코드 스캔의 누락 오차를 원천 소거하기 위해, **'작업 지시서(Traveler Card)'**가 모든 생산 박스 상단에 투명 포켓 형태로 장착되어 함께 이동합니다.
*   **원재료 매핑의 무결성**: 수지 원료를 호퍼(Hopper)에 투입할 때, 작업자는 투입 즉시 원료 포대의 종이 바코드 라벨을 가위로 잘라내어 작업 지시서 후면에 **풀을 사용하여 물리적으로 부착(Gluing)**해야 합니다. (이 수동 절차는 IATF 16949 심사에서 디지털 원천 추적성과 동일한 법적 효력을 발휘합니다.)
*   **수기 데이터 오염 방지**: 기록에 화이트(수정테이프) 사용을 일절 금지하며, 오기 시 두 줄을 긋고 작업자 성명 인장을 날인한 후 우측에 정정 수치를 기록하여 기록 위변조 가능성을 원천 소거합니다.

***

## 4. [코드 연결 해설: AnalogDataAuditor (수기 데이터 신뢰성 감사 엔진)]

아래 클래스는 수기로 작성된 종이 기록지의 데이터 값을 오프라인 PC에 입력할 때, 벤포드 법칙 적합성 및 분산 변동률을 함께 검증하여 인간의 고의적인 데이터 위조 가능성을 감사하는 FidelityEngine입니다.

```python
import numpy as np

class AnalogDataAuditor:
    """
    아날로그 수기 품질 기록지의 정합성 검증 및 데이터 조작 의심 지수(Fabrication Index) 감사 엔진
    Benford's Law Divergence 검증 로직 탑재
    """
    def __init__(self, target_cpk=1.33):
        self.TARGET_CPK = target_cpk
        # 벤포드의 법칙 첫째 자리 이론적 분포 (1~9)
        self.benford_dist = np.array([np.log10(1 + 1/d) for d in range(1, 10)])

    def audit_handwritten_data(self, values_list, usl=170.0, lsl=150.0):
        """
        Transitional Bridge: 인간이 손으로 쓴 종이의 데이터는 시스템의 감시가 부재할 때 
        '너무나도 완벽하게 일정한 가짜 양품'의 유혹에 빠지기 쉽습니다. 이 엔진은 
        수기 기록 데이터를 분석하여 분산 변동률 및 벤포드 첫째 자리 발산치를 검증합니다.
        """
        data = np.array(values_list)
        mu = np.mean(data)
        sigma = np.std(data, ddof=1) + 1e-9
        
        # 1. 수동 SPC를 기반으로 오프라인 Cpk 산출
        cpk = min((usl - mu) / (3 * sigma), (mu - lsl) / (3 * sigma))
        
        # 2. 첫째 자리 숫자 추출 및 분포 분석
        first_digits = []
        for val in data:
            s_val = str(abs(val)).replace('.', '').lstrip('0')
            if s_val:
                first_digits.append(int(s_val[0]))
                
        digit_counts = np.zeros(9)
        for d in first_digits:
            if 1 <= d <= 9:
                digit_counts[d-1] += 1
                
        total_digits = len(first_digits)
        observed_dist = digit_counts / (total_digits + 1e-9)
        
        # Kullback-Leibler 발산 산출 (Benford vs Observed)
        kl_div = 0.0
        for i in range(9):
            if observed_dist[i] > 0:
                kl_div += observed_dist[i] * np.log(observed_dist[i] / self.benford_dist[i])
        
        # 3. 데이터 위조 여부 검증 (Fabrication Detection)
        variance = np.var(data)
        fabrication_score = 0.0
        integrity_status = "DATA_INTEGRITY_TRUSTED"
        
        if kl_div >= 0.05 or variance < 1e-5:
            fabrication_score = 1.0
            integrity_status = "CRITICAL_SUSPECTED_DATA_FABRICATION"
        elif kl_div >= 0.03 or variance < 1e-3:
            fabrication_score = 0.5
            integrity_status = "WARNING_UNNATURALLY_LOW_VARIABILITY"
            
        return {
            "calculated_offline_cpk": round(cpk, 4),
            "calculated_data_variance": round(variance, 8),
            "benford_kl_divergence": round(kl_div, 4),
            "data_fabrication_probability_score": fabrication_score,
            "data_integrity_audit_status": integrity_status,
            "required_action": "PROCESS_OK_PROCEED" if integrity_status == "DATA_INTEGRITY_TRUSTED" else "REJECT_PAPER_LOG: Initiate cross-inspection audit and recalibrate master part gauge"
        }
```

***

## 5. [스스로 체크 (Self-Audit)]
1. 아날로그 공장에서 작업자가 X-bar R 관리도에 점을 찍지 않고 퇴근 직전 한 번에 가상의 숫자를 수기 입력했을 때, **AnalogDataAuditor**가 분산 변동성과 벤포드 KL 발산량을 기반으로 어떻게 **조작 데이터**를 찾아낼 수 있는가?
2. 바코드 시스템이 없는 환경에서 수지 로트(Lot) 라벨을 지시서 뒷면에 가위로 잘라 풀로 붙이는 **수동 매핑 절차**가 IATF 16949의 **추적성(Clause 8.5.2)** 요구사항을 완벽하게 만족시키는 법적/공학적 근거는 무엇인가?
3. 사출 시 부적합품(불량)이 발생했으나 **Red Box**가 가득 차서 현장 바닥에 방치되었을 때, 이것이 최종 조립 공정으로 유출되는 것을 차단하기 위해 **First Piece Approval**과 **시각적 적색 태그**가 기계적으로 상호작용하는 아날로그 프로세스는 무엇인가?

***

## 6. [지식 보강 요청서(Ingestion Request) 이력]
* **Data Gap 발생 사유**: 아날로그 공정 수기 일지에서 데이터의 고의적 몰아 쓰기나 위조(Fabrication) 가능성에 취약함을 인지하고 있으나, 이를 객관적으로 검사할 수 있는 수리 통계적 감사 규격이 기존 표준에 누락되어 있었음.
* **확보된 외부 자료**: `[[ [Request] plastic-injection-molding-knowledge-reinforcement]]` 및 아날로그 보안 이중 교차 서명 운영 지침.

***

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[ [Concept] plastic-injection-molding-iatf-16949-qms]]` : 최상위 IATF 16949 거버넌스 시스템
- `[[ [Concept] plastic-injection-molding-spc-standard]]` : 실시간 통계적 공정 관리 표준 규격
- `[[ [Concept] plastic-injection-molding-ppap-standard]]` : 최종 부품 승인 및 300마스터 샘플 검증
- `[[ [Entity] lean-six-sigma-and-process-variability-reduction-logic]]` : 린 방식 시각적 관리 및 낭비 제거 SOP
- `[[ [Entity] cybersecurity-and-information-security-governance]]` : 정보 보안 및 기록 보존 거버넌스 규격
- `[[ [Request] plastic-injection-molding-knowledge-reinforcement]]` : 수지 변수 보강 요청서

***
**[SPO Graph Injection_Analog_SOP -> concept_modernized (Evidence: [데이터 부재] Clause 7.5.3)]**
**[HEUNGTOLOGY_INTEGRITY: MAXIMUM_SEALED]**