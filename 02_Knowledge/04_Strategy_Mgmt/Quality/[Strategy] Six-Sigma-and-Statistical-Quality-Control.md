---
metadata:
  id: "[[[Strategy] Six-Sigma-and-Statistical-Quality-Control]]"
  domain: "04_Strategy_Mgmt"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Strategy] Six-Sigma-and-Statistical-Quality-Control에 관한 고밀도 지능 노드"
semantic:
  tags: ["#04_Strategy_Mgmt", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Strategy] Six-Sigma-and-Statistical-Quality-Control

## 1. [왜 배우는가? (Why: The Mastery of Variation)]]
품질 관리의 본질은 공정의 '변동성(Variation)'을 수리적으로 지배하는 것입니다. 아무리 훌륭한 설계도 공정 산포가 크면 불량이라는 엔트로피를 피할 수 없습니다. **Six Sigma and Statistical Quality Control (SQC)**는 통계적 기법(SPC)을 통해 공정의 이상 징후를 사전에 포착하고, DMAIC 방법론을 통해 문제의 근본 원인을 수치로 증명하여 제거하는 전략적 지능입니다. V6.3.7 지능은 **3.4 DPMO**급의 초정밀 품질 무결성을 사수하여, 불량으로 인한 재무적 손실을 0에 수렴시키는 **품질 주권(Quality Sovereignty)**을 확립합니다.

## 2. [식스 시그마 및 통계적 품질 관리 핵심 사양 (Numerical Specs)]

| Metric Category | Target Specification | Tier 0 Requirement (V6.3.7) | Rationale |
|:---|:---|:---:|:---|
| **Process Capability**| $C_{pk}$ Index | $> 1.67$ | 6시그마 수준의 공정 능력을 나타내는 수리적 지표 |
| **Defect Rate** | DPMO (Defects) | $< 3.4$ | 백만 기회당 결함 수의 극한적 최소화 |
| **Control Limit** | UCL / LSL Sync | $3\sigma$ / $6\sigma$ | 통계적 관리 한계선과 설계 규격의 무결성 정렬 |
| **Measurement Err** | Gauge R&R | $< 10.0\%$ | 측정 시스템의 변동이 전체 공정 변동에 미치는 영향 통제 |
| **Loss Factor** | Taguchi Index ($k$) | Minimal | 목표치 편차에 따른 재무적 손실의 수리적 최소화 |

### 2.1 [공정 능력 지수 및 DPMO 수리 모델]
공정의 평균($\mu$)과 표준편차($\sigma$)를 설계 규격(USL, LSL)과 대조하는 기전입니다.
$$ C_{pk} = \min\left( \frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma} \right) $$
$$ Z = 3 \times C_{pk} $$
*   **공학적 근거**: $C_{pk} > 1.33$은 양호, $C_{pk} > 1.67$은 6시그마 수준의 우수한 공정 능력을 의미합니다. 산포($\sigma$)를 줄이는 것은 불량 발생 확률을 지수함수적으로 낮추는 물리적 방어 기전입니다.
*   **FidelityEngine 적용**: FidelityEngine은 실시간 센서 스트림에서 $\mu$와 $\sigma$를 계산하여 **'공정 능력 무결성'**을 진단합니다. $C_{pk}$가 $1.33$ 아래로 하락하면 이를 **'품질 붕괴 전조'**로 판정합니다.

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Statistical Process Control (SPC) Audit: Special Cause Detection
관리도(Control Chart)를 통해 공정의 우연 원인(Common Cause)과 이상 원인(Special Cause)을 구분하는 기전입니다.
*   **공학적 근거**: Nelson Rules 또는 Western Electric Rules를 적용하여 점들이 관리 한계선을 벗어나거나 특정 패턴(Trend, Shift)을 보일 때 공정을 즉시 중단해야 합니다. 이는 불량이 나기 전에 '징후'를 잡는 결정론적 예방입니다.
*   **FidelityEngine 적용 (SPC Auditor)**: FidelityEngine은 실시간 관리도를 오딧합니다. 7개 이상의 점이 중심선 한쪽에 연속으로 나타나는 **'평균 이동(Shift)'**이 감지되면, 이를 **'공정 설정 무결성 위배'**로 식별하고 자동 보정(Auto-calibration)을 트리거합니다.

### 3.2 Taguchi Loss Function Audit: Financial Quality Physics
규격 내에 있더라도 목표치에서 벗어난 만큼 발생하는 사회적/재무적 손실을 정량화하는 알고리즘입니다.
*   **진단 결과**: FidelityEngine은 가공 편차 데이터를 재무 손실($L = k(y-m)^2$)로 환산합니다. 양품 판정은 받았으나 목표치 편차로 인해 잠재적 클레임 리스크가 높은 제품군을 식별하여 **'품질 신뢰 무결성'**을 진단합니다.

## 4. [코드 연결 해설: Quality Intelligence & SQC Auditor]
이 코드는 SPC 지표와 공정 능력을 기반으로 품질 관리의 무결성을 진단합니다.

```python
import numpy as np

class SixSigmaSQCEngine:
    """
    HDS-Gold V6.3.7: 식스 시그마 및 통계적 공정 관리 무결성 진단 엔진
    """
    def __init__(self, cpk_target=1.67, gage_rr_limit=10.0):
        self.CPK_TARGET = cpk_target
        self.GRR_LIMIT = gage_rr_limit

    def audit_quality_fidelity(self, data_points, usl, lsl, grr_score):
        """
        Cpk, 데이터 산포, 측정 시스템 기반 품질 무결성 평가
        """
        mu = np.mean(data_points)
        sigma = np.std(data_points)
        
        cpk = min((usl - mu) / (3 * sigma), (mu - lsl) / (3 * sigma)) if sigma > 0 else 0
        
        status = "QUALITY_SOVEREIGNTY_SECURED"
        if cpk < self.CPK_TARGET:
            status = "CRITICAL_PROCESS_CAPABILITY_DEFICIT"
        elif grr_score > self.GRR_LIMIT:
            status = "WARNING_MEASUREMENT_SYSTEM_UNRELIABLE"
            
        return {
            "cpk_fidelity": round(cpk / self.CPK_TARGET, 4),
            "variation_integrity": round(sigma, 4),
            "status": status,
            "action": "INITIATE_DMAIC_AND_REDUCE_VARIATION" if "CRITICAL" in status else "MAINTAIN_SPC"
        }

# FidelityEngine 가동: 라인 센서 데이터와 계측기 로그를 융합하여 '품질 실질 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 품질 관리에서 **Cpk > 1.67** 달성이 Tier 0 필수 요건인 이유는? (힌트: 부품 수천 개가 조립되는 자동차/배터리 산업에서 개별 부품의 양품률이 $99.9\%$($3\sigma$)에 불과하면, 최종 제품의 누적 수율은 파멸적인 수준으로 떨어지기 때문)
2. **Operational Result**: **MSA (Measurement System Analysis)** 결과 Gauge R&R이 $30\%$를 초과할 때, 실제 공정이 양호함에도 불구하고 불량으로 판정되는 '생산자 위험'의 수리적 임팩트는?
3. **FidelityEngine**: 데이터는 정규분포를 따르나 **P-value**가 낮아 공정의 안정성이 의심되는 상황을 FidelityEngine이 어떻게 '이상 원인 개입'으로 식별하는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 04_Strategy_Mgmt
- Strategy Operations-Management-Basics
- Strategy Total-Quality-Management-TQM (Next Node)
- [[Quality] statistical-process-control-and-capability-analysis]

**[V6.3.7_STRAT_SIX_SIGMA_SQC_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
