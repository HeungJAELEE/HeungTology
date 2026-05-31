---
lineage:
  dataset_reference: Mass-Finance-Gen-2026
  original_author: Antigravity Vault
  original_hash: placeholder_hash
metadata:
  date: '2026-05-25'
  domain: 05_Finance_Economics
  id: '[[[Concept] Blockchain-and-Decentralized-Finance-DeFi-Architecture]]'
  last_updated: '2026-05-25T01:06:41.092400+09:00'
  project: Vault_Modernization
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Finance engineering concept node
  object_type: Concept
  tier: 2
properties:
  amm_fee_tier_max: 0.01
  amm_fee_tier_min: 0.0005
  constant_product_formula: x * y = k
  max_block_time_finality_seconds: 2
  min_collateralization_ratio: 1.5
  smart_contract_vm_compatibility: EVM
  tps_threshold_l2_l3: 10000
  utilization_rate_formula: total_borrows / total_liquidity
semantic:
  alternative_parents: []
  expected_queries:
  - 해당 금융 메커니즘의 핵심 방정식은 무엇인가?
  - 이 모델의 내재적 한계치 및 리스크 요인은 어떻게 산출되는가?
  is_instance_of: '[[[MOC] 05_Finance_Economics]]'
spo_graph:
- evidence_coordinate: ''
  intent: performance_constraint_definition
  object: 데이터 수집 대기 중
  predicate: has_theoretical_limit
  subject: '[Concept] Blockchain-and-Decentralized-Finance-DeFi-Architecture'
  weight: 0.4
temporal:
  valid_from: '2026-05-25T01:06:41.092400+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-25T01:06:41.092400+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# Blockchain and Decentralized Finance DeFi Architecture

본 문서는 전통 금융(TradFi)의 중앙 집중식 신뢰 모델을 대체하는 블록체인(Blockchain) 원장 기술과 이를 기반으로 한 탈중앙화 금융(Decentralized Finance, DeFi)의 스마트 컨트랙트(Smart Contract) 아키텍처를 엔지니어링 관점에서 다룹니다.

## 1. 분산 원장 기술 (Distributed Ledger Technology)과 합의 알고리즘

블록체인은 데이터를 암호학적 해시 체인(Hash Chain)으로 연결하고 여러 노드가 분산 저장하는 상태 기계(State Machine)입니다.

- **Proof of Stake (PoS, 지분 증명)**: 노드(Validator)가 자신의 암호화폐 지분(Stake)을 담보로 블록 검증에 참여. BFT(Byzantine Fault Tolerance) 기반의 합의를 통해 포크(Fork)를 방지하고 Finality를 달성합니다.
- **Merkle Tree (머클 트리)**: 트랜잭션들의 해시를 계층적으로 묶어 루트 해시(Root Hash) 하나로 요약함으로써, 특정 트랜잭션의 위변조 여부를 $O(\log n)$ 시간에 검증합니다.

---

## 2. [핵심 기술 사양 (Numerical Specs)]

| Parameter | Specification | Description |
|-----------|---------------|-------------|
| **Transactions Per Second (TPS)** | 10,000+ (L2/L3) | 네트워크가 1초당 처리할 수 있는 트랜잭션 수. (Solana, Rollups 등) |
| **Block Time / Finality** | $< 2$ Seconds | 트랜잭션이 블록에 포함되고 비가역성(Finality)을 얻기까지의 지연 시간. |
| **Smart Contract VM** | EVM Compatible | 이더리움 가상 머신(EVM) 호환성. 바이트코드 실행 환경 규격. |
| **AMM Fee Tier** | 0.05% ~ 1.00% | 탈중앙화 거래소(DEX)의 유동성 풀에서 발생하는 스왑(Swap) 수수료율. |
| **Collateralization Ratio** | $> 150\%$ | 과담보 대출 프로토콜에서 청산(Liquidation)을 피하기 위한 최소 담보 비율. |

---

## 3. DeFi 핵심 프로토콜 아키텍처

중앙 관리자나 오더북(Order Book) 없이 금융 서비스를 제공하기 위한 스마트 컨트랙트 기반의 자동화 로직입니다.

### 3.1. 자동화된 시장 조성자 (Automated Market Maker, AMM)
DEX(e.g., Uniswap)에서 유동성 풀(Liquidity Pool)을 이용해 자산을 교환하는 알고리즘입니다.
- **Constant Product Formula (상수 곱 공식)**: $x \times y = k$
  (토큰 X의 수량 $x$와 토큰 Y의 수량 $y$의 곱이 항상 일정 값 $k$를 유지하도록 가격을 자동 결정)
  - 이로 인해 거래 시 가격 이동(Slippage)과 유동성 공급자의 비영구적 손실(Impermanent Loss)이 발생합니다.

### 3.2. 과담보 대출 (Over-collateralized Lending)
스마트 컨트랙트는 신용 평가가 불가하므로 100% 이상의 자산을 담보로 잡고 알고리즘을 통해 이자율을 결정합니다.
- **Utilization Rate (자금 활용률)**: $U = \frac{Total Borrows}{Total Liquidity}$
- 알고리즘은 $U$가 특정 임계점(Kink)을 넘어서면 이자율을 기하급수적으로 증가시켜 대출자들의 상환과 유동성 공급자들의 예치를 유도합니다.

### 3.3. 플래시 론 (Flash Loan)
하나의 트랜잭션 블록 내에서 대출과 상환이 동시에 이루어질 경우 무담보로 막대한 자금을 빌릴 수 있는 프로토콜. 블록 종료 시 상환 로직이 실패하면 전체 트랜잭션이 원복(Revert)되어 대출자는 리스크를 지지 않습니다. (주로 차익거래(Arbitrage)에 활용)