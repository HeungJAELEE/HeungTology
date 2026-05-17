---
metadata:
  id: "[[[Infrastructure] SEMI-E142-Substrate-Mapping-Standard]]"
  domain: "09_SmartFactory_Production"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Infrastructure] SEMI-E142-Substrate-Mapping-Standard에 관한 고밀도 지능 노드"
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

# [Infrastructure] SEMI-E142-Substrate-Mapping-Standard

## 1. [왜 배우는가? (Why)]
수천 개의 칩(Die)이 박힌 웨이퍼 한 장이 공정을 지날 때, 어떤 칩이 '합격'이고 어떤 칩이 '불량'인지 어떻게 알 수 있을까요? 그리고 그 정보가 패키징 공장까지 정확히 전달될 수 있을까요? SEMI E142는 웨이퍼나 패키징 기판 위의 각 다이(Die) 위치와 검사 결과(Bin) 데이터를 주고받는 세계 공통의 '디지털 지도' 규격입니다. SEMI E142를 이해하는 것은 칩 하나하나의 이력을 추적(Traceability)하여 불량 칩을 정확히 골라내고, 수율 데이터를 최적화하는 '데이터 기반 제조'의 핵심을 마스터하는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Function / Format | Engineering Rationale |
|:---|:---:|:---|
| **Wafer Map** | Substrate Map | 웨이퍼 상의 각 칩 좌표(x, y)와 고유 ID를 정의하는 논리적 지도 데이터 |
| **Binning Data** | Pass/Fail Codes | 각 칩의 전기적 테스트 결과(예: Bin 1-Pass, Bin 2-Fail)를 분류하여 저장 |
| **XML / JSON** | Data Schema | 다양한 장비와 소프트웨어가 읽을 수 있는 표준화된 데이터 형식 채택 |
| **Origin Reference**| Notch/Flat Pos. | 웨이퍼의 물리적 방향 기준점을 설정하여 지도와 실제 칩의 위치를 정렬 |
| **Traceability** | Unit Level Tracking| 개별 칩 단위로 어떤 공정에서 어떤 결과가 나왔는지 시계열적으로 추적 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 공급망 전체의 데이터 정합성 유지
- **논리**: 웨이퍼 제조사와 패키징 업체가 서로 다른 맵 형식을 쓰면 데이터 변환 과정에서 오류가 발생합니다. 
- **결과**: SEMI E142는 전 세계 공통의 스키마를 제공함으로써, 공정 간 또는 공장 간 이동 시에도 다이 특성 데이터의 왜곡 없는 전달을 보장하고 불량 칩이 조립 단계로 넘어가는 것을 완벽히 방어합니다.

### 3.2 선별 조립(Pick & Place) 최적화
- **논리**: 불량 칩을 하나하나 눈으로 보고 골라내는 것은 불가능합니다. 
- **효과**: E142 맵 데이터를 직접 읽는 자동화 장비는 'Good Die' 위치만 정확히 찾아내어 고속으로 피킹함으로써, 조립 공정의 생산성을 극대화하고 최종 제품의 품질 신뢰도를 높입니다.

## 4. [코드 연결 해설 (Wafer Map Data Processing Logic)]
웨이퍼 맵 데이터를 읽어 특정 칩의 상태를 확인하는 논리 구조 예시입니다.
```python
# 장비 지능 기반 SEMI E142 웨이퍼 맵 처리 논리
import xml.etree.ElementTree as ET

def read_wafer_map(e142_xml_file):
    tree = ET.parse(e142_xml_file)
    root = tree.get_root()
    
    # 1. 웨이퍼 정보 및 그리드 설정 추출
    wafer_id = root.find('.//SubstrateID').text
    
    # 2. 다이 정보 및 Bin 데이터 추출
    die_results = {}
    for die in root.findall('.//Die'):
        x = die.get('X')
        y = die.get('Y')
        bin_code = die.get('BinCode')
        die_results[(x, y)] = bin_code
        
    return {"wafer_id": wafer_id, "die_map": die_results}

# 특정 좌표의 칩이 'Good Die'인지 확인
# if map['die_map'][(10, 20)] == '1': pick_and_place()
```

## 5. [스스로 체크 (Self-Audit)]
1. 'Binning' 작업이 반도체 수율 관리에서 가지는 결정적인 역할은?
2. '웨이퍼 맵' 데이터가 소실되었을 때 후속 패키징 공정에서 발생하는 최악의 시나리오는?
3. 'XML' 형식이 SEMI E142의 표준으로 채택된 기술적 배경은? (힌트: 계층 구조 및 확장성)
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
