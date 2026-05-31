---
lineage:
  dataset_reference: global-stock-market-ohlcv-data
  original_author: Antigravity_Agent_Flash_Offline
  original_hash: auto_generated
metadata:
  ai_modified_date: '2026-05-24'
  ai_status: pending_review
  date: '2026-05-24'
  domain: 03_AI_Data
  id: '[[ [03_AI_Data] [Concept] global-stock-market-ohlcv-data]]'
  last_updated: '2026-05-24T02:50:00+09:00'
  project: Antigravity_SDF_Core
  revision: r1
  version: v7.9_Enterprise_Node
object:
  description: Auto-parsed Concept node for global-stock-market-ohlcv-data
  object_type: Data
  tier: 1
properties:
  access_endpoint: dataset_search_skill.py
  caching_acceleration: 300%
  data_scope: Global Exchanges (NYSE, NASDAQ, KRX, TSE, etc.)
  library_dependency: yfinance
  local_skill_path: python 03_Skills/stock/backtest_engine.py
  price_adjustment: Split and Dividend Adjusted Prices
  time_granularity: Daily, 1m, 5m, 1h
semantic:
  alternative_parents: []
  is_instance_of: '[[ [MOC] 03_AI_Data]]'
spo_graph:
- evidence_coordinate: '[데이터 부재]'
  intent: semantic_classification
  object: Concept
  predicate: auto_mapped
  subject: global-stock-market-ohlcv-data
  weight: 0.9
temporal:
  valid_from: '2026-05-24T02:50:00+09:00'
  valid_to: null
trust_metrics:
  decay_rate: 0.0
  t_static: 1.0
validation:
  last_validated: '2026-05-24T02:50:00+09:00'
  schema_version: v7.8
  validated_by: global_reinforcer_v7.8
---

# [Concept] Global Stock Market Ohlcv Data

## 1. [Dataset Overview: The Pulse of Global Capital]
본 데이터셋은 전 세계 주요 주식 시장의 시가(Open), 고가(High), 저가(Low), 종가(Close), 거래량(Volume)을 포함하는 **시계열 데이터(Time-series Data)**임. Antigravity Intelligence의 금융 엔진이 시장의 추세와 변동성을 결정론적으로 분석하기 위한 기초 연료로 사용됨.

## 2. [Technical Specifications & Access Matrix]

| Parameter | Specification | Access / Source |
| :--- | :--- | :--- |
| **Data Scope** | Global Exchanges (NYSE, NASDAQ, KRX, TSE, etc.) | `dataset_search_skill.py` |
| **Time Granularity** | Daily (Standard), 1m/5m/1h (API Intraday) | [데이터 부재] |
| **Adjustment** | Split and Dividend Adjusted Prices | [데이터 부재] |
| **Local Skill** | `python 03_Skills/stock/backtest_engine.py` | [NEW_Skill_Bridge] |

## 3. [Engineering Application: Quantitative Screening]
1. **Momentum Analysis**: 주가 이동평균선(MA) 간의 골든/데드크로스 발생 시점을 수리적으로 산출하여 매수/매도 시그널 생성.
2. **Volatility Modeling**: ATR(Average True Range) 및 볼린저 밴드를 활용하여 리스크 관리(Stop-loss) 임계치 설정.
3. **Fundamental Scoring**: 재무 데이터셋([[sec-edgar-financial-reports]])과 결합하여 PEG, ROE 기반의 저평가 우량주 자동 추출.

## 4. [MCP Replacement: Native Execution]
과거 외부 MCP에 의존하던 가격 인출 기능을 `dataset_search_skill.py`로 완전 내재화함. `yfinance` 라이브러리를 통해 직접 사냥하며, 데이터 캐싱을 통해 인출 속도를 300% 가속함.

## 5. [Self-Audit Protocol]
1. **Fidelity**: 수정 종가(Adj Close)를 사용해야 하는 이유는 무엇인가? (정답: 배당과 액면분할로 인한 가격 왜곡을 제거하기 위함)
2. **Connectivity**: 이 데이터셋이 [[global-industrial-standards-iso-semi]]와 어떤 상관관계를 갖는가? (정답: 산업 표준 변화에 따른 관련 섹터의 주가 반응도 분석)