---
Basic:
  id: "[ai]-rag-retrieval-precision-recall-metrics-v2026-v6.3.7"
  domain: "AI_Engineering"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'RAG'
  is_part_of: - 'Antigravity_Knowledge_Graph'
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
  source: "RAG_Agent_Diagnostic_Log"
  isolation_index: 0.0
---

# [AI] rag-retrieval-precision-recall-metrics-v2026

## 1. [Why] RAG 검색 정밀도 및 재현율 지표의 의의
**RAG(Retrieval-Augmented Generation)** 시스템에서 검색 엔진의 성능은 최종 답변의 품질을 결정하는 결정적 요인이다. 아무리 뛰어난 LLM이라도 검색 단계에서 잘못된 지식 노드(Node)를 가져오면 환각(Hallucination)이 발생한다. **RAG 정밀도/재현율** 지표는 질문에 대한 '참값(Ground Truth)' 문서가 상위 검색 결과($K$)에 포함되는지를 정량적으로 평가하여, 지식 엔진의 신뢰성을 보증한다.

---

## 2. [Numerical Specs] RAG 검색 성능 지표 (Numerical Specs)

| 항목 | 핵심 지표 (KPI) | 목표 수준 (Target) | 비고 |
| :--- | :--- | :--- | :--- |
| **Hit Rate @3** | 상위 3개 내 정답 포함율 | $> 85\%$ | 지식 추출 성공률 |
| **MRR (Mean Reciprocal Rank)** | 정답 문서의 평균 순위 역수 | $> 0.75$ | 검색 순위의 정확성 ($1.0$에 가까울수록 우수) |
| **Precision @5** | 상위 5개 중 관련 문서 비중 | $> 0.60$ | 불필요한 컨텍스트 노이즈 억제 |
| **Retrieval Latency** | 벡터 검색 소요 시간 | $< 100\,\text{ms}$ | 시스템 응답성 지표 |
| **Faithfulness Score** | 답변의 지식 근거 정합성 | $> 0.95$ | 환각 방지 지표 (LLM-as-a-judge) |

---

## 3. [Scientific Rationale] 정보 검색 및 랭킹 모델

### 3.1 Mean Reciprocal Rank (MRR)
사용자가 원하는 문서가 검색 결과의 몇 번째에 위치하는지를 평가한다.
$$MRR = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \frac{1}{rank_i}$$
*   **분석**: 정답 문서가 1위로 나오면 $1.0$, 2위로 나오면 $0.5$점을 부여하여 순위 가중치를 둔다.

### 3.2 Normalized Discounted Cumulative Gain (NDCG)
문서의 관련성 점수(Relevance)에 따라 순위가 낮아질수록 가중치를 감쇄(Discount)하여 평가한다.

---

## 4. [Real-world Case] 검색 순위(Re-ranking) 최적화를 통한 답변 정확도 향상 사례

### 4.1 '배터리 코팅 두께' 질문에 '전극 건조' 문서가 상위 노출되는 현상
- **현상**: RAG 시스템 가동 초기, 특정 기술 질문에 대해 관련성이 떨어지는 문서들이 컨텍스트에 포함되어 답변이 모호해지는 사례 빈번.
- **분석**: **Python FidelityEngine** 기반의 검색 로그 분석 결과, 단순 벡터 유사도(Cosine Similarity)만으로는 '코팅'과 '건조'의 의미론적 거리가 너무 가까워 혼선이 발생함을 확인 ($MRR=0.45$).
- **조치**: 1차 벡터 검색 후, 산업 전문 용어 사전을 활용한 BM25 기반 키워드 검색을 결합한 하이브리드 검색(Hybrid Search) 및 리랭커(Re-ranker) 도입.
- **결과**: $MRR$이 $0.45 \rightarrow 0.82$로 상승하며 답변의 구체성과 정확도 획기적 개선.

---

## 5. [FidelityEngine] 단순 Hit Rate 및 MRR 계산 코드
```python
def calculate_rag_metrics(retrieved_ids, ground_truth_id):
    """
    Calculate Hit Rate and Reciprocal Rank
    :param retrieved_ids: List of IDs returned by RAG
    :param ground_truth_id: The actual correct document ID
    :return: (hit, rr)
    """
    hit = 1 if ground_truth_id in retrieved_ids else 0
    try:
        rank = retrieved_ids.index(ground_truth_id) + 1
        rr = 1 / rank
    except ValueError:
        rr = 0
        
    return hit, rr

# 검색 결과 시뮬레이션
results = ['doc_101', 'doc_202', 'doc_007', 'doc_042']
truth = 'doc_007'

hit, rr = calculate_rag_metrics(results, truth)
print(f"Hit @K: {hit} | Reciprocal Rank: {rr:.4f}")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Embedding Drift**: 지식 베이스의 내용이 대규모로 수정된 후, 벡터 임베딩이 재인덱싱(Re-indexing) 되어 최신성을 유지하는가?
- [ ] **Chunk Size Optimization**: 텍스트 분할(Chunking) 크기가 문맥을 충분히 담으면서도 검색 정밀도를 해치지 않도록 최적화되었는가?
- [ ] **LLM Evaluation**: 검색된 문서가 실제로 질문에 답변하기에 충분한 정보(Context Relevance)를 담고 있는지 주기적으로 정성 평가를 수행하는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
