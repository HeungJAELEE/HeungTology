---
Basic:
  id: "[[[Semiconductor] Track-System"
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

# [[[Semiconductor] Track-System

## 1. [왜 배우는가? (Why)]]
노광 장비가 빛을 쏘아 그림을 그리는 '펜'이라면, 트랙 시스템은 종이(웨이퍼)에 잉크(감광액)를 고르게 바르고, 다 그려진 그림을 선명하게 나타나게 하는(현상) '전후처리기'입니다. 노광 장비와 하나의 시스템으로 연결되어(In-line), 수천 장의 웨이퍼를 끊임없이 처리하며 감광액의 두께 균일도와 현상 정밀도를 유지합니다. 트랙 장비의 성능이 곧 노광 전체 공정의 수율(Yield)과 생산성(Throughput)을 결정짓는 핵심 변수가 됩니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | Coater Unit | Developer Unit | Hot Plate (Bake) |
|:---|:---:|:---:|:---:|
| **Spin Speed** | 1,000 ~ 6,000 RPM | 500 ~ 2,000 RPM | N/A |
| **Thickness Unif.** | < 1 nm ($3\sigma$) | N/A | N/A |
| **Temp Control** | $\pm 0.1$ °C | $\pm 0.1$ °C | $\pm 0.05$ °C |
| **Developer Type** | N/A | Puddle / Spray | N/A |
| **Throughput** | 250 ~ 300 WPH | 250 ~ 300 WPH | In-line Synced |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 스핀 코팅 (Spin Coating)의 유체 역학
웨이퍼를 고속 회전시켜 원심력으로 감광액(PR)을 얇게 펴는 과정입니다.
- **로직**: 감광액의 점도(Viscosity)와 회전 속도(RPM)가 박막 두께를 결정합니다.
- **수식**: $ T \propto \omega^{-1/2} $ ($T$: 두께, $\omega$: 각속도). 고속 회전 시 용매(Solvent)의 증발 속도 또한 최종 두께 균일도에 큰 영향을 미칩니다.

### 3.2 베이크 (Bake) 공정의 화학적 로직
- **PAB (Pre-Applied Bake)**: 코팅 후 용매를 제거하여 PR을 고형화.
- **PEB (Post Exposure Bake)**: 노광 후 산(Acid)의 확산을 유도하여 화학적 증폭(CAR)을 완성.
- **로직**: PEB 온도의 1도 차이는 선폭(CD) 수 나노미터의 변화를 초래하므로, 정밀한 온도 균일도가 생명입니다.

### 3.3 현상 (Developing) 및 Puddle 방식
노광된 영역(Positive) 또는 노광되지 않은 영역(Negative)을 화학 용액으로 씻어내는 과정입니다.
- **Puddle Method**: 웨이퍼 위에 현상액을 웅덩이(Puddle)처럼 띄워 표면 장력을 이용해 균일한 반응을 유도하는 방식이 주로 사용됩니다.

## 4. [코드 연결 해설 (Sequence Optimization)]
트랙 장비 내의 로봇 암(Robot Arm) 스케줄링 및 공정 파라미터 제어 논리입니다.
```python
# 트랙 장비 내 웨이퍼 핸들링 및 베이크 시간 제어
def handle_track_sequence(wafer_id):
    # 1. Coater: PR 도포 (RPM 제어)
    spin_coater.start(rpm=3500, ramp_up=1.5)
    
    # 2. PAB: 용매 제거 (온도 및 시간 엄격 준수)
    hot_plate.bake(temp=110.0, duration=90.0)
    
    # 3. Interface to Scanner: 노광기로 이송
    track_robot.transfer_to_scanner(wafer_id)
    
    # 4. PEB: 노광 후 베이크 (확산 제어)
    hot_plate.bake(temp=105.0, duration=60.0)
    
    # 5. Developer: 현상 공정
    developer.apply_puddle(time=45.0)
```

## 5. [스스로 체크 (Self-Audit)]
1. 스핀 코팅 중 회전 속도(RPM)를 높였을 때 박막 두께가 얇아지는 물리적 원인은?
2. PEB(Post Exposure Bake) 온도가 타겟보다 높게 설정되었을 때 패턴의 선폭(CD)은 어떻게 변하겠는가? (Positive PR 기준)
3. 트랙 장비와 노광기가 인라인(In-line)으로 연결되어야만 하는 공학적 필연성은 무엇인가? (Queue Time 관리 측면)

---
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
