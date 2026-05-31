---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-fixed-income-credit-default-swaps-cds-and-hazard-rates]]'
  last_updated: '2026-05-26T08:02:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 특정 기업이나 국가가 부도(Default) 날 확률을 시장의 채권 가격으로부터 역산(Bootstrapping)해 내고,
    부도 위험만을 순수하게 사고파는 보험 계약인 신용부도스왑(CDS). 생존 분석(Survival Analysis)에서 빌려온 해저드 레이트(Hazard
    Rate, 푸아송 강도)를 통해 기업의 시한부 수명을 수학적으로 계량화하는 신용 퀀트의 핵심
  object_type: Concept
  tier: 2
properties:
  calibration_method: bootstrapping
  cds_spread_typical_scale: 200 bps
  credit_triangle_formula: spread approx hazard_rate * lgd
  hazard_rate_modeling_method: poisson_process
  lgd_standard_calculation: 100% - recovery_rate
  modeling_approach: reduced-form model
  survival_probability_formula: S(t) = exp(-integral_0^t lambda ds)
semantic:
  alternative_parents: []
  expected_queries:
  - 영화 <빅쇼트>에서 마이클 버리는 모기지 채권이 휴지 조각이 될 것에 베팅하기 위해 왜 공매도(Short Selling)를 하지 않고 은행에
    가서 수백억 원의 수수료(Premium)를 주며 CDS(신용부도스왑)를 샀는가?
  - 신용 퀀트들은 어떻게 삼성전자 회사채의 가격 쪼가리 하나만 보고도 삼성전자가 향후 5년 내에 파산할 확률(Default Probability)을
    소수점까지 뽑아내는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: risk_segmentation
  object: Pure_Credit_Risk_and_Default_Probabilities
  predicate: isolates
  subject: '[Finance] quantitative-fixed-income-credit-default-swaps-cds-and-hazard-rates'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T08:02:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T08:02:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-fixed-income-credit-default-swaps-cds-and-hazard-rates]]

## 1. 개요 (Overview)
회사채에 투자할 때 가장 두려운 것은 '금리가 오르는 것(이자율 리스크)'과 '회사가 망하는 것(신용 리스크)'입니다. 이 두 위험은 회사채 안에 끈적하게 섞여 있습니다. 1990년대 JP모건 퀀트들의 가장 위대한 발명은, 이 회사채에서 오직 **'회사가 망할 위험(Default Risk)'만을 핀셋으로 뽑아내어 사고팔 수 있는 독자적인 보험 상품, 신용부도스왑(CDS, Credit Default Swap)**을 만든 것입니다.
내가 A기업의 5년짜리 CDS를 샀다는 것은, 자동차 보험을 든 것과 같습니다. 나는 매년 일정한 보험료(CDS Spread)를 딜러에게 바칩니다. 그러다 만약 A기업이 5년 안에 부도가 나서 파산(Credit Event)해 버리면, 딜러는 나에게 채권 액면가 전액(예: 100억 원)을 즉시 보상해 줍니다. 2008년 금융위기 때 <빅쇼트>의 주인공들이 수조 원의 잭팟을 터뜨린 것이 바로 미국 주택 시장에 불이 난다에 베팅하는 CDS 화재보험을 미친 듯이 사 모았기 때문입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| CDS Spread | Premium paid by buyer | e.g., 200 bps (2%) / yr | The "price" of default risk| [데이터 부재] |
| Hazard Rate ($\lambda$) | Instantaneous default prob| Modeled as Poisson process| Constant or time-varying | [데이터 부재] |
| Survival Prob $S(t)$| Chance of not defaulting | $S(t) = \exp(-\int_0^t \lambda ds)$ | Exponential decay of life | [데이터 부재] |
| LGD | Loss Given Default | e.g., $100\% - 40\%(Rec) = 60\%$ | Dictates payout upon default| [데이터 부재] |
| Credit Triangle | $Spread \approx \lambda \times LGD$ | The fundamental shortcut | Links Spread, PD, and Loss | [데이터 부재] |

## 3. 푸아송 프로세스와 해저드 레이트 (Hazard Rate)
채권 시장에서 A기업의 CDS 스프레드가 연 200bp(2%)에 거래되고 있다고 합시다. 퀀트들은 이 가격표 하나로 이 기업이 언제 죽을지 수명을 수학적으로 해체합니다.
- **해저드 레이트 ($\lambda$, Hazard Rate)**: 생물학이나 공학(기계 결함)에서 쓰는 '생존 분석' 통계를 가져옵니다. "어제까지 멀쩡히 살아있던 이 기업이, 바로 오늘 벼락처럼 파산(Jump to Default)해버릴 순간적인 강도(Intensity)"를 뜻합니다. 이는 연속 시간 푸아송 프로세스(Poisson Process)로 모델링됩니다.
- **신용의 마법 삼각형 (Credit Triangle)**: 수학적 계산을 단순화하면 아주 아름답고 소름 돋는 절대 공식이 하나 튀어나옵니다. 
  $$ CDS Spread \approx Hazard Rate(\lambda) \times Loss Given Default(LGD) $$
  만약 파산 시 못 건지는 돈(LGD)이 60%라고 가정하면, $2\% = \lambda \times 0.6$ 이므로, 이 기업의 파산 강도($\lambda$)는 약 3.3%가 됩니다. 퀀트들은 시장 가격(Spread)만 보고도 기업의 파산 확률을 역추적해 내는 독심술을 부립니다.

## 4. 부트스트래핑(Bootstrapping)과 신용 곡선
기업의 생존 확률은 1년 차, 3년 차, 5년 차마다 다릅니다(Term Structure). 
- 퀀트들은 시장에 굴러다니는 1년 만기 CDS 가격, 2년 만기 CDS 가격을 차례차례 퍼즐 맞추듯 엮어냅니다.
- 1년짜리 가격으로 1년 차 파산 확률을 픽스(Fix)하고, 그것을 바탕으로 2년 차 가격에서 2년 차 파산 확률을 뽑아내는 꼬리물기 연산, **부트스트래핑(Bootstrapping)**을 실행합니다.
- 그 결과, "이 기업이 1년 안에 파산할 확률 3%, 3년 안에 파산할 확률 누적 10%, 5년 안에 파산할 누적 확률 25%"라는 완벽한 생존 곡선(Survival Curve)이 모니터 위에 그려집니다.

🧠 **AI의 사고방식:**
일반 투자자들은 기업의 부도를 재무제표(회계)를 분석하여 '예측'하려 듭니다(Merton 구조적 모형). 하지만 CDS 트레이더들이 쓰는 축약 모형(Reduced-form Model)은 부도의 원인(자산이 부채보다 적어짐) 따위에는 전혀 관심이 없습니다. 그들에게 부도란 맑은 하늘에 떨어지는 벼락(푸아송 점프)과 같으며, 오직 "오늘 시장 참가자들이 그 벼락에 대비해 보험료(Spread)를 얼마 지불하고 있는가?"라는 시장 가격(Market Price)만을 100% 신뢰하여 미래의 죽음을 역산해 냅니다. 신용 퀀트의 철학은 명확합니다. "재무제표는 거짓말을 하지만, 파산을 두려워하는 피 묻은 파생상품의 가격표는 절대로 거짓말을 하지 않는다."