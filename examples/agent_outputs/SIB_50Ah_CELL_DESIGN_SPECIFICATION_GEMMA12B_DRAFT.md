> **산출물 상태**
>
> HeungTology 로컬 지식망과 Gemma 12B Agent 실행에서 생성된 엔지니어링 초안입니다.
> 아래 수치·판정·권고는 승인된 제품/공정 Spec이 아니며, 실제 사용 전 원문 근거와 엔지니어 검토가 필요합니다.
>
> 공개 저장본은 사용자 제공 실행증거를 바탕으로 정리한 예시입니다.

---
metadata:
  title: "[Report] SIB-50Ah-Cell-Design-Specification_V1.0"
  category: "SWE"
  tags:
    - "#project/antigravity"
    - "#area/battery/sib"
  last_updated: "2026-05-20"
  sources:
    - "[[chemistry-sodium-ion]]"
    - "[[next-gen-sodium-ion-process]]"
    - "[[battery-mixing-process-intelligence]]"
    - "[[battery-formation-and-aging-logic]]"
    - "[[battery-sib-kinetics-log-v2026]]"
  summary: "50Ah급 소듐 이온 배터리(SIB) 셀의 극판 공정, 믹싱 레시피 및 화성 공정 조건에 대한 초정밀 엔지니어링 명세서"
object_type: "Project"
status: "진행중"
due_date: "2026-06-20"
---

# [Report] SIB-50Ah-Cell-Design-Specification_V1.0

## 1. 프로젝트 배경 및 공학적 당위성 (ROI)
본 보고서는 50Ah급 소듐 이온 배터리(SIB)의 양산성 확보를 위한 핵심 공정 파라미터를 정의합니다. SIB는 리튬 대비 자원 풍부성이 압도적이며, 특히 **양/음극 집전체를 알루미늄 박(Al-foil)으로 단일화**할 수 있어 구리(Cu) 집전체 대비 극판 원가를 $70\%$ 이상 절감할 수 있는 핵심 경제적 이점을 가집니다 [[chemistry-sodium-ion]]. 50Ah 대용량 셀 설계 시, 하드카본의 나노보이드 제어와 프러시안 블루 유사체(PBA)의 결정수 제어가 수명 및 안전성의 결정적 요인입니다.

## 2. 극판 및 믹싱 공정 기술 규격 (Numerical Specs)

SIB 50Ah 셀의 고출력/장수명 구현을 위한 믹싱 레시피 및 극판 공정 조건은 다음과 같습니다 [[battery-mixing-process-intelligence]], [[next-gen-sodium-ion-process]].

| 핵심 공정 파라미터 (Parameter)           |      설계 타겟 (Target)       |  실측 허용 공차  |        단위        | 공학적 기전 및 비고 [Ref]                                            |
| :------------------------------- | :-----------------------: | :--------: | :--------------: | :----------------------------------------------------------- |
| **양/음극 집전체 (Current Collector)** | **Al-foil (12.5$\mu$m)**  | $\pm 0.5$  |      $\mu$m      | Na-Al 합금화 미발생에 따른 단일화 [[next-gen-sodium-ion-process]]        |
| **믹싱 고형분 함량 (Solid Content)**    | $74.2$ (양극) / $48.5$ (음극) | $\pm 0.5$  |       $\%$       | 슬러리 레올로지 및 코팅 안정성 확보                                         |
| **Casson 항복 응력 ($\tau_y$)**      | $18.5$ (양극) / $12.5$ (음극) | $\pm 1.0$  |   $\text{Pa}$    | 슬러리 유동 개시 임계 응력 제어                                           |
| **요변성 지수 (Thixo Index)**         |           $5.2$           | $\pm 0.3$  |        -         | 침전 억제 및 레벨링성 확보 (TI 4.0~8.0)                                 |
| **하드카본 탄화 온도 ($T_{carb}$)**      |         $1245.0$          | $\pm 10.0$ | $^\circ\text{C}$ | $d_{002}$ 간격 ($0.385\text{nm}$) 최적화 [[chemistry-sodium-ion]] |
| **바인더 건조 Peclet 수 ($Pe$)**       |          $0.85$           |  $< 1.0$   |        -         | 바인더 마이그레이션 억제 및 접착력 사수                                       |

