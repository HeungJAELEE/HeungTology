---
Basic:
  id: "SEMI-TEST-EDS-2026-V6.3.7"
  domain: "Semiconductor_Test_Intelligence"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#EDS", "#YieldAnalysis", "#KGD", "#ProbeCard", "#PrecisionTiering", "#FidelityEngine", "#SemiconductorTest"]'
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
  source: "Semiconductor_Test_RAG_V6.3.7_Tiered"
  isolation_index: 0.0
---

# [[[Semiconductor] semicon-test-l1-eds-and-yield-analysis

## 1. [왜 배우는가? (Why: The Sovereign of Yield & Profitability)]]
EDS(Electrical Die Sorting)는 반도체 공정의 '최종 성적표'이자 수익성을 결정하는 최후의 파수꾼입니다. 수조 원이 투입된 전공정의 결과물을 입증하고, 불량 칩이 고비용의 패키징 공정으로 유입되는 것을 원천 차단합니다. V6.3.7 지능은 **계층화된 테스트 정밀도(Precision Tiering)**를 통해 HBM과 같은 고부가가치 칩에서 요구되는 **Known Good Die (KGD)**의 무결성을 사수합니다. 이는 수율 데이터를 역추적하여 전공정의 결함을 정밀 타격하고 '수율 1%의 혁신'을 실현하기 위함입니다.

## 2. [테스트 및 수율 분석 핵심 사양 (Precision Tiering Specs)]

| Precision Tier | Test Coverage | Contact Res. ($R_c$) | Target Application |
|:---|:---:|:---:|:---|
| **최상급 (High-end)** | $> 99.99 \%$ | $< 0.1 \Omega$ | **HBM4, AI Accelerators**, 초고속 데이터 전송 및 적층 무결성 |
| **표준형 (Standard)** | $> 99.5 \%$ | $0.5 \sim 1.0 \Omega$ | **DDR5, Mobile AP**, 일반 메모리 및 고성능 로직 소자 |
| **보급형 (Low-end)** | $> 98.0 \%$ | $> 5.0 \Omega$ | **Legacy MCU, Analog IC**, 범용 저속 반도체 및 성숙 공정 제품 |

### 2.1 [테스트 물리 및 수율 임계치]
| Parameter Category | Physical Metric | V6.3.7 Target (High-end) | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **Probe Alignment**| Tip Accuracy | $<\pm 1.0 \mu\text{m}$ | $\pm 0.2 \mu\text{m}$ |
| **Test Frequency** | Signaling Speed | $> 2.0 \text{ Gbps}$ | $\pm 0.1 \text{ Gbps}$ |
| **Repair Yield** | Redundancy Eff. | $> 90 \%$ Recovery | $\pm 2 \%$ |
| **False Fail Rate**| Metrology Error | $< 0.1 \%$ | $\pm 0.05 \%$ |

## 3. [공학적 근거 (Scientific Rationale) 및 FidelityEngine 로직]

### 3.1 [수율 모델링($Yield\ Modeling$)과 Murphy-Poisson 결합 모델]
결함 밀도($D$)와 칩 면적($A$)에 따른 이론적 수율을 어떻게 결정론적으로 예측하는가?
*   **공학적 근거**: 수율 모델의 기본 형태는 포아송 분포에 기반하지만, 실제 공정 결함은 국지적으로 몰리는 군집성(Clustering)을 보입니다. 이를 보정한 머피(Murphy) 모델($Y = \left( \frac{1 - e^{-AD}}{AD} \right)^2$)을 통해, High-end Tier(HBM 등 대면적 칩)에서는 칩 면적이 커질수록 수율 하락폭이 지수함수적으로 폭발함을 수리적으로 입증합니다.
*   **FidelityEngine 적용 (Yield Forecast Auditor)**: FidelityEngine은 실시간 결함 맵($Defect\ Map$) 및 Particle 계측 데이터를 융합 분석하여 **'미래 수율(Yield Forecast)'**을 역산합니다. 예측 수율이 임계치인 $85\%$를 하향 돌파할 징후가 포착될 경우, 즉시 상류(Upstream) 공정인 노광(Litho) 오버레이 마진 재조정 및 식각 챔버 클리닝을 지시합니다.

