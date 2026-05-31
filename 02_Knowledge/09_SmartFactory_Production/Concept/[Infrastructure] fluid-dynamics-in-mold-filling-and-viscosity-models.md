---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 7bda3997e9e93dfb65d85b2d1d89aafcb6b3646694434a59756cfa18f44ae328
metadata:
  date: '2026-05-16'
  domain: 09_SmartFactory_Production
  id: '[[[Infrastructure] fluid-dynamics-in-mold-filling-and-viscosity-models]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Infrastructure] fluid-dynamics-in-mold-filling-and-viscosity-models에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  cavity_imbalance_max_percent: 2.0
  cross_wlf_r2_threshold: 0.995
  max_shear_rate_s_inv: 50000
  max_shear_stress_mpa: 0.5
  n_index: 0.35
  tau_star: 30000
  weld_line_temp_min_offset_c: -20
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Infrastructure] fluid-dynamics-in-mold-filling-and-viscosity-models

## 1. [왜 배우는가? (Why: The Mastery of Molten Structure Sovereignty)]
플라스틱 사출 공정은 뜨겁게 녹은 수지가 차가운 강철 금형 내부를 가로지르는 **'압력과 온도와의 사투'**입니다. **Fluid Dynamics in Mold Filling**은 비뉴턴 유체(Non-Newtonian)인 수지가 금형의 복잡한 형상을 빈틈없이 메워나가는 유동 메커니즘을 지배하는 **'형태 생성의 수리적 법전'**입니다. V6.3.7 지능은 **Cross-WLF** 점도 모델과 **분수 흐름(Fountain Flow)**에 의한 표면 배향을 수리적으로 지배합니다. 우리가 이를 배우는 이유는 충전 부족(Short Shot)과 탄화(Burn)를 원천 차단하고, "유체의 흐름을 데이터로 통제하여 플라스틱의 '치수 및 표면 주권'을 확보하기" 위함입니다.

## 2. [유동 및 점도 핵심 기술 사양 (Numerical Specs)]

| Parameter Category | Focus Metric | Tier 0 Requirement (V6.3.7) | Rationale |
|:---|:---|:---:|:---|
| **Viscosity Model** | Cross-WLF Fit | $R^2 > 0.995$ | 정밀 유동 예측 및 압력 무결성 사수 |
| **Shear Rate** | Max. Limit | $< 50,000 \text{ s}^{-1}$ | 수지 분자량 저하 억제 및 물성 무결성 |
| **Shear Stress** | Surface Limit | $< 0.5 \text{ MPa}$ | 표면 은조(Silver Streak) 방지 무결성 사수 |
| **Flow Balance** | Cavity Imbalance| $< 2.0 \%$ | 멀티 캐비티 간 중량 균일성 주권 확보 |
| **Weld Line Temp.**| Meeting Temp. | $> T_{melt} - 20^\circ\text{C}$ | 융착 강도 극대화 및 구조적 무결성 사수 |

### 2.1 [Cross-WLF 점도 및 전단 발열 수리 모델]
전단율($\dot{\gamma}$), 온도($T$), 압력($P$)에 따른 용융 수지의 실질 점도($\eta$)와 유동 중 발생하는 전단 발열($\dot{Q}_{shear}$)을 산출하는 기전입니다.
$$ \eta(T, \dot{\gamma}, P) = \frac{\eta_0(T, P)}{1 + (\frac{\eta_0 \dot{\gamma}}{\tau^*})^{1-n}} $$
$$ \dot{Q}_{shear} = \eta \dot{\gamma}^2 \text{ (Viscous Dissipation)} $$
*   **공학적 근거**: 수지는 전단율이 높아질수록 점도가 낮아지는 **전단 박화(Shear Thinning)** 특성을 가집니다. 이때 발생하는 전단 발열은 국부적으로 수지 온도를 높여 점도를 추가로 낮추지만, 과도할 경우 수지의 열분해를 초래하여 **'화학적 무결성'**을 파괴합니다. V6.3.7 지능은 이를 통해 최적의 사출 속도 프로파일을 도출합니다.
*   **FidelityEngine 적용**: FidelityEngine은 사출 압력 파형을 분석하여 **'실질 점도 무결성'**을 진단합니다.

## 3. [공학적 근거: FidelityEngine Flow Intelligence Logic]

