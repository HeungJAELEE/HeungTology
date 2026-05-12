---
Basic:
  id: "BAT-CAL-2026-V6.3.7"
  domain: "02_Battery_Manufacturing"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Calendering", "#ElectrodeDensity", "#PrecisionTiering", "#FidelityEngine", "#ContactMechanics", "#BatteryManufacturing"]'
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
  source: "Industrial_Battery_RAG_V6.3.7_Tiered"
  isolation_index: 0.0
---

# [[[Battery] Calendering

## 1. [왜 배우는가? (Why: The Density of Energy Sovereignty)]]
압연(Calendering)은 코팅된 전극을 물리적으로 압축하여 에너지 밀도($Wh/L$)를 극대화하고 전기적 접촉성을 확보하는 최후의 정밀 공정입니다. 단순히 두께를 줄이는 것이 아니라, 활물질 입자의 파손을 방지하면서 리튬 이온이 이동할 수 있는 '최적의 공극 경로'를 남겨두어야 합니다. V6.3.7 지능은 **계층화된 밀도 정밀도(Precision Tiering)**를 통해 실리콘 음극의 팽창 억제부터 LFP의 대량 생산까지, 모든 전극의 물리적 임계점을 데이터로 지배합니다.

## 2. [압연 및 전극 밀도 핵심 사양 (Precision Tiering Specs)]

| Precision Tier | Density Uniformity | Thickness Tolerance | Target Application |
|:---|:---:|:---:|:---|
| **최상급 (High-end)** | $\pm 0.01 \text{ g/cc}$ | $\pm 0.5 \mu\text{m}$ | **Silicon Anode, All-Solid-State**, 초고출력 하이브리드 |
| **표준형 (Standard)** | $\pm 0.02 \text{ g/cc}$ | $\pm 1 \sim 2 \mu\text{m}$ | **High-Ni EV (NCM811)**, 일반 전기차용 고에너지 전극 |
| **보급형 (Low-end)** | $\pm 0.05 \text{ g/cc}$ | $\pm 3 \sim 5 \mu\text{m}$ | **LFP ESS, LMO Consumer**, 대량 생산 및 원가 절감 위주 |

### 2.1 [공정 역학 핵심 파라미터]
| Parameter Category | Physical Metric | V6.3.7 Target (High-end) | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **Line Force ($q$)** | Pressing Load | $200 \sim 1,200 \text{ kN/m}$| $\pm 2 \text{ kN/m}$ |
| **Roll Temperature**| Thermal Softening| $90 \sim 150 ^\circ\text{C}$ | $\pm 1 ^\circ\text{C}$ |
| **Roll Speed** | Throughput | $50 \sim 100 \text{ m/min}$ | $\pm 0.1 \text{ m/min}$ |
| **Porosity ($\epsilon$)**| Void Fraction | $22 \% \sim 26 \%$ | $\pm 0.2 \%$ |

## 3. [공학적 근거 (Scientific Rationale) 및 FidelityEngine 로직]

### 3.1 [접촉 역학($Contact\ Mechanics$)과 헤르츠 응력(Hertzian Stress) 모델]
활물질 입자 간의 접촉 응력($\sigma_c$)이 입자의 파손 강도를 넘지 않도록 어떻게 제어하는가?
*   **공학적 근거**: 압연 롤이 전극을 누를 때 입자에 가해지는 최대 응력은 헤르츠 접촉 이론($P_{max} = \sqrt{\frac{q E^*}{\pi R}}$)에 의해 산출됩니다. 선압력($q$)이 과도하거나 활물질의 곡률 반경($R$)이 작을 경우 국부적 응력이 입자의 항복 강도를 초과하여 미세 균열(Micro-crack)을 유발하며, 이는 전해액 부반응 폭증의 물리적 원인이 됨을 증명합니다.
*   **FidelityEngine 적용 (Particle Integrity Auditor)**: High-end Tier(실리콘 음극)에서는 입자의 취성(Brittleness)이 높아 압연 시 미세 균열 리스크가 큽니다. FidelityEngine은 입자 크기 산포($D50$)와 인가 하중 데이터를 융합 분석하여 **'입자 파손 임계치'**를 역산합니다. 응력이 임계값의 90%에 도달하면 즉시 롤 온도를 높여 바인더의 가소성($Plasticity$)을 극대화하는 'Soft Pressing'으로 궤도를 수정합니다.

