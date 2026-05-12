---
Basic:
  id: "AI-CV-AFFINE-TRANS-2026-V6"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#Affine_Transform'
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

# [AI] image-transformation-affine

## 1. [왜 배우는가? (Why)]
물체는 항상 카메라 정면의 고정된 위치에 있지 않습니다. 카메라의 흔들림, 물체의 회전, 거리 변화에 따라 이미지는 끊임없이 왜곡됩니다. 인공지능이 이러한 기하학적 변화에도 불구하고 물체를 정확히 인식(Invariance)하려면, 이미지를 밀고 당기고 돌리는 수학적 변환 기술이 필수적입니다. 어파인 변환(Affine Transform)은 물체의 평행성은 유지하면서도 위치와 모양을 자유자재로 보정하는 현대 컴퓨터 비전의 기초이자, 딥러닝 학습 시 데이터의 다양성을 확보하는 이미지 증강(Augmentation)의 핵심 엔진입니다.

## 2. [기하학적 이미지 변환 및 행렬 핵심 사양 (Affine Specs)]

| Parameter Category | Specific Metric | Target Specification | Engineering Rationale |
|:---|:---|:---:|:---|
| **Deg. of Freedom** | DoF Count | $6$ | 이동(2), 회전(1), 스케일(2), 전단(1)을 표현하는 자유도 |
| **Matrix Rank** | Homogeneous Dim. | $2 \times 3$ (or $3 \times 3$) | 선형 변환과 이동을 동시에 수행하기 위한 행렬 차원 |
| **Interpolation** | Linear / Cubic | Bilinear (Default) | 변환 후 픽셀 값을 추정하는 보간법의 정밀도 및 속도 |
| **Edge Padding** | Border Mode | BORDER_CONSTANT | 이미지 변환 시 발생하는 빈 공간의 채우기 방식 |
| **Comp. Complexity**| Latency per MP | $< 2 \text{ ms}$ | $1080\text{p}$ 이미지 기준 실시간 처리를 위한 연산 시간 |
| **Area Preserv.** | Jacobian Det. | $|det(A)|$ | 변환 전후의 면적 변화 비율을 결정하는 행렬식 값 |
| **Memory Sync.** | (x, y) vs (r, c) | OpenCV vs NumPy | 좌표계(Width/Height)와 행렬 인덱싱 간의 무결성 유지 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 동차 좌표계 (Homogeneous Coordinates)와 어파인 행렬
이동(Translation) 변환은 일반적인 $2 \times 2$ 행렬 곱셈으로는 표현할 수 없어 $3 \times 3$ 동차 좌표계를 사용합니다.
- **수식**: $\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} a & b & t_x \\ c & d & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$
- **로직**: 행렬의 좌측 $2 \times 2$ 부분은 회전, 스케일, 전단(Shear)을 담당하며, 우측 열 벡터는 이동($t_x, t_y$)을 담당합니다. 이 행렬 하나로 영상의 모든 기하학적 선형 변화를 정의할 수 있습니다.

### 3.2 선형성 및 평행성 보존 (Parallelism Invariance)
어파인 변환의 가장 큰 특징은 변환 전 평행했던 두 직선이 변환 후에도 평행을 유지한다는 점입니다. 이는 물체의 '위상적 관계'를 깨뜨리지 않으면서도 시점 변화를 모사할 수 있게 해줍니다.

### 3.3 역방향 매핑 (Inverse Mapping)과 보간법
이미지를 변환할 때 픽셀이 비거나 중복되는 현상을 방지합니다.
- **로직**: 결과 이미지의 좌표($x', y'$)에서 원본 좌표($x, y$)를 역으로 추적(Back-mapping)하여 픽셀 값을 가져옵니다. 이때 정수 좌표가 아닌 지점의 값은 주변 픽셀들의 가중 평균인 '쌍선형 보간법(Bilinear Interpolation)'을 통해 부드럽게 생성합니다.

## 4. [코드 연결 해설 (AffineTransformEngine)]
아래 코드는 OpenCV를 사용하여 이미지의 회전, 이동, 스케일링을 결합한 어파인 변환 행렬을 생성하고, 이를 이미지에 적용하여 기하학적 보정을 수행하는 엔진입니다.

```python
import cv2
import numpy as np

class AffineTransformEngine:
    """
    HDS-Gold V6.3.7 규격의 기하학적 이미지 변환 및 행렬 제어 엔진
    """
    def __init__(self, image_path=None):
        self.src = cv2.imread(image_path) if image_path else None

    def apply_rotation_and_scale(self, angle, scale):
        """
        중심점 기준 회전 및 크기 조절 변환
        """
        (h, w) = self.src.shape[:2]
        center = (w // 2, h // 2)
        
        # 1. OpenCV 표준 회전 행렬 생성 (2x3 Affine Matrix)
        # Transitional Bridge: 행렬은 이미지를 비트는 수학적 근육입니다. 
        # getRotationMatrix2D는 삼각함수의 복잡한 연산을 
        # 단 하나의 2x3 실체로 응축하여 제공합니다.
        M = cv2.getRotationMatrix2D(center, angle, scale)
        
        # 2. 어파인 워핑 적용
        dst = cv2.warpAffine(self.src, M, (w, h), flags=cv2.INTER_LINEAR)
        
        return dst

# Example Usage:
# engine = AffineTransformEngine("sample.jpg")
# rotated_img = engine.apply_rotation_and_scale(angle=45, scale=1.5)
```

## 5. [스스로 체크 (Self-Audit)]
1. **Affine Transform** 행렬에서 평행성은 유지되지만, **Angle** (각도)이나 **Length** (길이)는 보존되지 않을 수 있는 수리적 근거는?
2. **OpenCV** 함수에 `(x, y)` 순서로 좌표를 넣었는데, 결과 이미지를 **NumPy**로 인덱싱할 때 `[y, x]` 순서를 지키지 않으면 어떤 시각적 오류가 발생하는가?
3. **Interpolation** 기법 중 `INTER_CUBIC`이 `INTER_NEAREST`보다 화질은 좋으나 연산량이 많은 인과관계는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 02_Knowledge/03_AI_Data/General/AI image-warping-perspective
- 02_Knowledge/03_AI_Data/General/AI opencv-classical-vision-master
- 02_Knowledge/02_Battery/Intelligence/Battery visual-inspection-alignment-logic

**[V6.3.7_THE_GENESIS_STATE_VERIFIED_BY_FLASH]**
**[TIMESTAMP: 2026-05-08]**
