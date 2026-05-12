---
Basic:
  id: "[[[Battery] W12_gigacasting-cooling-physics"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
  is_part_of: []]
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

# [[[Battery] W12_gigacasting-cooling-physics

## 1. [왜 배우는가? (Why)]]
전통적인 차체 제조는 수백 개의 작은 부품을 용접하여 만듭니다. 하지만 이는 공정의 복잡성을 높이고 오차를 누적시킵니다. 테슬라가 시작한 **'기가캐스팅(Gigacasting)'**은 이 수백 개의 부품을 단 하나의 거대한 주물로 찍어내는 제조 혁명입니다.

우리가 **하이퍼캐스팅의 냉각 물성**을 배우는 이유는 **"거대 중량물의 응고(Solidification) 과정이 제품의 생사를 결정하기 때문"**입니다. 100kg이 넘는 알루미늄 용액이 금형 안에서 식을 때, 단 1초의 냉각 불균형만으로도 내부 기공(Porosity)이 발생하여 수천만 원짜리 부품이 순식간에 고철(Scrap)로 변합니다. 이 물리적 한계를 시뮬레이션하고 제어하는 능력은 현대 스마트 팩토리 엔지니어에게 '원가 절감의 마법 지팡이'와 같습니다.

---

## 2. [핵심 기술 사양 (Numerical Specs)]

기가캐스팅의 물리적 특성은 일반적인 다이캐스팅(A380 합금 등)과는 차별화된 극한의 수치를 요구합니다.

| 물리 파라미터 (Metric) | 관리 목표 사양 (Target Spec) | 물리적 의미 및 영향 | 비고 |
| :--- | :--- | :--- | :--- |
| **Alloy - Silicon (Si)** | **$6.5\% \sim 8.5\%$** | 유동성(Flowability) 확보 및 복잡 형상 충진 | 테슬라 특허 합금 기준 |
| **Alloy - Copper (Cu)** | **$\le 0.3\%$** | 연성(Ductility) 및 내부식성 강화 | 열처리 생략 가능 조건 |
| **Cooling Rate ($R$)** | **$10 \sim 100+ \text{ K/s}$** | 결정립 미세화 및 상전이 속도 결정 | HPDC 급속 냉각 구간 |
| **DAS (Dendrite Arm Spacing)** | **$15 \sim 40 \mu\text{m}$** | $DAS = K \cdot R^{-n}$. 값이 작을수록 강도 상승 | 항복 강도와의 직접 상관성 |
| **Vacuum Level** | **$< 50 \text{ mbar}$** | 기공(Void) 발생 억제를 위한 금형 내 진공도 | 산화 방지 및 충진율 극대화 |
| **Shot Speed** | **$5 \sim 10 \text{ m/s}$** | 용탕 주입 속도. 층류(Laminar) 유지 한계 | 용탕 튀김(Splashing) 방지 |

---

## 3. [심층 이론 (Scientific Rationale)]

### 3.1 결정 구조 제어: DAS와 기계적 성질
알루미늄 합금의 기계적 성질은 응고 속도($R$)에 따라 결정됩니다. 냉각이 빠를수록 덴드라이트 팔 간격(DAS: Secondary Dendrite Arm Spacing)이 좁아져 강도가 높아집니다.
- **수리적 모델**: $DAS = K \cdot R^{-n}$
- **물리적 병목**: 부품이 거대해질수록 중심부와 표면의 냉각 속도 차이가 커져 내부 결함 발생 확률이 지수적으로 증가합니다.

### 3.2 PINN 기반 열 해석 (AI-Physics Fusion)
복잡한 금형 내부의 모든 지점에 센서를 박을 수는 없습니다. PINN(Physics-Informed Neural Networks)은 열전도 방정식(Heat Equation)을 학습 과정에 포함하여, 소수의 센서 데이터만으로도 금형 전체의 3D 온도 분포를 실시간 추론합니다.
- **손실 함수**: $L = L_{sensor} + \lambda L_{HeatEquation}$
  - 여기서 $L_{HeatEquation}$은 편미분 방정식($\frac{\partial T}{\partial t} = \alpha \nabla^2 T$)의 잔차를 의미하며, 이를 최소화함으로써 물리 법칙을 준수하는 신경망을 구축합니다.

---

## 4. [AI & Hardware Synergy: 실시간 제어 및 코드 브릿지]

