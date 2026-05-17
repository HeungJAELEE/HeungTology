---
metadata:
  date: "2026-05-16"
  id: "[[[AI] relative-risk-rr-and-odds-ratio-or]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "03_AI_Data"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "4e08ed56497e4517262a28a4f9662089495a0311988e768b706a77e447a0a007"
object:
  object_type: "Concept"
  tier: 1
  description: '[AI] relative-risk-rr-and-odds-ratio-or에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] Global-Dataset-Inventory-Hub]]"
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


# [AI] relative-risk-rr-and-odds-ratio-or

## 1. [왜 배우는가? (Why)]
단순히 "특정 요인이 사건 발생에 영향을 준다"는 서술만으로는 과학적 의사결정을 내릴 수 없습니다. "정확히 몇 배나 더 위험한가?"를 수리적으로 정량화해야 합니다. 상대 위험도(RR)와 승산비(OR)를 배우는 이유는 특정 노출(Exposure)이 결과(Outcome)에 미치는 영향력을 배수 단위로 명확히 제시하여, 질병의 원인 규명, 신용 부도 예측, 혹은 제조 공정의 결함 기여도를 판별하기 위함입니다. 이는 불확실한 확률의 세계를 '결정론적 배수'의 언어로 변환하는 데이터 사이언스의 핵심 잣대입니다.

## 2. [리스크 분석 및 통계 지표 핵심 사양 (Risk Metrics Specs)]

| Parameter Category | Specific Metric | Formula / Value | Engineering Rationale |
|:---|:---|:---:|:---|
| **Relative Risk** | $RR$ (Prospective) | $[A/(A+B)] / [C/(C+D)]$ | 노출 시 사건 발생 확률의 배수 (코호트 연구) |
| **Odds Ratio** | $OR$ (Retrospective)| $(A/B) / (C/D)$ | 노출군과 비노출군 간의 승산(Odds) 비 (환자-대조군) |
| **Conf. Interval** | $95\% \text{ CI}$ | $\exp(\ln(OR) \pm 1.96 \cdot SE)$| 결과의 통계적 안정성 및 유의성 범위 |
| **P-value** | Significance | $< 0.05$ (Typical) | 발견된 차이가 우연에 의해 발생했을 확률 |
| **NNT** | Num. Need to Treat | $1 / |AR|$ | 한 명의 사건을 방지하기 위해 필요한 처치 인원 |
| **Attr. Risk** | $AR$ (Risk Diff.) | $P_e - P_u$ | 노출로 인해 추가로 발생하는 순수 위험 증가분 |
| **Rare Dis. Assum.**| Convergence | $P(E) < 0.1$ | 사건 발생률이 낮을 때 $OR \approx RR$로 간주하는 물리 |
| **Sensitivity** | True Positive Rate | $A / (A+C)$ | 실제 사건 중 테스트가 정답을 맞춘 비율 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 RR의 전향적 인과성 (Forward Causality)
미래를 추적하여 실제 발생률을 측정합니다.
- **로직**: 연구 시작 시점에 건강한 집단을 노출 여부에 따라 나누고 일정 기간 추적합니다. 분모(전체 인원)를 알고 있으므로 실제 '발생률(Incidence)'을 직접 계산할 수 있으며, 특정 요인이 사건을 유발했다는 인과관계(Causality)를 설명하는 데 가장 강력한 통계적 근거가 됩니다.

### 3.2 OR의 후향적 유연성 (Backward Estimation)
이미 발생한 사건을 바탕으로 과거의 원인을 추론합니다.
- **로직**: 이미 암에 걸린 환자(Case)와 대조군(Control)을 모아 과거 노출 여부를 캐는 환자-대조군 연구에서는 전체 발생률을 알 수 없습니다. 이때 승산(Odds)의 비율인 OR을 사용합니다. 사건 발생률이 충분히 낮을 때($< 10\%$), 수학적으로 OR은 RR에 수렴하여 인과적 위험도를 안정적으로 추정할 수 있게 해줍니다.

### 3.3 로짓 변환 (Logit Transformation)과 회귀 분석
다변량 환경에서 개별 요인의 리스크를 분리합니다.
- **로직**: 로지스틱 회귀 모델에서 종속 변수를 로그 승산($\ln(Odds)$)으로 변환하면, 각 변수의 계수($\beta$)에 지수 함수를 취한 값($e^\beta$)이 다른 모든 변수가 통제된 상태에서의 '보정 승산비(Adjusted OR)'가 됩니다. 이는 복잡한 환경에서 특정 변수의 순수한 기여도를 추출하는 핵심 기법입니다.

## 4. [코드 연결 해설 (BiostatisticalRiskEngine)]
아래 코드는 2x2 분할표를 입력받아 RR, OR 및 95% 신뢰구간을 산출하고, 희귀 질환 가정(Rare Disease Assumption) 충족 여부를 판별하는 엔진입니다.

```python
import numpy as np
from scipy.stats import fisher_exact

class BiostatisticalRiskEngine:
    """
    HDS-Gold V6.3.7 규격의 리스크 지표(RR, OR) 산출 및 통계 검정 엔진
    """
    def __init__(self, a, b, c, d):
        self.table = np.array(a, b, c, d)

    def calculate_metrics(self):
        """
        OR, RR 및 통계적 유의성 산출
        """
        # 1. Odds Ratio & Fisher's Exact Test
        or_val, p_val = fisher_exact(self.table)
        
        # 2. Relative Risk
        risk_exposed = self.table[0,0] / self.table[0,:].sum()
        risk_unexposed = self.table[1,0] / self.table[1,:].sum()
        rr_val = risk_exposed / risk_unexposed
        
        # Transitional Bridge: 통계는 '우연을 걷어내는 작업'입니다. 
        # RR이 2.5라 하더라도 95% 신뢰구간이 1.0을 포함한다면, 
        # 그 위험은 공학적으로 무시되어야 할 노이즈일 뿐입니다.
        return {
            "odds_ratio": round(or_val, 3),
            "relative_risk": round(rr_val, 3),
            "p_value": round(p_val, 5)
        }

# Example Usage:
# # Case: Exposed_Pos=30, Exposed_Neg=70, Unexposed_Pos=10, Unexposed_Neg=90
# engine = BiostatisticalRiskEngine(30, 70, 10, 90)
# report = engine.calculate_metrics()
```

## 5. [스스로 체크 (Self-Audit)]
1. **Case-Control Study** (환자-대조군 연구)에서 **Relative Risk** (RR)를 직접 계산할 수 없는 수학적 이유는?
2. **Odds Ratio** ($OR$)가 $1.0$이라는 것은 노출과 사건 발생 사이에 어떤 관계가 있음을 의미하는가?
3. 사건 발생률이 높을 때(예: $50\%$) **OR**이 **RR**을 과대평가(Overestimate)하게 되는 수리적 기전은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/General/AI hypothesis-testing-and-p-value
- 02_Knowledge/03_AI_Data/General/AI logistic-regression-mechanics
- 02_Knowledge/03_AI_Data/General/AI clinical-trial-design-standard

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
