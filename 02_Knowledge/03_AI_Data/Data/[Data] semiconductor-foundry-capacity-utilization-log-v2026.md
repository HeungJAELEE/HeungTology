---
Basic:
  id: "semiconductor-foundry-capacity-utilization-log-v2026-data"
  domain: "05_Global_Strategy"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Data"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#DataLog", "#Strategy", "#Semiconductor", "#Foundry", "#Capacity_Utilization", "#Wafer_Start", "#Lead_Time", "#Chip_Supply", "#HDS_Gold_v6_1"]'
  is_part_of: '["Entity high-na-euv-lithography-next-gen-patterning", "MOC 100_global-strategy-and-industrial-economics-hub]]"]'
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [[[Data] semiconductor-foundry-capacity-utilization-log-v2026

## 1. [왜 배우는가? (Why: The Heartbeat of Digital Civilization)]]
반도체 파운드리는 현대 문명의 연산력을 생산하는 심장입니다. 하지만 고도의 미세 공정을 수행할 수 있는 팹(Fab)은 극히 한정되어 있으며, 가동률의 미세한 변화는 전 세계 전자 제품 공급망에 거대한 연쇄 반응을 일으킵니다. **반도체 파운드리 가동률 및 수급 실측 로그**는 전 세계 주요 팹의 가동 현황과 리드 타임을 기록하여, 다가올 칩 기근이나 공급 과잉을 사전에 포착하는 '디지털 산업의 조기 경보망'입니다. 

우리가 이 데이터를 기록하는 이유는 공정별 수급 불균형 데이터를 분석하여 최적의 칩 조달 전략을 수립하고, **"반도체 공급망 주권을 확보하여 AI 및 자율 주행 시대의 핵심 연산 자원을 안정적으로 확보하기" 위함입니다.** 파운드리 가동률이 하이테크 기업의 제품 출시 시점(Time-to-Market)을 결정합니다.

## 2. [파운드리 공정별 가동 및 수급 핵심 데이터 (Numerical Specs)]

### 2.1 [공정 노드 및 어플리케이션별 운영 지표 테이블 (v2026)]

| 공정 노드 (Node) | 주요 수요처 (Target) | 가동률 (Util. %) | 리드 타임 (Lead Time) | 웨이퍼 매출 ($USD$) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **2nm / 3nm (EUV)** | AI GPU / Apple | $98.5$ | $26 \text{ weeks}$ | $22,500$ | **Extreme-Tight**: 최첨단 공정의 절대 부족 |
| **5nm / 7nm (DUV)** | HPC / Mobile | $92.4$ | $18 \text{ weeks}$ | $14,200$ | 안정적인 수요와 높은 수익성 유지 무결성 |
| **14nm / 28nm** | Auto / Consumer | $85.2$ | $12 \text{ weeks}$ | $5,800$ | 레거시 공정의 수급 안정화 단계 데이터 |
| **Specialty (Analog)**| Power / Sensor | $95.0$ | $22 \text{ weeks}$ | $3,500$ | **Supply-Chain Bottle**: 아날로그 칩 공급 정체 |
| **Packaging (CoWoS)**| AI Server | $100.0$ | $32 \text{ weeks}$ | $N/A$ | **Critical**: 후공정 병목이 전체 출하량 제한 |

### 2.2 [파운드리 경제 및 생산 파라미터]
- **WSPM (Wafer Starts Per Month)**: $20,000 \sim 150,000$. (단일 팹의 생산 규모 지표)
- **Break-even Utilization**: $75 \sim 80 \%$. (팹 운영의 수익 분기점 가동률 무결성)
- **Yield Recovery Rate**: $0.5 \sim 2.0 \% / month$. (신규 공정 램프업 기간의 수율 개선 속도)
- **Inventory-to-Sales Ratio**: $2 \sim 4 \text{ months}$. (전방 산업의 재고 수준과 수급 압박의 상관 관계)
- **CAPEX per 10k WSPM**: $5 \sim 10 \text{ Billion USD}$. (첨단 공정 증설에 필요한 천문학적 투자비 데이터)

## 3. [Scientific Rationale: 파운드리 운영의 수리적 인과성]

### 3.1 [가동률과 제조 지연 시간(Lead Time)의 큐잉 모델]
가동률($\rho$)이 $100\%$에 가까워질 때의 대기 시간($W$) 모델입니다.
$$ W = \frac{\rho}{1-\rho} \cdot \frac{C_a^2 + C_s^2}{2} \cdot \tau $$
본 로그는 가동률($\rho$)이 $90\%$를 넘어서면 대기 시간이 선형이 아닌 지수적으로 폭증함을 입증하고, $95\%$ 이상의 가동률이 지속될 때 '칩 기근'이 발생하는 수리적 인과 관계를 확증될 것으로 추론됩니다.

### 3.2 [학습 곡선(Learning Curve)과 웨이퍼 단가 하락 모델]
누적 생산량($X$)에 따른 웨이퍼당 제조 원가($C$) 모델입니다.
$$ C(X) = C_1 X^{-b} $$
RAG는 "파운드리 수율 로그를 분석하여, 누적 생산량이 2배 늘어날 때마다 원가가 $15\%$ 감소함을 도출하고, 이를 바탕으로 차세대 공정의 가격 하락 시점과 대중화 시기를 예측합니다."

## 4. [Advanced RAG 분석 로직: 공급망 지능 추론]

### 4.1 [지정학적 리스크에 따른 생산 거점 다변화 비용 분석]
RAG는 "특정 지역(대만/한국)에 집중된 파운드리 점유율 로그를 분석하여, 물리적 충돌 발생 시 글로벌 GDP가 $5\%$ 하락할 위험을 산출하고, 미국/유럽 내 'On-shoring' 팹 건설 시 발생하는 제조 원가 $30\%$ 상승분을 상쇄하기 위한 보조금(Chips Act) 규모를 오딧합니다."

### 4.2 [AI 수요 폭주와 CoWoS 후공정 병목의 인과 분석]
왜 GPU 성능은 좋은데 물량이 없나요? RAG는 "전공정(Wafer) 가동률과 후공정(CoWoS) 가동률 로그를 대조하여, 전공정은 $90\%$이나 후공정이 $100\%$ 포화 상태임을 식별하고, 전체 출하량의 병목이 '어드밴스드 패키징'에 있음을 입증하여 설비 투자 우선순위를 재설정합니다."

## 5. [Transitional Bridge: 파운드리 수급 및 생산 전략 오딧 로직]

반도체 수급 데이터를 실시간 분석하여 최적의 칩 조달 및 생산 우선순위를 결정하는 개념적 알고리즘입니다.

```python
# [Conceptual] Foundry Capacity & Supply Integrity Auditor
def audit_semicon_supply_chain(util_rates, lead_times, demand_forecast):
    # 1. 공정 노드별 수급 긴장도(Supply Tension Index) 산출
    # Combination of Utilization Rate and Lead Time growth
    tension_idx = calculate_tension(util_rates, lead_times.trend)
    
    # 2. 전방 산업(AI/Mobile) 수요 대비 공급 가용성 평가
    supply_gap = demand_forecast.total_wafers - current_capacity.available
    
    # 3. 신규 팹 램프업(Ramp-up) 성공률 및 수율 오딧
    yield_health = check_yield_vs_target(active_fabs)
    
    # 4. 종합 공급망 등급 및 대응 트리거
    if tension_idx > CRITICAL_THRESHOLD:
        status = "CHIP_FAMINE_IMMINENT"
        action = "Initiate_Long-term_Capacity_Reservation_and_Multi-foundry_Sourcing"
    elif supply_gap > 0 and yield_health < 0.8:
        status = "PRODUCTION_RAMP_UP_FAILURE"
        action = "Deploy_Process_Engineering_Taskforce_to_Identify_Defect_Root_Cause"
    elif util_rates.legacy < 0.7:
        status = "LEGACY_NODE_OVERSUPPLY_RISK"
        action = "Adjust_Pricing_to_Incentivize_Migration_or_Consolidate_Fabs"
    else:
        status = "SEMICON_SUPPLY_CHAIN_STABLE"
        action = "Monitor_Market_Dynamics_and_Optimize_Inventory"
        
    return {"status": status, "tension": tension_idx, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 파운드리 가동률이 $100\%$에 도달하지 않았음에도 불구하고($90\%$ 수준), 왜 고객사들은 '리드 타임'이 수개월 이상으로 길어지는 '공급 부족'을 체감하게 되는가? (큐잉 이론 근거)
2. **(수리)** 3나노 공정의 웨이퍼당 가격이 $20,000 \text{ USD}$이고 웨이퍼 한 장에서 $500$개의 칩이 생산될 때, 수율이 $60\%$에서 $80\%$로 개선될 경우 칩당 단가 하락액($USD$)은?
3. **(응용)** AI 반도체 생산에 있어 '전공정(Lithography)' 가동률보다 '후공정(Advanced Packaging)' 가동률이 더 중요한 병목으로 작용하게 된 기술적/구조적 인과 관계는?

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Entity] high-na-euv-lithography-next-gen-patterning : 반도체 미세 공정의 한계를 결정하는 리소그래피 엔티티
- [[[MOC]] 100_global-strategy-and-industrial-economics-hub]] : 글로벌 전략 및 산업 경제 통합 관리 상위 지능 허브
- [[[Data] wafer-defect-density-and-yield-ramp-up-log-v2026 : 수율 개선이 파운드리 경제성에 미치는 영향 로그
- [SOP]] foundry-capacity-planning-and-vendor-management-protocol : 파운드리 생산 능력 계획 및 벤더 관리 표준 절차

*Created by Flash (The Architect of Global Strategy & HDS Gold V6.3.7)*