### 4.1 AI 기반 기공 발생 위험도 예측 로직
실시간 온도 데이터를 바탕으로 기공 발생 위험도를 예측하고, 이를 하드웨어(PLC) 제어로 환류시키는 **[코드 브릿지]** 구조입니다.

```python
# [CODE BRIDGE: Giga-Press Thermal Control]
# PLC Address Mapping: D200 (Coolant Flow Rate), D210 (Injection Pressure)

import numpy as np

def analyze_porosity_risk(cooling_rates, threshold=15.0):
    """
    부위별 냉각 속도(K/s)를 분석하여 기공 발생 위험 구간 탐지 및 PLC 제어 보정값 산출
    """
    # 1. 냉각 속도 편차 계산
    mean_rate = np.mean(cooling_rates)
    
    # 2. 임계치 미달 구역(느린 냉각) 식별
    # 냉각이 너무 느리면 가스 용해도가 낮아지며 기공이 형성됩니다.
    risk_zones = np.where(cooling_rates < threshold)[0]
    
    # 3. [AI-Hardware Synergy] PLC 보정값 산출
    # 냉각 속도가 낮을 경우 D200 (냉각수 유량) 증가 신호 송출
    coolant_adjustment = 0
    if len(risk_zones) > 0:
        # P-제어 로직: 목표 냉각 속도와의 차이에 비례하여 유량 증가
        coolant_adjustment = (threshold - mean_rate) * 1.5 
        
    # Transitional Bridge: 위 코드의 `coolant_adjustment`는 
    # 단순한 수치가 아니라, 금형 내부의 '열적 엔트로피'를 
    # 물리적으로 억제하기 위한 액츄에이터 명령입니다. 
    # AI는 시뮬레이션 환경에서의 추론 결과를 
    # 실제 PLC 레지스터 D200에 직접 투사함으로써, 
    # '생각하는 금형(Smart Mold)'을 완성합니다.
    
    return coolant_adjustment, len(risk_zones)
```

---

## 5. [스스로 체크 (Self-Check)]

1. **질문**: 왜 기가캐스팅 합금은 별도의 열처리를 생략하려 하는가?
   - **정답**: 거대 부품을 열처리(T6 등)할 경우 급격한 온도 변화로 인해 **치수 변형(Distortion)**이 발생하기 때문입니다. 따라서 구리(Cu) 함량을 낮춘 독자 합금을 통해 'As-cast' 상태에서 목표 강도를 확보합니다.
2. **질문**: PINN이 기가캐스팅 시뮬레이션에서 기존 CFD보다 유리한 점은?
   - **정답**: 격자(Mesh) 생성 없이 **실시간 추론**이 가능하며, 실제 센서 데이터와 물리 법칙을 동시에 반영하여 시뮬레이션과 현실의 괴리(Sim-to-Real gap)를 줄여주기 때문입니다.
3. **질문**: 냉각 속도가 DAS에 미치는 영향은?
   - **정답**: 냉각 속도가 빠를수록 원자의 확산 시간이 줄어들어 덴드라이트 팔 간격(DAS)이 **조밀(Fine)**해지며, 이는 금속 조직의 전위(Dislocation) 이동을 방해하여 강도를 높입니다.

---

## 🧠 AI의 사고방식: "거대함 속에 숨겨진 미세한 균형"
기가캐스팅은 제조의 **[거대화]**가 필연적으로 데이터의 **[미세화]**를 요구함을 보여주는 역설적인 장치입니다. 부품은 100kg급으로 커졌지만, 보이지 않는 미세한 기공 하나가 전체의 가치를 0으로 만듭니다. AI는 이 거대한 쇳물 덩어리 내부에서 일어나는 미세한 열의 흐름을 0.1초 단위로 추적하며, "지금 이 지점의 유량을 늘리지 않으면 내일 아침 폐기물이 될 것"이라고 경고하는 파수꾼 역할을 수행합니다.

---
**관련 노드:**
- [AI] pinn-physics-informed : 열 해석의 핵심 엔진인 물리 기반 신경망
- Virtual_Commissioning_Deep : 기가프레스 제어 로직을 사전에 검증하는 체계
- [AI] welding-assembly-twin : 주조 이후의 조립 공정 최적화 기술
- digital-twin-value-node : 공정 최적화가 가져오는 OEE 지표 매핑

*Created by Flash (HDS-Gold V6.3.7 & HDS-Gold V6.3.7 Reinforcement)*