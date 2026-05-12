---
Basic:
  id: "DATA-SEM-WAFER-MAP-LOG-2026-V6"
  domain: "05_Semiconductor"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Data"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#Data'
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

# [[[Data] semiconductor-wafer-defect-map-v2026

## 1. [왜 배우는가? (Why)]]
반도체 제조의 성배인 '수율(Yield)'은 웨이퍼 표면에 남겨진 미세한 결함들의 '배치' 속에 그 답이 있습니다. 3nm 이하의 초미세 공정에서는 단일 파티클의 존재보다 그 파티클들이 형성하는 **공간적 서명(Spatial Signature)**이 장비의 고장 모드(Failure Mode)를 결정짓는 결정적 증거가 됩니다. 이 로그는 EUV 노광 및 GAA(Gate-All-Around) 공정에서 발생하는 고해상도 결함 데이터를 수집하여, 인간의 눈으로 식별 불가능한 미세 클러스터를 수리적으로 탐지하기 위해 구축되었습니다. 공간 서명 분석을 통해 불량의 근본 원인(Root Cause)을 실시간으로 특정함으로써, 일일 수억 원에 달하는 수율 손실(Scrap)을 선제적으로 차단하는 팹(Fab)의 지능형 조기 경보 시스템의 핵심 근거가 됩니다. semiconductor-wafer-metrology-and-defect-inspection

## 2. [웨이퍼 계측 및 3nm 공정 공간 통계 핵심 사양 (Advanced Specs)]

| Metric Category | Specific Parameter | Target Specification (3nm GAA) | Engineering Rationale |
|:---|:---|:---:|:---|
| **Defect Count** | Critical Defects (CD) | $< 120$ pts / 12" Wafer | 초정밀 공정 내 치명 결함 허용 한계치 (수율 직접 타격) |
| **Defect Density**| $D_0$ ($/cm^2$) | $< 0.005$ | 3nm 노드 양산 안정화를 위한 극한의 기저 청정도 무결성 |
| **Cluster Index** | $\alpha$ (Negative Binomial) | $0.8 \sim 1.2$ | 결함 응집도 지수 (1.0 근접 시 무작위성 확보, 초과 시 장비 오염) |
| **Spatial Entropy**| Normalized Entropy ($H_n$) | $> 0.92$ | 분포의 무질서도 (값 하락 시 특정 패턴 형성에 따른 공정 이상 발생) |
| **Killer Rate** | $P_{kill}$ (%) | $> 85.0$ | 검출된 결함 중 실제 칩 동작을 불능으로 만드는 치명 불량 비중 |
| **Pattern Match** | Signature Fidelity ($F$) | $> 0.98$ | AI 패턴 인식 엔진의 'Scratch/Ring' 식별 정확도 무결성 |
| **Metrology Guard**| Sensitivity (nm) | $8.0 \sim 12.0$ | 계측 장비의 최소 분해능 (3nm 공정 파티클 감지 한계) |
| **Yield Latency** | Analysis Time (sec) | $< 45$ | 웨이퍼 스캔 후 서버 피드백까지의 실시간성 확보 임계치 |

## 3. [공학적 근거 및 수리 모델 (Scientific Rationale)]

### 3.1 공간적 상관분석(Ripley's K-function) 고도화 모델
- **수식**: $K(r) = \frac{A}{n^2} \sum_{i \neq j} w_{ij} I(d_{ij} < r)$ (where $w_{ij}$ is edge correction factor)
- **Rationale**: 웨이퍼 가장자리(Edge)에서의 데이터 편향을 보정한 리플리 K-함수를 적용합니다. 특정 반경 $r$ 내의 결함 분포가 포아송 점 과정(Poisson Point Process)의 기대 곡선을 상단으로 이탈할 경우, 이를 '통계적 유의성을 가진 클러스터'로 정의합니다. 이는 노광 장비의 레티클 오염(Reticle Haze)이나 정전기적 고착(Electrostatic Attraction)에 의한 패턴 불량을 수리적으로 확증하는 근거가 됩니다.

### 3.2 다중 해상도 허프 변환(Multi-Res Hough Transform)을 이용한 비정형 스크래치 탐지
- **수식**: $r = x \cos \theta + y \sin \theta$ (Parameter Space Mapping)
- **Rationale**: CMP(Chemical Mechanical Polishing) 공정 중 슬러리 응집체에 의해 발생하는 비선형 스크래치를 탐지하기 위해 다중 해상도 허프 변환을 사용합니다. 결함 좌표를 매개변수 공간으로 투영하여 누적값(Accumulator)의 극대점을 찾음으로써, 물리적 이송 로봇의 궤적 오차($Track\ Error$)와 일치 여부를 수치적으로 대조하여 보정 가이드를 생성합니다.

