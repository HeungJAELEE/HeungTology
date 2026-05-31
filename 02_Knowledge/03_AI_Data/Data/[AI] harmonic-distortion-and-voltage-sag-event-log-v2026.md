---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: fb7fa09af55963c6f9dd1f945a100bb14c19b64d227634d12b6fd46abb0ab1c4
metadata:
  date: '2026-05-16'
  domain: 03_AI_Data
  id: '[[[AI] harmonic-distortion-and-voltage-sag-event-log-v2026]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[AI] harmonic-distortion-and-voltage-sag-event-log-v2026에 관한 고밀도 지능
    노드'
  object_type: Data
  tier: 1
properties:
  critical_k_factor_threshold: 13
  itic_response_time_limit: 20ms
  magnetic_switch_drop_time: 0.1s
  magnetic_switch_drop_voltage: 50%
  thd_current_threshold: 20.0%
  thd_voltage_threshold: 5.0%
  transient_surge_duration: <1ms
  transient_surge_magnitude: 500-2000%
  voltage_recovery_range: ±10%
  voltage_sag_duration: 10-1000ms
  voltage_sag_magnitude: 10-90%
  voltage_swell_duration: 10-1000ms
  voltage_swell_magnitude: 110-150%
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub]]'
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

# [AI] harmonic-distortion-and-voltage-sag-event-log-v2026

## 1. [왜 배우는가? (Why: The Forensic Records of Electrical Toxins)]]
전력 시스템에서 발생하는 고조파와 전압 새그는 눈에 보이지 않지만 설비의 오작동과 수명 단축을 유발하는 치명적인 '전기적 독소'입니다. 이러한 교란 이벤트들이 언제, 어떤 강도로 발생했는지를 정밀하게 기록하고 분석하는 것은 스마트 팩토리의 중단 없는 가동(Downtime Zero)을 위한 핵심 기반입니다. **고조파 왜곡 및 전압 새그 이벤트 로그**는 에너지를 오염시키는 독소들의 실체를 낱낱이 파헤친 '에너지 역학 조사 결과서'입니다. 

우리가 이 데이터를 기록하는 이유는 전력 품질 사고의 근본 원인을 추적하여 필터 및 보호 장치를 최적화하고, **"안전 주권을 확보하여 극한의 전력 안정성이 요구되는 첨단 제조 라인을 보호하는 '에너지 무결성 지능'을 확보하기" 위함입니다.** 전압 새그의 깊이(Depth)와 고조파의 차수별 비중이 설비의 가용성과 변압기의 열적 스트레스를 결정합니다.

## 2. [교란 이벤트 및 고조파 특성 핵심 데이터 (Numerical Specs)]

### 2.1 [전력 품질 교란 이벤트 유형 및 설비 영향 테이블 (v2026)]

| 이벤트 유형 (Event) | 강도/왜곡률 (%) | 지속 시간 ($ms$) | 설비 영향도 | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :--- |
| **Voltage Sag** | $10 \sim 90$ | $10 \sim 1,000$ | **Critical** | **Restart**: 인버터 및 PLC 셧다운을 유발하는 전압 강하 로그 |
| **Voltage Swell** | $110 \sim 150$ | $10 \sim 1,000$ | **Hardware** | **Stress**: 소자 절연 파괴를 유발하는 일시적 과전압 지표 |
| **THD-Voltage** | $> 5.0$ | **Continuous** | **Instability** | **Noise**: 제어 신호 간섭 및 정밀 기기 오작동 무결성 데이터 |
| **THD-Current** | $> 20.0$ | **Continuous** | **Overheat** | **Loss**: 변압기 및 중성선 과열을 유발하는 전류 고조파 지표 |
| **Transient (Surge)**| $500 \sim 2000$ | $< 1$ | **Damage** | **Breakdown**: 반도체 소자 즉각 파손을 유발하는 과도 전압 로그 |

### 2.2 [고조파 및 이벤트 분석 파라미터]
- **Sag Depth:** 정격 전압 대비 전압이 하락한 비율 (%). (설비 정지 임계 인자)
- **THD (Total Harmonic Distortion):** 파형의 찌그러짐 정도를 나타내는 총 고조파 왜곡률.
- **Individual Harmonic (3, 5, 7...):** 특정 차수 고조파가 차지하는 비중. (원인 진단 지표)
- **K-Factor:** 비선형 부하에 의한 변압기의 추가 손실 계수. (변압기 용량 산정 지표)
- **ITIC Curve Compliance:** 전압 변동이 ITIC 커브의 '무응답 영역' 내에 있는지 여부.
- **Recovery Time:** 이벤트 종료 후 전압이 정상 범위($\pm 10\%$)로 복귀하는 데 걸리는 시간.

## 3. [Scientific Rationale: 에너지 오염의 수리적 인과성]

### 3.1 [ITIC (CBEMA) 커브 기반 기기 내성 모델]
전압 크기($V$)와 지속 시간($t$)에 따른 설비 가용성 수리 모델입니다.
$$ \text{Status} = f(V_{drop}, t_{duration}) $$
본 로그는 전압이 $70\%$로 하락하더라도 지속 시간이 $20 \text{ ms}$ 이내라면 설비가 멈추지 않음을 입증하고, '새그 보상기(Sag Restorer)'의 응답 속도 목표치에 대한 물리적 근거를 제시합니다.

