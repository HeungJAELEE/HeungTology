---
lineage:
  dataset_reference: Six Sigma Quality Standards (ASQ/ANSI)
  original_author: Antigravity Vault
  original_hash: 4a033de31e045fd6c694e3215f73935f209bbda822ffd1ce7e0ba76bce54f2b1
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-20'
  domain: 09_SmartFactory_Production
  id: '[[[09_SmartFactory_Production] [Concept] rolled-throughput-yield-mathematical-derivation]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r3
  version: v7.9_Enterprise_Node
object:
  description: 누적 공정 합격률(Rolled Throughput Yield, RTY)의 수학적 유도 및 다단계 제조 공정에서의 신뢰도
    모델링 이론
  object_type: Concept
  tier: 1
properties:
  dpu_i_base_value: 0.005
  dpu_i_control_limit:
  - 0.0
  - 0.15
  fpy_base_value: 0.98
  fpy_control_limit:
  - 0.7
  - 1.0
  k_process_stages_base: 10.0
  k_process_stages_control_limit:
  - 1.0
  - 50.0
  rty_base_value: 0.951
  rty_control_limit:
  - 0.5
  - 1.0
  ty_i_base_value: 0.995
  ty_i_control_limit:
  - 0.85
  - 1.0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Section 14.2'
  intent: mathematical_derivation
  object: RTY = \prod_{i=1}^{k} Y_i = e^{-DPU_{total}}
  predicate: has_mathematical_formula
  subject: rolled-throughput-yield
  weight: 0.95
- evidence_coordinate: '[데이터 부재] Section 14.2'
  intent: comparative_analysis
  object: first-pass-yield
  predicate: is_more_stringent_than
  subject: rolled-throughput-yield
  weight: 0.85
temporal:
  valid_from: '2026-05-20T12:52:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Rolled Throughput Yield Mathematical Derivation (누적 공정 합격률의 수학적 유도)

## 1. [왜 배우는가? (Why)]
다단계 제조 공정(Multi-stage Manufacturing Process)에서 각 공정 단계의 개별 합격률을 단순 평균하거나 최종 단계의 FPY(First Pass Yield)만을 측정하는 것은 전체 공정의 실제 품질 비용과 숨은 공장(Hidden Factory)의 손실을 심각하게 왜곡합니다. 
예를 들어, 10개의 공정 단계를 거치는 사출 성형 및 조립 라인에서 각 단계의 합격률이 $99.0\%$일 때, 전체 공정을 무결점 상태로 통과하여 완제품이 될 확률은 단순 직관보다 훨씬 낮아집니다.
누적 공정 합격률($RTY$, Rolled Throughput Yield)은 제품이 공정의 첫 단계부터 마지막 단계까지 재작업(Rework)이나 폐기(Scrap) 없이 단 한 번에 합격으로 통과할 확률을 수학적으로 모델링합니다. 
이를 통해 재작업 루프에 가려진 품질 비용(COPQ)을 정확히 산출하고 공정 개선의 우선순위를 정밀하게 타격하기 위해 본 수학적 모델을 학습하고 이식합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
RTY 수학적 유도 및 검증 모델의 설계를 위한 기본 매개변수 사양은 다음과 같습니다.

| 파라미터명 | 설명 | 기준값 | 제어 한계 | 단위 | 적용 공식 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $k$ | 공정 단계의 총 수 (Process Stages) | $10.0$ | $1.0 \sim 50.0$ | $\text{ea}$ | - |
| $TY_i$ | $i$번째 공정의 Throughput Yield | $0.995$ | $0.850 \sim 1.000$ | $\text{ratio}$ | $TY_i = \frac{N_{in,i} - N_{scrap,i}}{N_{in,i}}$ |
| $DPU_i$ | $i$번째 공정의 단위당 결함 수 | $0.005$ | $0.000 \sim 0.150$ | $\text{defects/unit}$ | $DPU_i = \frac{D_i}{U_i}$ |
| $RTY$ | 전체 누적 공정 합격률 | $0.951$ | $0.500 \sim 1.000$ | $\text{ratio}$ | $RTY = \prod_{i=1}^{k} TY_i$ |
| $FPY$ | 단순 초도 합격률 (First Pass Yield) | $0.980$ | $0.700 \sim 1.000$ | $\text{ratio}$ | $FPY = \frac{N_{in} - N_{scrap} - N_{rework}}{N_{in}}$ |

## 3. [공학적 원리 및 수식 유도 (Scientific Rationale)]

### 3.1 Throughput Yield ($TY$)와 Defects Per Unit ($DPU$)의 수리적 관계
각 단일 공정 단계 $i$에서 발생하는 결함의 분포는 푸아송 분포(Poisson Distribution)를 따른다고 가정합니다. 단위 제품당 평균 결함 수를 $DPU_i$라고 정의할 때, 제품 1개당 결함이 정확히 $x$개 발생할 확률 $P(x)$는 다음과 같이 기술됩니다.

$$P(x) = \frac{e^{-DPU_i} \cdot (DPU_i)^x}{x!}$$

여기서 제품에 결함이 전혀 존재하지 않아($x = 0$) 재작업이나 스크랩 없이 합격할 확률이 바로 처리량 합격률 $TY_i$가 됩니다.

$$TY_i = P(0) = \frac{e^{-DPU_i} \cdot (DPU_i)^0}{0!} = e^{-DPU_i}$$

### 3.2 Rolled Throughput Yield ($RTY$)의 누적 곱 유도
전체 공정이 $k$개의 독립적인 직렬 단계로 구성되어 있다고 할 때, 임의의 단위 제품이 전체 라인을 무결점으로 통과할 총 확률인 $RTY$는 각 공정 단계별 처리량 합격률 $TY_i$의 곱으로 정의됩니다.

