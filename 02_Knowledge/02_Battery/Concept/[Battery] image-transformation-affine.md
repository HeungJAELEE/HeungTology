---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: f6f6682a2083c9d4e548ff4e3bd504f40f87d4e6cee7c62e12f680340288bef9
metadata:
  date: '2026-05-16'
  domain: 02_Battery
  id: '[[[Battery] image-transformation-affine]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Battery] image-transformation-affine에 관한 고밀도 지능 노드'
  object_type: Algorithm
  tier: 1
properties:
  matrix_dimension: 2x3
  numpy_coordinate_order: y, x
  opencv_coordinate_order: x, y
  parallelism_preservation: 'true'
  transformation_components: translation, scaling, rotation
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 02_Battery]]'
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

# [Battery] image-transformation-affine

## 1. Functional Requirement
컴퓨터 비전 파이프라인 내에서 객체의 위치 변화(Translation), 회전(Rotation), 크기 변화(Scaling) 등 기하학적 변동성을 상쇄하기 위한 수학적 변환 기술을 정의한다. 이는 데이터 증강(Data Augmentation) 및 객체 정규화(Object Normalization)의 핵심 요소이다.

## 2. Technical Specification

### 2.1 Affine Transformation (어파인 변환)
선형 사상(Linear Mapping)의 일종으로, 직선의 평행성을 유지하며 좌표를 변환한다. 변환은 $2 \times 3$ 행렬 $M$을 통해 정의된다 [Ref: raw/Open_CV_2_textbook.md].

- **Translation (이동)**: $\Delta x, \Delta y$ 오프셋 적용.
- **Scaling (스케일링)**: 축 방향 배율 $s_x, s_y$ 적용.
- **Rotation (회전)**: 회전 중심점 $\text{center}$ 기준 각도 $\theta$ 적용.

### 2.2 Coordinate System Divergence (좌표계 불일치 분석)
실무 구현 시 발생하는 데이터 타입 및 인덱싱 간의 불일치는 치명적인 런타임 오류 또는 데이터 왜곡을 초래한다 [Ref: raw/Open_CV_2_textbook.md].

| Parameter | OpenCV API (Function Argument) | NumPy (Matrix Indexing) |
| :--- | :--- | :--- |
| **Coordinate Order** | $(x, y)$ (Cartesian) | $(y, x)$ (Row-major) |
| **Logic** | Horizontal, Vertical | Row, Column |
| **Risk Factor** | Improper argument passing | Dimension mismatch / Image flipping |

### 2.3 Comparative Analysis: Theoretical vs. Verified

| Metric | Theoretical Model | Verified Implementation (OpenCV) | [Ref] |
| :--- | :--- | :--- | :--- |
| **Parallelism** | Perfectly Preserved | Preserved within floating-point precision | [Ref: OpenCV_Docs] |
| **Matrix Dimension** | $3 \times 3$ (Homography) | $2 \times 3$ (Affine) | [Ref: OpenCV_2_textbook.md] |
| **Transformation Type** | Projective Mapping | Linear Affine Mapping | [Ref: OpenCV_2_textbook.md] |

## 3. Implementation Standard

### 3.1 OpenCV Rotation & Scaling Protocol
회전과 스케일링을 단일 연산으로 처리하기 위해 `getRotationMatrix2D`와 `warpAffine`을 순차적으로 적용한다 [Ref: raw/Open_CV_2_textbook.md].

```python
# 1. Transformation Matrix Generation
# M = cv2.getRotationMatrix2D(center, angle, scale)
M = cv2.getRotationMatrix2D(center, angle, scale)

# 2. Affine Mapping Application
# dst = cv2.warpAffine(src, M, (width, height))
dst = cv2.warpAffine(src, M, (width, height))
```

## 4. Dependency Graph
- **Parent Node**: `Open_CV_2`
- **Sibling Node**: `[[[Battery] image-warping-perspective]]` (Non-parallelism transformation)
- **Successor Node**: `[[[AI] edge-detection-sobel]]` (Feature extraction post-transformation)