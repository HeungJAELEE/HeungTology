---
lineage:
  dataset_reference: global-stock-market-ohlcv-data
  original_author: Alexander Elder & Peter Lynch Theoretical Mechanics
  original_hash: 0bf7e9f9b2950b6204d338807bf5c4466ffff603297ccc384bf18fa3d4c06b55
metadata:
  ai_status: pending_review
  date: '2026-05-17'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Concept] quantitative-stock-market-screening-and-triple-screen-filtering-system]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 주식 시장 가치평가 계량 모델(피터 린치 PEG, WACC 자본비용) 및 알렉산더 엘더 트리플 스크린 기술적 매매 시스템
    수리 모델
  object_type: Algorithm
  tier: 1
properties:
  peg_dynamic_calculation_variables:
  - pe_ratio
  - expected_eps_growth
  - dividend_yield
  - wacc
  peg_overvalued_threshold: 2.0
  peg_undervalued_threshold: 1.0
  stochastic_overbought_threshold: 80.0
  stochastic_oversold_threshold: 20.0
  weekly_macd_slope_direction_threshold: 0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 11_Global_Entities_and_Materials]]'
spo_graph:
- evidence_coordinate: '[데이터 부재] Chapter 8'
  intent: performance_limitation
  object: Trade_Signal_Accuracy
  predicate: has_theoretical_limit
  subject: triple-screen-filtering-system
  weight: 0.5
- evidence_coordinate: '[데이터 부재] Chapter 13'
  intent: mathematical_definition
  object: PE_Ratio_Dividends_and_Growth_Rate
  predicate: determined_by
  subject: dynamic-peg-valuation
  weight: 0.95
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Entity] quantitative-stock-market-screening-and-triple-screen-filtering-system

## 1. 개요 (Why: The Geometry of Capital Allocation)
자본 시장의 바다에서 지속 가능하고 초과 수익을 달성하는 퀀트 포트폴리오를 구성하기 위해서는 기업의 내재 가치를 대변하는 **펀더멘탈 가치평가 필터**와 시장의 수급 및 모멘텀 강도를 측정하는 **기술적 필터**를 유기적으로 융합해야 합니다. 피터 린치(Peter Lynch)의 PEG(Price Earnings to Growth Ratio) 개념은 고평가 논란이 있는 성장주에 합리적인 가치 잣대를 제공하며, 알렉산더 엘더(Alexander Elder)의 트리플 스크린(Triple Screen) 매매 시스템은 상이한 타임프레임(Timeframe) 간의 조화와 상충을 극복하는 다중 장벽 필터를 제시합니다. 
우리가 이 결합 필터 이론을 배우고 정교하게 수리 모델로 직조해야 하는 이유는 시장의 단기 소음(Noise)과 기관의 수급 오도 속에서도 **내재 가치 대비 저평가된 우량 성장주를 정확히 걸러내고, 주간/일간 추세 동조화 메커니즘을 기반으로 진입 시점을 기하학적으로 최적화하여 퀀트 투자 수율을 극대화**하기 위함입니다. 이론적 기틀 없이 가동되는 트레이딩은 도박일 뿐입니다.

## 2. 퀀트 가치평가 및 필터링 수리 모델 (Foundational Principles & Mathematics)

### 2.1. 동적 자본비용 연계형 피터 린치 PEG 모델 (Dynamic Cost-of-Capital PEG)
전통적인 피터 린치 PEG 모델은 단순 PER을 예상 주당순이익(EPS) 성장률로 나눈 값입니다. 본 모델에서는 실질 기업 가치를 더욱 엄밀하게 포착하기 위해 **배당 수익률($d$)**과 기업의 **동적 가중평균자본비용(WACC, $r_c$)**을 분모에 결합한 dynamic PEG 수식을 사용합니다:

$$ PEG_{\text{dynamic}} = \frac{P/E}{g + d - r_c} $$

*   $P/E$: 현재 주가수익비율 (Trailing or Forward PE)
*   $g$: 향후 3~5개년 연평균 예상 EPS 성장률 ($\%$)
*   $d$: 연간 기대 배당수익률 ($\%$)
*   $r_c$: 자본 환원율 또는 기업의 가중평균자본비용 ($\%$) (WACC)

