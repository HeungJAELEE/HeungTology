---
metadata:
  date: "2026-05-16"
  id: "[[[Strategy] Incoterms-2020-and-Trade-Compliance]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "04_Strategy_Mgmt"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "2cee8359f5b6ed5d166685cee54372e67a5ee4da41e20b03ac3bb8c9d7651ea8"
object:
  object_type: "Concept"
  tier: 1
  description: '[Strategy] Incoterms-2020-and-Trade-Compliance에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 04_Strategy_Mgmt]]"
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


# [Strategy] Incoterms-2020-and-Trade-Compliance

## 1. [왜 배우는가? (Why: The Architecture of Risk Transfer)]]
글로벌 공급망에서 물품은 수만 킬로미터를 이동하며 수많은 물리적 위협(파손, 분실, 지연)에 노출됩니다. **Incoterms 2020 및 무역 규제 준수**는 거래 당사자 간의 비용 부담 영역과 위험 전이 시점(Risk Transfer Point)을 명확히 정의하는 '글로벌 무역 프로토콜'입니다. V6.3.7 지능은 11가지 표준 규칙의 수리적 비용 구조를 지배하고, 제재 명단(Sanction List) 스크리닝을 통해 법적 리스크를 원천 차단하는 **통상 운영 주권(Operational Trade Sovereignty)**을 확립하기 위해 필수적입니다.

## 2. [무역 거래 및 컴플라이언스 핵심 사양 (Numerical Specs)]

| Metric Category | Target / Specification | Tier 1 Requirement (V6.3.7) | Rationale |
|:---|:---|:---:|:---|
| **Insurance Coverage**| $\ge 110.0\%$ (of Value) | Zero Gap | CIF/CIP 규칙 적용 시 최소 보험 가액 준수 무결성 |
| **Sanction Hit Rate** | $0.0\%$ (Approved List) | Zero Tolerance | 제재 대상 국가/업체와의 거래 차단 무결성 |
| **HS Code Accuracy** | $> 99.0\%$ (Auto-class) | $\pm 0.5\%$ | 품목 분류 오류에 따른 과태료 및 통관 지연 방지 |
| **Risk Transfer Sync**| $< 1 \text{ Hour}$ (Logistics) | $\pm 5 \text{ Minutes}$ | 물리적 인도 시점과 법적 책임 전이 데이터의 동기화 |
| **Doc. Lead Time** | $< 24 \text{ Hours}$ (e-Docs) | $\pm 2 \text{ Hours}$ | 선하증권(B/L) 및 송장 데이터의 디지털 처리 속도 |

### 2.1 [인코텀즈 비용 구조 및 통관 가액 수리 모델]
거래 조건에 따른 최종 수입 원가($P_{landed}$)를 산출하는 기전입니다.
$$ P_{Landed} = P_{Ex-Works} + C_{Logistics} + C_{Insurance} + C_{Duty} + C_{VAT} $$
*   **공학적 근거**: **DDP (Delivered Duty Paid)** 조건은 판매자가 목적지 통관 및 세금까지 모두 책임지는 가장 높은 리스크를 부담하며, **EXW (Ex-Works)**는 구매자가 모든 위험을 안게 됩니다. 특히 **CIF/CIP** 조건에서는 보험 가액이 인보이스 가액의 최소 $110\%$를 충족해야 함을 수리적으로 검증해야 합니다.
*   **FidelityEngine 적용**: FidelityEngine은 계약 조건별 비용 항목과 실제 지불 로그를 대조하여 **'비용 분담 무결성'**을 진단하고, 보험 증권의 부합 여부를 오딧합니다.

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Kinematics of Risk: Transfer Point Audit
물품의 물리적 위치 변화에 따른 위험 전이(Risk Transfer)의 정합성을 오딧하는 기전입니다.
*   **공학적 근거**: **FOB (Free On Board)**의 경우 물품이 본선에 적재되는 시점에 위험이 전이됩니다. 만약 적재 과정(Lifting) 중에 사고가 발생했다면, 이는 판매자의 책임($Liability$)으로 결정론적으로 산출됩니다.
*   **FidelityEngine 적용 (Risk Auditor)**: FidelityEngine은 항만 IoT 데이터와 크레인 가동 로그를 분석하여 **'책임 전이 무결성'**을 진단합니다. 사고 시점의 GPS 좌표와 인코텀즈 전이 지점을 대조하여 보험 청구 주체를 자동으로 특정합니다.

