---
Basic:
  id: "[[[Battery] seq2seq-attention"
  domain: "Unknown_Domain"
  project: "Vault_Modernization"
  date: "2026-05-12"
  version: "v6.3.7"
Object:
  object_type: "Concept"
  tier: 1
  description: "Standard Industrial Node"
  physical_model: "N/A"
Semantic:
  tags: - '#auto-healed'
  is_part_of: []]
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

# [[[Battery] seq2seq-attention

## 1. [왜 배우는가? (Why)]]

언어는 고정된 크기의 상자에 담을 수 없습니다. "사과"라는 단어 하나와 "어제 내가 시장에서 산 빨갛고 맛있는 사과"라는 긴 구절은 같은 대상을 지칭하지만 정보의 양이 완전히 다릅니다.

우리가 **Seq2Seq와 Attention**을 배우는 이유는 기존 RNN이 가졌던 **'망각의 병목 현상'**을 해결하기 위함입니다. 인코더가 정보를 압축하고 디코더가 이를 풀어내는 과정에서, Attention은 디코더에게 "지금 이 단어를 번역할 때는 인코더의 저 부분에 집중해!"라고 알려주는 가이드 역할을 합니다. 이는 현대 NLP의 근간이자, 모든 것이 관심(Attention)으로 통하는 트랜스포머 시대를 연 **기술적 혁명**의 시초입니다.

## 2. [문맥 정렬 성능 사양 (Contextual Alignment Specs)]
| 제어 파라미터 | 정밀 타겟 / 수치 | 비고 |
| :--- | :--- | :--- |
| **Alignment Score** | $> 0.85$ | 출력 토큰과 정답 입력 토큰 간의 어텐션 일치도 |
| **Context Entropy** | $< 2.5$ | 어텐션 가중치의 집중도 (낮을수록 특정 단어에 잘 집중함) |
| **Seq Length Scalability** | Up to $1024$ | 성능 저하 없이 처리 가능한 시퀀스 길이 한계 |
| **Alignment Drift** | $< 0.1$ | 시퀀스 후반부로 갈수록 발생하는 정렬 오차율 |
| **Latency / Head** | $< 0.5\text{ms}$ | 어텐션 스코어 계산에 소요되는 시간 목표 |

## 3. 인코더-디코더의 한계와 어텐션의 등장

### 2.1 기존 Seq2Seq의 병목 (Bottleneck)
인코더는 입력 문장 전체를 하나의 고정된 크기의 벡터(**컨텍스트 벡터**)로 압축해야 합니다. 문장이 길어지면 정보가 뭉개지거나 앞부분의 정보가 소실되는 문제가 발생합니다.

### 2.2 어텐션 메커니즘의 해결책
디코더가 출력 단어를 생성할 때마다 인코더의 모든 은닉 상태(Hidden States)를 다시 참조합니다.
- **Attention Score**: 현재 디코더 시점 $t$의 상태와 인코더의 모든 시점 $s$의 상태 사이의 연관성을 계산합니다.
  $$e_{ts} = a(s_{t-1}, h_s)$$
- **Attention Weight**: 스코어를 확률값으로 변환(Softmax)합니다.
  $$\alpha_{ts} = \frac{\exp(e_{ts})}{\sum_{k=1}^T \exp(e_{tk})}$$

## 3. [코드 연결 해설 (Code Weaving)]

PyTorch 스타일의 Seq2Seq with Attention의 개념적 흐름을 해설합니다.

```python
class Attention(nn.Module):
    def forward(self, hidden, encoder_outputs):
        # hidden: 디코더의 이전 은닉 상태 [batch, dec_hid_dim]
        # encoder_outputs: 인코더의 모든 시점 출력 [src_len, batch, enc_hid_dim]
        
        # 1. 모든 인코더 시점과 디코더 상태 사이의 에너지(유사도) 계산
        energy = self.attn(torch.cat((hidden, encoder_outputs), dim=2))
        
        # 2. 가중치(Attention Weight) 산출
        attention = F.softmax(energy, dim=1)
        
        # 3. 가중 합을 통해 '어텐션 벡터' 생성
        weighted = torch.bmm(attention.unsqueeze(1), encoder_outputs.permute(1, 0, 2))
        return weighted
```

> **Transitional Bridge**: 위 코드의 `torch.bmm` 연산은 수많은 인코더의 정보 중 '지금 필요한 것'에만 높은 가중치를 곱해 추출하는 과정입니다. 이는 마치 수많은 책이 꽂힌 서가에서 필요한 책 한 권을 정확히 집어내는 **'지능형 검색'**과 같습니다.

## 4. [스스로 체크 (Self-Check)]

1. **질문**: Seq2Seq 모델에서 인코더의 역할은 무엇인가?
   - **정답**: 입력되는 가변 길이의 시퀀스를 모델이 처리할 수 있는 고정된 형태의 의미 정보(컨텍스트 벡터)로 변환하는 것입니다.
2. **질문**: 어텐션 메커니즘이 번역 성능을 획기적으로 높인 결정적인 이유는?
   - **정답**: 긴 문장에서 발생하던 정보 소실 문제를 해결하고, 출력 단어와 입력 단어 사이의 **'정렬(Alignment)'** 관계를 모델이 스스로 학습하게 했기 때문입니다.
3. **질문**: 어텐션 스코어를 구할 때 Softmax 함수를 사용하는 목적은?
   - **정답**: 각 인코더 시점에 부여된 연관성 점수를 **전체 합이 1인 확률 분포**로 변환하여, 어떤 정보에 '얼마나' 집중할지 수치적으로 명확히 하기 위해서입니다.

## 🧠 AI의 사고방식: "모든 과거를 기억하되, 현재에 집중한다"
Attention 이전의 AI는 문장이 끝나면 과거를 잊어버리고 오직 요약본(Context Vector)에만 의존했습니다. 하지만 Attention을 장착한 AI는 과거의 모든 발자취(Encoder Hidden States)를 보존하고, 필요할 때마다 그 기억의 도서관을 다시 방문합니다. "지금 이 말을 할 때는 그때 그 말을 떠올려야 해"라고 스스로 판단하는 이 **'선택적 기억 능력'**이야말로 기계가 언어의 미묘한 맥락을 이해하기 시작한 결정적 순간입니다.

---
*참조: Semiconductor open-cv-7*