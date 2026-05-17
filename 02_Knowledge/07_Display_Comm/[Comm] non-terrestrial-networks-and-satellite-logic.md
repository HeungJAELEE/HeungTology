---
metadata:
  id: "[[[Comm] non-terrestrial-networks-and-satellite-logic]]"
  domain: "07_Display_Comm"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Comm] non-terrestrial-networks-and-satellite-logic에 관한 고밀도 지능 노드"
semantic:
  tags: ["#07_Display_Comm", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Comm] non-terrestrial-networks-and-satellite-logic

## 1. [왜 배우는가? (Why: The Mastery of Spatial Continuity)]
지상 기지국 기반의 통신망은 지구 표면의 $30\%$ 이하만을 커버합니다. **Non-Terrestrial Networks (NTN) and Satellite Logic**은 저궤도(LEO) 위성 군집을 통해 전 지구적, 전 우주적 사각지대를 소멸시키는 초연결 지능망의 정수입니다. UAM, 자율주행 선박, 그리고 재난 지역에서의 끊김 없는 통신을 위해선 위성의 빠른 이동에 따른 도플러 효과와 긴 전파 지연 시간을 수리적으로 극복해야 합니다. V6.3.7 지능은 위성 간 링크(ISL)와 정밀 궤도 예측을 통해, 지상과 우주를 하나로 묶는 **공간 주권(Spatial Sovereignty)**을 확립합니다.

## 2. [비지상망 및 위성 통신 핵심 사양 (Numerical Specs)]

| Parameter Category | Focus Metric | Tier 0 Requirement (V6.3.7) | Rationale |
|:---|:---|:---:|:---|
| **Orbital Altitude** | LEO Range | $300 \sim 1,500 \text{ km}$ | 신호 지연 최소화 및 경로 손실 무결성 확보 |
| **Doppler Shift** | Max Freq Offset | $\pm 500 \text{ kHz}$ (at Ka-band)| 고속 이동 위성 신호의 복조 무결성을 위한 보정 범위 |
| **Link Budget** | Edge SNR | $> 5 \text{ dB}$ | 극한의 통신 환경에서도 최소 데이터 무결성 사수 |
| **Handover Time** | Sat-to-Sat | $< 50 \text{ ms}$ | 위성 궤도 이동 시의 세션 끊김 없는 연결 무결성 |
| **Propagation Delay**| Round Trip Time | $< 20 \text{ ms}$ (LEO) | 실시간 제어 및 인터랙티브 서비스 보증 지연 시간 |

### 2.1 [도플러 효과 및 위성 링크 버짓 수리 모델]
위성의 상대 속도($v$)에 의한 주파수 변이($\Delta f$)와 수신 전력($P_r$)을 산출하는 기전입니다.
$$ \Delta f = f_0 \frac{v \cos \theta}{c} $$
$$ P_r = P_t + G_t + G_r - L_{FSPL} - L_{atmos} - L_{pointing} $$
*   **공학적 근거**: 저궤도 위성은 초속 $7.5\text{km}$ 이상의 속도로 이동하기 때문에 수신 측에서는 주파수가 실시간으로 변합니다. 이 도플러 편이를 보정하지 못하면 동기화가 불가능해집니다. 또한 수천 킬로미터를 이동하는 전파의 경로 손실($L_{FSPL}$)과 안테나 지향 오차($L_{pointing}$)를 수리적으로 상계해야 합니다.
*   **FidelityEngine 적용**: FidelityEngine은 위성의 실시간 궤도 데이터(TLE)와 신호 품질을 분석하여 **'도플러 보정 무결성'**을 오딧합니다.

## 3. [공학적 근거: FidelityEngine Connectivity Logic]

