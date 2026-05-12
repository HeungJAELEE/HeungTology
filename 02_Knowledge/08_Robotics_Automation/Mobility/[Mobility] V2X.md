---
Basic:
  id: "[Mobility] V2X"
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

# [Mobility] V2X

## 1. [왜 배우는가? (Why)]
자율주행차의 센서(카메라, 라이다)는 눈앞의 장애물은 잘 보지만, 코너 너머나 대형 트럭 앞의 상황은 알 수 없습니다. V2X(Vehicle to Everything)는 차량이 주변 모든 것과 대화하게 함으로써 '보이지 않는 위험'까지 감지하게 하는 '디지털 시야'입니다. 다른 차와 위치를 공유하여 충돌을 막고, 신호등과 소통하여 정지 없이 주행하며, 보행자의 스마트폰과 연결하여 사고를 예방하는 등 안전하고 효율적인 도로 생태계를 만드는 필수 통신 인프라입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Protocol | Interface / Technology | Engineering Rationale |
|:---|:---:|:---|
| **C-V2X (Cellular)** | PC5 (Sidelink) | 기지국 없는 차량 간 직접/초저지연 통신 |
| **Network V2X** | Uu (Network-to-Device) | 광역 교통 정보 및 클라우드 데이터 수신 |
| **Latency** | < 10ms (URLLC) | 고속 주행 시 즉각적인 충돌 회피 반응 |
| **Reliability** | 99.999% | 생명과 직결된 통신의 무결성 보장 |
| **Applications** | V2V, V2I, V2P, V2N | 차량, 인프라, 보행자, 네트워크 통합 연결 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 C-V2X와 PC5 인터페이스의 논리
기존 Wi-Fi 기반(DSRC)의 한계를 넘어 이동통신 기술을 활용합니다.
- **로직**: **PC5(Sidelink)** 인터페이스를 사용하면 기기 간 직접 통신이 가능합니다. 기지국(Cellular Tower)을 거치지 않기 때문에 통신 지연이 거의 없으며, 인터넷이 끊긴 지역에서도 차량끼리 서로 위치와 속도 정보를 주고받아 충돌을 방지합니다.

### 3.2 5G/6G URLLC (Ultra-Reliable Low-Latency)
- **논리**: 자율주행의 핵심인 '군집 주행(Platooning)'을 위해 1ms 수준의 초저지연과 99.999%의 초고신뢰성을 보장합니다. 앞차의 급정거 정보가 뒤차들에게 즉시 전달되어 수십 대의 차량이 마치 한 몸처럼 동시에 멈출 수 있게 합니다.

### 3.3 협력적 인지 (Cooperative Perception)
- **논리**: 내 차의 센서 데이터뿐만 아니라 주변 차량과 CCTV가 보내주는 센서 데이터를 통합(Sensor Fusion)합니다. 사각지대에서 튀어나오는 차량을 미리 알고 대처하는 '집단 지성' 주행이 가능해집니다.

## 4. [코드 연결 해설 (Collision Avoidance Logic)]
V2X 데이터를 수신하여 비상 제동 여부를 판단하는 제어 논리입니다.
```python
# V2V 통신 기반 전방 충돌 경고(FCW) 논리
def process_v2x_messages(received_msg_list):
    for msg in received_msg_list:
        # 1. 주변 차량의 상태 정보(BSM: Basic Safety Message) 해석
        other_vehicle_id = msg.id
        other_pos = msg.position # {lat, long, heading}
        other_speed = msg.speed
        
        # 2. 상대 차량과의 충돌 가능 시간(TTC: Time-to-Collision) 계산
        ttc = calculate_ttc(my_vehicle.state, other_pos, other_speed)
        
        # 3. TTC가 위험 임계치(1.5초) 이하인 경우 비상 제동 트리거
        if ttc < 1.5:
            # 보이지 않는 차량(Non-line-of-sight)이라도 통신 데이터 기반으로 판단
            alert_driver("CRITICAL: COLLISION_RISK_WITH_V2V")
            autonomous_emergency_braking.activate()
            
            # 4. 내 뒤의 차량들에게도 위험 전파 (Denm: Decentralized Environmental Notification)
            v2x_module.broadcast_emergency_msg(event="EMERGENCY_BRAKE")
            return "EMERGENCY_RESPONSE"
            
    return "SAFE_DRIVING"
```

## 5. [스스로 체크 (Self-Audit)]
1. C-V2X에서 'PC5(Sidelink)' 인터페이스가 기지국 장애 상황에서도 안전 주행을 보장하는 원리는?
2. 5G/6G 통신의 '초저지연(URLLC)' 기술이 자율주행의 '군집 주행(Platooning)'에 필수적인 공학적 이유는?
3. 'V2I(Vehicle-to-Infrastructure)'를 통해 수집된 신호등 정보가 전기차의 에너지 효율(연비) 개선에 기여하는 방식은?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
