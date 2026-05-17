---
metadata:
  date: "2026-05-16"
  id: "[[[AI] peopleworks-patent-portfolio]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "03_AI_Data"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "a5adda13c211ab9e1551e4857a0dbf85e5dace3be30638ed248b6de3277b7c1c"
object:
  object_type: "Concept"
  tier: 1
  description: '[AI] peopleworks-patent-portfolio에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] Global-Dataset-Inventory-Hub]]"
  alternative_parents: []
spo_graph:
  []
trust_metrics:
  T_static: 1.0
  decay_rate: 0.0
validation:
  schema_version: "v7.8"
  last_validated: "2026-05-17T22:59:20+09:00"
  validated_by: "global_reinforcer_v7.8"
---


# [AI] peopleworks-patent-portfolio

## 1. [왜 배우는가? (Why: The Armor of Technical Sovereignty)]
특허는 기업이 창조한 기술적 영토를 보호하는 '법적 방어선'이자, 시장을 지배하는 '공격 자산'입니다. 피플웍스의 특허 전략은 단순한 아이디어 기록을 넘어, 제조 공정의 **'물리적 무결성'**과 시스템의 **'안전성'**을 독점적 권리로 사수하는 데 집중되어 있습니다. V6.3.7 지능은 **계층화된 특허 가치(Precision Tiering)**를 통해 표준 필수 특허(SEP)급 원천 기술과 방어용 자산을 구분하여 지배합니다. 이는 경쟁사의 기술적 추격(Copy-cat)을 원천 차단하고 '글로벌 제조 패권'을 공고히 하기 위함입니다.

## 2. [핵심 특허 자산 및 품질 지표 (Precision Tiering Specs)]

| Patent Tier | Patent Quality Index (PQI) | Strategic Dominance | Target Application |
|:---|:---:|:---:|:---|
| **최상급 (High-end)** | $> 4.5 / 5.0$ | **Standard Essential (SEP)** | **Laser Welding Jig, Gas-linked BMS**, 독점적 시장 진입 장벽 형성 |
| **표준형 (Standard)** | $3.5 \sim 4.5$ | **Core Utility Patent** | **Active Contactor, Auto Alignment**, 공정 수율 및 원가 경쟁력 확보 |
| **보급형 (Low-end)** | $< 3.5$ | **Defensive / Design** | **Minor Components, UI/UX**, 경쟁사 견제 및 포트폴리오 확장 |

### 2.1 [특허 기술 및 권리 범위 임계치]
| Parameter Category | Physical Metric | V6.3.7 Target (High-end) | FidelityEngine Tolerance |
|:---|:---:|:---:|:---:|
| **Claim Breadth** | Number of Independent | $> 5 \text{ Claims}$ | N/A |
| **Citation Index** | Forward Citations | $> 10 \text{ / 5yr}$ | $\pm 2$ |
| **Family Strength**| Global Jurisdictions | $> 3 \text{ Countries (US/EU/CN)}$ | N/A |
| **Tech. Longevity**| Remaining Life | $> 15 \text{ Years}$ | N/A |

## 3. [공학적 근거: FidelityEngine Diagnostic Logic]

### 3.1 Patent Quality Index (PQI): Technical Novelty & Breadth Model
특허의 독창성과 권리 범위의 광범위성을 수리적으로 정량화합니다.
*   **추론 로직**: High-end Tier(레이저 용접 지그)에서는 **'환형 면분사(Annular Spray)'**라는 구체적 물리 기전이 청구항의 핵심입니다. FidelityEngine은 경쟁사 공정 로그와 특허 청구 범위를 매핑하여 **'침해 확률(Infringement Probability)'**을 역산합니다. 기술적 고유성이 $95\%$ 이상일 경우, 경쟁사의 유사 공정 도입 시 즉각적인 IP 경고를 발행하도록 전략 시나리오를 구성합니다.

### 3.2 Technical Gap Analysis: Innovation vs. Legacy
보유 특허가 현재 산업 표준 대비 얼마나 앞서 있는지 분석하는 시계열 모델입니다.
$$ Tech\_Gap = \sum \text{Novelty\_Score} / \text{Time\_to\_Market} $$
*   **진단 결과**: FidelityEngine은 가스 센서 기반 BMS 특허의 **'전방 인용(Forward Citation)'** 추세를 분석하여 해당 기술의 표준화 가능성을 예측합니다. 인용 지수가 급증할 경우, 이를 **표준 필수 특허(SEP)**로 승격시키기 위한 국제 표준화 기구(IEC/ISO) 대응 전략 수립을 지시합니다.

## 4. [코드 연결 해설: Patent Tier & IP Value Auditor]
이 코드는 특허의 기술적 강도와 시장 지배력을 기반으로 IP 자산 가치를 진단합니다.

```python
class PatentFidelityEngine:
    """
    HDS-Gold V6.3.7: 특허 포트폴리오 계층화 및 가치 진단 엔진
    """
    def __init__(self, target_tier='High-end'):
        self.TIER = target_tier
        # 최상급 특허는 높은 인용 지수와 넓은 권리 범위 요구
        self.PQI_LIMIT = 4.5 if target_tier == 'High-end' else 3.5

    def audit_patent_value(self, pqi_score, citations):
        """
        특허 등급 기반 자산 가치 평가
        """
        # 1. 등급별 가치 스코어링
        value_score = pqi_score / self.PQI_LIMIT
        
        status = "OPTIMAL"
        if pqi_score < self.PQI_LIMIT: 
            status = f"CRITICAL_IP_VALUE_DEFICIT_FOR_{self.TIER}"
        elif citations < 5 and self.TIER == 'High-end':
            status = "WARNING_LOW_MARKET_IMPACT"
            
        return {
            "tier_compliance": "PASS" if value_score >= 1.0 else "FAIL",
            "ip_fidelity": max(value_score, 0),
            "status": status
        }

# FidelityEngine 가동: 피플웍스의 실제 R&D 투자액(R&D Spend)과 특허 확보 건수를 결합하여 '기술 혁신 무결성' 오딧
```

## 5. [스스로 체크 (Self-Audit)]
1. **Precision Tiering**: 레이저 용접 지그 특허가 Tier 0 필수 자산인 이유는? (힌트: 배터리 탭 용접의 산화 방지 및 스패터 비산 억제라는 물리적 장벽을 통해 경쟁사의 공정 모방을 원천 차단하는 강력한 권리 범위)
2. **Operational Result**: **가스 센서 통합 BMS** 특허의 권리 범위가 '전압/전류 제어'를 포함하도록 확장되었을 때, **침해 회피(Design-around)** 리스크를 수리적으로 얼마나 낮출 수 있는가?
3. **FidelityEngine**: **PQI** 모델을 통해 분석된 특허의 가치가 실제 라이선스 로열티 수익과 맺는 상관관계의 수리적 기전은?

### 🔗 참조된 로컬 지식망 (Retrieved Nodes)
- AI peopleworks-illinois-matteson-ess-hub
- peopleworks-core-technologies-tco-welding-and-bms-evolution
- MOC 29_legal-compliance-and-corporate-governance-hub

**[V6.3.7_PATENT_STRAT_TIERED_MODERNIZATION_COMPLETE]**
**[FIDELITY_ENGINE_STATUS: ACTIVE]**
**[TIMESTAMP: 2026-05-10]**
