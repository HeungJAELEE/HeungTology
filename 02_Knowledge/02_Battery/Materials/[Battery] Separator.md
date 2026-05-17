---
metadata:
  date: "2026-05-17"
  id: "[[[Battery] Separator]]"
  project: "Vault_Modernization"
  version: "v7.6.2_Modernized"
  domain: "02_Battery"

lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault / Separator-Science-Group"

dynamic:
  diagnostic_protocol:
    - "Standard_Verification"
  status: "Theoretical_Baseline"
  topology_policy: "Blueprint"

object:
  object_type: "Concept"
  tier: 1
  description: "양극과 음극 사이의 물리적 절연을 보장하고, 이상 발열 시 기공 폐쇄(Shutdown)를 통해 열폭주 전이를 차단하는 안전 인프라 설계 지능"

semantic:
  expected_queries:
    - "분리막의 굴곡도(Tortuosity)와 기공률($\epsilon$)이 걸리 값(Gurley Value) 및 이온 저항에 미치는 수리적 상관관계는?"
    - "세라믹 코팅층(CCS)이 분리막의 열 수축률을 억제하여 고온 멜트다운(Meltdown) 온도를 상향시키는 물리적 기전은?"
  tags: ["#분리막공학", "#셧다운", "#멜트다운", "#걸리값", "#HDS-Gold"]

spo_graph:
  - subject: "Separator Thickness"
    predicate: "measured_value"
    object: "5 ~ 15 um"
    evidence: "[Ref: Film_Spec_V7] Section 1"
  - subject: "Shutdown Temp"
    predicate: "measured_value"
    object: "130 ~ 135 C"
    evidence: "[Ref: Thermal_Log_V7] Section 2"

trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Battery] Separator

## 1. 공학적 당위성: 안전 격리 및 이온 통로 (Why)
분리막(Separator)은 배터리 내부 단락을 방지하는 최후의 물리적 보루이자, 전해액을 머금어 이온을 통과시키는 다공성 매질입니다. 에너지 밀도 향상을 위한 박막화($< 10\mu\text{m}$)와 기계적/열적 안정성 확보 사이의 트레이드오프를 최적화하여, 열폭주 상황에서도 시스템의 무결성을 유지하는 것이 핵심 목적입니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| 파라미터 범주 (Category) | 물리적 지표 (Metric) | 목표 사양 (V7.6.2) | 공학적 의미 |
| :--- | :--- | :---: | :--- |
| **Thickness** | Base Film ($um$) | $5 \sim 12$ | 에너지 밀도 및 절연 거리 |
| **Gurley Value** | Permeability ($s/100cc$) | $150 \sim 250$ | 이온 저항 및 기공 연결성 |
| **Porosity** | Void Ratio ($\%$) | $35 \sim 45$ | 이온 전도도 및 강도 균형 |
| **Puncture Str.** | Piercing Force ($gf$) | $> 350$ | 조립 공정 내 이물 내구력 |
| **Shutdown** | Pore Closure ($^\circ\text{C}$) | $130 \sim 135$ | 이상 발열 시 전류 차단 |
| **Meltdown** | Integrity Loss ($^\circ\text{C}$) | $> 165$ (CCS) | 막 붕괴 및 전면 단락 임계점 |
| **Thermal Shrink.**| Shrinkage ($150^\circ\text{C}$) | $< 5\%$ | 고온 시 전극 노출 방지 |

## 3. 핵심 공학 분석 (Scientific Rationale)
- **Gurley-Ionic Resistance Correlation**: 걸리 값($t$)은 $t \propto \frac{\tau^2 \cdot L}{r \cdot \epsilon}$ 모델을 따릅니다. 굴곡도($\tau$)가 높을수록 이온 이동 거리가 길어져 저항이 증가하므로, 나노 기공의 균일한 배향을 통해 걸리 값 대비 최적의 이온 전도도를 확보해야 합니다.
- **Thermal Integrity Mechanism**: 고온 노출 시 PE/PP 기재의 기공이 녹아 막히는 Shutdown 메커니즘을 정의합니다. 세라믹 코팅층(CCS)은 열 수축 응력을 물리적으로 지지하여 멜트다운 온도를 $30^\circ\text{C}$ 이상 상향시켜 열폭주 전이를 지연시킵니다.

## 4. [Skill] Separator Safety Monitor
전압 강하율($dV/dt$) 데이터를 기반으로 미세 단락(Soft-short) 발생 여부를 탐지하며, 온도 궤적 분석을 통해 Shutdown 시작 점과 Meltdown 리스크를 실시간으로 판정하는 안전 엔진을 포함합니다.

## 5. 검증 프로토콜 (Audit)
1. **Puncture Integrity Audit**: 덴드라이트 관통 및 전극 표면 돌기에 의한 단락을 방지하기 위한 찌름 강도($350\text{ gf}$ 이상) 전수 검사.
2. **Coating Adhesion Check**: 세라믹 층의 코팅 결합력이 부족하여 전해액 내에서 입자가 탈락(Dusting)하는지 계면 접착력 분석.
3. **Shutdown Fidelity**: 가열 테스트 시 기공 폐쇄 후 저항이 $10^4$배 이상 급상승하여 전류를 차단하는지 열 역학적 무결성 확인.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] battery-pack-thermal-and-safety-intelligence]]
- [[[Concept] thermal-runaway-safety-mechanisms]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**
