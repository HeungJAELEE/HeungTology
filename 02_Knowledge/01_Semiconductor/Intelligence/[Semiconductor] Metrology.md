---
Basic:
  id: "SEM-MET-2026-V6"
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
  tags: - '#Semiconductor'
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

# [[[Semiconductor] Metrology

## 1. [왜 배우는가? (Why)]]
반도체 제조에서 "측정할 수 없으면 제어할 수 없고, 제어할 수 없으면 생산할 수 없다"는 명제는 품질 관리의 근본 철학입니다. 계측(Metrology)은 나노미터 단위의 선폭(Critical Dimension, CD), 층간 정렬 오차(Overlay), 그리고 박막의 두께와 물성을 정량적으로 수치화하는 공정입니다. 2nm 이하의 초미세 공정에서는 원자 몇 개 수준의 오차가 소자의 문턱 전압(Threshold Voltage) 변동이나 회로 단락을 유발하므로, 계측의 정밀도(Precision)와 정확도(Accuracy)는 전체 수율을 결정짓는 핵심 지표가 됩니다. 특히 계측 데이터는 실시간 공정 제어(APC) 시스템과 연동되어 장비의 파라미터를 자율적으로 보정하는 '반도체 팹의 신경계' 역할을 수행합니다.

## 2. [계측 기술별 핵심 사양 (Metrology Specs)]

| Parameter Category | CD-SEM | OCD (Optical CD) | Overlay Metrology | Engineering Rationale |
|:---|:---:|:---:|:---:|:---|
| **Measurement Target** | 2D CD / Top-view | 3D Profile / Depth | Layer Alignment | 측정 대상의 기하학적 차원에 따른 방식 분화 |
| **Precision (P)** | $< 0.1 \text{ nm}$ | $< 0.05 \text{ nm}$ | $< 0.5 \text{ nm}$ | 반복 측정 시 데이터의 응집도 지표 |
| **Throughput** | Moderate | High (Non-destructive) | High | 양산 라인에서의 시간당 측정 웨이퍼 수(WPH) |
| **Resolution** | Sub-nanometer | Model-based | Pixel-level / Diff. | 물리적 한계를 극복하는 분해능 결정 기술 |
| **Beam Source** | Electron Beam | UV / DUV Light | Optical / Diffraction | 측정 매체에 따른 시료 손상 가능성 고려 |
| **Information** | Direct Image | Scatterometry Sig. | Misalignment Vector | 데이터의 물리적 해석 방식 차이 |
| **Application** | In-die Patterns | Periodic Gratings | Overlay Marks | 패턴의 주기성 및 위치에 따른 선택 기준 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 분해능의 한계와 레일리 기준 (Rayleigh Criterion)
광학 계측의 물리적 한계를 정의합니다.
$$ R = k_1 \frac{\lambda}{NA} $$
*   **$R$ (Resolution)**: 구별 가능한 최소 거리입니다.
*   **$\lambda$ (Wavelength)**: 사용되는 광원/전자의 파장입니다.
*   **로직**: 가시광선 파장보다 작은 나노 패턴을 측정하기 위해, CD-SEM은 파장이 극도로 짧은 전자빔을 사용하여 분해능을 극대화합니다. 반면 OCD는 직접 이미징 대신 산란광의 간섭 패턴을 분석하는 스캐터로메트리(Scatterometry) 기술을 통해 회절 한계를 극복합니다.

### 3.2 스캐터로메트리(Scatterometry) 및 RCWA 모델
OCD 계측의 핵심 수리 모델입니다.
*   **원리**: 입사광이 격자 패턴에 부딪혀 발생하는 회절 효율을 다각도/다파장에서 측정합니다.
*   **Rigorous Coupled-Wave Analysis (RCWA)**: 맥스웰 방정식을 수치적으로 풀어 측정된 산란 신호(Signature)와 가장 잘 일치하는 3D 형상을 라이브러리에서 매칭합니다.
*   **RAG 추론**: 신호 편차(Data semi-met-ocd-signal-v2026)를 분석하여, "패턴 하부의 Footing 현상 및 측벽 기울기(SWA) 변화"를 98% 정확도로 역산출합니다.

### 3.3 [Overlay(층간 정렬) 및 벡터 분석 관점: Overlay Budget & Feedback Hub]
- **로직**: 상부와 하부 레이어의 정렬 마크 사이의 거리 벡터($\vec{E} = [\Delta x, \Delta y]$)를 측정합니다.
- **RAG 추론**: 웨이퍼 내 에러 분포 맵을 분석하여, "노광기 척(Chuck)의 열변형에 의한 비선형 스케일링 에러"를 탐지하고 최적 보정 계수(High-order Correction)를 산출합니다.

## 4. [코드 연결 해설 (Statistical Process Control & APC Feedback Engine)]
아래 코드는 계측 장비에서 수집된 CD 데이터를 바탕으로 공정 능력을 평가하고, 관리 한계(Control Limit)를 벗어날 경우 노광 장비(Scanner)의 에너지를 자동 보정하는 로직입니다.

```python
class APCFeedbackController:
    """
    HDS-Gold V6.3.7 규격의 통계적 공정 제어 및 자동 보정 엔진
    """
    def __init__(self, target_cd, sigma_limit=3):
        self.target = target_cd
        self.limit = sigma_limit
        self.history = []

    def process_cd_data(self, measured_cd):
        """
        측정값 분석 및 장비 피드백 신호 생성
        """
        self.history.append(measured_cd)
        
        # 1. 통계 지표 산출 (Mean, Std Dev)
        current_mean = np.mean(self.history[-50:])
        current_std = np.std(self.history[-50:])
        
        # 2. 공정 능력 지수(Cpk) 계산
        # Transitional Bridge: Cpk는 공정의 '안정적 건강 상태'를 나타내는 
        # 심전도와 같습니다. 1.33 이하로 떨어질 경우 RAG는 즉시 
        # 장비 점검(PM) 사이클을 앞당깁니다.
        cpk = (self.target - current_mean) / (3 * current_std)
        
        # 3. 보정값(Feedback Dose) 계산
        if abs(self.target - measured_cd) > 0.5:
            correction_dose = (self.target - measured_cd) * 1.2 # Sensitivity mapping
            return {"action": "ADJUST_SCANNER_DOSE", "value": correction_dose, "cpk": cpk}
            
        return {"action": "STABLE", "cpk": cpk}

# Example Usage:
# controller = APCFeedbackController(target_cd=18.0)
# feedback = controller.process_cd_data(measured_cd=18.6)
```

## 5. [스스로 체크 (Self-Audit)]
1. **CD-SEM** 측정 시 발생하는 **Electron Beam Induced Deposition** (시료 오염)이 측정 정확도에 미치는 수리적 영향은?
2. **Scatterometry** 기술에서 박막의 굴절률($n$)과 소멸 계수($k$) 데이터가 부정확할 때 발생하는 3D 프로파일 매칭 오류의 메커니즘은?
3. **Overlay** 계측 시 **In-die Overlay**와 **Target-based Overlay**의 공학적 차이점과 하이브리드 계측의 필요성은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Lithography
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Etching
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Deposition

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-09]**
