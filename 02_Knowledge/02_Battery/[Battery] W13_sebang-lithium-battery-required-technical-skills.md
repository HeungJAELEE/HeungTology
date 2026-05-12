---
Basic:
  id: "BAT-CAREER-SEBANG-2026-V6"
  domain: "02_Battery"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#Career'
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

# [[[Battery] W13_sebang-lithium-battery-required-technical-skills

## 1. [왜 배우는가? (Why)]]
세방리튬배터리(주) 음성공장은 단순 생산 라인을 넘어, 고도의 자동화와 AI 통합이 이루어지는 스마트 팩토리 환경입니다. 이곳에서 요구하는 인재상은 단순히 기계를 조작하는 작업자가 아니라, '데이터 기반의 문제 해결사(Problem Solver)'입니다. 슬러리의 유변 데이터를 보고 다음 공정의 코팅 두께를 예측하며(Mixing-Coating 연계), 용접부의 변위 데이터를 통해 배터리의 장기 신뢰성을 판독하고(Assembly Quality), 수만 대의 설비 로그를 분석해 전체 설비 효율(OEE)을 1%라도 끌어올릴 수 있는 엔지니어링 역량이 필수적입니다. 본 문서는 채용 현장의 요구와 산업 표준을 결합하여, 배터리 제조 엔지니어로서 생존하고 성장하기 위한 핵심 기술 지표를 정의합니다.

## 2. [배터리 엔지니어 핵심 기술 사양 (Skill Specs)]

| Skill Category | Specific Competency | Target Level / Metric | Engineering Rationale |
|:---|:---|:---:|:---|
| **Process Control** | CPK / PPK Analysis | $C_{pk} > 1.33$ | 공정의 통계적 안정성 및 수율 보증 능력 |
| **Automation** | PLC Programming | Mitsubishi/LS (Expert) | 설비 시퀀스 제어 및 트러블슈팅 역량 |
| **Data Analysis** | Statistical Tools | Minitab / Python (SQL) | 6-Sigma 기반 공정 이상 원인(RCA) 분석 |
| **Quality Std.** | Automotive Specs | IATF 16949 / ISO 9001 | 글로벌 완성차 공급을 위한 품질 경영 이해 |
| **Measurement** | NDT / Metrology | CT / Ultrasound / Vision | 비파괴 검사 데이터를 통한 내부 결함 판독 |
| **Maintenance** | Predictive Maint. | PdM (PdM) Logic | 진동/전류 분석을 통한 설비 고장 사전 예측 |
| **IIoT Interface** | Connectivity | OPC-UA / MQTT | L1(Field)에서 L3(MES)까지의 데이터 브릿지 구축 |
| **Soft Skills** | Project Management | PMP / Agile | 도메인 간(소재-설비-IT) 협업 및 일정 관리 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 설비 종합 효율 (OEE) 계산 및 최적화
엔지니어는 단순 가동 시간을 넘어 공장의 생산성을 정량화할 수 있어야 합니다.
- **수식**: $OEE = Availability \times Performance \times Quality$
- **의미**: 설비가 계획된 시간 대비 얼마나 가동되었는지(가동률), 설계 속도 대비 얼마나 생산했는지(성능), 생산품 중 양품 비중은 얼마인지(품질)를 곱하여 공장의 '진짜 지능'을 측정합니다.

### 3.2 6-시그마 (DMAIC) 문제 해결 로직
현장의 불량 발생 시 감(Guess)이 아닌 체계적인 접근법을 따릅니다.
- **Define-Measure-Analyze-Improve-Control**: 불량을 정의하고, 데이터를 측정하며, 인과 관계를 분석하여 개선안을 도출하고, 이를 표준화하여 유지 관리합니다.

### 3.3 유변학 및 접합 물성의 상관관계
- **전극 공정**: 틱소트로피(Thixotropy) 분석을 통해 슬러리의 도포 안정성을 예측합니다.
- **조립 공정**: 용접 입열량 제어 및 HAZ(Heat Affected Zone) 분석을 통해 배터리 탭의 전기적 저항과 기계적 강도를 동시에 사수합니다.

## 4. [코드 연결 해설 (Production Analytics Tool)]
아래 코드는 생산 라인에서 발생하는 데이터를 실시간 집계하여 OEE 지표를 산출하고, 공정 능력 지수(CPK)를 계산하여 라인의 이상 여부를 판단하는 엔지니어링 도구입니다.

```python
import numpy as np

class ProductionAnalyticsTool:
    """
    HDS-Gold V6.3.7 규격의 생산 지표 분석 및 품질 관리 엔진
    """
    def __init__(self, plan_qty, plan_time_min):
        self.plan_qty = plan_qty
        self.plan_time = plan_time_min * 60 # seconds

    def calculate_oee(self, total_run_time, actual_qty, good_qty):
        """
        Availability, Performance, Quality 기반 OEE 산출
        """
        availability = total_run_time / self.plan_time
        performance = (actual_qty / total_run_time) / (self.plan_qty / self.plan_time)
        quality = good_qty / actual_qty if actual_qty > 0 else 0
        
        oee = availability * performance * quality
        return {
            "OEE": round(oee * 100, 2),
            "Bottleneck": "AVAILABILITY" if availability < 0.8 else "PERFORMANCE"
        }

    def calculate_cpk(self, data, usl, lsl):
        """
        공정 능력 지수(CPK) 계산: (USL-mu)/3s 와 (mu-LSL)/3s 중 최솟값
        """
        mu = np.mean(data)
        sigma = np.std(data)
        
        cpu = (usl - mu) / (3 * sigma)
        cpl = (mu - lsl) / (3 * sigma)
        cpk = min(cpu, cpl)
        
        return {
            "CPK": round(cpk, 4),
            "Status": "STABLE" if cpk > 1.33 else "PROCESS_INCAPABLE"
        }

# Example Usage:
# tool = ProductionAnalyticsTool(plan_qty=1000, plan_time_min=480)
# oee_report = tool.calculate_oee(total_run_time(sec)=25000, actual_qty=950, good_qty=940)
# cpk_report = tool.calculate_cpk(data=[10.1, 10.2, 10.0, 10.3], usl=10.5, lsl=9.5)
```

## 5. [스스로 체크 (Self-Audit)]
1. 세방리튬배터리 면접에서 **"OEE를 5% 개선하기 위해 어떤 데이터에 집중하겠는가?"**라는 질문을 받았을 때, 가동 손실(Availability Loss)과 성능 손실(Performance Loss)의 차이를 들어 답변하시오.
2. **CPK**가 $1.0$ 미만으로 떨어졌을 때, 단순 '작업자 교육'이 아닌 '설비 파라미터(DOF)' 관점에서 해결책을 제시하는 논리는?
3. **IIoT** 환경에서 **OPC-UA** 프로토콜이 기존 하드와이어링 방식 대비 '데이터 무결성(Integrity)' 확보에 있어 가지는 강점은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/09_SmartFactory_Production/ControlSystems/Control Statistical-Process-Control
- 02_Knowledge/02_Battery/Battery W12_smart-factory-architecture
- 02_Knowledge/03_AI_Data/Industrial/AI Quality-Control-AI

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**