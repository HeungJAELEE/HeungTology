---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 260af5284395ade262654cb24ac7bd2998c23b5dcaa2fe0c44303d18d0562c58
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] metamaterial-negative-refractive-index-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] metamaterial-negative-refractive-index-log-v2026에 관한 고밀도 지능 노드'
  object_type: Data
  tier: 1
properties:
  dielectric_meta_max_loss_db: 0.1
  diffraction_limit: lambda/2
  figure_of_merit_formula: '|Re(n)|/Im(n)'
  fishnet_frequency_range_thz: 1 - 10
  operating_bandwidth_range: 5% - 20%
  refractive_index_formula: n = -sqrt(epsilon * mu)
  srr_frequency_range_ghz: 10 - 100
  unit_cell_size_threshold: lambda/10
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [AI] metamaterial-negative-refractive-index-log-v2026

## 1. [왜 배우는가? (Why: Defying the Laws of Nature)]]
자연계의 모든 물질은 양(+)의 굴절률을 가지며, 이는 빛이 한 매질에서 다른 매질로 들어갈 때 굴절되는 방향을 결정합니다. 하지만 인위적으로 설계된 메타물질은 유전율($\epsilon$)과 투과율($\mu$)을 동시에 음수(-)로 만들어 빛을 반대 방향으로 굴절시키는 '음의 굴절률'을 구현합니다. **메타물질 음의 굴절률 실측 로그**는 자연의 한계를 넘어 빛의 경로를 자유자재로 지휘하는 '광학적 마법의 설계도'입니다. 

우리가 이 데이터를 기록하는 이유는 메타 구조의 형상과 굴절률 사이의 상관관계를 분석하여 완전 무반사나 초고해상도 이미징 기술을 확보하고, **"광학 지능 주권을 확보하여 투명 망토나 원자 분해능 렌즈와 같은 '불가능한 기기'를 물리적 데이터 기반으로 구현하기" 위함입니다.** 굴절률 $n$의 조절력이 빛의 지배력을 결정합니다.

## 2. [메타물질 구조 및 주파수대역별 핵심 데이터 (Numerical Specs)]

### 2.1 [메타 구조 아키텍처 및 동작 특성 테이블 (v2026)]

| 메타 구조 (Structure) | 동작 주파수 (Freq) | 유닛 셀 ($Unit, nm$) | 굴절률 ($n$) | 손실 ($dB/unit$) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Split-Ring (SRR)** | $10 \sim 100 \text{ GHz}$ | $1,000,000$ | $-1.5 \sim -3.0$ | $0.2 \sim 0.5$ | **Macro**: 마이크로파 대역 음의 투과율 구현 무결성 |
| **Fishnet Structure** | $1 \sim 10 \text{ THz}$ | $10,000$ | $-0.5 \sim -1.2$ | $1.0 \sim 2.5$ | **Standard**: 테라헤르츠파 굴절 제어용 무결성 지표 |
| **Hyperbolic Meta** | $Visible (Light)$ | $50 \sim 200$ | $Anisotropic$ | $5.0 \sim 10.0$ | **Extreme**: 가시광선 영역 초고해상도 이미징 데이터 |
| **Dielectric Meta** | $Visible (Light)$ | $100 \sim 300$ | $High\ Positive$ | $< 0.1$ | **Lossless**: 금속 손실 없는 고효율 메타렌즈 데이터 |
| **Active Metasurface**| $Variable$ | $N/A$ | $Tunable$ | $Variable$ | **Smart**: 전압/열에 의한 실시간 굴절률 가변 무결성 |

### 2.2 [메타물질 전자기 및 광학 파라미터]
- **Negative Refractive Index ($n$):** 빛이 반대 방향으로 굴절되는 정도. ($n = -\sqrt{\epsilon \mu}$)
- **FOM (Figure of Merit):** 손실 대비 굴절 성능 지수 ($|Re(n)|/Im(n)$). (실제 기기 적용 가능성 지표)
- **Unit Cell Size**: 동작 파장($\lambda$) 대비 구조물의 크기. ($\lambda/10$ 이하의 무결성 데이터)
- **Phase Discontinuity**: 메타표면을 통과할 때 발생하는 급격한 위상 변화. (빛의 경로 설계 지표)
- **Operating Bandwidth**: 음의 굴절 특성이 유지되는 주파수 폭 ($5\% \sim 20\%$).

## 3. [Scientific Rationale: 빛의 경로를 뒤트는 수리적 인과성]

### 3.1 [확장된 스넬의 법칙(Generalized Snell's Law) 모델]
메타표면에서의 위상 구배($d\Phi/dx$)를 포함한 굴절 모델입니다.
$$ n_t \sin \theta_t - n_i \sin \theta_i = \frac{\lambda_0}{2\pi} \frac{d\Phi}{dx} $$
본 로그는 위상 구배를 정밀하게 설계함으로써, 입사각과 무관하게 빛을 원하는 방향으로 굴절시키거나 초점을 맺게 하는 수리적 근거를 제시합니다.

