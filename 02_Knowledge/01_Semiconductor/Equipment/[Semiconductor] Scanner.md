---
Basic:
  id: "[[[Semiconductor] Scanner"
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

# [[[Semiconductor] Scanner

## 1. [왜 배우는가? (Why)]]
현대 반도체 제조에서 회로를 그리는 노광 장비의 주력은 스테퍼(Stepper)가 아닌 스캐너(Scanner)입니다. 스테퍼가 한 샷(Shot)씩 찍고 이동하는 방식이라면, 스캐너는 렌즈의 가장 선명한 부분만을 사용하여 마스크와 웨이퍼를 동시에 스캔함으로써 더 넓은 면적을 더 정밀하게 그려냅니다. 특히 7nm 이하의 미세 공정을 가능케 하는 EUV 스캐너는 인류가 만든 가장 정교한 장비 중 하나로, 국가적 차원의 핵심 자산입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Feature | Stepper (Legacy) | DUV Scanner | EUV Scanner (Next) |
|:---|:---:|:---:|:---:|
| **Operation Mode** | Step-and-Repeat | Step-and-Scan | Step-and-Scan (Vacuum) |
| **Exposure Field** | Limited by Lens | Large (Scanning) | Optimized for Reflective |
| **Overlay Accuracy** | ~10 nm | < 2 nm | < 1 nm |
| **Scanning Speed** | N/A | 600 ~ 800 mm/s | 1000 mm/s + |
| **Light Source** | i-line / KrF | ArF / ArF-i | EUV (13.5 nm) |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 Step-and-Scan 메커니즘의 우위
스캐너는 렌즈의 중앙부(가장 수차가 적은 부분)에 좁은 슬릿(Slit) 모양의 빛을 쏘고, 마스크(Reticle) 스테이지와 웨이퍼 스테이지를 정교하게 동기화하여 이동시키며 패턴을 완성합니다.
- **로직**: 이 방식을 통해 렌즈의 크기를 키우지 않고도 더 큰 노광 면적(Exposure Field)을 확보할 수 있으며, 렌즈 가장자리에서 발생하는 광학적 왜곡(Aberration)을 최소화할 수 있습니다.

### 3.2 동기화 및 스테이지 제어 (Sync & Mechatronics)
마스크 스테이지와 웨이퍼 스테이지는 렌즈 배율에 따라 일정한 비율(보통 4:1)로 반대 방향으로 이동해야 합니다.
- **수식**: $ V_{mask} = M \times V_{wafer} $ ($M$: 렌즈 축소 배율)
이때 발생하는 수 나노미터 단위의 동기화 오차조차 허용되지 않으므로, 자기 부상(Maglev) 스테이지와 레이저 간섭계(Laser Interferometer) 기반의 정밀 제어가 수반됩니다.

### 3.3 EUV 스캐너의 광학적 도전
EUV 스캐너는 빛이 유리 렌즈에 흡수되는 특성 때문에 다층막(Multi-layer) 반사 거울을 사용하며, 모든 광학 경로는 진공 상태에서 이루어집니다.

## 4. [코드 연결 해설 (Overlay Control)]
스캐너의 패턴 정렬 오차(Overlay Error)를 보정하는 제어 논리입니다.
```python
# 스캐너 레이아웃 오차 보정 알고리즘 (Overlay Correction)
def calculate_scanner_offsets(metrology_data):
    # 계측 장비로부터 전달받은 이전 레이어와의 정렬 오차 분석
    dx, dy = extract_alignment_error(metrology_data)
    
    # 웨이퍼 스테이지의 X, Y 좌표 및 회전(Theta) 보정값 산출
    correction_x = -dx * PID_GAIN
    correction_y = -dy * PID_GAIN
    
    # 스캐너 제어기로 보정값 전송
    scanner_controller.apply_stage_bias(correction_x, correction_y)
    
    # 고차 다항식(High-order Correction)을 통한 웨이퍼 뒤틀림 보정
    apply_wafer_expansion_compensation(metrology_data.temperature)
```

## 5. [스스로 체크 (Self-Audit)]
1. 스캐너가 스테퍼 대비 대면적 노광에 유리한 구조적 이유는 무엇인가?
2. 마스크와 웨이퍼 스테이지의 동기화 오차가 발생했을 때, 패턴의 CD(Critical Dimension)에는 어떤 영향이 있겠는가?
3. EUV 스캐너가 기존 DUV 스캐너와 달리 거울(Mirror) 시스템을 채택해야만 했던 물리적 필연성은?

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
