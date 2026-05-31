---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 45b0de14e37baf4a849df4c461fce1570558e5702b46c4a78436e5fcb6351fea
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] safety-instrumented-systems-sis-and-sil-rating-physics]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] safety-instrumented-systems-sis-and-sil-rating-physics에 관한
    고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  diagnostics_coverage: '> 99%'
  pfd_avg_formula: lambda_du * (ti / 2)
  proof_test_interval: 1-2 years
  redundancy_logic: 2oo3
  rrf_formula: 1 / pfd_avg
  sil_1_pfd_avg: < 10^-1
  sil_2_pfd_avg: < 10^-2
  sil_3_pfd_avg: < 10^-3
  sil_4_pfd_avg: < 10^-4
  target_hft: '1'
  target_pfd_avg: < 10^-3
  target_response_time: < 100ms
  target_rrf: '> 1000'
  target_sff: '> 90%'
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 11_Global_Entities_and_Materials]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Entity] safety-instrumented-systems-sis-and-sil-rating-physics

## 1. [왜 배우는가? (Why: The Last Line of Defense)]]
공장의 제어 시스템이 해킹당하거나 물리적으로 파손되어 반응기 압력이 폭발 직전까지 치솟을 때, 인간의 개입 없이도 스스로 밸브를 잠그고 전원을 차단하여 대참사를 막는 '산업의 최후의 보루'를 어떻게 설계할 수 있을까요? **안전 계장 시스템(SIS) 및 안전 무결성 등급(SIL)의 확률적 설계**는 기계의 오동작 확률을 수학적으로 계산하여 인명과 환경을 지키는 '산업의 양심'입니다. 단순히 "안전하게 만든다"는 주관적 믿음이 아니라, "1,000년에 단 한 번도 실패하지 않을 확률($SIL\ 3$)"을 수치로 입증해야 합니다. 우리가 이를 배우는 이유는 단 한 번의 사고가 기업의 존립과 지역 사회의 안전을 파괴할 수 있기 때문이며, "안전의 가치를 데이터로 설계하고 지배하는 '글로벌 리스크 거버넌스 패권 및 행성적 제조 주권'을 확보하기" 위함입니다. 안전 등급이 시스템의 신뢰 지도를 결정합니다.

## 2. [핵심 기술 사양 및 수리적 정의 (Numerical Specs & Mathematical Rationale)]

SIS의 무결성은 '요청 시 실패할 평균 확률($PFD_{avg}$)'에 의해 정의됩니다.

### 2.1 [안전 무결성 등급(SIL)의 수리적 정의]
$PFD_{avg}$는 안전 기능이 필요할 때 제대로 작동하지 않을 확률이며, 이를 통해 위험 감소 계수($RRF$)를 도출될 것으로 예상됩니다.
$$ RRF = \frac{1}{PFD_{avg}} $$
*   **SIL 1**: $RRF = 10 \text{ \~ } 100$ ($PFD_{avg} < 10^{-1}$)
*   **SIL 2**: $RRF = 100 \text{ \~ } 1000$ ($PFD_{avg} < 10^{-2}$)
*   **SIL 3**: $RRF = 1000 \text{ \~ } 10000$ ($PFD_{avg} < 10^{-3}$)
*   **SIL 4**: $RRF > 10000$ ($PFD_{avg} < 10^{-4}$, 원자력급)

### 2.2 [PFD 수식과 점검 주기($TI$)]
단일 채널 시스템의 $PFD_{avg}$는 고장률($\lambda$)과 테스트 주기($TI$)에 의해 결정됩니다.
$$ PFD_{avg} \approx \lambda_{DU} \cdot \frac{TI}{2} $$
*   $\lambda_{DU}$: 발견되지 않은 위험 고장률 (Dangerous Undetected)
*   **물리적 의미**: 장비가 좋아도 점검을 안 하면($TI \uparrow$) 안전 등급은 급격히 하락합니다.