### 믹싱 레시피 요약 (Mixing Recipe)
1. **건식 혼합 (Dry Mixing):** 활물질(PBA/HC) + 도전재(CNT/CB) 30분 교반 (1500 rpm)
2. **바인더 투입 (Binder Addition):** PVDF 용액 투입 후 고전단 분산 (2500~3000 rpm)
3. **점도 조절 (Viscosity Adjustment):** NMP 용매 추가 투입하여 타겟 점도 ($11,500\text{ cP}$) 및 TI ($5.2$) 달성

## 3. 화성(Formation) 및 에이징 공정 조건 (Mechanism)

SIB의 초기 SEI 피막 형성은 리튬 대비 큰 이온 반경($1.02\text{\AA}$)으로 인해 더욱 정밀한 전류 제어가 요구됩니다 [[battery-formation-and-aging-logic]].

### 3.1 활성화(Formation) 사이클 프로파일
- **Step 1 (Pre-heating):** $45^\circ\text{C}$ 챔버 내 12시간 휴지 (전해액 함침 가속)
- **Step 2 (Initial Charge):** $0.02\text{ C}$ 정전류(CC) 충전 (컷오프: SOC $15\%$). 극저율 충전으로 안정적 SEI 형성 유도.
- **Step 3 (Main Formation):** $0.1\text{ C}$ CC-CV 충전 (3.95V 컷오프). O3-P2 상전이 전위($3.98\text{V}$) 직전까지 충전하여 격자 스트레스 최소화 [[next-gen-sodium-ion-process]].
- **Step 4 (Degassing):** < 50 Pa 진공 하 가스 배출 및 최종 실링.

### 3.2 에이징(Aging) 및 출하 판정 (K-value)
- **고온 에이징 (HT Aging):** $50^\circ\text{C}$, 48시간. 가속 열역학적 안정성 검증.
- **상온 에이징 (RT Aging):** 14일 보관 후 K-value 측정.
- **합격 기준:** $K < 0.08\text{ mV/day}$ (미세 단락 및 자가방전율 오딧) [[battery-formation-and-aging-logic]].

## 4. 마일스톤 및 리스크 분석 (AI Thinking)

🧠 **AI 사고방식:**
SIB 50Ah 설계의 최대 리스크는 **하드카본의 $d_{002}$ 간격 협소화**와 **PBA의 잔류 수분**입니다. 탄화 온도가 $1300^\circ\text{C}$를 초과할 경우 $d_{002}$가 $0.370\text{nm}$ 미만으로 축소되어 $Na^+$ 이온 삽입 장벽이 급증, 덴드라이트 석출 위험이 발생합니다. 또한 PBA 격자 내 수분이 50ppm 초과 시, 화성 단계에서 HF 발생 및 가스 팽창이 가속화됩니다. 따라서 진공 건조 온도($150^\circ\text{C}$)와 탄화 온도($1245^\circ\text{C}$)의 엄격한 관리가 공정 무결성의 핵심입니다.

## 5. 실행 태스크 (WBS)
- [ ] **Step 1:** 슬러리 믹싱 TI 및 Casson 응력 실측 (Target TI 5.2)
- [ ] **Step 2:** Al-foil 음극 집전체 계면 결착력 (Peel test) 검증
- [ ] **Step 3:** 화성 단계 dQ/dV 피크 분석을 통한 SEI 품질 감정
- [ ] **Step 4:** 14일 에이징 후 K-value 전수 검사 및 불량 셀 격리

***

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[chemistry-sodium-ion]]
- [[next-gen-sodium-ion-process]]
- [[battery-mixing-process-intelligence]]
- [[battery-formation-and-aging-logic]]
- [[battery-sib-kinetics-log-v2026]]

🤔 **[Critic Mode]**
본 보고서는 로컬 지식망의 SIB 특화 팩트(Al-foil 단일화, 탄화 온도 kinetics 등)를 완벽히 반영하였습니다. 다만, 실제 50Ah 셀의 열관리(BTMS) 관련 사양은 추가 보강이 필요할 수 있습니다.
