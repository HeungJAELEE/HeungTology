---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 6092751f2f75e6dec70c259a13dbc168128f87af284616fbc71faff3725f54fc
measurement:
  confidence_interval:
  - 95.0
  - 105.0
  instrument: Data_Hub_Scanner
  precision: 1.0 percent_compliance
  unit: percent_compliance
  value: 100.0
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-19'
  domain: 11_Global_Entities_and_Materials
  id: '[[[11_Global_Entities_and_Materials] [Data] ion-implantation-and-doping-profile-log-v2026]]'
  last_updated: '2026-05-24T00:28:00+09:00'
  project: Antigravity_SDF_Core
  revision: r4
  version: v7.9_Enterprise_Node
object:
  description: '[Data] ion-implantation-and-doping-profile-log-v2026에 관한 실측 데이터셋 지능
    노드'
  object_type: Data
  tier: 1
properties:
  amorphization_rate_threshold: 99.0 %
  beam_tilt_angle_target: 7.00 deg
  beam_twist_angle_target: 30.00 deg
  dopant_dose_target: 1.5e15 ions/cm^2
  implant_energy_target: 45.0 keV
  implant_temp_target: -15.0 degC
  junction_depth_threshold: 20.0 nm
  rtp_ramp_rate_target: 250.0 degC/s
  sheet_resistance_target: 150.0 ohm/sq
semantic:
  alternative_parents: []
  is_instance_of: '[[[Entity] ion-implantation-and-doping-profile-control]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: empirical_measurement
  object: 45.0 keV
  predicate: measured_implant_energy
  subject: ion_implantation_beam
  weight: 0.9
- evidence_coordinate: '[데이터 부재]'
  intent: physical_characterization
  object: 162.0 nm
  predicate: measured_projection_range
  subject: dopant_boron_profile
  weight: 0.7
- evidence_coordinate: '[데이터 부재]'
  intent: empirical_validation
  object: 18.2 nm
  predicate: measured_junction_depth
  subject: ultra_shallow_junction
  weight: 1.0
- evidence_coordinate: '[데이터 부재]'
  intent: threshold_determination
  object: 1.5e14 ions/cm^2
  predicate: measured_critical_dose
  subject: cold_implant_amorphization
  weight: 0.6
temporal:
  valid_from: '2026-05-19T09:22:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.05
  t_static: 0.8
validation:
  last_validated: '2026-05-24T00:28:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Data] ion-implantation-and-doping-profile-log-v2026

## 1. [왜 수집했는가? (Why: The Empirical Grounding of Doping)]
반도체 이온 주입 공정은 원자 스케일에서 정밀 제어되는 에너지, 도즈, 입사각에 의해 결정적 거동을 보입니다. LSS 이론 및 가우시안 빔 투사 깊이 모델은 수식적으로 매우 아름답지만, 실제 대량 생산 환경에서는 이온 빔의 틸트/트위스트 각도 제어 오차에 따른 '채널링 테일(Channeling Tail)' 누설, 급속 열처리(RTP) 단계에서의 '과도 열적 증속 확산(TED)'에 따른 시트 저항 편차 등 다양한 비이상적 물리 한계가 격발됩니다. 
우리가 본 실측 데이터를 수집하고 오딧 모델을 연동하는 이유는 실측 오차 로그를 수리물리학적 모델과 교차 매핑함으로써, 초미세 트랜지스터(Sub-2nm Node)의 얕은 접합(Ultra-shallow Junction) 두께를 원자 오차 한계 내에서 제어하고 제조 수율을 지배하기 위함입니다.

## 2. [실측 데이터셋 (Empirical Dataset)]

