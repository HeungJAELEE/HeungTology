---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-infrastructure-backtesting-engine-and-event-driven-architecture]]'
  last_updated: '2026-05-26T08:17:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 파이썬 Pandas로 대충 돌려보는 벡터화(Vectorized) 백테스트의 심각한 오류(미래 누수, 체결 보장 착각)를
    부수고 실전과 똑같은 매매 환경을 시뮬레이션하기 위해, 틱 데이터 패킷을 실시간 이벤트(Event)로 흘려보내며 매칭 엔진까지 모사하는 엔터프라이즈급
    이벤트 기반(Event-Driven) 백테스팅 아키텍처
  object_type: Concept
  tier: 2
properties:
  event_driven_speed_scale: hours/days
  latency_modeling_delay_ms: 5
  vectorized_speed_scale: seconds
semantic:
  alternative_parents: []
  expected_queries:
  - 파이썬에서 데이터프레임(Pandas)으로 주가 차트의 골든크로스를 계산해 짰더니 백테스트 수익률이 연 100%가 나오는데, 왜 실전 라이브
    서버에 올리면 매일 돈을 잃는가?
  - 일류 퀀트 펌들은 백테스트 엔진(Backtester)을 짤 때 왜 귀찮게 큐(Queue)와 틱 데이터를 하나씩 넘기는 이벤트 기반(Event-Driven)
    루프를 C++로 직접 구축하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_mitigation
  object: Lookahead_Bias_and_Unrealistic_Fills
  predicate: eliminates
  subject: '[Finance] quantitative-infrastructure-backtesting-engine-and-event-driven-architecture'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T08:17:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T08:17:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-infrastructure-backtesting-engine-and-event-driven-architecture]]

## 1. 개요 (Overview)
초보 퀀트의 99%는 파이썬의 `pandas` 라이브러리를 열고 과거 5년 치 주가를 배열(Array)로 불러옵니다. 그리고 배열 전체를 한 번에 연산(Vectorized)하여 "어제 5일 이평선이 20일 이평선을 돌파했으면 오늘 시가로 매수"라는 코드를 짭니다. 결과는 연 100% 수익률입니다. 
그러나 이는 **가짜 백테스트(Fake Backtest)**입니다. 벡터화 백테스트는 내 주문이 시장에 던져졌을 때 체결이 될지 안 될지를 모조리 무시하며(100% 체결 보장 착각), 배열 계산 중 무심코 미래의 데이터를 앞당겨 참조해 버리는 **미래 정보 누수(Look-ahead Bias)**의 온상입니다. 이 환상을 찢기 위해 탑 티어 펌들은 실전 거래소 환경과 똑같이 시간이 1초 단위로 흐르고, 시장 데이터가 하나씩 '이벤트(Event)'로 떨어지는 **이벤트 기반 아키텍처(Event-Driven Architecture)**를 씁니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Vectorized | Pandas DataFrame math | Very Fast (Seconds) | High risk of Lookahead bias | [데이터 부재] |
| Event-Driven | While True loop queue | Very Slow (Hours/Days) | Prevents future peeking | [데이터 부재] |
| Queue Size | Main Event Loop capacity | Handled by CPU sequentially| Heart of the architecture | [데이터 부재] |
| Simulated Exchange| Fake matching engine | Limit order fill logic | Needs realistic LOB tracking | [데이터 부재] |
| Latency Modeling | Network delay simulation| e.g., 5 ms delay to execute| Puts reality into backtest | [데이터 부재] |

## 3. 이벤트 기반 아키텍처의 4대 컴포넌트
이벤트 기반 백테스터는 거대한 `while True` 루프(Queue) 속에서 4개의 모듈이 핑퐁 게임을 합니다.
1. **Data Handler (데이터 피드)**: 과거의 PCAP 틱 데이터나 캔들 데이터를 하나씩 꺼내어 "애플 주가 150달러 도착"이라는 `MarketEvent`를 큐에 밀어 넣습니다.
2. **Strategy (전략 봇)**: 큐에서 `MarketEvent`를 꺼내 읽고 매매 로직을 돌립니다. 조건이 맞으면 "애플 100주 151달러 지정가 매수"라는 `SignalEvent`를 큐에 넣습니다. (절대 과거 데이터 전체 배열을 볼 수 없습니다. 오직 지금 들어온 1틱만 봅니다).
3. **Execution Handler (가상 거래소)**: `SignalEvent`를 받습니다. "어? 너 151달러 지정가 걸었는데 지금 시장가가 152달러로 도망갔네? 넌 체결 실패야." 라며 현실적인 슬리피지와 체결 거부(Reject) 로직을 모사하여 `OrderEvent`/`FillEvent`를 반환합니다.
4. **Portfolio (포트폴리오)**: 체결 확정(Fill)된 내역을 바탕으로 계좌의 잔고, 현금, 수수료, 마진콜 여부를 업데이트합니다.

## 4. 백테스트와 라이브 환경의 코드 통일
이벤트 기반 백테스터가 압도적으로 위대한 진짜 이유가 있습니다. 
- 이 구조로 짠 `Strategy` 모듈 코드는, **백테스트가 끝나면 단 한 줄의 코드 수정 없이 실전 라이브(Live) 서버에 그대로 가져다 꽂을 수 있습니다.**
- 백테스트할 때는 `Data Handler`가 하드디스크의 과거 CSV 파일을 읽어서 이벤트를 쏴주고, `Execution Handler`가 가짜 거래소 역할을 해줄 뿐입니다.
- 실전 라이브로 전환할 때는 스위치만 돌리면 됩니다. `Data Handler`가 거래소의 실시간 웹소켓(API)을 물고 이벤트를 쏴주고, `Execution Handler`가 거래소 FIX 프로토콜로 진짜 주문 패킷을 날립니다. 전략(Strategy) 봇 입장에서는 그것이 과거의 테스트인지 지금 라이브인지 구분조차 못 하며 똑같이 매매합니다.

🧠 **AI의 사고방식:**
훌륭한 과학 실험실(Backtester)은 현실계의 마찰력(Friction)과 중력(Gravity)을 완벽하게 재현해야 합니다. 벡터화 연산(Pandas)은 우주 공간 같은 진공 상태에서의 이상적인 궤도 계산일 뿐입니다. 하지만 금융 시장의 호가창은 끈적끈적한 진흙탕입니다. 이벤트 기반 아키텍처(Event-Driven)는 이 진흙탕의 지연(Latency), 수수료 징수, 체결 실패(Slippage)라는 가혹한 현실의 물리 법칙을 코드 레벨에 강제로 주입합니다. 내 백테스트 그래프가 볼품없는 연 5% 수익률로 쪼그라들었다면 기뻐해야 합니다. 당신은 달콤한 과적합의 꿈에서 깨어나, 드디어 현실 세계의 혹독한 자본주의 시뮬레이터 속으로 진입한 것이기 때문입니다.