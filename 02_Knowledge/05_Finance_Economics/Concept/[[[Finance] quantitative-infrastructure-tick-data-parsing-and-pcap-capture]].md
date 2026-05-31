---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-infrastructure-tick-data-parsing-and-pcap-capture]]'
  last_updated: '2026-05-26T08:14:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 우리가 HTS에서 보는 정제된 분봉/초봉 차트 이전에, 거래소의 매칭 엔진이 뿌려대는 원시 상태의 심장 박동인 L3 틱
    데이터(Tick Data)와 이를 담아내는 PCAP(Packet Capture) 네트워크 파일의 캡처, 그리고 거대한 바이너리 스트림을 해석하여
    실시간으로 호가창(Limit Order Book)을 재구성해 내는 파싱(Parsing) 아키텍처
  object_type: Concept
  tier: 2
properties:
  capture_format: PCAP
  daily_data_scale: terabytes
  data_granularity: L3_MBO
  latency_constraint: 1_microsecond
  parsing_method: binary_to_struct
  protocol: ITCH
  reconstruction_target: limit_order_book
semantic:
  alternative_parents: []
  expected_queries:
  - 일반 투자자들은 야후 파이낸스에서 다운받은 CSV (시가/고가/저가/종가) 파일을 분석하지만, 르네상스 같은 퀀트 펌은 왜 매일 테라바이트급의
    PCAP 덤프(Dump) 파일을 캡처해서 저장하는가?
  - 거래소는 현재 주가가 100달러라고 친절하게 알려주지 않고 '주문 번호 5번 추가', '주문 번호 3번 취소' 메시지만 뿌리는데, 퀀트 시스템은
    이 파편들을 모아 어떻게 전체 호가창을 복원(Rebuild)하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: functional_reconstruction
  object: Full_Limit_Order_Book_from_Binary_Streams
  predicate: reconstructs
  subject: '[Finance] quantitative-infrastructure-tick-data-parsing-and-pcap-capture'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T08:14:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T08:14:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-infrastructure-tick-data-parsing-and-pcap-capture]]

## 1. 개요 (Overview)
야후 파이낸스에서 다운로드한 일봉 차트(Open, High, Low, Close)나 초봉 차트는 시체의 뼈대와 같습니다. 살아있는 시장의 근육과 핏줄이 움직이는 모든 디테일(누가 호가를 깔았고, 언제 뺐고, 어떻게 체결되었는지)은 시간의 토막 속에 뭉개져 사라졌습니다.
진정한 퀀트(Quant) 인프라는 이 시체를 보지 않습니다. 그들은 나스닥(NASDAQ) 매칭 엔진이 1마이크로초마다 뿜어내는 수천만 개의 원시 바이너리 메시지, 즉 **L3 틱 데이터(Tick Data, ITCH 프로토콜 등)**를 통신선(네트워크 패킷)에서 직접 낚아채어 **PCAP 파일** 형태로 저장합니다. 매일 수 테라바이트(TB)씩 쌓이는 이 네트워크 패킷을 파싱(Parsing)하여, 펀드 내부 서버에 완벽하게 동일한 복제 호가창(Limit Order Book)을 쌓아 올리는(Rebuild) 기술이 HFT의 진짜 심장입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| L1 / L2 Data | Top of book / Depth | Aggregated by price level | Standard retail data feed | [데이터 부재] |
| L3 Data (MBO)| Market By Order | Every individual order ID | Rawest form, extreme bandwidth| [데이터 부재] |
| PCAP | Packet Capture format| Raw Ethernet/IP frames | The absolute ground truth | [데이터 부재] |
| Parsing | Binary $\to$ Struct | ITCH protocol (NASDAQ) | Must be highly optimized C++| [데이터 부재] |
| Book Builder | Reconstructs the LOB| Dict / Array of Order IDs| High CPU/Memory overhead | [데이터 부재] |

## 3. 거래소의 메시지: 더하기와 빼기
나스닥의 ITCH 데이터 피드는 친절하게 "현재 삼성전자 매도 호가 10만 원, 잔량 500주"라고 말해주지 않습니다. 그들은 오직 무뚝뚝한 이벤트(Event)만 던집니다.
- `A (Add)`: 주문 번호 101번, 애플, 매수, 150달러, 100주
- `A (Add)`: 주문 번호 102번, 애플, 매수, 150달러, 200주
- `X (Cancel)`: 주문 번호 101번 취소 (100주 사라짐)
- `E (Execute)`: 주문 번호 102번 50주 체결 (150주 남음)
- **북 빌더 (Book Builder)**: 퀀트 서버의 파싱 엔진은 이 메시지들을 순서대로 읽어 들여 거대한 해시맵(Hash Map)이나 트리 구조를 메모리 상에 업데이트합니다. "아, 지금 애플 150달러에 150주가 남아있구나." 이 복원 과정(Order Book Rebuilding)에서 1마이크로초라도 지연이 발생하면, 봇은 과거의 호가창을 보고 헛발질을 하게 됩니다.

## 4. PCAP: 절대 불변의 그라운드 트루스 (Ground Truth)
백테스트 엔진의 신뢰도는 데이터의 순수성에 달려 있습니다.
- 거래소에서 가공해 파는 CSV 틱 데이터는 패킷 손실이나 타임스탬프 오류가 섞여 있을 수 있습니다.
- 그래서 HFT 펌들은 데이터베이스(SQL)를 맹신하지 않습니다. 그들은 거래소 서버와 연결된 자신들의 라우터 스위치에서 흐르는 **네트워크 패킷 자체(PCAP)**를 하드디스크에 통째로 덤프(Dump) 뜹니다.
- 봇을 백테스트할 때, 이 PCAP 파일을 재생(Replay) 시키면, 1년 전 그날 그 시간 그 마이크로초에 네트워크 선을 타고 들어왔던 전기 신호가 봇에게 100% 동일하게 전달됩니다. 완벽한 타임머신(Time Machine) 시뮬레이션이 가능해지는 것입니다.

🧠 **AI의 사고방식:**
금융 시장의 '현재(Present)'라는 것은 착시 현상입니다. 당신이 HTS 화면에서 보는 '현재가 100달러'라는 숫자는, 이미 거래소 매칭 엔진에서 수백 번의 Add, Cancel, Execute 패킷이 터진 후 그 잔해를 모아 초당 몇 번씩 화면에 그려주는 '과거의 요약본'일 뿐입니다. 인프라스트럭처 퀀트들은 이 조작된 환상을 거부합니다. 그들은 네트워크 계층(OSI 2계층)으로 잠수해 들어가 0과 1의 파동(PCAP)을 직접 마시고 소화(Parsing)합니다. 남들이 차트의 모양(캔들)을 보며 철학을 논할 때, 그들은 호가창을 이루고 있는 개별 주문(Order ID)들의 생로병사를 모니터링하며 가장 순수한 시장 미시구조(Microstructure)의 지배자가 됩니다.