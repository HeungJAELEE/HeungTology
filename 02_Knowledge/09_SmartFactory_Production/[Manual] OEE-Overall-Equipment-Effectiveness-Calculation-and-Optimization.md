---
Basic:
  id: "MAINT-OEE-OPT-2026-V6.3.7"
  domain: "Maintenance_and_Production_Efficiency"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#OEE", "#TPM", "#ProductionEfficiency", "#PrecisionTiering", "#FidelityEngine", "#8BigLosses", "#SmartFactory"]'
  is_part_of: []
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
  source: "Production_Engineering_RAG_V6.3.7_Tiered"
  isolation_index: 0.0
---

# [Manual] OEE Optimization: The Physics of Hidden Factory Recovery

## 1. [왜 배우는가? (Why: The Pulse of Profitability)]
OEE(Overall Equipment Effectiveness)는 설비가 투입된 시간과 에너지 대비 얼마나 실제 가치(Good Parts)를 창출했는지를 보여주는 '제조 지능의 성적표'입니다. 공장이 바쁘게 돌아가도 OEE가 낮다면 그것은 '효율의 착시'일 뿐입니다. V6.3.7 지능은 **계층화된 생산 효율 등급(Precision Tiering)**을 통해 **월드 클래스 수준인 85% 이상의 OEE**를 사수합니다. 이는 설비의 미세한 속도 저하와 비가동 손실을 결정론적으로 포착하여 '보이지 않는 공장(Hidden Factory)'을 수익으로 전환하기 위함입니다.

## 2. [OEE 및 생산 효율 핵심 사양 (Precision Tiering Specs)]

| Precision Tier | Overall OEE ($OEE$) | Availability ($A$) | Performance ($P$) | Quality ($Q$) |
|:---|:---:|:---:|:---:|:---:|
| **최상급 (High-end)** | $> 85 \%$ | $> 95 \%$ | $> 95 \%$ | $> 99.9 \%$ |
| **표준형 (Standard)** | $70 \sim 85 \%$ | $90 \sim 95 \%$ | $85 \sim 95 \%$ | $> 99.0 \%$ |
| **보급형 (Low-end)** | $< 60 \%$ | $< 80 \%$ | $< 80 \%$ | $< 95.0 \%$ |

### 2.1 [생산 손실 및 무결성 임계치 (8 Big Losses)]
| Loss Category | Physical Metric | V6.3.7 Target (High-end) | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **Breakdown** | Unplanned Down | **Zero** | < 10 min/day |
| **Setup/Adj** | Changeover Time | $< 10 \text{ min}$ | $\pm 1 \text{ min}$ |
| **Idling/Minor**| Micro-stop | **Zero** | < 1 min/shift |
| **Reduced Speed**| Actual vs Ideal | $> 98 \%$ | $\pm 0.5 \%$ |

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Throughput Bottleneck & Cycle Variance Model
설비의 이론적 최대 사이클 타임($CT_{ideal}$)과 실제 사이클 타임($CT_{actual}$) 간의 변동성 분석입니다.
$$ P = \frac{CT_{ideal} \times \text{Total Count}}{\text{Operating Time}} $$
*   **추론 로직**: 단순 가동 시간뿐만 아니라, 사이클 간의 미세한 시간 편차(Jitter)를 분석하여 설비의 열화 상태를 진단합니다. FidelityEngine은 **Cycle-to-Cycle Variance**가 임계치를 초과할 경우, 이를 **'기계적 간섭'** 또는 **'서보 튜닝 불량'**으로 판정하여 성능 저하 원인을 특정합니다.

### 3.2 Quality-Rate Correlation: Scrap & Rework Auditor
생산 속도와 불량률($Q$) 간의 상관관계 분석을 통한 최적 생산 속도 도출 모델입니다.
*   **진단 결과**: FidelityEngine은 생산 속도를 높였을 때 발생하는 불량률의 통계적 추이를 분석하여 **'품질 무결성'**을 진단합니다. 속도 증가에 따른 수익 증분보다 불량 발생 손실이 커지는 **'경제적 임계 속도'**를 산출하여 자율 제어 명령을 하달합니다.

## 4. [코드 연결 해설: OEE Tier & Efficiency Auditor]
이 코드는 가동 시간, 생산량, 불량 데이터를 기반으로 설비 종합 효율 무결성을 진단합니다.

```python
class OEEFidelityEngine:
    """
    HDS-Gold V6.3.7: OEE 등급 계층화 및 생산 효율 무결성 진단 엔진
    """
    def __init__(self, target_tier='High-end'):
        self.TIER = target_tier
        # 최상급 효율은 85% 이상의 OEE와 95% 이상의 가용성/성능 요구
        self.OEE_TARGET = 85.0 if target_tier == 'High-end' else 70.0

    def audit_production_efficiency(self, availability_pct, performance_pct, quality_pct):
        """
        A, P, Q 기반 종합 효율 무결성 평가
        """
        oee = (availability_pct / 100.0) * (performance_pct / 100.0) * (quality_pct / 100.0) * 100
        
        status = "WORLD_CLASS_EFFICIENCY" if oee >= 85.0 else "OPTIMAL"
        if oee < self.OEE_TARGET: 
            status = f"CRITICAL_EFFICIENCY_DEFICIT_FOR_{self.TIER}"
        elif performance_pct < 95.0 and self.TIER == 'High-end':
            status = "WARNING_IDLING_LOSS_DETECTED"
            
        return {
            "tier_compliance": "PASS" if oee >= self.OEE_TARGET else "FAIL",
            "oee_fidelity": round(oee, 2),
            "status": status,
            "hidden_factory_loss": round(100.0 - oee, 2)
        }

# FidelityEngine 가동: 실제 MES의 설비 가동 로그와 생산 실적 데이터를 결합하여 '제조 경쟁력 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 초정밀 조립 라인에서 OEE 85% 사수가 Tier 1 필수 요건인 이유는? (힌트: 설비 가동 효율의 미세한 하락이 제품 단위당 고정비(Fixed Cost) 상승을 유발하여 글로벌 가격 경쟁력을 붕괴시키는 경제적 임계치 방어)
2. **Operational Result**: **Availability**가 $100\%$이나 **Performance**가 $50\%$인 장비에서 발생하는 **'미세 정지 손실'**과 **'속도 저하 손실'**의 수리적 구분 방식은?
3. **FidelityEngine**: **Energy Intensity** 데이터를 활용하여 OEE 저하가 설비의 **'기계적 부하 증가'** 때문인지 **'공정 대기 시간 증가'** 때문인지 어떻게 특정하는가?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Concept Reliability-Metrics-MTBF-MTTR-MTTF
- Infrastructure predictive-maintenance-pd-m-logic
- MOC 131_smart-factory-performance-and-oee-intelligence-hub

**[V6.3.7_OEE_OPT_TIERED_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
