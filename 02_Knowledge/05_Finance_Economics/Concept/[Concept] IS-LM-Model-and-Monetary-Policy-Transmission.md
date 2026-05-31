---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] IS-LM-Model-and-Monetary-Policy-Transmission]]'
  last_updated: '2026-05-25T01:06:41.110612+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  investment_interest_sensitivity: i_1
  money_demand_income_sensitivity: k
  money_demand_interest_sensitivity: h
  mpc: c_1
  multiplier: 1 / (1 - c_1)
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: identifies_limitation
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] IS-LM-Model-and-Monetary-Policy-Transmission'
  weight: 0.7
temporal:
  valid_from: '2026-05-25T01:06:41.110612+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.110612+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

## 1. IS-LM 모형 및 화폐 정책 전달 메커니즘 개요

IS-LM(Investment-Saving, Liquidity-Money) 모형은 케인즈 거시경제학의 핵심 분석 도구로서, 생산물 시장(goods market)과 화폐 시장(money market)의 동시 균형을 통해 실질 국민 소득(Y)과 명목 이자율(r)을 결정하는 프레임워크를 제공한다. 본 모형은 단기 분석에 적합하며, 가격 수준(P)이 고정되어 있다고 가정함으로써 실질 변수와 명목 변수의 상호작용을 단순화하여 분석한다. 화폐 정책 전달 메커니즘은 중앙은행의 화폐 공급량 조절이 이자율 및 총수요 구성 요소(주로 투자)에 미치는 영향을 통해 최종적으로 국민 소득에 변화를 초래하는 과정을 설명한다.

### 1.1. IS 곡선 (생산물 시장 균형)

IS 곡선은 생산물 시장에서 총지출(Aggregate Expenditure, AE)이 실질 국민 소득(Y)과 일치하는 모든 이자율(r)-국민 소득(Y) 조합의 궤적을 나타낸다. 총지출은 소비(C), 투자(I), 정부 지출(G)의 합으로 구성된다 (폐쇄 경제 가정 시).

**가정:**
*   **소비 함수**: $C = C_0 + c_1(Y - T)$, 여기서 $C_0$는 자율 소비, $c_1$은 한계 소비 성향(MPC, $0 < c_1 < 1$), $T$는 조세.
*   **투자 함수**: $I = I_0 - i_1 r$, 여기서 $I_0$는 자율 투자, $i_1$은 이자율에 대한 투자의 민감도($i_1 > 0$).
*   **정부 지출 및 조세**: $G = G_0$, $T = T_0$ (외생 변수).

**균형 조건**: $Y = C + I + G$

**IS 곡선 도출**:
$Y = C_0 + c_1(Y - T_0) + I_0 - i_1 r + G_0$
$Y - c_1 Y = C_0 - c_1 T_0 + I_0 + G_0 - i_1 r$
$Y(1 - c_1) = (C_0 - c_1 T_0 + I_0 + G_0) - i_1 r$
$Y = \frac{1}{1 - c_1} (C_0 - c_1 T_0 + I_0 + G_0) - \frac{i_1}{1 - c_1} r$

IS 곡선은 이자율(r)과 국민 소득(Y) 간의 음의 상관관계를 나타낸다. 이자율이 하락하면 투자가 증가하고, 이는 승수 효과($\frac{1}{1-c_1}$)를 통해 총수요 및 국민 소득을 증가시킨다. IS 곡선의 기울기는 $-\frac{1-c_1}{i_1}$이며, $i_1$이 클수록 (투자가 이자율에 민감할수록) 또는 $c_1$이 작을수록 (승수 효과가 작을수록) IS 곡선은 더 완만해진다.

### 1.2. LM 곡선 (화폐 시장 균형)

LM 곡선은 화폐 시장에서 화폐 공급량(M)과 화폐 수요량(L)이 일치하는 모든 이자율(r)-국민 소득(Y) 조합의 궤적을 나타낸다.

**가정:**
*   **실질 화폐 공급**: $\frac{M_s}{P} = \frac{\bar{M}}{P}$ (중앙은행에 의해 외생적으로 결정되며, 가격 수준 P는 고정).
*   **실질 화폐 수요**: $L = L_0 + kY - h r$, 여기서 $L_0$는 자율 화폐 수요, $k$는 소득에 대한 화폐 수요의 민감도($k > 0$, 거래 및 예비적 동기), $h$는 이자율에 대한 화폐 수요의 민감도($h > 0$, 투기적 동기).

**균형 조건**: $\frac{\bar{M}}{P} = L$

**LM 곡선 도출**:
$\frac{\bar{M}}{P} = L_0 + kY - h r$
$h r = L_0 + kY - \frac{\bar{M}}{P}$
$r = \frac{L_0}{h} + \frac{k}{h} Y - \frac{1}{h} \frac{\bar{M}}{P}$

