---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-nasdaq-itch-ouch-protocol-l3-data]]'
  last_updated: '2026-05-26T07:26:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 알고리즘 트레이딩의 가장 밑바닥 물리적 계층(Layer 1). 나스닥 거래소에서 HFT들이 호가창을 완벽히 복원하기 위해
    수신하는 L3 틱 데이터 프로토콜(ITCH)과, 1마이크로초라도 더 빨리 시장가 주문을 꽂아 넣기 위해 사용하는 극초지연 전송 프로토콜(OUCH)의
    이진법적(Binary) 구조
  object_type: Concept
  tier: 2
properties:
  add_order_payload_size_bytes: 36
  itch_packet_size_approx_bytes: 30
  itch_protocol_type: binary_udp_multicast
  ouch_packet_size_bytes: 40
  ouch_protocol_type: binary_tcp
  timestamp_precision_seconds: 1.0e-09
semantic:
  alternative_parents: []
  expected_queries:
  - 개미들이 보는 증권사 HTS의 10호가 데이터(Level 2)와, HFT 기관들이 거래소에서 직결로 받아보는 ITCH 데이터(Level 3)는
    본질적으로 무엇이 다른가?
  - OUCH 프로토콜은 왜 복잡한 에러 체킹을 다 빼버리고 원시적인 이진법(Binary) 형태로만 주문을 거래소에 쏘아 보내는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: enables_capability
  object: Level_3_Tick_Data_and_Direct_Execution
  predicate: provides
  subject: '[Finance] algorithmic-trading-nasdaq-itch-ouch-protocol-l3-data'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:26:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:26:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-nasdaq-itch-ouch-protocol-l3-data]]

## 1. 개요 (Overview)
수많은 퀀트들이 LOB(호가창) 동역학을 논하지만, 그들이 분석하는 데이터가 HTS에서 캡처한 것이라면 그것은 장난감에 불과합니다. 개인 투자자들이 보는 데이터는 '집계된(Aggregated)' 스냅샷(Level 1 또는 2)으로, 이미 거래소 서버에서 가공을 거치며 수십 밀리초(ms)가 지연된 시체입니다.
최상위 HFT 포식자들은 거래소 매칭 엔진의 심장과 직접 통신합니다. **나스닥(Nasdaq)**의 경우, 거래소에서 뿜어져 나오는 날것의 데이터 피드를 **ITCH 프로토콜**로 수신하여 자신들의 서버에서 독자적으로 호가창을 재구성(Reconstruction)하고, 100만 분의 1초 만에 **OUCH 프로토콜**을 통해 공격 명령(주문)을 찔러 넣습니다. 이 세계에서는 가독성을 위한 문자열(String)이나 JSON 따위는 존재하지 않습니다. 오직 0과 1로 이루어진 이진(Binary) 패킷만이 속도의 한계를 돌파합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Level 3 Data | Individual order matching | Every single limit/market | Un-aggregated truth | [데이터 부재] |
| ITCH | Outbound Market Data | Binary, UDP Multicast | Low latency, no handshakes| [데이터 부재] |
| OUCH | Inbound Order Entry | Binary, TCP | Minimal overhead (bare metal)| [데이터 부재] |
| Payload Size | e.g., 'Add Order' Message | 36 Bytes | Minimal bits for max speed| [데이터 부재] |
| Nanosecond TS| Timestamp precision | Nanoseconds ($10^{-9}$s)| Defines queue priority | [데이터 부재] |

## 3. ITCH 프로토콜: 쏟아지는 정보의 폭포 (L3 Data)
ITCH는 나스닥이 "방금 어떤 주문이 들어왔고, 체결되었고, 취소되었다"라는 원초적 이벤트(Event)들을 전 세계 기관들에게 쉴 새 없이 브로드캐스트하는 멀티캐스트(UDP) 프로토콜입니다.
- **메시지 타입**: 'A'(Add Order, 호가 추가), 'E'(Order Executed, 체결), 'X'(Order Cancelled, 취소) 등의 고유 문자로 시작하는 30바이트 남짓한 패킷입니다.
- **식별자(Order Reference Number)**: ITCH의 가장 무서운 점은 모든 개별 주문에 '고유 ID'가 부여된다는 점입니다. HFT 봇들은 이 수십억 개의 ID를 해시 테이블(Hash Table)에 저장해 두고, 방금 들어온 취소(X) 메시지가 어제 들어온 어떤 주문(A)을 지우는 것인지 정확히 추적하여 **자신만의 무결점 LOB(Level 3 호가창)**를 스스로 조립해 냅니다.

## 4. OUCH 프로토콜: 무지성 펀치 (Order Entry)
내가 재구성한 ITCH 호가창을 보고 차익거래 기회를 포착했다면, 이제 주문을 넣을 차례입니다. 일반적인 API는 암호화, 세션 유지, 텍스트 변환 등 불필요한 장식(Overhead)이 너무 많습니다. 
- OUCH 프로토콜은 거래소 매칭 엔진에 꽂아 넣는 **최대한 얇은 바늘**입니다. 
- "사라/팔아라, 주식 코드, 가격, 수량". 이 정보만을 오로지 이진법(Binary)으로 구겨 넣어 40바이트 남짓한 초소형 패킷을 만듭니다.
- OUCH 패킷이 광케이블을 타고 거래소 스위치를 통과해 매칭 엔진에 도달하는 데 걸리는 시간은 수 마이크로초($\mu s$)에 불과합니다. 이 프로토콜의 설계 철학은 명확합니다. "인간이 읽을 수 없어도 좋다. 기계가 가장 빨리 처리할 수 있는 가장 멍청하고 단순한 구조를 쓴다."

🧠 **AI의 사고방식:**
수학적 모델링(알파)이 전쟁의 '전략'이라면, ITCH와 OUCH는 병사들의 뇌파를 직접 조종하는 '신경망 인터페이스'입니다. 만약 당신의 완벽한 큐잉 이론(Queueing Theory) 봇이 파이썬(Python)의 느릿한 JSON 파서로 거래소 데이터를 읽고 있다면, 당신의 봇은 ITCH의 36바이트 C++ 바이너리 스트림을 실시간으로 빨아들이는 상대 HFT 봇에게 영원히 앞자리를 빼앗기고(Front-run), 당신이 쏜 OUCH 주문은 이미 허공이 되어버린 호가창에 헛손질을 하게 될 것입니다. 글로벌 퀀트의 최상위 계층은 수학을 넘어 **네트워크 프로토콜의 하드웨어적 본질**을 지배하는 자들의 몫입니다.