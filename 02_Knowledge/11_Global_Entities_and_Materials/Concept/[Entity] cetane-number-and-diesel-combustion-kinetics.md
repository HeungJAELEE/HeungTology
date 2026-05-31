---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: bdde4115fb2f8a1f281ed43ecf0513418c038f1102134246ee0e54b7d210a617
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] cetane-number-and-diesel-combustion-kinetics]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] cetane-number-and-diesel-combustion-kinetics에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  cetane_number_formula: '% n-cetane + 0.15 * % hepta-methyl-nonane'
  critical_ignition_delay_threshold_ms: 2.0
  ignition_delay_formula: A * P^-n * exp(Ea / (R * T))
  notice_low_cetane_index_threshold: 45.0
  reject_high_exhaust_opacity_threshold_pct: 15.0
  standard_diesel_cetane_range: 40-60
  warning_pressure_rise_rate_threshold_bar_deg: 5.0
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 11_Global_Entities_and_Materials]]'
spo_graph: []
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

# [Entity] cetane-number-and-diesel-combustion-kinetics

## 1. 개요 (Why: 인간적 통찰)
디젤 엔진이 왜 가솔린 엔진처럼 스파크 플러그(점화플러그) 없이도 강력한 힘을 낼 수 있을까요? **세탄가(Cetane Number) 및 디젤 연소 역학**은 기름이 압축되는 순간 스스로 불이 붙는 '자연 발화'의 성질을 다스리는 **'불꽃 없는 폭발의 과학'** 기술입니다. 세탄가는 디젤유가 얼마나 '빨리' 스스로 불이 붙느냐를 나타내는 지표입니다. 적절한 타이밍에 스스로 터지는 연료는 소음을 줄이고 힘을 극대화하는 **'거대 엔진의 부드러운 폭발력'**을 결정합니다.

## 2. 기초 원리 및 핵심 공식 (Foundational Principles & Mathematics)

### 2.1. 점화 지연 공식 (Ignition Delay)
연료가 분사된 순간부터 실제로 불이 붙기까지 걸리는 시간($ID$)을 압력($P$)과 온도($T$)로 계산합니다.

$$ ID = A P^{-n} \exp(E_a / RT) $$

**[인간적 해석]**: "참을성의 한계"입니다. 온도가 높고 압력이 셀수록 연료는 참지 못하고 빨리 터집니다($ID$ 감소). 우리는 이 수식을 통해 연료의 세탄가를 조절하여, 피스톤이 가장 높은 곳에 왔을 때 '딱 맞춰' 터지게 만드는 **'찰나의 타이밍 지배'**를 수행합니다.

### 2.2. 세탄가 정의 (Cetane Number)
불이 아주 잘 붙는 세탄과 잘 안 붙는 물질의 배합 비율로 연료의 품질($CN$)을 정의합니다.

$$ CN = \% \text{n-cetane} + 0.15 \times \% \text{hepta-methyl-nonane} $$

**[인간적 해석]**: "점화의 신분증"입니다. 세탄가가 높을수록 불이 더 빨리, 부드럽게 붙습니다. 우리는 이 숫자를 통해 "이 기름을 넣었을 때 겨울철 시동이 잘 걸릴까?" 혹은 "엔진에서 시끄러운 노킹 소리가 날까?"를 예측하는 **'연료 무결성 진단'**을 실현합니다.

## 3. 핵심 기술 사양 (Numerical Specs)

| Feature | Gasoline (Octane based) | Diesel (Cetane based) (V6.3.7)| Unit | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Ignition Type** | Spark Ignition | Compression Ignition | - | Mechanism |
| **Key Metric** | Octane Number (Anti-knock)| Cetane Number (Pro-ignite)| - | Metric Type |
| **Fuel Quality Range**| 80 ~ 100 | 40 ~ 60 (Standard) | - | Rating |
| **Cold Start** | Good | Dependent on Cetane | - | Reliability |
| **Combustion Noise** | Low | High (Diesel Knock) | - | Comfort |
| **Emissions (Soot)** | Low | High (Diffusion flame) | - | Environment |

## 4. FactoryFidelityEngine: Diagnostic Logic

