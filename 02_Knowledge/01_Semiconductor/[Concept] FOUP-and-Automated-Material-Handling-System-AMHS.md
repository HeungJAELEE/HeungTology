---
Basic:
  date: '2026-05-12'
  domain: Unknown_Domain
  id: '[Concept] FOUP-and-Automated-Material-Handling-System-AMHS'
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
  - Assistant to an Antigravity industrial process engineer.
  - A technical document titled "[Concept] FOUP-and-Automated-Material-Handling-System-AMHS".
  - Create 5 expected queries for searching this document later.
  - Queries must be specific and practical/professional (실무적).
  - Must end with a '?'.
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

# [Concept] FOUP-and-Automated-Material-Handling-System-AMHS

## 1. [왜 배우는가? (Why)]
반도체 공장은 사람보다 로봇이 더 바쁘게 움직이는 곳입니다. 천장에는 레일을 따라 달리는 OHT(Overhead Hoist Transport)가 수천 대 돌아다니고, 웨이퍼는 FOUP(Front Opening Unified Pod)이라는 특수 용기에 담겨 안전하게 운반됩니다. AMHS(Automated Material Handling System)는 이 거대한 물류 흐름을 관리하는 자율 지능 체계입니다. FOUP과 AMHS를 이해하는 것은 웨이퍼 한 장도 깨지지 않고 오염되지 않게 공장 구석구석으로 배달하는 '반도체 공장의 혈류'를 배우는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Technology / Logic | Engineering Rationale |
|:---|:---:|:---|
| **FOUP** | 300mm Sealed Pod | 25장의 웨이퍼를 담아 외부 오염으로부터 완벽히 차단하는 밀폐 용기 표준 |
| **OHT** | Linear Motor Drive | 천장 레일을 따라 고속(최대 5m/s)으로 이동하며 웨이퍼를 반송하는 로봇 |
| **N2 Purging** | Oxidation Control | FOUP 내부에 질소를 주입하여 산소와 습도를 제거, 웨이퍼 산화 방지 |
| **Stocker** | Buffer Storage | 공정 대기 중인 FOUP을 보관하고 순서를 조율하는 자동 보관 창고 |
| **MCS** | Material Control Sys| 모든 OHT의 이동 경로를 최적화하고 정체를 방지하는 중앙 관제 소프트웨어 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 국소 환경(Mini-environment)의 완성
- **논리**: 공장 전체를 극도로 깨끗하게 유지하는 것은 비경제적입니다. 
- **결과**: 웨이퍼를 FOUP이라는 밀폐 공간에 가둬서 이동시킴으로써, 공장 전체의 청정도는 낮추고 웨이퍼 주변의 청정도는 Class 1로 유지하여 설비 투자비와 운영비를 대폭 절감합니다.

### 3.2 반송 정체 방지 알고리즘 (Deadlock Avoidance)
- **논리**: 수천 대의 OHT가 레일 위에서 꼬이면 공장 전체가 멈춥니다. 
- **효과**: AMHS의 제어 엔진(MCS)은 실시간 교통량과 장비 가동 상태를 분석하여 최단 경로를 배정하고 교차로에서의 정체를 방지하는 알고리즘을 통해 물류 처리량(Throughput)을 극대화합니다.

## 4. [코드 연결 해설 (OHT Routing & FOUP Purging Logic)]
OHT에게 목적지를 부여하고 FOUP 내부의 질소 농도를 관리하는 논리 구조입니다.
```python
# 물류 지능 기반 AMHS 및 FOUP 제어 논리
def control_fab_logistics(foup_id, destination_tool):
    # 1. 최적 반송 경로 계산
    path = mcs_engine.calculate_shortest_path(foup_id, destination_tool)
    
    # 2. OHT에게 명령 하달
    oht_robot.dispatch(foup_id, path)
    
    # 3. 이동 중 FOUP 내부 환경 감시
    if foup_id.humidity > 5.0:
        # 질소 퍼징 시스템 가동하여 습도 조절
        purging_system.start_n2_injection(foup_id)
        return "PURGING_ACTIVE_AND_MOVING"
        
    return "MOVING_TO_DESTINATION"
```

## 5. [스스로 체크 (Self-Audit)]
1. 반도체 웨이퍼를 '오픈 카세트'가 아닌 'FOUP'에 담아 운반해야 하는 결정적인 이유는?
2. 'OHT'가 'AGV'나 'AMR'보다 반도체 공장(FAB) 물류에 더 많이 쓰이는 기술적 배경은? (힌트: 공간 효율성)
3. 'Stocker'가 단순히 보관을 넘어 '생산 계획(Scheduling)'에 기여하는 바는?
---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**