---
Basic:
  id: "[[[Semiconductor] Dry-Etcher"
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

# [[[Semiconductor] Dry-Etcher

## 1. [왜 배우는가? (Why)]]
나노미터 단위의 회로 패턴을 형성하기 위해서는 수평 방향의 식각을 억제하고 수직 방향으로만 깎아내는 '이방성(Anisotropy)' 식각이 필수적입니다. 용액을 사용하는 습식 식각(Wet Etch)은 사방으로 깎이는 특성 때문에 미세 패턴 구현이 불가능합니다. Dry-Etcher는 플라즈마 상태의 이온과 라디칼을 제어하여, 나노미터 급의 선폭을 정밀하게 조각해내는 반도체 공정의 핵심 도구입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | CCP (Capacitively Coupled) | ICP (Inductively Coupled) | ALE (Atomic Layer Etch) |
|:---|:---:|:---:|:---:|
| **Plasma Density** | Moderate ($10^9 \sim 10^{11} cm^{-3}$) | High ($10^{11} \sim 10^{12} cm^{-3}$) | Atomic Precise |
| **Ion Energy Control** | Difficult (Coupled) | Excellent (Decoupled) | Extreme (Pulse) |
| **Selectivity** | Moderate | High | Infinite (Theoretical) |
| **Anisotropy** | High | High | Atomic Level |
| **Application** | Dielectric Etch (Hard) | Conductor/Silicon Etch | 2nm Logic / 3D-NAND |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 플라즈마 식각의 시너지 로직 (Ion-Assisted Etching)
건식 식각은 화학적 라디칼 반응과 물리적 이온 충격의 조합입니다.
- **로직**: 라디칼만 있으면 등방성(Isotropic) 식각이 되고, 이온만 있으면 선택비(Selectivity)가 낮아집니다. 이온이 바닥면을 때려 화학 결합을 약화시키면, 라디칼이 그 자리에서 반응하여 휘발성 물질을 만들어내는 시너지 논리를 통해 수직 방향의 높은 식각 속도를 확보합니다.

### 3.2 ALE (Atomic Layer Etch) 및 분할 제어
원자 층 단위로 깎아내는 차세대 식각 로직입니다.
1. **Surface Modification**: 가스를 주입하여 표면에 반응 층을 형성 (Self-limiting).
2. **Removal**: 저에너지 이온을 충격하여 변형된 원자 한 층만 제거.
- **장점**: 식각 손상(Damaged Layer)을 획기적으로 줄이고, 원자 단위의 깊이 조절이 가능합니다.

### 3.3 플라즈마 발생 방식: CCP vs ICP
- **CCP**: 두 평행 전극 사이에 강한 전계를 걸어 플라즈마를 발생. 이온 에너지가 높아 단단한 절연막 식각에 유리.
- **ICP**: 코일을 통해 유도 자기장을 걸어 플라즈마를 발생. 밀도가 높고 이온 에너지와 밀도를 독립적으로 제어 가능하여 미세 실리콘 식각에 유리.

## 4. [코드 연결 해설 (Endpoint Detection Logic)]
식각이 끝나는 시점을 감지하는 EPD(Endpoint Detection) 알고리즘입니다.
```python
# 광학 센서(OES) 기반 식각 종료 시점(EPD) 감지 로직
def detect_etch_endpoint(wavelength_data):
    # 식각 부산물(By-product) 가스의 특정 파장 강도 모니터링
    intensity = extract_intensity(wavelength_data, target_nm=440.5) # 예: SiF4 파장
    
    # 부산물 농도가 급격히 낮아지면 하부 층(Stop Layer) 노출로 간주
    if calculate_slope(intensity) < ENDPOINT_THRESHOLD:
        stop_plasma_power()
        initiate_over_etch_sequence(duration=2.0) # 잔여물 제거를 위한 추가 식각
        return "SUCCESS"
```

## 5. [스스로 체크 (Self-Audit)]
1. 습식 식각(Wet Etch)이 미세 패턴 형성에 불리한 물리적 이유는 무엇인가? (Anisotropy 관점)
2. ALE 기술이 기존 RIE(Reactive Ion Etch) 대비 가지는 공학적 우위는 무엇인가?
3. ICP 식각 장비가 CCP 대비 미세 공정 제어에 유리한 이유는 무엇인가?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
