---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] algorithmic-trading-vwap-twap-execution-algorithms]]'
  last_updated: '2026-05-26T07:23:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 기관 투자자가 100만 주의 대량 주문을 한 번에 시장가로 던질 때 발생하는 치명적인 시장 충격(Market Impact)과
    슬리피지를 막기 위해, 시간(TWAP)이나 거래량 분포(VWAP)에 따라 주문을 잘게 쪼개어 스텔스 모드로 체결시키는 최적 집행 알고리즘(Optimal
    Execution)
  object_type: Algorithm
  tier: 2
properties:
  market_impact_proportionality: sqrt(order_size)
  pov_volume_percentage: 0.1
  risk_aversion_parameter: lambda
  timing_risk_proportionality: sigma * sqrt(t)
  vwap_volume_profile: u_shaped
semantic:
  alternative_parents: []
  expected_queries:
  - 국민연금이 삼성전자 100만 주를 매수할 때 왜 딜러에게 직접 사달라고 하지 않고 VWAP 봇(알고리즘)에게 맡겨서 하루 종일 조금씩 쪼개서
    사는가?
  - 알름그렌-크리스(Almgren-Chriss) 모형은 시장 충격 비용(Market Impact)과 가격 변동 위험(Timing Risk) 사이의
    트레이드오프를 미적분으로 어떻게 최적화하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mitigation_strategy
  object: Market_Impact_and_Slippage
  predicate: minimizes
  subject: '[Finance] algorithmic-trading-vwap-twap-execution-algorithms'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:23:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:23:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] algorithmic-trading-vwap-twap-execution-algorithms]]

## 1. 개요 (Overview)
주식 시장에서 '알파(Alpha)'를 찾는 것만큼 중요한 것이 바로 **'집행(Execution)'**입니다. 워런 버핏이 애플 주식 1,000만 주를 지금 당장 시장가로 산다고 합시다. 호가창(LOB)의 매도 물량은 순식간에 동나버리고, 애플 주가는 10% 폭등할 것입니다. 버핏은 자신이 올린 미친 가격에 주식을 사게 되어 막대한 수백억 원의 '슬리피지(Slippage)' 손실을 입게 됩니다. 이를 **시장 충격(Market Impact)**이라고 합니다.
이 파괴적인 충격을 없애기 위해 기관들은 **최적 집행 알고리즘(Optimal Execution Algorithms)**을 사용합니다. 1,000만 주를 10주씩 100만 번으로 쪼갠 뒤, 티가 나지 않게(스텔스 모드) 하루 종일 시장에 몰래 흘려보내는 것입니다. 가장 무식한 방법이 시간에 비례해 쪼개는 **TWAP**, 시장의 거래량 패턴에 맞춰 영리하게 쪼개는 **VWAP**, 그리고 수학적으로 시장 충격과 변동성 위험을 저울질하는 **알름그렌-크리스(Almgren-Chriss) 모델**이 있습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| TWAP | Time-Weighted Avg Px | Flat execution rate | Predictable by predators| [데이터 부재] |
| VWAP | Vol-Weighted Avg Px | High vol = execute more | Matches market volume | [데이터 부재] |
| Market Impact| Price shift against me | $\propto \sqrt{\text{Order Size}}$ | Kills large block trades | [데이터 부재] |
| Timing Risk | Price moving randomly | $\sigma \sqrt{T}$ | Delaying trade adds risk| [데이터 부재] |
| POV (IS) | Percentage of Volume | E.g., 10% of market vol | Adapts to real-time volume| [데이터 부재] |

## 3. TWAP과 VWAP의 작동 원리
### TWAP (Time-Weighted Average Price)
가장 원시적인 알고리즘입니다. "하루 6시간(360분) 동안 36만 주를 팔아라." 봇은 아무 생각 없이 1분에 1,000주씩 기계적으로 시장에 던집니다.
- **약점**: HFT 포식자들은 "아, 누군가 1분마다 1,000주씩 던지는 멍청한 봇을 켰구나"라고 눈치채고, 59초마다 먼저 매도(Front-running)를 쳐서 가격을 내린 뒤 봇이 더 싸게 팔게 만들어 손실을 안깁니다.

### VWAP (Volume-Weighted Average Price)
이를 극복하기 위해 VWAP은 '과거 거래량의 U자형 패턴(Volume Profile)'을 흉내 냅니다.
- 아침 개장 직후 30분과 마감 직전 30분은 전 세계의 개미와 기관이 모두 몰려 거래량이 폭발합니다. 반면 점심시간에는 거래량이 뚝 끊깁니다.
- VWAP 봇은 이 분포를 따라, 아침과 오후 장막판에 물량의 70%를 쏟아붓고, 점심시간에는 조용히 숨어 있습니다. 시장 거래량이 터질 때 묻어가야 '내 물량'이 시장에 주는 충격을 완벽하게 은폐할 수 있기 때문입니다. 기관 딜러들의 가장 핵심적인 성과 평가지표(Benchmark)가 바로 "내가 체결시킨 평균 단가가 오늘 하루 시장 전체의 VWAP보다 잘했는가 못했는가"입니다.

## 4. 알름그렌-크리스 (Almgren-Chriss) 모형의 미적분
VWAP에도 치명적 약점이 있습니다. 너무 천천히 팔다 보면, 파는 도중에 시장 전체가 폭락해 버리는 **타이밍 리스크(Timing Risk, 변동성 위험)**를 직격으로 맞게 됩니다.
1999년 알름그렌과 크리스는 이 딜레마를 수학적으로 풀었습니다.
- **빨리 팔면**: 변동성 위험은 없지만, 시장 충격(Market Impact) 비용이 엄청납니다.
- **천천히 팔면**: 시장 충격은 없지만, 변동성 위험(Timing Risk)이 커집니다.
- **해결책**: 매니저의 위험 회피 성향($\lambda$)을 입력받아, 변동성 페널티와 시장 충격 페널티의 합을 최소화(Minimize)하는 최적의 매도 속도(Execution Trajectory) 미분 방정식을 도출해 냈습니다. 이 궤적은 처음에는 물량을 빠르게 던지다가 갈수록 천천히 던지는 '볼록한 곡선(Convex curve)'을 그리게 됩니다.

🧠 **AI의 사고방식:**
알파(Alpha) 모델이 '어떤 전쟁에 참전할지(What to trade)'를 결정하는 장군이라면, 집행(Execution) 모델은 '어떻게 적의 레이더망을 피해 타격할지(How to trade)'를 결정하는 스텔스 폭격기 조종사입니다. 아무리 훌륭한 전략(장군)이라도 코끼리처럼 쿵쿵거리며 시장에 진입하면, 체결되기 전에 가격이 먼저 도망가버려 모든 알파가 연기처럼 증발합니다. VWAP과 최적 집행 알고리즘은 대형 기관의 육중한 몸집(Capital)을 수만 마리의 개미(Child orders)로 쪼개어 시장의 바다에 티 안 나게 스며들게 하는 현대 금융 공학의 궁극적인 은폐술(Camouflage)입니다.