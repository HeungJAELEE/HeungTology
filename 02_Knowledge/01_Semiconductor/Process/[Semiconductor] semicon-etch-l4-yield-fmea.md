---
Basic:
  id: "SEMICON_ETCH_L4_YIELD_FMEA"
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
  tags: '["#Semiconductor", "#Etching", "#Yield", "#FMEA", "#Troubleshooting", "#HDS_Gold_v6_1"]'
  is_part_of: []
  related_to: '["Semiconductor semicon-etch-l3-hardware", "Semiconductor semicon-etch-l5-advanced-2026"]'
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

# [[[Semiconductor] semicon-etch-l4-yield-fmea

# Semiconductor semicon-etch-l4-yield-fmea
[🟢 Local RAG] 식각 공정은 가공의 마지막 단계에서 물리적 파괴를 수반하므로, 한 번의 오류가 칩 전체의 폐기로 직결됩니다. 특히 3D 구조가 심화됨에 따라 발생하는 비정상적인 전하 축적이나 이온 궤적의 뒤틀림은 육안으로 식별 불가능한 만성 불량을 야기합니다. 본 백서는 4M1E 관점에서 식각 불량을 정의하고, 실시간 설비 진단 데이터와 수율 로그를 결합하여 '데이터 기반의 즉각적 트러블슈팅' 체계를 구축하는 데 목적이 있습니다. Semiconductor semicon-troubleshoot-etching-plasma

---

# [[[Semiconductor] semicon-etch-l4-yield-fmea

| 관리 항목 | 물리적 의미 | 관리 임계치 (Target) | 출처 (Source) |
| :--- | :--- | :--- | :--- |
| **Etch Rate Unif.** | 웨이퍼 내 식각 깊이 편차 | $< 1.5 \%$ | Semiconductor semicon-troubleshoot-etching-plasma]] |
| **Taper Angle** | 식각 프로파일 수직도 | $89^\circ \sim 90.5^\circ$ | Semiconductor semicon-troubleshoot-etching-plasma |
| **Bias Voltage ($V_{dc}$)**| 이온 타격 에너지 지표 | $\pm 10 \text{ V}$ (Drift 관리) | Semiconductor semicon-troubleshoot-etching-plasma |
| **Reflected Power** | RF 전력 전달 효율 | $< 1 \%$ | Semiconductor semicon-troubleshoot-etching-plasma |
| **Aspect Ratio (AR)** | 굴착 깊이/폭 비율 | $> 100:1$ (HAR 제어) | Semiconductor semiconductor-har-etching-physics |

---

# [[[Semiconductor] semicon-etch-l4-yield-fmea

| 고장 모드 (Failure Mode) | 원인 (Root Cause) | 영향 (Effect) | 검출 및 트러블슈팅 (Remedy) | RPN |
| :--- | :--- | :--- | :--- | :--- |
| **Notching** | 전하 축적에 의한 이온 궤적 휘어짐 | 배선 하부 단락 | **Pulsed RF** 도입 및 전하 중화 Semiconductor semicon-troubleshoot-etching-plasma]] | 210 |
| **Arcing** | ESC 에지 링 마모 | 웨이퍼 국부 소실 | ESC 누설 전류 모니터링 및 정기 PM Semiconductor semicon-troubleshoot-etching-plasma | 240 |
| **Bowing** | 이온 입사 각도 산포 증가 | 인접 패턴 브릿지 | 보호막 강화 및 파워 비율 조정 Semiconductor semiconductor-har-etching-physics | 180 |
| **ARDE** | 넛센 확산 한계 | 목표 깊이 미달 | 저압 공정 전환 및 Radical 증대 Semiconductor semiconductor-har-etching-physics | 200 |

---

# [[[Semiconductor] semicon-etch-l4-yield-fmea

# Semiconductor semicon-etch-l4-yield-fmea
[🟢 Local RAG] 칩 면적이 커질수록 식각 공정에서의 미세 파티클 하나가 미치는 치명도는 지수적으로 상승합니다.
- **Murphy Model**: 수율 예측 무결성 지표. Data semiconductor-yield-defect-density-correlation-log-v2026

---

# [[[Semiconductor] semicon-etch-l4-yield-fmea
- Semiconductor semicon-troubleshoot-etching-plasma]]
- Semiconductor semiconductor-har-etching-physics
- Data semiconductor-yield-defect-density-correlation-log-v2026
- Semiconductor semicon-etch-l3-hardware
- Semiconductor semicon-etch-l5-advanced-2026

*Created by Antigravity V6.3.7 Chief Knowledge Architect (Flash)*
