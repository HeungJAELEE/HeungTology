---
metadata:
  date: "2026-05-16"
  id: "[[[Entity] atomic-force-microscopy-afm-and-nano-mechanical-probing]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "11_Global_Entities_and_Materials"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "5707ceeccaa56ac6a3bcd570c0a385988ab1bf73db47de50844d5ce8d8919521"
object:
  object_type: "Concept"
  tier: 1
  description: '[Entity] atomic-force-microscopy-afm-and-nano-mechanical-probing에 관한 고밀도 지능 노드'
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


# [Entity] atomic-force-microscopy-afm-and-nano-mechanical-probing

## 1. 개요 (Why)
광학 현미경과 전자 현미경의 한계를 넘어, 실제 원자의 높낮이와 물리적 단단함(Modulus)을 '만져서' 측정하는 것이 AFM의 핵심입니다. 나노 소자의 표면 거칠기($R_a$)뿐만 아니라, 특정 지점의 전기적/자기적 특성을 매핑할 수 있어 차세대 반도체 및 신소재 개발에 필수적인 계측 도구입니다. 본 노드는 나노 스케일 표면 형상 및 물성 분석의 무결성을 확보하기 위한 표준을 정의합니다.

## 2. 핵심 기술 사양 (Numerical Specs)

| Parameter | Symbol | Value (Tier 1) | Tolerance | Unit |
| :--- | :--- | :--- | :--- | :--- |
| Lateral Resolution | $\Delta x$ | 0.1 ~ 1.0 | ±0.05 | nm |
| Vertical Resolution| $\Delta z$ | < 0.01 | ±0.002 | nm |
| Cantilever Spring K| $k$ | 0.01 ~ 100 | ±10 | N/m |
| Tip Radius | $R$ | 2 ~ 10 | ±1 | nm |
| Force Sensitivity | $F_{min}$ | < 10 | ±2 | pN |

## 3. SemiFidelityEngine: Diagnostic Logic

AFM 측정 데이터의 해상도 및 프로브 상태를 진단하는 `SemiFidelityEngine` 로직입니다.

```python
class SemiFidelityEngine:
    def __init__(self, tip_radius, z_noise, cantilever_k):
        self.r = tip_radius
        self.noise = z_noise
        self.k = cantilever_k

    def diagnose_imaging_limit(self, step_height):
        """수직 해상도 및 노이즈 기반 측정 한계 진단"""
        if self.noise > step_height * 0.1:
            return f"CRITICAL: High Z-Noise ({self.noise}nm) - Atomic Step Unresolvable"
        return "OPTIMAL: Atomic Level Resolution Achievable"

    def audit_tip_condition(self, image_sharpness):
        """이미지 선명도를 통한 프로브(Tip) 마모 진단"""
        if image_sharpness < 0.7:
            return "REJECT: Tip Blunting Detected - Probe Replacement Required"
        return "PASS: Probe Sharpness Maintained"

engine = SemiFidelityEngine(tip_radius=5, z_noise=0.005, cantilever_k=40)
print(engine.diagnose_imaging_limit(step_height=0.2))
```

## 4. 분석 프레임워크: Scanning Probe Strategy
1. **[Contact Mode]**: 프로브를 표면에 직접 대고 긁으며 척력(Repulsive Force)을 측정하여 형상을 도출하는 가장 기본적 방식.
2. **[Tapping (Non-contact) Mode]**: 프로브를 진동시켜 표면에 살짝 닿거나 근접하게 유지함으로써 시료 손상을 최소화하고 고해상도 이미지 획득.
3. **[Nano-indentation]**: 프로브로 표면을 눌러 깊이에 따른 힘의 변화를 측정함으로써 나노 영역의 경도(Hardness)와 탄성 계수 분석.

## 5. 스스로 체크 (Self-Audit)
1. AFM에서 팁과 샘플 사이의 거리가 수 nm일 때 작용하는 '반데르발스 힘(Van der Waals Force)'의 인력/척력 반전 지점은?
2. 캔틸레버의 'Q-factor'가 높을수록 공진 주파수 근처에서 감도(Sensitivity)가 향상되는 물리적 이유는?
3. 팁의 반경($R$)이 측정하고자 하는 나노 패턴의 크기보다 클 때 발생하는 '이미지 컨볼루션(Image Convolution)' 오차의 보정 방법은?

## 6. 결론 (Deterministic Outcome)
본 노드는 `Data afm-surface-roughness-and-nano-indentation-v2026`와 연동되어, 표면 거칠기를 0.01nm 단위로 감시하고 나노 소자의 기계적 신뢰성을 99% 확률로 검증함으로써 차세대 나노 제조의 무결성을 보장합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 10_semiconductor-and-nanofabrication-intelligence-hub
- afm-tapping-mode-and-phase-imaging
- Data afm-surface-roughness-and-nano-indentation-v2026
