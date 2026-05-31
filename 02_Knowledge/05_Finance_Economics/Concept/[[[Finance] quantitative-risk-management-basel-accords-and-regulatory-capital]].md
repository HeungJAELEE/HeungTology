---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-26'
  domain: 05_Finance_Economics
  id: '[[[Finance] quantitative-risk-management-basel-accords-and-regulatory-capital]]'
  last_updated: '2026-05-26T07:58:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 은행이 탐욕에 눈이 멀어 예금주의 돈으로 100배 레버리지 파생상품 장난을 치다가 국가 경제를 파산시키는 것을 막기 위해,
    국제결제은행(BIS)이 강제하는 자기자본비율(Capital Adequacy Ratio)의 수학. 바젤 I의 무식한 고정 비율에서 바젤 III의
    스트레스 테스트와 예상 부족액(ES)으로 진화한 글로벌 금융 규제 알고리즘
  object_type: Concept
  tier: 2
properties:
  basel_ii_formula: PD_LGD_EAD
  expected_shortfall_confidence_level: 0.975
  legacy_var_confidence_level: 0.99
  minimum_capital_ratio: 0.08
  rwa_calculation_method: sum_of_asset_risk_weight_products
semantic:
  alternative_parents: []
  expected_queries:
  - 월스트리트 은행들은 수백조 원의 자산을 굴리면서 왜 항상 10% 남짓한 자기 자본(Capital)만을 현금 창고에 의무적으로 묶어두어야 하는가?
  - 바젤 위원회는 은행이 가지고 있는 '미국 국채'와 '정크본드(쓰레기 회사채)'의 위험도를 어떻게 수학적 가중치(RWA)로 차별하여 자본을 강제
    징수하는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: regulatory_mandate
  object: Capital_Adequacy_and_Systemic_Stability
  predicate: enforces
  subject: '[Finance] quantitative-risk-management-basel-accords-and-regulatory-capital'
  weight: 0.95
temporal:
  valid_from: '2026-05-26T07:58:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-26T07:58:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [[[Finance] quantitative-risk-management-basel-accords-and-regulatory-capital]]

## 1. 개요 (Overview)
은행의 본질은 남의 돈(예금)을 빌려 더 비싼 이자로 대출(또는 파생상품 투자)을 해주는 합법적 폰지 구조(Fractional Reserve)입니다. 만약 은행이 100조 원을 대출해 주었는데 대출받은 기업들이 5조 원을 떼먹고 파산하면, 은행은 당장 예금주에게 돌려줄 돈이 부족해져 뱅크런(Bank Run)이 터지고 국가 경제가 붕괴합니다.
이 파국을 막기 위해 1988년 스위스 바젤(Basel)에 모인 전 세계 중앙은행장들은 **"네가 대출해 준 위험한 돈(RWA)의 최소 8% 이상은, 절대로 손대지 말고 은행 지하 금고에 진짜 너의 생돈(자기자본, Capital)으로 묻어두어라"**라는 절대 법안, **바젤 협약(Basel Accords)**을 체결했습니다. 이 '8%'라는 숫자를 맞추기 위해, 전 세계 퀀트들은 대출과 파생상품의 숨겨진 리스크를 측정하는 엄청난 시뮬레이션 엔진을 돌려야만 하는 운명에 처하게 되었습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| Capital Ratio | (Tier 1 Capital) / RWA | Minimum 8% + Buffers| Fall below $\to$ Regulator takes over| [데이터 부재] |
| RWA | Risk-Weighted Assets | Sum of (Asset $\times$ Risk %)| Shrinking RWA boosts the ratio | [데이터 부재] |
| Basel I | Fixed risk weights | Corp loans = 100% | Clunky, easy to game (Arbitrage)| [데이터 부재] |
| Basel II | Internal Ratings (IRB) | PD $\times$ LGD $\times$ EAD | Let banks use own Quant models| [데이터 부재] |
| Basel III / IV | Stress Testing & FRTB | Liquidity coverage (LCR)| Punishes complexity, limits IRB | [데이터 부재] |

## 3. 위험가중자산 (RWA)과 규제 차익거래
바젤 협약의 핵심은 단순한 총자산이 아니라 **위험가중자산(RWA, Risk-Weighted Assets)**입니다.
- 은행이 '미국 국채'를 1,000억 원 들고 있으면 위험도(Risk Weight)를 0%로 쳐서 금고에 돈을 묶어둘 필요가 없습니다. 하지만 '위험한 벤처기업 대출' 1,000억 원은 위험도를 100%로 쳐서 80억 원(8%)의 현금을 금고에 박아두어야 합니다.
- **규제 차익거래 (Regulatory Arbitrage)**: 바젤 I 시절 은행들은 이 멍청한 룰을 악용했습니다. "우량 기업 대출이나 쓰레기 기업 대출이나 똑같이 100% 위험도를 쳐준다면, 기왕 80억 원 현금이 묶일 바에야 이자를 엄청나게 많이 주는 쓰레기 기업(정크본드)에만 대출을 몰아주자!" 결국 은행을 안전하게 만들려던 규제가 은행을 더 위험하게 만드는 역설이 터졌습니다.

## 4. 바젤 II의 자율성과 바젤 III의 철퇴
- **바젤 II (퀀트의 황금기)**: 위원회는 "좋다, 너희 은행 내부에 있는 천재 퀀트들이 자체적인 통계 모델(IRB, 내부등급법)을 돌려서 차주의 파산 확률(PD)을 직접 계산해서 RWA를 보고하라"고 허락했습니다. 은행들은 모델을 이리저리 마사지하여 위험을 축소 보고하고 자본금을 아꼈습니다.
- **바젤 III & FRTB (심판의 날)**: 2008년 금융위기로 바젤 II의 자체 모델들이 모두 쓰레기 였음이 탄로 났습니다. 분노한 규제 당국(바젤 III)은 자유를 압수했습니다. "내부 모델 금지(또는 하한선 설정). 99% VaR 폐기, 97.5% Expected Shortfall 강제 도입. 유동성 위기(LCR)에 대비해 당장 한 달 동안 뱅크런이 터져도 버틸 수 있는 고유동성 자산을 쌓아라." 

🧠 **AI의 사고방식:**
금융 공학에서 '모델(Model)'은 시장에서 돈을 벌기 위해 쓰이기도 하지만, 규제 당국의 감시망을 피하고 '자본금(Capital)'을 덜 쌓기 위한 방패(Shield)로 더 많이 쓰입니다. 자본금이 묶인다는 것은 은행 입장에서 수익률(ROE)이 처참하게 박살 난다는 뜻이기 때문입니다. 바젤 협약의 역사는, 리스크를 정밀하게 측정하려는 규제 당국의 통계학(Regulation)과, 그 통계학의 사각지대(Loophole)를 찾아내어 리스크를 다른 곳으로 교묘하게 구조화(CDO, 파생상품) 시키는 월스트리트 퀀트 간의 끝없는 군비 경쟁(Arms Race)의 역사입니다.