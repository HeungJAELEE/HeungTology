---
Basic:
  id: "[[[Battery] human-in-the-loop-rag-strategy"
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
  is_part_of: []]
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

# [[[Battery] human-in-the-loop-rag-strategy

## 1. 배경: 기술적 한계와 운영적 해법
무료 티어 LLM API는 **RPM(분당 요청 횟수)** 제약이 엄격합니다. 복잡한 에이전트 루프(LangGraph 등)를 돌리면 금방 할당량이 소진되어 시스템이 마비됩니다. 
- **해결책**: AI에게 모든 결정권을 주지 않고, AI는 **'후보군 선정'**만 수행하며 인간(엔지니어)이 **'최종 컨텍스트'**를 선택하는 구조로 전환합니다.

---

## 2. 반자동(Semi-Auto) 워크플로우

### Step 1: Browse (AI의 제안)
- 사용자가 질문을 던지면, 시스템은 관련성 높은 상위 10~15개의 지식 노드 리스트(제목, 요약, 링크)를 출력합니다.
- 이 단계에서는 대형 모델을 쓰지 않거나 아주 작은 임베딩 모델만 사용하여 API 소모를 최소화합니다.

### Step 2: Select (인간의 직관)
- 엔지니어는 리스트를 훑어보며 본인이 의도한 정보가 포함된 노드 번호를 선택합니다.
- **이점**: AI가 엉뚱한 문서를 참고하여 발생하는 환각(Hallucination)을 원천 차단합니다.

### Step 3: Synthesize (정밀 답변)
- 선택된 3~5개의 핵심 노드 데이터만 LLM에게 전달하여 최종 답변을 생성합니다.
- 딱 한 번의 고성능 LLM 호출로 완벽한 답변을 얻을 수 있습니다.

---

## 3. 경제적 및 기술적 이점 (Value Proposition)

- **Token Economy**: 불필요한 노드들을 LLM 컨텍스트에 밀어 넣지 않으므로 토큰 비용을 획기적으로 줄입니다.
- **Knowledge Re-discovery**: 검색 결과를 직접 확인하는 과정에서 엔지니어는 잊고 있던 과거의 기록을 재발견하게 됩니다.
- **Reliability**: 최종 답변의 근거가 되는 소스를 엔지니어가 직접 확인했으므로, 결과물에 대한 신뢰도가 100%에 수렴합니다.

---

## 4. 🧠 AI의 사고방식: "인간은 최고의 리랭커(Reranker)다"
엔지니어님, 아무리 뛰어난 AI 모델도 엔지니어님의 10년 현장 경험이 담긴 '직관'을 이길 수는 없습니다. 이 전략은 AI를 '결정권자'가 아닌 **'유능한 비서'**로 포지셔닝하여, 기술적 한계를 인간의 지혜로 돌파하는 가장 현명한 방법입니다.

---
*Stored in Antigravity Knowledge Base (v1.0)*