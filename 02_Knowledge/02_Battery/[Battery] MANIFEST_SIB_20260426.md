---
metadata:
  date: "2026-05-17"
  id: "[[[Battery] MANIFEST_SIB_20260426]]"
  project: "Vault_Modernization"
  version: "v7.6.2_Modernized"
  domain: "02_Battery"

lineage:
  dataset_reference: "battery-sib-performance-and-inventory-log_2026-05-16"
  original_author: "Antigravity Vault / SIB-Research-Group"

dynamic:
  diagnostic_protocol:
    - "Standard_Verification"
  status: "Theoretical_Baseline"
  topology_policy: "Blueprint"

object:
  object_type: "Concept"
  tier: 1
  description: "나트륨 이온 배터리(SIB)의 화학적 구성, 리튬 이온 대비 비교 우위 및 0V 방전 안정성 매니페스트"

semantic:
  expected_queries:
    - "나트륨 이온 배터리가 리튬 이온 대비 0V 완전 방전 시 안전한 열역학적 이유는?"
    - "SIB 하드 카본 음극의 층간 거리(d002) 임계 설계치는?"
  tags: ["#나트륨이온", "#SIB", "#0V방전", "#하드카본", "#알루미늄집전체"]

spo_graph:
  - subject: "SIB Discharge Stability"
    predicate: "allows"
    object: "0V Deep Discharge"
    evidence: "[Ref: MANIFEST_SIB] Section 3.3"
  - subject: "Hard Carbon Spacing"
    predicate: "has_theoretical_limit"
    object: "> 0.37 nm"
    evidence: "[Ref: Stokes-Einstein] Section 3.1"

trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Battery] MANIFEST_SIB_20260426

## 1. 개요: 저원가/고안전 SIB 솔루션
나트륨 이온 배터리(SIB)는 리튬($Li$) 대신 자원이 풍부한 나트륨($Na$)을 활용하여 원가를 획기적으로 절감하는 차세대 에너지 저장 솔루션입니다. 특히 알루미늄 집전체 통합과 0V 방전 안정성을 통해 물류 및 보관의 혁신을 제공하며, ESS 및 보급형 EV 시장을 타겟으로 합니다.

## 2. 기술 사양 및 비교 표준 (Standard Specs)

| 파라미터 | 리튬 이온 (LIB) | 나트륨 이온 (SIB) | 공학적 근거 |
| :--- | :---: | :---: | :--- |
| **원재료 비용** | 높음 (Li) | **매우 낮음 (Na)** | 자원 풍부성 ($NaCl$ 기반) |
| **음극 소재** | 흑연 (Graphite) | **하드 카본 (Hard Carbon)** | $Na^+$ 이온 반경 수용 능력 |
| **집전체 (음극)** | 구리 (Cu) | **알루미늄 (Al)** | $Na$와 알루미늄 간 합금화 부재 |
| **0V 방전 안정성** | 위험 (Cu 용출) | **안전 (용출 없음)** | 0V 환경 알루미늄 열역학적 안정성 |

## 3. 핵심 공학 분석 (Engineering Rationale)

### 3.1 확산 역학 (Diffusion Kinetics)
나트륨 이온은 리튬 대비 반경이 커서 전해액 내 이동도가 낮습니다. 이를 극복하기 위해 하드 카본의 층간 거리($d_{002}$)를 $0.37\text{ nm}$ 이상으로 확보하여 확산 경로를 최적화해야 합니다.

### 3.2 하드 카본 저장 메커니즘
흑연화되지 않는 하드 카본은 'Intercalation'과 'Pore Filling'의 이중 모드 메커니즘을 통해 나트륨을 저장하며, 이는 SIB 특유의 저전압 플래토(Plateau) 영역을 형성합니다.

### 3.3 경제성 및 물류 혁신
음극 집전체로 저렴한 알루미늄 박을 사용함으로써 원가를 30~40% 절감하며, 0V 완전 방전 운송을 통해 화재 위험을 근본적으로 차단하는 물류적 이점을 제공합니다.

## 4. 진단 및 운영 프로토콜
- **0V Storage Protocol**: 장기 보관 시 0V 방전 상태 유지로 안전성 극대화.
- **Thermal Management**: 저온($-40\text{ }^\circ\text{C}$) 및 고온 환경에서의 작동 범위 확보.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] Battery-Materials-and-Chemistry-Master-Guide]]
- [[[Data] Battery-SIB-Performance-and-Inventory-Log_2026-05-16]]

**[V7.6.2_HARDCORE_FIDELITY_VERIFIED]**
