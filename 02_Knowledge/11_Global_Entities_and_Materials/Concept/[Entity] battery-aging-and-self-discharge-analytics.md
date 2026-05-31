---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 804fc1f7da4fe44dc9db76705904ca21aec6d8167c6936c759d77b1f470e3364
metadata:
  date: '2026-05-16'
  domain: 11_Global_Entities_and_Materials
  id: '[[[Entity] battery-aging-and-self-discharge-analytics]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Entity] battery-aging-and-self-discharge-analytics에 관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  arrhenius_temp_threshold_celsius: 45
  cycle_life_ncm_min: 2000
  external_data_endpoint: battery-aging-curve-and-self-discharge-log-v2026
  internal_res_eol_threshold_ratio: 2.0
  self_discharge_eol_threshold_pct_month: 10
  self_discharge_fresh_threshold_pct_month: 3
  self_discharge_warning_threshold_mv_day: 5.0
  soh_eol_threshold_pct: 80
  target_prediction_accuracy_pct: 95
  voltage_drop_eol_threshold_mv_day: 10
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

# [Entity] battery-aging-and-self-discharge-analytics

## 1. 개요 (Why)
배터리는 살아있는 생명체와 같아서 시간이 흐를수록 늙어갑니다. 내부 저항이 커지고 용량이 줄어드는 '노화(Aging)'와 가만히 두어도 전하가 새어나가는 '자가 방전(Self-discharge)'은 전기차의 주행 거리를 단축시키고 수명을 결정짓는 핵심 요소입니다. 본 노드는 배터리의 노화 과정을 수치화하고, 이를 정밀하게 예측하여 배터리 자산 가치를 극대화하기 위한 분석 표준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Fresh Cell | Aged (EOL) | Unit |
| :--- | :--- | :--- | :--- | :--- |
| State of Health | $SoH$ | 100 | 80 ~ 70 | % |
| Self-discharge | $SD$ | < 3 | > 10 | % / month |
| Internal Res | $R_{dc}$ | 1.0 | > 2.0 | ratio (relative)|
| Cycle Life | $N$ | > 2,000 | N/A | cycles (NCM) |
| Voltage Drop | $\Delta V_{rest}$| < 1 | > 10 | mV/day |

## 3. BMSFidelityEngine: Diagnostic Logic

배터리의 노화 상태 및 자가 방전 위험을 진단하는 `BMSFidelityEngine` 로직입니다.

```python
class BMSFidelityEngine:
    def __init__(self, current_capacity, internal_resistance, rest_v_drop):
        self.cap = current_capacity # Ah
        self.res = internal_resistance # mOhm
        self.drop = rest_v_drop # mV/day

    def diagnose_soh_health(self, bol_capacity):
        """용량 유지율 기반 수명 건전성 진단"""
        soh = (self.cap / bol_capacity) * 100
        if soh < 80:
            return f"CRITICAL: Battery EoL (SoH: {soh:.1f}%) - Replacement or Second-life Required"
        return f"OPTIMAL: Battery Health Stable (SoH: {soh:.1f}%)"

    def audit_self_discharge(self):
        """휴지기 전압 강하 기반 자가 방전 진단"""
        if self.drop > 5.0: # 5mV/day 초과 시 비정상 자가 방전 의심
            return f"WARNING: Abnormal Self-discharge ({self.drop}mV/day) - Check for Micro-shorts"
        return "PASS: Leakage Current Within Normal Range"

engine = BMSFidelityEngine(current_capacity=42, internal_resistance=15, rest_v_drop=1.5)
print(engine.diagnose_soh_health(bol_capacity=50))
```

## 4. 분석 프레임워크: Aging Analysis Hierarchy
1. **[Capacity Fade Modeling]**: SEI 층의 지속적인 성장과 리튬 이온의 소모(LLI) 과정을 물리적-수학적 모델로 구현하여 수명 곡선 예측.
2. **[Resistance Growth Tracking]**: 양극재 구조 붕괴나 전해질 산화로 인한 내부 저항 증가를 DCIR(직류내부저항) 측정을 통해 상시 모니터링.
3. **[Machine Learning-based RUL]**: 과거 충방전 데이터를 기반으로 잔여 수명(Remaining Useful Life)을 딥러닝으로 예측하여 유지보수 시점 최적화.

## 5. 스스로 체크 (Self-Audit)
1. 고온(45도 이상) 보관 시 배터리의 '자가 방전' 속도가 지수 함수적으로 빨라지는 아레니우스(Arrhenius)적 이유는?
2. 배터리 노화 시 전압 평탄도(Voltage Plateau) 변화가 'OCV-SoC' 맵의 드리프트를 유발하여 SoC 추정 오차를 키우는 기전은?
3. '급속 충전'이 리튬 플레이팅을 유도하여 노화를 가속화하는 물리적 임계 전류 밀도($J_{crit}$) 계산법은?

## 6. 결론 (Deterministic Outcome)
본 노드는 `Data battery-aging-curve-and-self-discharge-log-v2026`와 연동되어, 배터리의 모든 충방전 이력을 분석하고 잔여 수명을 95% 이상의 정확도로 예측함으로써 배터리 생애 주기 관리의 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 11_advanced-battery-next-gen-intelligence-hub
- cycle-life-vs-calendar-life
- Data battery-aging-curve-and-self-discharge-log-v2026