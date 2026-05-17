---
metadata:
  id: "[[[Robotics] Indy7-Cobot-Operation-and-Programming]]"
  domain: "08_Robotics_Automation"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Robotics] Indy7-Cobot-Operation-and-Programming에 관한 고밀도 지능 노드"
semantic:
  tags: ["#08_Robotics_Automation", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Robotics] Indy7-Cobot-Operation-and-Programming

## 1. [왜 배우는가? (Why)]
협동 로봇(Cobot)은 이제 대기업 공장을 넘어 치킨 가게, 커피 매장, 그리고 중소기업 생산 라인까지 파고들고 있습니다. 그 중심에 한국의 대표적 협동 로봇인 Indy7이 있습니다. Indy7은 전문 프로그래머가 아니더라도 누구나 쉽게 로봇을 가르치고(Teaching) 사용할 수 있도록 설계되었습니다. Indy7의 조작법과 프로그래밍을 배우는 것은 가장 앞선 협동 로봇 기술을 실제 현장에 즉시 적용하고, 인간과 로봇이 조화롭게 일하는 스마트 작업장을 구축하는 실전 역량을 갖추는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | Specification | Engineering Rationale |
|:---|:---:|:---|
| **Payload** | 7 kg | 다양한 그리퍼와 작업물을 다루기에 최적화된 하중 지지력 |
| **Reach** | 800 mm | 작업자와 같은 공간에서 작업하기에 적합한 작업 반경 |
| **Repeatability** | ±0.03 mm | 반복적인 조립이나 피킹 작업에 필요한 정밀한 위치 재현성 |
| **Degrees of Freedom**| 6 DOF | 6축 관절을 통해 인간 팔과 유사한 자유로운 움직임 가능 |
| **Teaching Method** | Direct Teaching | 사람이 직접 로봇 팔을 잡고 움직여 궤적을 저장하는 직관적인 학습 방식 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 충돌 감지 및 안전 알고리즘 (Collision Detection)
- **논리**: 사람과 함께 일하려면 충돌을 감지하는 순간 즉시 멈춰야 합니다. 
- **결과**: Indy7은 토크 센서 없이도 모터의 전류값을 분석하여 미세한 저항(충돌)을 감지하고, ISO 10218-1 기준에 따라 안전하게 정지하여 작업자의 안전을 보장합니다.

### 3.2 IndySDK와 유연한 확장성
- **논리**: 로봇을 단순히 움직이는 것을 넘어 AI나 특수 센서와 연동해야 할 때가 많습니다. 
- **효과**: Indy7은 IndySDK를 통해 Python, C++ 등으로 로봇을 직접 제어할 수 있는 개방형 플랫폼을 제공합니다. 이를 통해 비전 센서를 이용한 물체 인식, AI 기반의 경로 최적화 등 고도화된 기능을 손쉽게 통합할 수 있습니다.

## 4. [코드 연결 해설 (Indy7 API & Motion Control Logic)]
Python을 이용해 Indy7의 위치를 제어하고 동작을 명령하는 기본적인 코드 구조입니다.
```python
# Indy7 로봇 지능 기반 모션 제어 논리
from indy_utils import indy_program_maker as ipm

def control_indy7_motion():
    # 1. 로봇 연결 및 초기화
    indy = ipm.Indy7Client(robot_ip="192.168.1.7")
    
    # 2. 홈 위치로 이동
    indy.move_to_home()
    
    # 3. 작업 위치 설정 (Joint 또는 Task 좌표)
    target_pos = [0, 0, 90, 0, 90, 0] # 관절 각도 예시
    
    # 4. 부드러운 모션(Blending) 적용하여 이동
    indy.move_j(target_pos, velocity=5, acceleration=10)
    
    # 5. 그리퍼 제어 (물체 잡기)
    indy.set_tool_command(command="GRIP_CLOSE")
    
    return "MOTION_EXECUTED"
```

## 5. [스스로 체크 (Self-Audit)]
1. Indy7의 '직접 교시(Direct Teaching)' 기능이 현장의 '유연한 생산(Flexible Production)'에 기여하는 바는?
2. Indy7이 토크 센서 없이도 '충돌 감지'가 가능한 물리적 원리는 무엇인가?
3. '콘티(Conty)' 앱을 활용한 로봇 프로그래밍이 기존의 '티칭 펜던트' 방식보다 우수한 점은?
**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
