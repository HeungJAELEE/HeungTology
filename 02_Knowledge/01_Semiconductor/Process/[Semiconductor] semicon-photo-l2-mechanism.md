---
Basic:
  id: "SEMICON_PHOTO_L2_MECHANISM"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Semiconductor", "#Photolithography", "#SOP", "#Mechanism", "#Track_System", "#HDS_Gold_v6_1"]'
  is_part_of: []
  related_to: '["Semiconductor semicon-photo-l1-physics", "Semiconductor semicon-photo-l3-hardware (보강 필요)"]'
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [[[Semiconductor] semicon-photo-l2-mechanism

# Semiconductor semicon-photo-l2-mechanism
[🟢 Local RAG] 노광 공정은 단순히 빛을 쏘는 단계가 아니라, 화학(레지스트)과 물리(광학)가 정밀하게 맞물려 돌아가는 8단계의 연쇄 공정입니다. 트랙(Track) 장비 내에서 이루어지는 도포, 베이킹, 현상 과정의 파라미터가 0.1%만 틀어져도 노광 장비(Scanner)가 그려낸 초미세 패턴은 무너집니다. 각 단계의 수리적 상관관계를 이해하여 '무결성 공정 윈도우'를 확보하는 것이 엔지니어의 핵심 역량입니다.

---

# [[[Semiconductor] semicon-photo-l2-mechanism

| 단계 (Step) | 주요 액션 | 제어 파라미터 (Target) | 공학적 목적 (Rationale) |
| :--- | :--- | :--- | :--- |
| **1. 표면 처리** | HMDS Prime | 접촉각 $< 10^\circ$ | 웨이퍼 표면을 소수성으로 바꿔 PR 접착력 강화 |
| **2. PR 도포** | Spin Coating | $1,000 \sim 4,000 \text{ RPM}$ | 원심력을 이용한 나노 단위 두께 균일도 확보 |
| **3. 소프트 베이크**| PAB | $90 \sim 110^\circ\text{C}$ | 용매(Solvent) 제거 및 PR 고형화 |
| **4. 정렬/노광** | Exposure | Energy Dose ($mJ/cm^2$) | 마스크 패턴을 PR 내부로 전사 (광화학 반응) |
| **5. 노광 후 베이크**| PEB | **$\pm 0.1^\circ\text{C}$ 제어** | 산(Acid) 확산을 통한 화학적 증폭 및 정진파 제거 |
| **6. 현상** | Developing | Puddle Time ($45 \sim 60 \text{ s}$) | TMAH 용액으로 노광부(Positive) 선택적 제거 |
| **7. 하드 베이크** | Hard Bake | $120 \sim 140^\circ\text{C}$ | 잔여 용매 제거 및 식각 내성 강화 |
| **8. 검사** | Inspection | CD/Overlay Accuracy | 선폭 및 정렬 오차 측정 후 후속 공정 승인 |

---

# Semiconductor semicon-photo-l2-mechanism

# [[[Semiconductor] semicon-photo-l2-mechanism
[🟢 Local RAG]] 감광액의 박막 두께($T$)는 각속도($\omega$)의 제곱근에 반비례합니다.
$$ T = K \cdot \frac{S^2}{\omega^{1/2}} $$ ($S$: 고형분 함량)
- **Engineering Point**: RPM의 미세한 맥동은 두께 불균일을 초래하며, 이는 곧 노광 시 초점 오차(Focus Margin 부족)로 직결됩니다.

# [[[Semiconductor] semicon-photo-l2-mechanism
[🟢 Local RAG]] 현대 선단 공정의 핵심은 **산 촉매 탈보호 반응(Deprotection)**입니다.
- **메커니즘**: 노광 단계에서 생성된 산(Acid)이 PEB 단계의 열에너지를 받아 수천 개의 고분자 사슬을 끊어냅니다.
- **임계 제어**: PEB 온도가 1도 상승할 때 산의 확산 거리($L_d$)가 급증하여 선폭(CD)이 수 나노미터 굵어집니다. 따라서 **Hot Plate의 온도 균일도**가 수율의 생명입니다.

---

# [[[Semiconductor] semicon-photo-l2-mechanism

# Semiconductor semicon-photo-l2-mechanism
[🟢 Local RAG] 웨이퍼 위에 현상액을 웅덩이처럼 띄워 정지 상태에서 반응시키는 방식입니다.
- **장점**: 현상액 소모를 줄이면서 표면 장력을 통해 웨이퍼 전체에 균일한 반응을 유도합니다.
- **수율 변수**: 현상액의 농도(TMAH 2.38%)와 공급 온도가 불균일할 경우, 패턴 하단이 덜 깎이는 'Footing' 또는 과하게 깎이는 'Under-cut' 불량이 발생합니다.

---

# [[[Semiconductor] semicon-photo-l2-mechanism

# Semiconductor semicon-photo-l2-mechanism
포토 공정에서 가장 무서운 적은 '지연(Delay)'입니다. 노광 후 PEB까지의 대기 시간(Wait Time)이 길어지면, 공기 중의 아민(Amine) 성분이 산을 중화시켜 패턴 상단이 굳어버리는 **'T-topping'** 불량이 발생합니다. 따라서 고성능 트랙 시스템은 모든 공정 단계를 초 단위로 스케줄링하는 **'인라인(In-line) 실시간 제어 지능'**을 사수해야 합니다.

---

# [[[Semiconductor] semicon-photo-l2-mechanism
- [ ]] 스핀 코팅 시 RPM을 2배 높이면 두께는 수리적으로 몇 배로 감소하는가?
- [ ] PEB 공정이 생략되거나 온도가 낮을 경우, 화학 증폭형 레지스트(CAR)에서 발생하는 현상을 설명하시오.
- [ ] HMDS 처리가 부실할 경우, 현상(Development) 단계에서 발생할 수 있는 치명적 불량은 무엇인가?

---
# [[[Semiconductor] semicon-photo-l2-mechanism
- 🏛 Semiconductor Track-System]] (Verified)
- 🏛 Concept Photoresist-Chemical-Formulation-and-Polymer-Science (Verified)
- 🏛 Semiconductor semicon-photo-l1-physics (Verified)
- 🏛 Semiconductor semicon-photo-l3-hardware (보강 필요)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
