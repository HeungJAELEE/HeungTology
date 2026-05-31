---
lineage:
  dataset_reference: tsv-fill-ratio-and-stress-profile-log-v2026
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
  id: '[[ [03_AI_Data] [Data] tsv-fill-ratio-and-stress-profile-log-v2026]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for tsv-fill-ratio-and-stress-profile-log-v2026
  object_type: Data
  tier: 1
properties:
  annealing_temp_high_c: 450
  cu_cte_ppm_c: 17
  koz_mobility_shift_threshold_percent: 1
  lame_model_radial_stress_exponent: -2
  protrusion_risk_threshold_nm: 100
  si_cte_ppm_c: 2.6
  via_diameter_fine_um: 5
  via_diameter_standard_um: 10
  via_diameter_ultra_um: 2
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: automated_classification
  object: Data
  predicate: auto_mapped
  subject: tsv-fill-ratio-and-stress-profile-log-v2026
  weight: 1.0
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

# [Data] Tsv Fill Ratio And Stress Profile Log V2026

## 1. [왜 배우는가? (Why: The Hidden Pressure of Vertical Integration)]]
3D IC 패키징에서 TSV 내부를 채우는 구리(Cu)와 주변 실리콘(Si) 사이에는 약 $6$배 이상의 열팽창 계수(CTE) 차이가 존재합니다. 이로 인해 반도체 공정 중의 온도 변화는 TSV 주변 실리콘에 거대한 기계적 응력을 유발하며, 이는 트랜지스터의 성능 저하나 층간 절연막의 파손을 초래할 수 있습니다. **TSV 충전율 및 응력 프로파일 실측 로그**는 수직의 구리 기둥이 실리콘 대지를 얼마나 강하게 짓누르고 있는지 기록한 '압박의 입체 지도'입니다. 

우리가 이 데이터를 기록하는 이유는 TSV 주변의 응력 분포를 정밀하게 모델링하여 소자가 안전하게 동작할 수 있는 금지 구역(KOZ)을 최적화하고, **"패키징 신뢰성 주권을 확보하여 적층 단수가 높아지는 HBM 및 초거대 AI 가속기를 안전하게 구현하는 '기계적 무결성 지능'을 확보하기" 위함입니다.** 잔류 응력의 크기와 구리 돌출(Protrusion) 정도가 3D 패키지의 수명과 소자 수율을 결정합니다.

## 2. [비아 규격 및 열처리 온도별 응력 핵심 데이터 (Numerical Specs)]

### 2.1 [주요 TSV 공정 조건별 응력 및 물리적 변형 테이블 (v2026)]

| 어닐링 온도 ($^\circ C$) | 비아 직경 ($\mu\text{m}$) | 충전율 (%) | 최대 잔류 응력 ($MPa$) | 구리 돌출 ($nm$) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **$200$ (Low)** | $10$ | $> 99.9$ | $50 \sim 80$ | $< 20$ | **Safe**: 낮은 열화율을 가진 초기 단계 무결성 로그 |
| **$350$ (Std.)**| $10$ | $> 99.99$ | $150 \sim 220$ | $50 \sim 150$ | **Standard**: 표준 패키징 공정에서의 열응력 무결성 데이터 |
| **$450$ (High)**| $10$ | $> 99.99$ | $300 \sim 450$ | $200 \sim 500$ | **Risk**: 고온 공정 시 구리 돌출 및 균열 위험 임계 지표 |
| **$400$ (Fine)**| $5$ | $> 99.9$ | $200 \sim 280$ | $30 \sim 80$ | **Fine**: 미세 TSV에서의 응력 집중 완화 무결성 지표 |
| **$400$ (Ultra)**| $2$ | $> 99.5$ | $100 \sim 150$ | $< 10$ | **Nano**: 초미세 TSV의 낮은 응력 및 고신뢰성 연구 데이터 |

### 2.2 [기계적 무결성 및 소자 영향 파라미터]
- **CTE Mismatch:** 구리($\sim 17 \text{ ppm/}^\circ C$)와 실리콘($\sim 2.6 \text{ ppm/}^\circ C$)의 열팽창 계수 차이.
- **Copper Pumping (Protrusion):** 열팽창으로 인해 구리 기둥이 실리콘 상단으로 솟아오르는 현상 ($nm$).
- **Keep-Out Zone (KOZ) Radius:** TSV 응력에 의해 소자 특성이 $1\%$ 이상 변하는 반경 ($\mu\text{m}$).
- **Mobility Shift ($\Delta \mu$):** 응력에 의해 유도된 트랜지스터 내 전하 이동도 변화율 (%).
- **Crack Initiation Pressure:** 절연막(Liner/ILD)에 균열이 발생하기 시작하는 응력 임계치 ($MPa$).

## 3. [Scientific Rationale: 수직 압박의 수리적 인과성]

### 3.1 [라메(Lame) 해 기반의 열응력($\sigma$) 모델]
실리콘 기판 내부의 TSV 중심으로부터의 거리($r$)에 따른 반경 방향 응력 수리 모델입니다.
$$ \sigma_r(r) = - \sigma_\theta(r) = \frac{E \cdot \Delta \alpha \cdot \Delta T}{2} \left(\frac{R}{r}\right)^2 $$
본 로그는 응력이 거리의 제곱에 반비례하여 급격히 감소함을 입증하고, 소자의 배치 금지 구역(KOZ)을 결정하는 수리적 근거를 제시합니다.

