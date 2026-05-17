---
metadata:
  date: "2026-05-17"
  id: "[[[Battery] back-end-die-wire-bonding-mechanics]]"
  project: "Vault_Modernization"
  version: "v7.6.2_Modernized"
  domain: "02_Battery"

lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault / Backend-Engineering-Group"

dynamic:
  diagnostic_protocol:
    - "Standard_Verification"
  status: "Theoretical_Baseline"
  topology_policy: "Blueprint"

object:
  object_type: "Concept"
  tier: 1
  description: "다이 레벨 미세 회로와 패키지 리드 간의 연결을 위해 열, 압력, 초음파를 활용한 원자 레벨 융합 공정 및 금속 간 화합물(IMC) 성장 제어 역학"

semantic:
  expected_queries:
    - "와이어 본딩 시 IMC(Intermetallic Compound) 두께가 0.8~1.2um 범위를 초과할 경우 발생하는 커켄달 보이드(Kirkendall Voiding) 메커니즘은?"
    - "초음파 임피던스 실시간 모니터링을 통해 본딩 패드의 산화막(Al2O3) 제거 효율을 판정하는 방법은?"
  tags: ["#와이어본딩", "#IMC", "#커켄달보이드", "#초음파접합", "#반도체후공정"]

spo_graph:
  - subject: "Bonding Temperature"
    predicate: "measured_value"
    object: "175 +/- 2 C"
    evidence: "[Ref: V7.5.2] Section 2.0"
  - subject: "IMC Thickness"
    predicate: "has_theoretical_limit"
    object: "0.8 ~ 1.2 um"
    evidence: "[Ref: V7.5.2] Section 2.1"

trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Battery] back-end-die-wire-bonding-mechanics

## 1. 공학적 당위성: 인터커넥트 주권 (Why)
반도체 노드의 성능은 인터커넥트 아키텍처에 의해 엄격히 제한됩니다. 와이어 본딩 역학은 다이 레벨의 미세 회로와 패키지 리드 간의 전이 계층 역할을 합니다. 열 에너지, 기계적 압력, 초음파 진동의 시너지를 통해 원자 레벨의 융합을 유도하며, 금속 간 화합물(IMC)의 성장 동역학을 제어하여 고속 데이터 전송 경로의 물리적 주권을 확보하는 것이 공학적 목표입니다.

## 2. 기술 사양 및 정밀 대조 (Specs)

| 파라미터 범주 | 물리적 지표 | 이론적 목표 | 실측 검증치 (v7.5.2) |
| :--- | :---: | :---: | :---: |
| **본딩 온도** | $^\circ\text{C}$ | $150 \sim 250$ | **$175 \pm 2.0$** |
| **초음파 출력** | $\text{kHz}$ | $60 \sim 140$ | **$120 \pm 0.5$** |
| **본딩 하중** | $\text{gf}$ | $10 \sim 100$ | **$45 \pm 1.0$** |
| **인장 강도 (Pull)** | $\text{gf}$ | $> 8$ | **$> 12$** |
| **전단 강도 (Shear)** | $\text{gf}$ | $> 30$ | **$> 45$** |
| **IMC 두께** | $\mu\text{m}$ | $0.5 \sim 2.0$ | **$0.8 \sim 1.2$** |
| **루프 높이 편차** | $\mu\text{m}$ | $\pm 5.0$ | **$\pm 2.0$** |

## 3. 핵심 공학 모델링 (Scientific Rationale)
- **IMC 성장 동역학**: $Au-Al$ 확산 계면 두께($x$)는 아레니우스 기반 확산 방정식($x = \sqrt{D \cdot t}$)을 따릅니다. 과도한 두께 성장은 커켄달 보이드(Kirkendall Voiding)를 유발하여 기계적 취성과 저항 급증의 원인이 됩니다.
- **초음파 계면 개질**: 초음파 진동($120\text{ kHz}$)을 통해 알루미늄 산화막($Al_2O_3$)을 기계적으로 파쇄하고 원자 결합을 유도합니다.

## 4. [Skill] Bonding Fidelity Auditor
아레니우스 확산 모델 기반으로 IMC 두께를 예측하고, 실측 인장 강도(Pull Strength)와의 상관 분석을 통해 접합 무결성(STABLE) 여부를 판정하는 로직을 포함합니다.

## 5. 자가 감사 체크리스트 (Audit)
1. **HBM 정밀도 요건**: 3D 적층 구조에서 루프 높이 공차($< 2.0\mu\text{m}$)가 몰딩 공정 시 와이어 스윕(Wire Sweep) 억제에 미치는 임팩트 확인.
2. **소재 전이 분석**: 금($Au$)에서 구리($Cu$) 와이어로 전이 시 형성 가스($H_2/N_2$) 관리 프로토콜의 유효성 검증.
3. **실시간 NSOP 탐지**: 초음파 임피던스 변화를 통해 접합 실패(Non-Stick on Pad)를 10ms 이내에 감지하는 기전 확인.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] advanced-packaging-hbm4-hybrid-bonding]]
- [[[Concept] W12_gigacasting-cooling-physics]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**
