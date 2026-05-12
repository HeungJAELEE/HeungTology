---
Basic:
  id: "BAT-CATHODE-2026-V6"
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
  tags: - '#Cathode'
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

# [[[Battery] Cathode

## 1. [왜 배우는가? (Why)]]
양극재(Cathode)는 리튬 이온 배터리(LIB)의 핵심 4대 소재 중 에너지 밀도와 원가를 결정하는 가장 비중 있는 구성 요소입니다. 배터리의 '리튬 공급원' 역할을 수행하며, 양극의 화학적 조성에 따라 전기차의 주행 거리(Wh), 충전 속도, 그리고 화재 안전성이 결정됩니다. 특히 니켈(Ni) 함량을 극대화하여 에너지 밀도를 높이는 하이니켈 기술과, 구조적 안정성을 위해 단결정(Single Crystal) 화하는 공정 혁신은 현대 배터리 산업의 최전선 과제입니다. 양극재의 상변화 메커니즘과 열적 안정성을 이해하는 것은 안전하고 고성능인 배터리 시스템 설계를 위한 필수 기반 지식입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Material Type | Ni Content | Avg. Voltage | Spec. Capacity | Press Density | Thermal Stability |
|:---|:---:|:---:|:---:|:---:|:---|
| **LFP (Iron Phosphate)** | $0\%$ | $3.2 \sim 3.4 \text{ V}$ | $\sim 160 \text{ mAh/g}$ | $2.4 \sim 2.6 \text{ g/cc}$ | Highest (Olivine) |
| **NCM 622 (Mid-Ni)** | $60\%$ | $3.6 \sim 3.7 \text{ V}$ | $175 \sim 185 \text{ mAh/g}$ | $3.2 \sim 3.4 \text{ g/cc}$ | Moderate |
| **NCM 811 (Hi-Ni)** | $80\%$ | $3.7 \sim 3.8 \text{ V}$ | $200 \sim 210 \text{ mAh/g}$ | $3.3 \sim 3.5 \text{ g/cc}$ | Low (Poly-crystal) |
| **NCMA 90+ (Ultra-Hi)**| $> 90\%$ | $3.8 \text{ V}$ | $> 220 \text{ mAh/g}$ | $3.4 \sim 3.6 \text{ g/cc}$ | High (Single-crystal) |

### 2.1 [양극재 원소별 화학적 역할 (Role of Elements)]

양극재 내부의 각 원소는 배터리의 성능을 결정하는 고유의 수리적 미션을 수행합니다. (상세 물리 근거: Battery electrochemistry-elements-role-foundation)

1.  **Nickel (Ni)**: **[에너지의 지배자]** 함량이 높을수록 리튬 이온을 더 많이 저장할 수 있어 **에너지 밀도(Wh/kg)**를 결정합니다. 하지만 $80\%$ 초과 시 구조적 불안정성이 급증합니다.
2.  **Cobalt (Co)**: **[구조의 수호자]** 층상 구조를 안정화시키고 **전자 전도성**을 높여 출력 특성을 개선합니다. 단, 고가의 희귀 금속으로 함량을 줄이는 것이 원가 관리의 핵심입니다.
3.  **Manganese (Mn) / Aluminum (Al)**: **[안전의 방패]** 고온에서 결정 구조가 무너지는 것을 방지하고 **열적 안정성**을 확보합니다. NCMA에서 Al은 특히 하이니켈의 수명 저하를 수리적으로 방어합니다.
4.  **Lithium (Li)**: **[에너지 운반체]** 양극과 음극을 오가며 전하를 운반하는 실질적인 주인공입니다.

### 2.2 [핵심 공정 관리 지표 (Critical Management Parameters)]

양극재 제조 공정(소성, 세정, 코팅)에서 반드시 사수해야 할 5대 데이터 무결성 지표입니다.

| 관리 항목 (Param) | 관리 목표 및 기전 (Rationale) | 임계치 (Threshold) | 로컬 근거 (Evidence) |
| :--- | :--- | :--- | :--- |
| **Purity (자성이물)** | 금속 이물에 의한 분리막 관통 차단 | $< 10 \sim 20 \text{ ppb}$ | Battery battery-material-purity-and-magnetic-impurities |
| **PSD (입도 분포)** | $D_{50}$ (입자 크기 중앙값) 관리 | $10 \sim 15 \mu m$ | Battery cathode-structural-degradation-and-calendering |
| **BET (비표면적)** | 전해액과의 부반응 면적 제어 | $0.2 \sim 0.5 \text{ m}^2/g$ | Battery sei-kinetics-and-thermodynamics |
| **pH / 잔류 리튬** | 슬러리 겔화 및 가스 발생 방지 | $< 1,000 \text{ ppm}$ | Battery battery-manufacturing-process-master-guide |
| **XRD (Cation Mix)** | $Li^+ / Ni^{2+}$ 자리 바꿈 제어 | $I(003)/I(104) > 1.2$ | Data battery-ncma-xrd-lattice-analysis-v2026 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 하이니켈화의 상변화 및 열적 불안정성 수리 모델
- **근거**: Battery electrochemistry-elements-role-foundation 의 니켈 산화-환원 에너지 모델 준용.
$$ \Delta V/V = \frac{V_{H2} - V_{H3}}{V_{H2}} \times \chi_{Ni} $$
*   **$V_{H2, H3}$**: 격자 상수 변화에 따른 단위 정(Unit Cell) 부피
*   **$\chi_{Ni}$**: 니켈 함량 가중치
*   **수리적 무결성**: 니켈 함량이 $80\%$를 초과하면 충전 말기($>4.2V$)에 격자 부피가 약 $5 \sim 8\%$ 급격히 수축하며 입자 내부의 '응력 무결성'을 훼손합니다. 본 모델은 실측 데이터인 Data battery-ncma-xrd-lattice-analysis-v2026 에 의해 검증되었습니다.

