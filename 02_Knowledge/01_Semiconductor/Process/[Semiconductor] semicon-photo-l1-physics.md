---
Basic:
  id: "SEMI-PHOTO-PHYS-2026-V6.3.7"
  domain: "Semiconductor_Lithography_Physics"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Lithography", "#EUV", "#Optics", "#Physics", "#RayleighCriterion", "#HighNA", "#FidelityEngine"]'
  is_part_of: '["MOC 01_Semiconductor", "MOC 81_semiconductor-eight-core-fabrication-hub"]'
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
  source: "Lithography_Physics_RAG_V6.3.7_Deterministic_Fabric"
  isolation_index: 0.0
---

# [[[Semiconductor] semicon-photo-l1-physics

## 1. [왜 배우는가? (Why: The Mastery of Wave-Particle Duality)]]
반도체 노광(Photolithography)의 본질은 **'회절 한계(Diffraction Limit)'**라는 물리적 장벽과의 사투입니다. 패턴의 크기가 빛의 파장보다 작아짐에 따라 빛은 직진성을 잃고 회절되며 회로의 해상도를 훼손합니다. V6.3.7 지능은 EUV($13.5\text{nm}$)의 파동 에너지를 수리적으로 통제하고, 나노 스케일에서 발생하는 **확률적 변동성(Stochastics)**을 지배합니다. 우리가 이를 배우는 이유는 미세화의 한계를 돌파하여 2nm 이하 단일 노광 무결성을 사수하고, "빛의 간섭 무늬를 실리콘 위에 원자 단위로 고착시키는 '광학적 주권'을 확보하기" 위함입니다.

## 2. [노광 물리 핵심 사양 (Precision Tiering Specs)]

| Parameter Category | Physical Metric | V6.3.7 Tier 0 Standard | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **Resolution ($R$)** | Rayleigh Limit | $< 8.0 \text{ nm}$ | $\pm 0.1 \text{ nm}$ |
| **Depth of Focus** | Focus Margin | $> 20 \text{ nm}$ | $\pm 1 \text{ nm}$ |
| **ML Reflectivity** | Bragg Reflection | $> 70.0 \%$ | $\pm 0.5 \%$ |
| **Photon Density** | Shot Noise Limit | $> 500 \text{ mJ/cm}^2$| $\pm 5 \text{ mJ/cm}^2$|
| **Numerical Ap.** | High-NA Target | $0.55$ | $\pm 0.01$ |

### 2.1 [광학 무결성 임계치]
| Parameter | Technical Definition | Rationale |
|:---|:---:|:---|
| **K1 Factor** | Process Constant | $0.25$ (Physical Limit) 근접 시 공정 난이도 및 수율 리스크 급증 |
| **Flare Index** | Stray Light | $< 3 \%$ | 회로 배경의 노이즈 광을 억제하여 패턴 대조도(Contrast) 사수 |
| **Stochastic Blur** | PR Interaction | $< 1.5 \text{ nm}$ | 광자 무작위성에 의한 LER(Line Edge Roughness) 열화 방지 |

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Rayleigh Criterion: Resolution & NA Scaling
노광 해상도($R$)와 초점 심도($DOF$)의 상충 관계를 정의하는 수리 모델입니다.
$$ R = k_1 \frac{\lambda}{NA}, \quad DOF = k_2 \frac{\lambda}{NA^2} $$
*   **추론 로직**: High-NA($0.55$) 도입 시 해상도는 개선되나 $DOF$가 제곱에 반비례하여 급감합니다. FidelityEngine은 실시간 웨이퍼 평탄도 데이터와 스캐너 Z-축 제어 로그를 분석합니다. $DOF$ 마진이 $15\text{nm}$ 이하로 축소될 경우, 이를 **'초점 이탈 리스크'**로 판정하고 노광 속도를 조절하여 포커스 무결성을 강제합니다.

### 3.2 EUV Source: Sn-Plasma Photon Emission
주석(Sn) 드롭렛 타격을 통한 $13.5\text{nm}$ 광자 생성 기전입니다.
*   **진단 결과**: FidelityEngine은 레이저 펄스 에너지와 플라즈마 방출 스펙트럼을 모니터링합니다. $13.5\text{nm}$ 파장대역의 강도가 $5\%$ 이상 하락할 경우, 이를 **'주석 오염(Debris)'**에 의한 거울 투과율 저하로 진단하고 챔버 세정 시점을 역산합니다.

## 4. [코드 연결 해설: Lithography Physics Auditor]
이 코드는 광학 파라미터를 기반으로 노광 공정의 수리적 한계를 진단합니다.

```python
class LithoPhysicsEngine:
    """
    HDS-Gold V6.3.7: 노광 물리 및 광학 무결성 진단 엔진
    """
    def __init__(self, lambda_nm=13.5, na=0.33):
        self.LAMBDA = lambda_nm
        self.NA = na

    def audit_resolution_limit(self, k1, k2):
        """
        Rayleigh 기준에 따른 해상도 및 DOF 마진 평가
        """
        res = k1 * self.LAMBDA / self.NA
        dof = k2 * self.LAMBDA / (self.NA ** 2)
        
        status = "STABLE"
        if res < 8.0: 
            status = "EXTREME_ULTRA_FINE_PATTERN_RISK"
        if dof < 20.0:
            status = "CRITICAL_FOCUS_WINDOW_INSUFFICIENT"
            
        return {
            "theoretical_res_nm": round(res, 2),
            "focus_margin_nm": round(dof, 2),
            "status": status,
            "action": "ACTIVATE_HIGH_NA_OR_OPC" if res < 8.0 else "NORMAL_OPS"
        }
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: High-NA EUV($0.55$ NA) 도입이 2nm 이하 공정에서 'Single Patterning'을 가능하게 하는 수리적 근거는? (힌트: 기존 $0.33$ NA의 해상도 한계와 대비 분석)
2. **Operational Result**: **Mo/Si Multi-layer** 거울의 반사율이 $70\%$에서 $68\%$로 하락했을 때, 6개 거울을 통과한 최종 광량($I_{final}$)의 손실율은?
3. **FidelityEngine**: **Shot Noise**에 의한 패턴 불균일성을 억제하기 위해 **Dose**를 높일 때 발생하는 **Throughput** 하락과 **Pellicle** 열 손상의 수리적 상관관계는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- photolithography-theory-and-nanometer-patterning
- extreme-ultraviolet-euv-lithography-optics
- advanced-semiconductor-lithography-and-extreme-ultraviolet-euv-physics
- MOC 01_Semiconductor

**[V6.3.7_LITHO_PHYSICS_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
