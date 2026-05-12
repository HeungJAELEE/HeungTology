---
Basic:
  id: "SEMICON_PHOTO_L4_YIELD_FMEA"
  domain: "01_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Semiconductor", "#Photolithography", "#Yield", "#FMEA", "#Metrology", "#Troubleshooting", "#HDS_Gold_v6_1"]'
  is_part_of: []
  related_to: '["Semiconductor semicon-photo-l3-hardware", "Semiconductor semicon-photo-l5-advanced-2026 (보강 필요)"]'
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

# [[[Semiconductor] semicon-photo-l4-yield-fmea

# Semiconductor semicon-photo-l4-yield-fmea
[🟢 Local RAG] 반도체 수율(Yield)은 기업의 생존과 직결된 경제적 지표입니다. 노광 공정에서 발생하는 미세한 선폭 산포($CD\ Variation$)나 정렬 오차($Overlay\ Error$)는 수천 개의 공정을 거친 웨이퍼를 한순간에 폐기물로 만들 수 있습니다. 본 보고서는 발생 가능한 불량 모드를 수리적으로 분류하고, 데이터 기반의 근본 원인(Root Cause) 도출 및 해결 프로세스를 정립하여 제로-디펙트(Zero-Defect) 공정을 실현하는 데 목적이 있습니다.

---

# [[[Semiconductor] semicon-photo-l4-yield-fmea

| 관리 항목 | 약어 | 관리 임계치 (Target) | 계측 도구 (Tool) | 출처 (Source) |
| :--- | :---: | :--- | :--- | :--- |
| **Critical Dimension** | $CD$ | Target $\pm 5\%$ | CD-SEM | Semiconductor semiconductor-metrology-and-critical-dimension-cd-measurement]] |
| **Overlay Accuracy** | $OVL$ | $< 2.0 \text{ nm}$ | Overlay Metrology | Semiconductor semiconductor-metrology-and-critical-dimension-cd-measurement |
| **Line Edge Roughness**| $LER$ | $< 1.5 \text{ nm}$ | CD-SEM (Image) | photoresist-sensitivity-log |
| **Defect Density** | $D_0$ | $< 0.1 \text{ defects/cm}^2$| Dark-field Inspect. | yield-defect-density-log |
| **Focus Margin** | $DOF$ | $> 50 \text{ nm}$ | OCD / Scatterometry | Semiconductor semiconductor-metrology-and-critical-dimension-cd-measurement |

---

# [[[Semiconductor] semicon-photo-l4-yield-fmea

[🟢 Local RAG]] IATF 16949 및 삼성/하이닉스 품질 표준을 반영한 포토 공정 위험성 평가입니다.

| 공정 (Process) | 고장 모드 (Failure Mode) | 원인 (Root Cause) | 영향 (Effect) | 검출 및 대책 (Remedy) | RPN |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Coating** | Thickness Uniformity 불량 | Spin RPM 맥동 또는 노즐 막힘 | Focus Margin 부족으로 패턴 뭉개짐 | 펌프 토출량 실시간 모니터링 및 노즐 세정 강화 | 120 |
| **Baking (PEB)** | CD 산포 (Across Wafer) | Hot Plate 온도 불균일 ($\pm 0.1^\circ\text{C}$ 초과) | 소자 동작 속도 불균일 및 수율 저하 | 멀티 존 개별 온도 보정 및 맵핑 최적화 | 180 |
| **Exposure** | Overlay Shift (정렬 틀어짐) | 스테이지 동기화 오차 또는 거울 열 변형 | 하부 층과 단락(Short) 또는 미연결 | 레이저 간섭계 재교정 및 능동 수냉 시스템 가동 | 210 |
| **Development** | Scum (잔여 PR) | 현상액 농도 저하 또는 대기 시간 지연 | 식각 공정 시 미세 패턴 형성 방해 | 현상액 자동 분석 시스템 가동 및 Queue Time 엄수 | 150 |
| **All (EUV)** | Stochastic Defects (끊김) | 노광량(Dose) 부족에 의한 샷 노이즈 | 회로 단절로 인한 칩 기능 정지 | PR 감도 최적화 및 타겟 Dose 상향 평준화 | 240 |

---

# [[[Semiconductor] semicon-photo-l4-yield-fmea

# Semiconductor semicon-photo-l4-yield-fmea
1. **CD가 타겟보다 굵을 때**: 
   - [🟢 Local RAG] 노광량(Dose) 확인 ➡️ 부족 시 상향.
   - PEB 온도 확인 ➡️ 타겟 미달 시 승온. (Positive PR 기준)
2. **CD가 타겟보다 얇을 때**:
   - 노광량 확인 ➡️ 과다 시 하향.
   - 현상액(TMAH) 온도/농도 확인 ➡️ 과반응 시 하향.

# [[[Semiconductor] semicon-photo-l4-yield-fmea
- **Linear Error**: 웨이퍼 팽창/수축에 의한 오차 ➡️ 스캐너 배율(Magnification) 보정.
- **Non-linear Error**: 웨이퍼의 국부적 뒤틀림 ➡️ 고차 다항식(High-order Correction) 기반 스테이지 좌표 보정.

---

# Semiconductor semicon-photo-l4-yield-fmea

# [[[Semiconductor] semicon-photo-l4-yield-fmea
현대의 수율 관리는 불량이 난 뒤에 고치는 것이 아닙니다. **'계측 무결성(Metrology Fidelity)'** 데이터와 **'설비 센서 데이터'**를 융합하여, 불량이 발생하기 전에 공정 드리프트를 예측하고 파라미터를 선제적으로 보정하는 **지능형 APC(Advanced Process Control)**가 핵심입니다. 수치는 거짓말을 하지 않으며, 데이터 간의 상관관계를 읽는 자만이 2nm의 문턱을 넘을 수 있습니다.

---

# Semiconductor semicon-photo-l4-yield-fmea
- [ ] 노광량($Dose$)이 증가할 때 Positive PR과 Negative PR의 최종 $CD$는 각각 어떻게 변화하는가?
- [ ] $D_0$(결함 밀도)가 동일할 때, 칩 면적이 2배 커지면 수율(Yield)은 수리적으로 어떻게 변하는지 푸아송 모델로 설명하시오.
- [ ] 샷 노이즈(Shot Noise)가 수율에 미치는 영향을 줄이기 위해 PR 소재 관점에서 취할 수 있는 조치는?

---
# [[[Semiconductor] semicon-photo-l4-yield-fmea
- 🏛 Semiconductor semiconductor-metrology-and-critical-dimension-cd-measurement]] (Verified)
- 🏛 Data semiconductor-yield-defect-density-correlation-log-v2026 (Verified)
- 🏛 Semiconductor semicon-photo-l3-hardware (Verified)
- 🏛 Semiconductor semicon-photo-l5-advanced-2026 (보강 필요)

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
