---
metadata:
  id: "[[[Infrastructure] WMS-Warehouse-Management-System-and-Inventory-Control]]"
  domain: "09_SmartFactory_Production"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Infrastructure] WMS-Warehouse-Management-System-and-Inventory-Control에 관한 고밀도 지능 노드"
semantic:
  tags: ["#09_SmartFactory_Production", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Infrastructure] WMS-Warehouse-Management-System-and-Inventory-Control

## 1. [왜 배우는가? (Why)]
창고에 물건이 얼마나 있는지, 어디에 있는지 모른다면 공장은 멈춥니다. 자재가 있는데 못 찾아서 또 사거나, 없는 줄 알았는데 나중에 유통기한이 지나 발견된다면 막대한 손실입니다. WMS(창고 관리 시스템)는 창고 안의 모든 물건에 '디지털 주소'를 부여하고 일거수일투족을 감시하는 지휘 본부입니다. 물건이 들어올 때(Inbound)부터 나갈 때(Outbound)까지 데이터로 관리하여 재고 낭비를 없앱니다. 이를 이해하는 것은 물류의 불확실성을 제거하고 공장의 동맥을 원활하게 흐르게 하는 '공급망 관리의 기초'를 마스터하는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Function | Process Logic | Engineering Rationale |
|:---|:---:|:---|
| **Inbound** | Receiving & Put-away | 도착한 물건의 수량을 검수하고 최적의 보관 위치를 지정하여 저장 |
| **Inventory Mgmt**| Real-time Tracking | 현재 재고량, 유통기한, 롯트(Lot) 정보를 실시간으로 관리 |
| **Picking** | Route Optimization | 주문이 들어오면 로봇이나 작업자가 가장 짧은 동선으로 물건을 집어오게 유도 |
| **Inventory Acc.**| Cycle Counting | 전수 조사를 위해 공장을 멈추지 않고, 평소에 부분적으로 재고를 대조해 정확도 유지 |
| **Integration** | ERP/MES Bridge | 생산 계획(MES) 및 판매 데이터(ERP)와 연동하여 필요한 자재를 미리 준비 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 위치 최적화와 작업 효율
- **논리**: 자주 나가는 물건은 출입구 가까이에, 가끔 나가는 물건은 먼 곳에 두어야 합니다. 
- **결과**: WMS는 입출고 빈도(ABC 분석)에 따라 물건의 위치를 유동적으로 재배치합니다. 이는 지게차나 로봇의 이동 거리를 최소화하여, 물류 처리 속도를 높이고 에너지 소비를 줄이는 최적화 솔루션을 제공합니다.

### 3.2 데이터 가시성(Visibility)과 안전 재고
- **논리**: 재고가 너무 많으면 돈이 묶이고, 너무 적으면 생산이 멈춥니다. 
- **효과**: WMS를 통해 실시간 재고 흐름을 파악하면, 필요한 만큼만 가지고 있는 '적정 재고' 수준을 과학적으로 산출할 수 있습니다. 이는 기업의 자금 회전율을 높이고 재고 유통기한 경과로 인한 폐기 손실을 방지합니다.

## 4. [코드 연결 해설 (WMS Picking Order & Inventory Update Logic)]
출고 주문을 받아 피킹 리스트를 생성하고 재고를 차감하는 논리 구조입니다.
```python
# 전략 지능 기반 WMS 재고 및 피킹 관리 논리
def process_outbound_order(order_id, items_requested):
    # 1. 재고 가용성(ATP) 확인 및 할당
    for item in items_requested:
        if not wms_db.has_enough_stock(item.id, item.qty):
            return f"ERROR: INSUFFICIENT_STOCK_FOR_{item.id}"
    
    # 2. 최적 피킹 경로(Shortest Path) 생성
    # Algorithm: Travelling Salesman Problem (TSP) Approximation
    picking_list = route_engine.generate_pick_list(items_requested)
    
    # 3. 재고 차감 및 출고 상태 업데이트
    for item in items_requested:
        wms_db.decrease_stock(item.id, item.qty, reason="ORDER_OUT")
        
    # 4. 물류 로봇(AMR)에 피킹 작업 하달
    robot_fleet.assign_task(picking_list)
    
    return f"ORDER_{order_id}_PROCESSED: PICKING_STARTED"
```

## 5. [스스로 체크 (Self-Audit)]
1. 'ERP'의 재고 관리 기능과 'WMS'의 전문적인 재고 관리 기능의 가장 큰 차이는?
2. 창고 관리에서 '바코드' 대신 'RFID'를 도입했을 때 얻을 수 있는 데이터 정확도상의 이점은?
3. 'ABC 분석'을 통한 재고 배치가 물류 센터의 '회전율'에 미치는 영향은?
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
