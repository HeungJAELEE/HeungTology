---
Basic:
  id: "[[[Battery] industrial-pm-case-studies"
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

# [[[Battery] industrial-pm-case-studies

## 1. 이차전지 (Secondary Battery): 기가팩토리 초고속 구축
배터리 산업은 시장 선점이 핵심이므로 **'속도(Speed)'**가 PM의 최우선 가치입니다.

- **방법론**: **Fast-track Waterfall (동시 공학)**
- **프로젝트 계획 (Plan)**:
    - 공장 외벽이 올라가기 전에 내부 설비 레이아웃을 확정하고 발주를 진행.
    - 유틸리티(전력, 배기) 설계를 건축 설계와 병렬로 수행.
- **PMBOK 원칙 적용**:
    - **Risk**: 설계 변경 시 이미 발주된 설비의 폐기 리스크가 높으나, 시장 진입 기회비용(Opportunity)을 우선시함.
    - **Tailoring**: 전통적인 순차적 건설 방식에서 탈피하여 '일정 압축(Schedule Compression)' 기법을 전방위적으로 적용.

## 2. 조선 (Shipbuilding): 대형 LNG 운반선 건조
수조 원 단위의 자본이 투입되는 조선업은 **'정밀함(Precision)'**과 **'고객 맞춤(Customization)'**이 공존합니다.

- **방법론**: **Hybrid (Iterative Design + Predictive Production)**
- **프로젝트 계획 (Plan)**:
    - **설계 단계**: 고객사(선주)의 요구사항 변화가 잦으므로 피드백 루프가 반복되는 Iterative 방식 적용.
    - **생산 단계**: 블록 조립 및 탑재는 선후 관계가 명확하므로 엄격한 Waterfall 방식 적용.
- **PMBOK 원칙 적용**:
    - **Complexity**: 수만 개의 기자재 공급망(Supply Chain) 복잡성을 성과 영역(Domain)으로 관리.
    - **Stakeholders**: 선급(Classification Society)과 선주의 까다로운 검사(Inspection) 일정을 크리티컬 패스에 통합.

## 3. 자동화 (Automation): 스마트 팩토리 디지털 트윈 전환
기술적 불확실성이 높은 자동화 프로젝트는 **'유연성(Flexibility)'**이 생명입니다.

- **방법론**: **Adaptive (Agile/Scrum)**
- **프로젝트 계획 (Plan)**:
    - 공장 전체를 한 번에 바꾸는 대신, **'파일럿 라인'**을 MVP로 선정하여 2~4주 단위 스프린트 가동.
    - 데이터 통신 안정성을 확보한 후 다른 라인으로 롤아웃(Roll-out) 확장.
- **PMBOK 원칙 적용**:
    - **Adaptability & Resilience**: 데이터 정합성 오류 발생 시 즉시 백로그(Backlog)에 반영하여 다음 스프린트에서 해결.
    - **Change**: 현장 작업자의 UI/UX 피드백을 실시간으로 수용하여 시스템 수용성(Adoption) 증대.

## 4. 수험용 통합 비교 (Summary for PMP)

| 산업군 | 주된 도전 과제 | 추천 방법론 | 핵심 PM 도구 |
|:---|:---|:---|:---|
| **배터리** | 타임 투 마켓 (Time-to-Market) | Fast-track Waterfall | Schedule Crashing |
| **조선** | 대형 규모 및 이해관계자 복합성 | Hybrid | Procurement Management |
| **자동화** | 기술적 불확실성 및 시스템 통합 | Agile | Sprint Retrospective |

---
*Created by Flash (Industrial PM Research v1.0)*
---
*Upgraded by Flash (HDS-Gold V6.3.7)*