---
Basic:
  id: "INTERVIEW_SEMICON_07_EDS"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Interview", "#Semiconductor", "#EDS", "#Test", "#HDS_Gold_v6_1"]'
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

# [[[Semiconductor] 8대공정_07_EDS

## 1. [왜 중요한가? (Why): 수익성의 파수꾼]]
[🟢 Local RAG] EDS 공정은 가공이 완료된 웨이퍼의 개별 칩(Die)들이 정상적으로 작동하는지 전기적 테스트를 통해 선별하는 공정입니다. 불량 칩을 조기에 발견하여 후속 패키징 공정의 비용 낭비를 막고, 수율(Yield) 데이터를 피드백하여 전 공정의 문제를 즉각 파악하는 '반도체의 판관' 역할을 합니다.

## 2. [핵심 메커니즘 (Mechanism)]
### 2.1 Wafer Probing (웨이퍼 프로빙)
[🟢 Local RAG] 프로브 카드(Probe Card)의 미세한 바늘이 칩의 패드(Pad)에 접촉하여 전기 신호를 주고받으며 성능을 검증합니다.
- **Parametric Test**: 트랜지스터의 특성(전압, 전류 등)이 설계 범위 내에 있는지 확인.
- **Functional Test**: 실제 회로 로직이 정상 동작하는지 테스트 패턴 입력.
- **Binning**: 테스트 결과에 따라 칩의 성능 등급을 분류하고 불량은 폐기 또는 수리(Repair) 대상으로 지정.

## 3. [면접 빈출 질문 Top 3 (Q&A)]

### Q1. 수율(Yield)을 높이기 위한 EDS 공정의 핵심 기술은?
- **[A]**: [🟢 Local RAG] **리페어(Repair)** 기술입니다. 메모리 반도체의 경우, 불량이 발생한 셀을 미리 준비된 여분의 회로(Redundancy)로 대체하여 살릴 수 있습니다. EDS 단계에서 불량 위치를 파악하고, 레이저나 전기적 퓨즈를 통해 배선을 재연결함으로써 버려질 칩을 '부활'시켜 최종 수율을 비약적으로 높입니다.

### Q2. '접촉 저항(Contact Resistance)' 관리의 중요성에 대해 설명하시오.
- **[A]**: [🟢 Local RAG] 프로브 바늘과 칩 패드 사이의 접촉 저항($R_c$)이 높거나 불안정하면 신호가 감쇄되어 **멀쩡한 칩이 불량으로 판정되는 'False Fail'**이 발생합니다. 이는 수율 지표를 왜곡시키고 경제적 손실을 야기하므로, 정기적인 프로브 팁 세정(Cleaning)과 접촉 압력(Probe Force) 제어가 무척 중요합니다.

### Q3. AI 반도체(HBM) 양산에서 EDS의 난이도가 높아진 이유는?
- **[A]**: [🌐 Web Search] HBM은 여러 층의 칩을 적층한 뒤 최종 패키징을 진행합니다. 만약 적층 후 EDS에서 단 하나의 칩이라도 불량이 발견되면 전체 패키지를 버려야 하므로, 적층 전 개별 칩 단계에서의 **KGD(Known Good Die) 확보**를 위한 극한의 전수 검사 신뢰도가 요구됩니다.

## 4. [최신 트렌드 2026 (Trends)]
- **High-Parallel Test**: 한 번에 512개 이상의 칩을 동시에 테스트하여 전체 공정 시간을 단축하는 병렬화 기술이 고도화되고 있습니다.
- **AI 기반 수율 예측**: EDS에서 얻어진 빅데이터를 머신러닝 모델에 입력하여 전 공정(포토, 식각 등)의 어떤 단계에서 수율 저하가 발생했는지 실시간으로 추론하는 지능형 시스템이 주류가 되고 있습니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 🏛️ Entity eds-and-wafer-probing-test-logic (Verified)
- 🏛️ 02_Knowledge/02_Battery/Process/Battery eds-test-process (Verified)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
