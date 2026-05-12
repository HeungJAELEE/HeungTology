---
Basic:
  id: "[[[Semiconductor] 3D-NAND"
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

# [[[Semiconductor] 3D-NAND

## 1. [왜 배우는가? (Why)]]
데이터 스토리지의 밀도를 높이기 위해 기존 2D(Planar) 구조에서 발생하던 셀 간 간섭(Cell-to-Cell Interference)을 해결하는 유일한 물리적 해답이 3D-NAND입니다. 수직으로 셀을 쌓아 올림으로써 물리적 한계를 극복하고, 단위 면적당 비트(Bit) 용량을 기하급수적으로 늘려 현대의 데이터 센터와 모바일 스토리지 혁명을 가능케 했습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | 232L Class | 300L+ (Target) | 400L+ (Future) |
|:---|:---:|:---:|:---:|
| **Layer Count** | 232 ~ 238 Layers | 300 ~ 320 Layers | 400 Layers + |
| **I/O Speed** | 2.4 Gbps | 3.2 Gbps | 4.0 Gbps |
| **Etch Aspect Ratio** | 60:1 | 75:1 | 90:1 + |
| **Stacking Logic** | Double Stack | Triple Stack | Multi-Stack (4+) |
| **Areal Density** | ~14 Gbit/mm² | ~20 Gbit/mm² | ~28 Gbit/mm² |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 HAR (High Aspect Ratio) Etching 및 채널 홀 논리
수백 층의 박막을 한꺼번에 뚫는 HAR 식각은 3D-NAND 제조의 극강의 난이도입니다.
- **로직**: 구멍이 깊어질수록 식각 가스의 유입과 부산물의 배출 속도가 저하되는 **Aspect Ratio Trap**이 발생합니다. 이를 극복하기 위해 극저온 식각(Cryogenic Etching) 및 플라즈마 제어 로직이 적용됩니다.

### 3.2 String Stacking (분할 적층)
단일 식각의 물리적 한계를 분할하여 해결하는 논리입니다.
- **수식**: 총 층수 $ L_{total} $이 단일 식각 한계 $ L_{limit} $을 초과할 때, $ n = \lceil L_{total} / L_{limit} \rceil $ 개의 데크(Deck)로 나누어 적층한 뒤 수직으로 연결합니다. 현재 300층 이상에서는 Triple Stack 이상이 필수적입니다.

### 3.3 CTF (Charge Trap Flash) 및 전하 제어
전하를 부도체 층에 가둠으로써 셀 두께를 얇게 유지하고 인접 셀 간의 전계 영향을 최소화합니다.

## 4. [코드 연결 해설 (FTL & Reliability)]
```c
// FTL 내의 수직 적층 오차 보정 논리
void adjust_write_voltage(int block_layer) {
    // 적층 하단부와 상단부의 채널 홀 직경 차이(Tapering)에 따른 전압 보정
    float v_comp = (block_layer < BOTTOM_LIMIT) ? 0.05 : 0.0;
    apply_vth_correction(v_comp);
}
```

## 5. [스스로 체크 (Self-Audit)]
1. 3D-NAND에서 'String Stacking'이 층수 증가에 따라 필수가 되는 공학적 이유는?
2. HAR Etching 공정에서 발생하는 'Bowing' 현상이 데이터 정합성에 미치는 영향은?
3. CTF 방식이 기존 Floating Gate 방식 대비 적층 고도화에 유리한 점은 무엇인가?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