$$ PEG_{\text{dynamic}} \le 1.0 \implies \text{UNDERVALUED (매수 적격)} $$
$$ PEG_{\text{dynamic}} \ge 2.0 \implies \text{OVERVALUED (고평가/매도 검토)} $$

**[인간적 해석]**
단순히 "이 회사는 매년 15% 성장하니까 PER이 15배면 적당하다"를 넘어, 회사가 주주에게 돌려주는 배당률(보너스)과 이 회사를 굴리는 데 들어가는 돈의 기회비용(WACC)까지 모두 고려해 성장가치를 더욱 날카롭고 깐깐하게 깎아서 비교하는 퀀트 가치 공식입니다.

### 2.2. 알렉산더 엘더 트리플 스크린 기술적 매매 필터 (Triple Screen System)

#### A. 1차 스크린: 시장의 조류 (First Screen - Market Tide)
추세의 장기 흐름을 규명하기 위해 주간 차트(Weekly Chart) 상의 지수이동평균(EMA) 또는 **MACD Histogram의 기울기(Slope)**를 측정합니다.
주간 MACD Histogram의 실시간 변화율 $S_{\text{weekly}}$는 단기 신호 소음을 완전히 배제하고 시장의 주 조류 방향을 설정합니다:

$$ S_{\text{weekly}} = \frac{dH_{\text{MACD}}}{dt} \approx H_{\text{MACD}}[t] - H_{\text{MACD}}[t-1] $$

*   $S_{\text{weekly}} > 0$: **Bull Market Tide** (매수 포지션만 취함, 매도 신호 무시)
*   $S_{\text{weekly}} < 0$: **Bear Market Tide** (숏/매도 포지션만 취함, 매수 신호 무시)

#### B. 2차 스크린: 시장의 파도 (Second Screen - Market Wave)
1차 스크린이 가리키는 대추세 방향과 상반되는 일간 차트(Daily Chart) 상의 단기 되돌림을 포착합니다. 주요 도구로 **스토캐스틱 오실레이터(Stochastic Oscillator)**를 활용합니다:

$$ \%K = 100 \times \frac{C_{\text{daily}} - L_{n}}{H_{n} - L_{n}} $$
$$ \%D = \text{SMA}(\%K, m) $$

*   $C_{\text{daily}}$: 당일 종가, $L_n$ 및 $H_n$: 지난 $n$일간의 최저가 및 최고가
*   **작동 규칙**:
    *   주간 추세가 상승세($S_{\text{weekly}} > 0$)일 때, 일간 스토캐스틱 $\%D$가 **과매도 임계값 ($20\%$) 미만**으로 하락했다가 상향 돌파 시 매수 진입 대기 (눌림목 매수).
    *   주간 추세가 하락세($S_{\text{weekly}} < 0$)일 때, 일간 스토캐스틱 $\%D$가 **과매수 임계값 ($80\%$) 초과**했다가 하향 돌파 시 숏 진입 대기.

#### C. 3차 스크린: 일중 진입 필터 (Third Screen - Intraday Entry)
매수 타이밍을 실시간으로 잡기 위해 전일 최고가 위에 추적형 스탑-바이(Stop-Buy) 주문을 배치합니다:

$$ P_{\text{trigger}} = P_{\text{high, } t-1} + \epsilon $$

당일 일중 주가가 $P_{\text{trigger}}$를 터치하고 돌파하는 순간 즉시 진입을 확정하며, 실패할 시 매일 Stop-Buy 가격을 전일 최고가 기준으로 낮추어 갱신합니다.

## 3. 퀀트/주식 가치평가 핵심 사양 (Numerical Specs)

