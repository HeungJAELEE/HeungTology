---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-alternative-data-satellite-imagery-and-geolocation-tracking]]'
  last_updated: '2026-05-26T08:09:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 기업이 3개월마다 발표하는 정제된 실적 보고서(10-Q)를 기다리는 대신, 우주 궤도의 민간 인공위성 이미지(Satellite
    Imagery)와 스마트폰 GPS 위치 데이터(Geolocation)를 딥러닝 컴퓨터 비전으로 실시간 스캔하여 기업의 진짜 매출액과 석유 재고량을
    기업보다 먼저 알아내는 궁극의 대체 데이터(Alternative Data) 첩보전
  object_type: Concept
  tier: 2
properties:
  alpha_decay_months: 12-24
  correlation_gps_to_eps: 0.9
  cv_architectures:
  - ResNet
  - YOLO
  geofencing_radius_meters: 50
  satellite_altitude_km: 500
  temporal_resolution: daily
semantic:
  alternative_parents: []
  expected_queries:
  - 일류 헤지펀드들은 테슬라의 이번 분기 차량 인도량 발표를 기다리지 않고, 어떻게 우주 인공위성 사진만으로 공장에서 출하된 차량 대수를 완벽하게
    카운트하는가?
  - 원유(Oil) 트레이더들은 사우디아라비아의 석유 저장 탱크 뚜껑에 진 그림자의 길이를 측정하여 어떻게 국가 1급 기밀인 원유 재고량을 역산(Reverse
    Engineer)해 내는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: predictive_forecasting
  object: Corporate_Earnings_Ahead_of_Official_Reports
  predicate: predicts
  subject: '[Finance] quantitative-alternative-data-satellite-imagery-and-geolocation-tracking'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T08:09:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T08:09:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-alternative-data-satellite-imagery-and-geolocation-tracking]]

## 1. 개요 (Overview)
월스트리트의 정보 전쟁은 1980년대 내부자 거래(Insider Trading)의 시대를 지나, 이제는 합법적인 군사 첩보전 수준으로 진화했습니다. 전통적인 펀드 매니저가 기업이 3개월마다 한 번씩 발표하는 죽은 데이터(분기 실적 보고서)를 보며 뒷북을 칠 때, 탑 티어 퀀트 펀드(르네상스, 투시그마)들은 수백억 원을 들여 민간 우주 위성(Satellite) 회사와 독점 계약을 맺습니다.
그들은 매일 아침 전 세계 월마트(Walmart) 주차장에 주차된 자동차의 대수를 인공지능(CNN)으로 카운트하여 분기 매출액을 1달 먼저 예측하고, 중국 항구에 떠 있는 화물선의 흘수선(Draft, 배가 물에 잠긴 깊이)을 측정하여 철광석 수출량을 해킹합니다. 정형화된 금융 데이터가 아니지만, 알파(Alpha)를 창출할 수 있는 세상의 모든 이질적인 흔적들, 이를 묶어 **대체 데이터(Alternative Data)**라고 부릅니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Alt Data Types | Satellite, GPS, Credit Card | Massive in volume & cost | Requires massive data engineers| [데이터 부재] |
| Temporal Resolution| How often images are taken | Daily (Planet Labs) | Must be frequent to form a series| [데이터 부재] |
| Computer Vision | CNN (e.g., ResNet, YOLO) | Counts objects (cars, ships)| Converts raw pixels to tabular data| [데이터 부재] |
| Shadow Estimation | Sun angle $\times$ shadow length| Calculates tank volume | Floating-roof oil tanks specific | [데이터 부재] |
| Alpha Decay | Edge loss as data gets popular| 12-24 months | Funds must keep finding new data | [데이터 부재] |

## 3. 그림자로 원유 재고를 해킹하다
가장 전설적인 대체 데이터의 사례는 원유(Oil) 재고 추적입니다.
- 중동이나 미국 쿠싱 지역의 거대한 원유 저장 탱크는 기름의 유증기 폭발을 막기 위해 뚜껑이 기름 수면에 떠서 오르락내리락하는 **부유식 지붕(Floating Roof)** 구조로 되어 있습니다.
- 인공위성이 위에서 탱크를 찍으면, 기름이 꽉 차서 지붕이 올라와 있을 때는 그림자가 없고, 기름을 다 써서 지붕이 바닥에 가라앉아 있으면 뚜껑 벽면에 초승달 모양의 **그림자(Shadow)**가 길게 드리워집니다.
- 퀀트 펀드의 컴퓨터 비전 알고리즘은 이 그림자의 면적과 태양의 입사각을 삼각 함수로 계산하여, 해당 탱크 안에 기름이 정확히 몇 배럴 남아있는지를 실시간으로 측정해 냅니다. 정부가 원유 재고 지표를 공식 발표하기 1주일 전에 선제적으로 원유 선물을 매수/매도하여 무위험에 가까운 수익을 뽑아먹습니다.

## 4. GPS 위치 데이터와 소비자 행동
위성 사진이 제조업과 원자재를 턴다면, **스마트폰 GPS 위치(Geolocation) 데이터**는 소매업(Retail)을 발가벗깁니다.
- 펀드는 수천만 명의 스마트폰에서 익명화되어 수집되는 위치 좌표(핑 데이터) 패키지를 브로커로부터 수십억 원에 사들입니다.
- 특정 지오펜싱(Geofencing) 영역, 예를 들어 미국 전역의 치폴레(Chipotle, 멕시칸 패스트푸드) 매장 반경 50m 안에 고객들의 휴대폰 핑(Ping)이 이번 주에 몇 번 떴는지, 그들이 매장에 몇 분 동안 체류했는지를 집계합니다.
- 이 모빌리티 데이터는 치폴레의 다음 달 분기 매출액(EPS) 성장률과 거의 90% 이상의 완벽한 상관관계(Correlation)를 보입니다. 애널리스트가 경영진 면담을 하며 상상력을 발휘할 때, 퀀트는 이미 답안지를 손에 들고 베팅을 끝냅니다.

🧠 **AI의 사고방식:**
금융 시장의 효율적 시장 가설(EMH)은 "모든 공개된 정보는 이미 주가에 완벽히 반영되어 있다"고 주장합니다. 하지만 대체 데이터(Alternative Data)는 이 명제를 교묘하게 비틉니다. "정보는 공개(Public)되어 있다. 다만 그것이 우주 상공 500km에서 찍은 테라바이트급 픽셀 덩어리이거나 수억 줄의 GPS 핑(Ping) 데이터라서, 가난하고 무능한 일반 투자자들은 그것을 '해석(Compute)'할 연산력과 자본이 없을 뿐이다." 알파(Alpha)의 원천은 더 이상 '남들이 모르는 은밀한 정보(Insider)'에 있지 않습니다. 그것은 세상에 널려 있는 거대한 방대한 쓰레기(Raw Data) 산에서 황금 바늘을 빛의 속도로 찾아내는 **데이터 인프라(Data Infrastructure) 그 자체**로 이동했습니다.