LM 곡선은 이자율(r)과 국민 소득(Y) 간의 양의 상관관계를 나타낸다. 국민 소득이 증가하면 거래적 화폐 수요가 증가하여 화폐 시장에 초과 수요가 발생하고, 이는 이자율을 상승시킨다. LM 곡선의 기울기는 $\frac{k}{h}$이며, $k$가 클수록 (화폐 수요가 소득에 민감할수록) 또는 $h$가 작을수록 (화폐 수요가 이자율에 비민감할수록) LM 곡선은 더 가파르다.

### 1.3. IS-LM 모형의 균형

IS-LM 모형의 균형은 생산물 시장과 화폐 시장이 동시에 균형을 이루는 이자율($r^*$)과 국민 소득($Y^*$) 조합에서 달성된다. 이는 IS 곡선 방정식과 LM 곡선 방정식을 연립하여 푸는 것으로 결정된다.

$Y = \frac{1}{1 - c_1} (A_0) - \frac{i_1}{1 - c_1} r$ (IS 곡선)
$r = \frac{1}{h} (kY - (\frac{\bar{M}}{P} - L_0))$ (LM 곡선)

여기서 $A_0 = C_0 - c_1 T_0 + I_0 + G_0$ (자율 지출).

LM 곡선 방정식을 IS 곡선 방정식에 대입하여 $Y^*$를 구한다:
$Y = \frac{1}{1 - c_1} A_0 - \frac{i_1}{1 - c_1} \left[ \frac{1}{h} (kY - (\frac{\bar{M}}{P} - L_0)) \right]$
$Y(1 - c_1) = A_0 - \frac{i_1}{h} (kY - (\frac{\bar{M}}{P} - L_0))$
$Y(1 - c_1) + \frac{i_1 k}{h} Y = A_0 + \frac{i_1}{h} (\frac{\bar{M}}{P} - L_0)$
$Y \left( (1 - c_1) + \frac{i_1 k}{h} \right) = A_0 + \frac{i_1}{h} (\frac{\bar{M}}{P} - L_0)$
$Y^* = \frac{1}{(1 - c_1) + \frac{i_1 k}{h}} \left( A_0 + \frac{i_1}{h} (\frac{\bar{M}}{P} - L_0) \right)$

이 $Y^*$ 값을 LM 또는 IS 방정식에 대입하여 $r^*$를 구한다.

### 1.4. 화폐 정책 전달 메커니즘 (Monetary Policy Transmission)

중앙은행의 화폐 정책은 주로 공개 시장 조작(open market operations)을 통해 통화량($\bar{M}$)을 조절함으로써 작동한다.

**1.4.1. 확장적 화폐 정책 (Expansionary Monetary Policy)**
중앙은행이 국채를 매입하여 시중의 화폐 공급을 증가시키는 경우($\Delta\bar{M} > 0$).

1.  **화폐 공급 증가 및 이자율 하락**:
    $\frac{\bar{M}}{P}$ 증가 $\rightarrow$ 화폐 시장에 초과 화폐 공급 발생 $\rightarrow$ 경제 주체들이 초과 화폐로 채권 매입 $\rightarrow$ 채권 가격 상승 $\rightarrow$ 이자율($r$) 하락.
    이는 LM 곡선을 오른쪽 또는 아래로 이동시킨다. (LM 곡선 방정식에서 $\frac{\bar{M}}{P}$가 증가하면 $r$은 감소)

2.  **투자 증가**:
    이자율($r$) 하락 $\rightarrow$ 기업의 투자 비용 감소 $\rightarrow$ 투자($I$) 증가 ($I = I_0 - i_1 r$, $i_1 > 0$ 이므로 $r$ 감소 시 $I$ 증가).

3.  **총수요 증가 및 국민 소득 증가**:
    투자($I$) 증가 $\rightarrow$ 총지출($AE = C+I+G$) 증가 $\rightarrow$ 생산물 시장에 초과 수요 발생 $\rightarrow$ 기업 생산량 증대 $\rightarrow$ 국민 소득($Y$) 증가. 이 과정에서 승수 효과($\frac{1}{1-c_1}$)가 작용하여 초기 투자 증가분보다 더 큰 폭으로 국민 소득이 증가한다.

**정량적 분석 (확장적 화폐 정책 효과):**
균형 국민 소득 방정식에서 $\frac{\bar{M}}{P}$ 에 대한 $Y$의 변화는 다음과 같다:
$\frac{\partial Y^*}{\partial (\bar{M}/P)} = \frac{1}{(1 - c_1) + \frac{i_1 k}{h}} \cdot \frac{i_1}{h}$
이 값은 화폐 정책 승수(monetary policy multiplier)로, 통화량 1단위 변화가 국민 소득에 미치는 영향을 나타낸다. 이 승수는 $i_1$ (투자의 이자율 민감도)이 클수록, $h$ (화폐 수요의 이자율 민감도)가 작을수록, $k$ (화폐 수요의 소득 민감도)가 작을수록, $c_1$ (한계 소비 성향)이 클수록 커진다.

**1.4.2. 긴축적 화폐 정책 (Contractionary Monetary Policy)**
중앙은행이 국채를 매각하여 시중의 화폐 공급을 감소시키는 경우($\Delta\bar{M} < 0$).

