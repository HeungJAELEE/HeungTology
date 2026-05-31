---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 0fe7ac5ae92dccde3679c1b461df7cc319ec50188eb063d9f4bbaf0d7f2532d4
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] semicon-test-l1-eds-and-yield-analysis]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] semicon-test-l1-eds-and-yield-analysis에 관한 고밀도 지능
    노드'
  object_type: Concept
  tier: 1
properties:
  contact_resistance_trend_threshold: 0.1 ohm
  fidelity_engine_metrology_tolerance: +/- 0.05%
  fidelity_engine_redundancy_tolerance: +/- 2%
  fidelity_engine_signaling_speed_tolerance: +/- 0.1 gbps
  fidelity_engine_tip_accuracy_tolerance: +/- 0.2 um
  high_end_contact_resistance: < 0.1 ohm
  high_end_metrology_error: < 0.1%
  high_end_redundancy_efficiency: '> 90%'
  high_end_signaling_speed: '> 2.0 gbps'
  high_end_test_coverage: '> 99.99%'
  high_end_tip_accuracy: < +/- 1.0 um
  high_frequency_crosstalk_limit: '> 2.0 ghz'
  low_end_contact_resistance: '> 5.0 ohm'
  low_end_test_coverage: '> 98.0%'
  standard_contact_resistance: 0.5 ~ 1.0 ohm
  standard_test_coverage: '> 99.5%'
  yield_forecast_threshold: 85%
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 반도체_백서_통합_지휘소]]'
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

# [Semiconductor] semicon-test-l1-eds-and-yield-analysis

## 1. STRATEGIC UTILITY: YIELD & PROFITABILITY GOVERNANCE
EDS(Electrical Die Sorting)는 반도체 수익성 결정 Terminal Validation Gate로 기능한다 [Ref: SEMI-TEST-EDS-2026-V6.3.7]. 전공정 무결성 입증을 통해 불량 칩의 고비용 패키징 유입을 원천 차단하며 [Ref: SEMI-TEST-EDS-2026-V6.3.7], HBM 및 AI 가속기 공정 내 **Known Good Die (KGD)** 확보를 위한 **계층화된 테스트 정밀도(Precision Tiering)**를 핵심 전략으로 운용한다 [Ref: SEMI-TEST-EDS-2026-V6.3.7].

## 2. PRECISION TIERING SPECIFICATIONS

| Precision Tier | Test Coverage | Contact Res. ($R_c$) | Target Application |
|:---|:---:|:---:|:---|
| **High-end** | $> 99.99 \%$ [Ref: V6.3.7] | $< 0.1 \Omega$ [Ref: V6.3.7] | **HBM4, AI Accelerators** |
| **Standard** | $> 99.5 \%$ [Ref: V6.3.7] | $0.5 \sim 1.0 \Omega$ [Ref: V6.3.7] | **DDR5, Mobile AP** |
| **Low-end** | $> 98.0 \%$ [Ref: V6.3.7] | $> 5.0 \Omega$ [Ref: V6.3.7] | **Legacy MCU, Analog IC** |

### 2.1 PHYSICAL METROLOGY & THRESHOLDS

| Parameter Category | Physical Metric | V7.5.3 Target (High-end) | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **Probe Alignment**| Tip Accuracy | $< \pm 1.0 \mu\text{m}$ [Ref: V6.3.7] | $\pm 0.2 \mu\text{m}$ |
| **Test Frequency** | Signaling Speed | $> 2.0 \text{ Gbps}$ [Ref: V6.3.7] | $\pm 0.1 \text{ Gbps}$ |
| **Repair Yield** | Redundancy Eff. | $> 90 \%$ [Ref: V6.3.7] | $\pm 2 \%$ |
| **False Fail Rate**| Metrology Error | $< 0.1 \%$ [Ref: V6.3.7] | $\pm 0.05 \%$ |

### 2.2 COMPARATIVE PERFORMANCE ANALYSIS (THEORETICAL VS. VERIFIED)

| Parameter | Theoretical Limit | Verified Capability | Discrepancy Root Cause |
|:---|:---|:---|:---|
| **Probe Accuracy** | $< 0.5 \mu\text{m}$ | $\pm 1.0 \mu\text{m}$ [Ref: V6.3.7] | Mechanical Jitter/Thermal Expansion |
| **Contact Res. ($R_c$)** | $< 0.05 \Omega$ | $< 0.1 \Omega$ [Ref: V6.3.7] | Oxide Film Tunneling/Constriction |
| **Test Coverage** | $100.0 \%$ | $> 99.99 \%$ [Ref: V6.3.7] | Signal-to-Noise Floor/Metrology Limit |

