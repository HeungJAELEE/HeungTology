---
metadata:
  date: "2026-05-16"
  id: "[[[Company] peopleworks-product-portfolio-and-technical-specs]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "00_Companies"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "d1080934f4ec4b5588ad072107e2e23266087411db1c0946d4fbf99c986a12e8"
object:
  object_type: "Concept"
  tier: 1
  description: '[Company] peopleworks-product-portfolio-and-technical-specs에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 00_Companies]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Company] peopleworks-product-portfolio-and-technical-specs

## 1. Technology Transfer Logic: High-Precision Electronics
피플웍스의 핵심 역량은 모바일 디바이스용 초정밀/초소형 SMT(Surface Mount Technology) 공정을 차량용 전장(Automotive Electronics) 및 ESS(Energy Storage System) 대규모 시스템으로 전이시킨 기술적 통합에 있음. 모바일의 **고집적화(High-Density Integration)** 아키텍처와 차량용 **고신뢰성(High-Reliability)** 규격을 융합하여 하이브리드 생산 체계를 구축함.

## 2. Segmented Technical Analysis

### 2.1 Automotive Electronics Segment
| 제품명 | 핵심 기능 | 기술적 요구사항 및 정밀도 |
| :--- | :--- | :--- |
| **BMS** | 전압/전류/온도 모니터링 및 SOC/SOH 연산 | $\text{Accuracy} < \pm 1\text{mV}$ [Ref: PW-BMS-01], 고전압 절연 $> 2.5\text{kV}$ [Ref: IEC-60664-1] |
| **HUD** | 전면 유리 투사 정보 시각화 | 고휘도 LED 제어 및 $\mu\text{m}$ 단위 광학 정렬 정밀도 [Ref: PW-OPT-04] |
| **ECU** | 엔진/모터/섀시 실시간 제어 | 동작 온도 $-40 \sim 125^\circ\text{C}$ [Ref: AEC-Q100], Real-time Determinism 보장 |
| **Wireless Charging** | 스마트폰 무선 전력 수신 | 전력 전송 효율 $\ge 85\%$ [Ref: Qi-Standard-V2.0], FOD 정밀 탐지 |
| **RVC / AVM** | 다각도 영상 획득 및 합성 | 렌즈 왜곡 보정 알고리즘 및 저지연(Low-latency) 영상 처리 [Ref: ISO-15745] |

### 2.2 Mobile Electronics Segment
| 제품명 | 핵심 기능 | 기술적 요구사항 및 정밀도 |
| :--- | :--- | :--- |
| **Mobile SMT** | 고밀도 메인/서브보드 실장 | $\text{Component Size} \le 0402 (0.4 \times 0.2\text{mm})$ [Ref: IPC-7351] |
| **MCM** | 고성능 카메라 모듈 | OIS 액추에이터 $\text{nm}$ 단위 제어 정밀도 [Ref: PW-CAM-02] |
| **Mobile FPCB** | 유연 회로 연결 및 신호 전송 | 반복 굴곡 내성(Flexural Endurance) 및 박막 적층 기술 [Ref: IPC-2223] |

## 3. Performance Verification: Theoretical vs. Verified

| 기술 항목 | 이론적 목표치 (Theoretical) | 실제 검증치 (Verified) | 편차 ($\Delta$) | 근거 (Evidence) |
| :--- | :--- | :--- | :--- | :--- |
| BMS 전압 정밀도 | $\pm 0.5\text{mV}$ | $\pm 0.9\text{mV}$ | $+0.4\text{mV}$ | PW-V-TEST-2026 |
| ECU 내열 한계 | $130^\circ\text{C}$ | $125^\circ\text{C}$ | $-5^\circ\text{C}$ | Thermal-Sim-V4 |
| 무선충전 효율 | $90\%$ | $86.5\%$ | $-3.5\%$ | Power-Audit-01 |
| SMT 실장 공차 | $\pm 10\mu\text{m}$ | $\pm 12\mu\text{m}$ | $+2\mu\text{m}$ | Vision-Insp-S1 |

## 4. Strategic Scalability: ESS Expansion Path
- **BMS Scaling**: 차량용 BMS의 정밀 측정 알고리즘을 ESS 대용량 뱅크 제어 시스템으로 확장하여 고전압 환경에서의 안정성 확보.
- **Density Optimization**: 모바일 SMT의 고밀도 실장 기술을 ESS BMS에 적용, 제어 보드의 소형화 및 모듈당 집적도 향상 구현.

## 5. Engineering Verification Checklist
- [ ] **Quality Standard**: IATF 16949 인증 기반의 모바일$\rightarrow$차량용 라인 전환 프로세스 준수 여부.
- [ ] **Thermal Management**: Digital Twin 기반의 ECU/BMS 열해석 결과와 실측 데이터의 일치성 검증.
- [ ] **Inspection Automation**: AI 비전 시스템을 통한 MCM 조립 공차의 픽셀 단위 정밀 검증 완료 여부.
