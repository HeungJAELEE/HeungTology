---
Basic:
  id: "SEMI-DEP-DOP-2026-V6.3.7"
  domain: "Semiconductor_Deposition_and_Doping_Physics"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Deposition", "#IonImplantation", "#ALD", "#Doping", "#GAA", "#FidelityEngine", "#FEOL"]'
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
  source: "Deposition_Doping_RAG_V6.3.7_Deterministic_Fabric"
  isolation_index: 0.0
---

# [[[Semiconductor] semicon-feol-l1-film-and-doping

## 1. [왜 배우는가? (Why: The Mastery of Atomic Architecture)]]
FEOL(Front-End of Line) 공정에서 **증착(Deposition)**은 트랜지스터의 구조적 뼈대를 형성하는 '원자층 적층'이며, **이온주입(Ion Implantation)**은 부도체인 실리콘에 전하 운반체(Dopant)를 심어 '전기적 생명'을 불어넣는 행위입니다. V6.3.7 지능은 **원자층 증착(ALD)**의 자기 제한적 반응과 이온의 **비정(Range)** 분포를 수리적으로 지배합니다. 우리가 이를 배우는 이유는 GAA(Gate-All-Around)와 같은 초미세 구조에서 단 한 층의 원자 오차가 소자의 누설 전류와 동작 속도를 결정짓기 때문이며, "물질의 배치를 나노 단위로 완벽히 통제하는 '제조 무결성'을 사수하기" 위함입니다.

## 2. [증착 및 도핑 핵심 사양 (Precision Tiering Specs)]

| Process Category | Key Parameter | V6.3.7 Tier 0 Standard | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **ALD Deposition** | GPC (Growth Per Cycle) | $1.0 \text{ \AA/cycle}$ | $\pm 0.05 \text{ \AA}$ |
| **Step Coverage** | AR $> 100:1$ | $\approx 100 \%$ | $\pm 0.5 \%$ |
| **Ion Implantation**| Range ($R_p$) | Target Depth $\pm 2\text{nm}$| $\pm 0.2 \text{ nm}$ |
| **Dopant Dose** | Concentration | $10^{11} \sim 10^{16} \text{ cm}^{-2}$| $\pm 1 \%$ |
| **Annealing** | Activation Rate | $> 99 \%$ | $\pm 0.1 \%$ |

### 2.1 [박막 및 접합 무결성 임계치]
| Parameter | Technical Definition | Rationale |
|:---|:---:|:---|
| **Uniformity** | Thickness Variation | $< 1.0 \%$ | 웨이퍼 전면의 소자 특성 균일도를 사수하기 위한 ALD 제어 한계 |
| **Straggle ($\Delta R_p$)**| Distribution Width | Minimum | 정션(Junction)의 수직적 날카로움을 유지하여 단채널 효과 방지 |
| **Thermal Budget**| Anneal Heat Load | $< 1,000 ^\circ\text{C}\cdot\text{s}$ | 도펀트의 과도 확산(TED)을 억제하여 설계된 도핑 프로파일 사수 |

## 3. [공학적 근거 (Scientific Rationale) 및 FidelityEngine 로직]

### 3.1 [ALD 동역학($ALD\ Kinetics$)과 자기 제한 흡착 모델]
원자 단위로 막을 쌓을 때 왜 두께가 제멋대로 자라지 않는가?
*   **공학적 근거**: 전구체 가스와 웨이퍼 표면 사이의 화학적 흡착(Chemisorption) 평형 모델에 의해, 증착량($\theta(t)$)은 포화도($\theta_{sat}$)에 지수 함수적으로 수렴합니다($\theta(t) = \theta_{sat} (1 - e^{-kPt})$). 시간이 무한히 지나도 딱 한 층의 원자만 결합하므로, 아무리 복잡한 3D 패턴(GAA)이라도 $100\%$의 단차 피복성을 달성함을 수리적으로 입증합니다.
*   **FidelityEngine 적용 (ALD Physics)**: 증착 속도(GPC)가 목표치보다 낮을 경우, FidelityEngine은 펄스 시간($t$)과 가스 분압($P$) 데이터를 실시간 분석합니다. 표면 포화도($\theta$)가 $1.0$에 도달하지 못했을 경우, 이를 **'흡착 무결성 위기'**로 판정하고 펄스 시간을 즉시 Ramping하여 원자층 무결성을 강제합니다.

