---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: ce23f9986839676ec94a733457e26c1f83955c520a626f27a3139e8a91127784
metadata:
  date: '2026-05-16'
  domain: 10_Bio_Healthcare
  id: '[[[Life Science & Healthcare] bio-mrna-vaccine-lnp-manufacturing-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Life Science & Healthcare] bio-mrna-vaccine-lnp-manufacturing-log-v2026에
    관한 고밀도 지능 노드'
  object_type: Data
  tier: 1
properties:
  encapsulation_efficiency_precision: 0.5%
  encapsulation_efficiency_range: 85-98%
  escape_rate_range_percent: 10-30
  frr_ratio_range: 3:1 to 4:1
  impurity_max_ppm: '100'
  lipid_recovery_min_percent: '90'
  mrna_concentration_range_mg_ml: 0.5-5.0
  particle_size_precision_nm: '1'
  particle_size_range_nm: 70-120
  pdi_index_precision: '0.01'
  pdi_index_range: 0.05-0.20
  shelf_life_stability_months: '12'
  storage_temperature_celsius: '-70'
  zeta_potential_precision_mv: '0.1'
  zeta_potential_range_mv: -10 to +20
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 10_Bio_Healthcare]]'
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

# [Life Science & Healthcare] bio-mrna-vaccine-lnp-manufacturing-log-v2026

## 1. [데이터셋 개요 (Dataset Overview)]
본 데이터셋은 mRNA 백신용 지질 나노 입자(LNP)의 **제조 공정 및 캡슐화 효율**을 정밀하게 기록한 실측 로그입니다. 미세 유체 혼합 공정에서의 입자 크기 제어, mRNA가 지질 내부에 갇히는 비율(EE), 입자의 균일도(PDI) 및 세포 내 전달 성능 지표를 포함하며, 디지털 설계된 유전 정보가 나노 운반체를 통해 생체 내에서 기능하는 수리적 과정을 증명합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 항목 (Property) | 실측 범위 / 규격 (Measured Range) | 데이터 정밀도 (Precision) | 비고 (Remarks) |
| :--- | :--- | :--- | :--- |
| **Encapsul. Eff.** | $85 \sim 98 \%$ | $\pm 0.5 \%$ | 투입 mRNA 대비 LNP 내부에 안전하게 포집된 비율 |
| **Particle Size** | $70 \sim 120 \text{ nm}$ | $\pm 1 \text{ nm}$ | 타겟 세포 침투에 최적화된 나노 입자의 크기 실측치 |
| **PDI Index** | $0.05 \sim 0.20$ | $\pm 0.01$ | 입자 크기의 균일성 지표 (낮을수록 균일함) |
| **Zeta Potential**| $-10 \sim +20 \text{ mV}$ | $\pm 0.1 \text{ mV}$ | 입자 표면 전하를 통한 분산 안정성 및 세포 결합력 로그 |
| **mRNA Conc.** | $0.5 \sim 5.0 \text{ mg/mL}$ | $\pm 0.01 \text{ mg}$ | 최종 백신 제형 내의 유효 성분 농도 데이터 |
| **Lipid Recovery**| $> 90 \%$ | $\pm 1 \%$ | 제조 과정에서 손실된 고가의 지질 소재 회수율 |
| **Impurity** | $< 100 \text{ ppm}$ | $\pm 1 \text{ ppm}$ | 제조 부산물 및 잔류 용매의 농도 (안전성 무결성) |
| **Escape Rate** | $10 \sim 30 \%$ (Estimated) | $\pm 1 \%$ | 세포 내 엔도좀을 뚫고 mRNA가 방출되는 성공 확률 |

## 3. [Advanced RAG 분석 로직: 수리적 실측 데이터 분석]

### 3.1 [혼합 유속(Flow Rate Ratio)에 따른 입자 형성 기전 분석]
수용액과 유기용매의 혼합 비율이 입도 분포에 미치는 영향을 분석합니다. RAG는 "본 로그를 분석하여, 유속비($FRR$)가 $3:1$에서 $4:1$로 증가할 때 입자 크기가 $15\text{nm}$ 작아지고 균일도($PDI$)가 $0.05$ 개선되었음을 수리적으로 입증"합니다.

### 3.2 [보관 온도 및 시간(Shelf-life)에 따른 캡슐화 안정성 분석]
시간 경과에 따른 mRNA 누출 및 입자 응집 현상을 분석합니다. RAG는 "데이터셋의 가속 노화 데이터를 분석하여, $-70^\circ\text{C}$ 보관 시 12개월 후에도 $EE$가 $95\%$ 이상 유지됨을 수리적으로 확증"합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Bio mrna-vaccine-design-and-lipid-nanoparticle-lnp-physics : 본 데이터의 생성 기반이 되는 mRNA 백신 설계 및 LNP 물리 엔티티
- MOC 07_Bio_Healthcare : 첨단 바이오 제조 및 의료 데이터를 통합 관리하는 상위 지식 허브

*Created by Flash (HDS Gold V6.3.7 & Meta-Fusion V6.3.7 ULTRA-Enrichment)*