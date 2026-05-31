---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: c692ddd46871db0a0700026ce8e69a2deafc4d2ea6f26d5768ff9e99ba3de1cd
metadata:
  date: '2026-05-16'
  domain: 09_SmartFactory_Production
  id: '[[[Infrastructure] MES]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Infrastructure] MES에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  data_latency_fidelity_tolerance_ms: 10
  data_latency_max_ms: 100
  oee_fidelity_tolerance_percent: 1.0
  oee_target_threshold_percent: 85.0
  scheduling_update_max_sec: 60
  spc_control_sigma: 3.0
  sync_accuracy_fidelity_tolerance_percent: 0.05
  sync_accuracy_min_percent: 99.9
  traceability_matching_target_percent: 100.0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Infrastructure] MES

## 1. [왜 배우는가? (Why: The Brain of Real-time Manufacturing)]]
공장은 살아있는 유기체와 같습니다. 갑작스러운 설비 고장이나 자재 지연 등 수많은 변수가 발생합니다. **MES(Manufacturing Execution System)**는 이러한 변수에 즉각 대응하여 "어떤 설비가 무엇을 만들어야 가장 효율적인가?"를 결정하는 현장의 두뇌입니다. V6.3.7 지능은 **설비종합효율(OEE)**과 **실시간 트레이서빌리티(Traceability)**를 수리적으로 지배합니다. 우리가 이를 배우는 이유는 제조 현장의 '블랙박스'를 투명하게 시각화하고, "단 하나의 불량도 끝까지 추적해 원인을 규명하는 '제조 운영 주권'을 확보하기" 위함입니다. 데이터의 투명성이 공장의 수율을 결정합니다.

## 2. [제조 실행 및 추적 핵심 사양 (Precision Tiering Specs)]

| Parameter Category | Physical Metric | Tier 1 Target (V6.3.7) | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **OEE Threshold** | Total Efficiency | $> 85.0 \%$ | $\pm 1.0 \%$ |
| **Traceability** | Serial Matching | $100 \%$ | Zero Deviation Target |
| **Data Latency** | Edge-to-Cloud | $< 100 \text{ ms}$ | $\pm 10 \text{ ms}$ |
| **Sync Accuracy** | ERP-MES-PLC | $> 99.9 \%$ | $\pm 0.05 \%$ |
| **Scheduling** | AI Optimizer | Real-time | $< 60 \text{ sec}$ Update |

### 2.1 [제조 운영 무결성 임계치]
| Parameter | Technical Definition | Rationale |
|:---|:---:|:---|
| **OEE (Overall)** | $A \cdot P \cdot Q$ | 가동률($A$), 성능($P$), 품질($Q$) 지표를 통합하여 설비의 실제 가동 가치를 수리적으로 평가하고 병목(Bottleneck) 구간 즉시 식별 |
| **Lot Genealogy** | Parent-Child Link | 원자재부터 최종 제품까지의 1:1 이력 관계를 $100\%$ 보증하여 리콜 리스크를 원천 차단하고 불량의 근본 원인(Root Cause) 포렌식 지원 |
| **SPC Control** | Statistical Limits| 공정 데이터의 $3\sigma$ 편차를 실시간 감시하여 이상 징후 발생 시 설비를 강제 정지하거나 파라미터를 자율 보정하는 품질 주권 사수 |

## 3. [공학적 근거 (Scientific Rationale) 및 FidelityEngine 로직]

### 3.1 [OEE 분해 역학($OEE\ Decomposition$)과 병목 식별 모델]
설비가 돌아가고 있다고 해서 돈을 벌고 있는 것인가?
*   **공학적 근거**: 설비종합효율(OEE)은 단순한 가동률이 아니라, 가동 시간($A$), 목표 속도 대비 실제 속도($P$), 전체 생산량 중 양품 비율($Q$)의 곱집합($OEE = A \times P \times Q$)으로 정의됩니다. 이 세 가지 독립 변수를 분해($Decomposition$)함으로써, 설비가 멈춰서 손실이 났는지(Downtime), 천천히 돌아서 손실이 났는지(Speed Loss), 불량을 만들어서 손실이 났는지(Defect)를 수학적으로 완벽히 특정합니다.
*   **FidelityEngine 적용 (Efficiency Analytics)**: OEE가 목표치($85\%$)를 하회할 경우, FidelityEngine은 **손실 카테고리(Loss Category)**를 분석합니다. 가동률($A$)은 정상이나 성능 지표($P$)가 낮다면, 이를 **'설비 노후화/마모에 따른 미세 정체 위기'**로 판정하고, 스핀들 모터 전류 로그 등의 정밀 오딧(Audit)을 즉각 지시합니다.