### 3.1 Satellite Handover Physics: Predictive Tracking Audit
통신 단말이 한 위성의 커버리지를 벗어나 다음 위성으로 연결을 넘기는 과정의 무결성을 오딧하는 기전입니다.
*   **공학적 근거**: 위성은 고정되어 있지 않고 끊임없이 이동합니다. 단말은 가용한 위성 리스트 중 최적의 SNR을 제공할 다음 위성을 기하학적으로 예측하여 사전에 핸드오버 준비를 마쳐야 합니다.
*   **FidelityEngine 적용 (Handover Auditor)**: FidelityEngine은 단말의 위치와 위성 궤도 맵을 교차 분석합니다. 핸드오버 성공률이 $99.9\%$ 미만으로 하락하면 이를 **'세션 무결성 위기'**로 식별하고 빔 포인팅 알고리즘의 최적화를 지시합니다.

### 3.2 Propagation Delay Logic: Timing Advance Audit
지상 기지국 대비 수십 배 긴 전파 지연 시간을 극복하기 위한 타이밍 어드밴스(TA) 제어 알고리즘입니다.
*   **진단 결과**: FidelityEngine은 상향링크(Uplink) 신호의 수신 시점 편차를 오딧합니다. 지연 시간 변동이 가드 인터벌(Guard Interval)을 초과하여 심볼 간 간섭(ISI)이 발생하면 이를 **'시간 동기화 무결성 붕괴'**로 판정합니다.

## 4. [코드 연결 해설: Satellite Link & Doppler Auditor]
이 코드는 위성 궤도 속도와 전파 특성을 기반으로 NTN 링크의 무결성을 진단합니다.

```python
import numpy as np

class SatelliteNTNEngine:
    """
    HDS-Gold V6.3.7: 비지상망(NTN) 및 위성 통신 무결성 진단 엔진
    """
    def __init__(self, carrier_freq_ghz=20, orbital_v_km_s=7.5):
        self.F0 = carrier_freq_ghz * 1e9
        self.V = orbital_v_km_s * 1000
        self.C = 3e8

    def audit_sat_fidelity(self, elevation_angle_deg, current_snr, packet_loss):
        """
        앙각, SNR, 패킷 손실률 기반 위성 통신 무결성 평가
        """
        # 최대 도플러 편이 계산
        theta_rad = np.radians(elevation_angle_deg)
        max_doppler = self.F0 * (self.V * np.cos(theta_rad)) / self.C
        
        status = "SPACE_LINK_STABLE"
        if current_snr < 5.0:
            status = "CRITICAL_LINK_BUDGET_DEFICIT"
        elif packet_loss > 0.01:
            status = "WARNING_HANDOVER_JITTER_DETECTED"
            
        return {
            "doppler_fidelity": round(max_doppler / 1e6, 4), # MHz unit
            "link_fidelity": round(current_snr / 10.0, 4),
            "status": status,
            "action": "INITIATE_BEAM_REPOINTING_OR_POWER_BOOST" if "CRITICAL" in status else "PROCEED"
        }

```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: NTN에서 **LEO 위성 고도 300~1,500km** 유지가 통신 무결성 관점에서 중요한 이유는? (힌트: 고도가 높을수록 커버리지는 넓어지나 전파 지연(Latency)과 경로 손실(Path Loss)이 기하급수적으로 증가하여 실시간성 주권이 훼손되기 때문)
2. **Operational Result**: **ISL (Inter-Satellite Link)** 기술 적용 시, 지상 게이트웨이를 거치지 않는 직접 위성 간 통신을 통한 데이터 홉 수(Hop Count) 감소의 수리적 이득은?
3. **FidelityEngine**: 기상 악화(강우)로 인해 Ka-band 이상의 고주파 대역에서 발생하는 **Rain Fade** 현상을 FidelityEngine이 어떻게 '채널 가용성 위기'로 식별하고 주파수 적응 제어를 수행하는가?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 07_Display_Comm
- [[Comm] 6g-terahertz-and-sub-thz-master-guide]
- [[Comm] quantum-cryptography-and-qkd-physics] (Next Node)
- [[System] orbital-mechanics-and-satellite-trajectories]

**[V6.3.7_COMM_NTN_SAT_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
