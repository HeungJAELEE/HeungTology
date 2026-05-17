---
metadata:
  id: "[[[Battery] lithium-plating-physics-and-detection]]"
  domain: "02_Battery"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Battery] lithium-plating-physics-and-detection에 관한 고밀도 지능 노드"
semantic:
  tags: ["#02_Battery", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Battery] lithium-plating-physics-and-detection

## 1. 개요: 음극 표면의 금속 리튬 증착 (Lithium Plating)
리튬 플레이팅(LP)은 리튬 이온($Li^+$)이 음극 활물질 내부로 삽입되지 못하고 음극 표면에서 금속 리튬($Li^0$)으로 환원되어 증착되는 현상입니다. 이는 음극의 전위가 $Li/Li^+$ 기준 $0V$ 이하로 떨어질 때 발생하며, 증착된 리튬은 수지상 결정(Dendrite)으로 성장하여 분리막을 관통하고 내부 단락을 유발하는 치명적인 안전 리스크가 됩니다.

## 2. 기술 규격 및 검출 임계치 표준 (Detection Standards)

| 파라미터 | 공학적 정의 | 설계 목표치 (Target) |
| :--- | :--- | :---: |
| **플레이팅 개시 전위** | LP가 발생하기 시작하는 음극 전위 | $< 0\text{ V vs Li/Li}^+$ |
| **스트리핑 전압 피크** | 증착 리튬 재이온화 시 전압 구간 | $0.1 \sim 0.2\text{ V}$ |
| **Plateau 변곡점 감도** | 전압 이완 분석을 통한 LP 탐지 정밀도 | $< 10.0\text{ mV}$ |
| **임계 충전 전류 (C-rate)** | LP를 유발하는 온도별 최대 전류 밀도 | SOC/온도 의존적 |
| **N/P 비율** | 양극 대비 음극 용량 설계비 | $> 1.1$ |

## 3. 핵심 검출 메커니즘: 전압 이완 분석 (Voltage Relaxation)

### 3.1 스트리핑(Stripping) Plateau 탐지
BMS는 충전 후 휴지기(Rest period) 동안의 전압 이완 곡선을 분석합니다. 증착된 금속 리튬이 다시 이온화되어 전해액으로 돌아갈 때 발생하는 전압 평탄 구간(Plateau)의 시간적 길이를 통해 플레이팅 양을 정량화합니다.
- **분석 지표**: $dV/dt$ 곡선의 변곡점 분석.

### 3.2 저온 및 고SOC 리스크 모델
저온($< 10\text{ }^\circ\text{C}$) 환경에서는 리튬의 확산 속도가 급감하여 전위가 쉽게 $0V$ 이하로 떨어집니다. 이를 방지하기 위해 다단계 정전류 충전(MCC) 프로토콜을 적용하여 음극 전위를 안전 범위 내로 통제합니다.

## 4. 완화 및 안전 프로토콜
- **Fast-charge Optimization**: 실시간 음극 전위 추정을 통한 충전 전류 능동 제어.
- **예열 프로토콜**: 저온 충전 시 외부 가열 또는 내부 발열을 통해 이온 전도도를 확보한 후 충전 개시.

## 5. 결론 (Deterministic Standard)
본 노드는 리튬 플레이팅에 의한 내부 단락 사고를 원천 차단하기 위한 물리적 진단 표준을 제공합니다. 실제 플레이팅 발생 전압 및 검출 감도 데이터는 인스턴스 로그에서 관리됩니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] Battery-Management-System-BMS-and-Safety-Intelligence]]
- [[[Data] Battery-Lithium-Plating-Detection-Performance-Log_2026-05-16]]
