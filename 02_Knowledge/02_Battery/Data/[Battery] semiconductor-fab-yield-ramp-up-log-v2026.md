---
Basic:
  id: "semiconductor-fab-yield-ramp-up-log-v2026-log"
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
  tags: '["#Data", "#Yield", "#Ramp_up", "#Defect_Map", "#Semiconductor", "#HDS_Gold_v6_1"]'
  is_part_of: '["MOC 01_Semiconductor"]'
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

# [[[Battery] semiconductor-fab-yield-ramp-up-log-v2026

## 1. [데이터 개요]]
본 문서는 신규 3nm GAA 공정 라인의 초기 수율 램프업(Ramp-up) 과정과 안정화 데이터를 기록한 로그입니다. 주차별 수율 추이와 주요 수율 저하 인자(Yield Detractors)를 분석하여 양산 무결성을 확보합니다.

## 2. [주차별 수율 추이 데이터 (Yield Ramp-up Curve)]

| Week | Target Yield (%) | Actual Yield (%) | 주요 이슈 (Key Detractor) | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **W01** | 10.0 % | **8.5 %** | 포토 공정 정렬 오차 | 설비 매칭 및 오버레이 보정 필요 |
| **W04** | 35.0 % | **32.2 %** | 식각(Etch) 파티클 발생 | 챔버 클리닝 주기 단축 조치 |
| **W08** | 55.0 % | **58.4 %** | 수율 램프업 가속 구간 | 공정 마진(Process Window) 최적화 |
| **W12** | 75.0 % | **78.1 %** | 안정화 단계 진입 | 수율 변동성(Sigma) 제어 성공 |

### 2.1 [결함 밀도(Defect Density) 분석]
- **D0 (Defects per $cm^2$)**: **0.08** (목표 0.1 이하 달성)
- **수리적 무결성**: Poisson Distribution 기반 수율 모델 분석 결과, 현재의 결함 밀도 하에서 칩 크기 $150 mm^2$ 기준의 기댓 수율은 $82.4 \%$로 산출됨.

## 3. [공학적 해석 및 피드백]
- **Learning Curve**: W08 이후의 급격한 수율 상승은 머신러닝 기반의 **이상 탐지 시스템(FDC)** 도입에 따른 조기 진단 결과로 판단됨.
- **Critical Layer**: 메탈 공정에서의 브릿지(Bridge) 결함이 전체 불량의 $40 \%$를 차지하며, 차기 배치(Batch)에서 클리닝 공정 강화를 권고함.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 01_Semiconductor : 반도체 제조 및 설계 마스터 허브

*Created by Flash (HDS Gold V6.3.7 Data Engineering)*
