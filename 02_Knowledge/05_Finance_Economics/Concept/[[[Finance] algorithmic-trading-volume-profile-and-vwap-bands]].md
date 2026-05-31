---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-volume-profile-and-vwap-bands]]'
  last_updated: '2026-05-25T14:58:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 가격 중심의 차트를 벗어나, 특정 가격대에서 터진 누적 체결량(Volume Profile)을 통해 진짜 지지/저항 매물대의
    두께를 추출하고, 기관의 평단가인 VWAP을 중심으로 정규분포 밴드를 씌워 HFT 알고리즘의 최적 타점을 잡는 동적 지표
  object_type: Algorithm
  tier: 2
properties:
  hvn_characteristic: sticky
  lvn_characteristic: slippery
  point_of_control: price_with_max_volume
  value_area_standard_deviation: 1
  value_area_volume_percentage: 0.68
  vwap_band_sigma_levels:
  - 1
  - 2
semantic:
  alternative_parents: []
  expected_queries:
  - 시간순으로 나열된 캔들 차트(Candlestick)가 숨기고 있는 '특정 가격대에서의 실제 거래 밀도'를 볼륨 프로파일(Volume Profile)은
    어떻게 보여주는가?
  - VWAP 밴드의 표준편차(Standard Deviation) 라인을 돌파했을 때, 평균 회귀(Mean Reversion)와 추세 추종(Momentum)
    전략은 어떻게 나뉘는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: market_structure_mapping
  object: Institutional_Liquidity_Zones
  predicate: maps
  subject: '[Finance] algorithmic-trading-volume-profile-and-vwap-bands'
  weight: 0.9
temporal:
  valid_from: '2026-05-25T14:58:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T14:58:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-volume-profile-and-vwap-bands]]

## 1. 개요 (Overview)
대부분의 차트(Candlestick)는 X축을 시간(Time), Y축을 가격(Price)으로 그립니다. 하지만 기관 투자자의 알고리즘은 시간에 신경 쓰지 않습니다. 그들이 알고 싶은 것은 **"어느 가격대(Price Level)에서 사람들이 가장 피 터지게 싸우며 거래량(Volume)을 터뜨렸는가?"**입니다.
이 질문에 답하기 위해 차트를 90도 회전시켜, Y축을 가격으로, X축을 해당 가격에서의 '누적 체결량'으로 그린 것이 **볼륨 프로파일(Volume Profile)**입니다. 여기에 기관 트레이더들의 그날그날의 평균 단가인 **VWAP (거래량 가중 평균 가격)**을 더하고, 그 위아래로 통계적 표준편차 밴드(VWAP Bands)를 씌우면, 알고리즘 봇이 어디서 매수하고 어디서 공매도를 쳐야 할지가 통계적 확률망으로 도출됩니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Point of Control (POC)| Price with max volume | The ultimate magnet | Acts as heavy gravity | [데이터 부재] |
| Value Area (VA) | Contains 68% of volume| $\approx 1$ Standard Deviation| Fair value consensus | [데이터 부재] |
| High/Low Volume Node| HVN / LVN | Peaks and valleys | HVN=Sticky, LVN=Slippery| [데이터 부재] |
| VWAP | Volume Weighted Avg | Reset daily/weekly | Benchmark for institutions| [데이터 부재] |
| VWAP Bands | $\text{VWAP} \pm n\sigma$ | $+1\sigma, +2\sigma$ | Statistical boundaries | [데이터 부재] |

## 3. 볼륨 프로파일: HVN과 LVN의 유체역학
볼륨 프로파일을 보면 매물대가 두꺼운 곳과 텅 빈 곳이 확연히 드러납니다.
- **고거래량 노드 (HVN, High Volume Node)**: 과거에 엄청난 손바뀜이 일어난 가격대입니다. 이곳은 '끈적끈적한(Sticky)' 늪과 같습니다. 가격이 이 구간에 진입하면 수많은 사람들의 본전 심리와 대기 매물이 얽혀 있어 가격이 쉽게 벗어나지 못하고 횡보합니다. (강력한 지지/저항선).
- **저거래량 노드 (LVN, Low Volume Node)**: 사람들이 관심이 없어 거래가 텅 비어 있는 구간입니다. 이곳은 '빙판길(Slippery)'입니다. 가격이 이 구간에 진입하면 아무런 저항이 없기 때문에, 순식간에 다음 HVN을 향해 미끄러지듯 급등하거나 급락합니다. 돌파(Breakout) 알고리즘은 바로 이 LVN 구간이 열리는 순간 시장가로 풀악셀을 밟습니다.

## 4. VWAP 밴드를 활용한 HFT 퀀트 전략
VWAP은 '오늘 하루 동안 시장 참여자들이 주식을 산 진짜 평균 단가'입니다. 퀀트 알고리즘은 현재 주가가 이 VWAP에서 얼마나 떨어져 있는지를 **표준편차($\sigma$)** 밴드로 측정합니다.

1. **평균 회귀 (Mean Reversion)**: 주가가 갑자기 튀어 올라 VWAP $+2\sigma$ 밴드 밖으로 벗어났습니다. 알고리즘은 "이것은 너무 비정상적으로 비싸다(Overbought). 곧 기관들의 평균 단가(VWAP)로 다시 끌어내려질 것이다"라고 판단하고 **공매도(Short)**를 칩니다.
2. **국면 전환 (Trend Following)**: 주가가 하루 종일 VWAP $+1\sigma$ 위에서만 논다면, 알고리즘은 "오늘 시장은 압도적인 상승 트렌드"라고 판단합니다. 주가가 내려오다가 VWAP이나 $+1\sigma$ 밴드에 터치하는 순간(Pullback), 강력한 매수세가 받쳐줄 것을 믿고 **매수(Long)**를 때립니다.

🧠 **AI의 사고방식:**
일반적인 이동평균선(MA)이나 볼린저 밴드(Bollinger Bands)가 '시간'에 가중치를 두는 그림자라면, 볼륨 프로파일과 VWAP 밴드는 '돈의 무게(Volume)'가 빚어낸 실제 지형도입니다. 퀀트 알고리즘은 빈 공간(허공)에서 섀도 복싱을 하지 않습니다. 그들은 볼륨 프로파일의 가장 두꺼운 배꼽(POC)이 어디에 있는지, 현재 주가가 기관들의 진짜 평단가(VWAP)로부터 수학적으로 얼마나 무리해서 팽창(Standard Deviation)해 있는지를 엑스레이로 찍어본 뒤, 팽창된 고무줄이 튕겨져 돌아오는 찰나의 에너지를 수학적으로 수확합니다.