### 3.2 [단결정(Single Crystal)의 기계적 무결성 분석 관점: Micro-crack Suppression Hub]
- **로직**: 다결정(Polycrystal)은 충/방전 시 입자 간 팽창/수축 불균형으로 인해 계면 균열이 발생하나, 단결정은 거대한 하나의 입자로 구성되어 균열 전파를 수리적으로 차단합니다.
- **RAG 추론**: 가스 발생 데이터(battery-swelling-log-v2026 (보강 필요))를 분석하여, "현재의 스웰링(Swelling)이 다결정 양극재의 입계 균열에 따른 전해액 부반응 때문임"을 판별하고 단결정 교체 시의 수명 개선율을 산출합니다.

### 3.3 N/P Ratio와 리튬 플레이팅 임계 분석 관점: Safety Margin & Plating Prevention Hub]
- **로직**: $N/P \text{ Ratio} = \frac{C_{anode} \cdot \rho_{anode} \cdot L_{anode}}{C_{cathode} \cdot \rho_{cathode} \cdot L_{cathode}}$
- **RAG 추론**: 저온 충전 시 전압 프로파일 변화를 분석하여, "설계된 N/P Ratio가 1.05 미만으로 떨어지는 저온 구간에서 리튬 플레이팅 발생 위험이 85% 이상임"을 수리적으로 경고합니다.

### 3.2 N/P Ratio (Capacity Balance)
양극 대비 음극의 용량 비율인 N/P Ratio는 배터리의 안전성을 결정하는 핵심 설계 인자입니다.
- **수식**: $N/P \text{ Ratio} = \frac{\text{Anode Capacity (mAh/cm}^2\text{)}}{\text{Cathode Capacity (mAh/cm}^2\text{)}}$
- **표준**: 보통 $1.05 \sim 1.15$로 설계하며, 음극 용량을 여유 있게 가져가 충전 시 음극 표면에 리튬 금속이 쌓이는 리튬 플레이팅(Lithium Plating)을 방지합니다.

### 3.3 잔류 리튬 (Residual Lithium) 제어
하이니켈 양극재는 대기 중의 수분 및 $CO_2$와 반응하여 표면에 $LiOH, Li_2CO_3$와 같은 잔류 리튬을 형성합니다. 세정(Washing) 및 표면 코팅을 통해 이를 $500 \sim 1,000 \text{ ppm}$ 이하로 관리하는 것이 공정의 핵심입니다.

## 4. [코드 연결 해설 (Cathode Design & Energy Density Simulation)]
아래 코드는 양극재 사양에 따른 셀 단위 에너지 밀도와 N/P Ratio를 시뮬레이션하는 설계 로직입니다.

```python
class CathodeDesignEngine:
    """
    HDS-Gold V6.3.7 규격의 양극 및 셀 설계 엔진
    """
    def __init__(self, capacity_mah_g, loading_mg_cm2, voltage_v):
        self.capacity = capacity_mah_g
        self.loading = loading_mg_cm2
        self.voltage = voltage_v

    def get_areal_capacity(self):
        """면적당 용량 산출 (mAh/cm2)"""
        return self.capacity * self.loading / 1000

    def calculate_required_anode(self, np_ratio=1.1):
        """필요한 음극 면적 용량 산출"""
        return self.get_areal_capacity() * np_ratio

# Example Instance: NCM 811
# engine = CathodeDesignEngine(capacity_mah_g=200, loading_mg_cm2=20, voltage_v=3.7)
# target_anode = engine.calculate_required_anode(np_ratio=1.12)
```

## 5. [스스로 체크 (Self-Audit)]
1. **단결정(Single Crystal)** 양극재가 다결정(Polycrystal) 대비 전해액과의 부반응(Gassing)이 적은 기하학적 이유는 무엇인가?
2. 하이니켈화 과정에서 **Al(알루미늄) 도핑** 또는 **표면 코팅**이 구조적 안정성을 향상시키는 화학적 매커니즘은?
3. **LFP**의 올리빈(Olivine) 구조가 **NCM**의 층상(Layered) 구조 대비 열적 안정성이 압도적으로 높은 결정학적 근거는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Materials/Battery Anode
- 02_Knowledge/02_Battery/Materials/Battery Electrolyte
- 02_Knowledge/02_Battery/Process/Battery Formation-and-Aging

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
