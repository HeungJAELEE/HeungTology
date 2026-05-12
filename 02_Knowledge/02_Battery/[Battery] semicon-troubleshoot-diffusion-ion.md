---
Basic:
  id: "[[[Battery] semicon-troubleshoot-diffusion-ion"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
  is_part_of: []]
  related_to: []
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

# [[[Battery] semicon-troubleshoot-diffusion-ion

## 1. [공학적 현상 (Phenomena): Diffusion & Ion Chronic Loss]]
확산 및 이온주입 공정은 칩의 전기적 성질($V_{th}$ 등)을 결정하는 핵심 단계입니다. 여기서의 만성 로스는 **열적 드리프트(Thermal Drift)**와 **빔 안정성(Beam Stability)**에 기인하며, 미세한 투입량 오차가 전체 칩의 성능 저하로 이어집니다.

## 2. [만성 로스 분석 및 해결 매트릭스 (Loss-Action-Theory)]

| 만성 로스 현상 | 원인 (Cause) | 해결 액션 (Remedy) | 공학적 원리 (Rationale) |
| :--- | :--- | :--- | :--- |
| **산화막 두께 편차** | **T/C (Thermocouple) Aging** | 열전대 교체 및 온도 프로파일(Profile) 재교정 | 고온 환경에서 T/C가 노후화되면 실제 온도보다 낮게 읽어 산화막이 설계보다 두껍게 형성됨. |
| **Doping 불균일** | **Beam Current Instability** | 이온 소스(Ion Source) 세정 및 가속 전압 안정화 | 이온 빔의 전류가 출렁이면 단위 면적당 주입되는 불순물 농도(Dose)가 달라짐. |
| **표면 결정 손상** | **Insufficient Annealing** | RTA (Rapid Thermal Anneal) 공정 시간/온도 보정 | 이온 충돌로 깨진 실리콘 결정 구조를 회복시키는 열처리가 부족하면 누설 전류 발생. |
| **쿼츠 오염 (Quartz Contam.)** | **Inner Tube Degradation** | 석영관 정기 세정 및 파티클 전수 조사 | 석영관 벽면에서 탈락된 입자가 고온 공정 중 웨이퍼 표면에 안착하여 결함 유발. |

## 3. [설비 하드웨어 체크리스트 (Hardware Diagnostics)]

### 3.1 Furnace Unit (확산로)
1. **Gas Sealing (Boat)**: 웨이퍼를 싣는 보트가 챔버 하단과 완벽히 밀폐되지 않으면 외부 공기 유입으로 산화막 질 저하.
2. **Cooling Fan System**: 공정 후 급속 냉각 시 팬의 속도가 일정하지 않으면 웨이퍼 뒤틀림(Warpage) 발생.

### 3.2 Ion Implanter Unit (이온주입기)
1. **Mass Analyzer Magnet**: 목표 이온만 걸러내는 자석의 자기장 세기가 정밀하지 않으면 다른 원소가 주입됨.
2. **Scan Velocity**: 빔이 웨이퍼를 훑는 속도가 일정해야 면 저항(Sheet Resistance) 균일도 확보 가능.

## 4. [품질 제어 지표 (KPI & Numerical Standards)]

| 지표 (Metric) | 관리 임계치 | 트러블슈팅 기준 |
| :--- | :--- | :--- |
| **Sheet Resistance (Rs)** | 설계치 $\pm 1 \%$ | 초과 시 이온 소스 필라멘트 및 가속 계통 전 점검 |
| **Junction Depth** | 설계치 $\pm 5\text{nm}$ | 범위를 벗어날 경우 열처리(Anneal) 온도 및 시간 재교정 |
| **Temp. Stability** | $\pm 0.5^\circ C$ | 초과 시 히터 구역별 전력 공급 장치(SCR) 점검 |

---
*Created by Flash (Diffusion-Ion Loss Engine v2.0)*