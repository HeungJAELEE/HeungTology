---
Basic:
  id: "SEM-LITH-2026-V6"
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
  tags: - '#Lithography'
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

# [[[Semiconductor] Lithography

## 1. [왜 배우는가? (Why)]]
반도체 리소그래피(Lithography)는 실리콘 웨이퍼 위에 나노미터 단위의 초미세 회로 패턴을 전사하는 반도체 제조의 핵심 중의 핵심 공정입니다. 무어의 법칙(Moore's Law)이 지속될 수 있는 동력은 얼마나 더 작은 선폭을 균일하게 그려내느냐에 달려 있으며, 이는 곧 노광 장비의 해상도(Resolution) 한계 극복 역사와 궤를 같이합니다. 특히 ArF에서 EUV(극자외선), 그리고 High-NA EUV로의 전환은 단순히 장비 교체가 아닌 광학, 화학, 기계 공학의 한계를 시험하는 기술적 도약입니다. 이 공정을 이해하는 것은 현대 반도체 성능 향상의 물리적 원천과 전 세계 반도체 공급망의 전략적 급소(Choke Point)를 파악하는 것과 같습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter / Metric | ArF Immersion | EUV (Standard) | High-NA EUV | Engineering Rationale |
|:---|:---:|:---:|:---:|:---|
| **Wavelength ($\lambda$)** | 193 nm | 13.5 nm | 13.5 nm | 파장이 짧을수록 해상도($R$) 개선 |
| **Numerical Aperture (NA)** | 1.35 | 0.33 | 0.55 | 개구수가 클수록 빛 집속력 향상 |
| **Resolution ($R$)** | ~38 nm | ~13 nm | ~8 nm | $k_1 \times \lambda / NA$ 에 의한 물리적 한계 |
| **Depth of Focus ($DOF$)** | $> 100 nm$ | ~50 nm | $< 30 nm$ | 공정 마진 확보를 위한 수직적 초점 범위 |
| **MEEF** | $> 3.0$ | $1.5 \sim 2.5$ | $< 1.5$ | 마스크 오차가 패턴에 증폭되는 지수 |
| **ASML Equipment** | NXT:2050i | NXE:3600D | EXE:5000/5200 | 세대별 대표 노광 장비 모델 |
| **Throughput (WPH)** | $> 275$ | $160 \sim 180$ | Target $220$ | 시간당 웨이퍼 처리량 (생산성 지표) |
| **Optics Type** | Refractive | Reflective | Anamorphic | 렌즈 투과형 vs 거울 반사형 아키텍처 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 노광 해상도의 물리적 한계 (Rayleigh Criterion)
리소그래피의 해상도는 빛의 회절(Diffraction) 현상에 의해 제한되며, 아래 수식에 의해 결정됩니다.
$$R = k_1 \cdot \frac{\lambda}{NA}$$
- $k_1$: 공정 계수 (물리적 한계치 0.25).
- $\lambda$: 광원의 파장 (EUV 도입으로 14배 단축).
- $NA$: 개구수 ($n \cdot \sin \theta$).

### 3.2 초점 심도 (Depth of Focus, $DOF$)
해상도를 높이기 위해 $NA$를 키우면 수직 방향의 초점 여유인 $DOF$가 급격히 감소하는 트레이드오프가 발생합니다.
$$DOF = k_2 \cdot \frac{\lambda}{NA^2}$$
High-NA ($NA=0.55$) 공정에서는 $DOF$가 극도로 얇아지므로 웨이퍼 평탄도(Planarization)와 고도의 스캐너 제어 기술이 필수적입니다.

### 3.3 High-NA EUV의 아나모픽 광학계 (Anamorphic Optics)
0.55 NA를 구현하기 위해 입사각이 커지면 마스크의 반사율이 저하되는 문제가 발생합니다. 이를 해결하기 위해 수평(X)과 수직(Y) 방향의 배율을 다르게 설정(예: X=4x, Y=8x)하는 아나모픽 설계가 도입되었습니다. 이는 단일 노광 가능 면적(Field Size)을 절반으로 줄이는 결과를 가져오지만, 초미세 패턴 구현을 위한 필연적 선택입니다.

## 4. [코드 연결 해설 (Computational Lithography & OPC)]
아래 코드는 광학 근접 효과(OPC) 시뮬레이션을 통해 마스크 패턴의 왜곡을 사전에 보정하는 개념적 로직입니다.

```python
import numpy as np
from scipy.signal import convolve2d

class LithographySimulator:
    """
    HDS-Gold V6.3.7 규격의 연산 리소그래피 시뮬레이터
    """
    def __init__(self, wavelength=13.5, na=0.33, k1=0.25):
        self.wavelength = wavelength
        self.na = na
        self.resolution = k1 * wavelength / na

    def generate_psf(self, size=21):
        """
        Point Spread Function (점 확산 함수) 생성 - 광학적 회절 모사
        """
        sigma = self.resolution / 2.355
        x = np.linspace(-size//2, size//2, size)
        y = np.linspace(-size//2, size//2, size)
        xx, yy = np.meshgrid(x, y)
        psf = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
        return psf / psf.sum()

    def simulate_exposure(self, mask_layout):
        """
        마스크 이미지를 광학계(PSF)와 컨볼루션하여 웨이퍼 전사 이미지 생성
        """
        psf = self.generate_psf()
        wafer_image = convolve2d(mask_layout, psf, mode='same')
        return (wafer_image > 0.5).astype(float) # Thresholding

    def apply_opc(self, target_layout):
        """
        간이 OPC: 왜곡이 예상되는 모서리에 보정 패턴(Serif) 추가
        """
        opc_mask = target_layout.copy()
        # Edge Detection 및 Serif 주입 로직 (생략)
        # 0.33 NA vs 0.55 NA의 수차(Aberration) 보정 파라미터 적용
        return opc_mask

# Example Implementation
# simulator = LithographySimulator(na=0.55) # High-NA 모드
# wafer_pattern = simulator.simulate_exposure(my_design)
```

## 4. [스스로 체크 (Self-Audit)]
1. **Rayleigh Criterion** 수식에서 $NA$를 높일 때 $DOF$가 제곱 비례로 감소하는 공학적 이유는 무엇인가?
2. EUV 공정에서 **Reflective Mirror** 시스템의 반사율이 약 70% 수준인 점이 광원의 초기 출력(Source Power) 요구량에 미치는 파급 효과는?
3. **High-NA EUV** 도입 시 기존 0.33 NA 대비 마스크 필드 크기가 절반으로 줄어드는 'Half-field' 이슈를 해결하기 위한 스티칭(Stitching) 공정의 난제는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Etching
- 02_Knowledge/01_Semiconductor/Process/Semiconductor Deposition
- 02_Knowledge/03_AI_Data/Industrial/AI Computer-Vision

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
