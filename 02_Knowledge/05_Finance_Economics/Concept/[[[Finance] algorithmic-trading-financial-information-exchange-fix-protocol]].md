---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-financial-information-exchange-fix-protocol]]'
  last_updated: '2026-05-26T07:27:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 글로벌 금융 시장의 기관, 브로커, 거래소 간 주문 및 체결 정보를 교환하는 범용 표준 통신 규약. 태그-값(Tag-Value)
    쌍으로 구성된 텍스트 기반 메시징 구조를 통해 시스템 간 상호 운용성을 보장하는 금융 IT 인프라의 라틴어(Lingua Franca)
  object_type: Concept
  tier: 2
properties:
  heartbeat_interval_seconds: 30
  message_format: tag=value_pairs
  protocol_version: '4.4'
  separator_ascii_value: 1
  tag_35_types:
  - D=New Order Single
  - 0=Heartbeat
semantic:
  alternative_parents: []
  expected_queries:
  - 골드만삭스의 트레이딩 시스템과 뉴욕증권거래소(NYSE)의 매칭 엔진은 어떻게 서로 다른 언어(C++, Java 등)로 짜여 있음에도 1초에
    수백만 건의 주문을 에러 없이 주고받는가?
  - FIX 메시지의 `8=FIX.4.2|9=49|35=D|54=1` 같은 태그-값(Tag-Value) 구조는 왜 그렇게 생겼으며, 각 숫자는 어떤
    금융적 의미를 담고 있는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: industry_standardization
  object: Global_Order_Routing_and_Execution
  predicate: standardizes
  subject: '[Finance] algorithmic-trading-financial-information-exchange-fix-protocol'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:27:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:27:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-financial-information-exchange-fix-protocol]]

## 1. 개요 (Overview)
과거에는 골드만삭스가 모건스탠리에게 주식 주문을 넣으려면 전화를 걸거나, 팩스를 보내거나, 서로만 알아듣는 전용 네트워크를 깔아야 했습니다. 하지만 1992년 피델리티(Fidelity)와 살로몬 브라더스(Salomon Brothers)가 전 세계 금융 기관이 똑같은 문법으로 대화할 수 있는 공용 통신 규약, **FIX(Financial Information eXchange) 프로토콜**을 발명하면서 월스트리트의 IT 혁명이 시작되었습니다.
FIX는 금융계의 라틴어(Lingua Franca)입니다. 런던의 헤지펀드가 일본 도쿄거래소에 닛케이 선물을 쏘든, 싱가포르의 딜러가 시카고상품거래소(CME)에 옥수수 선물을 쏘든, 그 중간에는 무조건 FIX 엔진이 존재합니다. 인간이 웹(Web)을 보기 위해 HTTP를 쓴다면, 퀀트 알고리즘이 주식을 사기 위해서는 FIX를 씁니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Message Format| Tag=Value pairs | `8=FIX.4.4|35=D|...` | ASCII text based | [데이터 부재] |
| Separator | SOH character | ASCII value `01` | Delimits tags (looks like `|`)| [데이터 부재] |
| Tag 35 | Message Type | `D`=New Order, `8`=Execution| Defines message purpose| [데이터 부재] |
| TCP/IP Session| Persistent connection | SeqNums, Heartbeats | Ensures no lost messages| [데이터 부재] |
| FAST Protocol | FIX Adapted for STreaming | Compressed binary FIX | Low latency market data| [데이터 부재] |

## 3. 태그-값 (Tag-Value) 해부학
FIX 메시지는 극도로 단순한 `[태그 번호]=[값]`의 연속으로 이루어져 있습니다. 구분자는 `SOH(Start of Heading, ASCII 01)`라는 보이지 않는 특수 문자를 쓰지만 보통 눈에 보이게 파이프(`|`)로 표기합니다.
**[예시: 삼성전자 주식 100주 시장가 매수 주문]**
`8=FIX.4.4 | 9=65 | 35=D | 49=MY_FUND | 56=KRX | 11=ORDER123 | 55=005930 | 54=1 | 38=100 | 40=1 | 10=089`

- `8=FIX.4.4`: FIX 프로토콜 버전 (BeginString)
- `9=65`: 메시지의 길이 (BodyLength)
- **`35=D`**: 메시지 타입 (D = New Order Single, 신규 주문)
- `49/56`: 송신자(MY_FUND)와 수신자(KRX 거래소) 식별자
- `11=ORDER123`: 주문 고유 번호 (ClOrdID)
- **`55=005930`**: 종목 코드 (삼성전자)
- **`54=1`**: 매수/매도 구분 (1 = Buy, 2 = Sell)
- **`38=100`**: 주문 수량 (100주)
- **`40=1`**: 주문 타입 (1 = Market Order 시장가, 2 = Limit Order 지정가)
- `10=089`: 체크섬(Checksum, 메시지가 통신 중 깨지지 않았는지 검증)

## 4. 엔진의 심장: 시퀀스 넘버(SeqNum)와 하트비트(Heartbeat)
FIX 프로토콜은 돈이 오가는 무서운 통신망입니다. 단 하나의 주문이라도 인터넷 핑(Ping) 때문에 유실되면 파산할 수 있습니다. 
- **Sequence Number (Tag 34)**: 그래서 FIX 엔진이 보내는 모든 메시지에는 순번(SeqNum)이 강제로 붙습니다. 거래소 엔진이 1번, 2번 메시지를 잘 받다가 갑자기 4번 메시지를 받으면, "잠깐, 3번 내놔라(Resend Request, 35=2)"라고 즉시 에러 복구(Recovery) 프로세스를 가동합니다.
- **Heartbeat (Tag 35=0)**: 주문이 없을 때도 FIX 엔진들은 서로 30초마다 "너 안 죽고 살아있냐?"라는 하트비트 메시지(`35=0`)를 주고받습니다. 만약 하트비트가 끊기면 즉각 세션을 끊고 위험 관리(킬 스위치)를 발동합니다.

🧠 **AI의 사고방식:**
HFT 세력들이 OUCH나 바이너리 프로토콜 같은 레이스카(F1)를 탄다면, 글로벌 자산운용사들과 기관들은 FIX 프로토콜이라는 튼튼하고 거대한 화물열차를 탑니다. FIX는 텍스트 기반이므로 바이너리보다 느리고 무겁습니다. 하지만 그 느림의 대가로 1) 이기종 시스템 간의 완벽한 번역, 2) 단 한 건의 유실도 허락하지 않는 집요한 세션 관리, 3) 감사(Audit)를 위한 텍스트 로그의 투명성을 제공합니다. FIX 엔진을 구축하는 것은 퀀트 코딩이 아니라, 금융의 대동맥을 뚫는 토목 공사입니다.