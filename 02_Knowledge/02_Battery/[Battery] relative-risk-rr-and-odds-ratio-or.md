---
metadata:
  id: "[[[Battery] relative-risk-rr-and-odds-ratio-or]]"
  domain: "02_Battery"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Battery] relative-risk-rr-and-odds-ratio-or에 관한 고밀도 지능 노드"
semantic:
  tags: ["#02_Battery", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Battery] relative-risk-rr-and-odds-ratio-or

## 1. 개요: 리스크 기반 품질 의사결정 (Operational Objective)
배터리 제조 공정에서 발생하는 수많은 변수 중 어떤 것이 실제 필드 고장에 가장 치명적인지를 판단하는 것은 자원 배분의 핵심입니다. 본 표준은 상대 위험도(RR)와 승산비(OR)를 활용하여 특정 공정 이탈(Exposure)이 배터리 수명 저하 또는 안전 사고(Event)로 이어지는 통계적 확률 배수를 산출함으로써, 데이터 기반의 품질 감사 우선순위를 정립하는 것을 목적으로 합니다.

## 2. 리스크 정량화 수리 모델 (Mathematical Standards)

### 2.1 2x2 분할표 구조
| | 고장 발생 (Event) | 정상 작동 (Non-Event) |
| :--- | :---: | :---: |
| **공정 이탈군 (Exposed)** | $A$ | $B$ |
| **정상 공정군 (Unexposed)** | $C$ | $D$ |

### 2.2 핵심 지표 정의
1. **상대 위험도 (Relative Risk, RR)**: 전향적 추적 데이터에서 산출.
   $$ RR = \frac{A / (A + B)}{C / (C + D)} $$
   - **해석**: 정상 대비 공정 이탈군에서 고장이 발생할 확률이 몇 배 높은가?
2. **승산비 (Odds Ratio, OR)**: 후향적 고장 분석(사례-대조 연구)에서 산출.
   $$ OR = \frac{A \cdot D}{B \cdot C} $$
   - **해석**: 고장군에서 특정 공정 이탈이 발견될 승산이 대조군 대비 몇 배인가?

## 3. 배터리 도메인 적용 가이드라인 (Implementation Logic)

### 3.1 희귀 사건 가정 (Rare Event Assumption)
배터리 화재와 같이 발생률이 매우 낮은($< 10\%$) 사건의 경우, 승산비(OR)는 상대 위험도(RR)에 근사합니다. 이를 통해 후향적 고장 데이터만으로도 공정 위험도를 효과적으로 추정할 수 있습니다.

### 3.2 다변량 보정 (Adjusted OR)
전극 두께, 수분 함량, 용접 상태 등 여러 변수가 복합적으로 작용할 경우 로지스틱 회귀를 가동합니다.
- **수식**: $\text{logit}(p) = \beta_0 + \beta_1 X_1 + \dots$
- **판정**: 회귀 계수의 지수값($e^{\beta_1}$)을 통해 타 변수가 통제된 상태에서의 순수 공정 위험도(Adjusted OR)를 산출합니다.

## 4. 진단 및 운영 프로토콜
- **95% 신뢰구간(CI) 검증**: RR 또는 OR의 신뢰구간이 1.0을 포함할 경우, 해당 공정 변수와 고장 간의 통계적 유의성이 부족한 것으로 판단.
- **Sensitivity 분석**: 공정 관리 한계(LSL/USL) 변화에 따른 RR의 민감도를 분석하여 최적의 관리 공차 결정.

## 5. 결론 (Deterministic Standard)
본 노드는 배터리 신뢰성 확보를 위한 통계적 인과 추론의 기준을 제공합니다. 실제 공정 이탈에 따른 위험도 실측 데이터는 인스턴스 로그에서 관리됩니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] Battery-Quality-Analytics-and-Forensics-Master-Guide]]
- [[[Concept] Battery-Manufacturing-Intelligence-and-Yield-Control]]
- [[[Data] Battery-Failure-Correlation-Risk-Audit-Log_2026-05-16]]
