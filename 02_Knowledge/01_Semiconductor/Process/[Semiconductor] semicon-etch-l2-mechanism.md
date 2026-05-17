---
metadata:
  id: "[[[Semiconductor] semicon-etch-l2-mechanism]]"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Semiconductor] semicon-etch-l2-mechanism에 관한 고밀도 지능 노드"
semantic:
  tags: ["#01_Semiconductor", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Semiconductor] semicon-etch-l2-mechanism

RIE(Reactive Ion Etching): 화학적 라디칼 반응성(Chemical Reactivity) 및 물리적 이온 방향성(Ion Directionality)을 결합한 하이브리드 수직 프로파일 구현 공정. 본 문서는 공정 파라미터 간 수리적 상관관계 정의 및 무결점 패터닝 표준 운영 절차를 규정함.

| 변수 (Parameter) | 수리적 영향 (Impact) | 제어 목적 (Rationale) | 출처 (Source) |
| :--- | :--- | :--- | :--- |
| **Gas Flow Ratio** | Chemical reaction rate | 선택비($Selectivity$) 및 측벽 보호막 제어 | [Ref: SEMI E47.1 Section 3.1] |
| **RF Bias Power** | Ion bombardment energy | 이방성($Anisotropy$) 강화 및 바닥면 타격 | [Ref: SEMI E47.1 Section 4.1] |
| **Chamber Pressure**| Mean Free Path ($\lambda$) | 이온의 직진성 및 확산 거동 제어 | [Ref: SEMI E47.1 Section 4.3] |
| **Cathode Temp.** | Surface reaction kinetics | 부산물 증착 및 폴리머 중합 조절 | [Ref: SEMI E47.1 Section 5.1] |
| **Dwell Time** | Residence time of species | 가스 교체 주기 및 배기 효율 제어 | [Ref: SEMI E47.1 Section 5.3] |

### [Theoretical vs Verified Contrast]
| Metric | Theoretical (Ideal) | Verified (Practical) | [Ref] |
| :--- | :--- | :--- | :--- |
| **Selectivity ($S$)** | $\infty$ (Purely Chemical) | $S < S_{limit}$ (Physical Sputtering limit) | [Ref: SEMI E47.1 Section 3.2] |
| **Anisotropy ($A$)** | $1.0$ (Perfect Vertical) | $A < 1.0$ (Ion Scattering/Bowing) | [Ref: SEMI E47.1 Section 4.2] |
| **Etch Rate ($ER$)** | Linear with radical flux | Non-linear (Ion-assisted kinetics) | [Ref: SEMI E47.1 Section 6.1] |

### 1. Gas Supply & Plasma Generation
- **Gas Modulation**: 불활성 가스(Ar) 및 반응성 가스($CF_4, CHF_3, Cl_2$) MFC 유입.
  - **SOP**: 설정 유량 $\pm 1\%$ [Ref: Antigravity_SOP] 이내 안정화 확인 후 RF 인가.
- **Plasma Generation**: RF Power 기반 가스 전리 및 플라즈마 벌크 생성.
  - **SOP**: Self-Bias 전압($V_{dc}$) 모니터링. 타겟 대비 $\pm 10\text{V}$ [Ref: Antigravity_SOP] 이상 편차 발생 시 공정 즉시 중단.

### 2. Passivation & Endpoint Detection (EPD)
- **Passivation Control**: $C_x F_y$ 계열 가스를 이용한 측벽 폴리머($Polymer$) 형성.
  - **SOP**: 폴리머 과다 증착 시 $O_2$ 가스 미세 첨가 통한 Scavenging 비율 튜닝.
- **EPD Implementation**: 광방출 분광법(OES) 기반 특정 파장 강도 감지.
  - **SOP**: 타겟 물질 제거 완료 시점(Intensity Drop) 감지 후 $0.1\text{s}$ [Ref: Antigravity_SOP] 단위 과식각(Over-etch) 수행 후 종료.

### 3. Mathematical Modeling
식각 속도($ER$)는 이온 보조 반응 모델에 의해 다음과 같이 정의됨:
$$ ER \approx \frac{1}{\rho} \cdot \frac{K \cdot S_{rad} \cdot J_{rad}}{1 + \frac{K \cdot S_{rad} \cdot J_{rad}}{Y_i \cdot J_i}} $$
- **Core Logic**: 선택비 극대화를 위한 화학적 반응($J_{rad}$) 비중 증가 시, 이방성($Anisotropy$) 저하 수반. 이온 보조 반응(Ion-assisted reaction) 임계점 확보가 공정 최적화의 핵심임.

### 4. Process Window Analysis
- **Pressure vs. Directivity**: 압력 상승 $\rightarrow$ 반응 속도 증가 $\rightarrow$ 평균 자유 행로($\lambda$) 감소 $\rightarrow$ 이온 충돌 빈도 증가 $\rightarrow$ 직진성 저하.
- **Power vs. Mask Integrity**: RF Bias 증가 $\rightarrow$ 이방성 향상 $\rightarrow$ 마스크 물리적 식각(Sputtering) 가속 $\rightarrow$ 프로파일 왜곡 유발.

### 5. Verification Checklist
- [ ] $O_2$ 농도 변화 $\rightarrow$ 폴리머 형성율 $\rightarrow$ $ER$ 상관관계 검증 완료 여부.
- [ ] $V_{dc}$ 급감 $\rightarrow$ IEDF 변화 $\rightarrow$ 프로파일(Bowing) 영향 평가 완료 여부.
- [ ] EPD 오작동 방지 Pre-conditioning 및 Chamber Cleaning SOP 준수 여부.

**Knowledge Lineage**
- 🏛 Entity: `plasma-physics-and-dry-etching-mechanisms-in-nanofabrication` (Verified)
- 🏛 Entity: `Semiconductor plasma-etching-mechanisms-and-high-aspect-ratio-control` (Verified)
- 🏛 Entity: `Semiconductor semicon-etch-l1-physics` (Verified)
- 🏛 Entity: `Semiconductor semicon-etch-l3-hardware` (Pending Upgrade)

*Document upgraded by Antigravity V7.5.3 Senior Architect*
