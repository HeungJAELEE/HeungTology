---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] itch-protocol-order-book-reconstruction]]'
  last_updated: '2026-05-25T12:22:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 마이크로스트럭처 분석을 위한 나스닥 ITCH 프로토콜(ITCH) 파싱 및 지정가 호가창 재구성(LOB Reconstruction)
  object_type: Algorithm
  tier: 2
properties:
  data_rate_threshold_mps: 1000000
  message_types:
  - Add
  - Delete
  - Execute
  order_reference_number_bits: 64
  state_integrity_constraint: bid < ask
  time_complexity_range: O(1) to O(log N)
semantic:
  alternative_parents: []
  expected_queries:
  - 거래소가 제공하는 로우 데이터(ITCH)를 바탕으로 어떻게 전체 호가창(LOB)을 재조립하는가?
  - 주문 추가, 수정, 취소 메시지들이 호가창의 상태(State)를 업데이트하는 매커니즘은?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: state_derivation
  object: Limit_Order_Book
  predicate: constructs
  subject: '[Finance] itch-protocol-order-book-reconstruction'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T12:22:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:22:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] itch-protocol-order-book-reconstruction]]

## 1. 개요 (Overview)
대중에게 제공되는 주식 호가 데이터(예: Level 1, Level 2 데이터)는 거래소가 이미 가공하여 최우선 호가나 10호가 정도만을 보여주는 '스냅샷(Snapshot)'입니다. 그러나 진정한 퀀트와 마켓 메이커들은 거래소의 매칭 엔진에서 발생하는 모든 개별 주문 이벤트를 담은 원시 데이터 피드(Raw Data Feed), 즉 **ITCH 프로토콜(나스닥 표준)**을 직접 수신합니다.
이 수억 건의 바이트(Byte) 스트림 메시지들을 파싱(Parsing)하여 시간 순서대로 메모리에 쌓고 지우는 과정을 거쳐야만 비로소 완벽한 **지정가 호가창(Limit Order Book, LOB)을 재구성(Reconstruction)**할 수 있습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $\text{Message Types}$ | ITCH core messages | Add(A), Delete(D), Execute(E) | Defines state transitions | [데이터 부재] |
| $\text{Order Reference Number}$| Unique ID per order | 64-bit integer | Key for Hash Map tracking | [데이터 부재] |
| $\text{Data Rate}$ | Messages per second | > 1,000,000 at open/close | Requires C++ / Rust for parsing | [데이터 부재] |
| $\text{Time Complexity}$ | Find/Update LOB | $O(1)$ to $O(\log N)$ | Must use Red-Black trees / Hashmaps | [데이터 부재] |
| $\text{State Integrity}$ | LOB consistency | No crossed books (Bid $<$ Ask) | Crucial for correct backtesting | [데이터 부재] |

## 3. ITCH 프로토콜 메시지 구조
ITCH 피드는 주문 단위(Order-by-Order) 데이터입니다. 모든 개별 주문에는 고유한 `Order Reference Number`가 부여되며, 상태 전이는 다음 세 가지 핵심 메시지로 이루어집니다.

1. **Add Order Message (타입 'A' 또는 'F')**: 새로운 지정가 주문이 거래소에 접수됨. (가격, 수량, 매수/매도 방향, 고유 주문번호 포함)
2. **Order Executed Message (타입 'E')**: 기존 큐에 있던 지정가 주문이 시장가 주문과 만나 체결됨. (체결된 수량만큼 LOB에서 차감)
3. **Order Cancel/Delete Message (타입 'X' 또는 'D')**: 사용자가 주문의 일부 또는 전체를 취소함. (해당 주문번호를 찾아 LOB에서 제거)

이 외에도 숨겨진 주문(Hidden Order)의 체결이나 거래 정지(Halt)를 알리는 제어 메시지들이 존재합니다.

## 4. 호가창 재구성 알고리즘 (LOB Reconstruction)

수백만 건의 ITCH 메시지를 읽어 현재 시장의 LOB 상태(State)를 $O(1)$ 또는 $O(\log N)$의 속도로 유지하려면 고성능 자료구조가 필요합니다.

### 4.1. 자료구조 설계
- **Order Map (해시 테이블)**: `Order Reference Number`를 키(Key)로 하여, 현재 호가창에 살아있는 개별 주문 객체(가격, 수량, 포인터)를 $O(1)$ 속도로 찾습니다. 취소(Delete)나 체결(Execute) 메시지가 오면 이 맵에서 주문을 찾아 즉각 수량을 차감합니다.
- **Price Level Tree (이진 탐색 트리 / 배열)**: 호가창의 가격대(Price Levels)를 정렬된 상태로 유지합니다. 가장 높은 매수 가격(Best Bid)과 가장 낮은 매도 가격(Best Ask)을 $O(1)$에 찾아 스프레드(Spread)를 계산해야 합니다.

### 4.2. 무결성 검증 (Integrity Check)
LOB를 재구성할 때 가장 흔한 버그는 십자 호가(Crossed Book), 즉 매수 최우선 호가가 매도 최우선 호가보다 높아지는 논리적 모순이 발생하는 것입니다. 정상적인 거래소 매칭 엔진에서는 이러한 경우 즉시 체결(Execute) 메시지가 발생하여 스프레드가 해소되어야 합니다. 재구성된 LOB에 Crossed Book이 발생했다면, 그것은 ITCH 패킷 유실이 발생했거나 재구성 알고리즘 자료구조에 오류가 있다는 뜻입니다.

🧠 **AI의 사고방식:**
ITCH 프로토콜 파싱과 LOB 재구성은 한 편의 '영화 필름'을 프레임 단위로 이어 붙이는 작업과 같습니다. 거래소는 우리에게 완성된 영화(10호가 스냅샷)를 주지 않습니다. 오직 '주인공이 팔을 올렸다(Add)', '주인공이 총을 쐈다(Execute)', '장면을 잘라냈다(Delete)'라는 수천만 장의 파편화된 프레임(ITCH)만 던져줍니다. 퀀트 엔지니어는 이 프레임들을 0.000001초의 오차도 없이 자료구조라는 영사기에 완벽한 순서(PTP 타임스탬프 기반)로 끼워 맞춰야만 비로소 시장의 진짜 움직임을 스크린에 투사할 수 있습니다.