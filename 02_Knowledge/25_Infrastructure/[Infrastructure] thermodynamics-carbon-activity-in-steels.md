---
metadata:
  id: "[[[Infrastructure] thermodynamics-carbon-activity-in-steels]]"
  domain: "25_Infrastructure"
  project: "Vault_Modernization"
  date: "2026-05-16"
  version: "v7.6.2_Modernized"
object:
  object_type: "Concept"
  tier: 1
  description: "[Infrastructure] thermodynamics-carbon-activity-in-steels에 관한 고밀도 지능 노드"
semantic:
  tags: ["#25_Infrastructure", "#지능망", "#HDS-Gold"]
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
trust_metrics:
  T_static: 1.0
  T_dynamic: 1.0
  isolation_index: 0.1
---

# [Infrastructure] thermodynamics-carbon-activity-in-steels

## 1. [왜 배우는가? (Why): 화학적 포텐셜과 확산의 지배]
탄소 활동도($a_C$)를 이해하는 것은 강철의 표면 강화 공정(침탄, 질화)에서 탄소가 얼마나 효율적으로 기지 조직으로 침투할지를 결정짓는 핵심 지표입니다. 단순히 탄소 농도가 높다고 확산이 잘 되는 것이 아니라, 합금 원소와의 상호작용에 따른 '화학적 포텐셜'의 차이가 실제 금속의 기계적 성질을 좌우합니다. 2nm 노드 반도체의 불순물 제어와 마찬가지로, 철강에서도 원자 단위의 활동도 제어가 부품의 내마모성과 피로 강도를 결정합니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| 항목 | 수식 / 단위 | 공학적 수치 (Fe-C) | 특징 및 의미 |
| :--- | :---: | :---: | :--- |
| **Activity ($a_C$)** | $a_C = \gamma_C \cdot X_C$ | - | 열역학적 유효 농도 (확산의 구동력) |
| **Max Solubility** | $wt\%$ | 2.14 ($1147^\circ C$) | 오스테나이트 영역 탄소 최대 고용량 |
| **Diff. Coeff. ($D$)** | $m^2/s$ | $10^{-11} \sim 10^{-12}$ | $900^\circ C$ 기준 탄소의 확산 속도 |
| **Activation Energy** | $kJ/mol$ | $\approx 100$ | 탄소 확산을 위한 최소 에너지 장벽 |
| **Wagner Coeff. ($\epsilon_C^{Si}$)**| - | $+10 \sim +15$ | Si가 탄소 활동도를 높이는 정도 (Positive) |
| **Wagner Coeff. ($\epsilon_C^{Cr}$)**| - | $-5 \sim -10$ | Cr이 탄소 활동도를 낮추는 정도 (Negative) |

## 3. [심층 이론 (Deep Analysis): 열역학적 인과관계]

### 3.1 와그너 상호작용 계수 (Wagner Interaction Parameter)
합금 원소가 탄소 활동도에 미치는 영향은 런-투-런 제어의 핵심입니다.
- **$\epsilon_C^j > 0$ (Si, Ni)**: 탄소와 반발하여 활동도를 높입니다. 이는 동일 농도에서도 탄소가 더 빨리 확산되거나 흑연으로 석출되게 만듭니다.
- **$\epsilon_C^j < 0$ (Cr, Mo, V)**: 탄소와 친화력이 강해 활동도를 낮춥니다. 이는 오스테나이트를 안정화하고 정교한 탄화물 분산을 가능케 합니다.

### 3.2 픽의 법칙 (Fick's Law) 및 확산 물리
- **1st Law ($J = -D \nabla c$)**: 농도 구배가 아닌 '화학적 포텐셜 구배'가 실제 확산의 근본 원인입니다.
- **2nd Law ($\frac{\partial c}{\partial t} = D \nabla^2 c$)**: 시간에 따른 침탄 깊이를 예측하는 수식입니다. 확산 깊이($x$)는 시간($t$)의 제곱근에 비례합니다($x \approx \sqrt{Dt}$).

## 4. [AI & Hardware Synergy: Inverse Metallurgical Design]
- **Carbon Profile Predictor**: RTX 4060 기반 AI 모델이 노내 가스 분압과 합금 원소 데이터를 결합하여 실시간 침탄 프로파일을 예측합니다. $0.01\%$ 단위의 탄소 농도 제어를 통해 최적 경화 깊이를 확보합니다.
- **Thermocalc Integration**: 대규모 열역학 DB와 팔란티어 온톨로지를 연동하여, 목표 물성에 최적화된 합금 조성(Si/Cr 비율)을 역설계(Inverse Design)합니다.

## 5. [스스로 체크 (Verification)]
1. 왜 탄소 활동도($a_C$)가 실제 농도($X_C$)보다 확산에 더 중요한 지표인가?
2. **Si** 함량이 높은 강재에서 침탄 공정을 수행할 때 주의해야 할 점은? (활동도 관점)
3. **$\epsilon_C^{Cr} < 0$**의 의미가 탄화물($Fe_3C, Cr_{23}C_6$) 안정성에 미치는 영향은?
4. **Fick's 2nd Law**를 기반으로 침탄 시간을 2배 늘렸을 때, 침투 깊이의 변화량은?
5. 왜 탄소($C$)는 철($Fe$) 격자 내에서 치환형이 아닌 **침입형(Interstitial)**으로 확산되는가? (원자 크기 관점)

*Created by Flash (HDS-Gold V6.3.7 Reinforcement)*