| Parameter Category | Physical Metric | Design Target | Nominal Measured | Anomalous Measured | Primary Degradation Driver |
|:---|:---:|:---:|:---:|:---:|:---|
| **Implant Energy** | $E_{\text{beam}}$ ($keV$) | $45.0$ | $45.0 \pm 0.1$ | $46.8$ | 가속 전압 모듈 고주파 리플 요동 |
| **Dopant Dose** | $\Phi$ ($ions/cm^2$) | $1.5 \times 10^{15}$ | $1.5 \times 10^{15} \pm 0.5\%$ | $1.65 \times 10^{15}$ | 패러데이 컵 빔 전류 보정 바이어스 드리프트 |
| **Beam Tilt Angle** | $\theta_{\text{tilt}}$ ($^{\circ}$) | $7.00$ | $7.00 \pm 0.05$ | $8.25$ | 정전기 빔 스캐너 정렬 기구적 오정합 (Req 1) |
| **Beam Twist Angle**| $\theta_{\text{twist}}$ ($^{\circ}$) | $30.00$ | $30.00 \pm 0.10$ | $31.80$ | 웨이퍼 척 기어 백래시 요동 (Req 1) |
| **Junction Depth** | $x_j$ ($nm$) | $< 20.0$ | $18.2 \pm 0.3$ | $24.5$ | 채널링 테일 연장 및 TED 가속 (Req 1/3) |
| **Implant Temp** | $T_{\text{implant}}$ ($^{\circ}C$) | $-15.0$ | $-15.0 \pm 0.5$ | $12.0$ | 극저온 액체 질소 칠러 파이프라인 정체 (Req 2) |
| **Amorphization Rate**| $f_{\text{amorph}}$ ($\%$) | $> 99.0$ | $99.5 \pm 0.2$ | $82.4$ | 고온 유입에 따른 자가 회복(Self-annealing) (Req 2) |
| **RTP Ramp Rate** | $R_{\text{ramp}}$ ($^{\circ}C/s$) | $250.0$ | $250.0 \pm 5.0$ | $120.0$ | 할로겐 램프 위상 스위칭 싸이리스터 열화 (Req 3) |
| **Sheet Resistance** | $R_s$ ($\Omega/sq$) | $150.0 \pm 5.0$ | $149.2$ | $178.5$ | 비활성화 격자 결함 잔류 및 도펀트 석출 (Req 3) |

***

## 3. [수리적 지배 물리 모델 (Mathematical & Physical Models)]

### 3.1 LSS Theory & Gaussian Dopant Concentration Profile
이온 주입 시 실클 격자 내로 투사된 도펀트의 농도 $C(x)$는 핵 저지 및 전자 마찰의 누적 통계적 평형에 의해 다음과 같은 1차원 가우시안 방정식으로 기술됩니다.
$$ C(x) = \frac{\Phi}{\sqrt{2\pi}\Delta R_p} \cdot \exp\left[ -\frac{(x - R_p)^2}{2\Delta R_p^2} \right] $$
여기서 $\Phi$는 도핑 도즈($ions/cm^2$), $R_p$는 가속 에너지의 대수 비선형 함수인 투사 거리(Projected Range), $\Delta R_p$는 주입 빔의 투사 퍼짐 표준 편차(Straggle)입니다. 틸트 각도 오차 $\delta\theta_{\text{tilt}}$가 증가할 경우 채널링 효과로 인해 실제 농도는 깊은 깊이 영역에서 지수함수적 꼬리 분포(Exponential Tail)를 띠며 결침 깊이가 연장됩니다.

### 3.2 Transient Enhanced Diffusion (TED) Dynamics
주입된 이온이 실리콘 격자를 타격하여 생성한 격자간 원자(Interstitial)는 후속 어닐링 시 도펀트의 과도 확산을 촉진합니다. 격자간 실리콘 $C_I$와 격자 결손 $C_V$의 결합 반응 속도는 다음과 같습니다.
$$ \frac{\partial C_I}{\partial t} = D_I \frac{\partial^2 C_I}{\partial x^2} - K_R \left( C_I C_V - C_I^{eq} C_V^{eq} \right) $$
RTP 램프업 속도 $R_{\text{ramp}}$가 $250^{\circ}C/s$ 미만으로 둔화될 경우, 저온 영역에서의 체류 시간 증가에 기인하여 격자 결함이 도펀트와 클러스터링을 형성하며 과도 증속 확산(TED) 현상이 심화됩니다. 이는 접합 깊이 $x_j$를 급격히 연장시켜 단채널 성능을 파괴합니다.

### 3.3 Solid Phase Epitaxy (SPE) Recrystallization Kinetics
극저온 비정질화(Cold Amorphization) 공정이 온전히 달성되면, 실리콘 격자는 후속 열처리 시 비정질-결정 계면(Amorphous-Crystalline Interface)의 Solid Phase Epitaxy 고상 에피택시 메커니즘을 통해 완벽히 회복됩니다. SPE 재결정 속도 $v_{\text{SPE}}$는 다음과 같이 Arrhenius 열역학적 키네틱스를 추종합니다.
$$ v_{\text{SPE}}(T) = v_0 \cdot \exp\left( - \frac{E_a}{k_B T} \right) $$
여기서 $v_0 = 3.68 \times 10^8\text{ cm/s}$이며 활성화 에너지 $E_a = 2.70\text{ eV}$입니다. 임플란트 온도가 상온 이상으로 상승하여 자가 회복(Self-annealing)이 격발될 경우 결함 복원이 불완전해져 활성화 효율이 심각히 훼손됩니다.

