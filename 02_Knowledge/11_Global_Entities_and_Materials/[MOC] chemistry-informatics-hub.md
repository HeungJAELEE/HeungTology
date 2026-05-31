---
lineage:
  dataset_reference: global-core-log-v2026
  original_author: Antigravity Vault Core Team
  original_hash: 17e529e2d458671c8cb16e088e292696ca5f733d89986a4507569afb877a8a62
metadata:
  date: '2026-05-14'
  domain: 11_Global_Entities_and_Materials
  id: MOC-CHEM-INFO-HUB-v6.4
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 'High-fidelity engineering node: [MOC] chemistry-informatics-hub.md'
  object_type: Data
  tier: 1
properties:
  biorxiv_corpus: bioRxiv
  coconut_db: COCONUT
  cod_db: COD
  ingestor_script: github_ingestor.py
  moleculenet_benchmark: MoleculeNet
  pubmed_corpus: PubMed
  rdb7_db: RDB7
  tdc_benchmark: TDC
  uspto_db: USPTO
  zinc_db: ZINC
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 11_Global_Entities_and_Materials]]'
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

# chemistry-informatics-hub

## 1. 개요 (Context)
본 문서는 Antigravity 시스템에 이식된 글로벌 화학 데이터셋 및 화학 정보학(Cheminformatics) 리소스를 총괄하는 지휘소입니다. 외부에서 수집된 방대한 화학 지식을 시스템의 공학적 의사결정에 활용할 수 있도록 분류하고 연결합니다.

## 2. 지식 클러스터 (Knowledge Clusters)

### 2.1 문헌 및 텍스트 데이터 (Literature & NLP)
- [[ext_chem_text_datasets]]: PubMed, bioRxiv 등 대규모 학술 코퍼스 및 NLP 벤치마크
- [[ext_chem_literature_v6]] (수동 정제): 고밀도 핵심 문헌 데이터셋

### 2.2 분자 구조 및 라이브러리 (Structures & Libraries)
- [[ext_chem_structures]]: COCONUT, COD, ZINC 등 대규모 화합물 구조 데이터베이스
- [[ext_chem_structures_v6]] (수동 정제): 핵심 구조 데이터셋

### 2.3 활성 및 물성 벤치마크 (Property Benchmarks)
- [[ext_chem_ml_structureproperty_benchmark_datasets]]: MoleculeNet, TDC 등 모델 학습용 표준 데이터셋
- [[ext_chem_molecular_activity_prediction_benchmark_datsets]]: 활성 절벽(Activity Cliff) 등 특화 벤치마크
- [[ext_chem_benchmarks_v6]] (수동 정제): 핵심 물성 벤치마크

### 2.4 약리학 및 임상 데이터 (Pharmacology & Clinical)
- [[ext_chem_pharmacology__adme__metabolism]]: ADME, 대사체 및 임상 약물 정보
- [[ext_chem_target_identification_data]]: 질병 표적 식별 및 유전체 데이터
- [[ext_chem_pharma_v6]] (수동 정제): 핵심 약리학 데이터셋

### 2.5 반응 및 공정 설계 (Reactions & Synthesis)
- [[ext_chem_reactions]]: USPTO, RDB7 등 화학 반응 및 합성 경로 데이터
- [[ext_chem_highthroughput_screening_data]]: 고처리량 스크리닝(HTS) 결과 데이터
- [[ext_chem_reactions_materials_v6]] (수동 정제): 핵심 반응 및 소재 데이터셋

## 3. 실행 엔진 (Execution Engine)
- [[github_ingestor.py]]: GitHub Awesome Chemistry Datasets 자동 수집 및 정제 스크립트

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[MOC] 00_INDEX]
- [[03_External_Data/Chemistry_Datasets/]]