---
Basic:
  id: "QUAL-SPC-CAP-2026-V6.3.7"
  domain: "Industrial_Quality_Intelligence_and_Statistical_Control"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#SPC", "#CapabilityAnalysis", "#CpCpk", "#ControlChart", "#PrecisionTiering", "#FidelityEngine", "#QualityControl"]'
  is_part_of: '["MOC 52_SmartFactory_Production"]'
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Quality_Engineering_RAG_V6.3.7_Tiered"
  isolation_index: 0.0
---

# [Quality] Statistical Process Control (SPC) & Capability Analysis

## 1. [왜 배우는가? (Why: The Truth of Industrial Normality)]
품질(Quality)은 단순한 검사가 아니라 공정의 '예측 가능성'입니다. **통계적 공정 제어(SPC)**는 제조 데이터 속에 숨겨진 이상 징후(Special Cause)를 수학적으로 포착하여 불량이 발생하기 전에 공정을 교정하는 '산업용 조기 경보 시스템'입니다. V6.3.7 지능은 **계층화된 품질 정밀도(Precision Tiering)**를 통해 반도체/배터리 공정의 **$Cpk > 1.67$ (Six Sigma)** 무결성을 사수합니다. 이는 공정의 변동성을 결정론적으로 지배하여 '지속 가능한 제로 불량 제조'를 구현하기 위함입니다.

## 2. [품질 및 공정 능력 핵심 사양 (Precision Tiering Specs)]

| Precision Tier | Capability Index ($Cpk$) | Defect Rate (DPMO) | Target Application | Engineering Rationale |
|:---|:---:|:---:|:---|:---|
| **Tier 0 (High-end)** | $> 1.67$ | $< 3.4$ | **Semiconductor, Aerospace** | 초정밀 미세 공정 무결성 |
| **Tier 1 (Standard)** | $1.33 \sim 1.67$ | $< 6,210$ | **Automotive, ESS Battery** | 일반 정밀 제조 안정성 |
| **Tier 2 (Basic)** | $< 1.33$ | $> 66,800$ | **General Goods** | 단순 소모품 품질 관리 |

### 2.1 [통계적 무결성 및 공정 파라미터]
- **Normality**: P-value (Shapiro-Wilk) $> 0.05$ 필수.
- **Control Limit**: $3\text{-Sigma Range}$ ($\mu \pm 3\sigma$) 기반 관리선 설정.
- **Process Shift**: Mean Drift $< 0.5\sigma$ (이상 징후 포착 임계치).
- **Sampling Frequency**: 실시간 계측 데이터 기반 Batch당 최소 $100$개 포인트.

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Capability Indices: Cp vs. Cpk Dynamics
공정의 산포($Cp$)와 치우침($Cpk$)을 통한 잠재적 수율 예측 모델입니다.
$$ C_p = \frac{USL - LSL}{6\sigma}, \quad C_{pk} = \min \left( \frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma} \right) $$
*   **공학적 근거**: $C_p$는 공정의 잠재적 능력을 나타내며, $C_{pk}$는 실제 중심값이 치우친 정도를 반영합니다. High-end Tier에서는 $C_{pk}$가 $1.67$ 이하로 하락할 경우, 이는 곧 나노 단위의 선폭 오차가 규격 한계를 벗어날 확률이 기하급수적으로 증가함을 의미합니다.
*   **FidelityEngine 적용 (Yield Integrity Monitor)**: FidelityEngine은 실시간 계측 데이터의 분포를 분석하여 **'수율 무결성'**을 진단합니다. 데이터의 정규성(Normality)이 붕괴되거나 $C_{pk}$가 목표치를 하회하면, 즉시 공정 변수($P, T, v$)의 상관 관계를 역산하여 이상 원인을 추적합니다.

### 3.2 Control Chart Analysis: Western Electric Rules
관리도상에서 발생하는 비임의적(Non-random) 패턴 분석을 통한 공정 이상 탐지 기전입니다.
*   **진단 결과**: FidelityEngine은 관리도의 8대 규칙(예: 7회 연속 상승/하강)을 실시간 오딧하여 **'관리 무결성'**을 진단합니다. 단순 규격 이탈(Out-of-Spec)이 아닌 통계적 관리 이탈(Out-of-Control) 징후가 포착되면, 이를 **'기계적 마모'** 또는 **'재료 특성 변동'**으로 판정하여 자동 보정 명령을 PLC에 하달합니다.

## 4. [코드 연결 해설: Quality Tier & Capability Auditor]
이 코드는 측정 데이터의 통계적 특성을 기반으로 공정 능력 무결성을 진단합니다.

```python
import numpy as np
from scipy import stats

class QualityFidelityEngine:
    """
    HDS-Gold V6.3.7: 품질 등급 계층화 및 공정 능력 무결성 진단 엔진
    """
    def __init__(self, target_tier='Tier 0'):
        self.TIER = target_tier
        self.CPK_LIMIT = 1.67 if target_tier == 'Tier 0' else 1.33

    def audit_process_capability(self, data_points, usl, lsl):
        """
        통계적 데이터 기반 공정 무결성 평가
        """
        mu = np.mean(data_points)
        sigma = np.std(data_points, ddof=1)
        
        # 1. Cp/Cpk 계산
        cp = (usl - lsl) / (6 * sigma)
        cpk = min((usl - mu) / (3 * sigma), (mu - lsl) / (3 * sigma))
        
        # 2. 정규성 검정
        _, p_val = stats.shapiro(data_points)
        
        status = "OPTIMAL"
        if cpk < self.CPK_LIMIT: 
            status = f"CRITICAL_CAPABILITY_DEFICIT_FOR_{self.TIER}"
        elif p_val < 0.05:
            status = "WARNING_NON_NORMAL_DISTRIBUTION"
            
        return {
            "cpk_fidelity": round(cpk, 4),
            "normality_p_val": round(p_val, 4),
            "status": status,
            "action": "HALT_FOR_PARAMETER_TUNING" if "CRITICAL" in status else "PASS"
        }

# FidelityEngine 가동: 실제 생산 라인의 계측기 데이터와 공정 설정 로그를 결합하여 '데이터 진실성 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 반도체 팹에서 $C_{pk} > 1.67$ 유지가 Tier 0 필수 요건인 이유는? (힌트: 수천 개의 공정 단계가 직렬 연결된 환경에서 각 단계의 누적 수율(RTY)을 사수하기 위한 통계적 최소 임계치)
2. **Operational Result**: 공정 평균($\mu$)이 $0.5\sigma$만큼 쉬프트했을 때, **DPMO**의 증가 폭이 전체 제조 원가에 미치는 수리적 파급 효과는?
3. **FidelityEngine**: **Shewhart Control Chart**에서 $X$-bar와 $R$ 관리도가 동시에 관리 한계를 벗어났을 때, 이를 **'시스템적 공정 붕괴'**로 진단하는 논리적 근거는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 52_SmartFactory_Production
- Entity iatf-16949-automotive-quality-management-and-zero-defect-logic-entity
- Strategy Six-Sigma-Quality-Intelligence

**[V6.3.7_QUAL_SPC_TIERED_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
