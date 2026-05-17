---
metadata:
  date: "2026-05-16"
  id: "[[[Strategy] MedTech-Regulatory-and-Safety-Standard]]"
  project: "Vault_Modernization"
  version: "v7.8_Enterprise_Node"
  revision: "r1"
  domain: "10_Bio_Healthcare"
  last_updated: "2026-05-17T22:59:20+09:00"
lineage:
  dataset_reference: "global-dataset-inventory-hub"
  original_author: "Antigravity Vault"
  original_hash: "09ced0b184beb5042862d109d655fb48e59623a2898eb116b3f3a7c47493ea14"
object:
  object_type: "Concept"
  tier: 1
  description: '[Strategy] MedTech-Regulatory-and-Safety-Standard에 관한 고밀도 지능 노드'
temporal:
  valid_from: "2026-05-17T22:59:20+09:00"
  valid_to: null
semantic:
  is_instance_of: "[[[MOC] 10_Bio_Healthcare]]"
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


# [Strategy] MedTech-Regulatory-and-Safety-Standard

## 1. [왜 배우는가? (Why)]]
의료 기기는 사람의 생명을 다룹니다. 아주 작은 오작동이나 해킹 하나가 누군가의 생명을 앗아갈 수 있습니다. 의료 기술 규제 및 안전 표준(MedTech-Regulatory-and-Safety-Standard)은 기술이 '단순한 발명품'을 넘어 '안전한 의료 도구'가 되기 위한 엄격한 약속입니다. 공장에서 어떻게 만드는지(ISO 13485), 소프트웨어 코드를 어떻게 관리하는지(IEC 62304), 해킹을 어떻게 막는지에 대한 국제적인 규칙입니다. 이를 이해하는 것은 혁신적인 기술이 환자의 곁에 안전하게 도달할 수 있도록 길을 닦는 '의료 규제 전문가'이자 '안전의 설계자'가 되는 것입니다.

## 2. [핵심 기술 사양 (Numerical Specs)]

| Component | Technology / Logic | Engineering Rationale |
|:---|:---:|:---|
| **ISO 13485** | QMS Standard | 의료 기기 특화 품질 경영 시스템. 설계부터 폐기까지 전 과정의 문서화 및 이력 관리 |
| **IEC 62304** | SW Lifecycle | 의료용 소프트웨어의 위험 등급(Class A, B, C)에 따른 엄격한 개발 및 테스트 표준 |
| **PCCP** | AI Update Plan | AI 알고리즘이 시장 출시 후 업데이트될 때마다 새로 허가받지 않아도 되는 사전 승인 제도 |
| **SBOM** | Software Bill of Mat. | 소프트웨어에 들어간 모든 오픈소스와 부품 목록을 투명하게 공개하여 보안 취약점 관리 |
| **ISO 14971** | Risk Management | 기기 사용 시 발생할 수 있는 모든 위험을 예측하고, 이를 허용 가능한 수준으로 낮추는 프로세스 |

## 3. [공학적 근거 (Scientific Rationale)]

### 3.1 FDA와 ISO 13485의 통합(QMSR)
- **논리**: 국가마다 품질 관리 기준이 다르면 제조사가 너무 힘듭니다. 
- **결과**: 2026년부터 FDA가 국제 표준인 ISO 13485를 전격 수용함에 따라, 한 번의 품질 인증으로 전 세계 시장에 진출할 수 있는 '글로벌 규제 조화'가 이루어져 혁신 기기의 보급 속도가 빨라졌습니다.

### 3.2 AI 기반 의료 기기의 동적 규제(PCCP)
- **논리**: AI는 데이터를 먹으며 계속 변하는데, 변할 때마다 재허가를 받는 것은 불가능합니다. 
- **효과**: 개발사가 미리 "이런 방향으로 성능을 개선하겠다"는 계획(PCCP)을 제출하고 승인받으면, 나중에 알고리즘이 업데이트되어도 환자의 안전을 해치지 않는 선에서 즉시 시장에 적용할 수 있습니다.

### 3.3 사이버 보안-by-디자인(Security-by-Design)
- **논리**: 연결된 의료 기기(IoMT)는 해커의 표적이 되기 쉽습니다. 
- **결과**: 개발 초기부터 보안 기능을 내재화하고, 소프트웨어 자재 명세서(SBOM)를 통해 취약점이 발견된 오픈소스를 즉시 파악하고 패치함으로써 환자의 생명과 개인정보를 해킹 위협으로부터 보호합니다.

## 4. [코드 연결 해설 (Regulatory Compliance & Risk Assessment Engine)]
제품 개발 단계에서 발생할 수 있는 위험 요소를 식별하고 규제 표준(IEC 62304) 준수 여부를 체크하는 논리 구조입니다.
```python
def conduct_medtech_compliance_audit(project_data, regulatory_standard):
    # 1. 소프트웨어 위험 등급 분류 (Safety Classification)
    # 기기 오작동 시 환자에게 미치는 영향에 따라 Class (A, B, C) 결정
    risk_class = project_data.evaluate_patient_impact()
    
    # 2. IEC 62304 프로세스 준수 점검 (Process Audit)
    # 위험 등급에 맞는 코드 리뷰, 유닛 테스트, 통합 테스트 문서화 여부 확인
    compliance_score = compliance_engine.check_documentation(project_data, risk_class)
    
    # 3. 사이버 보안 취약점 스캔 (SBOM Scan)
    # 사용된 오픈소스 라이브러리 중 CVE 취약점이 등록된 항목 탐지
    vulnerabilities = sbom_scanner.scan_components(project_data.libraries)
    
    # 4. 잔여 위험 평가 (Residual Risk Assessment)
    # 위험 통제 조치(Risk Control) 후에도 남은 위험이 수용 가능한지 판단
    is_safe_to_release = risk_manager.evaluate_iso_14971(project_data.risks, vulnerabilities)
    
    # 5. 인허가 서류(Submission Dossier) 자동 생성
    if is_safe_to_release and compliance_score > 95:
        submission_dossier.generate(format="FDA_510K_OR_CE_MDR")
        audit_status = "READY_FOR_SUBMISSION"
    else:
        audit_status = "REMEDIATION_REQUIRED"
        
    return {"status": audit_status, "class": risk_class, "security_issues": len(vulnerabilities)}
```

## 5. [스스로 체크 (Self-Audit)]
1. 'ISO 13485' 품질 경영 시스템이 일반적인 'ISO 9001'과 구별되는 '의료 기기 특화' 요구 사항(추적성, 청정도 관리 등)은?
2. 'FDA'의 'PCCP(사전 승인 변경 관리 계획)' 제도가 'AI 의료 기기'의 '지속적 성능 개선'과 '환자 안전' 사이의 균형을 맞추는 방법은?
3. '의료 기기 소프트웨어' 개발에서 'IEC 62304' 표준이 '위험 등급(Class A, B, C)'에 따라 요구하는 '문서화 및 테스트'의 수준 차이는?

**[V6.3.7_HDS_GOLD_MANDATE_ACTIVATED]**
