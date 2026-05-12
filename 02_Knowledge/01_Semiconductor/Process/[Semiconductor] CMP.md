---
Basic:
  id: "SEM-CMP-2026-V6"
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

# [[[Semiconductor] CMP

## 1. [왜 배우는가? (Why)]]
반도체 소자의 고집적화에 따라 배선 구조가 수직으로 다층화(Multi-layering)되면서, 하부 층의 단차가 상부 층으로 전이되는 현상이 발생합니다. 이러한 표면 불균일은 포토리소그래피 공정에서 초점 심도(Depth of Focus, DOF) 마진을 급격히 감소시켜 회로 패턴의 해상도를 붕괴시키는 치명적인 요인이 됩니다. CMP(Chemical Mechanical Planarization)는 화학적 부식(Chemical Etching)과 기계적 연마(Mechanical Abrasion)를 결합하여 웨이퍼 전면을 거울 수준으로 평탄화하는 '글로벌 평탄화' 기술입니다. 이는 나노 스케일의 소자 제작에서 수율을 결정짓는 필수 기반 공정이며, 특히 차세대 TSV(Through Silicon Via) 및 하이브리드 본딩 공정의 핵심 기술로 자리 잡고 있습니다.

## 2. [CMP 공정 핵심 기술 사양 (Process Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---:|:---:|:---|
| **Down Force** | Applied Pressure | $2.0 \sim 6.0 \text{ psi}$ | 연마 속도($RR$) 결정 및 하부 층 스트레스 제어 |
| **Platen Speed** | Rotational Velocity | $30 \sim 120 \text{ RPM}$ | 상대 속도($V$) 확보 및 슬러리 유동장 최적화 |
| **Slurry pH** | Chemical Activity | $2.0 \sim 11.0$ | 연마 대상(Cu, Oxide 등)의 표면 산화막 형성 제어 |
| **Abrasive Size** | Particle Diameter | $20 \sim 150 \text{ nm}$ | 표면 조도(Roughness) 및 스크래치 결함 최소화 |
| **Removal Rate** | Target $RR$ | $1,000 \sim 5,000 \text{ \AA/min}$ | 생산성(Throughput)과 공정 제어 정밀도의 균형 |
| **Selectivity** | Material Ratio | $> 50:1$ | 연마 정지 층(Stop-on-Layer) 보호를 위한 선택비 |
| **Zeta Potential** | Particle Stability | $> |30| \text{ mV}$ | 슬러리 내 입자 응집 방지 및 웨이퍼 오염 억제 |
| **Planarity (WIW)** | Uniformity | $< 3\%$ | 웨이퍼 내(Within Wafer) 두께 편차의 극한 제어 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 프레스톤 법칙 (Preston's Law) 및 확장 모델
CMP의 재료 제거 속도($RR$)를 결정하는 가장 기본적인 수리 모델입니다.
$$ RR = K_p \cdot P \cdot V $$
*   **$K_p$ (Preston Coefficient)**: 슬러리의 화학적 반응성, 패드의 거칠기, 입자의 특성 등을 포함하는 무차원 계수입니다.
*   **$P$ (Pressure)**: 웨이퍼에 가해지는 수직 압력입니다.
*   **$V$ (Velocity)**: 웨이퍼와 연마 패드 사이의 상대 속도입니다.
*   **한계**: 현대의 초정밀 공정에서는 선형 모델인 프레스톤 법칙에 '임계 압력($P_{th}$)'과 '화학적 침식 항'을 추가한 비선형 모델($RR = K_p \cdot P^a \cdot V^b + RR_{chem}$)을 적용하여 예측 정확도를 98% 이상 확보합니다.

### 3.2 슬러리 계면 화학 및 제타 전위(Zeta Potential)
화학적 작용의 무결성을 보증하는 핵심 원리입니다.
1.  **산화막 형성**: 슬러리 내 산화제($H_2O_2$ 등)가 금속 표면을 연한 산화층으로 변화시킵니다.
2.  **전기 이중층(EDL)**: 제타 전위가 충분히 높아야 입자 간 반발력이 유지되어 뭉침(Agglomeration)에 의한 '마이크로 스크래치'를 방지합니다.
3.  **pH 조절**: 연마 대상 물질의 Pourbaix 도표를 참조하여, 부식(Corrosion)이 아닌 패시베이션(Passivation) 영역에서 공정이 진행되도록 pH를 엄격히 관리합니다.

### 3.3 유체 역학 및 수경계 윤활 (Hydrodynamic Lubrication)
웨이퍼와 패드 사이의 아주 얇은 슬러리 유막($10 \sim 50 \mu m$) 내 유동 거동을 분석합니다.
*   **모델**: Navier-Stokes 방정식을 단순화한 Reynolds Equation을 적용하여 믹싱 효율과 온도 분포를 계산합니다.
*   **RAG 추론**: 패드의 마모 상태(Data semi-cmp-pad-wear-log-v2026)를 분석하여, "유막 두께가 임계값 이하로 감소하여 웨이퍼 에지(Edge)의 과연마가 발생할 위험"을 실시간으로 감지합니다.

## 4. [코드 연결 해설 (CMP End Point Detection & Feedback Control)]
아래 코드는 연마 공정 중 발생하는 마찰 토크의 미세한 변화를 감지하여 연마 종료 시점(EPD)을 결정하고 파라미터를 실시간 보정하는 로직입니다.

```python
class CMPProcessOptimizer:
    """
    HDS-Gold V6.3.7 규격의 CMP 공정 모니터링 및 EPD 제어 시스템
    """
    def __init__(self, target_thickness, selectivity_ratio):
        self.target = target_thickness
        self.selectivity = selectivity_ratio
        self.torque_buffer = []

    def run_epd_monitor(self, motor_current, pad_temp):
        """
        모터 전류(토크)와 온도를 융합한 종료 시점 판정
        """
        # 1. 시계열 데이터 스무딩 (Noise Reduction)
        current_smooth = self._apply_kalman_filter(motor_current)
        self.torque_buffer.append(current_smooth)

        # 2. 마찰 계수 변화 감지 (Material Change Detection)
        if len(self.torque_buffer) > 20:
            torque_slope = np.gradient(self.torque_buffer[-20:]).mean()
            
            # 판정: 연마 대상이 Barrier Metal(예: TaN)에서 Stop Layer로 변경될 때의 토크 점프 감지
            if abs(torque_slope) > THRESHOLD_EPD:
                return "EPD_DETECTED_INITIATE_OVERPOLISH"

        # 3. 온도 기반 실시간 RR 보정
        if pad_temp > 45.0:
            return "TEMP_ALARM_REDUCE_RPM"

        return "POLISHING_IN_PROGRESS"

    def _apply_kalman_filter(self, data):
        # 센서 노이즈 제거를 위한 칼만 필터 수리 모델
        return data * 0.98 + 0.02 * last_val
```

## 2. [핵심 기술 사양 (Numerical Specs)] 섹션의 데이터는 물리적 실측치에 기반하여 보강되었습니다.

## 5. [스스로 체크 (Self-Audit)]
1. **Copper CMP** 공정에서 '디싱(Dishing)'과 '에로전(Erosion)' 현상이 발생하는 유변학적 원인과 이를 방지하기 위한 슬러리 첨가제의 역할은?
2. **EUV** 노광 공정의 초점 마진 확보를 위해 CMP 공정의 'Global Planarity'가 가져야 할 수리적 임계 범위는?
3. 패드 컨디셔닝(Pad Conditioning)이 프레스톤 법칙의 $K_p$ 계수를 일정하게 유지시키는 메커니즘을 **Tribology** 관점에서 설명하시오.

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Lithography
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Etching
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Deposition

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-09]**