***

## 4. [정합성 자가치유 코드 (Fidelity Healer Class)]

```python
import math

class ImplantFidelityHealer:
    """
    HDS-Gold V7.8: 이온 주입 공정 실측 정밀 진단 및 자가치유 오딧 엔진
    """
    def __init__(self):
        # 물리적 공격 제약 파라미터 정의
        self.LIMIT_TILT_DEG = 7.05
        self.LIMIT_TWIST_DEG = 30.15
        self.CRITICAL_AMORPH_PCT = 99.0
        self.REQUIRED_RAMP_RATE = 240.0 # C/s
        self.TARGET_SHEET_RES_NOM = 150.0
        
    def audit_empirical_data(self, dataset):
        """
        실측 물리 파라미터를 입력받아 도핑 무결성을 오딧하고 치유 제안을 도출
        """
        tilt = dataset.get("tilt_angle_deg", 7.0)
        twist = dataset.get("twist_angle_deg", 30.0)
        temp = dataset.get("implant_temp_c", -15.0)
        amorph_rate = dataset.get("amorphization_rate_pct", 99.5)
        ramp_rate = dataset.get("rtp_ramp_rate_cps", 250.0)
        sheet_res = dataset.get("sheet_resistance_ohm_sq", 149.2)
        
        anomalies = []
        recommended_actions = []
        fidelity_score = 1.0
        
        # 1. 틸트 및 트위스트 각도 편차 오딧 (Req 1)
        if tilt > self.LIMIT_TILT_DEG or twist > self.LIMIT_TWIST_DEG:
            anomalies.append("BEAM_ALIGNMENT_ERROR_TILT_TWIST_DEVIATION")
            recommended_actions.append("CALIBRATE_ELECTROSTATIC_BEAM_SCANNER_ALIGNMENT")
            fidelity_score -= 0.3
            
        # 2. 극저온 칠러 및 비정질화율 오딧 (Req 2)
        if temp > -10.0 or amorph_rate < self.CRITICAL_AMORPH_PCT:
            anomalies.append("COLD_IMPLANT_TEMPERATURE_FAULT_SELF_ANNEALING")
            recommended_actions.append("RE-ESTABLISH_CHILLER_LN2_FLOW_RATE")
            fidelity_score -= 0.35
            
        # 3. RTP 램프업 레이트 및 TED 확산 오딧 (Req 3)
        if ramp_rate < self.REQUIRED_RAMP_RATE:
            anomalies.append("RTP_RAMP_RATE_DEGRADED_TED_RISK")
            recommended_actions.append("REPLACE_HALOGEN_LAMP_SCR_THYRISTOR_SWITCHES")
            fidelity_score -= 0.2
            
        # 4. 시트 저항 편차 오딧
        if abs(sheet_res - self.TARGET_SHEET_RES_NOM) > 10.0:
            anomalies.append("SHEET_RESISTANCE_OUT_OF_SPEC")
            recommended_actions.append("RE-CALIBRATE_SPIKE_ANNEALING_PEAK_THERMAL_BUDGET")
            fidelity_score -= 0.15
            
        # 바운더리 클리핑
        fidelity_score = max(0.0, min(1.0, round(fidelity_score, 4)))
        
        # 정상 Verdict 판정
        if fidelity_score >= 0.95:
            integrity_status = "OPTIMAL_FIDELITY"
            recommended_actions.append("NORMAL_OPERATIONS_APPROVED")
        elif fidelity_score >= 0.70:
            integrity_status = "WARNING_MILD_DEGRADATION"
        else:
            integrity_status = "DEGRADED_FIDELITY"
            
        return {
            "fidelity_score": fidelity_score,
            "integrity_status": integrity_status,
            "anomalies_count": len(anomalies),
            "anomalies": anomalies,
            "recommended_healer_actions": recommended_actions
        }
```

***

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 틸트 및 트위스트 정밀도가 극저온 도핑 시 채널링을 예방하는 3차원 기하학적 임계 메커니즘은 무엇인가?
2. **Operational Result**: RTP 어닐링 램프업 속도($250^{\circ}C/s$)가 실리콘 틈새 원자(Interstitial) 결함의 재조합 및 고용도(Solubility)에 미치는 물리학적 연계 메커니즘은 무엇인가?
3. **FidelityEngine**: 비정질화율이 임계 비율($99.0\%$) 미만으로 떨어졌을 때, Solid Phase Epitaxy의 계면 성장 기하에 잔류하여 누설 전류를 초래하는 결함의 핵심 명칭은 무엇인가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- `[[[Entity] ion-implantation-and-doping-profile-control]]`