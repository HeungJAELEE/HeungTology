---
Basic:
  id: "[semiconductor]-semiconductor-lithography-overlay-error-log-v2026-v6.3.7"
  domain: "Semiconductor_Fabrication"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Lithography'
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
  source: "Lithography_Scanner_APC_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-lithography-overlay-error-log-v2026

## 1. [Why]] 노광 오버레이(Overlay) 에러 로그의 공학적 의의
**노광(Lithography)** 공정에서 **오버레이(Overlay)**는 이전 레이어와 현재 레이어 간의 정렬 정밀도를 나타낸다. 회로 선폭이 나노미터 단위로 미세화됨에 따라, 정렬 오차가 수 nm만 발생해도 층간 회로가 겹치거나 끊어지는 심각한 불량이 발생한다. 본 노드는 스캐너(Scanner)에서 수집된 실시간 정렬 데이터를 분석하여 오버레이 산포를 최소화하고 수율 유출을 방지하는 데이터를 제공한다.

---

## 2. [Numerical Specs] 오버레이 제어 파라미터 (Numerical Specs)

| 항목 | 실측치 (Average) | 관리 한계 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Total Overlay (Mean + 3s)** | $1.8\,\text{nm}$ | $< 2.5\,\text{nm}$ | EUV/ArFi 레이어 기준 |
| **Shift (X, Y)** | $\pm 0.5\,\text{nm}$ | $\pm 1.0\,\text{nm}$ | 웨이퍼 평행 이동 오차 |
| **Rotation** | $0.02\,\mu\text{rad}$ | $< 0.05\,\mu\text{rad}$ | 회전 방향 정렬 오차 |
| **Magnification** | $0.15\,\text{ppm}$ | $< 0.3\,\text{ppm}$ | 열팽창에 의한 배율 오차 |
| **Stage Accuracy** | $0.3\,\text{nm}$ | $< 0.5\,\text{nm}$ | 스캐너 스테이지 위치 정밀도 |

---

## 3. [Scientific Rationale] 오버레이 모델링 및 보정 원리

### 3.1 Linear Modeling (1차 보정 모델)
웨이퍼 상의 위치($x, y$)에 따른 오버레이 에러($\Delta x, \Delta y$)를 선형 함수로 모델링한다.
$$\Delta x = T_x - R_x \cdot y + M_x \cdot x$$
$$\Delta y = T_y + R_y \cdot x + M_y \cdot y$$
*   **$T$ (Translation)**: 평행 이동.
*   **$R$ (Rotation)**: 회전.
*   **$M$ (Magnification)**: 배율.

### 3.2 APC (Advanced Process Control) Feedback
계측 설비에서 측정된 오버레이 맵을 실시간으로 스캐너에 피드백하여 다음 웨이퍼 노광 시 보정치(Offset)를 적용한다.

---

## 4. [Real-world Case] 노광기 스테이지 열 변형에 의한 오버레이 튀는 현상 해결 사례

### 4.1 주간 가동 시간 증가에 따른 비선형 오버레이 증가
- **현상**: 스캐너 가동 10시간 경과 후, 웨이퍼 에지 영역에서 오버레이 에러가 $3.5\,\text{nm}$로 급증하며 USL 초과.
- **분석**: **Python FidelityEngine** 기반의 로그 분석 결과, 스테이지의 고속 이동에 따른 마찰열로 인해 웨이퍼 척(Chuck)의 미세한 비선형 팽창 확인.
- **조치**: 스캐너 냉각 시스템의 설정 온도를 $0.05^\circ\text{C}$ 하향 조정하고, 비선형 보정 모델(High-order Correction)을 APC에 적용.
- **결과**: 에지 영역 오버레이 $2.1\,\text{nm}$로 안정화 및 리워크 비율 $10\%$ 절감.

---

## 5. [FidelityEngine] 오버레이 선형 보정 계산 코드
```python
def calculate_overlay_error(tx, ty, rx, ry, mx, my, x_pos, y_pos):
    """
    Predict overlay error at specific wafer position
    :param tx, ty: Translation offsets
    :param rx, ry: Rotation offsets
    :param mx, my: Magnification offsets
    :return: (dx, dy) predicted error in nm
    """
    dx = tx - (rx * y_pos) + (mx * x_pos)
    dy = ty + (ry * x_pos) + (my * y_pos)
    return dx, dy

# 웨이퍼 에지 지점(x=150mm, y=0mm)에서의 예측 에러
res_x, res_y = calculate_overlay_error(0.5, 0.3, 0.002, 0.002, 0.0001, 0.0001, 150, 0)
print(f"Predicted Error at Edge: dx={res_x:.3f} nm, dy={res_y:.3f} nm")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Alignment Mark Signal**: 웨이퍼 정렬 마크의 신호 대 잡음비(SNR)가 보정 프로세스 수행에 충분한가?
- [ ] **Inter-layer Matching**: 하부층과 현재 층의 노광기(Scanner)가 서로 다를 경우의 매칭 오차(Mix-and-Match)가 관리되고 있는가?
- [ ] **Throughput Impact**: 오버레이 정밀도 향상을 위한 추가 계측(Site 수 증가)이 라인 전체 타임(TAT)을 저해하지 않는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
