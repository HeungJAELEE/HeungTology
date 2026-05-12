---
Basic:
  id: "SF-ARCH-2026-V6"
  domain: "09_SmartFactory_Production"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#Smart_Factory'
  is_part_of: []
  related_to: []
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

# [[[Battery] W12_smart-factory-architecture

## 1. [왜 배우는가? (Why)]]
현대 제조 공정의 핵심 과제는 '비결정론적(Non-deterministic) 요소의 완전한 제거'입니다. 단순히 전산 시스템을 도입하는 것이 아니라, 마이크로초($\mu s$) 단위의 정밀 제어가 필요한 OT(Operational Technology) 영역과 시간 단위의 의사결정이 필요한 IT 영역을 어떻게 심리스(Seamless)하게 통합하느냐가 제품의 품질 수율(Yield)과 공장 가동률을 결정합니다. 스마트 팩토리 아키텍처를 배우는 이유는 ISA-95 수직 통합 모델을 넘어, 엣지 컴퓨팅과 AI가 결합된 '자율 조정 제조(Autonomous Orchestration)' 시스템을 구축하여 하드웨어의 물리적 한계를 소프트웨어의 논리적 흐름으로 극복하기 위함입니다.

## 2. [스마트 팩토리 아키텍처 핵심 사양 (System Specs)]

| Layer (ISA-95) | Function | Key Protocols | Latency Req. | Engineering Rationale |
|:---|:---|:---|:---:|:---|
| **L0: Field** | Sensors/Actuators | IO-Link, Analog | $< 1 \text{ ms}$ | 실시간 물리 현상 데이터 수집 및 구동 |
| **L1: Direct Ctl**| PLC / Motion | EtherCAT, PROFINET | $1 \sim 10 \text{ ms}$ | 하드 리얼타임 결정론적 제어 루프 |
| **L2: Supervisory**| SCADA / HMI | Modbus TCP, SLMP | $10 \sim 100 \text{ ms}$ | 설비 상태 감시 및 운전 파라미터 제어 |
| **L3: Execution** | MES / MOM | OPC-UA, MQTT | $100 \text{ ms} \sim 1 \text{ s}$ | 생산 실행 관리 및 품질 데이터 추적 |
| **L4: Business** | ERP / PLM | REST API, SQL | $> 1 \text{ s}$ | 전사적 자원 계획 및 수주 데이터 연동 |
| **TSN Sync** | Time Sensitive | IEEE 802.1AS | $< 1 \mu s$ | 네트워크 전반의 정밀 시간 동기화 오차 |
| **OEE Target** | Overall Eff. | Availability/Qual. | $> 85\%$ | 공장 가동 효율 극대화 목표 지표 |
| **Data Thru-put** | Bandwidth | High Speed Eth. | $> 10 \text{ Gbps}$ | 대규모 센서 데이터 및 비전 검사 데이터 처리 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 섀넌-하틀리(Shannon-Hartley) 정리에 따른 데이터 채널 용량
현장 센서 데이터의 신뢰성 있는 전송을 위한 물리적 한계를 정의합니다.
- **수식**: $C = B \log_2(1 + S/N)$ ($C$: 채널 용량, $B$: 대역폭, $S/N$: 신호 대 잡음비)
- **의미**: 전자기 노이즈가 심한 공장 환경에서 데이터 손실 없이 지능형 제어를 수행하기 위해서는 높은 $S/N$비를 확보할 수 있는 산업용 통신 규격(Shielded Twisted Pair 등)이 필수적입니다.

### 3.2 지터(Jitter)와 제어 안정성
표준 이더넷의 비결정론적 특성으로 발생하는 지터는 모션 제어의 오차를 유발합니다.
- **인과관계**: High Jitter $\rightarrow$ Sync Error $\rightarrow$ Mechanical Vibration $\rightarrow$ Product Defect.
- **해결책**: TSN(Time Sensitive Networking)을 도입하여 시간 슬롯을 물리적으로 분할, 실시간 데이터의 우선순위를 하드웨어 레벨에서 보장합니다.

### 3.3 나이퀴스트-섀넌(Nyquist-Shannon) 샘플링 정리
고속 비전 검사나 진동 분석 AI 모델을 위해 현장 데이터를 수집할 때, 정보 손실 없는 최소 샘플링 속도를 결정합니다. 수집된 고해상도 데이터는 엣지(Edge)에서 1차 가공되어 클라우드로 전송됨으로써 네트워크 부하를 최적화합니다.

## 4. [코드 연결 해설 (Factory Neural Orchestrator)]
아래 코드는 현장의 PLC 데이터(L1/L2)를 수집하여 MQTT 프로토콜을 통해 MES/AI 계층(L3)으로 전송하고, 이상 탐지 시 즉각적인 피드백을 제어 계층으로 하달하는 엣지 지능 로직입니다.

```python
import json
import paho.mqtt.client as mqtt

class FactoryNeuralOrchestrator:
    """
    HDS-Gold V6.3.7 규격의 스마트 팩토리 계층 통합 및 이상 탐지 엔진
    """
    def __init__(self, edge_id):
        self.id = edge_id
        self.client = mqtt.Client()

    def on_sensor_data_received(self, sensor_payload):
        """
        L1 센서 데이터 수집 및 엣지 분석
        """
        data = json.loads(sensor_payload)
        
        # 1. Edge AI: 진동 및 전류 기반 이상 탐지
        is_anomaly = self._run_edge_inference(data['vibration'], data['current'])
        
        # 2. 메타데이터 보강 및 상위 계층(MES) 보고
        report = {
            "origin": self.id,
            "status": "ANOMALY" if is_anomaly else "NORMAL",
            "telemetry": data,
            "timestamp": "ISO-8601"
        }
        
        self.client.publish(f"factory/edge/{self.id}/out", json.dumps(report), qos=1)
        
        # 3. 크리티컬 상황 시 PLC 즉시 정지 명령 (Feedback Loop)
        if is_anomaly:
            self._send_emergency_stop_to_plc(data['plc_ip'])

    def _run_edge_inference(self, vib, curr):
        # 엣지 가속기(TensorRT/OpenVINO) 기반 추론 로직
        return True if vib > 5.5 else False

# Example Usage:
# orchestrator = FactoryNeuralOrchestrator(edge_id="LINE-01-COATER-01")
# orchestrator.client.connect("10.10.1.100", 1883)
```

## 5. [스스로 체크 (Self-Audit)]
1. **ISA-95** 모델에서 **L3(MES)**와 **L4(ERP)** 간의 데이터 동기화 주기가 실시간 생산 스케줄링(Re-scheduling) 성능에 미치는 영향은?
2. **TSN**의 **Strict Priority** 큐잉 방식이 일반 데이터 트래픽 폭주 상황에서도 '제어 데이터'의 결정론적 전송을 보장하는 수리적 매커니즘은?
3. **MQTT QoS Level 2**를 산업용 현장에서 사용할 때의 장점과, 빈번한 데이터 통신 환경에서 발생할 수 있는 오버헤드 간의 트레이드오프는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/09_SmartFactory_Production/ControlSystems/Control PLC-Standard-Logic
- 02_Knowledge/03_AI_Data/Industrial/AI Quality-Control-AI
- 02_Knowledge/03_AI_Data/Industrial/AI Edge-Computing-Inference

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**