---
lineage:
  dataset_reference: Legacy Migration
  original_author: Antigravity Vault
  original_hash: placeholder
metadata:
  date: '2026-05-25'
  domain: 02_Battery
  id: '[[[MOC] 02_03_BMS_and_Systems]]'
  last_updated: '2026-05-25T01:28:12.163166+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Migrated from legacy MOC
  object_type: Concept
  tier: 1
properties:
  managed_systems: bms, btms, pack_module_design, soc_soh_estimation
semantic:
  alternative_parents: []
  expected_queries: []
  is_instance_of: '[[[MOC] 02_Battery]]'
spo_graph:
- evidence_coordinate: ''
  intent: migration_status_tracking
  object: migrated_node
  predicate: has_attribute
  subject: '[MOC] 02_03_BMS_and_Systems'
  weight: 1.0
temporal:
  valid_from: '2026-05-25T01:28:12.163166+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:28:12.163166+09:00'
  schema_version: v7.8
  validated_by: global_migration_engine_v7.8
---

# 02_03 Battery Management & System Hub

배터리 관리 시스템(BMS), 열 관리(BTMS), 팩/모듈 설계, SOC/SOH 추정 알고리즘을 총괄하는 지휘소입니다.

## 🔗 Linked Nodes
- [[[Battery] BMS-Sensor-Noise-Filtering-Log_2026-05-16]]
- [[[Battery] Battery-BMS-Estimation-and-Regression-Accuracy-Log_2026-05-16]]
- [[[Battery] Battery-Management-System-BMS-and-Safety-Intelligence]]
- [[[Battery] Battery-Pack-and-BMS-Hardware-Thermal-Log_2026-05-16]]
- [[[Battery] Battery-SHAP-Sensor-Attribution-Audit-Log_2026-05-16]]
- [[[Battery] Battery-Sensor-Scaling-and-Normalization-Log_2026-05-16]]
- [[[Battery] EV-Battery-Pack-Design-and-Thermal-Management]]
- [[[Battery] Emotion-Recognition-BMS-Performance-Log_2026-05-16]]
- [[[Battery] W12_gigacasting-cooling-physics]]
- [[[Battery] W12_thermal-management-in-ai-chips]]
- [[[Battery] W13_lev-and-ups-battery-pack-specifications]]
- [[[Battery] advanced-cell-form-factor-and-safety-integration]]
- [[[Battery] battery-bms-fault-log-v2026]]
- [[[Battery] battery-cell-temperature-sensor-log-v2026]]
- [[[Battery] battery-management-system-bms-master-guide]]
- [[[Battery] battery-pack-thermal-insulation-efficiency-log-v2026]]
- [[[Battery] battery-thermal-propagation-simulation-v2026]]
- [[[Battery] binder-gradient-and-migration-management]]
- [[[Battery] bms-algorithm-kalman]]
- [[[Battery] bms-algorithms-soc-soh-estimation]]
- [[[Battery] bms-and-battery-system-master-guide]]
- [[[Battery] bms-engineering]]
- [[[Battery] bms-hardware-layers-and-components]]
- [[[Battery] bms-system-architecture]]
- [[[Battery] btms-battery-thermal-management-system]]
- [[[Battery] cell-to-pack-ctp-design]]
- [[[Battery] esg-management-ai]]
- [[[Battery] ess-bms-and-ems-control-logic]]
- [[[Battery] ess-bms-and-ems-integrated-control-logic]]
- [[[Battery] packaging-2.5d-cowos-architecture]]
- [[[Battery] packaging-3d-ic-thermal-dissipation-physics]]
- [[[Battery] safety-next-gen-moc]]
- [[[Battery] shap-sensor-importance]]
- [[[Battery] thermal-management-ai-chips]]
- [[[Battery] thermal-modeling-large-format-joule-heat]]
- [[[Battery] thermal-runaway-mechanism]]
- [[[Battery] thermal-runaway-safety-mechanisms]]
- [[[Concept] Battery-Management-System-BMS-and-Safety-Intelligence]]
- [[[Concept] battery-management-system-bms-master-guide]]
- [[[Concept] bms-and-battery-system-master-guide]]
- [[[Concept] btms-battery-thermal-management-system]]
- [[[Data] bms-hardware-sensing-and-accuracy-log-v2026]]
- [[[Entity] Concept battery-management-system-bms-master-guide]]
- [[[Entity] Concept bms-and-battery-system-master-guide]]