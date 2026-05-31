---
metadata:
  ai_status: Approved
  domain: 01_Semiconductor
  id: '[[[Data] SEMI-E47-1-etch-process-standard]]'
  version: v7.9_Enterprise_Node
object:
  description: SEMI E47.1 - Standard for High-Aspect Ratio Etching Process Control
  object_type: Concept
properties:
  bias_rf_power_range: 100 ~ 500 W
  chamber_pressure_range: 10 ~ 50 mTorr
  etch_gas_cf4_o2_ratio: 5:1 ~ 10:1
  source_rf_power_range: 1000 ~ 3000 W
  standard_id: SEMI-E47-1
  wafer_chuck_temperature: 20 ± 1 °C
semantic:
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub.md]]'
spo_graph: []
---

# [Data] SEMI-E47-1 Etch Process Standard

## 1. Overview
SEMI-E47-1 규격은 첨단 반도체 제조 공정 중 고종횡비(High-Aspect Ratio, HAR) 식각(Etching) 공정의 플라즈마 제어 및 가스 유량, 압력 허용 오차를 명시하는 글로벌 표준 데이터입니다. 공정 레시피 최적화 및 수율 저하 분석 시 결정적 팩트로 작용합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Range/Limit | Critical Dependency | Rationale |
| :--- | :--- | :--- | :--- |
| Chamber Pressure | $10 \sim 50 \ mTorr$ | Mean Free Path ($\lambda$) | 이온 직진성 확보 및 측벽 손상 방지 |
| Source RF Power | $1000 \sim 3000 \ W$ | Plasma Density ($n_e$) | 식각 속도(Etch Rate) 결정 |
| Bias RF Power | $100 \sim 500 \ W$ | Ion Energy ($E_i$) | 수직 식각 프로파일(Anisotropy) 달성 |
| Etch Gas ($CF_4/O_2$) Ratio | $5:1$ ~ $10:1$ | Polymer Passivation | 선택비(Selectivity) 및 Bowing 억제 |
| Wafer Chuck Temperature | $20 \pm 1 \ ^{\circ}C$ | Desorption Rate | 표면 반응 역학(Kinetics) 제어 |

## 3. Data Integration
이 데이터는 식각 공정 노드의 `evidence_coordinate`로 사용되며, HAR 구조의 임계 치수(CD) 불량 분석 시 레시피 편차 검증 모델의 룰셋(Rule-set)으로 편입됩니다.