---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-research-alternative-data-satellite-and-credit-card-parsing]]'
  last_updated: '2026-05-26T07:31:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 3개월마다 발표되는 낡은 재무제표(Fundamental)를 버리고, 월마트 주차장의 위성 사진(Satellite), 수백만
    명의 익명화된 신용카드 결제 내역(Credit Card), 그리고 이메일 영수증 파싱을 통해 상장 기업의 이번 분기 매출액을 월스트리트 애널리스트보다
    한 달 먼저 수학적으로 추론해 내는 대체 데이터(Alternative Data) 퀀트 리서치
  object_type: Concept
  tier: 2
properties:
  financial_report_lag_days: 90
  satellite_resolution_m_pixel: 0.5
  satellite_visit_cadence: daily
  web_scraping_volume_petabytes_month: petabytes
semantic:
  alternative_parents: []
  expected_queries:
  - 퀀트 펀드들은 왜 월마트의 주가를 예측하기 위해 재무제표를 읽지 않고 지구 궤도를 도는 인공위성 사진을 돈 주고 사서 컴퓨터 비전(CNN)으로
    분석하는가?
  - 대체 데이터(Alt Data)는 그 자체로는 쓰레기 더미인데, 이를 어떻게 정제하고 티커(Ticker)에 맵핑해야 의미 있는 트레이딩 알파(Alpha)가
    튀어나오는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: predictive_forecasting
  object: Earnings_Surprises_before_Release
  predicate: predicts
  subject: '[Finance] quantitative-research-alternative-data-satellite-and-credit-card-parsing'
  weight: 0.9
temporal:
  valid_from: '2026-05-26T07:31:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:31:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-research-alternative-data-satellite-and-credit-card-parsing]]

## 1. 개요 (Overview)
과거의 펀드매니저들은 상장 기업의 실적을 예측하기 위해 공장 견학을 가고 CEO와 밥을 먹었습니다. 하지만 이런 정보는 느리고 주관적입니다. 오늘날 최상위 퀀트 펀드(Point72, Two Sigma 등)는 상상할 수 있는 모든 물리적, 디지털 흔적을 긁어모아 컴퓨터 비전과 NLP 머신러닝으로 분석하는 **대체 데이터(Alternative Data)** 혁명을 이끌고 있습니다.
그들은 인공위성으로 전 세계 10만 개의 대형마트 주차장 사진을 찍어 주차된 자동차 대수를 매일 카운트(CNN 알고리즘)하고, 이를 바탕으로 월마트의 3분기 오프라인 매출액을 추론합니다. 또한, 데이터 브로커들로부터 5천만 명의 익명화된 신용카드 결제 내역이나 지메일(Gmail)로 날아오는 우버 영수증 이메일을 사들여, 우버의 이번 분기 순이익이 시장 전망치(Consensus)를 상회할지 하회할지(Earning Surprise)를 공식 실적 발표일 한 달 전에 미리 확정 짓고 주식을 매집합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Ticker Mapping | Map raw text to Stock | Complex Entity Resolution | "Apple" $\to$ AAPL vs fruit | [데이터 부재] |
| Credit Card | Anonymized transactions | Billions of rows/day | Bias in card demographics | [데이터 부재] |
| Satellite Imagery| Resolution & Cadence | 0.5m/pixel, Daily visits | Cloud cover obscures data | [데이터 부재] |
| Web Scraping | E-commerce pricing | Petabytes / month | Sites block scraping IPs | [데이터 부재] |
| Point-in-Time | No look-ahead bias | Time-stamped strictly | Must prove when data arrived| [데이터 부재] |

## 3. 대체 데이터의 정제: 쓰레기에서 황금으로
대체 데이터는 엄청난 잠재력이 있지만, 사 오자마자 바로 쓸 수 있는 '숫자'가 아닙니다. 더럽고(Dirty), 비정형적(Unstructured)이며, 편향(Bias)되어 있습니다.
1. **엔티티 매핑(Entity Mapping)**: 신용카드 영수증에 `SBUX STORE #124`라고 찍혀 있다면 퀀트 시스템은 이를 스타벅스 티커(SBUX) 매출로 자동 연결해야 합니다. 만약 `APPLE STORE`가 농산물 직판장(과일 애플)인지 아이폰 매장(AAPL)인지 구분하지 못하면 쓰레기 알파가 나옵니다.
2. **샘플링 편향 제거**: 우리가 사들인 신용카드 데이터가 20대 대학생들 위주로 구성되어 있다면? 이 데이터만 믿고 롤렉스 시계(Richemont)의 매출이 급감했다고 판단해 공매도를 치면 큰일 납니다. 인구통계학적 가중치 조정을 통해 국가 전체 데이터로 정규화(Normalization)해야 합니다.

## 4. 정보의 비대칭성과 알파의 붕괴 (Alpha Decay)
대체 데이터 트레이딩의 본질은 **"남들은 모르는 것을 나만 안다"**는 합법적인 인사이더 트레이딩(Insider Trading)입니다. 
- 기업의 매출은 매일매일 발생하지만, 재무제표(10-Q)는 90일에 한 번씩 지연(Lagging)되어 발표됩니다. 
- 퀀트들은 신용카드 데이터라는 X-Ray를 통해 이 90일의 어둠 속을 꿰뚫어 보고, 실적 발표일 날 주가가 폭등할 것을 미리 알고 포지션을 선점합니다.
- **알파의 붕괴 (Decay)**: 하지만 치명적인 단점이 있습니다. 신용카드 벤더가 이 데이터를 나에게만 팔 때는 연간 50%의 수익이 났지만, 이 데이터가 유명해져서 월스트리트 50개 펀드에 똑같이 팔리기 시작하면 이 데이터가 주는 '초과 수익(Alpha)'은 0으로 완벽하게 수렴해 버립니다. 퀀트들이 매일같이 새로운 쓰레기 더미(Web Scraping, IoT 센서, 위치 정보 등)를 뒤지며 세상에 없는 기상천외한 새 데이터를 찾아 헤매는 이유가 바로 이 지독한 알파의 반감기 때문입니다.

🧠 **AI의 사고방식:**
전통적인 재무제표 퀀트(Fama-French)가 '백미러'를 보며 운전하는 것이라면, 대체 데이터 퀀트는 어둠 속에서 '적외선 야시경'을 끼고 달리는 것입니다. 대체 데이터의 철학은 명쾌합니다. "인간이 경제 활동을 하면 무조건 데이터 배기가스(Data Exhaust)가 남는다." 이 배기가스를 대기 중에 흩어지기 전에 포집하여, 딥러닝이라는 정유 공장에 넣고 정제해 내면, 그것이 곧 주가를 움직이는 가장 순수한 연료(Alpha)가 됩니다.