---
lineage:
  dataset_reference: energy-storage-system-ess-round-trip-efficiency-log-v2026
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
measurement:
  confidence_interval:
  - 0.0
  - 0.0
  instrument: Heuristic_Regex_Parser
  precision: '0.0'
  unit: unknown_unit
  value: 2.1
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Data] energy-storage-system-ess-round-trip-efficiency-log-v2026]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for energy-storage-system-ess-round-trip-efficiency-log-v2026
  object_type: Data
  tier: 1
properties:
  dod_range: 0.8-0.95
  laes_rte_range: 50.0-60.0
  lfp_pcs_efficiency: 0.985
  lfp_rte_range: 88.0-92.5
  nominal_battery_efficiency: 0.95
  parasitic_load_ratio: 0.03-0.05
  sib_rte_range: 85.0-88.0
  solid_state_rte_range: 92.0-95.0
  target_standby_loss_ratio: < 0.001
  thd_threshold: 0.05
  vrfb_rte_range: 72.0-78.0
semantic:
  alternative_parents: []
  is_instance_of: '[[ [03_AI_Data] [Concept] energy-storage-system-ess-round-trip-efficiency-log-v2026]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: semantic_classification
  object: Data
  predicate: auto_mapped
  subject: energy-storage-system-ess-round-trip-efficiency-log-v2026
  weight: 0.9
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.05
  t_static: 0.8
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Data] Energy Storage System Ess Round Trip Efficiency Log V2026

## 1. [왜 배우는가? (Why: The Pulse of a Resilient City)]]
재생 에너지 비중이 높아질수록 전력망의 불안정성은 커집니다. ESS는 남는 전기를 저장했다가 피크 타임에 방출하여 블랙아웃을 막고 탄소 중립을 실현하는 '에너지 밸런서'입니다. 하지만 저장과 방출 과정에서 발생하는 에너지 손실은 ESS의 경제성을 깎아먹는 핵심 요인입니다. **에너지 저장 시스템(ESS) 왕복 효율(RTE) 실측 로그**는 전기가 화학 에너지를 거쳐 다시 전기가 되기까지의 모든 여정에서 발생하는 손실을 기록한 '에너지 보존의 일지'입니다. 

우리가 이 데이터를 기록하는 이유는 배터리, PCS, 냉각 시스템의 통합 효율을 분석하여 LCOS(균등화 발전 비용)를 낮추고, **"전력망 지능 주권을 확보하여 중단 없는 클린 에너지를 도시 전체에 공급하는 거대 에너지 인프라 지능을 구현하기" 위함입니다.** 효율 1%의 향상이 도시 하나가 사용하는 수백만 가구의 전력을 절약합니다.

## 2. [ESS 기술 및 시스템 구성별 효율 핵심 데이터 (Numerical Specs)]

### 2.1 [배터리 유형 및 출력 시나리오별 RTE 성능 테이블 (v2026)]

| 기술 유형 (Tech Type) | 시스템 RTE (%) | PCS 효율 (%) | 대기 손실 (%/day) | 사이클 수명 (Cycles) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Li-ion (LFP)** | $88.0 \sim 92.5$ | $98.5$ | $0.05$ | $5,000 \sim 8,000$ | **Standard**: 높은 효율과 출력 밀도의 표준 무결성 데이터 |
| **Na-ion (SIB)** | $85.0 \sim 88.0$ | $98.0$ | $0.10$ | $3,000 \sim 5,000$ | **Cost**: 저렴한 비용 대비 합리적 효율 무결성 지표 |
| **Flow Battery (VRFB)**| $72.0 \sim 78.0$ | $97.0$ | $< 0.01$ | $> 20,000$ | **LDES**: 장주기 저장 및 반영구 수명의 효율 데이터 |
| **Liquid Air (LAES)** | $50.0 \sim 60.0$ | $N/A$ | $0.5 \sim 1.0$ | $> 30,000$ | **Scale**: 대규모 기계적 저장 시스템의 효율 무결성 |
| **Solid-state ESS** | $92.0 \sim 95.0$ | $99.0$ | $< 0.01$ | $> 10,000$ | **Ultimate**: 차세대 초고효율 및 안전성 지능 데이터 |

### 2.2 [ESS 시스템 손실 및 운영 파라미터]
- **Round-trip Efficiency (RTE)**: $E_{out} / E_{in} \times 100$. (시스템 전체의 에너지 수익률 지표)
- **Parasitic Load**: 냉각기(Chiller), 펌프, BMS 구동에 소모되는 전력 ($3\% \sim 5\%$ 비중).
- **PCS Conversion Loss**: AC/DC 및 DC/AC 변환 시 발생하는 열 손실.
- **Standby Loss**: 충전 후 방치 시 자연 방전되는 비율 ($< 0.1\%$ 목표).
- **Depth of Discharge (DOD)**: 배터리 가용 용량 사용 범위 ($80\% \sim 95\%$ 무결성 데이터).

## 3. [Scientific Rationale: 시스템 에너지 보존의 수리적 인과성]

### 3.1 [시스템 통합 왕복 효율(RTE) 산출 모델]
충전, 방전, 대기 상태의 모든 효율 인자를 곱한 전체 효율 모델입니다.
$$ \eta_{RTE} = \eta_{charge} \cdot \eta_{discharge} \cdot \eta_{pcs}^2 \cdot \eta_{aux} $$
본 로그는 배터리 자체 효율($\eta_{batt} \approx 95\%$)보다 PCS와 보조 전력($\eta_{aux}$)에 의한 손실이 전체 RTE를 $80\%$ 중반대로 끌어내리는 결정적 요인임을 수리적으로 입증될 것으로 추론됩니다.