| 파라미터 (Parameter) | 수리적 정의 및 동작 기전 (Mechanism Rationale) | 목표 사양 (V6.3.7) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :--- | :--- | :--- |
| **PFDavg** | Probability of failure on demand | $< 10^{-3} \text{ (SIL 3)}$ | 사고 시 시스템이 침묵할 확률을 극한으로 낮춤 |
| **RRF (Factor)** | Magnitude of risk reduction achieved | $> 1000$ | 원래 위험을 1/1000로 줄여 무결성을 사수함 |
| **HFT (Fault Tol.)**| Number of hardware failures tolerated | **1 (1oo2 or 2oo3)** | 부품 하나가 죽어도 안전 기능은 살아남음 입증 |
| **SFF (Fraction)** | Percentage of safe vs total failures | $> 90 \%$ | 고장이 나더라도 '안전한 쪽'으로 고장 나게 설계 |
| **Proof Test** | Interval between full functional tests | $1 \text{ \~ } 2 \text{ Years}$ | 시스템의 숨은 병을 찾아내는 정기적 무결성 사수 |
| **Response Time** | Time to achieve a safe state | $< 100 \text{ ms}$ | 폭발 전 순식간에 밸브를 닫는 시간적 무결성 |
| **Redundancy** | Independent redundant voting logic | **2oo3 (Voting)** | 세 개 중 두 개가 동의해야 작동하는 지능형 판단 |
| **Diagnostics** | Automatic self-testing coverage | $> 99 \%$ | 스스로 고장을 0.1초 만에 알아내는 지능적 무결성 |

## 3. [Advanced RAG 분석 로직: 수리적 인과 추론]

### 3.1 [Fail-safe vs Fail-operational의 상관분석]
왜 안전 시스템은 고장 나면 무조건 멈추나요? RAG는 "리스크 수용 로그를 분석하여, 불확실한 상태로 가동을 유지하는 것($Fail-operational$)보다 공정을 즉시 멈추는 것($Fail-safe$)이 수학적으로 총 기대 손실을 최소화하기 때문임을 입증될 것으로 추론됩니다. 이를 위해 전원이 끊기면 중력에 의해 저절로 닫히는 밸브와 같은 '수동적 안전' 경로를 수리적으로 도출될 것으로 예상됩니다.

### 3.2 [공통 원인 고장($CCF$)과 독립성의 인과 분석]
왜 SIS는 일반 PLC와 전선을 따로 써야 하나요? RAG는 "연쇄 사고 로그를 참조하여, 제어 시스템과 안전 시스템이 같은 전원이나 통신망을 공유하면 한 번의 낙뢰나 오류로 두 시스템이 동시에 죽기($Common\ Cause\ Failure$) 때문임을 산출될 것으로 예상됩니다. 이를 방지하기 위해 '물리적 분리($Segregation$)'와 '기술적 다양성($Diversity$)'을 사수하는 아키텍처를 수립합니다.

### 3.3 [중복성($Voting\ Logic$)과 가용도의 상관분석]
1oo2와 2oo3 중 무엇이 더 안전한가요? RAG는 "신뢰성 공학 로그를 분석하여, 1oo2는 안전성은 높지만 오작동($Spurious\ Trip$)으로 공장이 멈출 확률이 높고, 2oo3는 안전성과 가동률을 동시에 사수하는 '황금 비율'임을 입증될 것으로 추론됩니다. 이는 '안전을 위해 생산을 포기하지 않는' 고도의 지능형 리스크 아키텍처의 근거입니다.

## 4. [Conclusion: The Ethical Engine of Industry]
SIS와 SIL의 세계에서 숫자는 곧 생명입니다. 우리는 $10^{-3}$ 이하의 $PFD_{avg}$를 사수하고, 독립적 보호 계층($IPL$)의 논리적 무결성을 데이터로 검증함으로써, 기계의 탐욕이 재앙으로 변하지 않도록 감시하는 '산업의 수호신'을 구축합니다. Antigravity Intelligence는 이제 이 안전 계장 지능을 바탕으로 초대형 화학 단지의 비상 차단 시스템과 자율 주행 로봇의 '충돌 방지 무결성 경로'를 설계합니다. 우리가 **'우연의 사고를 필연의 확률로 지배하는 기술'**을 완성할 때, 인류의 제조 현장은 그 어떤 위협 속에서도 결코 무너지지 않는 '강인하고 윤리적인 터전'이 될 것입니다.

### 🔗 참조 출처 및 로컬 지식망 (Retrieved Nodes)
- MOC 70_industrial-automation-and-robotics-control-hub : 산업 자동화 및 로봇 제어를 관리하는 상위 지능 허브
- GEMINI.md : 최상위 안전 계장 시스템 및 SIL 등급 거버넌스 가이드
- [SOP] functional-safety-audit-and-pfd-calculation-manual : 실전 운영 무결성 검증 SOP
- "Functional Safety: A Straightforward Guide to IEC 61508" (David J. Smith) - Safety Rationale.
- "Guidelines for Safe Automation of Chemical Processes" (CCPS) - Risk Management Integration.

*Created by Flash (The Ethical Architect of Safety & HDS Gold V6.3.7)*