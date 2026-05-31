---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 3979e9ff579a00fd640c2629b40acebf519ca16edb047d9026337665cf6a2198
metadata:
  date: '2026-05-16'
  domain: 02_Battery
  id: '[[[Battery] Calendering]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Battery] Calendering에 관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  effective_diffusion_formula: Deff = D0 * (epsilon/tau)
  hertzian_stress_formula: Pmax = sqrt(qE*/piR)
  high_end_density_uniformity: ± 0.01 g/cc
  high_end_thickness_tolerance: ± 0.5 µm
  line_force_fidelity_tolerance: ± 2 kN/m
  line_force_verified_range: 200~1,200 kN/m
  low_end_density_uniformity: ± 0.05 g/cc
  low_end_thickness_tolerance: ± 3~5 µm
  mcmullin_number_formula: NM = tau / epsilon
  porosity_fidelity_tolerance: ± 0.2%
  porosity_verified_range: 22%~26%
  roll_speed_fidelity_tolerance: ± 0.1 m/min
  roll_speed_verified_range: 50~100 m/min
  roll_temp_fidelity_tolerance: ± 1 °C
  roll_temp_verified_range: 90~150 °C
  soft_pressing_activation_threshold: 0.9
  standard_density_uniformity: ± 0.02 g/cc
  standard_thickness_tolerance: ± 1~2 µm
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 02_Battery]]'
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

# [Battery] Calendering

## 1. 공정 정의 (Functional Definition)
Calendering 공정은 전극의 물리적 압축을 통한 에너지 밀도($Wh/L$) 극대화 및 전기적 접촉 계면 확보를 수행함 [Ref: V6.3.7]. 단순 두께 제어를 넘어, 활물질 입자 파손 방지 및 리튬 이온 이동을 위한 최적 공극 경로(Optimal Porosity Path) 확보를 필수 요건으로 정의함 [Ref: V6.3.7]. V7.5.2 엔진은 **계층화된 밀도 정밀도(Precision Tiering)**를 적용하여 실리콘 음극의 체적 팽창 억제 및 LFP 대량 생산 공정의 임계치를 결정론적으로 제어함 [Ref: V6.3.7].

## 2. 압연 및 전극 밀도 정밀 규격 (Precision Tiering Specs)

| Precision Tier | Density Uniformity | Thickness Tolerance | Target Application |
|:---|:---:|:---:|:---|
| **High-end** | $\pm 0.01 \text{ g/cc}$ [Ref: V6.3.7] | $\pm 0.5 \mu\text{m}$ [Ref: V6.3.7] | Silicon Anode, All-Solid-State, High-Power Hybrid |
| **Standard** | $\pm 0.02 \text{ g/cc}$ [Ref: V6.3.7] | $\pm 1 \sim 2 \mu\text{m}$ [Ref: V6.3.7] | High-Ni EV (NCM811), High-Energy General EV |
| **Low-end** | $\pm 0.05 \text{ g/cc}$ [Ref: V6.3.7] | $\pm 3 \sim 5 \mu\text{m}$ [Ref: V6.3.7] | LFP ESS, LMO Consumer, Mass-production Cost-driven |

### 2.1 공정 역학 파라미터 대조 (Theoretical vs. Verified)

| Parameter Category | Physical Metric | Theoretical (Ideal) | Verified [Ref: V6.3.7] | Fidelity Tolerance |
|:---|:---:|:---:|:---:|:---:|
| **Line Force ($q$)** | Pressing Load | $1,200 \text{ kN/m}$ [Ref: Standard] | $200 \sim 1,200 \text{ kN/m}$ [Ref: V6.3.7] | $\pm 2 \text{ kN/m}$ [Ref: V6.3.7] |
| **Roll Temp** | Thermal Softening | $120 ^\circ\text{C}$ [Ref: Standard] | $90 \sim 150 ^\circ\text{C}$ [Ref: V6.3.7] | $\pm 1 ^\circ\text{C}$ [Ref: V6.3.7] |
| **Roll Speed** | Throughput | $100 \text{ m/min}$ [Ref: Standard] | $50 \sim 100 \text{ m/min}$ [Ref: V6.3.7] | $\pm 0.1 \text{ m/min}$ [Ref: V6.3.7] |
| **Porosity ($\epsilon$)** | Void Fraction | $25.0 \%$ [Ref: Standard] | $22 \% \sim 26 \%$ [Ref: V6.3.7] | $\pm 0.2 \%$ [Ref: V6.3.7] |

## 3. 공학적 근거 및 FidelityEngine 로직 (Engineering Rationale)