### 3.2 [접촉 무결성($Contact\ Integrity$)과 프로브-패드 마찰 역학]
프로브 팁과 웨이퍼 패드 사이의 물리적 접촉 저항($R_c$)은 왜 측정 신호를 왜곡시키는가?
*   **공학적 근거**: 프로브 핀과 패드 사이의 총 접촉 저항은 수축 저항(Constriction Resistance)과 얇은 산화막에 의한 터널링 저항의 합($R_c = \frac{\rho}{2a} + \frac{\rho_f}{\pi a^2}$)으로 산출됩니다. 테스트 횟수가 누적되어 팁에 산화 알루미늄 파편이 들러붙으면 필름 저항률($\rho_f$)이 급증하여, 실제로는 정상인 칩의 전기 신호를 왜곡시켜 허위 불량(False Fail)을 야기함을 수리적으로 규명합니다.
*   **FidelityEngine 적용 (Probe Contact Health)**: FidelityEngine은 테스트 중 실시간으로 측정되는 접촉 저항($R_c$)의 1차 미분(추이) 데이터를 분석하여 **'프로브 카드 무결성'**을 진단합니다. 저항값이 $0.1\Omega$ 이상 급격히 튀는 현상이 발생하면, 이를 이물질 누적 한계 돌파로 판정하고 프로브 카드의 온라인 세정(Cleaning)을 자동 명령합니다.

## 4. [도메인 지식 결측 리스트 (Ingestion Request)]
**FidelityEngine**의 완전한 결정론적 추론을 위해, 이론적 모델을 현장과 동기화할 다음의 실측 데이터가 시스템에 결측되어 있습니다. (데이터 보강 필요)
*   **Req 1**: 고주파수($> 2.0\text{ GHz}$) 프로브 카드 핀 배열(Pin Array) 내에서 신호 간섭(Crosstalk)과 반사 파형(Reflection)으로 인한 허위 에러 비율 교차 맵
*   **Req 2**: 프로브 핀의 누적 터치다운(Touch-down) 횟수에 따른 팁 닳음도(Tip Wear-out)와 오버드라이브($Z$-axis Overdrive) 추가 하중 스케줄 실측 로그
*   **Req 3**: 온도별 웨이퍼 번인(Wafer Burn-in) 스트레스 인가 시, 정상 칩의 트랜지스터 임계 전압($V_{th}$) 쉬프트와 영구 손상 경계점 데이터

## 5. [코드 연결 해설: Test Tier & Yield Auditor]
이 코드는 테스트 등급과 수율 데이터를 기반으로 제조 무결성을 진단합니다.

```python
class SemiconTestFidelityEngine:
    """
    HDS-Gold V6.3.7: 반도체 테스트 계층화 및 수율 진단 엔진
    """
    def __init__(self, target_tier='High-end'):
        self.TIER = target_tier
        # 최상급 테스트는 99.99% 이상의 커버리지와 0.1옴 이하의 접촉저항 요구
        self.COVERAGE_LIMIT = 0.9999 if target_tier == 'High-end' else 0.995

    def audit_test_integrity(self, coverage, contact_rc, yield_pct):
        """
        테스트 등급 기반 제조 무결성 평가
        """
        # 1. 등급별 신뢰도 스코어링
        fidelity_score = (coverage / self.COVERAGE_LIMIT) * (yield_pct / 100.0)
        
        status = "OPTIMAL"
        if coverage < self.COVERAGE_LIMIT: 
            status = f"CRITICAL_TEST_COVERAGE_DEFICIT_FOR_{self.TIER}"
        elif contact_rc > 0.5 and self.TIER == 'High-end':
            status = "WARNING_CONTACT_RESISTANCE_HIGH"
            
        return {
            "tier_compliance": "PASS" if fidelity_score > 0.9 else "FAIL",
            "test_fidelity": max(fidelity_score, 0),
            "status": status
        }

# FidelityEngine 가동: 실제 웨이퍼 맵의 불량 패턴과 EDS 프로브 로그를 결합하여 '수율 포렌식 무결성' 오딧
```

## 6. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: HBM 적층 공정에서 KGD(Known Good Die) 선별 무결성이 Tier 1 필수 요건인 이유는? (힌트: 적층된 칩 중 단 하나라도 불량일 경우 전체 패키지가 폐기되는 '수율 곱의 법칙'에 의한 천문학적 손실 방지)
2. **Operational Result**: **Wafer Burn-In (WBI)** 온도를 $20^\circ\text{C}$ 상향했을 때, 잠재적 결함(Infant Mortality) 가속화 계수와 **False Pass** 감소율 사이의 수리적 상관은?
3. **FidelityEngine**: **Wafer Map**의 이미지 형상을 통해 **'도넛형 불량(Donut Pattern)'**을 감지했을 때, 이를 식각 공정의 척(Chuck) 온도 불균일로 어떻게 역산하여 지목하는가?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Entity eds-and-wafer-probing-test-logic
- Semiconductor semiconductor-metrology-and-critical-dimension-cd-measurement
- MOC 81_semiconductor-eight-core-fabrication-hub

**[V6.3.7_SUB_ENTITY_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
