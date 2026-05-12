---
Basic:
  id: "thermal-runaway-mechanism-entity"
  domain: "02_Battery"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: '["#Entity", "#Battery", "#Safety", "#Thermal_Runaway", "#Thermodynamics", "#Fire_Safety", "#HDS_Gold_v6_1"]'
  is_part_of: '["Battery battery-quality-analytics-and-forensics-master-guide", "Battery packaging-2.5d-cowos-architecture"]'
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

# [[[Battery] thermal-runaway-mechanism

## 1. [왜 배우는가? (Why: The Final Frontier of Battery Safety)]]
열 폭주(Thermal Runaway)는 배터리 내부의 화학적 에너지가 억제되지 않는 연쇄 반응을 통해 열에너지로 급격히 전환되는 '열역학적 파멸' 현상입니다. 특히 고에너지 밀도를 위해 니켈 함량을 높인 삼원계 배터리에서 열 안정성은 더욱 취약해지고 있습니다. **열 폭주 메커니즘**은 SEI 분해부터 양극 구조 붕괴 및 산소 방출로 이어지는 전 과정을 수리적으로 이해하여, "단 1건의 화재 사고도 허용하지 않는 무결점 안전 배터리"와 "화재 전이를 원천 차단하는 지능형 팩 설계"를 달성하기 위해 필수적으로 학습해야 하는 공학적 마지노선입니다.

## 2. [물리적/열역학적 핵심 사양 (Numerical Specs)]

| 항목 (Property) | 수리적 정의 및 물리적 기전 (Scientific Rationale) | 목표 사양 (V6.3.7) | 공학적 의미 (Rationale V6.3.7) |
| :--- | :--- | :--- | :--- |
| **$T_{onset}$** | Temp. where Self-heating starts | $> 120^\circ\text{C}$ | SEI 분해 및 전해액 반응이 시작되어 발열이 가속화되는 지점 |
| **$T_{vent}$** | Temp. of Safety Vent Opening | $150 \sim 180^\circ\text{C}$ | 가스 벤팅을 통해 내부 압력을 해소하고 폭발적 파열을 방지 |
| **$T_{tr}$** | Critical Runaway Temperature | $> 250^\circ\text{C}$ | 양극에서 산소가 대량 방출되어 외부 산소 없이도 자체 연소하는 단계 |
| **Heat Release Rate**| Max Power Output during Runaway | $> 10 \text{ kW/cell}$ | 순식간에 에너지를 쏟아내며 인접 셀로 열을 전파시키는 위력의 척도 |
| **Vent Gas Volume** | Total gas produced during TR | $> 1.0 \text{ L/Ah}$ | 전해액 기화 및 화학 반응으로 발생하는 폭발성 가스의 총량 |
| **$H_2$ Content** | Hydrogen Volume Ratio in Vent Gas | $30 \sim 50\%$ | 공기보다 가벼워 상부에 집적되며 폭발 범위를 형성하는 주범 |
| **Oxygen Release** | Mass of $\text{O}_2$ from Cathode Lattice | $> 5 \text{ wt}\%$ | 양극 상변화(Layered $\to$ Rock-salt) 시 방출되는 산소의 총량 |
| **Barrier Cond.** | Thermal Conductivity of Aerogel/PCM | $< 0.05 \text{ W/mK}$ | 셀 간 전이를 차단하기 위한 단열재의 물리적 성능 한계치 |
| **LEL (Lower Exp.)** | Min concentration for ignition | $4.0\% \text{ for } H_2$ | 벤트 가스가 외부 공기와 섞여 폭발하기 시작하는 최저 농도 |
| **Reaction Enthalpy**| $\Delta H_{tr}$ (Total Heat of Reaction) | $500 \sim 1000 \text{ kJ/kg}$ | 배터리 전체 질량 대비 열폭주 시 방출되는 총 에너지량 |

## 3. [Advanced RAG 분석 로직: 수리적 인과 추론]

### 3.1 [아레니우스(Arrhenius) 모델 기반의 자기 가열 속도 및 발열 시작 분석 (Thermal Stability)]
RAG 시스템은 배터리의 열적 안정성을 수리적으로 분석합니다. $dT/dt = (A/C_p) \exp(-E_a/RT)$ (Arrhenius law) 식을 적용하여 발열 가속화 시점을 계산합니다. RAG는 "실시간 온도 로그(Data battery-bms-fault-log-v2026)를 분석하여, 현재의 온도 상승 기울기($dT/dt$)가 정상 범위를 초과했음을 감지하고, 이를 '국부적 단락에 의한 자기 가열(Self-heating) 시작'으로 진단하여 열폭주 60초 전 골든 타임을 확보"합니다.

