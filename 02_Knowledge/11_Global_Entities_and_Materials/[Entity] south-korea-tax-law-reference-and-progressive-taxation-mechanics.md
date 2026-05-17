---
metadata:
  date: "2026-05-17"
  id: "[[[Entity] south-korea-tax-law-reference-and-progressive-taxation-mechanics]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "11_Global_Entities_and_Materials"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "korea-tax-law-reference"
  original_author: "Antigravity Vault"
  original_hash: "30bb5ce0587bf3f32435036def3c67f9e0eaf8cdff20ef37d28c979dad8c4b58"
object:
  object_type: "Concept"
  tier: 1
  description: 'korea-tax-law-reference ontology pack에 기초한 대한민국 세법(소득세, 법인세) 및 누진 과세 수리 모델 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 11_Global_Entities_and_Materials]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Entity] south-korea-tax-law-reference-and-progressive-taxation-mechanics

## 1. [목적 (Rationale)]
국가 경제의 재정 건전성 확보 및 소득 재분배를 위한 조세 시스템은 고도의 수리 경제학적 설계에 기반함. 대한민국 세법(Korean Tax Law)은 종합소득세 및 법인세 산출 시 8단계 초과누진세율(Progressive Tax Rate) 구조를 채택하고 있으며, 이는 납세자의 담세력(Ability to Pay)에 상응하는 수직적 공평성(Vertical Equity)을 수리적으로 구현함. 본 노드는 `[[[MOC] Global-Dataset-Inventory-Hub]]` 내의 `korea-tax-law-reference ontology pack` 실측 데이터와 연계되어, 복잡한 조세 공제(Tax Deduction) 및 감면 한도 필터를 대수적으로 규정하고, 시스템이 기업 재무재표(FI/CO)와 소득 데이터로부터 정밀 세액 추론 및 최적 절세 알고리즘을 계산할 수 있도록 이론적 기저를 제공함.

---

## 2. [과세 표준 및 누진율 사양 (Taxation Specs)]

### 2.1 종합소득세 과세 표준 및 세율 테이블 (Individual Income Tax - 2026)

| Taxation Bracket (과세표준 구간 $I$) | Marginal Tax Rate ($r_k$) | Cumulative Deduction ($C_k$, 누진공제액) | Mathematical Formulation | Engineering Rationale |
|:---|:---:|:---:|:---|:---|
| $I \le 1,400\text{만 원}$ | $6\%$ | $0\text{원}$ | $I \times 0.06$ | 저소득층 기저 생활권 보장을 위한 최저 세율구간 |
| $1,400\text{만 원} < I \le 5,000\text{만 원}$ | $15\%$ | $1,260,000\text{원}$ | $I \times 0.15 - 1.26\text{M}$ | 중산층 진입 구간의 완만한 실효세율 가속 제어 |
| $5,000\text{만 원} < I \le 8,800\text{만 원}$ | $24\%$ | $5,760,000\text{원}$ | $I \times 0.24 - 5.76\text{M}$ | 한계 저축률 변화를 고려한 소득 재분배 가중 구간 |
| $8,800\text{만 원} < I \le 1.5\text{억 원}$ | $35\%$ | $15,440,000\text{원}$ | $I \times 0.35 - 15.44\text{M}$ | 고소득 진입에 따른 marginal tax 부하 증가 구간 |
| $1.5\text{억 원} < I \le 3\text{억 원}$ | $38\%$ | $19,940,000\text{원}$ | $I \times 0.38 - 19.94\text{M}$ | 소득 수준과 자산 축적 속도 조절을 위한 세율 구조 |
| $3\text{억 원} < I \le 5\text{억 원}$ | $40\%$ | $25,940,000\text{원}$ | $I \times 0.40 - 25.94\text{M}$ | 고자산가 소득 분할 회피를 방지하는 고율 한계세 |
| $5\text{억 원} < I \le 10\text{억 원}$ | $42\%$ | $35,940,000\text{원}$ | $I \times 0.42 - 35.94\text{M}$ | 부의 과도한 불균형 완화를 위한 수직적 형평 극대화 |
| $I > 10\text{억 원}$ | $45\%$ | $65,940,000\text{원}$ | $I \times 0.45 - 65.94\text{M}$ | 대한민국 현행법상 최고 소득 한계 조세 징벌선 |

