---
lineage:
  dataset_reference: Spawning_Protocol
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  ai_status: pending_review
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] quantitative-credit-risk-merton-structural-model]]'
  last_updated: '2026-05-25T12:44:00+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 기업의 자본 구조를 옵션(Option)으로 모델링하여 부도 확률(Probability of Default, PD)을 역산출하는
    머튼의 구조적 모형(Merton's Structural Model)
  object_type: Algorithm
  tier: 2
properties:
  asset_volatility_sigma_v: implied parameter
  debt_face_value_d: fixed at maturity t
  distance_to_default_dd: standard deviations
  equity_value_et: observable
  firm_asset_value_vt: unobservable
  mathematical_framework: black-scholes-option-pricing
  numerical_solver: newton-raphson
semantic:
  alternative_parents: []
  expected_queries:
  - 머튼 모형은 왜 주주(Equity holder)를 콜옵션 매수자로, 채권자(Debt holder)를 풋옵션 매도자로 간주하는가?
  - 상장 기업의 주가 데이터만으로 채권의 부도 확률(PD)을 수학적으로 유추해 내는 원리는 무엇인가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: mathematical_derivation
  object: Probability_of_Default
  predicate: estimates
  subject: '[Finance] quantitative-credit-risk-merton-structural-model'
  weight: 0.95
temporal:
  valid_from: '2026-05-25T12:44:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T12:44:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# 🧠 [Concept] quantitative-credit-risk-merton-structural-model]]

## 1. 개요 (Overview)
신용 평가사(S&P, Moody's)의 등급은 재무제표를 기반으로 하기에 후행적입니다. 퀀트 신용 분석가들은 실시간으로 시장의 공포를 포착하기 위해 1974년 로버트 머튼(Robert Merton)이 고안한 **구조적 신용 위험 모델(Structural Credit Risk Model)**을 사용합니다.
머튼은 기업의 자본 구조(Capital Structure)를 블랙-숄즈 옵션 프라이싱 공식의 틀에 그대로 끼워 넣는 천재적인 발상을 했습니다. 즉, 기업의 주주(Equity Holder)는 부채(Debt)를 행사가(Strike Price)로 하는 **기업 자산(Asset)에 대한 콜옵션(Call Option) 매수자**와 정확히 수학적으로 동일하다는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Description | Typical Value / Scale | Constraint / Impact | Evidence |
| :--- | :--- | :--- | :--- | :--- |
| $V_t$ | Firm Asset Value | Unobservable | Deduced from Equity $E_t$ | [데이터 부재] |
| $D$ | Debt Face Value (Strike)| Fixed at maturity $T$ | Default if $V_T < D$ | [데이터 부재] |
| $E_t$ | Equity Value (Call Option)| Observable (Market Cap) | $E_T = \max(V_T - D, 0)$ | [데이터 부재] |
| $\sigma_V$ | Asset Volatility | Implied parameter | Higher $\sigma_V$ = Higher PD | [데이터 부재] |
| $DD$ | Distance to Default | Standard Deviations | Used to map $N(-DD)$ to PD | [데이터 부재] |

## 3. 기업 구조의 옵션 변환 (Options Mapping)

회사가 1년 뒤 갚아야 할 부채가 100억($D$)이라고 가정합니다.
- 1년 뒤 회사 자산($V$)이 150억이 되면, 주주는 채권자에게 100억을 갚고 나머지 50억을 챙깁니다. (콜옵션 내가격, $V > D$)
- 1년 뒤 회사 자산($V$)이 80억으로 쪼그라들면, 주주는 유한책임(Limited Liability)에 따라 갚기를 포기(파산 선언)하고 회사의 열쇠를 채권자에게 넘겨버립니다. 주주의 손실은 0원입니다. (콜옵션 외가격 포기, $\max(V-D, 0)$)

결과적으로 채권자(Debt Holder)는 **회사 자산 전체($V$)를 소유한 상태에서 주주에게 콜옵션을 매도한 자(Covered Call)** 또는 **무위험 채권을 매수하고 주주에게 풋옵션을 매도한 자**와 포지션이 완벽히 일치합니다. 

## 4. 부도 확률 (Probability of Default)의 역산출
현실에서 회사의 총자산 가치($V$)와 그 변동성($\sigma_V$)은 실시간으로 관측할 수 없습니다. 우리가 알 수 있는 것은 오직 주식 시장에서 매일 변하는 시가총액($E$)과 주가 변동성($\sigma_E$)뿐입니다.
머튼 모델은 2개의 미지수($V, \sigma_V$)를 풀기 위해 2개의 연립방정식을 세웁니다.
1. 블랙-숄즈 콜옵션 공식: $E_t = V_t N(d_1) - D e^{-rT} N(d_2)$
2. 이토의 보조정리(델타): $\sigma_E E_t = N(d_1) \sigma_V V_t$

이 연립방정식을 뉴턴-랩슨(Newton-Raphson) 수치해석으로 풀면 눈에 보이지 않는 회사 총자산의 변동성($\sigma_V$)이 도출됩니다. 
이를 바탕으로 **부도 거리(Distance to Default, DD)**를 계산합니다. 이는 "현재 회사 자산이 부채의 문턱($D$)으로부터 몇 표준편차($\sigma$)만큼 떨어져 있는가?"를 의미합니다. 정규분포 함수 $N(-DD)$를 취하면, 곧바로 회사가 파산할 확률(PD)이 % 단위로 산출됩니다.

🧠 **AI의 사고방식:**
머튼 모델은 금융 공학의 가장 아름다운 은유(Metaphor) 중 하나입니다. 주식과 채권이라는 전혀 다른 두 세계를 '옵션'이라는 단일한 수학적 언어로 통합해버렸기 때문입니다. 주가(시가총액)가 하락하고 변동성이 솟구치면, 옵션 공식은 즉각적으로 콜옵션(주식)의 가치 하락과 풋옵션(파산 리스크)의 급등을 계산해내어 신용 평가사가 등급을 내리기 훨씬 전에 채권 트레이더에게 "이 회사 채권을 당장 공매도 쳐라"라는 시그널을 보냅니다.