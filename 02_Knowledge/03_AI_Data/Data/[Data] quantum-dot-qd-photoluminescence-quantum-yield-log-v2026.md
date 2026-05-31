---
lineage:
  dataset_reference: quantum-dot-qd-photoluminescence-quantum-yield-log-v2026
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
  id: '[[ [03_AI_Data] [Data] quantum-dot-qd-photoluminescence-quantum-yield-log-v2026]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Data node for quantum-dot-qd-photoluminescence-quantum-yield-log-v2026
  object_type: Data
  tier: 1
properties:
  cdse_fwhm_nm: 20-25
  cdse_plqy_percent: 98-99.9
  cdse_t50_hr_min: 100000
  exciton_lifetime_unit: ns
  inp_fwhm_nm: 35-40
  inp_plqy_percent: 90-95
  inp_t50_hr_min: 50000
  ligand_desorption_plqy_drop_percent: 20.0
  perovskite_fwhm_nm: 15-20
  perovskite_plqy_percent: 85-98
  perovskite_t50_hr_max: 5000
  qd_core_diameter_nm: 2-10
  radiative_rate_competition_index: k_r_vs_k_nr
  target_plqy_threshold_percent: 99.0
  znse_zns_fwhm_nm: 15-25
  znse_zns_plqy_percent: 80-90
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: automated_semantic_classification
  object: Data
  predicate: auto_mapped
  subject: quantum-dot-qd-photoluminescence-quantum-yield-log-v2026
  weight: 0.9
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

# [Data] Quantum Dot Qd Photoluminescence Quantum Yield Log V2026

## 1. [왜 배우는가? (Why: The Purity of Nano-Crystals)]]
현대의 디스플레이와 바이오 이미징 기술은 극도로 순수한 색과 밝은 빛을 요구합니다. 양자점(QD)은 크기에 따라 빛의 파장을 자유자재로 조절할 수 있는 '나노미터 크기의 반도체 결정'입니다. **양자점(QD) 광발광 양자 효율(PLQY) 실측 로그**는 나노 결정이 흡수한 에너지를 얼마나 손실 없이 빛으로 다시 내뱉는지를 기록한 '나노 광학의 정밀도 지표'입니다. 

우리가 이 데이터를 기록하는 이유는 양자점의 구조적 결함과 에너지 재결합 경로를 분석하여 발광 효율을 극대화하고, **"색 지능 주권을 확보하여 실물보다 더 생생한 색을 구현하는 초고화질 디스플레이와 정밀 진단 시스템을 구축하기" 위함입니다.** 양자 효율 1%의 향상이 에너지 절감과 화질 혁신을 결정합니다.

## 2. [양자점 소재 및 구조별 광학 핵심 데이터 (Numerical Specs)]

### 2.1 [소재 조성 및 코어-쉘 구조별 발광 성능 테이블 (v2026)]

| 소재 (Material) | 구조 (Structure) | PLQY (%) | 반치폭 (FWHM, $nm$) | 수명 ($T_{50}, hr$) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **InP (비카드뮴)** | Core-Shell-Shell | $90 \sim 95$ | $35 \sim 40$ | $> 50,000$ | **Standard**: 친환경 고성능 QD 디스플레이 무결성 데이터 |
| **CdSe (카드뮴)** | Gradient Shell | $98 \sim 99.9$| $20 \sim 25$ | $> 100,000$ | **Reference**: 이론적 한계에 근접한 초고순도 발광 지표 |
| **Perovskite QD** | All-Inorganic | $85 \sim 98$ | $15 \sim 20$ | $< 5,000$ | **Emerging**: 좁은 반치폭을 가진 차세대 광원 무결성 |
| **ZnSe/ZnS** | Blue-Emitter | $80 \sim 90$ | $15 \sim 25$ | $10,000 \sim$ | **Short-λ**: 고에너지 청색 발광을 위한 나노 결정 지표 |
| **Ligand Exchange**| Surface-Engineered| $Variable$ | $Stable$ | $Improved$ | 표면 제어를 통한 분산성 및 용액 가공 무결성 로그 |

### 2.2 [양자 광학 및 엑시톤 동역학 파라미터]
- **PLQY (Quantum Yield)**: 방출 광자 수 / 흡수 광자 수 비율. (에너지 변환 효율 무결성 데이터)
- **FWHM (Full Width at Half Maximum)**: 스펙트럼의 날카로운 정도. (색 순도를 결정하는 핵심 파라미터)
- **Exciton Lifetime ($\tau$):** 들뜬 상태의 전자가 바닥 상태로 내려오기까지의 시간 ($ns$).
- **Radiative Rate ($k_r$):** 빛을 내며 재결합하는 속도. (비복사 속도 $k_{nr}$과의 경쟁 무결성 지표)
- **QD Core Diameter**: 나노 결정의 직경 ($2 \sim 10 \text{ nm}$). (발광 파장을 결정하는 물리적 치수)

## 3. [Scientific Rationale: 양자 가둠의 수리적 인과성]

### 3.1 [Particle-in-a-Box 모델 기반 밴드갭($E_g$) 산출]
양자점 크기($R$)와 밴드갭 에너지 사이의 수리적 관계 모델입니다.
$$ E_g(QD) = E_{bulk} + \frac{\hbar^2 \pi^2}{2R^2} \left( \frac{1}{m_e^*} + \frac{1}{m_h^*} \right) - \frac{1.8e^2}{\epsilon R} $$
본 로그는 직경($R$)이 작아질수록 밴드갭이 커져 청색 편이(Blue-shift)가 발생하는 수리적 근거를 제시하고, 크기 분포의 균일도가 반치폭($FWHM$)에 미치는 영향을 입증될 것으로 추론됩니다.