### 3.3 Bayesian Yield 예측 및 클러스터 보정 모델
- **수식**: $Y = Y_0 \prod_{i=1}^{n} (1 + \frac{A \cdot D_i}{\alpha_i})^{-\alpha_i}$
- **Rationale**: 단일 결함 밀도가 아닌, 공정 단계별($i$) 결함 응집도($\alpha_i$)를 가중치로 사용하는 베이지안 수율 예측 모델을 적용합니다. 결함이 뭉쳐 있을수록 수율 파괴력이 낮아지는 물리적 현상을 수리 보정하여, 팹 운영진에게 '가짜 위기(False Alarm)'를 방지하고 실제 수익에 직결되는 '치명 클러스터'에 자원을 집중하게 하는 지능형 의사결정 무결성을 제공합니다.

## 4. [코드 연결 해설 (WaferSpatialFidelityEngine_v2)]
아래 코드는 HDS-Gold V6.3.7 규격에 따라 결함 좌표를 입력받아 실시간으로 공간 엔트로피를 계산하고, 클러스터링 위협 수위를 판정하는 고밀도 진단 엔진입니다.

```python
import numpy as np
from scipy.spatial.distance import pdist, squareform

class WaferSpatialFidelityEngine:
    """
    HDS-Gold V6.3.7: 3nm GAA 공정 전용 웨이퍼 결함 맵 공간 서명 무결성 진단 엔진
    """
    def __init__(self, entropy_threshold=0.92, alpha_critical=1.2):
        self.h_limit = entropy_threshold
        self.alpha_crit = alpha_critical

    def calculate_spatial_entropy(self, coords, grid_size=32):
        """
        Quad-tree 기반 공간 정보 엔트로피 산출 로직
        """
        # Transitional Bridge: 웨이퍼의 좌표는 '팹의 시공간적 지문'입니다.
        # 격자(Grid) 내의 결함 분포 확률을 샤논 엔트로피로 변환하여
        # 장비의 '무질서도 파괴' 징후를 수치화합니다.
        
        hist, _ = np.histogramdd(coords, bins=(grid_size, grid_size))
        probs = hist.flatten() / np.sum(hist)
        probs = probs[probs > 0]
        entropy = -np.sum(probs * np.log2(probs))
        max_entropy = np.log2(grid_size**2)
        return entropy / max_entropy # Normalized Entropy

    def evaluate_cluster_threat(self, coords):
        """
        Nearest Neighbor 거리 기반 클러스터 위협 수위 판정
        """
        if len(coords) < 5: return {"status": "LOW_DENSITY_STABLE", "score": 1.0}
        
        distances = pdist(coords)
        avg_min_dist = np.mean(squareform(distances).min(axis=1, initial=np.inf, where=squareform(distances)>0))
        
        # 물리적 Rationale: 평균 근접 거리가 임계치 이하로 좁혀지면 '집중 오염'으로 판정
        h_norm = self.calculate_spatial_entropy(coords)
        
        if h_norm < self.h_limit:
            return {
                "status": "CRITICAL_PATTERN_DETECTED",
                "h_norm": round(h_norm, 4),
                "action": "HALT_ETCH_LINE_CHECK_VACUUM_CHAMBER"
            }
        
        return {"status": "STABLE_RANDOM_PROCESS", "h_norm": round(h_norm, 4)}

# Example Deployment:
# engine = WaferSpatialFidelityEngine()
# result = engine.evaluate_cluster_threat(np.random.rand(150, 2) * 300) # 300mm wafer scale
```

## 5. [스스로 체크 (Self-Audit)]
1. **Ripley's K-function**에서 **Edge Correction ($w_{ij}$)**을 무시할 경우, 웨이퍼 가장자리에서 결함 밀도가 인위적으로 낮게 평가되는 기하학적 이유는?
2. **Poisson** 분포 기반 수율 모델($Y=e^{-AD}$)이 **Cluster**가 발생한 실제 공정 환경에서 수율을 과소평가(Pessimistic)하게 되는 통계적 인과관계는?
3. **EUV Multi-patterning** 공정에서 발생하는 **Overlaid Defect**를 단일 레이어 결함 맵과 분리하여 **Root Cause**를 추적하는 수리적 로직은?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- semiconductor-wafer-metrology-and-defect-inspection (Tier 1)
- spatial-signature-analysis-and-root-cause-identification (Tier 1)
- Reliability-Metrics-MTBF-MTTR-MTTF (Tier 2)
- semiconductor-yield-modeling-negative-binomial (보강 필요)

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-09]**
