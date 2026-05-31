---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: debc0baa3b035a13c42512f7002362364bb2d00101394df24f3768224d1102aa
metadata:
  date: '2026-05-16'
  domain: 08_Robotics_Automation
  id: '[[[Robotics] LiDAR]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: '[Robotics] LiDAR에 관한 고밀도 지능 노드'
  object_type: Hardware
  tier: 1
properties:
  clustering_min_distance_m: 0.5
  fmcw_commercialization_target_year: 2026
  max_detection_range_m: 250
  voxel_grid_size_m: 0.1
  wavelength_high_nm: 1550
  wavelength_low_nm: 905
semantic:
  alternative_parents: []
  is_instance_of: '[[[MOC] 08_Robotics_Automation]]'
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

# [Robotics] LiDAR

## 1. [왜 배우는가? (Why)]
카메라는 2차원 영상으로 거리를 추정하지만, LiDAR는 레이저를 통해 사물과의 실제 거리를 센티미터(cm) 단위 오차로 직접 측정합니다. 이는 자율주행차가 밤이나 그림자 속에서도 사물의 정확한 크기와 위치를 파악하게 하여 '충돌 제로'를 달성하기 위한 필수 센서입니다. 특히 2026년에는 고가의 기계식 회전 구조를 벗어나 칩 형태의 고정형(Solid-state) 및 4D 정보(속도)를 주는 FMCW 기술이 상용화되며 자율주행의 신뢰성을 극대화하고 있습니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | Logic / Technology | Engineering Rationale |
|:---|:---:|:---|
| **Measurement** | ToF (Time of Flight) / FMCW | 거리 측정 방식 (반사 시간 vs 주파수 변조) |
| **Wavelength** | 905nm / 1550nm | 인체 안전성 및 장거리 탐지 성능 결정 |
| **Scanning** | Solid-state (OPA/Flash) | 기계적 가동부 제거로 내구성/양산성 확보 |
| **Resolution** | Point Cloud Density | 초당 수백만 개의 점으로 정밀 형상 재구성 |
| **Detection** | Max Range (> 250m) | 고속 주행 시 전방 조기 제동 거리 확보 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 ToF vs FMCW LiDAR의 수치적 논리
- **ToF (Time of Flight)**: 짧은 펄스를 쏘고 돌아오는 시간($\Delta t$)으로 거리를 구합니다. 구조가 단순하지만 햇빛이나 다른 차의 레이저 간섭에 취약합니다. 수식: $ d = \frac{c \cdot \Delta t}{2} $
- **FMCW (Frequency Modulated Continuous Wave)**: 연속된 파형의 주파수를 변조하여 발사하고, 돌아온 파형과의 주파수 차이(Beat Frequency)를 분석합니다. 거리뿐만 아니라 도플러 효과를 통해 물체의 **순간 속도(Radial Velocity)**까지 동시에 측정하는 '4D 인지'가 가능하며, 외부 간섭에 매우 강력합니다.

### 3.2 1550nm 파장의 우위
- **논리**: 905nm는 저렴하지만 망막 손상 위험으로 출력을 높이기 어렵습니다. 반면 1550nm는 각막에서 흡수되어 인체에 안전하므로 훨씬 높은 출력을 낼 수 있으며, 이를 통해 300m 이상의 초장거리 탐지가 가능합니다.

### 3.3 고정형 (Solid-state) 아키텍처
- **논리**: 거울을 회전시키는 기계식 구조는 진동과 온도 변화에 취약합니다. OPA(Optical Phased Array)나 MEMS 기술을 이용해 빛의 방향을 전기적으로 조절하면 수명과 신뢰성이 비약적으로 향상됩니다.

## 4. [코드 연결 해설 (Point Cloud Processing)]
LiDAR로부터 들어오는 수백만 개의 점 데이터(Point Cloud)를 클러스터링하여 객체를 인식하는 논리입니다.
```python
# LiDAR 포인트 클라우드 데이터 처리 및 객체 분리
def process_lidar_data(point_cloud_raw):
    # 1. 노이즈 제거 및 지면 여과 (Ground Filtering)
    # RANSAC 알고리즘을 사용하여 도로 바닥면 평면을 찾아 제거
    cloud_filtered = filter_noise(point_cloud_raw)
    
    # 2. 공간 분할 (Voxelization)
    # 연산 속도를 높이기 위해 3D 공간을 격자(Voxel) 단위로 단순화
    voxel_grid = create_voxel_grid(cloud_filtered, size=0.1)
    
    # 3. 객체 군집화 (Clustering)
    # 거리 기반(Euclidean Clustering)으로 점들을 묶어 개별 객체로 인식
    object_clusters = cluster_points(voxel_grid, min_dist=0.5)
    
    for cluster in object_clusters:
        # 4. 바운딩 박스(Bounding Box) 생성 및 속도 추출 (FMCW 사용 시)
        bbox = calculate_min_bounding_box(cluster)
        velocity = cluster.get_average_doppler_velocity()
        
        # 5. 자율주행 판단 엔진에 객체 정보 전달
        send_to_planner(id=cluster.id, shape=bbox, velocity=velocity)
        
    return "PERCEPTION_SYNCED"
```

## 5. [스스로 체크 (Self-Audit)]
1. FMCW LiDAR가 기존 ToF 방식 대비 '도플러 효과'를 통해 얻는 공학적 이점은?
2. 1550nm 파장을 사용하는 LiDAR가 905nm 대비 기후(안개, 비) 대응력이 높은 이유는?
3. '고정형(Solid-state)' LiDAR 도입이 자율주행 차량의 양산 단가 절감에 기여하는 방식은?

**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**