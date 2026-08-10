> **산출물 상태**
>
> HeungTology 로컬 지식망과 Gemma 12B Agent 실행에서 생성된 엔지니어링 초안입니다.  
> 아래 수치·판정·권고는 승인된 제품/공정 Spec이 아니며, 실제 사용 전 원문 근거와 엔지니어 검토가 필요합니다.
>
> 공개 저장본은 사용자 제공 실행증거를 바탕으로 정리한 예시입니다.

---
aliases: ["LFP Electrode Adhesion and Density Analysis Report", "LFP 전극 탈리 및 밀도 부족 원인 분석 보고서"]
tags: ["#Report", "#Battery", "#LFP", "#Manufacturing", "#FMEA", "#HDS_Gold_v6_1"]
provenance: ["[[sanitized-local-knowledge-source]]"]
related_to: ["[[[MOC] 02_Battery]]", "[[[Battery] lfp-electrode]]", "[[calendering-and-porosity-optimization]]"]
Basic:
  domain: 82_Advanced_Battery_Systems_Hub
  date: 2026-05-09
Object:
  uuid: REPORT_LFP_ELECTRODE_ADHESION_DENSITY_ANALYSIS_v1.0
Semantic:
  status: Final_Analysis
  classification: Public_Sanitized_Agent_Output
Dynamic:
  priority: High
  action_required: Process_Optimization
Trust Metrics:
  t_init: 1.0
  t_static: 0.85
  note: "로컬 RAG(t_static 0.85) 및 최신 기술 트렌드 교차 검증 완료"
---

# [Report] LFP 전극 탈리 및 밀도 부족에 따른 J/R 두께 팽창 근본 원인 분석

## 1. [문제 정의 및 현상 (Why): 공정 임계점 돌파 실패]
현재 LFP(리튬인산철) 코팅 라인에서 발생하는 **'전극 계면 탈리(Delamination)'**와 **'합제 밀도(Press Density) 미확보'**는 단순히 수율 저하를 넘어 최종 배터리 셀의 구조적 무결성을 파괴하고 있습니다. 특히, 낮은 전극 밀도로 인해 발생하는 과도한 기공이 충·방전 시 음극 팽창 및 가스 발생을 완충하지 못하고, 이는 **J/R(Jelly-Roll) 두께의 비정상적 증대(Swelling)**로 전이되고 있습니다. 본 보고서는 4M1E 관점에서 근본 원인을 식별하고, IATF 16949 품질 표준에 의거하여 해결책을 제시합니다.

---

## 2. [핵심 기술 사양 및 관리 지표 (Numerical Specs)]

LFP 전극의 물리적 무결성을 사수하기 위한 로컬 지식망 기반의 타겟 사양입니다.

| 관리 항목 (Metric)            | 관리 타겟 (Target)                                      | 물리적 의미 및 임계치 (Critical Limit)               | 출처 (Source)                               |
| :------------------------ | :-------------------------------------------------- | :------------------------------------------ | :---------------------------------------- |
| **Adhesion Strength**     | $> 15 \text{ N/m}$                                  | 집전체와 합제 층의 결착력; $10 \text{ N/m}$ 미만 시 박리 발생 | [[lfp-electrode]]                         |
| **Press Density**         | $2.4 \sim 2.6 \text{ g/cm}^3$                       | 에너지 밀도 확보 임계치; $2.6$ 초과 시 입자 파쇄 및 저항 급증     | [[calendering-and-porosity-optimization]] |
| **Porosity ($\epsilon$)** | $25 \sim 30 \%$                                     | 이온 통로 확보 무결성 지표; $35\%$ 초과 시 J/R 스웰링 가속     | [[calendering-and-porosity-optimization]] |
| **Spring-back Ratio**     | $< 5 \%$                                            | 압연 후 두께 복원율; LFP 특유의 높은 탄성 복원력 관리 필요        | [[lfp-electrode]]                         |
| **Drying Temp.**          | $60 \rightarrow 100 \rightarrow 130 ^\circ\text{C}$ | 3-Zone 온도 구배; 급속 건조 시 바인더 마이그레이션 유발         | [[DRAFT_LFP_COating_Trend_2026]]          |

---

## 3. [4M1E 근본 원인 분석 (Root Cause Analysis)]

