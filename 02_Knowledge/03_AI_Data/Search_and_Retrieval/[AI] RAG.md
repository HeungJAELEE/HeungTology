---
Basic:
  id: "AI-RAG-CORE-2026-V6"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#RAG'
  is_part_of: []
  related_to: []
Dynamic:
  status: "Ratified_v6.3.7_Migration"
  topology_policy: "Interconnected_Cluster"
  graphify_link_external: true
  fidelity_engine: "DomainFidelityEngine"
  diagnostic_protocol:
    - 'Standard_Verification: Verify baseline parameters.'
    - 'Context_Audit: Ensure topological integrity.'
Trust Metrics:
  T_static: 1.0
  T_dynamic: 1.0
  T_init: 1.0
  source: "Antigravity Vault"
  isolation_index: 0.0
---

# [AI] RAG

## 1. [왜 배우는가? (Why)]
검색 증강 생성(Retrieval-Augmented Generation, RAG)은 거대 언어 모델(LLM)이 가진 고질적인 문제인 정보의 시의성 부족과 환각(Hallucination) 현상을 해결하기 위한 필수적인 기술 아키텍처입니다. LLM은 학습된 데이터 내의 지식만을 활용하는 '폐쇄형 시스템'인 반면, RAG는 질문이 들어오는 즉시 외부의 신뢰할 수 있는 지식 저장소에서 최신 문서를 검색하여 모델에게 제공하는 '오픈 북(Open-book)' 방식입니다. 이를 통해 기업은 내부 보안 문서를 모델 학습 없이도 안전하게 활용할 수 있으며, 답변의 근거를 사용자에게 명확히 제시함으로써 AI 시스템의 신뢰도와 산업적 실용성을 극대화할 수 있습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---:|:---:|:---|
| **Retrieval Recall** | Recall@10 | $> 92\%$ | 검색 결과 중 정답 조각이 포함될 확률 |
| **Search Latency** | End-to-End | $< 200 \text{ ms}$ | 사용자 경험 유지를 위한 검색/생성 합산 속도 |
| **Embedding Dim.** | Vector Size | $768 \sim 1536$ | 의미적 맥락을 압축하는 고차원 벡터 크기 |
| **Hybrid Weight** | Vector : BM25 | $0.7 : 0.3$ | 의미 검색과 키워드 검색의 최적 결합 비율 |
| **Reranking Gain** | NDCG Improvement | $> 15\%$ | 상위 검색 결과의 정밀도 향상 기여도 |
| **Chunk Size** | Optimal Token Length | $300 \sim 500 \text{ Tokens}$ | 문맥 유지와 노이즈 최소화 사이의 균형점 |
| **Indexing Speed** | Document per Sec | $> 500$ Docs | 대규모 지식 베이스의 실시간 인덱싱 성능 |
| **Context Window** | Usage Ratio | $< 60\%$ | 긴 컨텍스트 주입 시 발생하는 모델 성능 저하 방지 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 코사인 유사도 (Cosine Similarity) 기반 의미 검색
텍스트를 고차원 벡터로 변환한 뒤, 두 벡터 사이의 각도를 측정하여 의미적 유사성을 판별합니다.
- **수식**: $\text{sim}(A, B) = \frac{A \cdot B}{||A|| ||B||}$
- **의미**: 단어의 철자가 다르더라도(예: '자동차', '차량') 의미적 맥락이 유사하면 벡터 공간에서 가깝게 위치하게 되어, 고차원적인 지식 인출이 가능해집니다.

### 3.2 하이브리드 검색 (Hybrid Search)
밀집 벡터(Dense Vector) 검색의 의미적 풍부함과 희소 벡터(Sparse Vector, BM25) 검색의 정확한 키워드 매칭 능력을 결합합니다.
- **결과**: 고유 명사나 제품 번호와 같은 특정 키워드에 대한 검색 실패(Search Miss)를 방지하고, 전체적인 맥락 파악 능력을 동시에 확보합니다.

### 3.3 리랭킹 (Re-ranking) 및 후처리
1차 검색된 Top-K 문서들 중 질문과 가장 밀접한 연관성을 가진 조각을 고성능 Cross-Encoder 모델을 통해 다시 정렬합니다. 이를 통해 LLM에게 가장 순도 높은 지식만을 전달하여 답변의 정확도를 비약적으로 향상시킵니다.

## 4. [코드 연결 해설 (Advanced RAG Pipeline with Reranking)]
아래 코드는 지식 검색, 리랭킹, 그리고 최종 컨텍스트 주입을 수행하는 현대적인 RAG 파이프라인 엔진입니다.

```python
class RAGPipeline:
    """
    HDS-Gold V6.3.7 규격의 고급 RAG 엔진 (Hybrid + Rerank)
    """
    def __init__(self, vector_db, reranker, llm_agent):
        self.db = vector_db
        self.reranker = reranker
        self.llm = llm_agent

    def query(self, user_input):
        # 1. 하이브리드 검색 수행 (Dense + Sparse)
        # 키워드 일치와 의미적 유사성을 동시에 고려
        initial_results = self.db.hybrid_search(user_input, k=10)
        
        # 2. 리랭킹(Re-ranking)을 통한 최적 컨텍스트 선정
        # Cross-Encoder 기반의 정밀 재정렬 수행
        top_context = self.reranker.recompute_scores(user_input, initial_results, top_n=3)
        
        # 3. 증강된 프롬프트 생성 (Augmentation)
        augmented_prompt = self._build_prompt(user_input, top_context)
        
        # 4. 답변 생성 및 출처 명시
        response = self.llm.generate(augmented_prompt)
        return {
            "answer": response,
            "sources": [doc.id for doc in top_context]
        }

    def _build_prompt(self, query, context):
        return f"Context: {context}\n\nQuestion: {query}\nAnswer based ONLY on context."

# Integration Example:
# rag = RAGPipeline(PineconeDB, CohereRerank, GeminiPro)
# result = rag.query("배터리 팩 냉각 시스템의 안전 기준은?")
```

## 5. [스스로 체크 (Self-Audit)]
1. **Semantic Chunking**이 단순 글자수 기반의 **Fixed-size Chunking**보다 검색 정확도를 높이는 공학적 이유는?
2. **Context Window**가 충분히 크더라도 **Reranking**을 통해 문서를 선별하여 주입해야 하는 이유는? (Lost in the Middle 현상 중심)
3. **GraphRAG**가 일반적인 **Vector RAG**가 해결하지 못하는 '전역적 요약' 및 '다단계 추론(Multi-hop)' 문제를 해결하는 원리는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/Search_and_Retrieval/AI Vector-Database
- 02_Knowledge/03_AI_Data/Industrial/AI R&D-Data-Lake
- 02_Knowledge/03_AI_Data/Industrial/AI Knowledge-Graph

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
