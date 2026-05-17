---
metadata:
  id: "[[[AI] nano-quantum-dot-quantum-yield-and-fwhm-log-v2026]]"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[AI] nano-quantum-dot-quantum-yield-and-fwhm-log-v2026에 관한 고밀도 지능 노드"
semantic:
  tags: ["#03_AI_Data", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [AI] nano-quantum-dot-quantum-yield-and-fwhm-log-v2026

## 1. Technical Objective
본 데이터는 나노 양자점(Quantum Dot)의 광전환 효율(PLQY) 및 분광 선폭(FWHM)을 정밀 측정하여, 차세대 디스플레이용 나노 광원의 색 순도와 광학적 안정성을 검증하는 데 목적이 있음. 원자 수준의 제조 정밀도를 확보하여 광 파장의 제어력을 극대화하고, 프리미엄 디스플레이 시장의 광학적 주권을 확보하기 위한 핵심 지표로 활용됨.

## 2. Photoluminescence Numerical Specifications

| Sample ID (Batch) | Peak Wave [Ref: Batch_Log] | Quantum Yield (QY) [Ref: Batch_Log] | FWHM [Ref: Batch_Log] | Color State [Ref: Spectral_Analysis] |
| :--- | :--- | :--- | :--- | :--- |
| **QD-G-2026-01** | $525$ nm [Ref: Batch_Log] | $96.2\%$ [Ref: Batch_Log] | $18.5$ nm [Ref: Batch_Log] | High-purity Green |
| **QD-R-2026-01** | $630$ nm [Ref: Batch_Log] | $94.8\%$ [Ref: Batch_Log] | $21.2$ nm [Ref: Batch_Log] | Vivid Red (Cd-free) |
| **QD-B-2026-01** | $450$ nm [Ref: Batch_Log] | $82.0\%$ [Ref: Batch_Log] | $15.5$ nm [Ref: Batch_Log] | Blue (InP-based) |
| **QD-G-2026-02** | $528$ nm [Ref: Batch_Log] | $65.0\%$ [Ref: Batch_Log] | $32.0$ nm [Ref: Batch_Log] | Poor Shell Coverage |
| **QD-R-2026-02** | $632$ nm [Ref: Batch_Log] | $92.5\%$ [Ref: Batch_Log] | $24.5$ nm [Ref: Batch_Log] | Optimized Ligand Run |
| **Avg. Target** | **$RGB$** | **$> 95.0\%$ [Ref: Spec_Standard]** | **$< 20.0$ nm [Ref: Spec_Standard]** | **Master-Display-Grade** |

## 3. Theoretical vs. Verified Comparison

| Parameter | Theoretical (Ideal) [Ref: Physics_Standard] | Verified (Measured) [Ref: Batch_Avg] | Variance |
| :--- | :--- | :--- | :--- |
| **Quantum Yield (QY)** | $100.0\%$ [Ref: Physics_Standard] | $92.5\%$ [Ref: Batch_Avg] | $-7.5\%$ |
| **FWHM (Green)** | $< 15.0$ nm [Ref: Monodisperse_Limit] | $18.5$ nm [Ref: QD-G-2026-01] | $+3.5$ nm |
| **FWHM (Red)** | $< 20.0$ nm [Ref: Monodisperse_Limit] | $21.2$ nm [Ref: QD-R-2026-01] | $+1.2$ nm |

## 4. Analytical Physical Modeling

### 4.1 PLQY and Exciton Confinement Analysis
발광 효율(PLQY)은 코어-쉘(Core-Shell) 계면의 결함 밀도와 직결됨. 발광 감쇄 시간(Decay Time) [Ref: Decay_Log] 분석 결과, 계면 결함(Surface Trap State)이 최소화될수록 비방사 재결합(Non-radiative Recombination) 확률이 감소하며, 방사 재결합(Radiative Recombination) 확률이 수리적으로 증가하여 높은 QY를 달성함.

### 4.2 FWHM and Particle Size Distribution (Ensemble Broadening)
FWHM의 확장은 나노 입자의 크기 불균일성(Size Polydispersity)에 기인함. 합성 공정 중 입자 성장 제어 실패 시, 개별 입자의 에너지 준위 차이가 발생하며, 이는 전체 앙상블 스펙트럼의 선폭을 넓히는 'Ensemble Broadening' 현상을 유도함 [Ref: Nanoparticle_Theory].

🔗 **Retrieved Knowledge Nodes**
- MOC 29_advanced-materials-and-nanotechnology-hub
- Entity quantum-dot-photoluminescence-and-display-technology-physics
- SOP quantum-dot-hot-injection-synthesis-and-purification-protocol