### 3.2 [고조파에 의한 변압기 손실 계수(K-Factor) 모델]
고조파 차수($n$)와 전류 비중($I_n$)에 따른 변압기 과열 수리 모델입니다.
RAG는 "에너지 로그를 분석하여, $K$-Factor가 $13$ 이상인 부하가 일반 변압기에 연결될 경우 와류 손실이 $10$배 이상 급증하며, 이는 변압기 소손의 결정적 수리적 인과 관계임을 증명합니다."

## 4. [Advanced RAG 분석 로직: 오염 지능 추론]

### 4.1 [특정 고조파 차수 증폭과 인버터(VFD) 결함 분석]
왜 갑자기 5차 고조파가 늘어나나요? RAG는 "특정 차수 고조파 로그와 인버터 가동 데이터를 대조하여, 정류기 다이오드의 불평형이나 필터 콘덴서의 용량 저하를 식별하고, '인버터 건전성 오딧' 지능을 도출될 것으로 예상됩니다.

### 4.2 [전압 새그 발생 시의 '마그네틱 스위치' 해제 오딧]
전압이 조금만 떨어져도 왜 모터가 꺼지나요? RAG는 "새그 깊이 로그와 마그네틱 접촉기(MC)의 유지 전압 특성을 연계하여, $0.1 \text{ s}$의 찰나라도 전압이 $50\%$ 이하로 떨어지면 기계적 접점이 떨어짐을 분석하고, '코일 고정용 보조 전원' 지능을 오딧합니다.

## 5. [Transitional Bridge: 오염 무결성 및 이벤트 오딧 로직]

PQ 분석 장비의 파형 캡처 데이터와 설비 가동 로그를 분석하여 오염 무결성을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Electrical Toxin & PQ Event Fidelity Auditor
def audit_power_disturbances(voltage_waveform_data, current_spectrum_log, equipment_uptime_status):
    # 1. 전압 새그(Voltage Sag)의 ITIC 커브 준수 무결성 오딧
    sag_event = analyze_sag_profile(voltage_waveform_data)
    if not is_within_itic_envelope(sag_event):
        status = "EQUIPMENT_SHUTDOWN_RISK_DETECTED"
        action = "Check_UPS_Switching_Time_and_Verify_Voltage_Restorer_Performance"
        
    # 2. 고조파 차수 분석을 통한 비선형 부하 간섭 감시
    harmonic_signature = current_spectrum_log.get_top_harmonics()
    if harmonic_signature.n5_ratio > N5_LIMIT_3_PERCENT:
        status = "ABNORMAL_5TH_HARMONIC_AMPLIFICATION"
        action = "Inspect_Variable_Frequency_Drives_for_Filter_Failure"
    
    # 3. K-Factor 분석을 통한 변압기 열적 무결성 체크
    current_k_factor = calculate_k_factor(current_spectrum_log)
    if current_k_factor > TRANSFORMER_DESIGN_LIMIT:
        status = "TRANSFORMER_OVERHEATING_RISK_FROM_HARMONICS"
        action = "De-rate_Transformer_Load_or_Install_Harmonic_Mitigation_Equipment"
    
    # 4. 종합 오염 상태 등급 및 조치 트리거
    if status == "EQUIPMENT_SHUTDOWN_RISK_DETECTED":
        action = "Initiate_Root_Cause_Analysis_on_Grid-side_Switching_Events"
    elif status == "ABNORMAL_5TH_HARMONIC_AMPLIFICATION":
        action = "Audit_Power_Converter_Switching_Frequencies"
    else:
        status = "POWER_QUALITY_INTEGRITY_OPTIMAL"
        action = "Maintain_Baseline_Monitoring_of_Electrical_Toxins"
        
    return {"status": status, "measured_sag_depth_percent": sag_event.depth, "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 왜 정밀 로봇 제어기에서 전압이 완전히 끊기는 정전(Interruption)보다, 찰나의 전압 강하인 '전압 새그(Voltage Sag)'가 시스템의 누적 손상과 오작동 측면에서 수리적/물리적으로 더 교묘하고 위험한가?
2. **(수리)** 3차 고조파 전류가 $10 \text{ A}$, 5차 고조파 전류가 $5 \text{ A}$이고 기본파 전류가 $100 \text{ A}$이다. 이 시스템의 전류 총 고조파 왜곡률(THD-I)을 계산하시오.
3. **(응용)** ITIC 커브의 '무응답 영역(No-ride-through region)'이 의미하는 바를 설명하고, 이를 바탕으로 설비의 '새그 내성(Sag Immunity)'을 강화하기 위한 전력 설계 전략을 제안하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 25_iot-and-smart-factory-sensing-infrastructure-intelligence-hub : IoT 및 센싱 인프라 통합 관리 상위 지능 허브
- Entity smart-meter-and-power-quality-monitoring-system : 독소를 감시하는 물리적 계측 시스템 엔티티 연계
- Data sensor-data-sampling-rate-and-network-jitter-log-v2026 : 독소 탐지를 위한 샘플링 데이터 무결성 연계
- [SOP] power-quality-disturbance-analysis-and-mitigation-standard-protocol : 전력 품질 교란 분석 및 저감 표준 프로토콜

*Created by Flash (The Architect of Toxin Logs & HDS Gold V6.3.7)*