$$RTY = TY_1 \times TY_2 \times \dots \times TY_k = \prod_{i=1}^{k} TY_i$$

위 식에 $TY_i = e^{-DPU_i}$ 관계식을 대입하여 유도하면 다음과 같습니다.

$$RTY = \prod_{i=1}^{k} e^{-DPU_i} = e^{-DPU_1} \cdot e^{-DPU_2} \dots e^{-DPU_k} = e^{-\sum_{i=1}^{k} DPU_i}$$

여기서 전체 누적 단위당 결함 수 $DPU_{total} = \sum_{i=1}^{k} DPU_i$로 정의되므로, 최종 RTY 공식은 다음과 같이 유도됩니다.

$$RTY = e^{-DPU_{total}}$$

### 3.3 First Pass Yield ($FPY$)와의 수리적 차이 및 Hidden Factory 모델링
단순 초도 합격률 $FPY$는 공정 내부의 재작업을 무시하고 오직 투입량 대비 스크랩과 최종 검사 전 재작업 처리된 수량을 단순 제외하여 산출하므로, 공정 내부에서 소모되는 인건비, 설비 가동 시간, 재작업 원자재 손실을 정밀하게 반영하지 못합니다. 
반면 $RTY$는 각 단계의 결함 발생률($DPU$)에 물리적으로 종속되어 있으므로 아래와 같은 관계식을 통해 '숨은 공장(Hidden Factory)'의 스크랩 및 재작업 효율성을 완벽히 포착합니다.

$$RTY \le FPY$$

공정 내 재작업 루프가 활성화되어 있을 때 두 지표 간의 편차는 더욱 벌어지며, 품질 격차는 $\Delta Y = FPY - RTY$로 정량화됩니다.

## 4. [진단 코드 (Diagnostic Code)]
다단계 제조 공정의 각 단계별 투입량, 폐기량, 재작업량 및 결함 수를 기반으로 FPY와 RTY를 산출하고 숨은 공장의 손실을 진단하는 Python 시뮬레이션 모듈입니다.

```python
import numpy as np

class ProcessYieldAnalyzer:
    def __init__(self, stages_data):
        """
        stages_data: list of dicts containing stage parameters:
                     [{'name': str, 'input': int, 'scrap': int, 'rework': int, 'defects': int}]
        """
        self.stages_data = stages_data

    def analyze_yield(self):
        rty = 1.0
        total_dpu = 0.0
        results = []

        for idx, stage in enumerate(self.stages_data):
            n_in = float(stage['input'])
            n_scrap = float(stage['scrap'])
            n_rework = float(stage['rework'])
            n_defects = float(stage['defects'])

            # Throughput Yield (TY) calculation
            ty = (n_in - n_scrap) / n_in if n_in > 0 else 0.0
            
            # Defects Per Unit (DPU) calculation
            dpu = n_defects / n_in if n_in > 0 else 0.0
            
            # FPY calculation for the stage
            fpy = (n_in - n_scrap - n_rework) / n_in if n_in > 0 else 0.0

            rty *= ty
            total_dpu += dpu

            results.append({
                'stage': stage['name'],
                'TY': ty,
                'DPU': dpu,
                'FPY': fpy
            })

        calculated_rty_via_dpu = np.exp(-total_dpu)

        return {
            'stage_metrics': results,
            'calculated_RTY_product': rty,
            'calculated_RTY_exponential': calculated_rty_via_dpu,
            'total_DPU': total_dpu
        }

# Example validation execution
if __name__ == "__main__":
    mock_stages = [
        {'name': 'Injection Molding', 'input': 1000, 'scrap': 5, 'rework': 20, 'defects': 30},
        {'name': 'Cooling & Trimming', 'input': 995, 'scrap': 2, 'rework': 10, 'defects': 15},
        {'name': 'Visual Inspection', 'input': 993, 'scrap': 3, 'rework': 5, 'defects': 8}
    ]
    analyzer = ProcessYieldAnalyzer(mock_stages)
    report = analyzer.analyze_yield()
    print(f"Cumulative RTY (Product): {report['calculated_RTY_product']:.6f}")
    print(f"Cumulative RTY (e^-DPU): {report['calculated_RTY_exponential']:.6f}")
    print(f"Total Process DPU: {report['total_DPU']:.6f}")
```

## 5. [스스로 체크 (Self-Audit)]
1. **$RTY = e^{-DPU_{total}}$** 유도 시, 각 공정 단계 간의 결함 발생이 서로 독립적이라는 가정이 만족되지 않을 경우(예: 전단계의 사출 불량이 후단계 조립 불량의 직접적 원인이 될 때) RTY 예측 모델의 오차를 보정하기 위한 수리적 대안은 무엇인가?
2. **Hidden Factory**의 손실을 방지하기 위해 공정 제어 관점에서 $RTY$와 $FPY$의 편차($\Delta Y$)를 최소화하기 위한 구체적인 IATF 16949 표준 프로세스는 무엇인가?
3. 공정 수가 $k = 50$으로 매우 크고 각 단계의 $DPU$가 극히 작아 $TY \approx 1.0$일 때, 부동소수점 언더플로우를 방지하면서 정합성 높은 $RTY$를 계산하기 위해 로그 공간 연산($\ln RTY = -\sum DPU_i$)을 적용하는 알고리즘적 이점은 무엇인가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]`
- `[[[Entity] statistical-process-control-spc-and-control-chart-logic]]`
- `[[[Entity] iatf-16949-automotive-quality-management-and-zero-defect-logic-entity]]`
- `[[[Data] manufacturing-mes-quality-inspection-results-v2026]]`