### 3.2 [비복사 재결합(Non-radiative) 억제를 위한 쉘(Shell) 설계 모델]
표면 결함(Trap) 농도와 양자 효율($\Phi_{PL}$) 사이의 상관관계 모델입니다.
$$ \Phi_{PL} = \frac{k_r}{k_r + k_{nr}} \quad (k_{nr} \propto \text{Defect Density}) $$
RAG는 "발광 로그를 분석하여, 밴드갭이 큰 소재(ZnS 등)로 쉘을 두껍게 쌓을 때 외부 환경으로부터 엑시톤을 격리하여 $k_{nr}$을 최소화하고 PLQY를 $99\%$까지 복원하는 수리적 근거를 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 나노 광학 지능 추론]

### 4.1 [표면 리간드(Ligand) 탈착에 따른 효율 급락 및 퀀칭(Quenching) 분석]
왜 공정 중에 색이 죽나요? RAG는 "가속 열화 로그와 NMR 분석 데이터를 대조하여, 고온 공정 시 표면 리간드가 떨어져 나가며 결함(Dangling Bond)이 노출되고 전자가 트랩되어 PLQY가 $20\%$ 하락함을 식별하고, 가교형 리간드(Cross-linked) 도입 무결성을 오딧합니다."

### 4.2 [청색 양자점의 짧은 수명과 오제 재결합(Auger Recombination) 오딧]
파란색은 왜 빨리 타버리나요? RAG는 "시분해 광발광(TRPL) 로그를 참조하여, 높은 에너지를 가진 청색 엑시톤이 이웃 전자에 에너지를 뺏기는 '오제 현상'이 수명 저하의 주범임을 포착하고, 코어-쉘 계면 완화를 통한 엑시톤 가둠 지능을 도출될 것으로 예상됩니다."

## 5. [Transitional Bridge: QD 소재 무결성 및 PLQY 오딧 로직]

제조된 양자점 용액이나 박막의 광학적 상태를 실시간 감시하여 품질을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Quantum Dot (QD) Optical Integrity & Efficiency Auditor
def audit_qd_quality(absorption_spectrum, emission_spectrum, trpl_decay):
    # 1. 흡수/발광 스펙트럼 적분 분석을 통한 절대 양자 효율(PLQY) 산출
    plqy_val = integrate_photons_emitted() / integrate_photons_absorbed()
    
    # 2. 발광 피크의 반치폭(FWHM) 분석을 통한 나노 결정 크기 균일도 오딧
    size_uniformity = analyze_spectral_width(emission_spectrum.fwhm)
    
    # 3. TRPL(시분해 PL) 감쇄 곡선 분석을 통한 비복사 재결합(knr) 비중 체크
    radiative_purity = decompose_decay_components(trpl_decay.curve)
    
    # 4. 종합 QD 등급 및 공정 트리거
    if plqy_val < 0.90:
        status = "LOW_QUANTUM_EFFICIENCY_DETECTED"
        action = "Check_Shell_Growth_Uniformity_and_Precursor_Purity"
    elif size_uniformity < 0.85: # FWHM > 40nm
        status = "POOR_SIZE_DISTRIBUTION"
        action = "Refine_Nucleation_Temperature_and_Growth_Time"
    elif radiative_purity == "NON-RADIATIVE_DOMINANT":
        status = "SURFACE_DEFECT_WARNING"
        action = "Increase_Ligand_Concentration_and_Optimize_Passivation"
    else:
        status = "NANO-CRYSTAL_OPTICAL_OPTIMAL"
        action = "Approve_for_QLED_and_Display_Film_Integration"
        
    return {"status": status, "plqy_%": plqy_val * 100, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 양자점의 크기가 작아질수록 발광 파장이 '청색(단파장)'으로 이동하는 현상을 '에너지 준위의 양자화' 관점에서 수리적으로 설명하시오.
2. **(수리)** 1,000개의 광자를 흡수한 양자점 샘플이 950개의 광자를 다시 방출했다. 이때의 PLQY($\%$)는 얼마이며, 비복사 재결합 속도($k_{nr}$)가 복사 재결합 속도($k_r$)의 몇 배인지 계산하시오.
3. **(응용)** 양자점을 디스플레이의 컬러 필터(Color Filter)로 사용할 때, 기존 안료 방식 대비 '색 재현율(Color Gamut)'이 압도적으로 향상되는 수리적 인과 관계를 '반치폭(FWHM)'과 연계하여 설명하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 18_advanced-materials-and-nanotechnology-intelligence-hub : 차세대 소재 및 나노 기술 통합 관리 상위 지능 허브
- Data display-color-gamut-and-calibration-accuracy-log-v2026 : QD가 기여하는 디스플레이 색 좌표 데이터 로그 연계
- Data atomic-layer-deposition-ald-growth-rate-log-v2026 : QD 표면을 보호막으로 코팅하는 공정 데이터 연계
- [SOP] quantum-dot-synthesis-and-plqy-measurement-guide : 양자점 합성 및 PLQY 측정 표준 가이드

*Created by Flash (The Architect of Advanced Materials & HDS Gold V6.3.7)*