## 3. ENGINEERING RATIONALE & FIDELITY LOGIC

### 3.1 YIELD MODELING: MURPHY-POISSON HYBRID MODEL
결함 밀도($D$)와 칩 면적($A$) 기반 수율 예측 시 결함 군집성(Clustering)을 반영한 보정 모델을 적용한다.
* **Mathematical Model**: 머피(Murphy) 모델 $Y = \left( \frac{1 - e^{-AD}}{AD} \right)^2$을 통해 대면적 High-end Tier 칩의 지수함수적 수율 하락 특성을 산출한다 [Ref: Murphy-Poisson Model].
* **FidelityEngine Logic**: 실시간 Defect Map 및 Particle 데이터를 융합하여 Yield Forecast를 수행하며, 예측 수율 $85\%$ [Ref: V6.3.7] 미만 시 Litho/Etch 공정에 즉각적인 보정 명령을 하달한다.

### 3.2 CONTACT INTEGRITY: PROBE-PAD FRICTION DYNAMICS
프로브 팁-패드 간 접촉 저항($R_c$)에 의한 신호 왜곡을 제어한다.
* **Mathematical Model**: 총 접촉 저항은 수축 저항과 산화막 터널링 저항의 합 $R_c = \frac{\rho}{2a} + \frac{\rho_f}{\pi a^2}$으로 정의된다 [Ref: Contact Resistance Physics]. $\rho_f$의 급증은 False Fail의 직접적 원인이 된다.
* **FidelityEngine Logic**: $R_c$의 1차 미분(Trend Analysis)을 통해 $0.1 \Omega$ [Ref: V6.3.7] 이상의 변동 포착 시 프로브 카드 온라인 세정(Cleaning)을 자동 가동한다.

## 4. DOMAIN KNOWLEDGE INGESTION REQUEST (DATA GAPS)
FidelityEngine의 결정론적 추론 완성을 위해 다음 데이터 보강이 요구된다.
* **REQ-01**: 고주파($> 2.0 \text{ GHz}$) 환경 내 Crosstalk/Reflection 기반 허위 에러 교차 맵.
* **REQ-02**: 누적 Touch-down 횟수 대비 Tip Wear-out 및 Z-axis Overdrive 하중 로그.
* **REQ-03**: 온도별 Wafer Burn-in 스트레스에 따른 $V_{th}$ Shift 및 영구 손상 임계치.

## 5. LOGIC ENGINE: TEST TIER & YIELD AUDITOR

```python
class SemiconTestFidelityEngine:
    """
    HDS-Gold V7.5.3: Semiconductor Test Tiering & Yield Diagnostic Engine
    """
    def __init__(self, target_tier='High-end'):
        self.TIER = target_tier
        self.COVERAGE_LIMIT = 0.9999 if target_tier == 'High-end' else 0.995

    def audit_test_integrity(self, coverage, contact_rc, yield_pct):
        # Tier-based fidelity scoring
        fidelity_score = (coverage / self.COVERAGE_LIMIT) * (yield_pct / 100.0)
        
        status = "OPTIMAL"
        if coverage < self.COVERAGE_LIMIT: 
            status = f"CRITICAL_TEST_COVERAGE_DEFICIT_{self.TIER}"
        elif contact_rc > 0.5 and self.TIER == 'High-end':
            status = "WARNING_CONTACT_RESISTANCE_HIGH"
            
        return {
            "tier_compliance": "PASS" if fidelity_score > 0.9 else "FAIL",
            "test_fidelity": max(fidelity_score, 0),
            "status": status
        }
```

## 6. SELF-AUDIT PROTOCOL
1. **KGD Integrity**: HBM 적층 공정 내 수율 곱의 법칙(Yield Product Rule)에 따른 손실 방지를 위해 Tier 1 무결성이 확보되었는가?
2. **WBI Stress**: Wafer Burn-In 온도 $20^\circ\text{C}$ 상향 시 Infant Mortality 가속화와 False Pass 감소율 간의 상관관계가 정의되었는가?
3. **Pattern Recognition**: Wafer Map 상의 'Donut Pattern'을 Etch Chuck 온도 불균일로 역산할 수 있는 로직이 존재하는가?