---
metadata:
  id: "[[[Semiconductor] yield-management-and-defect-density-modeling]]"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Semiconductor] yield-management-and-defect-density-modeling에 관한 고밀도 지능 노드"
semantic:
  tags: ["#01_Semiconductor", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Semiconductor] yield-management-and-defect-density-modeling

## 1. 개요 (Objective)
본 노드는 반도체 제조의 최종 경제적 가치를 결정하는 수율 관리(Yield Management)를 다룹니다. 나노 단위의 결함 밀도($D_0$)를 제어하여 초기 공정의 낮은 수율을 양산 수준으로 끌어올리는 램프업 전략과 2026년 실측 데이터를 기반으로 한 수율 모델을 정의합니다 [[yield-log-v2026]].

## 2. 핵심 기술 사양 (Numerical Specs)

| 기술 파라미터 (Parameter) | 실측 목표 (Target) | 단위 | 공학적 의미 [Rationale] |
| :--- | :---: | :---: | :--- |
| **Weekly Yield** | **15 $\to$ 92** | % | 수율 램프업 곡선의 수리적 궤적 |
| **Defect Density ($D_0$)** | **< 0.05** | $/cm^2$ | 단위 면적당 치명 결함 수 (무결성) |
| **Learning Index ($b$)** | **0.3 ~ 0.5** | Factor | 누적 생산에 따른 수율 개선 효율 |
| **Chip Area ($A$)** | 0.5 ~ 2.5 | $cm^2$ | 결함 발생 확률 비례 상수 |
| **CPGD Cost** | **< 10.0** | USD | 다이당 제조 원가 및 수익성 지표 |
| **Cycle Time** | **< 1.5** | days/step | 공정 피드백 및 학습 주기 무결성 |
| **Critical Layers** | 60 ~ 120 | Count | 수율 영향 핵심 공정 층수 |
| **WPM Capacity** | 10k ~ 100k | Wafers | 팹 투입량 및 규모의 경제 지표 |

## 3. 핵심 수율 모델 및 수리 인과성

### 3.1 Poisson 및 Murphy 수율 모델
수율은 칩 면적($A$)과 결함 밀도($D_0$)의 지수 함수로 정의됩니다.
* **수리 모델**: $Y = e^{-A \cdot D_0}$. 칩 면적이 $1.5cm^2$일 때 $D_0$가 $0.05$를 초과하면 수율이 급격히 하락하는 임계 데이터를 실측했습니다 [[yield-log-v2026]].

### 3.2 학습 곡선(Learning Curve) 분석
누적 웨이퍼 투입량이 증가함에 따라 공정 노하우가 축적되어 수율이 향상되는 원리입니다.
* **실측 현상**: 학습 지수($b$)가 $0.3$ 미만으로 하락할 경우 구조적 결함(Systematic Defect) 발생으로 간주하며, 즉각적인 공정 포렌식을 가동하여 무결성을 회복합니다.

## 4. 임계 면적 분석(CAA) 및 Killer Defect 제어
모든 결함이 불량을 일으키지는 않으며, 배선 간격보다 큰 'Killer Defect'만을 선별하여 제어합니다.
* **실측 데이터**: GDS-II 설계 데이터와 결함 맵을 중첩 분석하여, 실제 수율 손실의 $80\%$가 상위 $20\%$의 핵심 공정 층에서 발생함을 입증했습니다 [[yield-log-v2026]].

## 5. [FidelityEngine] Yield Learning Diagnostic Class
```python
class YieldLearningFidelityEngine:
    def __init__(self, target_yield=92):
        self.target_yield = target_yield
        
    def audit_rampup(self, current_yield, d0_value, learning_index):
        # 수율 개선 속도 및 결함 밀도 무결성 진단
        if d0_value > 0.05:
            return "CRITICAL: High Defect Density - Check Cleanroom Integrity"
        if learning_index < 0.3:
            return "WARNING: Stagnant Learning - Identify Systematic Defects"
        if current_yield >= self.target_y:
            return "YIELD_MATURITY_REACHED: Transition to Mass Production"
        return "RAMP_UP_ON_TRACK"
```

**[V7.5.3_MODERNIZED]**
**[GROUNDED_VIA: semiconductor-fab-yield-ramp-up-log-v2026]**
**[REFERENCES: [[yield-log-v2026]], [[fab-economics-node]]]**
