---
Basic:
  id: "[Concept] Active-Learning-and-Human-in-the-loop-for-Defect-Classification"
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

# [Concept] Active-Learning-and-Human-in-the-loop-for-Defect-Classification

## 1. [왜 배우는가? (Why)]
AI를 학습시키려면 수만 장의 사진에 사람이 직접 "이건 불량, 저건 정상"이라고 표시(Labeling)해야 합니다. 하지만 이는 너무 힘들고 비용이 많이 듭니다. 능동 학습(Active Learning)은 AI가 스스로 공부하면서 "이 사진은 헷갈려요, 가르쳐주세요!"라고 전문가(Human)에게 콕 집어 물어보는 기술입니다. AI가 모르는 것만 골라서 가르쳐주니 적은 노력으로도 훨씬 똑똑해집니다. 이를 이해하는 것은 인간의 전문 지식과 AI의 연산력을 효율적으로 결합하여, 가장 적은 비용으로 완벽한 불량 분류 시스템을 구축하는 '데이터 가성비 전략'을 마스터하는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Strategy | Technology / Logic | Engineering Rationale |
|:---|:---:|:---|
| **Uncertainty Sam.**| Least Confidence | AI가 판단하기에 확률값이 낮아 헷갈려 하는 데이터만 골라 라벨링 요청 |
| **Diversity Sam.** | Core-set Selection | 기존 학습 데이터와 성격이 완전히 다른 새로운 유형의 데이터를 탐색 |
| **HITL** | Human-in-the-loop | AI가 판정하고 인간이 검토하며, 그 결과가 다시 AI를 가르치는 선순환 구조 |
| **Incremental L.** | Model Update | 라벨링된 새로운 데이터를 즉시 반영하여 모델을 조금씩 똑똑하게 업그레이드 |
| **Labeling Tool** | Assisted Tagging | AI가 1차로 영역을 잡아주면 인간이 확인만 하는 효율적 작업 도구 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 정보 밀도(Information Density)의 극대화
- **논리**: 모든 데이터가 학습에 똑같이 도움이 되는 것은 아닙니다. 이미 아는 정상을 1,000번 더 보여주는 것보다, 한 번도 본 적 없는 기묘한 불량을 1번 보여주는 것이 모델 발전에 훨씬 효과적입니다. 
- **결과**: 능동 학습은 학습 효과가 높은 '고밀도 데이터'만 골라 학습시킴으로써, 전체 데이터의 10%만 라벨링하고도 90% 이상의 성능을 확보하는 경이로운 효율을 보여줍니다.

### 3.2 전문가의 암묵지(Tacit Knowledge) 전이
- **논리**: 베테랑 엔지니어만 아는 미세한 불량의 차이를 AI에게 가르쳐야 합니다. 
- **효과**: 인간 참여형(HITL) 아키텍처는 전문가의 판단 근거를 데이터 형태로 AI에게 지속적으로 주입합니다. 이는 AI가 단순한 패턴 인식을 넘어 전문가의 통찰력까지 닮아가게 하여 현장 적용 가능성을 극대화합니다.

## 4. [코드 연결 해설 (Active Learning Query Logic)]
AI가 헷갈리는 데이터를 선별하여 전문가 검토 대기열로 보내는 논리 구조입니다.
```python
# 전략 지능 기반 능동 학습 및 HITL 제어 논리
def query_uncertain_samples(unlabeled_pool, model, batch_size=50):
    # 1. 미라벨링 데이터에 대해 모델 예측 수행 (Softmax 확률값 획득)
    predictions = model.predict_proba(unlabeled_pool)
    
    # 2. 불확실성 지수(Entropy) 계산
    # 엔트로피가 높을수록 AI가 많이 헷갈려 함
    uncertainty_scores = calculate_entropy(predictions)
    
    # 3. 가장 헷갈리는 데이터 상위 N개 추출
    query_indices = np.argsort(uncertainty_scores)[-batch_size:]
    samples_to_label = unlabeled_pool[query_indices]
    
    # 4. 전문가 검토 대기열(Human Review Queue)로 전송
    labeling_service.push_to_expert_queue(samples_to_label)
    
    return f"QUERIED_{batch_size}_SAMPLES_FOR_HUMAN_REVIEW"
```

## 5. [스스로 체크 (Self-Audit)]
1. '랜덤 샘플링'과 비교했을 때 '능동 학습'이 가지는 가장 큰 경제적 이점은?
2. AI가 너무 확신에 차서 "이건 무조건 정상이야!"라고 오판할 때 이를 바로잡을 방법은?
3. '인간 참여형(HITL)' 시스템에서 전문가의 검토 속도가 전체 프로젝트 일정에 미치는 영향은?
---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