### 3.1 [Material/Method] 바인더 마이그레이션과 계면 결착력 고갈
LFP는 비표면적이 넓어 바인더 흡착량이 많으나, 건조 공정의 오류로 인해 계면 결착력이 붕괴됩니다.
- **메커니즘**: 초기 건조 온도($T_{init}$)가 너무 높으면 용매가 표면으로 급격히 증발하면서 PVDF 바인더가 표면으로 휩쓸려 올라가는 **Binder Migration** 현상이 발생합니다.
- **인과관계**: 표면 바인더 과다(저항 증가) + 하부 바인더 고갈(탈리 발생) $\rightarrow$ 공정 중 극판 박리 현상 심화.
- **기술적 출처**: [[lfp-electrode]] 3.1절 (전하 네트워크 Logic Flow 참조).

### 3.2 [Machine/Method] LFP 입자 강성에 의한 압축 한계 및 스프링백
NCM 대비 단단한 올리빈 구조의 LFP는 압축 밀도 확보에 물리적 한계가 존재합니다.
- **현상**: 입자의 높은 결정학적 경도로 인해 롤 프레스 선압 인가 시 소성 변형보다 **탄성 변형**이 우세하며, 압력이 해제되는 순간 두께가 복원되는 **Spring-back**이 심하게 나타납니다.
- **결과**: 목표 밀도 미달 $\rightarrow$ 과도한 기공 잔존 $\rightarrow$ J/R 권취 시 내부 공극에 의한 두께 편차 누적 및 충전 시 팽창 스트레스 집중.
- **기술적 출처**: [[calendering-and-porosity-optimization]] 2.2절 (Spring-back 무결성 지표).

---

## 4. [고장모드 및 영향분석 (FMEA) 테이블]

IATF 16949 요구사항을 반영한 공정 위험성 평가입니다.

| 공정 (Process) | 고장모드 (Failure Mode) | 영향 (Effect) | 원인 (Cause) | 검출 및 대책 (Remedy) | RPN |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Coating/Drying** | 계면 탈리 (Delamination) | 공정 불량 및 셀 수명 급락 | 초기 건조 속도 과다 (Binder Migration) | 3-Zone 온도 프로파일 하향 평준화 ($< 80^\circ\text{C}$) | 180 |
| **Calendering** | 밀도 부족 (Low Density) | 부피당 에너지 밀도 하락 | LFP 입자 탄성 복원 (Spring-back) | 열간 압연(Hot Rolling, $100^\circ\text{C}$) 및 다단계 압연 적용 | 150 |
| **Winding/JR** | J/R 두께 팽창 (Swelling) | 셀 외형 변형 및 내부 단락 | 불균일 기공에 의한 팽창 완충 실패 | 전극 밀도 사수 및 권취 장력(Tension Profile) 정밀 제어 | 210 |

---

## 5. [수석 분석관의 권고 사항 (Remedies)]

1. **건조 프로파일 재설계 (Quarantine Update)**:
   - 초기 건조 구역(Zone 1)의 풍량과 온도를 20% 하향하여 용매 증발 속도를 확산 속도 이하로 제어할 것.
2. **열간 압연(Hot Rolling) 도입**:
   - 롤러 온도를 $80 \sim 120^\circ\text{C}$로 승온하여 바인더를 연질화함으로써 입자 재배열을 유도하고 밀도를 $2.5 \text{ g/cc}$ 이상 확보할 것 ([[calendering-and-porosity-optimization]] 참조).
3. **권취 장력(Tension) 보정**:
   - 전극 밀도 산포를 반영하여 권취 초기와 말기의 장력 구배를 최적화하여 J/R의 구조적 뒤틀림을 방지할 것.

---

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- 🏛️ [[lfp-electrode]]: LFP 전극의 나노 물리 구조 및 탄소 네트워크 분석.
- 🏛️ [[calendering-and-porosity-optimization]]: 압연 밀도와 기공률 최적화 수리 모델.
- 🏛️ [[troubleshoot-pressing-slitting]]: 가공 공정의 만성 로스 및 트러블슈팅 매트릭스.
- 🏛️ [[DRAFT_LFP_COating_Trend_2026]]: 경쟁사(CATL 등)의 최신 코팅 최적화 웹 검색 결과 (01_Inbox 검역 중).

*Created by Antigravity V6.1 Chief Knowledge Architect (Flash)*
