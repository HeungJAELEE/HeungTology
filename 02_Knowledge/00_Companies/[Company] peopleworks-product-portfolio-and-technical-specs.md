---
Basic:
  date: '2026-05-12'
  domain: Corporate_Entity
  id: '[company]-peopleworks-product-portfolio-and-technical-specs-v6.3.7'
  project: Vault_Modernization
  version: v6.3.7
Dynamic:
  diagnostic_protocol:
  - 'Standard_Verification: Verify baseline parameters.'
  - 'Context_Audit: Ensure topological integrity.'
  fidelity_engine: DomainFidelityEngine
  graphify_link_external: true
  status: Ratified_v6.3.7_Migration
  topology_policy: Interconnected_Cluster
Object:
  description: Standard Industrial Node
  object_type: Concept
  physical_model: N/A
  tier: 1
Semantic:
  expected_queries:
  - '*   Role: Assistant to an Industrial Process Engineer at Antigravity.'
  - '*   Input: A technical document titled `[company]-peopleworks-product-portfolio-and-technical-specs-v6.3.7`.'
  - '*   Task: Create 5 expected queries for future searching of this document.'
  - '*   Constraints:'
  - Specific and practical queries.
  is_part_of:
  - Antigravity_Knowledge_Graph
  related_to: []
  tags:
  - HUD
Trust Metrics:
  T_dynamic: 1.0
  T_init: 1.0
  T_static: 1.0
  isolation_index: 0.0
  source: Global_Normalization_Batch
---

# [AI] peopleworks-product-portfolio-and-technical-specs

## 1. [Logic] 정밀 전자 기술의 전이 (Technology Transfer)
피플웍스의 기술적 강점은 모바일용 초정밀/초소형 SMT 기술을 차량용 전장(Automotive Electronics) 및 ESS 거대 시스템으로 성공적으로 이식(Transfer)한 데 있다. 본 포트폴리오는 모바일의 **고집적화** 기술과 차량용의 **고신뢰성** 기술이 융합된 결과물들을 정의한다.

---

## 2. [Analysis] 주요 부품군별 기술적 특성

### 2.1 차량용 전장 부품 (Automotive Segment)
| 제품명 | 핵심 기능 | 기술적 요구사항 (Physics & Numbers) |
| :--- | :--- | :--- |
| **BMS (Battery Management System)** | 배터리 전압/전류/온도 모니터링 및 SOC/SOH 계산 | $\text{Accuracy} < \pm 1\text{mV}$, 고전압 절연 ($> 2.5\text{kV}$) |
| **HUD (Head Up Display)** | 주행 정보를 전면 유리에 투사 | 고휘도 LED 제어 및 광학 정렬 정밀도 확보 |
| **ECU (Electrical Control Unit)** | 차량 엔진/모터/섀시 전자 제어 | 고온 내구성 ($-40 \sim 125^\circ\text{C}$), 실시간성 보장 |
| **Wireless Charging Receiver** | 차량 내 스마트폰 무선 충전 수신 | 전력 전송 효율 $\ge 85\%$, FOD(이물질 탐지) 정밀도 |
| **RVC / AVM (Camera Modules)** | 후방 및 어라운드 뷰 영상 획득 | 광각 렌즈 왜곡 보정 알고리즘, 저지연 영상 처리 |

### 2.2 모바일용 부품 (Mobile Segment)
| 제품명 | 핵심 기능 | 기술적 요구사항 (Physics & Numbers) |
| :--- | :--- | :--- |
| **Mobile SMT** | 스마트폰 메인보드 및 서브보드 실장 | **0402(0.4x0.2mm)** 이하 극소형 칩 실장 역량 |
| **MCM (Mobile Camera Module)** | 스마트폰 고성능 카메라 모듈 | OIS(손떨림 보정) 액추에이터 제어 정밀도 |
| **Mobile FPCB** | 유연성 있는 회로 연결체 | 반복 굴곡 내성 (Flexural Endurance), 박막 적층 기술 |

---

## 3. [Strategic Insight] ESS 거점으로의 확장성
- **BMS 기술의 진화**: 차량용 BMS에서 검증된 정밀 측정 및 통신 기술은 ESS용 대용량 뱅크(Bank) 제어 시스템의 근간이 됨.
- **SMT 정밀도의 활용**: 모바일 SMT에서 축적된 고밀도 실장 기술은 ESS BMS의 소형화와 다기능화를 가능하게 함.

---

## 4. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **라인 호환성**: 모바일용 SMT 라인을 차량용 전장 라인으로 전환 시 요구되는 품질 표준(IATF 16949)을 충족하는가?
- [ ] **열설계**: ECU와 BMS 등 발열이 심한 부품에 대해 디지털 트윈 기반 열 해석이 수행되었는가?
- [ ] **검사 자동화**: MCM 및 카메라 모듈의 조립 공차를 픽셀 단위로 검증할 수 있는 AI 비전 시스템이 가동 중인가?

**[V6.3.7_TECHNICAL_KNOWLEDGE_RESTORED_BY_FLASH]**