### 3.2 [LSS 이론($LSS\ Theory$)과 이온 정지능(Stopping Power) 역학]
빛의 속도로 날아간 이온은 어떻게 원하는 깊이에 정확히 멈추는가?
*   **공학적 근거**: 이온이 실리콘 격자 내에서 에너지를 잃고 멈추는 비정($R_p$)은 원자핵과의 충돌(Nuclear Stopping, $S_n$)과 전자와의 마찰(Electronic Stopping, $S_e$)의 역수에 대한 에너지 적분으로 도출됩니다($R_p = \int_0^{E_0} \frac{dE}{S_n(E) + S_e(E)}$). 이 수식을 통해 타겟 도펀트의 수직적 분포(Straggle)를 나노미터 단위로 조절합니다.
*   **FidelityEngine 적용 (Ion Transport Physics)**: 가속 전압($E_0$)과 이온 종으로부터 비정($R_p$)을 실시간 예측합니다. 측정된 전기적 저항(Rs)이 예측값과 다를 경우, 결정 구조의 방향성과 이온이 평행하게 나아가버리는 **'채널링(Channeling) 무결성 위기'** 또는 **'격자 손상 회복 미흡'**으로 진단하고 즉시 틸트(Tilt) 각도 및 어닐링 온도를 재계산합니다.

## 4. [도메인 지식 결측 리스트 (Ingestion Request)]
**FidelityEngine**의 완전한 결정론적 추론을 위해, 이론적 모델을 현장과 동기화할 다음의 실측 데이터가 시스템에 결측되어 있습니다. (데이터 보강 필요)
*   **Req 1**: ALD 공정 중 Precursor 분압($P$) 센서 및 펄스 시간($t$) 타임스탬프 로그 (1ms 주기)
*   **Req 2**: 공정 후 박막 두께(Ellipsometer) 및 GPC(Growth Per Cycle) 측정 결과 데이터셋
*   **Req 3**: 이온주입 장비의 가속 전압($E_0$), Dose 량 센서 로그 및 SIMS(Secondary Ion Mass Spectrometry) 깊이 프로파일 실측 데이터

## 5. [코드 연결 해설: Film & Doping Fidelity Auditor]
이 코드는 증착 및 도핑 데이터를 기반으로 소자의 구조적/전기적 무결성을 진단합니다.

```python
class FilmDopingEngine:
    """
    HDS-Gold V6.3.7: 박막 증착 및 도핑 무결성 진단 엔진
    """
    def __init__(self, target_gpc=1.0, target_rp=50.0):
        self.TARGET_GPC = target_gpc # Angstrom/cycle
        self.TARGET_RP = target_rp # nm

    def audit_feol_integrity(self, current_gpc, current_rp, uniformity):
        """
        GPC 및 Rp 기반 FEOL 무결성 평가
        """
        gpc_err = abs(current_gpc - self.TARGET_GPC) / self.TARGET_GPC
        
        status = "STRUCTURE_STABLE"
        if gpc_err > 0.05:
            status = "CRITICAL_ALD_SATURATION_VIOLATION"
        elif uniformity > 0.01:
            status = "WARNING_FILM_NON_UNIFORMITY_HIGH"
            
        return {
            "deposition_fidelity": round(1.0 - gpc_err, 4),
            "junction_precision": "PASS" if abs(current_rp - self.TARGET_RP) < 1.0 else "FAIL",
            "status": status,
            "action": "ADJUST_PULSE_TIME_OR_DOSAGE" if status.startswith("CRITICAL") else "NORMAL_OPS"
        }
```

## 6. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: GAA 공정에서 **ALD**의 단차 피복성(Step Coverage)이 $100\%$여야만 하는 수리적 이유는? (힌트: 나노시트 사이의 좁은 공간 내부로 전극 및 절연막이 침투해야 하는 물리적 제약)
2. **Operational Result**: 이온주입 후 **RTA (Rapid Thermal Annealing)** 시 시간이 너무 길어지면 발생하는 **TED (Transient Enhanced Diffusion)**가 소자의 단채널 효과에 미치는 수리적 영향은?
3. **FidelityEngine**: **Nuclear Stopping**과 **Electronic Stopping**의 비중이 이온의 가속 에너지에 따라 어떻게 변화하며, 이것이 최종 도핑 프로파일 형상($\Delta R_p$)에 미치는 영향은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- ion-implantation-and-dopant-diffusion-profiles-in-silicon
- atomic-layer-deposition-ald-and-surface-reaction-kinetics
- Semiconductor semiconductor-fabrication-master-guide
- MOC 81_semiconductor-eight-core-fabrication-hub

**[V6.3.7_SUB_ENTITY_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
