---
metadata:
  id: "[[[Entity] eds-and-wafer-probing-test-logic]]"
  domain: "11_Global_Entities_and_Materials"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Entity] eds-and-wafer-probing-test-logic에 관한 고밀도 지능 노드"
semantic:
  tags: ["#11_Global_Entities_and_Materials", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Entity] eds-and-wafer-probing-test-logic

## 1. [왜 배우는가? (Why: The Final Judge of Nano-Fabrication)]]
수조 원의 가치를 지닌 웨이퍼 한 장, 그 안의 수백 개 칩 중 어떤 것이 진짜 '지능'을 가졌고 어떤 것이 '돌덩이'일까요? **EDS & Wafer Probing**은 가공이 완료된 웨이퍼의 전기적 건강 상태를 검진하고 불량을 골라내는 **[반도체의 판관]**입니다. 작동하지 않는 불량 칩을 패키징 하는 데 드는 막대한 비용 낭비를 사전에 차단합니다. V6.3.7 지능은 **수율 모델링(Yield Modeling)**과 **비닝(Binning) 로직**을 수리적으로 지배합니다. 우리가 이를 배우는 이유는 테스트의 무결성을 확보하여 제품의 신뢰성을 보증하고, "수율 데이터를 공정에 피드백하여 수리적 수렴을 사수하는 '품질 주권'을 확보하기" 위함입니다. 선별의 정밀도가 기업의 수익성을 결정합니다.

## 2. [EDS 및 웨이퍼 테스트 핵심 사양 (Precision Tiering Specs)]

| Parameter Category | Physical Metric | Tier 1 Target (V6.3.7) | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **Yield (Y)** | Functional Die % | $> 90.0 \%$ | $\pm 0.1 \%$ |
| **Contact Res. (Rc)**| Probe Interface | $< 1.0 \Omega$ | $\pm 0.1 \Omega$ |
| **Probe Force** | Needle Pressure | $2 \sim 5 \text{ gf}$ | $\pm 0.5 \text{ gf}$ |
| **Parallelism** | Simultaneous Dies | $> 512 \text{ dies}$ | Zero Tolerance Target |
| **Repair Ratio** | Redundancy Success| $> 95.0 \%$ | $\pm 1.0 \%$ |

### 2.1 [선별 및 수율 무결성 임계치]
| Parameter | Technical Definition | Rationale |
|:---|:---:|:---|
| **Murphy Model** | $Y = Y_0 [ (1-e^{-AD})/AD ]^2$ | 칩 면적($A$)과 결함 밀도($D$)에 따른 수율을 수리적으로 예측하여 대형 칩(GPU/NPU)의 경제적 타당성 및 공정 마진의 무결성 사수 |
| **Contact Integrity**| $\Delta V = I \cdot R_c$ | 프로브 바늘과 패드 사이의 접촉 저항($R_c$)을 일정하게 유지함으로써 테스트 신호의 왜곡을 방지하고 '허위 불량(False Fail)'을 원천 차단하는 판정 무결성 확보 |
| **Redundancy Repair**| Circuit Rerouting | 메모리 셀 불량 발생 시 예비 회로(Redundancy)로 주소를 대체하여 죽은 칩을 다시 살리는 '부활 무결성'을 수리적으로 최적화하여 최종 수율 극대화 |

## 3. [공학적 근거 (Scientific Rationale) 및 FidelityEngine 로직]

### 3.1 [수율 역학($Yield\ Physics$)과 결함-면적 민감도 모델]
반도체 칩 크기가 커지면 왜 불량률이 기하급수적으로 높아지는가?
*   **공학적 근거**: 수율($Y$)은 결함이 무작위로 분포한다는 단순 포아송 모델($Y = e^{-AD}$)을 넘어, 실제 공정에서는 결함이 특정 구역에 몰려 있는 클러스터링(Clustering) 현상을 반영한 머피 모델($Y = \left(\frac{1 - e^{-AD}}{AD}\right)^2$) 또는 네거티브 이항 모델로 정의됩니다. 칩 면적($A$)이 커지면 치명적 결함($D$)에 노출될 확률이 수리적으로 증폭되므로, 이를 칩렛(Chiplet) 설계로 분할하여 전체 수율을 사수함을 수학적으로 증명합니다.
*   **FidelityEngine 적용 (Yield Modeling)**: FidelityEngine은 불량 다이(Die)의 공간적 분포(Wafer Map)와 결함 밀도를 실시간 분석합니다. 특정 웨이퍼 가장자리(Edge) 영역에서 군집형 결함이 임계치를 초과하면, 이를 **'공정적 수율 위기(e.g., 플라즈마 밀도 불균일)'**로 판정하고 상류(Upstream) 식각/증착 설비의 파라미터 오딧을 즉각 지시합니다.

