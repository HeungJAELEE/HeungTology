---
metadata:
  date: "2026-05-17"
  id: "[[[Battery] electrolyte-salt-precipitation]]"
  project: "Vault_Modernization"
  version: "v7.6.2_Modernized"
  domain: "02_Battery"

lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault / Thermal-Stability-Group"

dynamic:
  diagnostic_protocol:
    - "Standard_Verification"
  status: "Theoretical_Baseline"
  topology_policy: "Blueprint"

object:
  object_type: "Concept"
  tier: 1
  description: "전해질 시스템 내 화학적 포텐셜($\mu$) 불균형으로 인한 염($LiPF_6$)의 고체 결정 상전이(Salt Precipitation) 및 HF 생성 부식 메커니즘"

semantic:
  expected_queries:
    - "온도 하락에 따른 깁스 자유 에너지($\Delta G$) 변화가 염전출 핵생성(Nucleation)을 유도하는 수리적 기전은?"
    - "왈든의 법칙(Walden's Rule)에 근거하여 전해질 점도 상승이 이온 전도도 급감에 미치는 물리적 상관관계는?"
  tags: ["#염전출", "#LiPF6", "#왈든의법칙", "#화학적부식", "#HDS-Gold"]

spo_graph:
  - subject: "LiPF6 Solubility"
    predicate: "measured_value"
    object: "0.4 ~ 1.5 M"
    evidence: "[Ref: BAT-MAT-SALT-PRECIP-2026-V6] Section 1"
  - subject: "Ionic Conductivity"
    predicate: "measured_value"
    object: "1.0 ~ 12.0 mS/cm"
    evidence: "[Ref: BAT-MAT-SALT-PRECIP-2026-V6] Section 1"

trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Battery] electrolyte-salt-precipitation

## 1. 공학적 당위성: 화학적 평형 유지 (Why)
전해질 시스템 내 $LiPF_6$ 및 유기 용매 간의 화학적 평형(Chemical Equilibrium) 유지는 셀 안전성의 근간입니다. 염전출(Salt Precipitation)은 온도 하락 또는 농도 불균형에 따른 화학적 포텐셜($\mu$) 임계점 초과 및 고체 결정 상전이를 의미합니다. 이는 분리막 기공 폐쇄와 $HF$ 생성에 의한 화학적 부식을 유발하여 배터리 내부 안정성을 근본적으로 파괴합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| 파라미터 범주 (Category) | 물리적 지표 (Metric) | 목표 사양 (V7.6.2) | 공학적 의미 (Rationale) |
| :--- | :--- | :---: | :--- |
| **Solubility Limit**| $LiPF_6$ Conc. | $0.4 \sim 1.5 \text{ M}$ | 저온(-40C) 포화 농도 사수 |
| **Ionic Cond.** | $\sigma$ (Sigma) | $1.0 \sim 12.0 \text{ mS/cm}$ | 이온 수송 능력 하한선 |
| **Viscosity** | $\eta$ (Eta) | $1.0 \sim 10.0 \text{ cP}$ | 저온 유동성 안정 지표 |
| **Moisture Limit** | $H_2O$ Content | $< 20 \text{ ppm}$ | $HF$ 생성 억제 임계치 |
| **Acid Content** | $HF$ Conc. | $< 50 \text{ ppm}$ | 양극 격자 부식 방지 한계 |
| **Transference No.**| $t_+$ (Li-ion) | $0.3 \sim 0.4$ | 리튬 이온 선택적 기여도 |
| **Oxidation Pot.** | Stability Window| $> 4.5 \text{ V}$ | 고전압 분해 저항성 |

## 3. 핵심 공학 분석 (Scientific Rationale)
- **Gibbs Free Energy & Nucleation**: 염전출은 $\Delta G = -RT \ln(C / C_{sat})$ 모델을 따릅니다. 온도 하락 시 $C_{sat}$이 급감하여 $\Delta G < 0$ 상태가 되면 고체 결정 핵생성이 유도되며, 이는 분리막 굴곡도($\tau$)를 물리적으로 증가시켜 이온 통로를 차단합니다.
- **Walden's Rule**: 전해질의 점도($\eta$)와 이온 전도도($\sigma$) 간의 상관관계($\sigma \cdot \eta \approx \text{const.}$)를 정의합니다. 저온 환경에서의 점도 지수적 상승은 이온 전도도의 비선형적 급감을 초래하는 물리적 결정 인자입니다.

## 4. [Skill] Electrolyte Chemistry Engine
온도별 $LiPF_6$ 평형 용해도 곡선을 기반으로 현재 농도의 포화 지수(Saturation Index)를 산출하며, 염전출 임계점 도달 시 HF 생성 가속 및 내부 저항(DCR) 상승 폭을 예지하는 시뮬레이션 로직을 포함합니다.

## 5. 검증 프로토콜 (Audit)
1. **Solubility Audit**: 저온 챔버 테스트를 통해 특정 용매 배합비에서의 염 석출 시작 온도 실측 및 이론 모델 교차 검증.
2. **HF Generation Monitoring**: 전해액 내 수분 함량에 따른 시간별 $HF$ 농도 변화를 적정법(Titration)으로 실측하여 부식 리스크 평가.
3. **Viscosity Tracking**: 아레니우스 점도 관계식을 활용하여 저온 출력 제한(De-rating) 프로토콜의 수리적 정당성 확보.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] electrolyte-additives-and-interface-chemistry]]
- [[[Concept] battery-materials-and-chemistry-master-guide]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**
