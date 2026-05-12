---
Basic:
  id: "[data]-smart-factory-wms-inventory-accuracy-log-v2026-v6.3.7"
  domain: "Smart_Factory_Operations"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Data"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'WMS'
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
  source: "WMS_Inventory_RealTime_Log"
  isolation_index: 0.0
---

# [[[Data] smart-factory-wms-inventory-accuracy-log-v2026

## 1. [Why]] 창고 관리 시스템(WMS) 재고 정확도의 공학적 의의
스마트 팩토리에서 **재고 정확도(Inventory Accuracy)**는 생산 계획(APS)과 실제 가동 간의 싱크를 맞추는 근간이다. 시스템상의 재고와 실제 창고의 실물이 일치하지 않으면 원재료 부족으로 인한 라인 정지(Line Stop)나 과잉 재고에 따른 자본 잠식이 발생한다. 본 노드는 **RFID/바코드** 및 **AGV/AMR** 연동 데이터를 기반으로 실시간 재고 오차율을 분석하여 물류 최적화를 지원한다.

---

## 2. [Numerical Specs] WMS 재고 및 물류 파라미터 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 목표 (Target) | 비고 |
| :--- | :--- | :--- | :--- |
| **Inventory Accuracy ($I_a$)** | $99.2\%$ | $> 99.9\%$ | 실물 대 장부 일치율 |
| **Cycle Count Duration** | $4\,\text{hr/zone}$ | $< 2\,\text{hr/zone}$ | 순환 실사 소요 시간 |
| **Picking Error Rate** | $0.05\%$ | $< 0.01\%$ | 오피킹(Miss-picking) 발생율 |
| **Inventory Turnover** | $15.5\,\text{times/yr}$ | $> 18.0\,\text{times/yr}$ | 재고 회전율 |
| **Safety Stock Level** | $3.5\,\text{days}$ | $2 \sim 5\,\text{days}$ | 서비스 레벨 기반 안전 재고량 |

---

## 3. [Scientific Rationale] 재고 오차 및 보충 모델

### 3.1 Inventory Discrepancy Analysis (오차 원인 분석)
오차 발생의 주요 원인을 피킹 실수, 입고 누락, 파손(Scrap) 등으로 분류하고 파레토 차트로 관리한다.
$$I_a = \left( 1 - \frac{\sum |Q_{sys} - Q_{real}|}{\sum Q_{sys}} \right) \times 100$$

### 3.2 Economic Order Quantity (EOQ) 모델
재고 유지 비용과 주문 비용의 합을 최소화하는 최적 주문량을 산출한다.
$$EOQ = \sqrt{\frac{2DS}{H}}$$
*   **$D$**: 연간 수요량.
*   **$S$**: 1회 주문 비용.
*   **$H$**: 단위당 연간 재고 유지 비용.

---

## 4. [Real-world Case] 원재료 수량 오차에 따른 배터리 라인 정지 방지 사례

### 4.1 전해액 드럼 수량 불일치 감지 및 긴급 발주
- **현상**: 시스템상으로는 전해액 5드럼 잔여로 표시되나, AMR(자율 주행 로봇)의 무게 센서 스캔 결과 2드럼만 실물로 확인됨. (오차율 $60\%$)
- **분석**: **Python FidelityEngine**을 활용한 입출고 로그 대조 결과, 3일 전 수동 입고 처리 시 스캔 누락 확인.
- **조치**: APS(생산 계획 시스템)와 연동하여 익일 생산 물량을 긴급 조정하고, 원재료 협력사에 긴급 발주(L/T 4시간) 요청.
- **결과**: 생산 라인 정지(Loss Cost 약 $5$억 원) 사전 방지 및 WMS 스캔 프로세스 강제화 조치.

---

## 5. [FidelityEngine] 재고 정확도 및 EOQ 계산 코드
```python
import math

def calculate_inventory_metrics(sys_qty, real_qty, annual_demand, order_cost, holding_cost):
    """
    Calculate WMS metrics
    :return: dict of results
    """
    accuracy = (1 - abs(sys_qty - real_qty)/sys_qty) * 100
    eoq = math.sqrt((2 * annual_demand * order_cost) / holding_cost)
    
    return {
        "Accuracy": accuracy,
        "EOQ": eoq
    }

# 실측 데이터 대입
res = calculate_inventory_metrics(1000, 995, 50000, 150, 10)
print(f"Inventory Accuracy: {res['Accuracy']:.2f}%")
print(f"Recommended EOQ   : {res['EOQ']:.0f} units")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Real-time Sync**: ERP와 WMS 간의 재고 데이터 동기화 지연이 $1\,\text{min}$ 이내인가?
- [ ] **Location Integrity**: 빈 로케이션(Empty Bin) 관리 및 입고 시 최적 경로(Slotting Optimization)가 반영되는가?
- [ ] **Auto-Refill**: 안전 재고 수준 도달 시 구매 시스템(SRM)과 연동하여 자동 발주 신호가 생성되는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