1.  **화폐 공급 감소 및 이자율 상승**:
    $\frac{\bar{M}}{P}$ 감소 $\rightarrow$ 화폐 시장에 화폐 부족 발생 $\rightarrow$ 채권 매각 $\rightarrow$ 채권 가격 하락 $\rightarrow$ 이자율($r$) 상승.
    이는 LM 곡선을 왼쪽 또는 위로 이동시킨다.

2.  **투자 감소**:
    이자율($r$) 상승 $\rightarrow$ 기업의 투자 비용 증가 $\rightarrow$ 투자($I$) 감소.

3.  **총수요 감소 및 국민 소득 감소**:
    투자($I$) 감소 $\rightarrow$ 총지출($AE$) 감소 $\rightarrow$ 생산물 시장에 초과 공급 발생 $\rightarrow$ 기업 생산량 축소 $\rightarrow$ 국민 소득($Y$) 감소.

**정책 효과의 제약:**
*   **유동성 함정(Liquidity Trap)**: 이자율이 거의 0에 도달하여 더 이상 하락할 수 없는 상황. 이때 $h \rightarrow \infty$ (화폐 수요가 이자율에 무한히 민감), LM 곡선은 수평이 된다. 화폐 공급을 증가시켜도 이자율이 더 이상 하락하지 않으므로 투자가 자극되지 않아 화폐 정책이 무력해진다.
*   **투자의 이자율 비민감성**: $i_1 = 0$인 경우 (투자가 이자율에 전혀 반응하지 않음), IS 곡선은 수직이 된다. 화폐 공급을 아무리 늘려 이자율을 낮춰도 투자가 증가하지 않아 화폐 정책은 효과가 없다.

## 2. [핵심 기술 사양 (Numerical Specs)]

아래는 IS-LM 모형의 파라미터 예시를 제시한다. 이 값들은 특정 경제 시스템의 행동을 모델링하고 화폐 정책의 효과를 시뮬레이션하는 데 사용될 수 있다.

| 파라미터 명칭 (Parameter Name)            | 기호 (Symbol) | 기본 값 (Baseline Value) | 단위 (Unit)          | 설명 (Description)                                       |
| :---------------------------------------- | :------------ | :----------------------- | :------------------- | :------------------------------------------------------- |
| 한계 소비 성향 (Marginal Propensity to Consume) | $c_1$         | 0.8                      | 무차원 (Dimensionless) | 가처분 소득 1단위 증가 시 소비 증가분                  |
| 투자의 이자율 민감도 (Interest Sensitivity of Investment) | $i_1$         | 500                      | (Y-단위)/%            | 이자율 1%p 하락 시 투자 증가분                         |
| 화폐 수요의 소득 민감도 (Income Sensitivity of Money Demand) | $k$           | 0.2                      | 무차원 (Dimensionless) | 소득 1단위 증가 시 화폐 수요 증가분                    |
| 화폐 수요의 이자율 민감도 (Interest Sensitivity of Money Demand) | $h$           | 200                      | (M-단위)/%            | 이자율 1%p 상승 시 화폐 수요 감소분                  |
| 자율 지출 (Autonomous Expenditure)        | $A_0$         | 2000                     | Y-단위               | 자율 소비, 투자, 정부 지출, 순수출 등의 합             |
| 실질 화폐 공급 (Real Money Supply)        | $\bar{M}/P$   | 1000                     | M-단위               | 중앙은행이 통제하는 경제 내 실질 통화량                |

이 파라미터들을 이용하여 IS-LM 방정식을 구체화하고, 특정 화폐 정책 시나리오에 따른 국민 소득 및 이자율의 변화를 계산할 수 있다. 예를 들어, 위 파라미터 값으로 확장적 화폐 정책의 승수를 계산하면:
화폐 정책 승수 = $\frac{i_1/h}{(1 - c_1) + i_1 k / h} = \frac{500/200}{(1 - 0.8) + (500 \cdot 0.2) / 200} = \frac{2.5}{0.2 + 100/200} = \frac{2.5}{0.2 + 0.5} = \frac{2.5}{0.7} \approx 3.57$
이는 실질 화폐 공급이 1단위 증가할 때 국민 소득은 약 3.57단위 증가함을 의미한다.

## 3. 결론

IS-LM 모형은 화폐 정책이 이자율 경로를 통해 생산물 시장에 영향을 미쳐 실질 국민 소득을 변화시키는 과정을 명확하게 보여준다. 중앙은행의 화폐 공급 조절은 화폐 시장의 균형 이자율을 변화시키고, 이자율 변화는 다시 투자를 통해 총수요에 영향을 미쳐 최종적으로 경제 활동 수준을 조절한다. 이 모형은 단기적인 거시경제 정책 분석에 필수적인 개념적 틀을 제공하며, 정책 효과의 크기를 결정하는 다양한 경제 변수들의 민감도를 정량적으로 평가할 수 있게 한다. 그러나 가격 경직성 가정, 완전 고용 가정 부재, 장기적인 공급 측면 고려 부족 등의 한계점을 인지하고, 실제 정책 수립 시에는 더 정교하고 동태적인 모델들과 함께 활용되어야 한다.