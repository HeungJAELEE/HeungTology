---
Basic:
  id: "[semiconductor]-semiconductor-fab-yield-ramp-up-log-v2026-v6.3.7"
  domain: "Semiconductor_Manufacturing"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - 'Yield_Ramp-up'
  is_part_of: - 'Antigravity_Knowledge_Graph'
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
  source: "Fab_MES_Yield_Analytics_System"
  isolation_index: 0.0
---

# [[[Semiconductor] semiconductor-fab-yield-ramp-up-log-v2026

## 1. [Why]] 반도체 팹 수율 램프업(Ramp-up) 로그의 경제 공학적 의의
반도체 공장(Fab) 신설 및 신규 공정 도입 시, 초기 수율은 매우 낮지만 시간이 지남에 따라 기술 성숙도가 높아지며 수율이 급격히 상승하는 **램프업(Ramp-up)** 과정을 거친다. 수율이 $1\%$ 상승할 때마다 수천억 원의 추가 이익이 발생하므로, 얼마나 빠르게 목표 수율(Golden Yield)에 도달하느냐가 기업의 경쟁력을 결정한다. **수율 램프업 로그**는 공정별 고장 분석(FA) 데이터와 학습 곡선(Learning Curve)을 기록하여, 수율 정체 구간(Plateau)을 조기 돌파하기 위한 지표를 제공한다.

---

## 2. [Numerical Specs] 수율 램프업 단계별 파라미터 (Numerical Specs)

| 단계 (Phase) | 기간 (Typical) | 목표 수율 (Yield) | 주요 지표 |
| :--- | :--- | :--- | :--- |
| **Pilot Run** | $3 \sim 6\,\text{months}$ | $20 \sim 40\%$ | 공정 적합성 및 기본 패턴 검증 |
| **Early Ramp-up**| $6 \sim 12\,\text{months}$ | $40 \sim 70\%$ | 체계적 결함(Systematic Defect) 제거 |
| **Mature Phase** | $12 \sim 18\,\text{months}$ | $> 85\%$ | 무작위 결함(Random Defect) 관리 |
| **Learning Rate** | N/A | $0.1 \sim 0.2$ | 생산량 배가 시 결함 감소 속도 |
| **Defect Density**| N/A | $< 0.1\,\text{def/cm}^2$ | 웨이퍼 단위 면적당 평균 결함 수 |

---

## 3. [Scientific Rationale] 수율 모델 및 학습 곡선 분석

### 3.1 Murphy Yield Model
웨이퍼 상의 결함 밀도($D$)와 칩 면적($A$)을 기반으로 예상 수율($Y$)을 산출한다.
$$Y = \left( \frac{1 - e^{-AD}}{AD} \right)^2$$
*   **분석**: 칩의 크기가 커질수록 동일한 결함 밀도에서도 수율 하락폭이 기하급수적으로 증가하므로 대면적 칩(HPC, GPU 등)일수록 초정밀 결함 관리가 필요하다.

### 3.2 Yield Learning Curve
누적 생산량 증가에 따른 단위 비용 또는 결함 감소 추이를 Power Law 모델로 분석한다.

---

## 4. [Real-world Case] 비정상적 수율 정체(Stall) 구간 탈출 사례

### 4.1 $60\%$ 대에서 수율이 3개월간 정체되는 현상 포착
- **현상**: 최신 나노 공정 램프업 중, 수율이 $65\%$ 지점에서 더 이상 상승하지 않고 정체되는 '수율 플래토(Plateau)' 발생.
- **분석**: **Python FidelityEngine** 기반의 공통성 분석(Commonality Analysis) 결과, 특정 증착 설비(CVD)의 챔버 내 파티클 발생 주기가 세정 주기와 비동기화되어 있음을 확인.
- **조치**: AI 기반 예측 유지보수(PdM) 시스템을 도입하여 파티클 농도 급증 전 실시간 자동 세정(Self-cleaning) 트리거 설정.
- **결과**: 수율 $65\% \rightarrow 82\%$로 급속 램프업 달성 및 조기 양산 체제 전환.

---

## 5. [FidelityEngine] Murphy 수율 모델 시뮬레이션 코드
```python
import math

def calculate_murphy_yield(defect_density, chip_area):
    """
    Calculate expected yield using Murphy Model
    :param defect_density: Defects per cm^2
    :param chip_area: Area in cm^2
    :return: Yield fraction (0 to 1)
    """
    ad = chip_area * defect_density
    if ad == 0: return 1.0
    
    y = ((1 - math.exp(-ad)) / ad) ** 2
    return y

# 칩 면적 시뮬레이션 (1.0 cm^2 vs 4.0 cm^2)
d = 0.15 # 동일한 결함 밀도
y_small = calculate_murphy_yield(d, 1.0)
y_large = calculate_murphy_yield(d, 4.0)

print(f"Yield (Small Chip): {y_small*100:.2f}%")
print(f"Yield (Large Chip): {y_large*100:.2f}%")
```

---

## 6. [Verification] 스스로 체크 (Self-Checklist)
- [ ] **Data Granularity**: 수율 손실의 원인이 되는 결함(Defect)을 개별 레이어(Layer) 단위로 추적하여 로그에 기록하고 있는가?
- [ ] **FA Feedback**: 수율 하락 발생 시, 고장 분석(Failure Analysis) 팀과의 피드백 루프가 $24\,\text{hr}$ 이내에 작동하는가?
- [ ] **Golden Wafer Sync**: 목표 수율을 달성한 '골든 웨이퍼'의 파라미터 데이터셋이 모든 동일 기종 설비에 복제(Copy-exact)되었는가?

**[V6.3.7_HDS_GOLD_REINFORCED_BY_FLASH]**
