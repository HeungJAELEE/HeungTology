# HeungTology

제조·반도체·배터리 분야의 Markdown 지식을 **변경분만 증분 색인**하고, 자연어 질문과 관련된 **원문 후보 파일을 검색·재정렬**하는 로컬 RAG 검색 프로토타입입니다.

현재 구현은 답변을 자동 생성하는 사내 챗봇이 아니라 다음 작업에 집중합니다.

```text
Markdown·YAML 원문
→ 변경 파일 감지
→ Metadata·관계정보 파싱
→ BGE-M3 Embedding
→ ChromaDB 증분 Upsert
→ 후보 검색
→ BGE Reranker
→ 원문 후보 순위·무결성 상태 출력
```

## 해결하려는 문제

제조 현장의 공정·설비·품질 지식은 파일마다 용어, 폴더, 링크와 작성 형식이 달라 같은 문제를 다시 조사할 때 과거 원문을 찾는 데 시간이 듭니다.

HeungTology는 기존 문서를 대규모 시스템으로 이관하기 전에 다음과 같은 작은 시작점을 제공합니다.

- 기존 Markdown 문서를 지식 Source로 유지
- YAML Frontmatter로 Domain·문서유형·상위관계·신뢰도 구조화
- 신규·수정 파일만 다시 색인해 전체 재처리 최소화
- 자연어 질문으로 관련 원문 후보 탐색
- Reranking으로 후보 우선순위 재정렬
- 최종 사실판단과 공개판정은 사용자가 원문에서 수행

## 현재 구현 구조

### 1. Knowledge Source

지식 원문은 `02_Knowledge` 아래 Markdown 파일로 관리합니다. YAML Frontmatter에서 다음 항목을 읽습니다.

- Domain
- Object Type
- Tier
- `is_instance_of`
- Expected Queries
- SPO 관계 Metadata
- 문서 일자와 정적 신뢰도

현재 관계정보는 별도 Graph DB를 순회하는 구조가 아니라, 검색 문맥에 포함해 Vector Retrieval과 Reranking에 활용합니다.

### 2. Incremental Sync

`rag_cli_v2.py --sync` 실행 시 다음 순서로 동작합니다.

1. 대상 폴더의 Markdown 파일 탐색
2. 제외 폴더 필터링
3. 파일 수정시각과 Checkpoint 비교
4. 신규·수정 파일만 파싱
5. ChromaDB에 문서 단위 Upsert
6. 동기화 Checkpoint 갱신

현재 구현은 신규·수정 파일의 증분 Upsert를 지원합니다. 삭제된 원문과 Index의 자동 정합화는 다음 Engineering Gate입니다.

### 3. Local Retrieval Stack

| 구분 | 현재 구현 |
|---|---|
| Vector DB | ChromaDB Persistent Client |
| Embedding | `BAAI/bge-m3` |
| Reranker | `BAAI/bge-reranker-v2-m3` |
| Runtime | Windows 로컬 환경·CUDA |
| Interface | Python CLI |
| Output | 후보 파일명·상위관계·재정렬 점수·무결성 상태 |

Embedding과 Reranker는 로컬 모델을 사용합니다. 현재 Query 경로는 Google·Gemini 등 외부 LLM API를 호출하지 않습니다.

### 4. Retrieval and Reranking

질문 입력 후 다음 과정을 수행합니다.

1. Tier 0 후보와 일반 후보 검색
2. 동일 파일경로 중복 제거
3. Query–Document Pair Reranking
4. 문서일자 기반 동적 신뢰도 반영
5. 본문 SHA-256과 저장된 Evidence Hash 비교
6. 최종 후보 순위 출력

Hash가 불일치하면 해당 후보의 Score를 낮추고 무결성 경고를 표시합니다. Hash가 없는 문서는 기존 신뢰도 기준으로 처리합니다.

## 실행

### 환경

현재 코드는 CUDA 사용을 전제로 합니다.

- Python
- CUDA 대응 PyTorch
- ChromaDB
- Sentence Transformers
- FlagEmbedding
- python-frontmatter
- 로컬에 준비된 BGE-M3·BGE Reranker Model

### 전체 또는 변경분 동기화

```powershell
python rag_cli_v2.py --sync
```

### 자연어 검색

```powershell
python rag_cli_v2.py "2170 저항용접 미접합과 Formation IR의 관계"
```

CLI는 관련 원문 후보를 순위로 보여줍니다. 최종 답변 생성, 인용문 조립과 권한판정은 현재 실행범위에 포함되지 않습니다.

## 전통 제조기업 적용 관점

이 프로젝트의 실용성은 고가의 Enterprise Platform을 즉시 도입했다는 데 있지 않습니다. 기존 파일을 유지하면서 작은 범위부터 검색 가능하게 만들 수 있다는 점에 있습니다.

- 기존 Markdown·문서 폴더 재사용
- 변경분 중심의 증분 색인
- 원문 후보를 먼저 보여주는 검토형 검색
- 제조 Domain·문서유형·관계 Metadata 보존
- 향후 부서별 권한·Web UI·외부 API Adapter로 확장 가능한 분리구조

현재 로컬 CUDA 구조는 외부 API 사용료가 없지만 GPU 환경을 요구합니다. 표준 사무용 PC와 외부 API를 사용하는 경량 배포형은 현재 구현이 아니라 후속 Architecture Option입니다.

## 다음 Engineering Gate

- CPU Fallback과 표준 PC Benchmark
- 외부 Embedding·LLM API Adapter 및 비용정책
- 삭제·이동 파일과 Index 정합화
- 문서 Chunking·원문 위치 표시
- 대표 Query·정답문서 Ground Truth 기반 Retrieval 평가
- Web UI·사용자 인증·부서별 권한
- 생성답변·Citation·원문 Readback
- Secret·감사로그·장애복구와 운영배포

## 현재 완료범위

- Markdown·YAML Source 구조
- 신규·수정 파일 증분 동기화
- ChromaDB 문서 Index
- BGE-M3 후보검색
- BGE Reranker 재정렬
- 신뢰도·Hash 기반 후보 Score 보정
- CLI 검색결과 출력

HeungTology는 현재 **로컬 제조지식 검색 프로토타입**입니다. 운영형 사내 LLM Wiki는 위 Engineering Gate를 통과한 다음 단계입니다.
