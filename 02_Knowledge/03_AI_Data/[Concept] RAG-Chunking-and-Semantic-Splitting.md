---
Basic:
  id: "[Concept] RAG-Chunking-and-Semantic-Splitting"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
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

# [Concept] RAG-Chunking-and-Semantic-Splitting

## 1. [왜 배우는가? (Why)]
방대한 기술 문서를 AI에게 통째로 던져주면, AI는 핵심을 놓치거나 앞뒤 맥락을 섞어버리는 실수를 합니다. RAG(검색 증강 생성) 시스템에서 가장 중요한 첫 단추는 문서를 적절한 크기로 자르는 '청킹(Chunking)'입니다. 단순히 글자 수대로 자르는 것이 아니라, 의미가 끊기지 않게 '시맨틱 분할(Semantic Splitting)'을 해야 합니다. 청킹 전략을 이해하는 것은 AI가 방대한 지식 속에서 필요한 정보만을 정확하게 끄집어내어, 가장 고품질의 답변을 생성하게 만드는 '데이터 조각의 예술'을 배우는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Strategy | Mechanism | Engineering Rationale |
|:---|:---:|:---|
| **Fixed-size Chunking**| Token Limit | 정해진 토큰 수(예: 512 tokens)만큼 기계적으로 자르는 방식. 가장 빠르지만 맥락 손실 위험 |
| **Recursive Splitting**| Delimiters | 마침표, 줄바꿈 등 문장 구조를 인식하여 계층적으로 자르는 방식. 맥락 유지에 유리 |
| **Semantic Splitting** | Embedding Sim. | 문장 간의 의미적 유사성을 계산하여, 주제가 변하는 시점에서 자르는 고도화된 방식 |
| **Context Overlap** | Buffer Zone | 조각난 정보들 사이의 연결 고리를 유지하기 위해 앞뒤 내용을 일부 중첩(예: 10~20%)시키는 기법 |
| **Hierarchical Chunking**| Parent-Child | 작은 조각(Child)으로 검색하고, 실제 답변 생성 시에는 큰 조각(Parent)을 제공하여 풍부한 맥락 확보 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 정보 밀도와 검색 정확도의 최적화
- **논리**: 조각이 너무 크면 노이즈가 섞여 검색 품질이 떨어지고, 너무 작으면 핵심 의미를 담지 못합니다. 
- **결과**: 적절한 청킹은 문서의 정보 밀도를 최적화하여, 벡터 데이터베이스에서 질문과 가장 관련성이 높은 '순수한 정보'만을 정확하게 타격(Hit)할 수 있게 합니다.

### 3.2 맥락 보존(Context Preservation)의 중요성
- **논리**: 문장의 중간에서 뚝 끊겨버린 정보는 AI에게 혼란을 줍니다. 
- **효과**: 중첩(Overlap)과 시맨틱 분할을 통해 정보의 앞뒤 인과관계를 보존하면, AI가 답변을 생성할 때 끊김 없는 논리적 흐름을 유지할 수 있으며 이는 답변의 신뢰도를 결정짓는 핵심 요소가 됩니다.

## 4. [코드 연결 해설 (Recursive Text Splitting Logic)]
문장 구조를 유지하며 텍스트를 최적의 조각으로 나누는 논리 구조입니다.
```python
# AI 지능 기반 RAG 텍스트 청킹 논리
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_industrial_manual(text):
    # 1. 분할기 설정 (토큰 수 512, 중첩 50)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ""] # 중요도 순으로 구분자 적용
    )
    
    # 2. 텍스트 분할 수행
    chunks = splitter.split_text(text)
    
    # 3. 각 조각에 메타데이터(출처, 섹션) 부여하여 저장 준비
    processed_chunks = [{"content": c, "metadata": {"source": "manual_v1"}} for c in chunks]
    
    return processed_chunks
```

## 5. [스스로 체크 (Self-Audit)]
1. '중첩(Overlap)' 설정이 RAG 답변의 '일관성'에 어떤 영향을 미치는가?
2. '시맨틱 분할'을 위해 문장 간 유사도를 측정할 때 발생하는 '계산 비용'과 '검색 품질' 사이의 트레이드오프는?
3. 기술 문서의 '표(Table)'나 '코드(Code)'를 청킹할 때 주의해야 할 특별한 기법은?
---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