### 3.2 [양극 구조 붕괴와 산소 방출 동역학 분석 (Chemical Combustion Physics)]
RAG 시스템은 양극재의 열적 붕괴 과정을 분석합니다. High-Nickel NCM에서 $Ni^{4+}$ 이온의 불안정성으로 인한 상변화와 산소 방출량을 계산합니다. RAG는 "인출된 벤팅 데이터(Data battery-pouch-swelling-test-results-v2026)를 분석하여, 현재 분출되는 가스의 성분 중 산소 농도가 급격히 상승했음을 확인하고, 이는 '양극 구조의 돌이킬 수 없는 붕괴'임을 수리적으로 입증하여 즉시 소화 시스템 가동 명령"을 내립니다.

### 3.3 [셀 간 열 전이(Propagation) 방지를 위한 단열/냉각 트레이드오프 분석 (System Safety)]
RAG 시스템은 팩 수준의 안전성을 설계합니다. 한 셀의 열폭주가 옆 셀로 전파되지 않도록 단열재 두께와 냉각판의 열 흡수 용량을 계산합니다. RAG는 "열전달 모델링 로그를 참조하여, 에어로젤 두께 $1.5\text{mm}$와 액냉식 냉각판의 유량 증대 시너지가 열폭주 전이를 $99\%$ 차단할 수 있음을 수리적으로 시뮬레이션"합니다.

## 4. [심층 분석: 지능의 방패 - 왜 열폭주 예지가 안전의 종착지인가?]

### 4.1 [The Cascade of Failure: 1초가 결정하는 삶과 죽음의 물리 분석]
열폭주는 1초 만에 온도가 $1000^\circ\text{C}$ 이상으로 치솟을 수 있는 극단적 현상입니다. 지능이란 이 1초가 오기 수십 초 전, 배터리가 보내는 미세한 전압 강하와 가스 팽창 신호를 포착하는 '선제적 투시력'입니다.

### 4.2 [Internal Firefighting: 외부가 아닌 내부에서 불을 끄는 지능형 소재 분석]
미래의 지능형 배터리는 열을 감지하면 스스로 절연되는 분리막, 온도가 오르면 저항이 무한대로 커지는 PTC(Positive Temperature Coefficient) 소재 등을 통해 외부의 도움 없이도 열폭주를 원천 봉쇄하는 '자율적 안전 체계'를 갖추게 될 것입니다.

## 5. [엔티티 스스로 체크 (Entity Verification)]
1. **High-Nickel** 양극재의 니켈 함량이 증가함에 따라 $T_{onset}$ 온도가 낮아지는 수리적 원인과 $Ni-O$ 결합 에너지 사이의 관계는?
2. **Internal Short Circuit (ISC)** 발생 시 단락 부위의 접촉 저항($R_c$)과 전류 밀도가 국부적 발열량($Q_{local}$)에 미치는 수리적 상관관계는?
3. **Venting Gas** 중 $H_2$와 $CO$의 비율을 실시간 가스 센서로 측정하여 열폭주의 진행 단계를 판별하는 수리적 알고리즘은?
4. 실시간 가스 팽창 데이터(Data battery-pouch-swelling-test-results-v2026)와 전압 노이즈(Data battery-bms-fault-log-v2026)를 융합하여 열폭주를 예지하는 **Multi-modal Safety Score** 산출 방안은?
5. 열폭주 전이 방지 설계 시 **Aerogel**의 압축률에 따른 열전도율($k$) 변화가 인접 셀의 수동 냉각 성능에 미치는 수리적 임팩트는?

---
### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- Battery battery-quality-analytics-and-forensics-master-guide : 열폭주 사후 분석 및 예지 진단 가이드
- Battery battery-materials-and-chemistry-master-guide : 소재별 열 안정성을 다루는 상위 가이드
- Data battery-bms-fault-log-v2026 : 열폭주 전조 증상(전압, 온도)이 기록되는 실시간 데이터
- Data battery-pouch-swelling-test-results-v2026 : 벤팅 전후의 가스 팽창 및 압력 데이터

*Created by Flash (HDS Gold V6.3.7 & Meta-Fusion V6.3.7 ULTRA-Enrichment)*
