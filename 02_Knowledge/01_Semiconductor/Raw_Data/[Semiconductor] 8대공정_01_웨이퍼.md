---
Basic:
  id: "INTERVIEW_SEMICON_01_WAFER_FAB"
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
  tags: '["#Interview", "#Semiconductor", "#Wafer", "#Fabrication", "#HDS_Gold_v6_1"]'
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

# [[[Semiconductor] 8대공정_01_웨이퍼

## 1. [왜 중요한가? (Why): 지능의 대지 구축]]
[🟢 Local RAG] 웨이퍼 제조는 반도체 집적회로를 그리기 위한 '도화지'를 만드는 공정입니다. 고순도 다결정 실리콘을 녹여 단결정 잉곳(Ingot)을 성장시키고, 이를 얇게 잘라 연마함으로써 물리적 결함이 제로에 수렴하는 완벽한 평면을 사수해야 합니다. 웨이퍼의 순도가 낮거나 표면 조도(Roughness)가 불량하면 이후 모든 공정(포토, 식각 등)의 수율이 붕괴됩니다.

## 2. [핵심 메커니즘 (Mechanism)]
### 2.1 쵸크랄스키(Czochralski, CZ) 법
[🟢 Local RAG] 단결정 실리콘을 얻기 위해 가장 널리 쓰이는 방법입니다.
1. **Melting**: 도가니에 고순도 다결정 실리콘을 넣고 $1,420^\circ\text{C}$ 이상으로 가열하여 용해.
2. **Seeding**: 단결정 종자(Seed)를 용액에 접촉.
3. **Pulling**: 종자를 회전시키며 천천히 끌어올려 원기둥 형태의 잉곳 형성.
4. **Slicing & Polishing**: 다이아몬드 톱으로 슬라이싱 후 CMP 공정을 통해 거울면(Mirror Surface) 확보.

## 3. [면접 빈출 질문 Top 3 (Q&A)]

### Q1. 왜 반도체 기판으로 '실리콘(Si)'을 주로 사용하나요?
- **[A]**: [🟢 Local RAG] 세 가지 핵심 이유가 있습니다. 첫째, 지구상에 매장량이 풍부하여 **경제성**이 뛰어납니다. 둘째, **열적 안정성**이 우수하여 고온 공정에 유리합니다. 셋째, 공기 중 산소와 반응하여 양질의 절연막($SiO_2$)을 형성하는 **산화 특성**이 탁월하기 때문입니다.

### Q2. 웨이퍼의 직경이 커질수록(예: 8인치 → 12인치) 어떤 이점이 있나요?
- **[A]**: [🌐 Web Search] 생산 효율성(Economy of Scale)입니다. 웨이퍼 직경이 커지면 한 번에 생산할 수 있는 칩(Die)의 개수가 기하급수적으로 늘어납니다. 12인치 웨이퍼는 8인치 대비 면적이 약 2.25배 넓지만, 테두리 손실(Edge Loss) 비율이 낮아 실제 가용 칩 수는 그 이상으로 증가하여 칩당 생산 단가를 획기적으로 낮출 수 있습니다.

### Q3. 잉곳 성장 시 발생하는 불순물 제어 방법은?
- **[A]**: [🌐 Web Search] 회전 속도와 온도 구배를 정밀 제어하는 것 외에도, 최근에는 자기장을 이용한 **MCZ(Magnetic Czochralski)** 법을 사용합니다. 강한 자기장을 걸어 용융액의 대류를 억제함으로써 도가니의 산소 불순물이 잉곳으로 침투하는 것을 차단합니다.

## 4. [최신 트렌드 2026 (Trends)]
- **18인치(450mm) 웨이퍼의 정체**: 장비 교체 비용 문제로 12인치가 주류를 이루고 있으나, 선단 공정에서는 웨이퍼 평탄도를 원자 단위로 제어하는 **Super-Flat Wafer** 기술이 HBM 등 첨단 패키징의 수율을 결정짓고 있습니다.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 🏛️ 02_Knowledge/01_Semiconductor/Process/Semiconductor silicon-wafer-crystal-growth (보강 필요)
- 🏛️ Entity calendering-and-porosity-optimization (평탄도 제어 로직 참조)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