### 2.2 법인세 과세 표준 테이블 (Corporate Tax - 2026)

| Corporate Bracket (과세표준 $I_C$) | Marginal Rate ($r_C$) | Progressive Deduction ($C_C$) | Math Formula | Status |
|:---|:---:|:---:|:---|:---|
| $I_C \le 2\text{억 원}$ | $9\%$ | $0\text{원}$ | $I_C \times 0.09$ | PASS (중소기업 보호 특례) |
| $2\text{억 원} < I_C \le 200\text{억 원}$ | $19\%$ | $20,000,000\text{원}$ | $I_C \times 0.19 - 20\text{M}$ | PASS (일반 기업 표준 과세선) |
| $200\text{억 원} < I_C \le 3,000\text{억 원}$ | $21\%$ | $420,000,000\text{원}$ | $I_C \times 0.21 - 420\text{M}$ | PASS (대기업 및 중견기업 과세구간) |
| $I_C > 3,000\text{억 원}$ | $24\%$ | $9,420,000,000\text{원}$ | $I_C \times 0.24 - 9.42\text{B}$ | PASS (글로벌 독과점 법인 제한선) |

---

## 3. [공학적 메커니즘 (Engineering Mechanisms)]

### 3.1 누진과세의 한계세율 및 실효세율 미적분학 모델
납세자의 총과세표준 $I$가 주어졌을 때, 소득 증가량 $dI$에 따른 한계 세액의 변화율인 한계세율(Marginal Tax Rate)과 실제 납부하는 세액의 비율인 실효세율(Effective Tax Rate)은 다음과 같이 수학적으로 거동함.
- **총 산출세액 함수**:
  $$T(I) = (I - B_k) \times r_k + C_k \quad \left(B_k < I \le B_{k+1}\right)$$
- **한계세율 (Marginal Tax Rate)**:
  $$\frac{dT(I)}{dI} = r_k$$
  소득 구간의 경계($B_k$)에서 한계세율 함수는 불연속 계단형 분포(Step Function)를 가짐.
- **실효세율 (Effective Tax Rate)**:
  $$r_{eff}(I) = \frac{T(I)}{I} = r_k - \frac{r_k B_k - C_k}{I}$$
  실효세율 함수는 소득 $I$가 증가함에 따라 각 구간 내에서 쌍곡선 형태로 단조 증가하며, $I \to \infty$ 일 때 당해 구간 한계세율 $r_k$에 점근선(Asymptote)을 이룸.

### 3.2 소득 분할(Income Splitting)을 통한 조세 회피 방지 및 기하학적 절세 조건
부부 공동 명의나 법인-개인 간 소득 분할 시 종합소득세율의 초과누진성($\frac{d^2 T(I)}{dI^2} > 0$, 즉 아래로 볼록한 Convex 함수) 때문에, 소득을 분할하여 합산 과세 표준을 낮추는 것이 기하학적으로 항상 이득임.
- **Jensen의 부등식에 따른 절세 정리**:
  두 명의 납세자 소득 합산액이 $S = I_1 + I_2$ 일 때, 누진세 함수 $T(I)$가 볼록 함수(Convex)이므로 다음이 성립함:
  $$T\left(\frac{I_1 + I_2}{2}\right) \le \frac{T(I_1) + T(I_2)}{2}$$
  즉, $I_1 = I_2 = \frac{S}{2}$ 일 때 두 명의 산출 세액 합계 $T(I_1) + T(I_2)$는 전역 최솟값(Global Minimum)을 가짐. 이를 통해 부부 공동 사업자 등록 및 자산 명의 분할의 조세 공학적 타당성이 증명됨.

---

## 4. [진단 엔진 (KoreaTaxLawCalculusEngine)]