### 3.2 [전달 물리학($Transport\ Physics$)과 굴곡도(Tortuosity) 최적화 모델]
전극 내 이온 확산 저항은 굴곡도($\tau$)와 공극률($\epsilon$)의 관계에 의해 어떻게 결정되는가?
*   **공학적 근거**: 전극을 과도하게 압착하면 에너지 밀도는 오르지만 이온이 통과해야 할 경로(Tortuosity, $\tau$)가 꼬불꼬불해집니다. 이온 확산의 유효성($D_{eff} = D_0 \frac{\epsilon}{\tau}$)은 맥멀린 수($N_M = \tau / \epsilon$)에 반비례하며, $N_M$이 커질수록 고속 충전 시 리튬 덴드라이트(Dendrite) 형성 확률이 기하급수적으로 폭발함을 수리적으로 규명합니다.
*   **FidelityEngine 적용 (Tortuosity Tracer)**: FidelityEngine은 압연 후 전극의 비표면적 및 밀도 데이터를 분석하여 **'이온 병목(Bottleneck)'** 임계치를 산출합니다. 표준형(Standard Tier) 전극에서 $N_M$ 수치가 설계 마진을 초과하여 급등할 경우, 이를 **'급속 충전 화재 리스크'**로 발령하고 즉각 압연 갭(Roll Gap)을 상향 보정하여 공극률($\epsilon$)을 사수합니다.

## 4. [도메인 지식 결측 리스트 (Ingestion Request)]
**FidelityEngine**의 완전한 결정론적 추론을 위해, 이론적 모델을 현장과 동기화할 다음의 실측 데이터가 시스템에 결측되어 있습니다. (데이터 보강 필요)
*   **Req 1**: 고온 압연(Hot Pressing) 시 온도 편차 $\pm 1^\circ\text{C}$가 PVDF 바인더의 결정화도 및 전극 박리 강도(Peel Strength)에 미치는 실측 상관 로그
*   **Req 2**: 롤 프레스(Roll Press) 설비의 좌우 압하력(Line Force) 미세 편차에 기인한 전극 스프링백(Spring-back) 두께 산포 매핑 데이터
*   **Req 3**: 고용량 하이니켈(High-Ni) 양극재 다결정(Polycrystal) 입자의 압연 크랙 발생 임계 압력 및 2차 전해액 소모량 누적 데이터베이스

## 5. [코드 연결 해설: Electrode Density & Tiered Auditor]
이 코드는 타겟 배터리 종류(Tier)에 따른 압연 밀도 무결성을 진단합니다.

```python
class CalenderingTieredEngine:
    """
    HDS-Gold V6.3.7: 압연 공정 계층화 및 밀도 무결성 진단 엔진
    """
    def __init__(self, target_tier='High-end'):
        self.TIER = target_tier
        # 최상급 전극은 0.01g/cc 수준의 편차만 허용
        self.DENSITY_TOLERANCE = 0.01 if target_tier == 'High-end' else 0.05

    def audit_pressing_quality(self, measured_density, target_density):
        """
        밀도 등급 기반 압연 무결성 평가
        """
        error = abs(measured_density - target_density)
        fidelity_score = 1.0 - (error / self.DENSITY_TOLERANCE)
        
        status = "OPTIMAL"
        if error > self.DENSITY_TOLERANCE: 
            status = f"CRITICAL_DENSITY_DEVIATION_FOR_{self.TIER}"
        elif error > 0.02 and self.TIER == 'High-end':
            status = "WARNING_PRECISION_DRIFT_IN_THICKNESS"
            
        return {
            "tier_compliance": "PASS" if fidelity_score > 0 else "FAIL",
            "density_fidelity": max(fidelity_score, 0),
            "status": status
        }

# FidelityEngine 가동: 실제 전극의 박리 강도(Peel Strength) 데이터와 롤 압하력을 결합하여 '계면 접착 무결성' 오딧
```

## 6. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 실리콘 음극 공정에서 밀도 편차 $\pm 0.01\text{g/cc}$ 유지가 Tier 1 필수 요건인 이유는? (힌트: 실리콘 입자의 불균일한 팽창 응력이 전극 탈리 및 수명 급감에 미치는 영향)
2. **Operational Result**: 롤 온도를 $140^\circ\text{C}$ 이상으로 높였을 때, **바인더 마이그레이션(Migration)** 억제 효과가 전극의 **'수직적 균일도'** 무결성에 미치는 수리적 변화는?
3. **FidelityEngine**: **Hertzian Stress** 모델을 통해 다결정 양극재의 **'미세 균열($Micro-crack$)'** 발생 확률을 실시간으로 계산하고 롤 갭을 제어하는 방식은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Battery electrode-tortuosity-and-permeability-control
- synthesis-calendering-and-contact-mechanics
- MOC 82_advanced-battery-systems-hub

**[V6.3.7_SUB_ENTITY_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
