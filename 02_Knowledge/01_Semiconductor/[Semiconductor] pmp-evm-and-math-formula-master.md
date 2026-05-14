---
Basic:
  date: '2026-05-12'
  domain: Unknown_Domain
  id: '[[[Semiconductor] pmp-evm-and-math-formula-master'
  project: Vault_Modernization
  version: v6.3.7
Dynamic:
  diagnostic_protocol:
  - 'Standard_Verification: Verify baseline parameters.'
  - 'Context_Audit: Ensure topological integrity.'
  fidelity_engine: DomainFidelityEngine
  graphify_link_external: true
  status: Ratified_v6.3.7_Migration
  topology_policy: Interconnected_Cluster
Object:
  description: Standard Industrial Node
  object_type: Concept
  physical_model: N/A
  tier: 1
Semantic:
  expected_queries:
  - Assistant to an Industrial Process Engineer at "Antigravity".
  - Technical document about Earned Value Management (EVM) for semiconductor projects.
  - Create 5 expected queries for later searching/retrieving this document.
  - Specific and practical (professional/industry-focused).
  - End with '?'.
  is_part_of: []
  related_to: []
  tags:
  - '#auto-healed'
Trust Metrics:
  T_dynamic: 1.0
  T_init: 1.0
  T_static: 1.0
  isolation_index: 0.0
  source: Antigravity Vault
---

# [[[Semiconductor] pmp-evm-and-math-formula-master

## 1. [왜 배우는가? (Why): 느낌이 아닌 숫자로 프로젝트를 관리하다]]
프로젝트가 잘 진행되고 있는지 묻는다면 대부분 "열심히 하고 있다"라고 답합니다. 하지만 획득 가치 관리(EVM)는 이를 거부합니다. "현재 1억을 썼는데, 실제로 만들어진 가치는 얼마인가?"를 수치화하여 현재의 상태를 정확히 진단하고, 남은 기간 동안 돈이 얼마나 더 들지(EAC), 언제 끝날지(ETC)를 과학적으로 예측합니다.

## 2. [핵심 기술 사양 (Numerical Specs): EVM 성과 및 예측 지표 데이터]

프로젝트의 성패는 효율 지수($CPI, SPI$)의 안착 여부에 의해 결정됩니다.

| 지표 (Metric) | 관리 임계치 (Spec) | 물리적/관리적 의미 | 비고 |
| :--- | :--- | :--- | :--- |
| **CPI (Cost Perf.)** | $\ge 1.0$ | 투입 비용 대비 가치 창출 효율 ($EV/AC$) | $1.0$ 미만 시 예산 초과 |
| **SPI (Sched Perf.)** | $\ge 1.0$ | 계획 시간 대비 업무 완료 효율 ($EV/PV$) | $1.0$ 미만 시 일정 지연 |
| **CV (Cost Variance)**| $\ge 0$ | 가치와 비용의 단순 차이 ($EV-AC$) | 화폐 단위 지표 |
| **SV (Sched Variance)**| $\ge 0$ | 가치와 계획의 단순 차이 ($EV-PV$) | 시간의 가치화 지표 |
| **EAC (At Comp.)** | $\le BAC$ | 현재 추세 지속 시 예상 총 프로젝트 비용 | 재무 예측의 핵심 |
| **TCPI (To-Complete)**| $\le 1.1$ | 잔여 예산 내 목표 달성을 위해 필요한 효율 | $1.1$ 초과 시 목표 달성 희박 |

## 3. [심층 이론 (Deep Dive): 3가지 핵심 데이터와 예측 논리]

### 3.1 PV, AC, EV: EVM의 3대 지표
- **Planned Value (PV)**: "오늘까지 얼마치 일하기로 약속했는가?" (계획의 가치)
- **Actual Cost (AC)**: "오늘까지 실제로 돈을 얼마 썼는가?" (투입의 가치)
- **Earned Value (EV)**: "오늘까지 실제로 해낸 일의 양은 얼마인가?" (결과의 가치)
- **Physics**: EV는 프로젝트의 '실질적 운동 에너지'이며, AC와의 비교는 '효율'을, PV와의 비교는 '속도'를 의미합니다.

### 3.2 EAC (Estimate At Completion) 예측 공식
현재의 상황에 따라 미래를 보는 안경이 달라집니다.
1. **Typical Case**: $EAC = BAC / CPI$. 현재의 비효율이 종료 시까지 지속될 것으로 볼 때.
2. **One-time Anomaly**: $EAC = AC + (BAC - EV)$. 현재의 비효율은 일시적 사고였으며, 앞으로는 계획대로 될 때.
3. **Double Constraint**: $EAC = AC + \frac{BAC - EV}{CPI \times SPI}$. 비용과 일정을 동시에 고려한 가장 보수적인 예측.

## 4. [AI & Hardware Synergy: Real-time EVM Integration]
- **ERP-PMIS Sync**: 전사적 자원 관리(ERP)의 실제 지출 데이터와 프로젝트 관리 시스템(PMIS)의 진척 데이터를 실시간 연동하여, 매일 아침 업데이트된 CPI/SPI를 대시보드에 시각화합니다.
- **Predictive EAC via LSTM**: 과거 프로젝트의 EVM 흐름을 학습한 딥러닝 모델(LSTM)이 단순 선형 예측인 EAC를 넘어, 위험 구간에서의 변동성을 반영한 고정밀 최종 비용을 예측합니다.

## 5. [스스로 체크 (Verification)]
- [ ] **CPI = 0.8**, **SPI = 1.2**인 프로젝트의 현재 건강 상태는? (정답: 일정은 계획보다 빠르지만, 돈을 낭비하며 일을 처리하고 있는 '비효율적 가속' 상태)
- [ ] **TCPI**가 1.0보다 크다는 것은 프로젝트 팀에게 어떤 의미인가?
- [ ] 왜 **SV**가 0인 상태가 반드시 프로젝트가 성공적으로 끝났음을 보장하지 않는가? (정답: SV는 가치 기반 일정 지표이므로, 실제 날짜 기반 지연과 차이가 있을 수 있기 때문)

---
*Reference: Project Management Institute (PMBOK Guide 7th Edition), PMP Exam Content Outline, Antigravity PMP Lab.*