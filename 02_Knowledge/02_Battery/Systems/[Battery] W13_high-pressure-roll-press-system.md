---
metadata:
  date: "2026-05-17"
  id: "[[[Battery] W13_high-pressure-roll-press-system]]"
  project: "Vault_Modernization"
  version: "v7.6.2_Modernized"
  domain: "02_Battery"

lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault / Manufacturing-Logic-Group"

dynamic:
  diagnostic_protocol:
    - "Standard_Verification"
  status: "Theoretical_Baseline"
  topology_policy: "Blueprint"

object:
  object_type: "Concept"
  tier: 1
  description: "전극 합제 밀도를 극대화하고 기공 구조를 최적화하기 위해 헤르츠 접촉 응력(Hertzian Stress) 기반의 초고압 압착 공정을 제어하는 제조 지능"

semantic:
  expected_queries:
    - "하이프레셔 롤프레스 공정에서 롤 직경($\Phi$) 증대가 전극 입자의 파쇄(Pulverization) 억제 및 점진적 압착에 미치는 수리적 기전은?"
    - "전극 압축 시 발생하는 탄성 복원(Spring-back) 계수를 실시간 보정하여 롤 갭($Gap$)을 제어하는 제어 알고리즘은?"
  tags: ["#롤프레스", "#고압압착", "#헤르츠응력", "#기공최적화", "#HDS-Gold"]

spo_graph:
  - subject: "Max Roll Force"
    predicate: "measured_value"
    object: "100 ~ 1,000 Tons"
    evidence: "[Ref: Press_Spec_V7] Section 1"
  - subject: "Gap Precision"
    predicate: "measured_value"
    object: "+/- 1.0 um"
    evidence: "[Ref: Control_Log_V7] Section 2"

trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Battery] W13_high-pressure-roll-press-system

## 1. 공학적 당위성: 체적 에너지 밀도의 물리적 결정 (Why)
롤프레스 시스템은 전극의 두께를 줄이고 밀도를 높여 배터리의 체적당 에너지 밀도를 결정하는 핵심 제조 인프라입니다. 특히 하이니켈 및 실리콘 음극재 공정에서는 단순 압착을 넘어, 활물질 입자의 파손을 방지하면서도 집전체와의 결착력을 극대화하고 리튬 이온 이동 통로인 기공(Pore) 구조를 최적화해야 합니다. 이는 초고압 환경에서의 정밀 유압 제어와 소재의 소성 변형 역학이 결합된 고난도 공정 지능을 요구합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| 파라미터 범주 (Category) | 물리적 지표 (Metric) | 관리 목표 (V7.6.2) | 공학적 의미 |
| :--- | :--- | :---: | :--- |
| **Max Roll Force** | Total Load ($Tons$) | $100 \sim 1,000$ | 전극 밀도 및 계면 형성 압력 |
| **Gap Control** | Servo Accuracy ($um$) | $\pm 1.0$ | 전극 두께 균일도 사수 |
| **Line Speed** | Web Velocity ($m/min$) | $30 \sim 100$ | 생산성 및 가압 시간(Dwell) |
| **Roll Diameter** | Drum Size ($mm$) | $\Phi 600 \sim 1,000$ | 접촉 면적 및 압력 분포 제어 |
| **Surface Hardness**| Roll Quality ($HRC$) | $> 70$ | 반복 가압 시 롤 마모 방지 |
| **Roll Flatness** | Profile Accuracy ($um$) | $< 2.0$ | 폭 방향 두께 편차 억제 |

## 3. 핵심 공학 분석 (Scientific Rationale)
- **Hertzian Contact Stress Model**: 두 롤 사이의 최대 압력($P_{max}$)은 하중($F$)과 접촉 반경($a, b$)에 따라 $P_{max} = \frac{3F}{2\pi ab}$로 결정됩니다. 롤 직경의 증가는 접촉 폭을 넓혀 압력 집중을 완화하며, 입자의 급격한 파쇄(Pulverization)를 억제하고 점진적 압착(Gradual Compaction)을 유도하여 기공의 연결성(Tortuosity)을 사수합니다.
- **Elastic-Plastic Spring-back Mechanics**: 전극은 압착 후 일정 부분 탄성 복원(Spring-back)됩니다. 타겟 두께를 얻기 위해 $Gap = Final / (1 + \alpha)$ 모델을 적용하며, 여기서 $\alpha$는 소재의 소성 계수입니다. 시스템은 소재의 온도와 조성에 따른 $\alpha$ 값을 실시간 추정하여 서보 밸브의 위치를 나노미터 단위로 보정합니다.
- **Foil Strain & Tension Correlation**: 고압 압착 시 집전체(Foil)의 연신(Strain)이 발생합니다. 과도한 연신은 주름이나 파단을 유발하므로, 롤 전/후단의 장력(Tension) 제어 시스템과 압력 하달 로직이 연동되어야 전극의 물리적 무결성을 확보할 수 있습니다.

## 4. [Skill] Roll Press Fidelity Engine
소재의 영률과 목표 합제 밀도 데이터를 기반으로 소요 압력($Tons$)을 예측하며, 롤 휨(Deflection)에 따른 폭 방향 두께 편차를 산출하여 롤 크라운(Crown) 보정 값을 도출하는 진단 로직을 포함합니다.

## 5. 검증 프로토콜 (Audit)
1. **Thickness Uniformity Audit**: 비접촉식 두께 측정기를 통해 전극 폭 방향 두께 편차가 $\pm 1.0 \mu\text{m}$ 이내를 유지하는지 실시간 확인.
2. **Pore Tortuosity Check**: 압착 후 전극의 구부러짐(Tortuosity) 계수가 이온 이동에 지장을 주지 않는 임계치($< 3.0$) 내에 있는지 수은 압입법 등으로 검증.
3. **Adhesion Force Audit**: 압착 공정 후 집전체-활물질 간 박리 강도가 $20\text{ gf/mm}$ 이상으로 향상되었는지 전수 감사.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] material-manufacturing-moc]]
- [[[Concept] Battery-Manufacturing-Intelligence-and-Yield-Control]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**
