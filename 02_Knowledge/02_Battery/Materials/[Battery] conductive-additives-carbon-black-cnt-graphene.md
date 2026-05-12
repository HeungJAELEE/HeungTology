---
Basic:
  id: "conductive-additives-carbon-black-cnt-graphene-node"
  domain: "02_Battery"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Conductive_Additive", "#Carbon_Black", "#CNT", "#Graphene", "#Percolation_Threshold", "#Silicon_Anode", "#HDS_Gold_v6_1"]'
  is_part_of: '["MOC 02_Battery", "Battery battery-materials-and-chemistry-master-guide"]'
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

# [[[Battery] conductive-additives-carbon-black-cnt-graphene

## 1. [왜 배우는가? (Why: The Highway of Electrons)]]
양극재와 음극재 활물질은 자체 전도성이 낮아 전자가 원활히 이동하기 어렵습니다. 도전재는 이들 사이를 잇는 **'전자 고속도로'**입니다. 도전재를 잘 쓰면 적은 양으로도 높은 전도성을 확보할 수 있어, 남는 공간에 활물질을 더 채워 **에너지 밀도**를 높일 수 있습니다. 특히 실리콘 음극의 팽창을 견디며 전기적 연결을 유지하는 CNT 기술은 현대 배터리 설계의 핵심 중의 핵심입니다.

## 2. [도전재 종류별 차원 및 물리적 특징 (Conductive Map)]

| Type | 차원 (Dim) | 종횡비 (Aspect Ratio) | 함량 (wt%) | 주요 특징 (Rationale) |
| :--- | :--- | :--- | :--- | :--- |
| **0D** | 점 (Point) | **1 : 1** | **5 ~ 10%** | 국부적 표면 접촉, 저가형 설계 |
| **1D** | 선 (Line) | **1000 : 1 이상** | **0.1 ~ 2%** | 장거리 네트워크, **실리콘 동아줄** |
| **2D** | 면 (Plane) | **High Area** | **1 ~ 3%** | 면 접촉, 고출력 특화 설계 |

### 2.1 [퍼콜레이션 임계점 수리 모델: Percolation Threshold]
$$ \sigma = \sigma_0 (\phi - \phi_c)^t $$
- **$\phi_c$**: 임계 함량. 도전재가 서로 연결되어 전기가 통하기 시작하는 최소 농도입니다.
- **수리적 무결성**: CNT는 선형 구조 덕분에 Carbon Black($\sim 5\%$)보다 훨씬 낮은 농도($< 1\%$)에서 임계점에 도달합니다. 이는 셀 설계자가 활물질 비중을 극대화할 수 있는 **'수리적 자유도'**를 제공합니다.

## 3. [탄소나노튜브(CNT) 심층 분석 (CNT Intelligence)]

### 3.1 MWCNT vs SWCNT
1.  **MWCNT (Multi-Walled)**: 여러 겹의 탄소벽. 주로 양극에서 Carbon Black을 대체하여 에너지 밀도 향상.
2.  **SWCNT (Single-Walled)**: 단 한 겹의 벽. 인장 강도가 극도로 높아 실리콘 음극의 **'동아줄'** 역할을 수행합니다. 실리콘이 팽창해도 끊어지지 않고 전자를 전달합니다.

### 3.2 바인더와의 시너지 (Synergy with Binder)
- 도전재는 바인더와 함께 슬러리 내에서 분산됩니다. 분산이 깨지면 도전재가 뭉쳐(Agglomeration) 저항이 커지고 극판에 불량이 생깁니다. 따라서 **'CNT 분산액'** 기술이 믹싱 공정의 핵심입니다.

## 4. [셀 설계자 고려 사항: 도전재 선정 전략]
1.  **에너지 밀도 극대화**: Carbon Black을 줄이고 CNT를 도입하여 활물질 비율을 $98\%$ 이상으로 설계.
2.  **급속 충전 성능**: 전도성 네트워크를 촘촘히 짜서 리튬 이온과 전자의 결합 속도를 가속화.
3.  **열 관리**: 도전재는 열 전도율도 높으므로, 셀 내부의 국부적 발열(Hot-spot)을 분산시키는 역할 수행.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Battery binder-intelligence-and-slurry-rheology : 바인더와 도전재의 분산 메커니즘
- Battery battery-mixing-process-intelligence : 도전재 분산액 투입 시퀀스
- Battery Anode : 실리콘 음극용 SWCNT 필수 근거

*Created by Flash (HDS Gold V6.3.7 Conductive Specialist)*