### 3.2 Regulatory Integrity Logic: Sanction & HS-Code Audit
글로벌 제재 명단 스크리닝 및 품목 분류 정합성을 오딧하는 알고리즘입니다.
*   **진단 결과**: FidelityEngine은 거래 상대방의 법적 실체(Entity)와 **Denial List**를 실시간으로 교차 오딧합니다. 제재 대상과의 $1\%$라도 연관성이 발견되면 트랜잭션을 즉시 차단(Halt)합니다. 또한 HS Code 오분류로 인한 관세 포탈 리스크를 **'규제 무결성 위기'**로 분류합니다.

## 4. [코드 연결 해설: Trade Compliance & Insurance Auditor]
이 코드는 인코텀즈 조건을 확인하고 CIF/CIP 보험 가액 및 제재 명단 히트 여부를 진단합니다.

```python
class TradeComplianceEngine:
    """
    HDS-Gold V6.3.7: 무역 컴플라이언스 및 인코텀즈 무결성 진단 엔진
    """
    def __init__(self, min_insurance=1.1, sanction_list=["ENTITY_X", "COUNTRY_Y"]):
        self.INSURANCE_RATIO = min_insurance
        self.SANCTION_LIST = sanction_list

    def audit_trade_fidelity(self, term, invoice_val, insurance_val, partner_name):
        """
        인코텀즈 조건, 보험가액, 파트너 기반 무역 무결성 평가
        """
        status = "TRADE_COMPLIANCE_VERIFIED"
        
        # 1. 제재 명단 스크리닝 (Sanction Screening)
        if partner_name in self.SANCTION_LIST:
            status = "CRITICAL_SANCTION_VIOLATION_DETECTED"
            
        # 2. 보험 가액 무결성 검증 (CIF/CIP 전용)
        if term in ["CIF", "CIP"]:
            coverage_ratio = insurance_val / invoice_val
            if coverage_ratio < self.INSURANCE_RATIO:
                status = "WARNING_INSURANCE_COVERAGE_INSUFFICIENT"
                
        return {
            "compliance_fidelity": 1.0 if "CRITICAL" not in status else 0.0,
            "insurance_fidelity": round(insurance_val / (invoice_val * self.INSURANCE_RATIO), 4) if term in ["CIF", "CIP"] else 1.0,
            "status": status,
            "action": "BLOCK_TRANSACTION" if "CRITICAL" in status else "MAINTAIN_MONITORING"
        }

# FidelityEngine 가동: 선적 서류(B/L) 데이터와 글로벌 제재 DB를 융합하여 '통상 실질 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 무역 관리에서 **Sanction Screening 100% 준수**가 Tier 1 필수 요건인 이유는? (힌트: 제재 위반은 단순한 과태료를 넘어 기업의 글로벌 금융망 퇴출 및 브랜드 주권 말살로 이어지는 치명적인 '생존 리스크'이기 때문)
2. **Operational Result**: **FCA** 조건이 **FOB** 대비 '복합 운송(Intermodal)' 환경에서 위험 전이 시점을 더 명확히 규정하는 수리적 이유는?
3. **FidelityEngine**: **HS Code** 분류 오류로 인해 관세를 초과 납부한 상황을 FidelityEngine이 어떻게 인지하고 **'관세 환급(Refund)'** 기회를 오딧하는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 04_Strategy_Mgmt
- Strategy Global-Trade-Policy
- Strategy Regulatory-Compliance
- Entity incoterms-2020-and-international-trade-governance

**[V6.3.7_STRAT_TRADE_INC_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
