---
Basic:
  id: "[semiconductor]-semiconductor-equipment-commonality-analysis-v2026-v6.3.7"
  domain: "Semiconductor_Manufacturing"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Equipment_Commonality'
  is_part_of: - 'Antigravity_Knowledge_Graph'
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
  source: "Equipment_Commonality_Database"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-equipment-commonality-analysis-v2026

## 1. [Why]] 설비 공용화(Commonality) 분석의 공학적 의의
반도체 팹의 대규모 투자(CapEx)를 최적화하기 위해 **설비 공용화**는 필수적이다. 이종(Heterogeneous) 설비 간의 부품 및 인터페이스 공용화율을 높이면, **예비 부품(Spares) 재고**를 $30\%$ 이상 절감하고 유지보수 시간(MTTR)을 단축할 수 있다. 본 노드는 장비 간의 하드웨어 공통 분모를 수치화하여 운영 효율성을 극대화하는 전략적 데이터를 제공한다.

---

## 2. [Numerical Specs] 설비 공용화 지표 (Numerical Specs)

| 분석 항목 | 현재 공용화율 (Current) | 목표치 (Target) | 핵심 공용 부품군 |
| :--- | :--- | :--- | :--- |
| **Mechanical Interface** | $85\%$ | $> 95\%$ | 웨이퍼 반송 로봇 암(Arm), EFEM |
| **Control System (PLC)** | $92\%$ | $> 98\%$ | Mitsubishi Melsec, LS XG5000 |
| **Sensor/Actuator** | $65\%$ | $> 80\%$ | 진공 압력 센서, MFC (Mass Flow Controller) |
| **Power Supply Unit** | $78\%$ | $> 90\%$ | 24V DC/DC Converter, UPS Module |
| **Spares Interchangeability** | $55\%$ | $> 75\%$ | 세라믹 히터, 쿼츠 웨어(Quartz-ware) |

---

## 3. [Scientific Rationale] 공용화 상관관계 모델

### 3.1 Commonality Index ($C_i$) 계산
설비 군집 내에서 동일 부품이 사용되는 비율을 정량화한다.
$$C_i = \frac{\sum_{j=1}^{n} P_j \cdot E_j}{P_{total} \times E_{total}}$$
*   $P_j$: $j$번째 부품의 수량.
*   $E_j$: 해당 부품을 사용하는 설비의 수.
*   **분석**: 지수가 $1.0$에 가까울수록 표준화가 완벽히 이루어졌음을 의미하며, 이는 구매 협상력(Economy of Scale) 강화로 이어진다.

### 3.2 MTBF Reliability Correlation
공용 부품 사용 시, 통계적 표본 수가 증가하여 고장 모드(Failure Mode) 예측의 신뢰도가 향상된다.
$$\text{Reliability Growth} \propto \sqrt{\text{Commonality Usage}}$$

---

## 4. [Real-world Case] 비표준 MFC 도입에 따른 다운타임 발생 사례

### 4.1 이기종 MFC(Mass Flow Controller) 혼용에 의한 공정 변동
- **현상**: A사 식각 장비와 B사 식각 장비의 공용화율이 $40\%$ 미만인 상태에서, 비표준 MFC 고장 시 자재 수급 지연으로 48시간 다운타임 발생.
- **분석**: 데이터 분석 결과, 공용 MFC를 채택한 라인 대비 비표준 라인의 **Inventory Holding Cost**가 $2.5$배 높음.
- **조치**: **Python FidelityEngine**을 활용한 BOM(Bill of Materials) 매칭 시뮬레이션을 통해 5종의 MFC를 2종으로 통합 제안.
- **결과**: 부품 재고 비용 $35\%$ 절감 및 긴급 수리 대응 시간 $60\%$ 단축.

---

## 5. [FidelityEngine] 부품 공용화율 시뮬레이터
```python
def calculate_commonality_index(equipment_matrix):
    """
    Calculate Commonality Index for a given equipment-part matrix
    :param equipment_matrix: List of sets (each set contains part IDs for an equipment)
    :return: Commonality Index (0.0 to 1.0)
    """
    total_equipments = len(equipment_matrix)
    all_parts = set().union(*equipment_matrix)
    
    usage_sum = 0
    for part in all_parts:
        usage_count = sum(1 for equip in equipment_matrix if part in equip)
        usage_sum += usage_count
        
    ci = usage_sum / (len(all_parts) * total_equipments)
    return ci

# 설비 A, B, C의 사용 부품 리스트 시뮬레이션
equip_a = {"Robot_A", "PLC_X", "Sensor_1", "Pump_Y"}
equip_b = {"Robot_A", "PLC_X", "Sensor_2", "Pump_Y"}
equip_c = {"Robot_B", "PLC_X", "Sensor_1", "Pump_Z"}

print(f"Current Commonality Index: {calculate_commonality_index([equip_a, equip_b, equip_c]):.4f}")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **BOM Accuracy**: 현재 MES에 등록된 설비별 BOM 데이터가 현장의 실물 부품과 $100\%$ 일치하는가?
- [ ] **Interchangeability**: 공용 부품 교체 시 별도의 하드웨어 개조나 소프트웨어 패치 없이 즉시 가동(Plug & Play)이 가능한가?
- [ ] **Cost Benefit**: 공용화율 $10\%$ 상승 시 예상되는 재고 유지 비용 절감액이 정량적으로 산출되었는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