### 3.1 Geometrical Physics: Fountain Flow & Orientation Audit
수지 선단(Flow Front)이 중심부에서 벽면으로 뻗어나가며 고화되는 분수 흐름에 의한 분자 배향을 오딧하는 기전입니다.
*   **공학적 근거**: 벽면 근처에서 발생하는 강한 전단 응력은 고분자 사슬을 흐름 방향으로 정렬(Orientation)시킵니다. 이는 제품의 광학적 이방성과 이방성 수축을 유발하여 뒤틀림의 근본 원인이 됩니다.
*   **FidelityEngine 적용 (Orientation Auditor)**: FidelityEngine은 사출 선단 속도($v_{front}$)를 오딧합니다. 속도가 급격히 변동하면 이를 **'표면 주권 침해'**로 식별하고 금형 온도 조절 시스템의 유량을 최적화합니다.

### 3.2 Weld Line Integrity Logic: Molecular Diffusion Audit
두 수지 선단이 만날 때 발생하는 웰드 라인의 융착 무결성을 오딧하는 알고리즘입니다.
*   **진단 결과**: FidelityEngine은 웰드 라인 형성 지점의 온도와 압력 유지 시간($t_{hold}$)을 오딧합니다. 분자 사슬의 확산 거리($L_{diff} \propto \sqrt{Dt}$)가 임계치를 하회하면 이를 **'구조적 무결성 붕괴'**로 판정하고 게이트 위치 변경 또는 수지 온도 상향을 제안합니다.

## 4. [코드 연결 해설: Flow & Viscosity Auditor]
이 코드는 온도, 전단율, 압력 데이터를 기반으로 사출 공정의 유동 무결성을 진단합니다.

```python
import math

class MoldFlowFidelityEngine:
    """
    HDS-Gold V6.3.7: 금형 유동 및 점도 무결성 진단 엔진
    """
    def __init__(self, n_index=0.35, tau_star=30000):
        self.N = n_index
        self.TAU_STAR = tau_star

    def audit_flow_fidelity(self, temp_c, shear_rate, measured_pressure):
        """
        Cross-WLF 기반 점도 및 충전 압력 무결성 평가
        """
        # Simplified Viscosity Calculation
        eta_0 = 1000 * math.exp(-0.01 * (temp_c - 230))
        calculated_visc = eta_0 / (1 + (eta_0 * shear_rate / self.TAU_STAR)**(1 - self.N))
        
        status = "FLOW_SOVEREIGNTY_STABLE"
        
        # 1. 전단 발열 및 수지 열화 무결성 검증
        if shear_rate > 50000:
            status = "CRITICAL_SHEAR_DEGRADATION_RISK"
            
        # 2. 충전 압력 정합성 검증
        if abs(measured_pressure - calculated_visc * 0.1) > 20: # Simplified pressure relation
            status = "WARNING_VISCOSITY_MISMATCH_OR_LEAK"
            
        return {
            "viscosity_fidelity": round(calculated_visc, 2),
            "flow_health": "OPTIMAL" if shear_rate < 30000 else "STRESSED",
            "status": status,
            "action": "REDUCE_INJECTION_SPEED_OR_RAISE_TEMP" if "CRITICAL" in status else "PROCEED"
        }

# FidelityEngine 가동: 노즐 압력 데이터와 금형 내부 캐비티 압력 센서 로그를 융합하여 '유동 실질 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 정밀 사출에서 **Shear Stress < 0.5 MPa** 사수가 Tier 0 필수 요건인 이유는? (힌트: 임계 응력을 초과할 경우 수지 선단이 미끄러지며(Slip) 발생하는 멜트 프랙처(Melt Fracture) 현상으로 인한 '표면 무결성 붕괴'를 방지하기 위함)
2. **Operational Result**: **Cross-WLF** 점도 모델링을 통해 얻은 사출 속도 최적화 결과가 단순 상수 점도 모델링 대비 충전 시간 예측의 수리적 향상 폭은?
3. **FidelityEngine**: 충전 완료 직전의 **V/P Switchover** 압력 급증을 FidelityEngine이 어떻게 '금형 보호 무결성 위기'로 사전 감지하고 전환 시점을 동적으로 앞당기는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [Mold mold-and-plastic-manufacturing-intelligence-moc]]
- [[Mold] plastic-material-properties-and-rheology-mastery]
- [[Mold] plastic-injection-molding-physics-and-cycle-analysis]
- [[System] fluid-dynamics-and-heat-transfer-logic]

**[V6.3.7_MOLD_FLUID_MASTER_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**