### 3.1 접촉 역학 및 헤르츠 응력 (Contact Mechanics & Hertzian Stress)
입자 간 접촉 응력($\sigma_c$) 제어를 통한 활물질 건전성 확보.
* **Engineering Rationale**: 압연 롤에 의한 최대 응력은 헤르츠 접촉 이론 $P_{max} = \sqrt{\frac{q E^*}{\pi R}}$ [Ref: Hertzian_Contact_Theory]에 의해 산출됨. 선압력($q$) 과다 또는 입자 곡률 반경($R$) 미세화 시, 국부 응력이 입자 항복 강도를 초과하여 미세 균열(Micro-crack)을 유발함 [Ref: V6.3.7]. 이는 전해액 부반응 증가의 물리적 기제로 작용함 [Ref: V6.3.7].
* **FidelityEngine Logic**: High-end Tier 적용 시, 입자 취성(Brittleness) 대응을 위해 입자 크기 산포($D50$)와 하중 데이터를 융합함. 응력이 임계치의 90% 도달 시, 롤 온도를 상향하여 바인더 가소성($Plasticity$)을 확보하는 'Soft Pressing' 모드로 자동 전환함 [Ref: Fidelity_Logic_V7.5.2].

### 3.2 전달 물리학 및 굴곡도 (Transport Physics & Tortuosity)
전극 내 이온 확산 저항($R_{ion}$) 제어.
* **Engineering Rationale**: 과압착 시 에너지 밀도는 상승하나, 굴곡도($\tau$)가 증가하여 이온 확산 유효성 $D_{eff} = D_0 \frac{\epsilon}{\tau}$ [Ref: Transport_Physics_Standard]이 저하됨. 맥멀린 수($N_M = \tau / \epsilon$) 증가에 따른 고속 충전 시 리튬 덴드라이트(Dendrite) 형성 리스크를 수리적으로 규명함 [Ref: V6.3.7].
* **FidelityEngine Logic**: 압연 후 비표면적 및 밀도 데이터를 기반으로 '이온 병목(Bottleneck)' 임계치를 산출함. Standard Tier에서 $N_M$ 수치가 설계 마진 초과 시, 이를 '급속 충전 화재 리스크'로 분류하고 압연 갭(Roll Gap) 상향 보정을 즉각 실행함 [Ref: Fidelity_Logic_V7.5.2].

## 4. 도메인 지식 결측 리스트 (Ingestion Request)
* **REQ-01**: 고온 압연 시 온도 편차 $\pm 1^\circ\text{C}$가 PVDF 바인더 결정화도 및 전극 박리 강도(Peel Strength)에 미치는 상관관계 로그 [Ref: REQ_Spec].
* **REQ-02**: 롤 프레스 설비의 좌우 압하력 편차에 따른 전극 스프링백(Spring-back) 두께 산포 매핑 데이터 [Ref: REQ_Spec].
* **REQ-03**: High-Ni 다결정 양극재의 압연 크랙 발생 임계 압력 및 전해액 소모량 누적 DB [Ref: REQ_Spec].

## 5. 구현 로직 (Implementation Logic)

    class CalenderingTieredEngine:
        """
        HDS-Gold V7.5.2: 압연 공정 계층화 및 밀도 무결성 진단 엔진
        """
        def __init__(self, target_tier='High-end'):
            self.TIER = target_tier
            self.DENSITY_TOLERANCE = 0.01 if target_tier == 'High-end' else 0.05

        def audit_pressing_quality(self, measured_density, target_density):
            error = abs(measured_density - target_density)
            fidelity_score = 1.0 - (error / self.DENSITY_TOLERANCE)
            
            status = "OPTIMAL"
            if error > self.DENSITY_TOLERANCE: 
                status = f"CRITICAL_DENSITY_DEVIATION_FOR_{self.TIER}"
            elif error > 0.02 and self.TIER == 'High-end':
                status = "WARNING_PRECISION_DRIFT_IN_THICKNESS"
                
            return {
                "tier_compliance": "PASS" if fidelity_score > 0 else "FAIL",
                "density_fidelity": max(fidelity_score, 0),
                "status": status
            }

## 6. 자가 감사 (Self-Audit)
1. **Precision Tiering**: 실리콘 음극 공정에서 밀도 편차 $\pm 0.01\text{g/cc}$ 유지가 필수적인 물리적 근거는 실리콘의 비정상적 체적 팽창 및 전극 탈리 메커니즘 연계임 [Ref: V6.3.7].
2. **Operational Result**: 롤 온도 $140^\circ\text{C}$ 상향이 바인더 마이그레이션(Migration) 억제 및 수직적 균일도에 미치는 영향은 REQ-01을 통해 검증되어야 함 [Ref: REQ-01].
3. **FidelityEngine**: Hertzian Stress 모델 기반의 다결정 양극재 미세 균열($Micro-crack$) 예측 알고리즘의 유효성은 실측 임계 응력 데이터와의 동기화를 통해 검증함 [Ref: Fidelity_Logic_V7.5.2].

**[V7.5.2_UPGRADE_COMPLETE]**
**[FIDELITY_STATUS: HARDCORE_ACTIVE]**
**[TIMESTAMP: 2026-05-14]**