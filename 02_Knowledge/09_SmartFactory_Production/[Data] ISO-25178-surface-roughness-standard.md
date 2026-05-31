---
metadata:
  ai_status: Approved
  domain: 09_SmartFactory_Production
  id: '[[[Data] ISO-25178-surface-roughness-standard]]'
  version: v7.9_Enterprise_Node
object:
  description: 'ISO 25178 - Geometric Product Specifications (GPS) - Surface texture:
    Areal'
  object_type: Concept
properties:
  application_domains:
  - semiconductor
  - battery_electrode
  - high_precision_machining
  measurement_methods:
  - afm
  - optical_interferometer
  sa: arithmetical mean height
  sku: kurtosis
  sq: root mean square height
  ssk: skewness
  standard_id: iso_25178
  sz: maximum height
semantic:
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub.md]]'
spo_graph: []
---

# [Data] ISO-25178 Surface Roughness Standard

## 1. Overview
이 데이터 노드는 ISO 25178 (Areal Surface Texture) 표준 규격의 핵심 파라미터를 정의합니다. 반도체, 배터리 극판, 및 초정밀 가공 표면의 3D 거칠기를 정량화하기 위한 공통 기준선(Baseline)으로 작용합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Unit | Description (ISO Definition) | Mathematical Rationale |
| :--- | :--- | :--- | :--- |
| $Sq$ | $nm$ | Root mean square height | 표면 높이 분포의 표준 편차 (2차 모멘트) |
| $Ssk$ | - | Skewness | 표면의 비대칭성 (피크와 밸리의 편향성) |
| $Sku$ | - | Kurtosis | 높이 분포의 뾰족한 정도 |
| $Sa$ | $nm$ | Arithmetical mean height | 절대 높이의 산술 평균 |
| $Sz$ | $nm$ | Maximum height | 최대 피크 높이($Sp$)와 최대 밸리 깊이($Sv$)의 합 |

## 3. Data Integration
이 데이터는 AFM(Atomic Force Microscopy) 및 광학 간섭계(Optical Interferometer)의 원시 데이터를 분석할 때, 측정 좌표의 증거(Evidence Coordinate)로 참조됩니다.