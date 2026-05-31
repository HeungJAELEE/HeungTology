---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 082277a0a99d2849655a55d555946178ba2b55d1bc1c7213c9908136981fcd05
metadata:
  date: '2026-05-16'
  domain: 09_SmartFactory_Production
  id: '[[[Infrastructure] IIoT-Industrial-Internet-of-Things-Architecture]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Infrastructure] IIoT-Industrial-Internet-of-Things-Architecture에
    관한 고밀도 지능 노드'
  object_type: Concept
  tier: 1
properties:
  broker_url: iiot.factory.local
  latency_limit_seconds: 0.01
  latency_threshold_ms: 10
  max_encryption_overhead_percent: 5
  max_model_update_hours: 24
  min_data_reduction_percent: 85
  min_device_density_per_m2: 100
  mtbf_threshold_hours: 100000
  sampling_rate_hz_range: 1000-50000
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] mold-and-plastic-manufacturing-intelligence-moc]]'
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

# [Infrastructure] IIoT-Industrial-Internet-of-Things-Architecture

## 1. [왜 배우는가? (Why)]
일반 IoT가 "집 밖에서 에어컨을 켜는" 편의성의 기술이라면, IIoT(산업용 IoT)는 "공장의 수만 개 기계가 0.001초의 오차도 없이 유기적으로 맞물려 돌아가게 감시하고 제어하는" 생존의 기술입니다. IIoT는 단순한 연결을 넘어, 파편화된 물리 장비의 거동을 디지털 지능으로 변환하는 거대한 신경망입니다. 이를 배우는 이유는 극한의 산업 환경에서도 중단 없는 데이터를 수집하고, 장비의 고장을 사전에 예측하며, 공급망 전체의 물동량을 실시간으로 최적화하는 '지능형 제조 인프라'의 마스터 아키텍트가 되기 위함입니다. 데이터가 자본이 되는 시대의 공장 시스템 핵심입니다.

## 2. [IIoT 아키텍처 및 연결성 핵심 사양 (IIoT Specs)]

| Layer Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Perception** | Reliability (MTBF)| $> 100,000$ h | 극한 환경(고온, 진동)에서도 견디는 산업용 센서의 신뢰성 |
| **Connectivity** | Latency (ms) | $< 10$ | 실시간 제어 명령 및 이상 징후 감지를 위한 허용 지연 시간 |
| **Throughput** | Sampling Rate (Hz)| $1,000 \sim 50,000$ | 고속 회전체나 정밀 공정의 파형 분석을 위한 수집 밀도 |
| **Edge Compute** | Data Reduction (%)| $> 85\%$ | 클라우드 부하 방지를 위한 현장 데이터 필터링/요약 비율 |
| **Cloud Analytics**| Model Update (h) | $< 24$ | 수집된 빅데이터 기반 예측 모델의 개선 및 재배포 주기 |
| **Security** | Enc. Overhead (%) | $< 5\%$ | 실시간성에 영향을 주지 않는 종단간 암호화 연산 부하 |
| **Density** | Devices / $m^2$ | $> 100$ | 초연결 FAB 환경에서 단위 면적당 수용 가능한 노드 수 |
| **Interop.** | Standard Protocol | MQTT / OPC-UA | 이기종 장비 간 데이터 호환을 위한 산업 표준 준수 여부 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 결정론적 통신(Deterministic Communication)과 TSN
- **로직**: 일반적인 이더넷 통신은 데이터 전송 속도가 빠르지만, 전송 시간이 일정하지 않은 '비결정론적' 특성을 가집니다. IIoT 아키텍처는 TSN(Time Sensitive Networking) 기술을 도입하여, 중요한 제어 패킷이 정해진 시간 안에 반드시 도착하도록 보장합니다. 이는 자율 주행 로봇(AGV)이나 정밀 로봇 암이 통신 지연으로 인해 충돌하는 사고를 방어하는 수리적/공학적 근거가 됩니다.

