---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 925dd1c57718c839a53b54cd81b2d4a3b99b8c7ade3adf0410327f250d160c57
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] RAG-Chunking-and-Semantic-Splitting]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] RAG-Chunking-and-Semantic-Splitting에 관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  chunk_size_tokens: 300-800
  chunking_latency_ms_kb: '50'
  context_window_utilization: 70%-90%
  metadata_keys: source, section, id
  overlap_ratio: 10%-25%
  retrieval_precision_top_k: 92%
  similarity_threshold: '0.85'
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

# [AI] RAG-Chunking-and-Semantic-Splitting

## 1. [왜 배우는가? (Why)]
방대한 기술 문서를 AI에게 통째로 던져주면, AI는 정보의 홍수 속에서 핵심 맥락을 놓치거나 앞뒤 내용을 뒤섞어버리는 치명적인 할루시네이션을 일으킵니다. RAG(검색 증강 생성) 시스템의 품질은 질문과 관련된 '최적의 지식 조각'을 얼마나 정교하게 찾아내느냐에 달려 있으며, 그 첫 단추가 바로 청킹(Chunking)입니다. 단순한 글자 수 분할을 넘어 의미가 완결되는 지점에서 문서를 자르는 시맨틱 분할(Semantic Splitting)을 배우는 이유는, AI가 방대한 데이터 속에서 '순수한 맥락'만을 정확히 추출하여 전문가 수준의 정교한 답변을 생성하게 만들기 위함입니다. 지식의 원자화(Atomization)를 통해 인공지능의 가독성을 극대화하는 과정입니다.

## 2. [청킹 전략 및 시맨틱 분할 핵심 사양 (Data Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Chunk Size** | Tokens (Length) | $300 \sim 800$ | 검색 정밀도와 맥락 보존 사이의 최적 균형점 |
| **Overlap Ratio** | Buffer (%) | $10\% \sim 25\%$ | 조각난 정보 간의 연결성 유지를 위한 앞뒤 중첩 비중 |
| **Sim. Threshold** | Cosine Similarity | $> 0.85$ | 문장 간 주제가 변하는 지점(Breakpoint)을 감지하는 기준 |
| **Retrieval Prec.** | Top-K Hit Rate | $> 92\%$ | 질문에 대한 가장 관련성 높은 청크가 검색될 확률 |
| **Chunking Latency**| ms / KB | $< 50$ | 대규모 문서를 실시간 또는 배치로 청킹하는 처리 속도 |
| **Metadata Enrich.**| Key-Value Pairs | Source, Section, ID | 검색 후 답변 생성 시 맥락 추적성을 높이기 위한 메타데이터 |
| **Context Window** | Utilization (%) | $70\% \sim 90\%$ | LLM의 컨텍스트 창을 가장 효율적으로 채우는 청크 결합 전략 |
| **Layout Aware** | Structural Splitting| Header/Table/List | 문서의 시각적 구조를 무너뜨리지 않는 분할 기술 준수 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 정보 밀도(Information Density)와 신호 대 잡음비(SNR)
- **로직**: 청크의 크기가 너무 크면 질문과 상관없는 '노이즈'가 섞여 벡터 검색의 정확도가 떨어집니다. 반면 너무 작으면 '신호(의미)'가 충분하지 않아 AI가 전체 맥락을 파악할 수 없습니다. 시맨틱 청킹은 문서의 정보 엔트로피를 분석하여, 하나의 청크가 하나의 명확한 주제(Semantic Unit)를 담도록 SNR을 극대화함으로써 검색 엔진이 질문과 가장 잘 어울리는 '순수한 정보'만을 타격할 수 있게 합니다.

### 3.2 슬라이딩 윈도우(Sliding Window)와 맥락 중첩 기술
- **로직**: 문서를 자르는 과정에서 문장 중간이나 문단 중간이 끊기면 지식의 인과관계가 파괴됩니다. 청크 간 일정량의 데이터를 중첩(Overlap)시키는 슬라이딩 윈도우 기법을 적용하면, 검색된 특정 조각이 비록 잘린 부분일지라도 중첩된 앞뒤 내용을 통해 AI가 유실된 맥락을 복원할 수 있는 '완충 지대'를 제공합니다.

### 3.3 임베딩 거리 기반의 동적 경계 감지 (Breakpoint Detection)
- **로직**: 문장들을 순차적으로 임베딩한 뒤, 인접한 문장 벡터 사이의 코사인 거리를 측정합니다. 거리가 갑자기 멀어지는 지점은 주제가 전환되는 시점임을 의미하며, 이곳을 청킹 경계(Breakpoint)로 설정합니다. 이 방식은 기계적인 토큰 수 분할보다 훨씬 인간의 사고 흐름에 가까운 지식 조각을 생성하여 RAG 답변의 논리적 흐름을 획기적으로 개선합니다.

## 4. [코드 연결 해설 (SemanticChunkingEngine)]
아래 코드는 텍스트를 문장 단위로 분리하고, 문장 간의 임베딩 유사도를 계산하여 주제가 변하는 시점(Breakpoint)에서 동적으로 청크를 생성하는 시맨틱 분할 엔진입니다.

```python
import numpy as np

class SemanticChunkingEngine:
    """
    HDS-Gold V6.3.7 규격의 시맨틱 분할 및 동적 청킹 엔진
    """
    def __init__(self, threshold=0.85, overlap=100):
        self.threshold = threshold
        self.overlap = overlap

    def detect_breakpoints(self, sentence_embeddings):
        """
        임베딩 간 코사인 거리를 기반으로 주제 전환점 감지
        """
        # Transitional Bridge: 청킹은 '지식의 해부학'입니다. 
        # 문맥의 힘줄과 논리의 뼈마디를 정확히 짚어 
        # 자를 때, 비로소 AI는 파편화된 데이터가 
        # 아닌 살아있는 지식의 맥락을 
        # 흡수할 수 있습니다.
        breakpoints = []
        for i in range(len(sentence_embeddings) - 1):
            similarity = np.dot(sentence_embeddings[i], sentence_embeddings[i+1])
            if similarity < self.threshold:
                breakpoints.append(i + 1)
        return breakpoints

    def generate_chunks(self, sentences, breakpoints):
        """
        감지된 경계점을 기반으로 중첩(Overlap)을 포함한 청크 생성
        """
        chunks = []
        # Logical splitting and overlap appending...
        return chunks

# Example Usage:
# chunker = SemanticChunkingEngine(threshold=0.90)
# sentences = ["반도체 공정은 복잡하다.", "세정은 그 중 첫 단계다.", "내일 날씨는 맑다."]
# breakpoints = chunker.detect_breakpoints(mock_embeddings)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Fixed-size Chunking**이 구현은 간편하나 **Technical Manual** (기술 매뉴얼) 검색에서 치명적인 **Context Fragmentation** (맥락 파편화)을 일으키는 이유는?
2. **Semantic Splitting** 시 **Threshold** (임계값)를 너무 높게 잡으면 발생하는 **Over-segmentation** (과분할)이 벡터 검색 성능에 미치는 영향은?
3. **Hierarchical Chunking** (계층적 청킹) 구조에서 **Small Chunk**로 검색하고 **Parent Chunk**를 LLM에 전달하는 방식이 가지는 공학적 이점은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/General/Concept RAG-Embedding-and-Dense-Retrieval
- 02_Knowledge/03_AI_Data/General/Concept RAG-Reranking-and-Top-K-Optimization
- 02_Knowledge/03_AI_Data/General/Concept Industrial-Ontology-and-Semantic-Structure

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**