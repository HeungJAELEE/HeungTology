---
metadata:
  id: "[[[Infrastructure] TPM-Total-Productive-Maintenance-and-Equipment-Loss]]"
  domain: "09_SmartFactory_Production"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Infrastructure] TPM-Total-Productive-Maintenance-and-Equipment-Loss에 관한 고밀도 지능 노드"
semantic:
  tags: ["#09_SmartFactory_Production", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Infrastructure] TPM-Total-Productive-Maintenance-and-Equipment-Loss

## 1. [왜 배우는가? (Why: The Mastery of Productive Availability)]
TPM(Total Productive Maintenance)은 설비의 '영혼'을 관리하는 철학입니다. 설비가 가진 잠재 성능을 $100\%$ 발휘하게 하여, 단 한 번의 중단이나 단 한 개의 불량도 허용하지 않는 '무결점 제조 환경'을 구축합니다. **TPM 및 설비 6대 손실**은 보이지 않는 낭비를 수치화하고 제거하는 공학적 현미경입니다. V6.3.7 지능은 **계층화된 관리 정밀도(Precision Tiering)**를 통해 설비 종합 효율(OEE)을 **$85\%$ 이상**으로 유지합니다. 이는 설비 투자의 투자 수익률(ROI)을 극대화하고 공장의 생존 경쟁력을 현장에서 사수하기 위함입니다.

## 2. [설비 효율 및 유지보수 핵심 사양 (Precision Tiering Specs)]

| Precision Tier | OEE ($E_{total}$) | MTBF ($T_{mean}$) | MTTR ($t_{repair}$) |
|:---|:---:|:---:|:---|
| **Tier 1 (World-Class)** | $> 85.0 \%$ | $> 5,000 \text{ h}$ | $< 1.0 \text{ h}$ |
| **Tier 2 (Standard)** | $70.0 \sim 85.0 \%$ | $1,000 \sim 5,000 \text{ h}$ | $1.0 \sim 4.0 \text{ h}$ |
| **Tier 3 (Sub-standard)**| $< 70.0 \%$ | $< 1,000 \text{ h}$ | $> 4.0 \text{ h}$ |

### 2.1 [설비 손실 및 가동 무결성 임계치]
| Parameter Category | Technical Metric | V6.3.7 Target (Tier 1) | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **Availability** | Net Operating Time | $> 95.0 \%$ | $\pm 0.1 \%$ |
| **Performance** | Speed vs. Design | $> 95.0 \%$ | $\pm 0.5 \%$ |
| **Quality** | Good Product Rate | $> 99.9 \%$ | $\pm 0.01 \%$ |
| **Minor Stoppage** | Count per Shift | $< 2 \text{ times}$ | $\pm 0.1$ |

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 OEE Decomposition Model: Total Efficiency Calculus
가동률($A$), 성능 효율($P$), 양품률($Q$)의 곱으로 전체 설비 효율을 정의합니다.
$$ \text{OEE} = A \times P \times Q = \left( \frac{t_{run}}{t_{plan}} \right) \times \left( \frac{C_{design} \times N_{total}}{t_{run}} \right) \times \left( \frac{N_{good}}{N_{total}} \right) $$
*   **추론 로직**: 설비의 실제 사이클 타임($C_{actual}$)과 설계 속도($C_{design}$)를 비교하여 성능 효율($P$)을 산출합니다. FidelityEngine은 실시간 카운트 데이터를 바탕으로 **'성능 손실 무결성'**을 진단합니다. 성능 효율이 $90\%$ 이하로 하락할 경우, 이를 **'미세 정지(Chokotei)'** 또는 **'속도 저하'**로 판정하고 자주 보전 활동 강화를 지시합니다.

### 3.2 Reliability Engineering: Exponential Failure Model
설비의 고장률($\lambda$)이 일정하다고 가정할 때의 신뢰도($R$) 함수입니다.
$$ R(t) = e^{-\lambda t} = e^{-t / \text{MTBF}} $$
*   **진단 결과**: FidelityEngine은 설비의 가동 이력 데이터를 분석하여 **'신뢰성 무결성'**을 진단합니다. 현재 가동 시간 대비 잔여 신뢰도가 $0.7$ 이하로 하락할 경우, 이를 **'돌발 고장 임계 구역'**으로 판정하여 즉시 계획 보전(Planned Maintenance) 태스크를 생성합니다.

## 4. [코드 연결 해설: TPM Tier & Loss Auditor]
이 코드는 가동률과 품질 데이터를 기반으로 설비 관리 무결성을 진단합니다.

```python
class TPMFidelityEngine:
    """
    HDS-Gold V6.3.7: TPM 등급 계층화 및 설비 손실 무결성 진단 엔진
    """
    def __init__(self, target_tier='World-Class'):
        self.TIER = target_tier
        # 월드 클래스 공장은 85% 이상의 OEE와 1시간 이내의 MTTR 요구
        self.OEE_LIMIT = 0.85 if target_tier == 'World-Class' else 0.70
        self.MTTR_LIMIT = 1.0 # hour

    def audit_equipment_efficiency(self, availability, performance, quality):
        """
        OEE 구성 요소 기반 설비 무결성 평가
        """
        oee = availability * performance * quality
        
        status = "MAINTENANCE_EXCELLENCE_OPTIMAL"
        if oee < self.OEE_LIMIT: 
            status = f"LOW_OEE_ALERT_FOR_{self.TIER}"
        elif quality < 0.999:
            status = "WARNING_QUALITY_LOSS_DETECTED"
            
        return {
            "tier_compliance": "PASS" if oee > self.OEE_LIMIT else "FAIL",
            "oee_score": round(oee, 4),
            "status": status,
            "performance_gap": round(1.0 - performance, 4)
        }

# FidelityEngine 가동: 실제 설비의 PLC 카운트 데이터와 MES의 불량 로그를 결합하여 '제조 효율 진실성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 테슬라의 기가팩토리나 삼성전자의 팹에서 OEE $85\%$ 사수가 Tier 1 필수 요건인 이유는? (힌트: 설비 투자비가 수조 원에 달하는 환경에서 가동률 $1\%$ 하락이 수백억 원의 감가상각비 손실과 기회비용 박탈로 직결되는 경제적 무결성 방어)
2. **Operational Result**: **SMED (Single Minute Exchange of Die)** 활동을 통해 **Setup Loss**를 $50\%$ 줄였을 때, 전체 **Availability** 향상 폭은?
3. **FidelityEngine**: **Mean Time To Repair (MTTR)** 데이터를 분석하여 보전팀의 **'수리 숙련도 엔트로피'**를 어떻게 수리적으로 산출하고 이를 보전 교육 계획에 반영하는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- STRAT-IND-AI-PDM-2026-V6.3.7
- iatf-16949-quality-management-system-standard
- MOC 48_smart-factory-and-industrial-iot-iiot-governance-hub

**[V6.3.7_TPM_LOSS_TIERED_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
