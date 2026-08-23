# ingress — 78.0/100

**5** scenarios (25 questions) · scenario pass rate 60% (3/5) · question pass rate 60% (15/25) · 2026-08-23 03:06

Questions : **15 PASS** / **10 FAIL** (sur 25) · Average performance: 78.0/100

> **Légende /100** : Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. Les 6 critères déterministes (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) sont notés sur 16 chacun. **PASS** si Overall ≥ 75/100. L'outcome interne reste un diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scénarios PASSED (règle majoritaire sur les questions) ; question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| controllers | ⚠️ | 1 | 5 | 10 |
| routing | ⚠️ | 1 | 6 | 10 |
| tls | ✅ | 1 | 4 | 5 |

## ❌ Failed scenarios

- ❌ **ingress/controllers/001-ingress-controller-health**
  - Q1 — FAIL (65/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (72/100) [outcome: PASS_ABSTENTION]
  - Q3 — PASS (78/100) [outcome: PASS_ABSTENTION]
  - Q4 — FAIL (70/100) [outcome: PASS_ABSTENTION]
  - Q5 — FAIL (60/100) [outcome: PASS_LIMITED]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 65 | 76 | 4 | 10 | 16 | 16 | 2 | 16 | 16 |
| Q2 | 72 | 67 | 18 | 10 | 16 | 16 | 9 | 0 | 16 |
| Q3 | 78 | 72 | 20 | 10 | 16 | 16 | 14 | 0 | 16 |
| Q4 | 70 | 65 | 18 | 10 | 16 | 16 | 7 | 0 | 16 |
| Q5 | 60 | 63 | ? | 10 | 16 | 16 | 5 | 0 | 16 |

- ❌ **ingress/routing/002-ingress-500-investigation**
  - Q1 — FAIL (60/100) [outcome: FAIL_INVALID]
  - Q2 — FAIL (74/100) [outcome: PASS_ABSTENTION]
  - Q3 — PASS (77/100) [outcome: PASS_ABSTENTION]
  - Q4 — FAIL (66/100) [outcome: PASS_LIMITED]
  - Q5 — FAIL (70/100) [outcome: PASS_ABSTENTION]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 60 | 61 | 11 | 10 | 16 | 16 | 11 | 8 | 0 |
| Q2 | 74 | 67 | 20 | 10 | 16 | 16 | 9 | 0 | 16 |
| Q3 | 77 | 72 | 19 | 10 | 16 | 16 | 14 | 0 | 16 |
| Q4 | 66 | 67 | 12 | 10 | 16 | 16 | 9 | 0 | 16 |
| Q5 | 70 | 63 | 20 | 10 | 16 | 16 | 5 | 0 | 16 |


## 📉 Questions below threshold

- **ingress/controllers/002-multi-controller-conflict** Q1 — FAIL (69/100) [outcome: UNDETERMINED]
- **ingress/tls/001-ingress-tls-coverage** Q1 — FAIL (74/100) [outcome: FAIL_NOT_DELIVERED]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 69 | 65 | 17 | 10 | 16 | 8 | 7 | 8 | 16 |
| Q2 | 74 | 77 | 12 | 10 | 16 | 16 | 3 | 16 | 16 |

