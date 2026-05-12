---
Basic:
  id: "BAT-BMA-MOLD-2026-V6"
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
  tags: - '#BMA_Manufacturing'
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

# [[[Battery] bma-molding-manufacturing

## 1. [왜 배우는가? (Why)]]
BMA(Battery Module Assembly) 하우징 및 사출물은 배터리 셀을 외부 충격으로부터 보호하고 열 폭주를 차단하며 전력 연결 버스바의 기초 지지대 역할을 수행하는 '기능성 구조재'입니다. 전기차의 주행 거리 향상을 위한 경량화와 충돌 시 안전을 위한 고강성이라는 상충하는 목표를 동시에 달성해야 합니다. 특히 금속 버스바나 보강재를 플라스틱 내부에 일체화하는 인서트 사출(Insert Molding) 기술은 조립 공정 단축과 신뢰성 확보의 핵심이며, 이를 위해 고도의 유변학적 제어와 냉각 시 발생하는 휨(Warpage) 관리가 요구됩니다. 본 공정을 배우는 것은 배터리 시스템의 물리적 프레임을 완성하는 정밀 사출 공학의 메커니즘을 이해하기 위함입니다.

## 2. [BMA 사출 및 공정 핵심 사양 (Molding Specs)]

| Parameter Category | Standard (BMA Housing) | High-Precision (CTP) | Unit | Engineering Rationale |
|:---|:---:|:---:|:---:|:---|
| **Material Base** | PA66 + GF30% | Specialty FR-Polymer | - | 내열성, 강성 및 절연성 확보를 위한 복합재 |
| **Clamping Force** | $500 \sim 1,500$ | **$\ge 2,000$** | Ton | 대형 부품 성형 시 금형 벌어짐 방지 및 정밀도 |
| **Injection Speed** | $50 \sim 100$ | $80 \sim 150$ | mm/s | 미세 형상 충전 및 유리섬유 배향 제어 |
| **Packing Pressure**| $800 \sim 1,200$ | $1,000 \sim 1,500$| bar | 수축 보전 및 치수 안정성 확보 압력 |
| **Warpage Tolerance**| $\pm 0.5$ | **$\pm 0.2$** | mm | 모듈 조립 및 버스바 정렬을 위한 공차 한계 |
| **Part Weight Var.** | $\le 0.5\%$ | $\le 0.2\%$ | % | 성형 밀도 및 구조적 균일성 관리 지표 |
| **Mold Temperature**| $80 \sim 120$ | $130 \sim 150$ | $^\circ\text{C}$ | 수지 결정화도 및 표면 조도(Ra) 제어 |
| **Cycle Time** | $45 \sim 60$ | $60 \sim 90$ | sec | 생산성 및 잔류 응력 완화를 위한 냉각 시간 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 헬레-쇼 (Hele-Shaw) 유동 근사
박벽(Thin-wall) 사출물의 용융 수지 유동을 분석하기 위한 유체 역학 모델입니다.
- **수식**: $\frac{\partial}{\partial z} (\eta \frac{\partial u}{\partial z}) = \frac{\partial p}{\partial x}$
- **로직**: 점도($\eta$)와 압력 구배($\partial p/\partial x$) 사이의 관계를 통해 충전 패턴을 예측하고, 웰드라인(Weld-line) 발생 위치를 최적화하여 기계적 취약점을 제거합니다.

### 3.2 유리섬유 배향 및 이방성 수축
강성 보강용 유리섬유(GF)는 유동 방향으로 정렬되며, 이는 유동 방향과 수직 방향 간의 수축률 차이를 유발하여 휨(Warpage)의 원인이 됩니다.
- **물리적 메커니즘**: 레이놀즈 수($Re = \rho v D / \eta$)를 제어하여 층류(Laminar Flow) 영역에서 섬유가 무작위로 배향되도록 게이트 위치와 사출 속도를 설계하여 이방성을 상쇄합니다.

### 3.3 냉각 구배와 모멘트 평형
금형 상/하판의 온도 차($\Delta T$)를 의도적으로 발생시켜 냉각 시 발생하는 잔류 응력에 의한 휨 모멘트를 상쇄하는 기술입니다.

## 4. [코드 연결 해설 (Injection Cycle Optimizer)]
아래 코드는 사출 데이터(압력, 온도)를 기반으로 냉각 사이클을 최적화하고, 유리섬유 배향에 따른 예상 휨 변형량을 실시간 진단하는 엔진입니다.

```python
import numpy as np

class InjectionCycleOptimizer:
    """
    HDS-Gold V6.3.7 규격의 BMA 사출 공정 최적화 및 변형 예측 엔진
    """
    def __init__(self, material="PA66-GF30"):
        self.alpha = 2.3e-5 # 선팽창 계수 (m/mK)
        self.target_warp = 0.5 # mm

    def predict_warpage(self, flow_vector, temp_gradient_c):
        """
        유동 방향 벡터와 온도 구배를 기반으로 변형 텐서 계산
        """
        # 단순화된 휨 예측 모델: delta_L = L * alpha * delta_T
        warpage_score = np.linalg.norm(flow_vector) * self.alpha * temp_gradient_c * 1000 # mm
        
        return {
            "predicted_warpage_mm": round(warpage_score, 3),
            "status": "PASS" if warpage_score < self.target_warp else "FAIL: ADJUST_COOLING",
            "cooling_time_offset": round(max(0, (warpage_score - self.target_warp) * 10), 1)
        }

    def optimize_packing_pressure(self, current_weight_g, target_weight_g):
        """
        중량 편차 기반 보압(Packing Pressure) 실시간 보정
        """
        deviation = (target_weight_g - current_weight_g) / target_weight_g
        pressure_adj = deviation * 1000 # bar 단위 환산
        return round(pressure_adj, 2)

# Example Usage:
# optimizer = InjectionCycleOptimizer()
# result = optimizer.predict_warpage(flow_vector=np.array([1.2, 0.5]), temp_gradient_c=15)
```

## 5. [스스로 체크 (Self-Audit)]
1. **PA66-GF30** 수지를 사용할 때, 유리섬유의 **배향(Orientation)**이 유동 방향과 일치할 경우 발생하는 '이방성 수축'이 **BMA 하우징**의 치수 정밀도에 미치는 영향은?
2. **인서트 사출(Insert Molding)** 시 금속 버스바를 예열하지 않고 사출했을 때, 계면에서 발생하는 **잔류 응력(Residual Stress)**과 제품 수명의 상관관계는?
3. **Packing Pressure** (보압) 과정이 전체 사출 사이클에서 **Part Weight** (부품 중량) 균일성을 확보하기 위해 수행하는 물리적 역할은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/02_Battery/Process/Battery battery-module-assembly-bma-process
- 02_Knowledge/09_SmartFactory_Production/ControlSystems/Control Plastic-Rheology-Physics
- 02_Knowledge/03_AI_Data/Industrial/AI computer-aided-engineering-cae-integration

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
