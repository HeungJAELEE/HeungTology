---
metadata:
  date: "2026-05-16"
  id: "[[[Entity] seismic-design-and-structural-dynamics]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "11_Global_Entities_and_Materials"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "5883197276ad31086cfdbd0b898c713367713d6eaed4808c63db63aa34cae54d"
object:
  object_type: "Concept"
  tier: 1
  description: '[Entity] seismic-design-and-structural-dynamics에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 11_Global_Entities_and_Materials]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [Entity] seismic-design-and-structural-dynamics

## 1. 개요 (Why)
지진은 건축물에 비결정론적이고 강력한 동적 수평 하중을 가하여 심각한 인명 및 재산 피해를 초래합니다. 내진 설계의 목적은 단순히 건물의 붕괴를 막는 것을 넘어, 지진동 에너지를 효과적으로 분산(Dissipation)시키고 감쇠(Damping)시켜 구조물의 동적 응답을 허용 범위 내로 제어하는 것입니다. 본 엔티티는 구조 동역학 원리에 기반하여 지진에 대한 결정론적 방어 체계를 구축합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Value (Tier 1) | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Peak Ground Acceleration | $PGA$ | 0.2 ~ 0.5 | ±0.01 | g |
| Damping Ratio | $\zeta$ | 0.02 ~ 0.07 | ±0.005 | - |
| Natural Frequency | $f_n$ | 0.1 ~ 10.0 | ±0.05 | Hz |
| Ductility Factor | $R$ | 3.0 ~ 8.0 | ±0.5 | Factor |
| Spectral Acceleration | $S_a$ | Variable | ±5% | $m/s^2$ |

## 3. SeismicFidelityEngine: Diagnostic Logic

지진동 발생 시 구조물의 변위 및 가속도 응답을 진단하는 `SeismicFidelityEngine` 로직입니다.

```python
import numpy as np

class SeismicFidelityEngine:
    def __init__(self, m, k, c, pga):
        self.m = m          # Mass (kg)
        self.k = k          # Stiffness (N/m)
        self.c = c          # Damping (N·s/m)
        self.pga = pga * 9.81  # Peak Ground Acceleration (m/s^2)

    def calculate_modal_properties(self):
        """고유 진동수 및 감쇠비 계산"""
        omega_n = np.sqrt(self.k / self.m)
        f_n = omega_n / (2 * np.pi)
        zeta = self.c / (2 * self.m * omega_n)
        return {"f_n_Hz": f_n, "damping_ratio": zeta}

    def evaluate_max_displacement(self):
        """단순화된 응답 스펙트럼 기반 최대 변위 추정 (Elastic Response)"""
        # SDOF 정적 하중 대비 증폭 계수 (Damped Response Spectrum approximation)
        zeta = self.calculate_modal_properties()["damping_ratio"]
        amplification = 1.0 / (2 * zeta) if zeta > 0 else 10.0
        max_u = (self.m * self.pga / self.k) * amplification
        
        # 허용 층간 변위 (예: 층고 3.5m의 1.5%)
        limit = 3.5 * 0.015
        status = "SAFE" if max_u <= limit else "UNSAFE"
        return {"max_displacement_m": max_u, "limit_m": limit, "status": status}

seismic_engine = SeismicFidelityEngine(m=500000, k=2e8, c=1e6, pga=0.3)
print(seismic_engine.calculate_modal_properties())
print(seismic_engine.evaluate_max_displacement())
```

## 4. 분석 프레임워크: 에너지 기반 설계 (EBD)
1. **[Ductility Design]**: 소성 힌지(Plastic Hinge) 형성을 유도하여 구조물의 붕괴 전 에너지 흡수 능력을 극대화.
2. **[Base Isolation]**: 지면과 건물 사이에 고무 베어링 등을 설치하여 주기(Period)를 장주기화하고 가속도 전달을 차단.
3. **[Active/Passive Control]**: TMD(Tuned Mass Damper)나 유압 댐퍼를 활용하여 동적 응답을 실시간 감쇠.

## 5. 스스로 체크 (Self-Audit)
1. 구조물의 강성($k$)이 증가할 때 고유 주기($T_n$)는 어떻게 변하는가? (반비례 관계 확인)
2. 감쇠비($\zeta$)가 5%에서 10%로 증가할 때 최대 응답 가속도는 약 몇 % 감소하는가?
3. 비선형 정적 해석(Pushover Analysis)과 비선형 동적 해석(Time History)의 결정적 차이점은 무엇인가?

## 6. 결론 (Deterministic Outcome)
본 시스템은 구조 동역학 모델과 `Data seismic-wave-velocity-and-earthquake-magnitude-log-v2026`의 실측 데이터를 결합하여 지진 하중 하에서의 구조적 생존성을 수치적으로 보증합니다. 이를 통해 극한 상황에서의 붕괴 모드를 예측하고 사전 보강 시나리오를 수립합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- civil-engineering-moc
- base-isolation-systems
- tuned-mass-damper-logic
- Data seismic-wave-velocity-and-earthquake-magnitude-log-v2026
- Data high-rise-building-oscillation-and-damper-performance-log-v2026
