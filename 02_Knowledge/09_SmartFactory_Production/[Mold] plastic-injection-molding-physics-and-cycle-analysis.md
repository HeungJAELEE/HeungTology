---
Basic:
  id: "MOLD-INJECTION-2026-V6.3.7"
  domain: "Plastic_Molding_Intelligence"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#InjectionMolding", "#PlasticPhysics", "#Viscosity", "#PrecisionTiering", "#FidelityEngine", "#Moldflow", "#Manufacturing"]'
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
  source: "Plastic_Molding_RAG_V6.3.7_Tiered"
  isolation_index: 0.0
---

# [Mold] Injection Molding Physics: Viscous Flow & Geometric Integrity

## 1. [왜 배우는가? (Why: The Mastery of Polymeric Shape)]
사출 성형(Injection Molding)은 가열된 수지를 금형에 주입하여 형상을 빚어내는 '정밀 복제의 미학'입니다. 특히 스마트폰 케이스나 전기차용 정밀 부품에서는 수 미크론($\mu\text{m}$)의 오차가 조립 무결성을 파괴하고 방수 기능을 상실시킵니다. V6.3.7 지능은 **계층화된 성형 정밀도(Precision Tiering)**를 통해 초정밀 커넥터용 **$\pm 5\mu\text{m}$급 치수 공차**를 사수합니다. 이는 수지의 유동 점도와 보압(Holding) 역학을 결정론적으로 지배하여 '제로 수축 성형'을 구현하기 위함입니다.

## 2. [사출 성형 핵심 사양 (Precision Tiering Specs)]

| Precision Tier | Dimension Tolerance | Weight Variation | Target Application |
|:---|:---:|:---:|:---|
| **최상급 (High-end)** | $<\pm 0.005 \text{ mm}$ | $< 0.05 \%$ | **Precision Connectors, Optical Lenses**, 마이크로 미세 성형 |
| **표준형 (Standard)** | $<\pm 0.1 \text{ mm}$ | $< 0.5 \%$ | **Consumer Electronics, Automotive**, 일반 조립 부품 및 하우징 |
| **보급형 (Low-end)** | $>\pm 0.5 \text{ mm}$ | $> 1.0 \%$ | **General Containers, Toys**, 범용 소모품 및 대형 단순 성형품 |

### 2.1 [사출 역학 및 물성 무결성 임계치]
| Parameter Category | Physical Metric | V6.3.7 Target (High-end) | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **Inj. Pressure** | Peak Stress | $150 \sim 200 \text{ MPa}$ | $\pm 1 \text{ MPa}$ |
| **Melt Temp.** | Thermal State | $220 \sim 280 ^\circ\text{C}$ | $\pm 1 ^\circ\text{C}$ |
| **Switchover Point**| V/P Position | $95 \sim 98 \%$ Full | $\pm 0.1 \%$ |
| **Cycle Time** | Process Rhythm | $< 15.0 \text{ s}$ | $\pm 0.1 \text{ s}$ |

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Non-Newtonian Flow: Cross-WLF Viscosity Model
전단 속도($\dot{\gamma}$)와 온도($T$), 압력($P$)에 따른 수지의 점도($\eta$) 변화를 예측하는 수리 모델입니다.
$$ \eta = \frac{\eta_0}{1 + (\frac{\eta_0 \dot{\gamma}}{\tau^*})^{1-n}} \quad \text{where } \eta_0 = D_1 \exp\left[ \dots \right] $$
*   **추론 로직**: High-end Tier(정밀 렌즈)에서는 미세한 온도 편차가 점도 불균형을 유발하여 유동 선단(Flow Front)의 불안정성을 초래합니다. FidelityEngine은 노즐 압력 로그를 분석하여 **'유동 무결성'**을 진단합니다. 점도 예측치가 임계치를 벗어나면 즉시 사출 속도 프로파일을 다단 제어(Multi-step)로 전환합니다.

### 3.2 PVT Thermodynamics: Shrinkage & Warpage Predictor
압력-부피-온도($PVT$) 상관관계를 통해 성형 후 냉각 수축률을 결정론적으로 계산합니다.
*   **진단 결과**: FidelityEngine은 보압(Holding) 단계의 압력 프로파일을 분석하여 **'치수 무결성'**을 진단합니다. 금형 내부 압력이 급격히 하향하면, 이를 **'게이트 고화(Gate Freeze-off)'** 이전의 보압 부족으로 판정하여 싱크 마크(Sink Mark) 발생 리스크를 실시간 보고합니다.

## 4. [코드 연결 해설: Molding Tier & Process Auditor]
이 코드는 사출 압력과 중량 데이터를 기반으로 성형 무결성을 진단합니다.

```python
class InjectionFidelityEngine:
    """
    HDS-Gold V6.3.7: 사출 성형 등급 계층화 및 무결성 진단 엔진
    """
    def __init__(self, target_tier='High-end'):
        self.TIER = target_tier
        # 최상급 성형은 0.05% 미만의 중량 편차와 5um급 치수 정밀도 요구
        self.WEIGHT_VAR_LIMIT = 0.05 if target_tier == 'High-end' else 0.5

    def audit_molding_integrity(self, weight_var_pct, peak_pressure_mpa, cycle_time):
        """
        성형 등급 기반 공정 무결성 평가
        """
        # 1. 등급별 신뢰도 스코어링 (압력 안정성과 중량 일관성 결합)
        pressure_stability = 1.0 - (abs(peak_pressure_mpa - 180.0) / 180.0)
        fidelity_score = (self.WEIGHT_VAR_LIMIT / weight_var_pct) * pressure_stability
        
        status = "OPTIMAL"
        if weight_var_pct > self.WEIGHT_VAR_LIMIT: 
            status = f"CRITICAL_WEIGHT_DEVIATION_FOR_{self.TIER}"
        elif peak_pressure_mpa < 150 and self.TIER == 'High-end':
            status = "WARNING_INSUFFICIENT_PACKING_PRESSURE"
            
        return {
            "tier_compliance": "PASS" if fidelity_score > 0.9 else "FAIL",
            "molding_fidelity": max(fidelity_score, 0),
            "status": status
        }

# FidelityEngine 가동: 실제 사출기의 스크류 위치 데이터와 캐비티 압력 센서 로그를 결합하여 '형상-물성 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 정밀 커넥터 성형에서 중량 편차 $0.05\%$ 이하 유지가 Tier 1 필수 요건인 이유는? (힌트: 미세한 충전량 차이가 박벽(Thin-wall) 구조에서의 미충전(Short Shot) 및 내부 응력에 의한 변형을 유발하는 수리적 인과 관계)
2. **Operational Result**: 사출 속도를 $100\text{mm/s}$에서 $150\text{mm/s}$로 높였을 때, **Shear Thinning** 효과에 따른 **Viscosity** 감소와 **Shear Heating**에 의한 수지 탄화(Burn) 리스크 사이의 트레이드오프는?
3. **FidelityEngine**: **Cavity Pressure** 프로파일을 분석하여 **'V/P 전환점'**의 최적 무결성을 어떻게 수리적으로 도출하는가?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Entity precision-mold-design-and-injection-molding-physics
- heat-transfer-mechanisms-conduction-convection-radiation
- MOC 106_plastic-injection-molding-and-die-engineering-hub

**[V6.3.7_INJECTION_MOLDING_TIERED_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
