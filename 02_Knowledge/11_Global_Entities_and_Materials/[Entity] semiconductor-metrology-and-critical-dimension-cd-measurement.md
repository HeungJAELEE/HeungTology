---
metadata:
  id: "[[[Entity] semiconductor-metrology-and-critical-dimension-cd-measurement]]"
  domain: "11_Global_Entities_and_Materials"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Entity] semiconductor-metrology-and-critical-dimension-cd-measurement에 관한 고밀도 지능 노드"
semantic:
  tags: ["#11_Global_Entities_and_Materials", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Entity] semiconductor-metrology-and-critical-dimension-cd-measurement

## 1. 개요 (Why)
"측정할 수 없으면 제어할 수 없고, 제어할 수 없으면 수율을 확보할 수 없다." 반도체 미세 공정에서 나노미터 단위의 선폭(CD)이나 층간 정렬(Overlay) 오차는 곧바로 소자 불량으로 이어집니다. 계측(Metrology)은 공정의 눈 역할을 하며, 실시간 피드백을 통해 공정 변동을 억제합니다. 본 노드는 나노 스케일 제조의 무결성을 보장하기 위한 계측 표준 및 물리적 제어 기준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Target Value (Tier 1) | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- |
| CD Precision (3$\sigma$) | $\sigma_{cd}$ | < 0.1 | ±0.02 | nm |
| Overlay Accuracy | $OVL$ | < 1.0 | ±0.1 | nm |
| Beam Energy (SEM) | $E_b$ | 300 ~ 1000 | ±10 | eV |
| Sampling Rate | $S$ | > 50 | N/A | sites/wafer |
| Measurement Speed | $t_{meas}$ | < 0.5 | ±0.05 | sec/site |

## 3. SemiFidelityEngine: Diagnostic Logic

계측 데이터의 신뢰성 및 공정 산포를 진단하는 `SemiFidelityEngine` 로직입니다.

```python
import numpy as np

class SemiFidelityEngine:
    def __init__(self, cd_values, target_cd, tolerance):
        self.data = np.array(cd_values)
        self.target = target_cd
        self.tol = tolerance

    def diagnose_process_capability(self):
        """Cpk(공정능력지수) 기반 반도체 선폭 안정성 진단"""
        mu = np.mean(self.data)
        sigma = np.std(self.data)
        if sigma < 0.01: return "OPTIMAL: Extreme Precision (Sigma < 0.01nm)"
        
        cpk = min((self.target + self.tol - mu)/(3*sigma), (mu - (self.target - self.tol))/(3*sigma))
        if cpk < 1.67:
            return f"CRITICAL: CD Distribution Drift (Cpk: {cpk:.2f}) - Recalibrate Litho"
        return f"PASS: High-Fidelity Process (Cpk: {cpk:.2f})"

    def audit_measurement_repeatability(self, repeats):
        """반복 측정 데이터의 정밀도(Repeatability) 진단"""
        precision = np.std(repeats)
        if precision > 0.05:
            return f"REJECT: Metrology Tool Jitter High ({precision:.3f}nm)"
        return "PASS: Tool Measurement Reliable"

engine = SemiFidelityEngine(cd_values=[5.01, 4.99, 5.02, 5.00, 4.98], target_cd=5.0, tolerance=0.1)
print(engine.diagnose_process_capability())
```

## 4. 분석 프레임워크: Metrology Intelligence Hierarchy
1. **[CD-SEM (Scanning Electron Microscopy)]**: 저가속 전압 전자빔을 사용하여 포토레지스트나 식각된 패턴의 실제 형상을 2D/3D로 직접 계측.
2. **[OCD (Optical Critical Dimension)]**: 빛의 회절 패턴(Scatterometry)을 분석하여 박막 두께와 복잡한 3D 나노 구조(FinFET, GAA 등)의 치수를 간접적으로 고속 계측.
3. **[Run-to-Run (R2R) Control]**: 계측된 데이터를 리소그래피나 식각 설비에 즉각 전송하여 다음 웨이퍼의 공정 조건을 자동 미세 조정하는 피드백 루프.

## 5. 스스로 체크 (Self-Audit)
1. CD-SEM에서 '저가속 전압(Low Acceleration Voltage)'을 사용하는 이유 중 '웨이퍼 데미지'와 '차징(Charging)' 억제와의 물리적 상관관계는?
2. OCD 계측이 CD-SEM 대비 '비파괴' 및 '전수 검사' 측면에서 갖는 경제적 우위의 수학적 근거는?
3. 오버레이($Overlay$) 오차가 선폭($CD$) 오차보다 수율에 더 지배적인 영향을 미치는 공정 단계(예: Double Patterning)는?

## 6. 결론 (Deterministic Outcome)
본 노드는 `Data semiconductor-metrology-precision-and-p2p-log-v2026`와 연동되어, 나노미터 단위의 치수 변동을 실시간 감시하고 6-Sigma 품질 수준을 유지함으로써 반도체 양산 수율을 95% 이상으로 사수합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 10_semiconductor-and-nanofabrication-intelligence-hub
- cd-sem-imaging-physics
- Data semiconductor-metrology-precision-and-p2p-log-v2026
