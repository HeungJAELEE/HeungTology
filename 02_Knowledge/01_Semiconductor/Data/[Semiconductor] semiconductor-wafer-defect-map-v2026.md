---
Basic:
  id: "[semiconductor]-semiconductor-wafer-defect-map-v2026-v6.3.7"
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
  tags: - 'Wafer_Defect_Map'
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
  source: "In-line_Inspection_Vision"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-wafer-defect-map-v2026

## 1. [Why]] 웨이퍼 결함 맵(Defect Map) 분석의 공학적 의의
웨이퍼 표면에 발생하는 결함은 단순한 '점'이 아니라, 공정 설비의 **이상 징후(Anomaly)**를 나타내는 고밀도 정보다. 결함의 공간적 분포(Spatial Distribution)를 분석하면 고장의 근본 원인(Root Cause)이 식각 챔버의 오염인지, 반송 로봇의 기구적 마찰인지, 혹은 세정 공정의 노즐 막힘인지를 판별할 수 있다. 본 노드는 **SSA(Spatial Signature Analysis)**를 통해 수율을 사수하는 핵심 데이터를 제공한다.

---

## 2. [Numerical Specs] 결함 분석 파라미터 (Numerical Specs)

| 분석 지표 | 실측치 (Average) | 관리 한계 (UCL) | 핵심 결함 유형 |
| :--- | :--- | :--- | :--- |
| **Defect Count** | $45\,\text{ea/wafer}$ | $< 100\,\text{ea}$ | Particle, Scratch, Micro-bridge |
| **Killer Defect Rate** | $12\%$ | $< 5\%$ | 패턴 단락을 유발하는 치명적 결함 |
| **Cluster Defect Ratio** | $25\%$ | $< 15\%$ | 군집형 결함 (설비 오염 징후) |
| **Inspection Resolution** | $15\,\text{nm}$ | $10\,\text{nm}$ (Target) | 비전 검사 시스템의 최소 탐지 크기 |
| **False Alarm Rate** | $2.5\%$ | $< 1\%$ | 노이즈를 결함으로 오인하는 비율 |

---

## 3. [Scientific Rationale] 공간 서명 분석 (SSA) 모델

### 3.1 Defect Clustering Algorithm (DBSCAN)
결함의 밀도를 기반으로 군집을 형성하여 특정 패턴(Signature)을 도출한다.
*   **Ring Pattern**: 웨이퍼 가장자리 세정 불량 또는 베벨 식각(Bevel Etch) 이상.
*   **Scratch Pattern**: 반송 로봇 암(Arm) 또는 CMP 패드의 기구적 접촉.
*   **Radial Pattern**: 회전식 도포(Spin Coating) 시의 가스 흐름 불균형.

### 3.2 Random Defect vs. Systematic Defect
결함 발생이 통계적 확률(Poisson)을 따르는지, 특정 설비의 고정적 오류(Systematic)인지를 구분하여 조치 우선순위를 결정한다.
$$P(k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

---

## 4. [Real-world Case] CMP 공정 스크래치에 의한 대량 불량 방지 사례

### 4.1 CMP(Chemical Mechanical Polishing) 슬러리 응집체에 의한 원형 스크래치
- **현상**: 웨이퍼 중심부에서 외곽으로 뻗어나가는 나선형 스크래치 결함이 전체 롯트(Lot)의 $30\%$에서 발견됨.
- **분석**: **Python FidelityEngine**을 활용한 결함 좌표 시뮬레이션 결과, 스크래치의 곡률이 CMP 헤드의 회전수($\text{RPM}$)와 정확히 일치함을 SSA로 판별.
- **조치**: 슬러리 공급 라인의 필터($0.1\,\mu\text{m}$)를 즉시 교체하고, 패드 드레싱(Dressing) 압력을 $5\%$ 하향 조정.
- **결과**: 스크래치 결함 $95\%$ 제거 및 Killer Defect Rate $3\%$ 이내 진입.

---

## 5. [FidelityEngine] 결함 군집도 분석 코드 (Simplified)
```python
import math

def calculate_defect_density(wafer_radius, defect_count):
    """
    Calculate average defect density per cm^2
    :param wafer_radius: in mm (e.g., 150 for 300mm wafer)
    :param defect_count: total defects
    :return: defects per cm^2
    """
    area_cm2 = math.pi * (wafer_radius / 10)**2
    return defect_count / area_cm2

def is_cluster_suspected(defect_coords, threshold_dist=1.0):
    """
    Simple distance-based clustering check
    :param defect_coords: list of (x, y) tuples in mm
    :param threshold_dist: distance threshold for clustering
    :return: True if clusters are likely
    """
    # Logic: If more than 5 defects are within threshold_dist, suspect cluster.
    # (Simplified for demonstration)
    return len(defect_coords) > 20 # Dummy logic for this mock

# 300mm 웨이퍼 데이터 대입
density = calculate_defect_density(150, 45)
print(f"Defect Density: {density:.4f} ea/cm^2")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **SSA Mapping**: 검출된 결함의 좌표 데이터가 설비의 구동 모션(Rotation/Translation)과 일치하는 패턴을 보이는가?
- [ ] **Killer Defect Filtering**: 비전 알고리즘이 패턴 위의 결함과 빈 공간의 결함을 구분하여 '치명도'를 정확히 산출하는가?
- [ ] **Review Sync**: 검사 설비(KLA)에서 발견된 결함이 리뷰 설비(SEM)에서 정확히 추적(Re-detection)되는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