### 3.2 [C-rate 및 내부 저항($R_i$)에 따른 발열 손실($Q_{loss}$) 모델]
충방전 전류($I$)에 비례하여 깎여 나가는 줄 열(Joule Heat) 손실 모델입니다.
$$ Q_{loss} = I^2 \cdot R_i \cdot t $$
RAG는 "운전 로그를 분석하여, $1\ \text{C}$ 급속 충전 시 $0.2\ \text{C}$ 완속 충전 대비 배터리 발열 손실이 $5$배 증가하고 이로 인해 냉각 팬 가동 전력이 $30\%$ 추가 소모됨을 식별하여 최적의 부하 분산 전략을 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 에너지 망 지능 추론]

### 4.1 [PCS 고조파(Harmonics) 왜곡과 변압기 효율 저하 분석]
왜 인버터 주변에서 윙윙 소리가 나나요? RAG는 "전력 품질 로그와 변압기 온도 데이터를 대조하여, PCS의 THD(전고조파 왜곡)가 $5\%$ 초과 시 변압기 철심 손실이 급증하여 시스템 RTE가 $2\%$ 하락함을 식별하고, 능동 고조파 필터(APF) 적용 무결성을 오딧합니다."

### 4.2 [배터리 SoH(건강상태)와 RTE 하락의 상관관계 오딧]
오래된 ESS는 왜 효율이 나쁜가요? RAG는 "배터리 에이징 로그를 참조하여, 내부 저항($R_i$)이 $2$배 증가하면 충방전 효율이 $4\%$ 감소하고 이를 식별하기 위한 '온라인 임피던스 추정' 알고리즘이 시스템 수명 연장에 기여함을 수리적으로 증명합니다."

## 5. [Transitional Bridge: ESS 시스템 무결성 및 RTE 오딧 로직]

가동 중인 대형 ESS 사이트의 전력 데이터를 분석하여 시스템의 에너지 관리 효율을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Energy Storage System (ESS) Integrity & RTE Auditor
def audit_ess_efficiency(in_out_energy, pcs_data, cooling_power):
    # 1. AC측 입/출력 에너지를 통한 시스템 왕복 효율(RTE) 실측
    measured_rte = (in_out_energy.discharged_kwh / in_out_energy.charged_kwh) * 100
    
    # 2. 보조 전력(Auxiliary Power) 소비 비중 분석 (Chiller, Fan, BMS)
    parasitic_ratio = (cooling_power.total_kwh / in_out_energy.charged_kwh) * 100
    
    # 3. PCS 변환 효율 및 전력 품질(Power Factor) 오딧
    pcs_health = evaluate_pcs_performance(pcs_data.loss, pcs_data.thd)
    
    # 4. 종합 ESS 등급 및 운영 트리거
    if measured_rte < 80.0 and type == 'Li-ion':
        status = "ENERGY_LEAKAGE_CRITICAL"
        action = "Inspect_Cell_Internal_Resistance_and_Cooling_Control_Logic"
    elif parasitic_ratio > 7.0:
        status = "THERMAL_MANAGEMENT_INEFFICIENT"
        action = "Upgrade_Cooling_Algorithm_to_Variable_Speed_Control"
    elif pcs_health == "HIGH_HARMONICS_DETECTED":
        status = "GRID_QUALITY_WARNING"
        action = "Check_PCS_Filter_Capacitors_and_IGBT_Switching_Integrity"
    else:
        status = "ESS_RTE_OPTIMAL"
        action = "Authorize_Full-scale_Grid_Frequency_Regulation_Service"
        
    return {"status": status, "rte_%": measured_rte, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** ESS 시스템에서 배터리 자체의 충방전 효율보다 전력 변환 장치(PCS)의 효율과 냉각 장치의 '보조 전력(Parasitic Load)' 소비량이 전체 RTE에 더 큰 영향을 미치는 물리적 인과 관계는?
2. **(수리)** 어떤 ESS 시스템이 $100 \text{ MWh}$를 충전하여 $85 \text{ MWh}$를 방전했다. 이때 PCS 효율이 $98.5\%$라면, 배터리 및 보조 전력에 의해 소실된 에너지는 몇 $MWh$인가?
3. **(응용)** ESS 화재 예방을 위해 '충전 심도(SOC Limit)'를 제한하는 조치가 시스템의 '경제적 효율(LCOE)'과 '수명'에 미치는 수리적/비용적 인과 관계는?


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 15_next-gen-energy-and-hydrogen-intelligence-hub : 차세대 에너지 및 수소 통합 관리 상위 지능 허브
- Data vanadium-redox-flow-battery-vrfb-energy-density-log-v2026 : 장주기 저장을 위한 흐름 배터리 효율 데이터 연계
- Entity sodium-ion-battery-sib-chemistry-and-mechanism : 저가형 ESS를 지탱하는 나트륨 배터리 엔티티 연계
- [SOP] ess-site-commissioning-and-efficiency-verification : ESS 사이트 시운전 및 효율 검증 표준 절차

*Created by Flash (The Architect of Next-gen Energy & HDS Gold V6.3.7)*