---
Basic:
  id: "SEM-ETCH-2026-V6"
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
  tags: - '#Etching'
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

# [[[Semiconductor] Etching

## 1. [왜 배우는가? (Why)]]
식각(Etching) 공정은 리소그래피를 통해 형성된 포토레지스트(PR) 패턴을 마스크로 삼아, 하부의 박막을 물리적·화학적 방법으로 제거하여 실제 회로 구조를 완성하는 '조각' 공정입니다. 반도체 소자의 고집적화에 따라 단순히 평면적으로 깎는 것을 넘어, 수직으로 수천 개의 층을 뚫어야 하는 3D-NAND의 채널 홀(Channel Hole) 형성 등 극도의 종횡비(Aspect Ratio) 제어가 필수적입니다. 선택비(Selectivity)와 이방성(Anisotropy)의 미세한 불균형이 소자의 단락이나 누설 전류를 유발하므로, 원자 단위의 정밀도를 요구하는 식각 기술은 반도체 수율(Yield)과 성능의 결정적 변수입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter / Metric | Wet Etch | Dry Etch (RIE) | ALE (Atomic Layer) | Engineering Rationale |
|:---|:---:|:---:|:---:|:---|
| **Selectivity ($S$)** | $> 100:1$ | $10:1 \sim 30:1$ | $> 1000:1$ | 타겟층 대비 하부/마스크 잔존 비율 |
| **Etch Rate ($ER$)** | High | Moderate | Low (Cycle-based) | 분당 깎이는 두께 ($\text{nm/min}$) |
| **Uniformity** | Poor | $< 3.0\%$ | $< 0.5\%$ | 웨이퍼 내 영역별 식각 깊이의 편차 |
| **Aspect Ratio (AR)** | $< 1:1$ | $\sim 100:1$ | $> 200:1$ | 식각 깊이 대비 입구 폭의 비율 |
| **Ion Energy** | N/A | $100 \sim 1000$ eV | Controlled Cycle | 물리적 타격을 결정하는 이온 에너지 |
| **Plasma Source** | N/A | CCP / ICP | ICP / Remote | 플라즈마 밀도 및 분포 제어 방식 |
| **EPD Sensitivity** | Low | High (OES) | Ultra-High | 식각 종료 시점(End-Point) 탐지 정밀도 |
| **Defect Density** | Low | Moderate | Ultra-Low | 공정 후 잔류물 및 표면 손상 밀도 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 선택비(Selectivity)와 식각율($ER$)의 관계
식각 공정의 효율성은 타겟 물질($a$)과 보호되어야 할 물질($b$) 사이의 식각율 비율인 선택비($S_{a,b}$)에 의해 결정됩니다.
$$S_{a,b} = \frac{ER_a}{ER_b}$$
원자층 식각(ALE)은 화학적 흡착과 물리적 탈착 단계를 분리하여 $S_{a,b} \rightarrow \infty$를 지향합니다.

### 3.2 이방성(Anisotropy) 지수
수직 방향($ER_z$)과 수평 방향($ER_x$)의 식각 속도 차이를 나타내며, 미세 패턴 형성을 위해 $A \rightarrow 1$을 목표로 합니다.
$$A = 1 - \frac{ER_x}{ER_z}$$
이온 보조 식각(Ion-enhanced Etching)은 플라즈마의 직진성을 이용하여 수직 방향의 화학 반응을 가속화함으로써 높은 $A$값을 확보합니다.

### 3.3 종횡비 의존성 식각 (ARDE: Aspect Ratio Dependent Etching)
패턴의 종횡비가 커질수록 반응 가스의 유입과 부산물의 배출이 어려워져 식각 속도가 느려지는 현상(Micro-loading)입니다. 이를 극복하기 위해 **극저온 식각(Cryogenic Etch)** 또는 **펄스형 플라즈마(Pulsed Plasma)** 제어를 통해 이온의 도달 거리와 중성종의 확산을 극대화합니다.

## 4. [코드 연결 해설 (End-Point Detection Signal Analysis)]
아래 코드는 플라즈마 발광 분석(OES) 신호를 실시간으로 분석하여 식각 종료 시점(EPD)을 결정하는 알고리즘입니다.

```python
import numpy as np

class EtchEPDMonitor:
    """
    HDS-Gold V6.3.7 규격의 실시간 식각 종료 탐지 엔진
    """
    def __init__(self, target_wavelength, threshold_gradient=-0.05):
        self.target_wl = target_wavelength
        self.threshold = threshold_gradient
        self.signal_history = []

    def process_oes_signal(self, spectrum):
        """
        특정 파장대의 빛 세기(Intensity) 추출 및 변화율 계산
        """
        intensity = spectrum[self.target_wl]
        self.signal_history.append(intensity)
        
        if len(self.signal_history) < 5:
            return "MONITORING"

        # 최근 5개 포인트의 기울기(Gradient) 계산
        gradient = np.polyfit(range(5), self.signal_history[-5:], 1)[0]
        
        # 신호가 급격히 떨어지는 시점(물질 변화)을 EPD로 간주
        if gradient < self.threshold:
            return "STOP_ETCH"
        return "CONTINUE"

    def apply_over_etch(self, over_etch_percent=0.1):
        """
        잔류물 제거를 위한 추가 식각(Over-etch) 시간 계산
        """
        # 공정 마진을 위한 보수적 추가 시간 적용 로직
        pass

# Example Integration
# epd_monitor = EtchEPDMonitor(target_wavelength=405) # 예: Cl 발광 감지
# while True:
#     spectrum = plasma_sensor.read()
#     if epd_monitor.process_oes_signal(spectrum) == "STOP_ETCH":
#         etcher.stop_rf_power()
#         break
```

## 5. [스스로 체크 (Self-Audit)]
1. **ARDE(Aspect Ratio Dependent Etching)** 현상이 발생하는 물리적 원인 3가지(Knudsen Diffusion, Ion Bowing, Charge-up)에 대해 설명하시오.
2. 건식 식각에서 **Sidewall Passivation(측벽 보호막)**이 이방성 확보를 위해 수행하는 역할과 폴리머 생성 가스(예: $C_4F_8$)의 기여도는?
3. **ALE(Atomic Layer Etch)** 공정이 기존 RIE 방식에 비해 생산성(Throughput)이 낮음에도 불구하고 3nm 이하 공정에서 필수적인 이유는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Lithography
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Cleaning
- 02_Knowledge/09_SmartFactory_Production/Digital_Twin/SmartFactory Plasma-Simulation-Twin

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