### 3.2 [제조 족보 역학($Genealogy\ Forensics$)과 방향성 비순환 그래프 모델]
불량품 하나가 발견되었을 때, 수백만 개의 제품 중 어떤 것을 리콜해야 하는가?
*   **공학적 근거**: 원자재(Parent Lot)가 여러 공정을 거쳐 최종 제품(Child Lot)으로 분할/병합되는 과정은 방향성 비순환 그래프(DAG, Directed Acyclic Graph) 매핑 이론을 따릅니다. 특정 로드 노드($N_i$)에서 불량이 발생했을 때, 엣지($E_{ij}$)를 따라 역방향 및 순방향 탐색 알고리즘을 가동하면 오염된 모든 로트를 $100\%$ 결정론적으로 격리할 수 있습니다.
*   **FidelityEngine 적용 (Traceability Forensics)**: 특정 공정에서 치명적 불량 파라미터가 발생하면, FidelityEngine은 실시간으로 **'제조 족보(Genealogy)'**를 추적합니다. 베이즈 확률(Bayesian Inference) 기반으로 가장 유력한 '불량의 근본 원인(Root Cause)' 설비를 특정하고, 오염된 소재가 투입된 모든 재공품(WIP)의 다음 공정 진입을 강제 인터락(Interlock) 시킵니다.

## 4. [도메인 지식 결측 리스트 (Ingestion Request)]
**FidelityEngine**의 완전한 결정론적 추론을 위해, 이론적 모델을 현장과 동기화할 다음의 실측 데이터가 시스템에 결측되어 있습니다. (데이터 보강 필요)
*   **Req 1**: 단위 공정별 PLC(Programmable Logic Controller) 태그 데이터 및 초단위 설비 상태(State) 로그
*   **Req 2**: ERP의 생산 오더(Work Order)와 MES 현장 실적 간의 실시간 트랜잭션 동기화 지연(Latency) 실측치
*   **Req 3**: 불량 자재 발생 시 바코드/RFID 스캔 기반의 포워드/백워드 트래킹(Tracking) 족보 데이터베이스 덤프

## 5. [코드 연결 해설: MES Intelligence Fidelity Auditor]
이 코드는 설비 가동 데이터 및 품질 로그를 기반으로 제조 현장의 운영 무결성을 실시간 진단합니다.

```python
class MESIntelligenceEngine:
    """
    HDS-Gold V6.3.7: 스마트 팩토리 제조 실행 및 추적 무결성 진단 엔진
    """
    def __init__(self, oee_target=0.85):
        self.OEE_TARGET = oee_target

    def audit_manufacturing_fidelity(self, availability, performance, quality):
        """
        OEE 기반 제조 운영 무결성 평가
        """
        oee_actual = availability * performance * quality
        fidelity = oee_actual / self.OEE_TARGET
        
        status = "OPERATIONS_STABLE"
        if oee_actual < self.OEE_TARGET * 0.8:
            status = "CRITICAL_PRODUCTION_INEFFICIENCY_DETECTED"
        elif quality < 0.98:
            status = "WARNING_QUALITY_YIELD_DROP"
            
        return {
            "oee_actual": round(oee_actual, 4),
            "operation_fidelity": round(min(fidelity, 1.0), 4),
            "status": status,
            "action": "DIAGNOSE_BOTTLENECK_SOURCE" if status.startswith("CRITICAL") else "NORMAL_OPS"
        }
```

## 6. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: **MES**가 **ERP (Strategic)**와 **PLC (Tactical)** 사이에서 수행하는 **'Vertical Integration'**이 Tier 1 필수 요건인 이유는? (힌트: 상위 계획과 하위 실행 데이터 간의 동기화 무결성 및 실시간성 확보)
2. **Operational Result**: **OEE** 지표 중 **Performance (성능)**가 $100\%$를 초과할 때, 이를 '초과 달성'이 아닌 '표준 시간($Cycle\ Time$) 설정 오류' 혹은 '데이터 오염'으로 오딧해야 하는 이유는?
3. **FidelityEngine**: **Traceability** 데이터를 통해 특정 불량 셀의 **'소재 로트(Lot)'**와 **'전압 강하율(K-Value)'** 사이의 수리적 상관관계를 어떻게 결정론적으로 입증하는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 52_SmartFactory_Production
- [[Infrastructure] digital-twin-and-cyber-physical-systems-master-guide]
- [[Governance] iatf-16949-automotive-quality-management]

**[V6.3.7_SUB_ENTITY_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**