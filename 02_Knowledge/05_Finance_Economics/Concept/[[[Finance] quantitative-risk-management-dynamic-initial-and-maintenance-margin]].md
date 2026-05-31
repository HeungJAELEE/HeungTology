---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-risk-management-dynamic-initial-and-maintenance-margin]]'
  last_updated: '2026-05-26T07:30:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 레버리지 투자의 생명줄이자 사형 선고. 개별 자산의 변동성에 비례하여 실시간으로 요동치는 개시 증거금(Initial Margin)과
    유지 증거금(Maintenance Margin)의 동역학, 그리고 꼬리 리스크 상황에서 증거금 인상이 시장 전체의 연쇄 청산(Fire Sale)을
    부르는 유동성 스파이럴 현상
  object_type: Concept
  tier: 2
properties:
  initial_margin_range: 5-15% of notional
  maintenance_margin_ratio: 80% of im
  margin_call_trigger: maintenance_margin_breach
  margin_spiral_mechanism: procyclicality
  margin_volatility_relationship: directly_proportional
  span_risk_window: 1-2 days
semantic:
  alternative_parents: []
  expected_queries:
  - 롱텀캐피탈매니지먼트(LTCM)와 아케고스(Archegos)는 왜 자신들의 수학적 모델이 틀리지 않았음에도 파산해야만 했는가?
  - 주식 시장이 폭락할 때 거래소가 파생상품의 증거금(Margin) 비율을 기계적으로 인상해 버리면, 왜 시장은 더 가파르게 폭락하는 악순환(Margin
    Spiral)에 빠지는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: causal_risk_driver
  object: Liquidity_and_Fire_Sale_Spirals
  predicate: triggers
  subject: '[Finance] quantitative-risk-management-dynamic-initial-and-maintenance-margin'
  weight: 0.9
temporal:
  valid_from: '2026-05-26T07:30:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:30:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-risk-management-dynamic-initial-and-maintenance-margin]]

## 1. 개요 (Overview)
많은 퀀트 펀드들이 수익률(Return)이나 알파(Alpha)를 예측하다가 망하지만, 진짜 최상위 포식자들(예: LTCM, 아케고스 캐피털)은 모델이 완벽히 맞았음에도 파산했습니다. 그들을 죽인 것은 시장의 방향성이 아니라 **마진콜(Margin Call)**이었습니다.
파생상품(선물, 스왑) 거래는 총대금의 10% 남짓한 현금(증거금, Margin)만 걸고 10배의 레버리지를 쓰는 게임입니다. 퀀트들은 이 '10%'라는 비율이 영원히 고정되어 있을 것이라 착각하지만, 현실에서 이 증거금 비율은 시장의 변동성(Volatility)에 따라 실시간으로 요동치는 **동적 함수(Dynamic Function)**입니다. 시장이 평화로울 때는 거래소가 증거금을 5%로 깎아주어 레버리지를 20배로 늘려주지만, 시장이 패닉에 빠지면 거래소는 자기 살길을 찾기 위해 증거금을 단 하루 만에 30%로 올려버립니다. 이때 현금을 미리 준비하지 못한 레버리지 펀드들은 강제 청산(Liquidation)당하며 죽음을 맞이합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| IM | Initial Margin | e.g., 5-15% of Notional | Cash needed to open pos. | [데이터 부재] |
| MM | Maintenance Margin | e.g., 80% of IM | Trigger level for Margin Call| [데이터 부재] |
| Margin Call | Cash demand by broker | Re-top up to IM | Failure = Fire Sale | [데이터 부재] |
| SPAN | Standard PM of Risk | Max loss over 1-2 days| Exchanges' margin engine | [데이터 부재] |
| Margin Spiral | Procyclicality | Higher Vol $\to$ Higher IM $\to$ Sells| Crashes the market | [데이터 부재] |

## 3. 동적 증거금 계산: SPAN과 변동성 연동
CME(시카고상품거래소) 등 전 세계 주요 거래소는 증거금을 고정값으로 두지 않고 **SPAN(Standard Portfolio Analysis of Risk)** 시스템이나 VaR(Value at Risk) 모델을 돌려 매일 재계산합니다.
- **계산 로직**: "내일 시장이 3 표준편차($3\sigma$)만큼 폭락하고, 변동성이 20% 폭등한다면, 이 포트폴리오가 입을 수 있는 '최대 손실액'은 얼마인가?" 
- 거래소는 이 예상 최대 손실액을 정확히 커버할 수 있는 금액만큼을 **개시 증거금(Initial Margin, IM)**으로 강제 징수합니다.
- 즉, **증거금은 자산의 변동성($\sigma$)에 정비례합니다**. 평온한 강세장에서는 증거금이 싸고, 미친 듯이 요동치는 하락장에서는 증거금이 천정부지로 솟구칩니다.

## 4. 유동성 스파이럴 (Margin & Liquidity Spiral)
2008년 금융위기나 2020년 코로나 폭락장 때 시장이 펀더멘털을 무시하고 수직 낙하(Flash Crash)하는 근본적인 이유는 이 '동적 증거금'이 낳은 기계적 악순환 때문입니다 (Brunnermeier & Pedersen의 이론).
1. **외부 충격 발생**: 예상치 못한 뉴스로 주가가 5% 하락합니다.
2. **변동성 폭등**: 주가 하락으로 인해 모델 상의 내재 변동성(VIX)이 폭등합니다.
3. **증거금 인상 (Margin Hike)**: 거래소의 리스크 엔진(SPAN)이 기계적으로 모든 계좌의 증거금(IM) 요구량을 2배로 올려버립니다.
4. **강제 청산 (Fire Sale)**: 레버리지를 꽉 채워 쓰고 있던 헤지펀드들은 추가 현금을 낼 돈(마진콜)이 없습니다. 브로커는 펀드의 주식을 시장가로 모조리 내다 팝니다(강제 청산).
5. **더 큰 폭락과 변동성**: 이 강제 청산 물량 때문에 주가는 또 10% 폭락하고, 변동성은 더 폭등합니다. (다시 3번으로 돌아가 무한 반복)

🧠 **AI의 사고방식:**
이론적 재무학에서는 '무위험 차익거래(Arbitrage)' 기회가 생기면 똑똑한 차익거래자들이 돈을 싸 들고 와서 가격을 정상으로 되돌려 놓을 것이라 믿습니다(Limits to Arbitrage의 부정). 하지만 현실에서 이 차익거래자들(헤지펀드)은 마진콜을 맞고 가장 먼저 피를 흘리며 쓰러지는 피해자들입니다. 퀀트 포트폴리오의 진짜 리스크는 내 종목이 얼마나 떨어질까를 맞추는 것이 아니라, **"내일 거래소가 갑자기 내 증거금 한도를 2배로 깎아버려도 나는 내 포지션을 강제 청산당하지 않고 끝까지 홀딩(Holding)할 수 있는가?"**라는 유동성(Liquidity)의 물리적 체력 싸움입니다.