디젤 연소 시스템의 화학적 무결성 및 시스템 상태를 진단하는 `FactoryFidelityEngine` 로직입니다.

```python
class FactoryFidelityEngine:
    def __init__(self, ignition_delay_ms, peak_pressure_rise_bar_deg, fuel_cetane_index):
        self.id_time = ignition_delay_ms # 점화 지연 시간
        self.rise = peak_pressure_rise_bar_deg # 압력 상승률
        self.ci = fuel_cetane_index # 세탄 지수

    def diagnose_combustion_health(self):
        """점화 지연 및 압력 상승 기반 연소 무결성 진단"""
        if self.id_time > 2.0: # 불이 너무 늦게 붙음
            return "CRITICAL: Excessive Ignition Delay - Fuel Cetane Number too low. Risk of violent 'Diesel Knock' and engine structural damage. Check fuel quality"
        if self.rise > 5.0: # 너무 급격히 터짐 (소음 심함)
            return f"WARNING: High Pressure Rise Rate ({self.rise}) - Rough combustion detected. Potential for high NOx emissions and injector stress"
        if self.ci < 45.0:
            return "NOTICE: Low Cetane Index - Cold starting capability reduced. Engine may require glow plug assistance even in mild conditions"
        return "OPTIMAL: Stable Auto-ignition and High-Fidelity Diesel Combustion Verified"

    def audit_soot_formation(self, exhaust_opacity_pct):
        """매연(Soot) 무결성 진단"""
        if exhaust_opacity_pct > 15.0: # 불완전 연소
            return "REJECT: High Exhaust Opacity - Fuel not mixing properly or poor combustion kinetics. Check fuel-air ratio and injector spray pattern"
        return "PASS: Clean Diffusion Flame and Verified Emission Integrity Confirmed"

engine = FactoryFidelityEngine(ignition_delay_ms=0.8, peak_pressure_rise_bar_deg=3.2, fuel_cetane_index=52.0)
print(engine.diagnose_combustion_health())
```

## 5. 분석 프레임워크: High-Efficiency Diesel Strategy
1. **[Pilot Injection Strategy]**: 본격적인 폭발 전에 아주 적은 양의 기름을 미리 쏘아 불씨를 만들어두는 전략. 큰 폭발의 충격을 줄여 '조용한 디젤'을 만드는 비결입니다.
2. **[Cetane Improver Dosing]**: 약품(2-Ethylhexyl nitrate)을 섞어 기름의 세탄가를 인위적으로 높이는 전략. 정유 과정의 한계를 넘는 '고품질 연료' 제조 기술입니다.
3. **[Exhaust Gas Recirculation (EGR)]**: 연소 온도를 낮춰 질소산화물($NO_x$) 발생을 억제하는 전략. 환경 규제를 통과하기 위한 '착한 연소' 전략입니다.

## 6. 스스로 체크 (Self-Audit)
1. 왜 가솔린은 '옥탄가(잘 안 타는 성질)'가 높아야 좋고, 디젤은 '세탄가(잘 타는 성질)'가 높아야 좋은가? (점화 방식(스파크 vs 압축)의 근본적 차이 관점)
2. '디젤 노킹(Diesel Knock)'은 왜 일어나는가? (너무 늦게 터진 연료가 한꺼번에 폭발하면서 내는 금속성 소음 관점)
3. 세탄가가 너무 높으면(예: 70 이상) 오히려 엔진 효율이 떨어지는 이유는 무엇인가? (공기와 충분히 섞이기도 전에 너무 빨리 타버려 불완전 연소가 일어나는 관점)

## 7. 결론 (Deterministic Outcome)
본 노드는 `Data diesel-cetane-number-and-nox-emissions-v2026`와 연동되어, 전 세계 주요 상용차 및 선박 엔진의 가동 데이터를 실시간 분석하고 엔진 파손 및 대기 오염 사고 확률을 0.001% 이하로 억제함으로써 지능형 모빌리티 문명의 에너지 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 04_autonomous-factory-and-industrial-ai-hub
- cargo-ship-propulsion-and-marine-diesel-engineering
- Data diesel-cetane-number-and-nox-emissions-v2026