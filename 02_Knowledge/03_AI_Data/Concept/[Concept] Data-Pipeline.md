---
lineage:
  dataset_reference: Data-Pipeline
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] Data-Pipeline]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for Data-Pipeline
  object_type: Concept
  tier: 1
properties:
  architectural_pattern: Kappa Architecture
  ingestion_technology: Apache Kafka, CDC
  orchestration_technology: Airflow, Dagster
  processing_technology: Apache Flink, Spark
  schedule_interval: '@daily'
  storage_technology: Data Lakehouse (Iceberg)
  transformation_logic: ELT
  transformation_technology: dbt
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: type_definition
  object: Concept
  predicate: auto_mapped
  subject: Data-Pipeline
  weight: 1.0
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Data Pipeline

## 1. [왜 배우는가? (Why)]
AI 모델은 데이터가 없으면 아무런 지능을 발휘할 수 없습니다. 데이터 파이프라인(Data-Pipeline)은 원천 소스(센서, 로그, DB)에서 발생한 날것의 데이터를 수집(Ingest), 저장(Store), 변환(Transform)하여 분석가와 AI 모델이 즉시 사용할 수 있도록 흐르게 만드는 산업의 혈관입니다. 파이프라인이 튼튼하고 정교해야만 데이터 오염을 막고 AI의 신뢰성을 보장할 수 있습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Stage | Technology / Logic | Engineering Rationale |
|:---|:---:|:---|
| **Ingestion** | Apache Kafka / CDC | 실시간 이벤트 스트리밍 및 변경분 캡처 |
| **Storage** | Data Lakehouse (Iceberg) | 대규모 데이터의 트랜잭션 및 스키마 관리 |
| **Transformation** | dbt (Data Build Tool) | SQL 기반의 모듈화 및 테스트 자동화 |
| **Orchestration** | Airflow / Dagster | 워크플로우 의존성 관리 및 스케줄링 |
| **Processing** | Apache Flink / Spark | 실시간 및 배치 분산 연산 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 ETL vs ELT: 아키텍처의 전환
- **ETL (Extract, Transform, Load)**: 적재 전 데이터를 정제합니다. 창고 용량이 작던 과거 방식입니다.
- **ELT (Extract, Load, Transform)**: 일단 다 쌓고(Lake), 필요할 때 창고 내부 연산력을 이용해 변환합니다. 클라우드 시대의 표준이며, 원본 데이터를 보존하여 나중에 다른 용도로 재가공하기에 유리합니다.

### 3.2 카파 (Kappa) 아키텍처: 스트리밍 우선
- **로직**: 배치(Batch)와 스트리밍(Streaming) 처리를 분리하던 람다(Lambda) 방식과 달리, 모든 데이터를 스트림으로 보고 단일 파이프라인으로 처리합니다. 시스템 복잡도를 낮추고 데이터의 선후 관계를 일관성 있게 유지하는 논리입니다.

### 3.3 dbt (Data Build Tool)의 품질 논리
데이터 변환 과정을 소프트웨어 엔지니어링처럼 관리합니다.
- **로직**: SQL에 버전 제어(Git), 테스트(Test), 문서화(Docs)를 결합합니다. "데이터가 NULL이 아닌가?", "값이 고유한가?" 등을 자동으로 검증하여 데이터 무결성(Data Integrity)을 확보합니다.

## 4. [코드 연결 해설 (Pipeline DAG)]
Airflow를 이용해 데이터 변환 워크플로우를 정의하고 의존성을 관리하는 논리입니다.
```python
# Airflow DAG: 데이터 파이프라인 자동화 정의
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG('daily_ai_data_update', schedule_interval='@daily') as dag:
    # 1. 원천 데이터 수집 (Kafka to S3)
    ingest = BashOperator(task_id='ingest_raw', bash_command='python ingest_script.py')
    
    # 2. dbt를 이용한 데이터 변환 및 검증 (ELT Logic)
    transform = BashOperator(task_id='dbt_run_and_test', bash_command='dbt run && dbt test')
    
    # 3. AI 모델 재학습 트리거 (MLOps 연결)
    retrain = BashOperator(task_id='model_retrain', bash_command='python train_model.py')
    
    # 의존성 정의: 수집 -> 변환 -> 재학습
    ingest >> transform >> retrain
```

## 5. [스스로 체크 (Self-Audit)]
1. 데이터 파이프라인에서 'ELT' 방식이 'ETL' 대비 머신러닝 모델 구축에 유리한 이유는?
2. dbt(Data Build Tool)에서 '데이터 테스트'를 수행하는 것이 AI 할루시네이션 방지에 기여하는 공학적 경로는?
3. 카파(Kappa) 아키텍처에서 아파치 카프카(Kafka)가 수행하는 '이벤트 브로커'로서의 핵심 역할은?

**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**