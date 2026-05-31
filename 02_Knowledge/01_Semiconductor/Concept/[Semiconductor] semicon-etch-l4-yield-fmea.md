---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 5304bd35edb7bfc7a8a7145501fcd395420fe13aae5f5bb1bef27c7f95cce694
metadata:
  date: '2026-05-16'
  domain: 01_Semiconductor
  id: '[[[Semiconductor] semicon-etch-l4-yield-fmea]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Semiconductor] semicon-etch-l4-yield-fmea에 관한 고밀도 지능 노드'
  object_type: Risk
  tier: 1
properties:
  aspect_ratio_min: '100:1'
  bias_voltage_drift_limit: 10V
  etch_rate_uniformity_threshold: < 1.5%
  murphy_yield_model: Yield = ((1 - exp(-AD))/AD)^2
  ref_har_etching_physics: semiconductor-har-etching-physics
  ref_troubleshoot_etching_plasma: semiconductor-troubleshoot-etching-plasma
  ref_yield_defect_density_correlation: semiconductor-yield-defect-density-correlation-log-v2026
  reflected_power_threshold: < 1%
  taper_angle_range: 89.0 - 90.5 degrees
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 반도체_백서_통합_지휘소]]'
spo_graph: []
temporal:
  valid_from: '2026-05-17T22:59:20+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-17T22:59:20+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Semiconductor] semicon-etch-l4-yield-fmea

## 1. Executive Summary
식각 공정(Etching)은 물리적/화학적 제거를 통한 패턴 형성의 최종 단계로, 비가역적 파괴 특성으로 인해 단일 공정 오류가 칩 전체의 폐기(Total Scrap)로 직결되는 고위험 공정임. 특히 3D 구조의 고종횡비(HAR) 심화에 따른 비정상적 전하 축적 및 이온 궤적 왜곡은 비가시적 만성 불량의 주원인이 됨. 본 문서는 4M1E 관점에서 식각 불량 메커니즘을 정의하고, 설비 파라미터와 수율 로그의 상관관계 기반 트러블슈팅 체계를 규정함.

## 2. Process Control Parameters

| 관리 항목 | 물리적 의미 | 관리 임계치 (Target) | 출처 (Source) |
| :--- | :--- | :--- | :--- |
| **Etch Rate Unif.** | 웨이퍼 내 식각 깊이 편차 | $< 1.5 \%$ [Ref: semiconductor-troubleshoot-etching-plasma] | semiconductor-troubleshoot-etching-plasma |
| **Taper Angle** | 식각 프로파일 수직도 | $89^\circ \sim 90.5^\circ$ [Ref: semiconductor-troubleshoot-etching-plasma] | semiconductor-troubleshoot-etching-plasma |
| **Bias Voltage ($V_{dc}$)**| 이온 타격 에너지 지표 | $\pm 10 \text{ V}$ (Drift) [Ref: semiconductor-troubleshoot-etching-plasma] | semiconductor-troubleshoot-etching-plasma |
| **Reflected Power** | RF 전력 전달 효율 | $< 1 \%$ [Ref: semiconductor-troubleshoot-etching-plasma] | semiconductor-troubleshoot-etching-plasma |
| **Aspect Ratio (AR)** | 굴착 깊이/폭 비율 | $> 100:1$ (HAR) [Ref: semiconductor-har-etching-physics] | semiconductor-har-etching-physics |

### 2.1 Theoretical vs. Verified Analysis
| Parameter | Theoretical (Ideal) | Verified (Actual) | Deviation/Margin |
| :--- | :--- | :--- | :--- |
| Etch Rate Uniformity | $0.0 \%$ | $< 1.5 \%$ [Ref: semiconductor-troubleshoot-etching-plasma] | $\pm 1.5 \%$ |
| Taper Angle | $90.0^\circ$ | $89.0^\circ \sim 90.5^\circ$ [Ref: semiconductor-troubleshoot-etching-plasma] | $\pm 1.0^\circ$ |
| Reflected Power | $0.0 \%$ | $< 1.0 \%$ [Ref: semiconductor-troubleshoot-etching-plasma] | $< 1.0 \%$ |
| Aspect Ratio | $\infty$ | $> 100:1$ [Ref: semiconductor-har-etching-physics] | $\text{N/A}$ |

## 3. Failure Mode and Effects Analysis (FMEA)

| 고장 모드 (Failure Mode) | 원인 (Root Cause) | 영향 (Effect) | 검출 및 트러블슈팅 (Remedy) | RPN |
| :--- | :--- | :--- | :--- | :--- |
| **Notching** | 전하 축적 $\rightarrow$ 이온 궤적 휘어짐 [Ref: semiconductor-troubleshoot-etching-plasma] | 배선 하부 단락 (Short) | Pulsed RF 도입 및 전하 중화 [Ref: semiconductor-troubleshoot-etching-plasma] | 210 |
| **Arcing** | ESC 에지 링 마모 $\rightarrow$ Plasma Instability [Ref: semiconductor-troubleshoot-etching-plasma] | 웨이퍼 국부 소실 (Burn) | ESC 누설 전류 모니터링 및 정기 PM [Ref: semiconductor-troubleshoot-etching-plasma] | 240 |
| **Bowing** | 이온 입사 각도 산포 증가 [Ref: semiconductor-har-etching-physics] | 인접 패턴 브릿지 (Bridge) | 보호막 강화 및 파워 비율 조정 [Ref: semiconductor-har-etching-physics] | 180 |
| **ARDE** | 넛센 확산 한계 (Knudsen Diffusion) [Ref: semiconductor-har-etching-physics] | 목표 깊이 미달 (Under-etch) | 저압 공정 전환 및 $\text{Radical}$ 밀도 증대 [Ref: semiconductor-har-etching-physics] | 200 |

## 4. Yield Modeling & Correlation
Chip Area 증대에 따라 미세 파티클의 치명도는 지수적으로 상승하며, 이는 수율 손실의 주 요인이 됨.
- **Murphy Model**: $\text{Yield} = \left( \frac{1 - e^{-AD}}{AD} \right)^2$ 수식을 통한 수율 예측 무결성 지표 적용. [Ref: semiconductor-yield-defect-density-correlation-log-v2026]

**Reference List:**
- semiconductor-troubleshoot-etching-plasma
- semiconductor-har-etching-physics
- semiconductor-yield-defect-density-correlation-log-v2026
- semiconductor-etch-l3-hardware
- semiconductor-etch-l5-advanced-2026