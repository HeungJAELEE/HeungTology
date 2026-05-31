---
metadata:
  ai_status: Approved
  domain: 03_AI_Data
  id: '[[[Data] AFM-metrology-and-calibration-manual-v2026]]'
  version: v7.9_Enterprise_Node
object:
  description: 2026 Standard Operational Procedure & Calibration Manual for AFM
  object_type: Data
properties:
  cantilever_spring_constant: 40 N/m
  resonant_frequency: 300 kHz
  scanner_xy_linearity: 0.1%
  tip_radius: 5 nm
  z_axis_noise_floor: 0.03 nm
semantic:
  is_instance_of: '[[[MOC] Global-Dataset-Inventory-Hub.md]]'
spo_graph: []
---

# [Data] AFM Metrology and Calibration Manual (v2026)

## 1. Overview
본 매뉴얼 데이터는 나노스케일 계측을 위한 원자간력 현미경(Atomic Force Microscopy, AFM)의 캘리브레이션 및 운영 기준을 담고 있습니다. 팁(Tip) 마모도 보상 로직과 캔틸레버 스프링 상수 보정 알고리즘의 기준 데이터셋 역할을 수행합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]
| Parameter | Nominal Value | Tolerance | Application |
| :--- | :--- | :--- | :--- |
| Cantilever Spring Constant ($k$) | $40 \ N/m$ | $\pm 10\%$ | Tapping Mode Calibration |
| Resonant Frequency ($f_0$) | $300 \ kHz$ | $\pm 5 \ kHz$ | AC Mode Tuning |
| Tip Radius ($R$) | $5 \ nm$ | $< 2 \ nm$ | High-Resolution Scanning |
| Scanner X-Y Linearity | $0.1\%$ | $\pm 0.05\%$ | Piezoelectric Creep Correction |
| Z-axis Noise Floor | $0.03 \ nm$ (RMS) | Max $0.05 \ nm$ | Angstrom-level Profiling |

## 3. Data Integration
이 매뉴얼은 나노 계측 장비의 신뢰성 검증(Reliability Audit) 및 AI 기반 팁 손상 예측(Predictive Maintenance) 모델의 학습 데이터(Ground Truth)로 참조됩니다.