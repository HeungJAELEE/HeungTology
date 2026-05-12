---
Basic:
  id: "[[[Battery] semicon-troubleshoot-etching-plasma"
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

# [[[Battery] semicon-troubleshoot-etching-plasma

## 1. [공학적 현상 (Phenomena): Etch Chronic Loss]]
식각 공정은 챔버 내부의 화학적/물리적 환경이 시간에 따라 변하는 **드래프트(Drift)** 현상이 만성 로스의 주원인입니다. 특히 플라즈마 상태의 미세한 변동은 회로의 수직도(Profile)와 수율에 즉각적인 타격을 줍니다.

## 2. [만성 로스 분석 및 해결 매트릭스 (Loss-Action-Theory)]

| 만성 로스 현상 | 원인 (Cause) | 해결 액션 (Remedy) | 공학적 원리 (Rationale) |
| :--- | :--- | :--- | :--- |
| **식각 속도 저하 (ER Drift)** | **Polymer Build-up on Walls** | **WAC (Waferless Auto Clean)** 주기 단축 및 챔버 벽면 온도 상승 | 내벽의 폴리머가 플라즈마 에너지를 흡수하여 실제 반응에 쓰일 이온 밀도 감소. |
| **미세 아킹 (Micro-Arcing)** | **ESC Edge Contamination** | 정전 척(ESC) 및 에지 링(Edge Ring) 교체/세정 | 전하가 특정 부위에 집중되어 불꽃(Arc)이 튀면서 웨이퍼 파손 및 파티클 발생. |
| **선택비 저하 (Selectivity Loss)** | **MFC Flow Inaccuracy** | 질량 유량 제어기(MFC) Zero-point 보정 및 가스 필터 교체 | 가스 혼합비가 설계치와 어긋나면 목표 막질 외의 하부 막질까지 과식각됨. |
| **패턴 뭉개짐 (Notching)** | **Charge Accumulation** | RF Bias 파형 보정 및 저주파/고주파 비율 조정 | 전극 바닥에 쌓인 전하가 이온의 궤적을 휘게 하여 하부 패턴 측면을 깎아먹음. |

## 3. [설비 하드웨어 체크리스트 (Hardware Diagnostics)]

### 3.1 RF & Matching Unit
1. **RF Matching Speed**: 매칭이 늦어지면($>1\text{sec}$) 공정 초기에 에너지가 전달되지 않아 식각 불균일 발생.
2. **VPP (Peak-to-Peak Voltage)**: 전압 파형이 불규칙하면 플라즈마 밀도가 흔들리므로 실시간 모니터링 필수.

### 3.2 Gas & Vacuum Unit
1. **He Leak Test (Chamber)**: 챔버 기밀성이 깨지면 외부 질소/산소가 유입되어 화학 반응 왜곡.
2. **Throttle Valve Response**: 압력을 조절하는 밸브의 응답성이 떨어지면 공정 중 압력 헌팅(Hunting) 발생.

## 4. [품질 제어 지표 (KPI & Numerical Standards)]

| 지표 (Metric) | 관리 임계치 | 트러블슈팅 기준 |
| :--- | :--- | :--- |
| **Etch Rate Uniformity** | $< 1.5 \%$ | 초과 시 Showerhead 가스 분사 및 RF 전극 수평도 점검 |
| **Taper Angle** | $89^\circ \sim 90.5^\circ$ | 범위를 벗어날 경우 가스 조성비 및 Bias Power 조정 |
| **Reflected Power** | $< 1\%$ | 초과 시 Auto-matcher 부품 마모 및 케이블 접촉 불량 확인 |

---
*Created by Flash (Etch-Plasma Loss Engine v2.0)*