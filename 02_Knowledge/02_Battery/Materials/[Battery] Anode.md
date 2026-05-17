---
metadata:
  date: "2026-05-17"
  id: "[[[Battery] Anode]]"
  project: "Vault_Modernization"
  version: "v7.6.2_Modernized"
  domain: "02_Battery"

lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault / Anode-Science-Group"

dynamic:
  diagnostic_protocol:
    - "Standard_Verification"
  status: "Theoretical_Baseline"
  topology_policy: "Blueprint"

object:
  object_type: "Concept"
  tier: 1
  description: "리튬 이온의 저장을 담당하며, 급속 충전 성능과 전극 팽창 제어의 핵심인 음극 소재의 결정학적 및 역학적 설계 지능"

semantic:
  expected_queries:
    - "흑연 음극의 리튬 삽입/탈리 시 격자 상수 변화($\Delta a, \Delta c$)가 전극 스트레스에 미치는 수리적 영향은?"
    - "실리콘-탄소(Si-C) 복합 음극에서 공극(Void) 구조가 실리콘 팽창 완충에 기여하는 열역학적 기전은?"
  tags: ["#음극공학", "#흑연", "#실리콘음극", "#부피팽창", "#HDS-Gold"]

spo_graph:
  - subject: "Anode Expansion"
    predicate: "measured_value"
    object: "< 25 % (at 100% SOC)"
    evidence: "[Ref: Swelling_Log_V7] Section 1"
  - subject: "Li Diffusion (Anode)"
    predicate: "measured_value"
    object: "10^-10 ~ 10^-8 cm2/s"
    evidence: "[Ref: Kinetics_Data] Section 2"

trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Battery] Anode

## 1. 공학적 당위성: 전하 저장소 및 출력 제어 (Why)
음극(Anode)은 배터리 시스템의 에너지 저장 밀도와 초급속 충전(XFC) 능력을 결정하는 핵심 관문입니다. 흑연의 열역학적 안정성과 실리콘의 고용량 특성을 물리적으로 융합하여, 충전 시 발생하는 리튬 덴드라이트 성장을 억제하고 전극 수준의 부피 팽창($< 25\%$)을 관리하는 결정론적 설계가 요구됩니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| 파라미터 범주 (Category) | 물리적 지표 (Metric) | 흑연 (Graphite) | 실리콘 복합체 (Si-C) | 공학적 의미 |
| :--- | :--- | :---: | :---: | :--- |
| **Specific Cap.** | Capacity ($mAh/g$) | $360 \sim 365$ | $450 \sim 600$ | 에너지 밀도 직결 |
| **Initial Eff.** | ICE (%) | $\ge 93\%$ | $85 \sim 90\%$ | 비가역 리튬 소모량 |
| **Expansion** | Swelling (at SOC 100%) | $10 \sim 12 \%$ | $15 \sim 25 \%$ | 기계적 안정성 지표 |
| **Diffusion Coeff.**| $D_{Li}$ ($cm^2/s$) | $10^{-8} \sim 10^{-7}$ | $10^{-12} \sim 10^{-10}$ | 충전 속도 임계치 |
| **Adhesion** | Peel Strength ($gf/mm$) | $> 20$ | $> 35$ | 집전체 탈리 방지 강도 |
| **Porosity** | Net Voids (%) | $25 \sim 30 \%$ | $30 \sim 40 \%$ | 이온 통로 및 팽창 완충 |

## 3. 핵심 공학 분석 (Scientific Rationale)
- **SEI Growth Kinetics**: 음극 표면의 고체 계면 막(SEI) 형성은 $d_{SEI}(t) = \kappa \sqrt{D \cdot t}$ 모델을 따르며, 초기 효율(ICE)의 $5 \sim 10\%$ 소모를 유발합니다. 안정적인 SEI 형성을 위해 전해액 첨가제(FEC/VC)와의 화학적 정합성을 최적화해야 합니다.
- **Chemo-mechanical Expansion**: 실리콘의 부피 팽창 응력($\sigma$)은 격자 내 리튬 농도 구배에 비례합니다. 탄소 매트릭스 내 나노 실리콘 입경을 $150\text{ nm}$ 이하로 제어하여 응력 에너지를 입자 파괴 인성 임계치 이하로 관리합니다.

## 4. [Skill] Anode Expansion Fidelity Engine
소재 함량(Graphite/Si) 및 전극 기공률 데이터를 기반으로 충전 시 극판 두께 증가율을 예측하며, 팽창률 $25\%$ 초과 시 셀 케이스 파손 및 내부 단락 리스크를 경고하는 오딧 루틴을 가동합니다.

## 5. 검증 프로토콜 (Audit)
1. **Capacity Integrity Audit**: 실측 방전 용량이 이론치($372 \text{ mAh/g}$ @ Graphite) 대비 $-2\%$ 오차 범위를 유지하는지 전수 검증.
2. **Swelling Buffer Check**: 설계 기공률이 실리콘 팽창분을 수용 가능한 물리적 체적($V_{pore} > \Delta V_{Si}$)을 확보했는지 정밀 분석.
3. **Adhesion Audit**: $DOD$ 사이클 반복 시 활물질-동박 간 결합력이 초기치 대비 $80\%$ 이상 유지되는지 기계적 무결성 확인.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] material-anode-synthesis]]
- [[[Concept] binder-intelligence-and-slurry-rheology]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**