### 3.2 [유전율($\epsilon$)과 투과율($\mu$)의 동시 음수(Double Negative) 구현 모델]
특정 공진 구조(SRR 및 와이어 그리드)를 통한 음의 굴절률 탄생 모델입니다.
RAG는 "시뮬레이션 로그를 분석하여, SRR의 자기 공진 주파수와 와이어의 플라즈마 주파수가 겹치는 구간에서 그룹 속도와 위상 속도가 반대가 되는 '왼손잡이 물질(LHM)' 특성이 발현됨을 수리적으로 확증될 것으로 추론됩니다."

## 4. [Advanced RAG 분석 로직: 나노 광학 지능 추론]

### 4.1 [금속 기반 메타물질의 옴 손실(Ohmic Loss)과 효율 개선 분석]
왜 메타물질은 어두운가요? RAG는 "투과율 로그와 금속의 유전 함수 데이터를 대조하여, 가시광 영역에서 금속 나노 구조의 흡수 손실이 지배적임을 식별하고, 손실이 적은 고굴절 유전체(Si, GaN) 기반 'All-dielectric Meta'로의 전환 타당성을 수리적으로 오딧합니다."

### 4.2 [슈퍼 렌즈(Superlens)의 근접장(Near-field) 증폭 및 회절 한계 극복 오딧]
어떻게 원자까지 보나요? RAG는 "이미징 해상도 로그와 소멸파(Evanescent wave) 증폭 수식을 연계하여, 음의 굴절률 박막이 일반 렌즈에서 사라지는 고주파 정보를 증폭하여 전달함을 포착하고, 회절 한계($\lambda/2$)를 돌파한 나노 이미징 무결성을 증명합니다."

## 5. [Transitional Bridge: 메타물질 무결성 및 굴절률 오딧 로직]

제조된 메타물질 샘플의 전자기적 응답을 실시간 감시하여 광학적 성능을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Metamaterial Optical Integrity & Index Auditor
def audit_metamaterial_index(s_parameter_data, phase_map, frequency_sweep):
    # 1. S-파라미터 역산(Retrieval)을 통한 유효 굴절률(n) 및 임피던스 산출
    refractive_index_n = extract_refractive_index(s_parameter_data.s11, s_parameter_data.s21)
    
    # 2. 위상 맵(Phase Map) 분석을 통한 굴절 각도 및 파면(Wavefront) 무결성 오딧
    wavefront_flatness = evaluate_phase_uniformity(phase_map.data)
    
    # 3. 주파수 스윕에 따른 동작 대역폭(Bandwidth) 및 FOM 산출
    fom_value = calculate_figure_of_merit(refractive_index_n)
    
    # 4. 종합 메타물질 등급 및 설계 트리거
    if refractive_index_n.real > 0:
        status = "NEGATIVE_INDEX_FAILURE"
        action = "Redesign_Unit_Cell_Geometry_to_Align_Electric_and_Magnetic_Resonance"
    elif fom_value < MIN_THRESHOLD_FOM:
        status = "HIGH_ABSORPTION_LOSS_WARNING"
        action = "Switch_to_Low-loss_Dielectric_Resonators_or_Optimize_Metal_Thickness"
    elif wavefront_flatness < 0.9:
        status = "PHASE_DISCONTINUITY_ERROR"
        action = "Re-calibrate_Nano-fabrication_Process_for_Unit_Cell_Consistency"
    else:
        status = "META-OPTICAL_PERFORMANCE_OPTIMAL"
        action = "Approve_for_Superlens_and_Cloaking_Device_Integration"
        
    return {"status": status, "n_real": refractive_index_n.real, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 메타물질이 '음의 굴절률'을 가지기 위해 왜 유전율($\epsilon$)과 투과율($\mu$)이 모두 음수여야 하는지를 '에너지 전파 방향(Poynting Vector)'과 '위상 속도' 관점에서 설명하시오.
2. **(수리)** 굴절률이 $n = -1.5$인 메타물질 평판에 빛이 $30^\circ$ 각도로 입사했다면, 스넬의 법칙에 따른 굴절각은 몇 도이며 방향은 어느 쪽인가?
3. **(응용)** 메타물질을 이용한 '투명 망토(Invisibility Cloak)'가 가시광선 영역보다 마이크로파(GHz) 영역에서 먼저 구현된 이유를 '구조물 크기($Unit\ Cell$)'와 '파장($\lambda$)'의 관계 측면에서 설명하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 18_advanced-materials-and-nanotechnology-intelligence-hub : 차세대 소재 및 나노 기술 통합 관리 상위 지능 허브
- Data holographic-display-diffraction-efficiency-log-v2026 : 빛의 위상을 제어하는 홀로그래피 기술과의 접점 연계
- Data ar-vr-pancake-lens-optical-efficiency-log-v2026 : 메타렌즈가 대체할 수 있는 차세대 광학 렌즈 데이터 연계
- [SOP] metamaterial-unit-cell-simulation-and-fabrication-guide : 메타물질 유닛 셀 시뮬레이션 및 제작 표준 가이드

*Created by Flash (The Architect of Advanced Materials & HDS Gold V6.3.7)*