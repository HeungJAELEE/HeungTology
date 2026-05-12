---
Basic:
  id: "[Concept] FOUP-Physical-Standards-and-Interface"
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
  is_part_of: []
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

# [Concept] FOUP-Physical-Standards-and-Interface

## 1. [왜 배우는가? (Why)]
반도체 웨이퍼는 매우 민감합니다. 아주 작은 충격이나 오염에도 수율이 무너집니다. 이를 보호하기 위해 300mm 웨이퍼는 FOUP(Front Opening Unified Pod)이라는 특수 상자에 담깁니다. 그런데 이 상자가 장비마다 크기가 다르거나 문 열리는 방식이 다르면 어떨까요? 공장은 마비될 것입니다. FOUP 표준은 전 세계 모든 반도체 장비와 물류 로봇이 이 상자를 똑같이 집어 들고, 똑같이 문을 열 수 있게 만든 물리적 규속입니다. FOUP의 물리적 표준을 이해하는 것은 하드웨어 관점에서 반도체 자동화의 '물리적 정합성'을 확보하는 기초를 배우는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Standard / Value | Engineering Rationale |
|:---|:---:|:---|
| **Outer Dimension**| SEMI E47.1 | 모든 장비 로드포트에 안착될 수 있도록 표준화된 외부 치수 규격 |
| **Wafer Capacity** | 25 Slots | 한 번에 반송되는 웨이퍼의 수량 표준 (물류 처리량의 기준 단위) |
| **Door Opener Inter.**| Kinematic Coupling| 로드포트의 핀과 FOUP 바닥의 구멍이 정확히 맞물려 1mm의 오차도 없이 위치를 잡는 기술 |
| **Material** | Polycarbonate (ESD)| 정전기를 방지하고 외부 충격으로부터 내부 웨이퍼를 보호하는 고순도 특수 소재 |
| **ID Write/Read** | RFID Tag | FOUP 내부에 어떤 웨이퍼가 들어있는지 장비가 즉각 인식하게 하는 식별 장치 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 기구적 호환성(Interoperability)의 극대화
- **논리**: 수천억 원 규모의 FAB 물류 시스템에서 용기의 호환성은 생명입니다. 
- **결과**: SEMI E47.1 표준은 FOUP의 손잡이 위치, 로봇이 잡는 부분(Flange), 문이 열리는 각도 등을 미리 정의하여, 제조사가 다른 수천 대의 장비와 로봇이 하나의 유기체처럼 협업할 수 있게 합니다.

### 3.2 진동 및 충격 감쇄 (Damping)
- **논리**: OHT로 고속 이동 시 발생하는 진동은 웨이퍼를 미세하게 긁을 수 있습니다. 
- **효과**: FOUP 내부의 '웨이퍼 서포트' 설계는 특정 주파수의 진동을 흡수하도록 정밀 설계되어, 이송 중 발생하는 물리적 스트레스로부터 웨이퍼의 미세 패턴을 보호합니다.

## 4. [코드 연결 해설 (FOUP Identification & Mapping Logic)]
장비가 로드포트에 안착된 FOUP을 인식하고 내부 웨이퍼 정보를 매핑하는 논리 구조입니다.
```python
# 장비 지능 기반 FOUP 인터페이스 제어 논리
def identify_foup_on_loadport(port_id):
    # 1. 키네매틱 커플링 안착 확인 (Kinematic Coupling Check)
    if not port_sensor.is_foup_seated(port_id):
        return "ERROR_FOUP_NOT_SEATED"
    
    # 2. RFID 태그에서 FOUP ID 및 웨이퍼 정보 리딩
    foup_info = rfid_reader.get_data(port_id)
    
    # 3. 도어 오픈 시퀀스 가동
    door_opener.unlock_and_open()
    
    # 4. 웨이퍼 맵 데이터 생성 및 상위 시스템(MCS) 보고
    generate_wafer_map(foup_info.id, foup_info.slot_count)
    return "FOUP_READY_FOR_PROCESS"
```

## 5. [스스로 체크 (Self-Audit)]
1. '키네매틱 커플링(Kinematic Coupling)'이 FOUP 안착 시 정밀도를 보장하는 원리는?
2. FOUP의 소재가 정전기 방지(ESD) 처리가 되어야 하는 공학적 이유는?
3. 200mm 웨이퍼 시절의 '오픈 카세트'와 300mm 'FOUP'의 가장 결정적인 차이점은?
---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