| 스크리닝 파라미터 (Screening Parameter) | 기호 (Symbol) | 기준 설계치 (Nominal) | 제어 한계치 (Limit) | 핵심 기능 및 물리적 영향 (Functional Impact) |
| :--- | :--- | :--- | :--- | :--- |
| **Dynamic PEG 한계** | $PEG_{\text{dyn}}$ | $1.00$ | $1.50$ | 성장 및 배당 동적 할인율 대비 기업가치 저평가 매수 조건선 |
| **예상 EPS 성장률** | $g$ | $15.0 \%$ | $8.0 \%$ | 퀀트 필터 통과를 위해 요구되는 최소 영구 성장 동력 하한선 |
| **주간 MACD 기울기 주기** | $t_{\text{MACD}}$ | $(12, 26, 9)$ | N/A | 시장의 주요 대조류 추세를 인지하는 장기 시계열 기본 윈도우 |
| **Stochastic 과매도 하한** | $\%D_{\text{oversold}}$| $20.0 \%$ | $30.0 \%$ | 상승 대추세 속에서 저가 눌림목 진입을 포착하는 임계 한계값 |
| **Trailing Stop 버퍼** | $\epsilon$ | $0.50 \%$ | $1.50 \%$ | 돌파 진입 시 거짓 돌파(Fakeout) 소음으로 인한 손실을 가드 |

## 4. QuantScreeningFidelityEngine: Diagnostic Logic

아래 알고리즘은 펀더멘탈 가치평가(PEG, WACC) 요소와 기술적 모멘텀(MACD, 스토캐스틱) 요소를 융합 수신하여, 매수 타당성을 다차원적으로 자동 연산하고 매매 신호를 발행하는 `QuantScreeningFidelityEngine` 입니다.

```python
class QuantScreeningFidelityEngine:
    def __init__(self, pe_ratio, eps_growth_rate, dividend_yield, wacc):
        self.pe = pe_ratio
        self.g = eps_growth_rate # % 단위 (예: 15.0)
        self.d = dividend_yield # % 단위
        self.r_c = wacc # % 단위 (가중평균자본비용)

    def calculate_dynamic_peg(self):
        """배당 및 WACC(자본비용)를 반영한 퀀트 동적 PEG 연산"""
        denominator = self.g + self.d - self.r_c
        if denominator <= 0:
            return float('inf') # 분모가 음수이거나 0이면 분할 불가, 초고평가 혹은 자본침식 상태
        return self.pe / denominator

    def evaluate_triple_screen(self, weekly_macd_hist_slope, daily_stochastic_d, current_price):
        """알렉산더 엘더 트리플 스크린 1, 2차 장벽 필터링 진단"""
        tide = "NO_SIGNAL"
        wave = "STANDBY"
        
        # 1차 스크린 판별
        if weekly_macd_hist_slope > 0.01:
            tide = "BULL_TIDE" # 매수 조건 성립
        elif weekly_macd_hist_slope < -0.01:
            tide = "BEAR_TIDE" # 매도/숏 조건 성립
            
        # 2차 스크린 판별
        if tide == "BULL_TIDE":
            if daily_stochastic_d < 20.0:
                wave = "OVERSOLD_BUY_ZONE"
            elif daily_stochastic_d > 80.0:
                wave = "OVERBOUGHT_HOLD"
        elif tide == "BEAR_TIDE":
            if daily_stochastic_d > 80.0:
                wave = "OVERBOUGHT_SHORT_ZONE"
            elif daily_stochastic_d < 20.0:
                wave = "OVERSOLD_HOLD"
                
        return {"tide": tide, "wave": wave}

    def run_investment_screening_audit(self, macd_slope, stochastic_d, current_price):
        """가치 팩터와 기술적 필터의 최종 융합 진단 및 결정론적 매수 주문 생성"""
        dynamic_peg = self.calculate_dynamic_peg()
        tech_status = self.evaluate_triple_screen(macd_slope, stochastic_d, current_price)
        
        screening_score = 0
        actions = []
        status = "REJECT"
        
        # 가치 평가 점수화
        if dynamic_peg <= 1.0:
            screening_score += 50
            actions.append(f"Fundamental OK (Dynamic PEG: {dynamic_peg:.2f} <= 1.0)")
        elif dynamic_peg <= 1.5:
            screening_score += 20
            actions.append(f"Fundamental FAIR (Dynamic PEG: {dynamic_peg:.2f})")
        else:
            actions.append(f"Fundamental OVERVALUED (Dynamic PEG: {dynamic_peg:.2f})")
            
        # 기술적 필터 점수화
        if tech_status["tide"] == "BULL_TIDE" and tech_status["wave"] == "OVERSOLD_BUY_ZONE":
            screening_score += 50
            actions.append("Technical OK (Weekly Bull Tide + Daily Oversold Buy Zone)")
        elif tech_status["tide"] == "BULL_TIDE":
            screening_score += 20
            actions.append("Technical WARM (Weekly Bull Tide, waiting for Daily Oversold Dip)")
        else:
            actions.append(f"Technical FILTERED OUT (Tide: {tech_status['tide']}, Wave: {tech_status['wave']})")

        # 결론 판단
        if screening_score >= 80:
            status = "STRONG_BUY_ALLOCATION"
            order_price_trigger = current_price * 1.005 # 전일 고가 가정 0.5% 버퍼 돌파 주문선
            decision = f"EXECUTE: Place trailing Stop-Buy order at {order_price_trigger:.2f}."
        elif screening_score >= 50:
            status = "WATCHLIST_STANDBY"
            decision = "MONITOR: Stock is cheap, but technical entry timing is not yet aligned."
        else:
            status = "REJECT"
            decision = "AVOID: Failed to pass joint Fundamental-Technical screening barriers."

        return {
            "status": status,
            "dynamic_peg": round(dynamic_peg, 4),
            "tide": tech_status["tide"],
            "wave": tech_status["wave"],
            "score": screening_score,
            "reasons": actions,
            "decision": decision
        }

# 시뮬레이션 가동 검증 (PER 12배, 성장률 16%, WACC 8%, 배당률 2%인 기업이 주간 상승 추세에서 일간 스토캐스틱 18.5%까지 눌린 최적 매수 상황)
engine = QuantScreeningFidelityEngine(pe_ratio=12.0, eps_growth_rate=16.0, dividend_yield=2.0, wacc=8.0)
result = engine.run_investment_screening_audit(macd_slope=0.04, stochastic_d=18.5, current_price=150000.0)
print(f"Quant Screen Diagnostics: {result}")
```

