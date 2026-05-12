---
Basic:
  id: "[[[Strategy] Bottleneck-Analysis-Theory-and-Throughput-Maximization"
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

# [[[Strategy] Bottleneck-Analysis-Theory-and-Throughput-Maximization

## 1. [왜 배우는가? (Why)]]
공장 전체의 생산 속도는 가장 느린 장비 하나에 의해 결정됩니다. 아무리 다른 장비들이 빨리 돌아가도, 중간에서 한 곳이 막히면(Bottleneck) 전체 생산량은 늘어나지 않고 재고만 쌓입니다. 병목 분석(Bottleneck Analysis)은 공장이라는 거대한 강물에서 흐름을 방해하는 '바위'를 찾아내는 기술입니다. 병목을 해결하는 것이야말로 돈을 가장 적게 들이고 생산량을 가장 많이 늘릴 수 있는 지름길입니다. 이를 이해하는 것은 공정 전체를 꿰뚫어 보고 최소 투자로 최대 효과를 내는 '운영 최적화 지능'을 마스터하는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Concept | Action / Logic | Engineering Rationale |
|:---|:---:|:---|
| **Bottleneck ID** | Utilization Peak | 가동률이 100%에 가깝고 그 앞에 재고(WIP)가 가장 많이 쌓여있는 공정 식별 |
| **TOC** | Theory of Constraints | 전체 시스템의 성과는 소수의 제약 요인(병목)에 의해 결정된다는 경영 철학 |
| **Exploit** | Maximize Const. | 병목 장비가 단 1분도 쉬지 않도록 최우선적으로 관리하고 지원하는 전략 |
| **Subordinate** | Sync Non-const. | 병목이 아닌 공정들은 병목 공정의 속도에 맞춰 생산 속도를 조절하는 원칙 |
| **Elevate** | Capacity Expansion | 공정 개선으로도 해결 안 될 때, 추가 설비를 도입하여 병목의 절대 용량을 키우는 단계 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 국부 최적화와 전체 최적화의 충돌
- **논리**: 병목이 아닌 장비를 더 빨리 돌리면 재고만 늘어나고 비용만 발생합니다. 
- **결과**: 병목 분석 전략은 '전체 최적화'를 추구합니다. 병목 공정의 1시간 손실은 공장 전체의 1시간 손실과 같으며, 비병목 공정의 1시간 단축은 전체 시스템 관점에서 아무런 가치가 없음을 숫자로 증명합니다.

### 3.2 리틀의 법칙(Little's Law)과 리드 타임
- **논리**: 재고가 많을수록 제품이 공장을 빠져나가는 시간(Lead Time)은 길어집니다. 
- **효과**: 병목을 분석하여 흐름을 일정하게 유지하면, 공정 내 재고(WIP)를 획기적으로 줄일 수 있습니다. 이는 제품 출시 속도를 높이고 공장의 현금 흐름(Cash Flow)을 개선하는 강력한 경제적 효과로 이어집니다.

## 4. [코드 연결 해설 (Bottleneck Identification & WIP Monitoring Logic)]
실시간 공정 데이터를 분석하여 현재 어디가 병목인지 찾아내는 논리 구조입니다.
```python
# 전략 지능 기반 공정 병목 탐지 및 최적화 논리
def identify_manufacturing_bottleneck(process_line_data):
    # 1. 각 공정별 설비 가동률(Utilization) 및 대기 재고(WIP) 추출
    # data: [{"step": "ETCH", "util": 0.98, "wip": 500}, {"step": "CLEAN", "util": 0.45, "wip": 10}]
    
    # 2. 병목 지수(Bottleneck Index) 산출
    # 지수 = (가동률 * 0.7) + (WIP_Normalized * 0.3)
    max_index = -1
    bottleneck_step = None
    
    for step in process_line_data:
        index = (step["util"] * 0.7) + (normalize(step["wip"]) * 0.3)
        if index > max_index:
            max_index = index
            bottleneck_step = step
            
    # 3. 병목 해소 전략 제안
    if max_index > 0.90:
        return {
            "bottleneck": bottleneck_step["step"],
            "action": "EXPLOIT_IMMEDIATELY",
            "suggestion": "ENSURE_MATERIAL_AVAILABILITY_AND_PREVENTIVE_MAINTENANCE"
        }
    return "FLOW_IS_BALANCED"
```

## 5. [스스로 체크 (Self-Audit)]
1. "비병목 공정의 1시간 개선은 신기루에 불과하다"라는 말의 공학적 의미는?
2. 병목 공정 앞에 항상 일정량의 재고(Buffer)를 두어야 하는 이유는?
3. 병목을 해결했더니 다른 공정이 새로운 병목이 되는 현상을 무엇이라 부르는가?
---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
