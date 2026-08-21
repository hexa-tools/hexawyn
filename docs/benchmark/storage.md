# storage — 76.9/100

**1** scenarios passed, **3** failed, **1** undetermined (5 total) · 2026-08-21 04:43 · 20% pass rate

> Le verdict PASS/FAIL est déterminé par l'outcome contractuel des questions. Le score 0–100 mesure la performance et ne détermine pas le verdict.

Average performance: 76.9/100 · Questions above threshold: 11/17

## By category

| Category | ✅ Passed | ❌ Failed | ⚠️ Undetermined |
|----------|-------:|-------:|-------:|
| ⚠️ capacity | 0 | 2 | 0 |
| ✅ data-protection | 1 | 0 | 0 |
| ⚠️ volumes | 0 | 1 | 1 |

## ❌ Failed scenarios

- ❌ **storage/capacity/001-volume-capacity-forecast**
  - Q1 — FAIL_NOT_DELIVERED
  - Q2 — UNDETERMINED
  - Q3 — UNDETERMINED
  - Q4 — UNDETERMINED
  - Q5 — UNDETERMINED

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 82 | 79 | 19 | 16 | 16 | 16 | 3 | 12 | 16 |
| Q2 | 84 | 80 | 20 | 16 | 16 | 16 | 12 | 4 | 16 |
| Q3 | 90 | 87 | 20 | 16 | 16 | 16 | 11 | 12 | 16 |
| Q4 | 57 | 59 | ? | 4 | 16 | 16 | 3 | 4 | 16 |
| Q5 | 62 | 56 | 17 | 4 | 16 | 16 | 0 | 4 | 16 |

- ❌ **storage/capacity/002-large-unused-volumes**
  - Q1 — UNDETERMINED
  - Q2 — FAIL_INVALID
  - Q3 — FAIL_INVALID
  - Q4 — UNDETERMINED

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 84 | 80 | 20 | 16 | 16 | 16 | 12 | 4 | 16 |
| Q2 | 68 | 60 | 20 | 16 | 16 | 16 | 8 | 4 | 0 |
| Q3 | 74 | 68 | 20 | 16 | 16 | 16 | 16 | 4 | 0 |
| Q4 | 81 | 76 | 20 | 16 | 16 | 16 | 8 | 4 | 16 |

- ❌ **storage/volumes/001-stale-pvc-detection**
  - Q1 — FAIL_INVALID

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 75 | 70 | 19 | 10 | 16 | 16 | 12 | 16 | 0 |


## ⚠️ Undetermined scenarios

- ⚠️ **storage/volumes/002-pending-pvc-investigation** — UNDETERMINED
