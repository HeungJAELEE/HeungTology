---
lineage:
  dataset_reference: global-dataset-inventory-hub
  original_author: Antigravity Vault
  original_hash: 11158e6997a0fdfca3d08649e79ef38ced2fb9fa66e3d8eeadc606421abba4b2
metadata:
  date: '2026-05-17'
  domain: 02_Battery
  id: '[[[Battery] lithium-plating-physics-and-detection]]'
  last_updated: '2026-05-17T22:59:20+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: 리튬 플레이팅 가속 속도론(Butler-Volmer) 및 전압 이완(Relaxation) 2차 미분 진단 기하학과 염 석출(Salt
    Precipitation) 퇴화 메커니즘을 규정하는 고밀도 지능 노드
  object_type: Concept
  tier: 1
properties:
  c_crit: '> 0.5 C'
  e_onset: < 0 V vs. Li/Li+
  np_capacity_ratio: 1.08 ~ 1.15
  sigma_relax: < 5.0 mV/s^2
  v_strip: 0.08 ~ 0.18 V vs. OCV
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

# [Battery] lithium-plating-physics-and-detection

## 1. 개요: 음극 표면의 금속 리튬 증착 (Lithium Plating)
리튬 플레이팅(LP)은 리튬 이온($Li^+$)이 음극 활물질(Graphite 등) 내부로 삽입(Intercalation)되지 못하고, 음극 표면에서 금속 리튬($Li^0$)으로 환원되어 기생적으로 증착되는 전기화학적 퇴화 현상입니다. 이는 음극 국부 전위가 $Li/Li^+$ 기준 $0\text{ V}$ 이하로 떨어질 때 가속화됩니다. 증착된 리튬은 덴드라이트(Dendrite) 형태로 성장하여 분리막을 관통하여 내부 단락(Internal Short Circuit)을 유발하고 열폭주(Thermal Runaway)를 촉발하는 치명적인 안전 리스크의 근원이 됩니다.

## 2. 핵심 기술 사양 및 검출 임계치 표준 (Numerical Specs)

| 파라미터 | 공학적 정의 | 표준 임계치 및 목표치 |
| :--- | :--- | :---: |
| **LP 개시 열역학 전위 ($E_{\text{onset}}$)** | 금속 리튬 증착이 개시되는 열역학적 하한선 | $< 0\text{ V vs. Li/Li}^+$ |
| **스트리핑 평탄 전압 ($V_{\text{strip}}$)** | 증착 리튬이 재이온화(Stripping)될 때의 전압 고원 구간 | $0.08 \sim 0.18\text{ V vs. OCV}$ |
| **2차 미분 탐지 감도 ($\sigma_{\text{relax}}$)** | 전압 이완 분석($d^2V/dt^2$)을 통한 LP 진단 한계 | $< 5.0\text{ mV/s}^2$ |
| **N/P 용량비 (Capacity Ratio)** | 양극 극판 용량 대비 음극 극판 용량 설계 비율 | $1.08 \sim 1.15$ |
| **임계 충전 C-rate ($C_{\text{crit}}$)** | 온도($0^\circ\text{C}$) 기준 LP가 발생하기 시작하는 충전 속도 | $> 0.5\text{ C}$ |

## 3. 물리적 속도론 모델: Butler-Volmer 에너제틱스
리튬 증착 전류 밀도($j_{\text{plating}}$)는 음극 표면의 국부 과전위($\eta_{\text{plating}}$) 및 온도에 따른 전하 전달 속도론에 의해 결정되며, Butler-Volmer 수식으로 엄격히 지배됩니다:
$$j_{\text{plating}} = j_{0, \text{plating}} \left[ \exp\left( \frac{\alpha_a F \eta_{\text{plating}}}{R T} \right) - \exp\left( -\frac{\alpha_c F \eta_{\text{plating}}}{R T} \right) \right]$$
여기서 $j_{0, \text{plating}}$은 리튬 증착 교환 전류 밀도이며, 활성화 과전위는 $\eta_{\text{plating}} = \Phi_s - \Phi_l - U^{\theta}_{\text{plating}}$ 로 규정됩니다. 금속 리튬의 평형 전위 $U^{\theta}_{\text{plating}}$은 $0\text{ V vs. Li/Li}^+$ 이므로, 고체상 전위($\Phi_s$)와 전해액상 전위($\Phi_l$)의 전위차($\Phi_s - \Phi_l$)가 음수가 될 때 음극 표면에서의 전하 전달 반응은 삽입 반응보다 금속 리튬 증착 반응을 선호하게 됩니다.

