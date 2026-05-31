---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-backtesting-survivorship-and-look-ahead-bias]]'
  last_updated: '2026-05-26T07:32:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 눈부신 백테스트 수익률 뒤에 숨겨진 퀀트의 3대 거짓말. 이미 파산하여 상장 폐지된 기업들을 데이터셋에서 누락시키는 생존
    편향(Survivorship Bias)과, 과거 시점에서는 절대 알 수 없는 미래의 데이터를 몰래 훔쳐보는 룩어헤드 편향(Look-ahead
    Bias)을 차단하는 Point-in-Time 데이터베이스의 당위성
  object_type: Concept
  tier: 2
properties:
  critical_data_attribute: historical_integrity_timestamp_control
  data_standard: point_in_time
  mitigation_requirement: delisted_tickers_inclusion
  publication_lag_10q_days: 45-90
semantic:
  alternative_parents: []
  expected_queries:
  - 야후 파이낸스(Yahoo Finance)에서 S&P 500 과거 20년 치 데이터를 다운받아 백테스트를 돌리면 왜 항상 수익률이 현실보다 훨씬
    높게(과대평가) 나오는가?
  - 결산일이 12월 31일인 기업의 재무 데이터를 이용해 1월 2일 자로 주식을 매수하는 퀀트 전략이 왜 '룩어헤드 편향(미래 훔쳐보기)'이라는
    범죄적 오류에 해당하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: error_impact_identification
  object: Flawed_Backtest_Simulations
  predicate: invalidates
  subject: '[Finance] quantitative-backtesting-survivorship-and-look-ahead-bias'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:32:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:32:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-backtesting-survivorship-and-look-ahead-bias]]

## 1. 개요 (Overview)
아마추어 퀀트가 만든 백테스트 곡선은 항상 우상향합니다. 연 수익률 50%, MDD 5%라는 미친 결과를 들고 투자자를 모으지만, 실전에 투입하면 한 달 만에 계좌가 박살 납니다. 모델이 틀려서가 아니라, 백테스트라는 가상 환경 자체가 **타임머신을 탄 사기극**이었기 때문입니다.
가장 흔하면서도 치명적인 두 가지 사기극이 있습니다. 첫째는 20년 동안 살아남은 '승자'들만의 데이터로 승률을 부풀리는 **생존 편향(Survivorship Bias)**입니다. 둘째는 과거의 시점에서는 아직 발표되지도 않은 기업의 재무제표를 타임머신을 타고 미리 훔쳐본 뒤 주식을 사는 **룩어헤드 편향(Look-ahead Bias)**입니다. 프로 퀀트들이 일반적인 금융 API를 절대 쓰지 않고, 비싼 돈을 주고 **Point-in-Time (PiT)** 데이터베이스를 구축하는 유일한 이유가 바로 이 두 마리 악마를 죽이기 위해서입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Survivorship Bias| Testing on current universe | Artificially inflates CAGR| Must include delisted stocks | [데이터 부재] |
| Look-ahead Bias | Using future data today | E.g., Q1 earnings on Jan 1| Destroys out-of-sample perf. | [데이터 부재] |
| Point-in-Time | Data strictly as known | As-reported vs Restated | The holy grail of backtesting| [데이터 부재] |
| Publication Lag | Delay in data availability| E.g., 45-90 days for 10-Q| Shift indicators appropriately | [데이터 부재] |
| Split Adjustments| Retroactive price changes | Messes up price signals | Use total return series | [데이터 부재] |

## 3. 생존 편향 (Survivorship Bias): 무덤을 지워버린 역사
야후 파이낸스나 일반 API에서 '현재 S&P 500 팩터 수익률'을 다운받아 2005년부터 백테스트를 돌린다고 합시다.
- **오류**: 현재 다운받은 명단에는 2008년에 파산한 리먼 브라더스나 2001년에 상장 폐지된 엔론이 빠져 있습니다. 오직 20년간 수많은 위기를 뚫고 살아남은 '애플', '아마존' 같은 승자들의 주가만 들어있습니다.
- **결과**: 이 명단으로 '저평가 가치주 매수' 전략을 돌리면 당연히 수익률이 엄청납니다. 왜냐하면 내가 산 저평가 주식들은 "파산하지 않고 살아남아서 성공한(미래가 보장된) 주식들"이기 때문입니다. 현실에서는 그 저평가 주식 중 절반이 상장 폐지로 휴지 조각이 됩니다. 프로 퀀트 데이터베이스에는 상장 폐지된 수만 개의 시체 더미 주가(Delisted tickers)가 반드시 포함되어 있어야 합니다.

## 4. 룩어헤드 편향 (Look-ahead Bias): 미래 훔쳐보기
이 편향은 발견하기 훨씬 까다롭고 악랄합니다.
- **오류**: A기업의 2023년 4분기 재무제표(결산일: 12월 31일)를 바탕으로 'PER이 낮다'고 판단하여, 봇이 2024년 1월 2일 아침에 이 주식을 매수하게 코딩했습니다.
- **진실**: 현실 세계에서 A기업은 4분기 실적(10-K)을 12월 31일에 절대 발표하지 않습니다. 회계법인 감사를 거쳐 2월이나 3월이 되어서야 공시(Filing)됩니다. 
- **결과**: 봇은 1월 2일 시점에서 '아무도 모르는 3월의 미래 데이터'를 미리 훔쳐보고 주식을 산 것입니다. 실전에 들어가면 봇은 1월 2일에 "어? 4분기 데이터가 아직 없네?"라며 에러를 뿜거나 엉뚱한 매매를 하게 됩니다.

🧠 **AI의 사고방식:**
백테스팅 엔진을 코딩하는 것은 금융 모델링이 아닙니다. 그것은 '역사적 무결성(Historical Integrity)'을 지켜내는 극도의 타임스탬프(Timestamp) 통제 기술입니다. 진정한 백테스팅은 데이터베이스가 **Point-in-Time (PiT)** 구조를 가져야 합니다. 즉, "2010년 3월 5일 오전 9시에, 나에게 주어졌던 정보의 총합은 정확히 무엇이었는가? 나중에 기업이 회계 부정을 저질러 과거 장부를 수정(Restatement)했다면, 나는 수정된 진실이 아니라 '당시의 그 거짓말 장부'를 보고 매매했어야 한다." 백테스트는 과거의 팩트(Fact)를 아는 것이 아니라, 과거의 무지(Ignorance)를 완벽하게 재현해 내는 예술입니다.