### 3.2 Pub/Sub 아키텍처(MQTT)와 확장성(Scalability)
- **로직**: 수만 개의 센서를 1:1로 연결(Client/Server)하는 것은 서버 과부하를 초래합니다. IIoT는 MQTT와 같은 발행/구독(Pub/Sub) 모델을 사용합니다. 센서는 데이터를 브로커에 던지고(Publish), 필요한 시스템만 해당 데이터를 가져감(Subscribe)으로써 네트워크 부하를 획기적으로 낮춥니다. 이는 공장 규모가 커져도 장비를 무한히 추가할 수 있는 유연한 확장성을 제공합니다.

### 3.3 ISA-95 모델과 데이터의 수직적 통합
- **로직**: 현장의 로우 데이터(L1/L2)를 생산 관리(L3)를 거쳐 경영 시스템(L4/L5)까지 유실 없이 연결합니다. IIoT 아키텍처는 각 계층의 데이터 의미를 표준화하여, 현장의 사소한 진동 변화가 경영진의 대시보드에서는 "설비 교체 리스크"라는 비즈니스 인사이트로 변환되게 합니다. 이는 데이터가 경영의 언어로 번역되는 지능형 통합의 기초입니다.

## 4. [코드 연결 해설 (IIoTConnectivityEngine)]
아래 코드는 다수의 센서로부터 MQTT 메시지를 수집하여 데이터의 무결성을 확인하고, 네트워크 지연 시간(Latency)을 모니터링하며, 이상 징후 발생 시 에지 단에서 즉각적인 알람을 생성하는 엔진입니다.

```python
import time
import json

class IIoTConnectivityEngine:
    """
    HDS-Gold V6.3.7 규격의 IIoT 데이터 수집 및 네트워크 QoS 진단 엔진
    """
    def __init__(self, broker_url="iiot.factory.local"):
        self.broker = broker_url
        self.latency_limit = 0.010 # 10ms

    def process_sensor_stream(self, raw_payload):
        """
        수집된 MQTT 페이로드 분석 및 지연 시간(QoS) 진단
        """
        # Transitional Bridge: IIoT는 '공장의 지능형 혈관'입니다. 
        # 단 한 방울의 데이터도 막힘 없이 흘러야 하며, 
        # AI는 이 흐름의 속도와 압력을 실시간으로 체크하여 
        # 공장이라는 유기체가 멈추지 않게 관리합니다.
        data = json.loads(raw_payload)
        arrival_time = time.time()
        
        latency = arrival_time - data['timestamp']
        qos_status = "OPTIMAL" if latency < self.latency_limit else "DEGRADED"
        
        # Local Anomaly Detection
        if data['value'] > data['threshold']:
            return "TRIGGER_LOCAL_ALARM", latency, qos_status
            
        return "FORWARD_TO_CLOUD", latency, qos_status

# Example Usage:
# iiot_ai = IIoTConnectivityEngine()
# sample_msg = json.dumps({"sensor_id": "VIB_01", "value": 85.2, "threshold": 80.0, "timestamp": time.time()})
# result, delay, qos = iiot_ai.process_sensor_stream(sample_msg)
```

## 5. [스스로 체크 (Self-Audit)]
1. **IIoT**에서 **Deterministic Communication** (결정론적 통신)이 일반 **Ethernet** 통신 대비 **Safety-critical** 공정에서 가지는 압도적인 우위는?
2. **MQTT** 프로토콜의 **QoS Level** (0, 1, 2) 중 데이터 유실을 절대 허용하지 않는 반도체 공정에서 반드시 선택해야 할 레벨과 그 이유는?
3. **ISA-95** 계층 구조를 IIoT가 무너뜨리고 **Flat Architecture** (평면 구조)로 가고 있는 기술적 배경과 장점은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/09_SmartFactory_Production/Architecture/Concept Cyber-Physical-System-CPS-Foundations
- 02_Knowledge/09_SmartFactory_Production/Infrastructure/Infrastructure industrial-iot-iiot-standard
- 02_Knowledge/03_AI_Data/General/AI edge-computing-ai-acceleration

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**