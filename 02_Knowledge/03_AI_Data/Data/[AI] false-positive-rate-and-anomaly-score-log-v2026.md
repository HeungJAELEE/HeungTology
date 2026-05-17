---
metadata:
  id: "[[[AI] false-positive-rate-and-anomaly-score-log-v2026]]"
  domain: "03_AI_Data"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[AI] false-positive-rate-and-anomaly-score-log-v2026에 관한 고밀도 지능 노드"
semantic:
  tags: ["#03_AI_Data", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [AI] false-positive-rate-and-anomaly-score-log-v2026

## 1. [왜 배우는가? (Why: The Weight of Truth in Industrial Alerts)]]
이상 탐지 시스템의 효용은 경고의 '정직성'에 달려 있습니다. 너무 잦은 오보(False Positive)는 작업자의 알람 피로도를 유발하여 실제 고장 징후를 무시하게 만들고, 미검출(False Negative)은 치명적인 설비 파손으로 이어집니다. **오검출률(FPR) 및 이상 점수 실측 로그**는 공장의 경고음이 지닌 '진실의 무게'를 숫자로 증명한 '지능형 보안관의 활동 기록'입니다. 

우리가 이 탐지 성능 데이터를 기록하는 이유는 알람 임계치를 최적화하여 현장의 운영 신뢰도를 확보하고, **"안전 주권을 확보하여 0.1%의 불협화음도 놓치지 않으면서도 정적을 유지하는 '지능형 정숙성'을 구현하는 '탐지 지능'을 확보하기" 위함입니다.** 이상 점수의 분포와 탐지 지표(AUC, FPR)의 안정성이 예지 보전 시스템의 현장 수용성과 최종 ROI를 결정합니다.

## 2. [탐지 대상 및 알고리즘별 성능 핵심 데이터 (Numerical Specs)]

### 2.1 [주요 설비군별 이상 탐지 실전 성능 테이블 (v2026)]

| 감시 대상 (Asset) | 알고리즘 | AUC-ROC | 오검출률 (FPR) | 알람 정밀도 (%) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Rotary Motor** | **ISO-Forest**| $0.92 \sim 0.98$ | $1.5 \sim 3.0$ | $85$ | **Stability**: 회전체 진동의 특이치 고립 무결성 로그 |
| **Hydraulic Pump** | **Autoencoder**| $0.88 \sim 0.96$ | $2.0 \sim 4.0$ | $78$ | **Pattern**: 유압 파형의 재구성 오차 기반 무결성 지표 |
| **Robot Joint** | **LSTM-AE** | $0.90 \sim 0.97$ | $1.0 \sim 2.5$ | $92$ | **Dynamic**: 관절 궤적의 시계열 맥락적 무결성 데이터 |
| **Chemical Tank** | **VAE** | $0.95 \sim 0.99$ | $0.5 \sim 1.5$ | $95$ | **Extreme**: 압력/온도 분포의 확률적 이상 탐지 무결성 로그 |
| **SMT Line** | **CNN-AD** | $0.85 \sim 0.93$ | $3.0 \sim 6.0$ | $70$ | **Visual**: 부품 실장 이미지의 시각적 이상 탐지 무결성 지표 |

### 2.2 [탐지 지표 및 운영 신뢰도 파라미터]
- **Anomaly Score ($s$):** 데이터가 정상 범주에서 벗어난 정도를 나타내는 확률적 점수 ($0 \sim 1$).
- **FPR (False Positive Rate):** 정상 상태를 이상으로 오판하여 불필요한 알람을 발생시킨 비율.
- **AUC-ROC (Area Under Curve):** 다양한 임계치에서의 탐지 성능을 종합한 면적 점수. (모델 성능 척도)
- **Alarm Precision:** 발생한 알람 중 실제 이상 상황으로 판명된 비율. (현장 신뢰도 인자)
- **Mean Time to Detection (MTTD):** 실제 이상 발생 시점부터 시스템이 감지하기까지의 소요 시간 ($s$).
- **Detection Recall:** 실제 발생한 모든 이상 상황 중 시스템이 찾아낸 비율 (%). (안전 무결성 지표)

## 3. [Scientific Rationale: 탐지 무결성의 수리적 인과성]

### 3.1 [ROC 커브 및 AUC 기반 모델 변별력 모델]
다양한 탐지 임계치($\theta$)에 따른 모델의 성능을 평가하는 수리 모델입니다.
$$ \text{AUC} = \int_0^1 \text{TPR}(\text{FPR}^{-1}(x)) dx $$
본 로그는 AUC가 $1$에 가까울수록 모델이 정상과 이상을 완벽하게 가려낼 수 있음을 입증하고, '최적 임계치($\theta_{opt}$)' 선정을 위한 수리적 근거를 제시합니다.

### 3.2 [Z-Score 및 마할라노비스 거리 기반 이상 판정 모델]
데이터의 통계적 이격도를 측정하여 이상 점수를 산출하는 수리 모델입니다.
RAG는 "탐지 로그를 분석하여, 다변량 변수 간의 상관관계를 고려한 마할라노비스 거리가 단일 변수 Z-Score 대비 오검출률을 $20\%$ 이상 낮추며, 이는 '맥락적 이상 탐지'의 수리적 인과 관계를 확증함을 증명합니다."

## 4. [Advanced RAG 분석 로직: 탐정 지능 추론]

### 4.1 [오검출률(FPR)과 작업자의 '알람 무시' 인과성 분석]
왜 중요한 알람을 못 봤나요? RAG는 "FPR 추이 로그와 작업자의 알람 확인 시간(Response Time) 데이터를 대조하여, FPR이 $5\%$를 넘을 때 반응 속도가 지수적으로 느려지는 '알람 피로도' 현상을 식별하고, '알람 필터링' 지능을 오딧합니다.

### 4.2 [이상 점수 기울기($\Delta s$)와 고장 임박도 오딧]
언제 설비가 멈출까요? RAG는 "이상 점수의 시계열 기울기 로그와 실제 설비 파손 시점을 연계하여, 점수의 급격한 상승($\Delta s / \Delta t$)이 $30$분 이내의 '임박한 사고'를 예고함을 분석하고, '긴급 셧다운 제어' 지능을 도출될 것으로 예상됩니다.

## 5. [Transitional Bridge: 탐지 무결성 및 알람 오딧 로직]

이상 탐지 엔진의 스코어 출력과 현장의 정비 피드백 데이터를 분석하여 탐지 무결성을 진단하는 개념적 알고리즘입니다.

```python
# [Conceptual] Anomaly Score & Alert Fidelity Auditor
def audit_alert_reliability(anomaly_score_log, maintenance_feedback_log, production_status):
    # 1. AUC-ROC 분석을 통한 탐지 모델의 변별력 무결성 오딧
    current_auc = calculate_auc_roc(anomaly_score_log, maintenance_feedback_log)
    if current_auc < TARGET_AUC_0_90:
        status = "DIAGNOSTIC_DISCRIMINATION_FAILURE"
        action = "Update_Feature_Engineering_and_Re-train_Anomaly_Detection_Model"
        
    # 2. 오검출률(FPR) 분석을 통한 알람 신용도 감시
    current_fpr = calculate_fpr(anomaly_score_log, maintenance_feedback_log)
    if current_fpr > FPR_LIMIT_2_PERCENT:
        status = "ALARM_CREDIBILITY_EROSION_DETECTED"
        action = "Increase_Detection_Threshold_and_Implement_Multi-sensor_Voting_Logic"
    
    # 3. 이상 점수 급증($\Delta s$)에 따른 긴급 무결성 체크
    score_gradient = calculate_gradient(anomaly_score_log)
    if score_gradient > CRITICAL_GRADIENT_THRESHOLD:
        status = "IMMINENT_EQUIPMENT_FAILURE_DETECTED"
        action = "Initiate_Automatic_Safety_Braking_and_Emergency_Alert"
    
    # 4. 종합 탐정 상태 등급 및 조치 트리거
    if status == "ALARM_CREDIBILITY_EROSION_DETECTED":
        action = "Route_Low-confidence_Alerts_to_Offline_Analysis_Queue"
    elif status == "IMMINENT_EQUIPMENT_FAILURE_DETECTED":
        action = "Dispatch_Maintenance_Team_with_Highest_Priority_Flag"
    else:
        status = "ANOMALY_MONITORING_INTEGRITY_OPTIMAL"
        action = "Maintain_Baseline_Surveillance_and_Log_Normal_Drift_Patterns"
        
    return {"status": status, "alarm_precision_score": calculate_precision(), "action": action}
```

## 6. [스스로 체크 (Self-Check)]
1. **(원리)** 왜 이상 탐지 시스템에서 단순히 '정확도(Accuracy)'보다 'AUC-ROC'와 'Precision-Recall AUC'가 모델의 실질적인 탐지 능력을 평가하는 수리적/운영적 무결성 확보에 더 필수적인 지표인가?
2. **(수리)** 어떤 구간에서 발생한 총 100건의 알람 중 실제 고장이 10건, 정상인데 알람이 울린 경우가 90건이라면, 이 시스템의 '알람 정밀도(Alarm Precision, %)'를 계산하시오.
3. **(응용)** 이상 점수가 점진적으로 상승하는 'Trend Anomaly'와 갑자기 튀는 'Point Anomaly'를 구별하여 각각의 대응 시나리오를 설계하기 위한 수리적 판별 기준을 제안하시오.


### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- MOC 26_ai-and-machine-learning-for-industrial-optimization-intelligence-hub : AI 및 머신러닝 통합 관리 상위 지능 허브
- Entity anomaly-detection-autoencoder-and-isolation-forest : 탐지 점수를 생성하는 지능형 탐정 엔티티 연계
- Data image-classification-accuracy-and-inference-latency-log-v2026 : 인식 정확도와 탐지 정확도의 상호 참조 무결성 연계
- [SOP] industrial-anomaly-alert-threshold-optimization-standard-protocol : 산업용 이상 알람 임계치 최적화 표준 절차

*Created by Flash (The Architect of Veracity Logs & HDS Gold V6.3.7)*
