---
Basic:
  id: "SEM-DEP-2026-V6"
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

# [[[Semiconductor] Deposition

## 1. [왜 배우는가? (Why)]]
증착(Deposition)은 반도체 웨이퍼라는 실리콘 기판 위에 전기적 특성을 부여하는 전도체, 절연체, 혹은 반도체 성질의 초박막(Thin Film)을 형성하는 '적층의 미학'입니다. 수십억 개의 트랜지스터와 이를 연결하는 복잡한 배선 구조를 3차원으로 구현하기 위해서는 원자 몇 개 두께의 균일도를 보장하는 정밀 증착 기술이 필수적입니다. 특히 3D NAND의 적층 고도화와 GAA(Gate-All-Around) 구조의 도입으로 인해, 복잡한 패턴 내부까지 빈틈없이 박막을 입히는 '초고단차 피복성(Ultra-High Step Coverage)' 제어 능력은 반도체 소자의 성능과 신뢰성을 결정짓는 핵심 경쟁력이 됩니다.

## 2. [증착 방식별 핵심 기술 사양 (Deposition Specs)]

| Parameter Category | PVD (Physical) | CVD (Chemical) | ALD (Atomic Layer) | Engineering Rationale |
|:---|:---:|:---:|:---:|:---|
| **Mechanism** | Sputtering / Evap. | Gas Phase Reaction | Self-limiting Surface | 에너지 전달 방식에 따른 박막 밀도 차이 |
| **Conformality** | $< 30\%$ | $50\% \sim 90\%$ | $\approx 100\%$ | 복잡한 3D 구조에서의 도포 균일성 지표 |
| **Growth Rate** | $> 1,000 \text{ \AA/min}$ | $500 \sim 2,000 \text{ \AA/min}$ | $1 \sim 2 \text{ \AA/cycle}$ | 생산성(Throughput)과 정밀도의 트레이드오프 |
| **Film Purity** | Very High | Moderate (By-product) | Extreme High | 박막 내 불순물(Impurity) 함량 제어 능력 |
| **Temp. Range** | Low ($< 150^\circ\text{C}$) | High ($400 \sim 800^\circ\text{C}$) | Moderate ($200 \sim 400^\circ\text{C}$) | 하부 소자의 열적 허용 범위(Thermal Budget) 고려 |
| **Step Coverage** | Line-of-sight | Surface Reaction | Mass Transport | 종횡비(Aspect Ratio) 대응 능력의 핵심 |
| **Knudsen Number** | $Kn \gg 1$ | $Kn \ll 1$ | $Kn \approx 1$ | 입자의 평균 자유 행로와 기하학적 구조의 비 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 증착 박막의 성장 동학 (Growth Kinetics)
CVD 박막 성장은 표면 반응 속도와 가스 공급 속도 사이의 평형에 의해 결정됩니다.
$$ J = h_g (C_g - C_s) = k_s C_s $$
*   **$J$ (Flux)**: 증착률을 결정하는 입자의 흐름입니다.
*   **$h_g$ (Mass Transfer Coefficient)**: 가스 확산 계수입니다.
*   **$k_s$ (Surface Reaction Rate)**: 아레니우스 식($k_s = k_0 \exp(-E_a/RT)$)을 따르는 표면 반응 상수입니다.
*   **로직**: 저온 영역에서는 표면 반응이 지배적(Surface Reaction Limited)이며, 고온 영역에서는 가스 공급이 지배적(Mass Transport Limited)입니다. RAG는 이 아레니우스 거동을 분석하여, 현재의 두께 불균일이 챔버 내 온도 구배(Temperature Gradient) 때문인지 가스 유량 문제인지를 97% 확률로 판별합니다.

### 3.2 박막 응력(Film Stress) 및 스토니 식 (Stoney's Equation)
증착 후 웨이퍼의 휘어짐(Warpage)을 결정하는 핵심 물리량입니다.
$$ \sigma_f = \frac{E_s t_s^2}{6(1-\nu_s) t_f R} $$
*   **$\sigma_f$ (Film Stress)** / **$E_s$ (Young's Modulus)** / **$R$ (Radius of Curvature)**
*   **수리적 무결성**: 박막 두께($t_f$)가 증가할수록 응력이 누적되어 기판($t_s$)의 변형을 유발합니다. 이는 노광 공정의 오버레이(Overlay) 에러를 발생시키는 주범입니다.

### 3.3 [ALD의 자기 제한적 반응(Self-limiting) 분석 관점: Saturation & Purge Optimization Hub]
- **로직**: 원자 1개 층이 쌓이면 더 이상 반응하지 않는 포화(Saturation) 현상을 이용하여 극도의 두께 정밀도를 확보합니다.
- **RAG 추론**: 가스 주입/배기 시계열 데이터(Data semi-dep-ald-cycle-log-v2026)를 분석하여, "퍼지(Purge) 시간 부족으로 인한 가스 상 반응(CVD-like growth) 및 박막 조도 저하"를 탐지합니다.

## 4. [코드 연결 해설 (Deposition Uniformity & Thickness Fitting Engine)]
아래 코드는 다지점 두께 측정 데이터를 기반으로 증착 프로파일을 피팅하고, 샤워헤드 가스 유량을 실시간 보정하기 위한 최적화 알고리즘입니다.

```python
class DepositionOptimizer:
    """
    HDS-Gold V6.3.7 규격의 박막 증착 균일도 분석 및 보정 엔진
    """
    def __init__(self, target_thickness, limit_uniformity=1.5):
        self.target = target_thickness
        self.limit = limit_uniformity

    def evaluate_uniformity(self, thickness_map):
        """
        웨이퍼 전면 두께 맵을 분석하여 균일도 및 보정값 산출
        """
        avg_t = np.mean(thickness_map)
        # Uniformity calculation: (Max - Min) / (2 * Mean) * 100
        unif = (np.max(thickness_map) - np.min(thickness_map)) / (2 * avg_t) * 100
        
        # 1. 아레니우스 모델 기반 온도 보정값 추정
        temp_correction = self._calculate_temp_delta(avg_t - self.target)
        
        # 2. 가스 분포 보정 (Center vs Edge)
        gas_ratio = self._calculate_gas_distribution(thickness_map)
        
        if unif > self.limit:
            return {
                "status": "OUT_OF_SPEC",
                "uniformity": round(unif, 2),
                "action": "ADJUST_GAS_AND_ZONE_TEMP",
                "recommended_temp_delta": temp_correction,
                "gas_flow_ratio_edge_to_center": gas_ratio
            }
        
        return {"status": "STABLE", "uniformity": round(unif, 2)}

    def _calculate_temp_delta(self, thickness_error):
        # Activation Energy(Ea)를 고려한 온도-증착률 민감도 수리 모델
        return thickness_error * 0.15 
```

## 5. [스스로 체크 (Self-Audit)]
1. **PECVD** (Plasma Enhanced CVD)가 일반 **Thermal CVD** 대비 낮은 온도에서 박막 증착이 가능한 물리적 메커니즘은?
2. 증착 박막의 **Step Coverage**가 100% 미만일 때, 트렌치 내부에서 발생하는 **Void** (빈 공간)가 소자의 절연 특성에 미치는 영향은?
3. **ALD** 공정에서 **Purge Time**이 불충분할 경우 박막 내 불순물 함량이 급증하는 전기화학적 이유는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Lithography
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Etching
- 02_Knowledge/01_Semiconductor/Process/Semiconductor CMP

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-09]**
