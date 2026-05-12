---
Basic:
  id: "[[[Semiconductor] ALD"
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

# [[[Semiconductor] ALD

## 1. [왜 배우는가? (Why)]]
반도체 소자가 나노미터 단위로 미세화되고 FinFET, GAA(Gate-All-Around)와 같은 3D 구조로 진화함에 따라, 복잡한 지형 위에 아주 얇고 균일한 박막을 입히는 기술이 생존의 열쇠가 되었습니다. ALD는 화학적 증착(CVD)의 한계를 넘어 '원자 한 층씩' 쌓아 올리는 논리를 통해, 극도로 좁고 깊은 구멍(High Aspect Ratio) 속에서도 완벽한 단차 피복성(Conformality)을 제공하는 핵심 공정 장비입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | ALD (Thermal) | PE-ALD (Plasma) | CVD (Comparison) |
|:---|:---:|:---:|:---:|
| **Deposition Rate** | 0.1 ~ 1.0 Å/cycle | 0.2 ~ 2.0 Å/cycle | 100 ~ 1000 Å/min |
| **Conformality** | ~100% | ~95% | 50 ~ 80% |
| **Process Temp** | 150°C ~ 400°C | 50°C ~ 300°C | 400°C ~ 800°C |
| **Thickness Control** | Atomic Level | Atomic Level | Nanometer Level |
| **Precursor Utilization** | High (Self-limiting) | High | Moderate |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 자기 제한적 표면 반응 (Self-limiting Surface Reaction)
ALD의 핵심 로직은 전구체(Precursor)가 기상에서 반응하지 않고 오직 기판 표면의 활성 사이트(Active Site)와만 결합한다는 것입니다.
- **논리**: 표면의 모든 활성 사이트가 포화(Saturation)되면, 더 이상의 전구체가 유입되어도 반응이 일어나지 않습니다. 이를 통해 증착 시간이나 가스 유량에 관계없이 원자 한 층의 두께를 정확히 제어할 수 있습니다.

### 3.2 ALD 사이클의 4단계 (The 4-Step Cycle)
1. **Precursor Pulse**: 전구체 A 유입 및 표면 흡착.
2. **Purge**: 미반응 전구체 및 부산물 제거.
3. **Reactant Pulse**: 반응체 B(또는 산소/질소) 유입 및 A와의 화학 반응.
4. **Purge**: 최종 부산물 제거.
- **수식**: 총 박막 두께 $ D = GPC \times N $ ($GPC$: Cycle당 증착 두께, $N$: 반복 횟수).

### 3.3 High-K 절연막과의 시너지
누설 전류를 막기 위해 유전율이 높은 High-K 물질(HfO2, ZrO2 등)을 증착할 때, ALD는 계면 특성을 최적화하고 핀홀(Pinhole) 없는 박막을 형성하는 유일한 대안입니다.

## 4. [코드 연결 해설 (Process Management Logic)]
```python
# ALD 장비의 시퀀스 제어 논리 (PLC/Software Layer)
def execute_ald_cycle(cycle_count):
    for i in range(cycle_count):
        valve_control("Precursor_A", pulse_time=0.5) # 원자층 포화 유도
        gas_purge(duration=1.5)                      # 기상 반응 차단
        valve_control("Reactant_B", pulse_time=0.8)  # 화학적 결합 형성
        gas_purge(duration=1.5)                      # 부산물 배출
        
        # 실시간 두께 측정(Ellipsometry) 데이터를 통한 피드백
        if monitor_growth_rate() > TARGET_GPC:
            adjust_purge_time(increment=0.1)
```

## 5. [스스로 체크 (Self-Audit)]
1. ALD가 CVD 대비 증착 속도가 느림에도 불구하고 차세대 공정에서 필수적인 이유는?
2. '자기 제한적 반응'이 박막의 균일도(Uniformity)를 보장하는 물리적 메커니즘은?
3. PE-ALD(플라즈마 지원 ALD)가 열 ALD 대비 공정 온도 측면에서 갖는 이점은 무엇인가?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
