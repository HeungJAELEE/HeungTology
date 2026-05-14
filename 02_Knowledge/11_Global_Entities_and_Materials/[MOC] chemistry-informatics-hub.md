---
Basic:
  id: "MOC-CHEM-INFO-HUB-v6.4"
  date: 2026-05-14
  domain: 11_Global_Entities_and_Materials
Dynamic:
  status: Ratified (V6.4 Active)
Object:
  uuid: chemistry-informatics-hub-moc
  type: MOC
Semantic:
  is_part_of: '["[[[MOC] 00_INDEX]]"]'
  tags: '["#MOC", "#Chemistry", "#Informatics", "#Dataset", "#AIP"]'
Trust Metrics:
  T_init: 1.0
  T_static: 1.0
  note: "화학 정보학 및 외부 데이터셋 통합 관제 허브"
citation_count: 0
current_trust_level: 1.0
provenance: '["Project Antigravity V6.8 External Data Ingestion"]'
related_to: '["[[01-molecular-modeling-fundamentals]]", "[[01-pharmacology-and-drug-discovery-foundations]]"]'
trust_base: 1.0
trust_lambda: 0.0
type: MOC
---

# [MOC] Chemistry Informatics Hub (화학 정보학 통합 허브)

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
