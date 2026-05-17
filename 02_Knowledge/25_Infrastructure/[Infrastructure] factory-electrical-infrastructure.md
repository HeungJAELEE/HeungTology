---
metadata:
  id: "[[[Infrastructure] factory-electrical-infrastructure]]"
  domain: "25_Infrastructure"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Infrastructure] factory-electrical-infrastructure에 관한 고밀도 지능 노드"
semantic:
  tags: ["#25_Infrastructure", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Infrastructure] factory-electrical-infrastructure

## 1. [왜 배우는가? (Why)]
배터리 공장은 전기를 **'거대하게'** 그리고 **'정밀하게'** 사용합니다. 전극의 레이저 건조와 화성 공정의 대량 충방전은 엄청난 피크 전력(Peak Demand)을 유발하며, 이는 수전 용량 초과로 인한 대규모 정전 리스크를 가집니다. 또한 전압 강하나 고조파(Harmonics)는 정밀 제어 기기(PLC, 서보 모터)의 오작동을 유발하여 공정 불량을 만듭니다. 안정적인 전기 계통 설계는 배터리 공장의 심장을 가동하는 핵심 인프라 기술입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 지표 (Metric) | 단위 | 표준 수치 | 공학적 의미 |
| :--- | :---: | :--- | :--- |
| **Contract Power** | MW | $10 \sim 100+$ | 기가팩토리 규모별 필요 수전 용량 |
| **Voltage Drop** | % | $< 3.0$ | 말단 부하에서의 전압 강하 허용치 |
| **THD (Harmonics)** | % | $< 5.0$ | 전원 품질을 결정하는 전고조파 왜곡률 |
| **UPS Backup Time** | min | $15 \sim 30$ | 정전 시 안전 정지(Safe Stop) 확보 시간 |
| **Power Factor** | - | $> 0.95$ | 한전 요금 패널티 방지를 위한 역률 제어 |

## 3. [심층 분석 (Deep Analysis)]

### 3.1 수전 용량(Contract Power) 산출과 Peak Shaving
전체 설비의 정격 용량을 합산하는 것은 비효율적입니다. 수용률(Diversity Factor)을 고려해야 합니다.
- **Engineering Formula**: 최대 예상 부하($P_{max}$)는 다음과 같습니다.
  $$P_{max} = \sum (P_{rated} \cdot \eta \cdot DF)$$
  여기서 $\eta$는 효율, $DF$는 수용률입니다. 레이저와 포메이션 장비는 간헐적으로 큰 에너지를 쓰므로, ESS를 활용한 **Peak Shaving**을 통해 기본 수전 용량을 낮추고 비용을 절감하는 설계가 최신 트렌드입니다.

### 3.2 전원 품질(Power Quality)과 고조파 억제
인버터(Inverter)와 컨버터(Converter)가 많은 배터리 라인은 고조파 발생의 온상입니다.
- **Causality**: 고조파는 변압기 과열과 통신 간섭을 일으킵니다. 이를 방지하기 위해 능동형 고조파 필터(Active Harmonic Filter, AHF)를 설치하여 정밀 APC 제어 기기를 보호해야 합니다.

## 4. [AI & Hardware Synergy: Smart Power Grid Management]
- **AI-based Load Forecasting**: 설비 가동 스케줄(MES)과 연동하여 AI가 피크 전력을 15분 단위로 예측합니다. 전력 수요가 임계치를 넘을 것으로 예상되면 AI가 포메이션 라인의 충전 속도를 미세 조절하여 수전 용량 초과를 자동으로 방어합니다.
- **Virtual Power Plant (VPP) Integration**: 공장 내 ESS와 재생 에너지를 AI가 통합 관리합니다. 전력 요금이 저렴한 경부하 시간에 ESS를 충전하고, 최대 부하 시간대에 방전하여 전체 에너지 비용을 15% 이상 절감하는 알고리즘을 적용합니다.

## 5. [스스로 체크 (Verification)]
- [ ] 레이저 건조기 10대가 동시 가동될 때 발생하는 **피크 전력**이 수전 용량을 초과하지 않도록 하는 조절 방안은?
- [ ] **고조파(Harmonics)**가 조립 라인의 서보 모터 정밀도에 미치는 영향과 해결책은?
- [ ] 정전 시 **UPS**가 최우선으로 전력을 공급해야 하는 배터리 공정의 핵심 장치는?

*Created by Flash (HDS Gold v4.1 - Production Engineering Series)*