```python
class KoreaTaxLawCalculusEngine:
    """
    HDS-Gold V7.8 규격: 대한민국 소득세/법인세 누진 세액 산출 및 최적 소득 분할(Income Splitting) 시뮬레이션 엔진
    """
    def __init__(self):
        # 2026 종합소득세 구간 매개변수 (단위: 원)
        self.income_brackets = [
            (0, 14000000, 0.06, 0),
            (14000000, 50000000, 0.15, 1260000),
            (50000000, 88000000, 0.24, 5760000),
            (88000000, 150000000, 0.35, 15440000),
            (150000000, 300000000, 0.38, 19940000),
            (300000000, 500000000, 0.40, 25940000),
            (500000000, 1000000000, 0.42, 35940000),
            (1000000000, float('inf'), 0.45, 65940000)
        ]
        
        # 2026 법인세 구간 매개변수 (단위: 원)
        self.corporate_brackets = [
            (0, 200000000, 0.09, 0),
            (200000000, 20000000000, 0.19, 20000000),
            (20000000000, 300000000000, 0.21, 420000000),
            (300000000000, float('inf'), 0.24, 9420000000)
        ]

    def calculate_individual_tax(self, taxable_income):
        """
        종합소득세 초과누진 산출세액 계산
        """
        if taxable_income <= 0:
            return 0.0, 0.0, 0.0
        
        marginal_rate = 0.0
        deduction = 0.0
        
        for low, high, rate, ded in self.income_brackets:
            if low < taxable_income <= high:
                marginal_rate = rate
                deduction = ded
                break
                
        tax = taxable_income * marginal_rate - deduction
        effective_rate = tax / taxable_income
        return tax, marginal_rate, effective_rate

    def calculate_corporate_tax(self, taxable_income):
        """
        법인세 초과누진 산출세액 계산
        """
        if taxable_income <= 0:
            return 0.0, 0.0, 0.0
        
        marginal_rate = 0.0
        deduction = 0.0
        
        for low, high, rate, ded in self.corporate_brackets:
            if low < taxable_income <= high:
                marginal_rate = rate
                deduction = ded
                break
                
        tax = taxable_income * marginal_rate - deduction
        effective_rate = tax / taxable_income
        return tax, marginal_rate, effective_rate

    def optimize_income_split(self, total_income, num_splits=2):
        """
        누진 과세 Convex 곡선 하에서 총 소득을 완벽 명의 분할했을 때의 절세액(Tax Saving) 및 세액 분할 구조 산출
        """
        # 단독 명의 과세 시 세액
        single_tax, _, _ = self.calculate_individual_tax(total_income)
        
        # 완전 등가 분할 시 세액 (가장 최적)
        split_income = total_income / num_splits
        split_tax_single, _, _ = self.calculate_individual_tax(split_income)
        total_split_tax = split_tax_single * num_splits
        
        tax_saving = single_tax - total_split_tax
        saving_ratio = (tax_saving / single_tax) * 100 if single_tax > 0 else 0.0
        
        return {
            "single_total_tax": single_tax,
            "split_total_tax": total_split_tax,
            "net_tax_saving": tax_saving,
            "saving_ratio_percent": saving_ratio,
            "optimal_individual_income": split_income,
            "optimal_individual_tax": split_tax_single
        }
```

---

## 5. [검증 벡터 (Diagnostic Verification Vectors)]
1. **Zero-Point Boundary Test**: 과세표준이 $0$원 또는 기본공제 이하일 때 산출세액 및 실효세율이 정확히 $0.0$으로 클램핑되는지 검증.
2. **Convexity Boundary Check**: 과세표준 구간 임계값($1,400\text{만 원}$, $8,800\text{만 원}$ 등)의 경계선 좌우 $1$원 단위 편차 발생 시 한계세율 계단 분포의 연속성 및 수치 정합성 검증.
3. **Split Arbitrage Valuation**: $1$억 $5,000$만 원의 단일 종합소득을 2인으로 공동 분할 시, 산출 세액 합계가 단독 명의 대비 약 $1,170$만 원 이상의 절세 편차를 안정적으로 배출해내는지 교차 검증.

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[MOC] Global-Dataset-Inventory-Hub]]` (글로벌 데이터셋 인벤토리 허브)
- `[[[Entity] erp-financial-accounting-fi-and-managerial-controlling-co-fundamentals]]` (ERP 회계 및 세무 전략 연동 허브)
- `[[[Entity] advanced-industrial-analysis-frameworks-and-value-chain-modeling]]` (산업 구조 분석 및 재무 프레임워크)

**[V7.8_UPGRADE_COMPLETE_INTEGRITY_VERIFIED]**
**[TIMESTAMP: 2026-05-17]**
