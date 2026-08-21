# ingress — 78.0/100

**1** scenarios passed, **3** failed, **1** undetermined (5 total) · 2026-08-20 04:30 · 20% pass rate

> Le verdict PASS/FAIL est déterminé par l'outcome contractuel des questions. Le score 0–100 mesure la performance et ne détermine pas le verdict.

Average performance: 78.0/100 · Questions above threshold: 15/25

## By category

| Category | ✅ Passed | ❌ Failed | ⚠️ Undetermined |
|----------|-------:|-------:|-------:|
| ⚠️ controllers | 1 | 1 | 0 |
| ⚠️ routing | 0 | 1 | 1 |
| ⚠️ tls | 0 | 1 | 0 |

## ❌ Failed scenarios

- ❌ **ingress/controllers/002-multi-controller-conflict**
  - Q1 — FAIL_NOT_DELIVERED
  - Q2 — PASS_LIMITED
  - Q3 — PASS_ABSTENTION
  - Q4 — PASS_LIMITED
  - Q5 — PASS_LIMITED

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 63 | 68 | 9 | 10 | 16 | 16 | 2 | 8 | 16 |
| Q2 | 90 | 88 | 20 | 16 | 16 | 16 | 12 | 12 | 16 |
| Q3 | 90 | 88 | 20 | 16 | 16 | 16 | 12 | 12 | 16 |
| Q4 | 82 | 88 | 12 | 16 | 16 | 16 | 16 | 8 | 16 |
| Q5 | 81 | 78 | 19 | 16 | 16 | 2 | 16 | 12 | 16 |

- ❌ **ingress/routing/002-ingress-500-investigation**
  - Q1 — UNDETERMINED
  - Q2 — PASS_ABSTENTION
  - Q3 — FAIL_NOT_DELIVERED
  - Q4 — PASS_LIMITED
  - Q5 — PASS_ABSTENTION

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 75 | 76 | 14 | 10 | 16 | 16 | 10 | 8 | 16 |
| Q2 | 72 | 65 | 20 | 10 | 16 | 16 | 7 | 0 | 16 |
| Q3 | 68 | 63 | 18 | 10 | 16 | 16 | 5 | 0 | 16 |
| Q4 | 68 | 69 | 13 | 10 | 16 | 16 | 11 | 0 | 16 |
| Q5 | 66 | 67 | 12 | 10 | 16 | 16 | 9 | 0 | 16 |

- ❌ **ingress/tls/001-ingress-tls-coverage**
  - Q1 — FAIL_NOT_DELIVERED
  - Q2 — PASS_LIMITED
  - Q3 — PASS_LIMITED
  - Q4 — PASS_LIMITED
  - Q5 — PASS_LIMITED

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 74 | 77 | 12 | 10 | 16 | 16 | 3 | 16 | 16 |
| Q2 | 84 | 80 | 20 | 16 | 16 | 16 | 8 | 8 | 16 |
| Q3 | 92 | 91 | 19 | 16 | 16 | 16 | 11 | 16 | 16 |
| Q4 | 90 | 88 | 20 | 10 | 16 | 16 | 14 | 16 | 16 |
| Q5 | 91 | 90 | 19 | 10 | 16 | 16 | 16 | 16 | 16 |


## ⚠️ Undetermined scenarios

- ⚠️ **ingress/routing/001-ingress-routing-audit** — UNDETERMINED