## 4. OCV 전압 이완 및 2차 미분 진단 기하학
BMS는 고속 충전 종료 후 휴지기(Rest period) 동안의 개로 전압(OCV) 이완 곡선을 분석하여 플레이팅을 비파괴적으로 검출합니다.
1. **스트리핑 고원(Stripping Plateau) 생성**: 증착된 금속 리튬이 전해액 및 음극과 상호작용하여 재이온화($Li^0 \rightarrow Li^+ + e^-$)되는 동안, 음극 표면 전위는 리튬 평형 전위에 고정되어 전압 상승 곡선에 특유의 평탄한 고원 구간이 발생합니다.
2. **2차 미분 알고리즘 ($d^2V/dt^2$)**: 미세한 고원 구간의 종점을 정밀 검출하기 위해 이완 전압 $V(t)$의 시간 미분을 수행합니다. 전압 변화율 $dV/dt$ 곡선의 변곡점과 시간 이완 곡선의 2차 미분 $d^2V/dt^2$ 곡선의 극대점(Local Maximum)을 탐지하여 플레이팅 종료 시점을 정밀 확정합니다:
$$t_{\text{strip\_end}} = \arg\max_{t} \left( \frac{d^2V}{dt^2} \right)$$
이 평탄 구간의 시간 폭($\Delta t_{\text{plateau}}$)과 전류 밀도를 역산하여 증착된 리튬 용량($Q_{\text{plated}}$)을 $Q_{\text{plated}} \approx I_{\text{stripping}} \times \Delta t_{\text{plateau}}$ 수식으로 정량 추정합니다.

## 5. 최종 퇴화 상태: 염 석출 (Salt Precipitation) 메커니즘
저온 및 고속 충전 시 발생하는 전기화학적 퇴화의 종단은 단순한 리튬 누적에 그치지 않고 전해액 부반응과 결합한 치명적인 **염 석출(Salt Precipitation)** 현상으로 이어집니다.
1. **반응 인과관계**: 극심한 플레이팅($Li^0$) 발생 $\rightarrow$ 증착된 다공성 금속 리튬 표면에서 유기 용매 분해 반응 폭증 $\rightarrow$ SEI 피막의 무기 성분($LiF, Li_2CO_3$) 이상 증식.
2. **국부 농도 붕괴 및 염 석출**: 전하 전달의 급격한 국부적 편중으로 인해 고체-액체 계면 확산 경계층 내의 리튬염(예: $LiPF_6$) 국부 농도가 용해 임계치를 초과하게 됩니다. 이로 인해 리튬염의 고체 상전이가 트리거되어 용해도가 낮은 유기 및 무기 결정성 **염 석출(Salt Precipitation)** 현상이 최종 도출됩니다.
3. **영향성**: 석출된 염 결정이 음극 활물질의 기공(Pores)과 분리막(Separator)의 나노 채널을 물리적으로 폐쇄(Pore Clogging)함으로써, 국부 이온 전도도($\sigma_{\text{ion}}$)가 급감하고 셀 내부의 전하 전달 저항($R_{\text{ct}}$) 및 확산 임계 저항이 폭증하여 배터리 가용 수명을 급격히 단축시킵니다.

## 6. 완화 및 예방 프로토콜
- **음극 전위 관측 제어 (Anode Potential Observer)**: 실시간 전기화학 모델을 기반으로 $\Phi_s - \Phi_l > 10.0\text{ mV}$ 안전 마진을 사수하도록 다단계 충전 전류(MCC)를 가변 통제합니다.
- **저온 충전 능동 차단**: 셀 온도가 $0^\circ\text{C}$ 이하일 경우 플레이팅 예방을 위해 충전 심도를 0.2C 이하로 강제 억제하고 온열 히터를 구동합니다.

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- [[[Concept] Battery-Management-System-BMS-and-Safety-Intelligence]]
- [[[Data] Battery-Lithium-Plating-Detection-Performance-Log_2026-05-16]]
- [[[Entity] advanced-anode-and-cathode-materials-for-next-gen-batteries]]

[V7.8_ENTERPRISE_VERIFIED]