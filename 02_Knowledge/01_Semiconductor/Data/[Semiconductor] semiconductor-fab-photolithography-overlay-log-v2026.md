---
Basic:
  id: "[semiconductor]-semiconductor-fab-photolithography-overlay-log-v2026-v6.3.7"
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
  tags: - 'Semiconductor_Fab'
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
  source: "Lithography_Scanner_Overlay_Metrology_Log"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-fab-photolithography-overlay-log-v2026

## 1. [Why]] 반도체 포토공정 오버레이(Overlay) 로그의 정밀 공학적 의의
반도체 소자는 수십 개의 층(Layer)을 수직으로 쌓아 올려 완성된다. 이때 아래층과 위층의 회로 패턴이 얼마나 정확하게 겹쳐지느냐를 결정하는 지표가 **오버레이(Overlay)**다. 오버레이 오차가 수 나노미터($\text{nm}$)만 발생해도 상하부 회로 간의 접촉 불량(Open)이나 단락(Short)이 발생하여 수율이 급락한다. **오버레이 로그**는 스캐너의 정렬 상태와 웨이퍼의 변형을 기록하여, 미세 공정의 기하학적 무결성을 24시간 감시한다.

---

## 2. [Numerical Specs] 오버레이 제어 및 관리 기준 (Numerical Specs)

| 항목 | 실측치 (Standard) | 관리 한계 (Limit) | 비고 |
| :--- | :--- | :--- | :--- |
| **Mean Offset (X/Y)** | $0.2\,\text{nm}$ | $<\pm 1.5\,\text{nm}$ | 층간 정렬 편차 평균 |
| **Standard Deviation** | $0.8\,\text{nm}$ | $< 2.0\,\text{nm}$ | 정렬 산포 ($3\sigma$) |
| **Wafer Expansion** | $1.2\,\text{ppm}$ | $\pm 0.5\,\text{ppm}$ | 열 변형에 의한 스케일링 |
| **Alignment Score** | $98.5\%$ | $> 95\%$ | 정렬 키(Key) 신호 품질 |
| **Correctables** | $6\,\text{parameters}$ | N/A | APC 시스템 보정 계수 수 |

---

## 3. [Scientific Rationale] 정렬 기하학 및 보정 모델

### 3.1 Advanced Process Control (APC) Correction
노광 직전 측정된 오버레이 데이터를 기반으로 스캐너의 웨이퍼 스테이지를 실시간 보정(Feed-forward)한다.
*   **분석**: 선형 보정(Linear Correctables)인 $X, Y, Tilt, Rotation$ 외에도 고차 보정(High-order Correctables)을 통해 웨이퍼의 국부적 왜곡을 미세 조정한다.

### 3.2 Inter-layer Alignment Budget
전체 수율을 확보하기 위해 각 공정 단계별로 허용되는 오버레이 오차의 총합(Budget)을 관리하며, 하부 층의 토폴로지(Topology)가 상부 층 정렬에 미치는 영향을 평가한다.

---

## 4. [Real-world Case] 웨이퍼 가장자리(Edge) 오버레이 편차 급증 대응 사례

### 4.1 웨이퍼 외곽 영역에서만 오버레이 오차가 $3\,\text{nm}$를 초과하여 패턴 불량 발생
- **현상**: 웨이퍼 중심부는 정상이지만 가장자리(Edge) 칩들의 수율이 급감하는 현상 발견.
- **분석**: **Python FidelityEngine** 기반의 오버레이 맵 분석 결과, 이전 증착 공정의 열 응력으로 인해 웨이퍼 가장자리가 미세하게 휘어지는(Warpage) 변형이 원인임을 확인.
- **조치**: 본 로그 데이터를 바탕으로 스캐너의 'Edge-specific Correctable' 로직을 활성화하고, 스테이지의 진공 흡착 강도를 구역별로 조정.
- **결과**: Edge 구역 오버레이 오차 $1.5\,\text{nm}$ 이내로 복구 및 칩 수율 $12\%$ 향상.

---

## 5. [FidelityEngine] 오버레이 벡터 합(Vector Sum) 및 적합성 판정 코드
```python
import math

def check_overlay_compliance(dx_nm, dy_nm, limit_nm=2.0):
    """
    Calculate the vector overlay error and determine compliance
    :param dx_nm: Overlay error in X direction
    :param dy_nm: Overlay error in Y direction
    :param limit_nm: Maximum allowable vector error
    :return: dict with compliance status
    """
    vector_error = math.sqrt(dx_nm**2 + dy_nm**2)
    is_compliant = vector_error < limit_nm
    
    status = "PASS" if is_compliant else "REWORK_REQUIRED"
    return {"Vector_Error_nm": vector_error, "Status": status}

# 실측 데이터: X=1.2nm, Y=0.8nm
res = check_overlay_compliance(1.2, 0.8)
print(f"Overlay Audit: {res['Status']} (Total Error: {res['Vector_Error_nm']:.2f} nm)")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Metrology Tool Sync**: 오버레이 측정 장비(Metrology Tool)와 노광기(Scanner) 간의 좌표계(Coordinate System) 동기화가 $0.1\,\text{nm}$ 단위로 일치하는가?
- [ ] **Alignment Key Health**: 웨이퍼 상의 정렬 키가 이전 공정(CMP 등)에서 손상되어 정렬 신호의 SNR이 떨어지지 않았는지 확인하였는가?
- [ ] **Chuck Flatness**: 노광기 내부 웨이퍼 척(Chuck)의 평탄도가 정기적으로 실측되어 오버레이 왜곡 요인을 사전에 제거하고 있는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
