---
Basic:
  id: "SEM-CLEAN-2026-V6"
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
  tags: - '#Semiconductor'
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

# [[[Semiconductor] Cleaning

## 1. [왜 배우는가? (Why)]]
반도체 제조는 나노 스케일의 오염물질과의 사투입니다. 머리카락 굵기의 수만 분의 일에 해당하는 단일 입자(Particle)나 금속 이온 하나가 회로의 절연 파괴, 누설 전류 증가, 혹은 포토리소그래피의 DOF 불량을 유발하여 칩 전체를 폐기물로 만들 수 있습니다. 세정(Cleaning) 공정은 반도체 전체 공정의 약 30% 이상을 차지하며, 매 주요 공정 전후에 배치되어 웨이퍼 표면의 물리적·화학적 순수성을 복원합니다. 특히 3nm 이하의 초미세 공정에서는 세정액의 표면 장력이 패턴을 붕괴시키는 '패턴 리닝(Pattern Leaning)' 문제를 해결해야 하며, 이를 위한 건식 및 초임계 세정 기술은 차세대 수율 확보의 핵심 인텔리전스입니다.

## 2. [세정 공정 핵심 기술 사양 (Cleaning Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---:|:---:|:---|
| **PRE (Efficiency)** | Particle Removal | $> 99.5\% @ 10\text{nm}$ | 초미세 입자 제거 능력을 통한 수율 보증 |
| **Metal Contam.** | Ion Concentration | $< 10^{10} \text{ atoms/cm}^2$ | 소자 신뢰성 및 게이트 산화막 품질 확보 |
| **Zeta Potential** | Surface Charge | $> |30| \text{ mV}$ | 입자의 재부착(Re-deposition) 방지 정전기력 |
| **Etch Amount** | Oxide Removal | $1 \sim 5 \text{ \AA/step}$ | 하부 막질 손상 최소화와 오염물 제거의 균형 |
| **Surface Tension** | Drying Liquid | $< 20 \text{ mN/m}$ (IPA) | 건조 시 마랑고니 효과 유도 및 패턴 보호 |
| **Cleaning Temp.** | SC-1 / SC-2 | $45 \sim 75 ^\circ\text{C}$ | 화학 반응 속도 제어 및 기판 열화 방지 |
| **Megasonic Freq.** | Ultrasonic Input | $1 \sim 3 \text{ MHz}$ | 물리적 타격력 제어 및 미세 패턴 손상 방지 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 DLVO 이론 및 입자 부착/탈착 메커니즘
웨이퍼 표면과 오염 입자 사이의 상호작용을 정량화합니다.
$$ V_{total} = V_{vdw} + V_{edl} $$
*   **$V_{vdw}$ (Van der Waals Force)**: 입자를 표면에 끌어당기는 인력입니다.
*   **$V_{edl}$ (Electrostatic Double Layer Force)**: 제타 전위에 의해 발생하는 반발력입니다.
*   **로직**: 세정액의 pH를 조절하여 웨이퍼와 입자가 같은 극성의 전하를 띠게 함으로써, $V_{edl}$이 $V_{vdw}$를 압도하는 '에너지 장벽'을 형성하여 입자의 재부착을 근원적으로 차단합니다.

### 3.2 마랑고니 건조 (Marangoni Drying) 및 표면 장력 구배
세정 후 수분을 제거할 때 패턴 붕괴를 막는 핵심 유체역학 원리입니다.
*   **원리**: 웨이퍼를 순수(DIW)에서 끌어올릴 때 IPA 증기를 분사하여, 액막 상부와 하부 사이의 농도 차에 의한 '표면 장력 구배'를 발생시킵니다.
*   **효과**: 표면 장력이 낮은 곳에서 높은 곳으로 유체가 흐르는 성질을 이용하여, 미세 패턴 사이의 수분을 외부로 빨아냄으로써 모세관력에 의한 패턴 리닝을 방지합니다.

### 3.3 [SC-1 (Standard Clean 1) 산화-식각 시너지 분석 관점: Redox & Lift-off Hub]
- **로직**: $H_2O_2$가 표면을 화학적으로 산화시키고, $NH_4OH$가 그 산화막을 얇게 식각(Etch-back)해내며 입자를 들어 올리는(Lift-off) 방식입니다.
- **RAG 추론**: 화학액 농도 데이터(Data semi-clean-chem-log-v2026)를 분석하여, "암모니아 농도 저하에 따른 제타 전위 역전 현상 및 입자 재흡착 위험"을 실시간으로 감지합니다.

## 4. [코드 연결 해설 (Contamination Detection & Yield Correlation Engine)]
아래 코드는 스캐닝 장비의 결함 데이터(Defect Map)를 분석하여 세정 공정의 효율을 계산하고, 특정 구역의 오염 집중도를 바탕으로 세정 장비의 노즐 막힘 여부를 판별하는 로직입니다.

```python
class CleaningEfficiencyAnalyzer:
    """
    HDS-Gold V6.3.7 규격의 입자 제거 효율(PRE) 및 결함 클러스터 분석 엔진
    """
    def __init__(self, target_pre=99.8):
        self.target_pre = target_pre

    def run_pre_validation(self, pre_count, post_count, wafer_map):
        """
        세정 전후 입자 수 비교 및 결함 클러스터링 기반 장비 진단
        """
        # 1. 입자 제거 효율(PRE) 산출
        current_pre = ((pre_count - post_count) / pre_count) * 100
        
        # 2. 클러스터 분석 (특정 위치에 오염이 집중되는지 확인)
        cluster_density = self._detect_defect_clusters(wafer_map)
        
        if current_pre < self.target_pre:
            if cluster_density > 0.4:
                return "FAIL_ACTION: CHECK_NOZZLE_ALIGNMENT_AND_PRESSURE"
            else:
                return "FAIL_ACTION: REPLENISH_CLEANING_CHEMICALS"
        
        return {"status": "PASS", "pre": round(current_pre, 3)}

    def _detect_defect_clusters(self, map_data):
        # 결함 좌표 데이터를 이용한 밀집도 분석 수리 모델
        return np.mean(map_data) # 단순화된 예시
```

## 5. [스스로 체크 (Self-Audit)]
1. **DHF** (Diluted HF) 공정 후 웨이퍼 표면이 **Hydrophobic** (소수성) 상태가 되었을 때, 'Water Mark' 결함을 방지하기 위한 건식 공정 설계의 핵심은?
2. **Megasonic** 세정 시 주파수가 높아질수록(High Frequency) 캐비테이션 에너지는 낮아지지만 **Acoustic Streaming**은 강화되어 미세 패턴 보호에 유리한 이유는?
3. **Supercritical $CO_2$** 세정이 10nm 이하의 극미세 패턴 세정에서 표면 장력 문제를 완전히 해결할 수 있는 물리적 근거는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Lithography
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Etching
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Deposition

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-09]**
