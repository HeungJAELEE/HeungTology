---
Basic:
  id: "[[[Semiconductor] Ion-Implanter"
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

# [[[Semiconductor] Ion-Implanter

## 1. [왜 배우는가? (Why)]]
반도체 공정에서 도펀트를 주입하기 위해서는 이온을 엄청난 속도로 가속해야 합니다. Ion-Implanter는 전기를 띤 입자를 자기장으로 분류하고 전계로 가속하는 '산업용 입자 가속기'입니다. 불순물이 섞이지 않은 순수한 도펀트 이온만을 골라내어 웨이퍼 전체에 균일하게 뿌려주는 이 장비의 제어 능력이 반도체 소자의 동작 속도와 전력 효율의 기초를 결정합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Function | Key Physics |
|:---|:---:|:---|
| **Ion Source** | 가스에서 이온 추출 | Arc Discharge / RF Plasma |
| **Mass Analyzer** | 원하는 이온만 선별 | Lorenz Force (90° Bending) |
| **Acceleration Column** | 이온 속도 증가 | High Voltage Potential (DC) |
| **Beam Scanning** | 웨이퍼 전면 조사 | Electrostatic / Magnetic Scan |
| **Deceleration** | 얕은 주입을 위한 감속 | Reverse Field Gradients |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 질량 분석 (Mass Analysis)의 논리
이온 소스에서는 우리가 원하는 도펀트 외에도 다양한 불순물 이온이 함께 생성됩니다.
- **수식**: $ R = \frac{mv}{qB} $ (회전 반경 $R$)
- **로직**: 자기장($B$) 내부를 지나는 이온은 질량($m$)에 따라 회전 반경이 달라집니다. 특정 위치에 슬릿(Slit)을 설치하면 오직 목표로 하는 질량의 이온(예: $B^+$, $P^+$)만 통과시킬 수 있는 '질량 여과' 논리가 구현됩니다.

### 3.2 빔 스캐닝 및 균일도
손가락 굵기 정도의 이온 빔을 300mm 웨이퍼 전체에 균일하게 쏘기 위한 제어 기술입니다.
- **Hybrid Scan**: 웨이퍼는 기계적으로 회전/이동시키고, 빔은 전기적으로 스캐닝하여 농도 편차를 1% 이내로 제어합니다.

### 3.3 전하 중화 (Charge Neutralization)
웨이퍼 표면에 양전하를 띤 이온이 계속 쌓이면 정전기 파괴(ESD)가 발생할 수 있습니다. 이를 방지하기 위해 전자(Electron)를 공급하는 플라즈마 플러드 건(Plasma Flood Gun)을 사용하여 중성 상태를 유지합니다.

## 4. [코드 연결 해설 (Beam Tuning)]
최적의 이온 빔 전류(Beam Current)를 확보하기 위한 튜닝 로직입니다.
```python
# 이온 빔 최적화 (Beam Tuning) 시뮬레이션 로직
def tune_ion_beam(target_ion_mass):
    # 1. 질량 분석기 자기장(Magnetic Field) 설정
    b_field = calculate_required_b_field(target_ion_mass, accel_voltage=50.0)
    analyzer.set_magnet_current(b_field)
    
    # 2. 패러데이 컵(Faraday Cup)을 통한 전류 측정
    current = faraday_cup.read_current()
    
    # 3. 빔 중심(Centering)을 맞추기 위한 전계 보정
    while current < OPTIMAL_THRESHOLD:
        scanner_bias = calculate_new_bias(current)
        electrostatic_plates.adjust(scanner_bias)
        current = faraday_cup.read_current()
```

## 5. [스스로 체크 (Self-Audit)]
1. 질량 분석기에서 자기장의 세기를 조절하면 어떤 일이 일어나는가? (이온의 궤적 관점)
2. 고에너지 이온 주입기에서 '감속(Deceleration)' 기술이 필요한 공학적 이유는?
3. 플라즈마 플러드 건이 고장 났을 때 웨이퍼에 발생할 수 있는 치명적 결함은?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