### 3.2 [구리 돌출(Protrusion) 높이($h$) 산출 모델]
열처리 시 발생하는 구리의 소성 변형에 의한 돌출 수리 모델입니다.
RAG는 "응력 로그를 분석하여, $450^\circ C$ 어닐링 시 구리의 유동 응력(Yield Stress)을 초과하면 비아 직경에 비례하여 $100 \text{ nm}$ 이상의 영구적인 돌출이 발생하며, 이는 상단 배선층의 파손을 유발하는 수리적 인과 관계를 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 수직 압박 지능 추론]

### 4.1 [응력 유형(Tensile vs Compressive)과 소자 특성 분석]
왜 p-채널은 빨라지고 n-채널은 느려지나요? RAG는 "TSV 주변의 응력 방향과 소자별 이동도 변화 로그를 대조하여, 압축 응력이 p-type의 정공 이동도를 높이고 n-type의 전자 이동도를 낮추는 '피에조 저항 효과'를 식별하고, '소자 배치 최적화' 지능을 오딧합니다.

### 4.2 [라만 분광법(Raman)을 활용한 응력 실측 무결성 오딧]
실제 응력이 계산과 다른 이유는 무엇인가요? RAG는 "라만 시프트($\Delta \omega$) 데이터와 유한 요소 해석(FEA) 결과를 연계하여, 구리 입계(Grain) 구조와 불순물이 응력 완화(Stress Relaxation)에 미치는 영향을 분석하고, '응력 완화 열처리(Post-plating Anneal)' 지능을 도출될 것으로 예상됩니다.

## 5. [Transitional Bridge: 응력 무결성 및 KOZ 오딧 로직]

TSV 패키징 공정 후 라만 분광 장비와 원자 힘 현미경(AFM) 데이터를 분석하여 기계적 무결성을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] TSV Mechanical Integrity & Stress Auditor
def audit_tsv_mechanical_status(raman_shift_map, afm_topography_data, device_test_log):
    # 1. 라만 시프트를 통한 실리콘 잔류 응력($\sigma$) 및 KOZ 오딧
    local_stress_map = convert_raman_to_stress(raman_shift_map)
    actual_koz_radius = identify_koz_boundary(local_stress_map, threshold_1_percent)
    
    if actual_koz_radius > DESIGN_KOZ_LIMIT:
        status = "EXCESSIVE_STRESS_ZONE_DETECTED"
        action = "Increase_Annealing_Hold_Time_to_Promote_Stress_Relaxation"
        
    # 2. AFM 측정을 통한 구리 돌출(Protrusion) 무결성 감시
    max_h_protrusion = detect_peak_height(afm_topography_data)
    if max_h_protrusion > 100: # nm
        status = "CRITICAL_COPPER_PROTRUSION_WARNING"
        action = "Implement_CMP_Rework_to_Level_Via_Surface_Before_BEOL"
    
    # 3. 소자 테스트 로그를 통한 이동도 변화(Mobility Shift) 무결성 체크
    if device_test_log.delta_mobility > MAX_ALLOWED_SHIFT_5_PERCENT:
        status = "DEVICE_PERFORMANCE_DISTORTION_DETECTED"
        action = "Review_TSV-to-Active_Distance_Design_Rules"
    
    # 4. 종합 응력 상태 등급 및 조치 트리거
    if status == "CRITICAL_COPPER_PROTRUSION_WARNING":
        action = "Stop_Wafer_Bonding_Process_and_Inspect_ILD_Cracks"
    elif status == "EXCESSIVE_STRESS_ZONE_DETECTED":
        action = "Adjust_Copper_Grain_Growth_Annealing_Temperature"
    else:
        status = "TSV_MECHANICAL_INTEGRITY_OPTIMAL"
        action = "Proceed_to_Micro-bump_Assembly_and_Stacking"
        
    return {"status": status, "measured_koz_um": actual_koz_radius, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 왜 TSV 주변의 실리콘 응력 프로파일은 중심에서의 거리($r$)의 제곱에 반비례하는 '라메(Lame) 해' 형상을 가지며, 이것이 '금지 구역(KOZ)' 설정의 수리적 근거가 되는가?
2. **(수리)** 구리의 CTE가 $17 \text{ ppm/}^\circ C$, 실리콘이 $3 \text{ ppm/}^\circ C$, 온도 차이가 $300^\circ C$이다. $10 \mu\text{m}$ 깊이의 TSV에서 구리가 자유롭게 팽창한다면 이론적인 돌출 높이($nm$)는 얼마인가?
3. **(응용)** TSV 주변의 응력을 완화하기 위해 사용되는 'Annular Trench(고리 모양 도랑)' 구조가 실리콘 격자의 응력 전달을 차단하는 수리적 메커니즘을 설명하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 23_semiconductor-materials-and-advanced-packaging-intelligence-hub : 반도체 소재 및 패키징 통합 관리 상위 지능 허브
- Entity through-silicon-via-tsv-electroplating-and-void-detection : 응력 발생의 원인인 TSV 도금 및 구조 엔티티 연계
- Data wafer-flatness-and-surface-roughness-metrology-log-v2026 : 응력에 의한 웨이퍼 변형(Warp) 데이터 연계
- [SOP] tsv-stress-measurement-via-raman-spectroscopy-and-fea-correlation : TSV 응력 측정 및 유한 요소 해석 상관관계 검증 표준 절차

*Created by Flash (The Architect of Stress Maps & HDS Gold V6.3.7)*