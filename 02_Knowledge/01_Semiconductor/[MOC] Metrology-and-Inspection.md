---
Basic:
  id: "[moc]-metrology-and-inspection-v6.3.7"
  domain: "Semiconductor_Metrology"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "MOC"
  tier: 0
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Metrology'
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
  source: "Semiconductor_Quality_Assurance"
  isolation_index: 0.0
---

# [[[MOC] Metrology-and-Inspection

## 1. [Why]] 계측 및 검사(Metrology & Inspection)의 반도체 공학적 의의
반도체 제조 공정에서 **계측(Metrology)**과 **검사(Inspection)**는 공정의 방향을 결정하는 '눈'과 같다. $10\text{nm}$ 이하의 초미세 패턴을 구현함에 있어, 패턴의 치수(CD), 층간 정렬(Overlay), 미세 결함(Defect)을 나노미터급으로 측정하지 못하면 수율(Yield) 확보는 불가능하다. 본 MOC 허브는 전공정 및 후공정의 모든 계측 데이터를 통합 관리하여 공정 능력을 극대화하는 컨트롤 타워 역할을 수행한다.

---

## 2. [Numerical Specs] 주요 계측 및 검사 사양 (Numerical Specs)

| 항목 | 핵심 기술 (Technology) | 정밀도 (Precision) | 비고 |
| :--- | :--- | :--- | :--- |
| **CD (Critical Dimension)** | CD-SEM, Scatterometry | $< 0.1\,\text{nm}$ | 선폭 및 피치 계측 |
| **Overlay** | Optical, DBO (Diffraction) | $< 0.5\,\text{nm}$ | 상하층 패턴 정렬 오차 |
| **Defect Detection** | Bright-field, E-beam | $> 10\,\text{nm}$ (Min) | 이물 및 패턴 결함 검출 |
| **Thin Film Thickness** | Ellipsometry | $< 0.05\,\text{\AA}$ | 박막 두께 및 굴절률 |
| **Throughput** | High-speed Optics | $> 100\,\text{WPH}$ | 시간당 웨이퍼 처리량 |

---

## 3. [Scientific Rationale] 광학 및 전자빔 계측 모델

### 3.1 Scatterometry (OCD) 모델
주기적인 패턴에 조사된 빛의 회절 스펙트럼을 분석하여 패턴의 $3$D 형상을 재구성한다.
$$I(\lambda, \theta) = f(\text{Height, Width, Side-wall Angle})$$
*   **분석**: 실시간 비파괴 계측이 가능하여 대량 생산 라인의 공정 모니터링에 필수적이다.

### 3.2 Signal-to-Noise Ratio (SNR) in E-beam
전자빔을 이용한 검사 시 노이즈 대비 신호 강도를 극대화하여 미세 결함 검출력을 높인다.

---

## 4. [Real-world Case] 오버레이(Overlay) 자동 보정을 통한 수율 개선 사례

### 4.1 노광 공정의 상하층 정렬 오차 $0.5\,\text{nm}$ 달성
- **현상**: 신규 레이어 노광 시 특정 영역에서 오버레이 오차가 USL($2.0\,\text{nm}$)에 근접하며 후속 에칭 공정 시 회로 단선 위험 증가.
- **분석**: **Python FidelityEngine** 기반의 오버레이 로그 분석 결과, 하부층 웨이퍼의 미세 열 변형에 의한 비선형 왜곡(Grid Distortion) 포착.
- **조치**: 계측 설비에서 추출된 오버레이 맵을 노광기(Scanner)의 스테이지 보정 알고리즘(APC)에 즉시 피드백.
- **결과**: 오버레이 오차 $0.6\,\text{nm}$로 하락(안정화) 및 리워크(Rework) 비율 $30\%$ 감소.

---

## 5. [FidelityEngine] 계측 오차 보정(Matching) 알고리즘
```python
def calculate_matching_offset(ref_value, meas_value):
    """
    Calculate tool-to-tool matching offset
    :param ref_value: Reference standard value
    :param meas_value: Measured value from target tool
    :return: Offset to be applied
    """
    offset = ref_value - meas_value
    return offset

# CD-SEM 호기 간 매칭 시뮬레이션
ref_cd = 15.20 # nm
tool_a_cd = 15.35 # nm

applied_offset = calculate_matching_offset(ref_cd, tool_a_cd)
print(f"Tool A Calibration Offset: {applied_offset:.2f} nm")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Sampling Strategy**: 공정 변동을 감지하기 위한 웨이퍼 내 계측 지점(Shot/Site) 수가 통계적으로 유의미한가?
- [ ] **Gage R&R**: 계측기 자체의 반복성(Repeatability)과 재현성(Reproducibility)이 전체 공정 산포의 $10\%$ 이내인가?
- [ ] **Recipe Validation**: 신규 제품 등록 시 계측 조건(Recipe)이 실제 형상을 $99\%$ 이상 모사하도록 최적화되었는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