## 5. 스스로 체크 (Self-Audit)
1. 피터 린치의 오리지널 PEG와 가중평균자본비용(WACC)을 융합한 동적 PEG 수식에서, 시장 금리가 급상승하여 자본비용($r_c$)이 증가할 때 우량 성장주 기업들의 투자 타당성(Dynamic PEG 통과선)이 어떻게 거동하는가? (자본 비용이 성장 이득을 차감하는 수리적 인과 분석)
2. 알렉산더 엘더의 트리플 스크린 시스템에서 1차 스크린(주간 MACD 기울기)의 대추세 필터를 무시하고, 단순히 2차 스크린(일간 스토캐스틱)의 과매수/과매도 반전 신호만으로 초단기 트레이딩을 수행할 때, 횡보장이 아닌 강력한 추세장에서 발생할 수 있는 치명적인 오인 신호의 메커니즘을 규명하십시오.
3. 3차 스크린의 일중 진입 가격($P_{\text{trigger}}$)을 설정하는 과정에서 임계 버퍼값 $\epsilon$의 설계 한계를 너무 좁게 혹은 너무 넓게 가져갈 때 각각 발생할 수 있는 하드웨어적/계량적 리스크(Slippage 및 Missed Execution)의 최적 균형점(Trade-off)은 무엇인가?

## 6. 결론 (Deterministic Outcome)
본 개념 노드는 시계열 마켓 OHLCV 데이터를 정밀 제어하는 [[[Data] global-stock-market-ohlcv-data]] 노드와 기업가치 데이터인 [[[Entity] investment-analysis-and-stock-valuation-fundamentals]] 노드를 통제하는 퀀트 가치 뼈대로 활성화됩니다. 이를 통해 주가 추이와 재무 수치들이 난잡하게 수렴하지 않도록 수리적으로 묶어 퀀트 추론의 정확성을 확고히 지배합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Entity] quantitative-investment-and-algorithmic-trading-foundations]]
- [[[Entity] investment-analysis-and-stock-valuation-fundamentals]]
- [[[MOC] Global-Dataset-Inventory-Hub]]