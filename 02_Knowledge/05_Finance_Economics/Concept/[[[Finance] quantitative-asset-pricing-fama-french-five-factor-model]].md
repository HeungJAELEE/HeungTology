---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-asset-pricing-fama-french-five-factor-model]]'
  last_updated: '2026-05-26T07:21:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 과거 자산가격결정의 황제였던 파마-프렌치 3팩터(시장, 규모, 가치) 모형의 한계를 인정하고, 배당할인모형(DDM)의 근본
    원리에서 도출한 수익성(Profitability, RMW)과 투자(Investment, CMA) 팩터를 추가하여 가치주 프리미엄을 완전히 흡수해
    버린 5팩터 자산가격결정 모형의 최종 진화
  object_type: Algorithm
  tier: 2
properties:
  cma: investment_premium
  hml: value_premium
  mkt: market_excess_return
  rmw: profitability_premium
  smb: size_premium
semantic:
  alternative_parents: []
  expected_queries:
  - 파마와 프렌치는 왜 20여 년간 자신들이 주장했던 3팩터 모형(가치주 HML 팩터 중심)의 한계를 인정하고 5팩터 모형을 새롭게 발표해야만
    했는가?
  - 재무제표의 '수익성(RMW)'과 '설비투자(CMA)'라는 기업 금융(Corporate Finance)의 논리가 어떻게 주식의 기대 수익률(Asset
    Pricing)을 결정하는 팩터로 수학적으로 전환되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: theoretical_expansion
  object: Asset_Pricing_Factor_Space
  predicate: expands
  subject: '[Finance] quantitative-asset-pricing-fama-french-five-factor-model'
  weight: 0.9
temporal:
  valid_from: '2026-05-26T07:21:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:21:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-asset-pricing-fama-french-five-factor-model]]

## 1. 개요 (Overview)
1992년 파마(Fama)와 프렌치(French)는 "소형주(SMB)와 가치주(HML)가 시장(MKT)보다 돈을 더 잘 번다"는 3팩터 모형으로 노벨상과 학계를 평정했습니다. 하지만 시간이 흐르자 균열이 생겼습니다. 워런 버핏 같은 투자자들은 단순히 PBR이 낮은 가치주가 아니라, **"수익성(돈을 잘 버는가)이 높고, 쓸데없는 설비투자(자본 낭비)를 안 하는 우량주"**를 사서 엄청난 초과 수익을 내고 있었습니다.
2015년, 파마와 프렌치는 23년 만에 자신들의 3팩터 모형을 부수고, 수익성(Profitability)과 투자(Investment) 팩터를 추가한 **파마-프렌치 5팩터 모형(Five-Factor Model)**을 발표합니다. 놀랍게도 이 5팩터로 분석을 돌려보자, 과거 3팩터의 핵심이었던 '가치주 프리미엄(HML)'이 통계적으로 흔적도 없이 사라져 버렸습니다. 즉, 우리가 "가치주가 돈을 잘 번다"라고 착각했던 이유는, 그 가치주들 속에 사실은 '돈 잘 벌고 투자 적게 하는 우량 기업'들이 섞여 있었기 때문이라는 충격적인 진실이 밝혀집니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| MKT | Market Excess Return | $R_m - R_f$ | The original CAPM base | [데이터 부재] |
| SMB | Small Minus Big | Size premium | Still significant but weak | [데이터 부재] |
| HML | High Minus Low | Value premium | **Becomes redundant in 5F**| [데이터 부재] |
| RMW | Robust Minus Weak | Profitability (e.g., ROE) | High profits beat low profits| [데이터 부재] |
| CMA | Cons. Minus Agg. | Investment (Asset growth)| Low inv. beats high inv. | [데이터 부재] |

## 3. 배당할인모형(DDM)에서 팩터를 추출하다
파마와 프렌치는 왜 하필 수많은 지표 중 '수익성'과 '투자'를 골랐을까요? 그들은 가장 근본적인 주식 가치 평가 공식인 배당할인모형(Dividend Discount Model)의 방정식을 재배열했습니다.
$$ M_t = \sum_{\tau=1}^{\infty} \frac{E(Y_{t+\tau} - d B_{t+\tau})}{(1+r)^\tau} $$
- $M_t$: 현재 주가 (Market Value)
- $Y$: 미래의 이익 (Earnings)
- $dB$: 주주의 몫이 늘어나는 변화량 (장부 가치의 증가 = 투자, Investment)
- $r$: 내가 이 주식에 기대하는 요구 수익률 (Expected Return)

이 식을 $r$(기대 수익률)에 대해 정리하면 수학적 진실이 드러납니다.
1. **수익성(RMW, Robust Minus Weak)**: 현재 주가($M_t$)가 고정되어 있을 때, 미래의 이익($Y$, 수익성)이 높은 기업일수록 할인율($r$, 주주의 기대 수익률)이 높아야만 수학 공식이 성립합니다. 즉, 돈을 잘 버는 기업은 주식 시장에서 높은 프리미엄을 줍니다.
2. **투자(CMA, Conservative Minus Aggressive)**: 주가($M_t$)와 이익($Y$)이 고정되어 있을 때, 이익을 깎아 먹는 자산 투자($dB$)를 많이 하는 기업(Aggressive)일수록, 할인율($r$)이 낮아야만 공식이 성립합니다. 즉, 툭하면 유상증자나 쓸데없는 공장 건설로 장부 자산을 늘리는 기업은 주식 시장에서 저조한 수익률로 처벌받습니다.

## 4. 가치주(HML)의 죽음과 팩터의 흡수
5팩터 모형이 논문에 발표되자 퀀트계는 발칵 뒤집혔습니다.
회귀 분석을 돌려보니, 과거 3팩터 모형에서 막강한 힘을 발휘했던 HML(가치주 팩터)의 t-검정 통계량이 0에 수렴해 버린 것입니다.
- 해석: **가치주(PBR이 낮은 주식)가 수익률이 높았던 진짜 이유는, 걔네들이 PBR이 낮아서가 아니라, 그 낮은 PBR 속에 사실은 '수익성(RMW)이 좋고 무리한 투자(CMA)를 안 하는 성향'이 짙게 배어 있었기 때문입니다.**
- RMW와 CMA라는 현미경을 들이대자, 껍데기(HML)는 쓸모없어지고(Redundant) 진짜 알맹이(우량 기업의 속성)만이 팩터 프리미엄의 진정한 지배자로 남게 되었습니다.

🧠 **AI의 사고방식:**
3팩터 모형이 주식의 '가격표(시가총액, PBR)'만 보고 등급을 매기는 얄팍한 통계학이었다면, 5팩터 모형은 기업의 본질인 '재무제표(현금흐름과 자본적 지출)'를 해부하여 자산의 뼈대와 내장을 가격표와 수학적으로 엮어낸 생리학(Physiology)입니다. 파마와 프렌치는 자신들이 평생을 바쳐 쌓아 올린 가치주(HML)라는 우상(Idol)을 자기 손으로 부수고, 주가라는 것은 결국 기업이 창출하는 잉여 현금흐름(Profitability - Investment)의 할인일 뿐이라는 재무관리의 가장 고전적이고 영원한 진리로 찬란하게 귀환했습니다.