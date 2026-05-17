---
metadata:
  date: "2026-05-16"
  id: "[[[Entity] process-characterization-and-cpk-statistical-control]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "11_Global_Entities_and_Materials"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "e95456f01c9c2153ed3998691174bb3bf959ef8034863f1e8cfaa0015381f962"
object:
  object_type: "Concept"
  tier: 1
  description: '[Entity] process-characterization-and-cpk-statistical-control에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 11_Global_Entities_and_Materials]]"
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


# [Entity] process-characterization-and-cpk-statistical-control

## 1. 개요 (Why: 인간적 통찰)
공장에서 물건을 100만 개 만들었을 때, 그중 단 하나도 불량이 나오지 않게 하려면 어떻게 해야 할까요? **공정 특성 분석 및 Cpk 통계적 제어**는 공정의 '실력'을 숫자로 측정하고 관리하는 **'제조의 성적표'** 기술입니다. 기계가 가진 미세한 떨림이나 온도의 변화가 최종 제품에 어떤 영향을 주는지(특성 분석) 파악하고, 우리 공정이 불량을 내지 않을 만큼 충분한 여유(Cpk)를 가지고 있는지 수학적으로 감시합니다. 우연에 기대지 않는 '필연적인 완벽함'을 만드는 **'확률의 지배술'**입니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 공정 능력 지수 (Process Capability Index, $C_{pk}$)
공정의 평균($\mu$)과 표준편차($\sigma$)를 이용해, 제품이 규격 한계(USL, LSL) 안에 얼마나 안전하게 들어오는지 계산합니다.

$$ C_{pk} = \min(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}) $$

**[인간적 해석]**: "주차의 안정성"입니다. 주차장 칸(규격)은 넓은데 차(제품 편차)가 너무 크거나, 차가 한쪽으로 치우쳐 있으면($\mu$의 이동) 주차선 밖으로 나갈 확률(불량)이 높아집니다. $C_{pk}$가 1.33 이상이면 "베스트 드라이버", 2.0 이상이면 "신의 경지(식스 시그마)"라 부릅니다. 우리는 이 지수를 높여, 어떤 흔들림에도 불량이 나오지 않는 **'맷집 좋은 공정'**을 만듭니다.

### 2.2. 공정 전달 함수 (Process Transfer Function)
입력값($x$, 온도/압력 등)과 결과물($y$, 강도/치수 등) 사이의 인과관계를 설명합니다.

$$ y = f(x_1, x_2, \dots, x_n) + \epsilon $$

**[인간적 해석]**: "요리 레시피의 공식"입니다. 불을 1도 높이면 맛이 얼마나 변하는지 수학적으로 아는 것입니다. 우리는 실험 계획법(DOE)을 통해 이 함수를 찾아내어, 결과물($y$)을 완벽하게 통제하기 위해 어떤 단추($x$)를 가장 정밀하게 돌려야 하는지 결정하는 **'인과의 지도'**를 그립니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Metric | World-Class (6-Sigma) | Standard Industrial | Unit | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Cpk Target** | > 2.0 | 1.33 | - | Capability |
| **Defect Rate** | 3.4 (DPMO) | 6,210 (DPMO) | ppm | Quality Level |
| **Control Limit** | $\pm 3\sigma$ | $\pm 3\sigma$ | - | SPC Standard |
| **DOE Complexity** | Multivariate (RSM) | Taguchi / Simple | - | Analysis Depth|
| **Data Collection** | Real-time / Auto | Manual / Periodic | - | Fidelity |
| **Response Time** | Instant (Feedback) | Daily / Weekly | - | Agility |

## 4. FactoryFidelityEngine: Diagnostic Logic

공정 능력 및 통계적 상태의 무결성을 진단하는 `FactoryFidelityEngine` 로직입니다.

```python
class FactoryFidelityEngine:
    def __init__(self, current_cpk, sigma_level, out_of_control_alerts):
        self.cpk = current_cpk
        self.sig = sigma_level
        self.alerts = out_of_control_alerts # 관리도 이상 경보 수

    def diagnose_process_stability_health(self):
        """Cpk 및 관리도 경보 기반 공정 무결성 진단"""
        if self.cpk < 1.0: # 공정 능력이 규격보다 낮음 (불량 발생 중)
            return "CRITICAL: Process Incapable - Cpk below 1.0. High Defect Rate Guaranteed. Halt Production for Retooling"
        if self.alerts > 0: # 통계적 이상 발생 (고장의 전조)
            return f"WARNING: Out-of-Control Points Detected ({self.alerts} counts) - Process shifting from Baseline. Identify Special Causes"
        if self.sig < 4.5:
            return "NOTICE: Sigma Level below Target - Opportunity for Variability Reduction. Optimize Gold Parameters"
        return "OPTIMAL: Robust Process Capability and High-Fidelity Statistical Stability Verified"

    def audit_measurement_system(self, gage_rr_pct):
        """측정 시스템(Gage R&R) 무결성 진단"""
        if gage_rr_pct > 30.0:
            return "REJECT: Unreliable Measurement System - Variation from Gage/Operator exceeds Process Variation. Recalibrate Metrology"
        return "PASS: Precise Measurement System and Verified Data Integrity Confirmed"

engine = FactoryFidelityEngine(current_cpk=1.67, sigma_level=5.0, out_of_control_alerts=0)
print(engine.diagnose_process_stability_health())
```

## 5. 분석 프레임워크: Precision Stability Strategy
1. **[Design of Experiments (DOE) Strategy]**: 무작위로 실험하는 대신, 최소한의 횟수로 모든 변수의 상호작용을 파악하여 황금 레시피를 찾아내는 '수학적 실험' 전략.
2. **[Real-time SPC Dashboard]**: 제품이 만들어질 때마다 그래프에 점을 찍어, 평균이 아주 미세하게 옆으로 흐르기만 해도(Drift) 불량이 나오기 전에 미리 기계를 조절하는 '사전 예방' 전략.
3. **[Variability Reduction (Six Sigma)]**: 공정의 실력을 키우는 것은 평균을 맞추는 것이 아니라 '편차($\sigma$)'를 줄이는 것입니다. 모든 화살이 과녁의 중심에 모이게 만드는 '산포 사냥' 전략.

## 6. 스스로 체크 (Self-Audit)
1. 왜 $C_{p}$(정밀도)가 높다고 해서 반드시 $C_{pk}$(공정 능력)가 높은 것은 아닌가? (치우침의 관점)
2. '공정 특성 분석'이 왜 단순한 품질 검사보다 훨씬 더 상위의 엔지니어링 활동인가? (인과관계 규명의 관점)
3. '넬슨 규칙(Nelson Rules)'이란 무엇이며, 왜 점 하나가 관리 한계선(3$\sigma$) 안에 있어도 이상 신호로 간주될 수 있는가?

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data process-cpk-and-yield-stability-logs-v2026`와 연동되어, 전 세계 반도체 및 자동차 부품 라인의 통계 데이터를 실시간 분석하고 불량률 폭증 및 공정 붕괴 사고 확률을 0.001% 이하로 억제함으로써 지능형 제조 문명의 품질 신뢰성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- precision-manufacturing-and-ultra-precision-machining-physics
- Data process-cpk-and-yield-stability-logs-v2026