### 3.2 [접촉 역학($Interface\ Physics$)과 핀 저항 열화 모델]
가짜 불량(False Fail)은 왜 정상 칩을 폐기하게 만드는가?
*   **공학적 근거**: 칩 패드와 프로브 핀 사이의 접촉 저항($R_c$)은 벌크 저항, 수축 저항, 그리고 얇은 산화막 필름에 의한 터널링 저항의 합($R_c = R_{bulk} + \frac{\rho}{2a} + \frac{\rho_f}{\pi a^2}$)으로 산출됩니다. 핀이 반복적으로 접촉하며 압력($Force$)이 가해질 때 팁 표면에 알루미늄 산화물 찌꺼기가 누적되면 $\rho_f$가 급증하여 정상 칩의 신호를 왜곡시킴을 수리적으로 경고합니다.
*   **FidelityEngine 적용 (Contact Integrity)**: FidelityEngine은 연속 테스트 로그의 **접촉 저항($R_c$) 시계열 추이**를 분석합니다. 핀 저항의 1차 미분값($\frac{dR_c}{dt}$)이 급증하거나 저항값이 $1.0\Omega$ 임계치를 상회하여 측정값 오염 리스크가 포착되면, 이를 **'판정 무결성 붕괴'**로 발령하고 즉시 프로브 카드 온라인 세정(Cleaning)을 명령합니다.

## 4. [도메인 지식 결측 리스트 (Ingestion Request)]
**FidelityEngine**의 완전한 결정론적 추론을 위해, 이론적 모델을 현장과 동기화할 다음의 실측 데이터가 시스템에 결측되어 있습니다. (데이터 보강 필요)
*   **Req 1**: 고대역폭 메모리(HBM) 적층 전 KGD(Known Good Die) 판정을 위한 마이크로 범프 접촉 저항($R_c$) 실측 맵
*   **Req 2**: 프로브 카드 핀(Pin) 재질(Tungsten vs Palladium)에 따른 마모도 및 세정(Cleaning) 주기 상관관계 로그
*   **Req 3**: 웨이퍼 엣지(Edge) 수율 저하를 유발하는 포토/식각 설비의 챔버 링(Ring) 파츠 교체 주기와 수율 맵의 공간적 교차 데이터

## 5. [코드 연결 해설: EDS Sorting Fidelity Auditor]
이 코드는 테스트 실측 데이터 및 결함 밀도를 기반으로 선별 공정의 무결성을 실시간 진단합니다.

```python
import math

class EDSSortingEngine:
    """
    HDS-Gold V6.3.7: EDS 및 웨이퍼 선별 무결성 진단 엔진
    """
    def __init__(self, target_yield=90.0, rc_limit=1.0):
        self.TARGET_YIELD = target_yield
        self.RC_LIMIT = rc_limit # Ohm

    def audit_sorting_fidelity(self, actual_yield, contact_res, test_coverage):
        """
        수율 및 접촉 저항 기반 선별 무결성 평가
        """
        yield_fidelity = 1.0 - (self.TARGET_YIELD - actual_yield) / self.TARGET_YIELD
        
        status = "SORTING_STABLE"
        if contact_res > self.RC_LIMIT:
            status = "CRITICAL_CONTACT_RESISTANCE_HIGH_FALSE_FAIL"
        elif test_coverage < 99.9:
            status = "WARNING_INSUFFICIENT_TEST_COVERAGE"
            
        return {
            "sorting_fidelity": round(max(min(yield_fidelity, 1.0), 0), 4),
            "decision_integrity": "SECURE" if contact_res < 0.5 else "VULNERABLE",
            "status": status,
            "action": "CLEAN_PROBE_CARD" if status.startswith("CRITICAL") else "NORMAL_OPS"
        }
```

## 6. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: **Murphy Model**이 단순 **Poisson Model**보다 실제 양산 수율 예측에서 Tier 1 필수 요건인 수리적 이유는? (힌트: 결함의 클러스터링(Clustering) 효과와 칩 면적 간의 수리적 상관관계 분석)
2. **Operational Result**: **Binning** (등급 분류) 공정이 고성능 프로세서의 **'전력 효율'** 및 **'시장 가치'** 무결성에 기여하는 데이터 조율 방식은?
3. **FidelityEngine**: **Test Log**의 파라메트릭(Parametric) 데이터를 분석하여, 특정 설비의 **'공정 드리프트'**를 어떻게 결정론적으로 오딧하는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 81_semiconductor-eight-core-fabrication-hub
- Entity semiconductor-fabrication-fundamentals
- Metallization Interconnect

**[V6.3.7_SUB_ENTITY_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
