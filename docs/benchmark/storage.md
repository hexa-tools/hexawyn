# storage — 73.5/100

**0** scenarios passed, **3** failed, **1** undetermined (4 total) · 2026-08-21 05:25 · 0% pass rate

> Le verdict PASS/FAIL est déterminé par l'outcome contractuel des questions. Le score 0–100 mesure la performance et ne détermine pas le verdict.

Average performance: 73.5/100 · Questions above threshold: 9/15

## By category

| Category | ✅ Passed | ❌ Failed | ⚠️ Undetermined |
|----------|-------:|-------:|-------:|
| ⚠️ capacity | 0 | 1 | 1 |
| ⚠️ volumes | 0 | 2 | 0 |

## ❌ Failed scenarios

- ❌ **storage/capacity/002-large-unused-volumes**
  - Q1 — UNDETERMINED
  - Q2 — FAIL_NOT_DELIVERED
  - Q3 — UNDETERMINED
  - Q4 — UNDETERMINED

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q2 | 70 | 68 | 16 | 16 | 16 | 16 | 0 | 4 | 16 |
| Q3 | 83 | 79 | 20 | 16 | 16 | 16 | 11 | 4 | 16 |
| Q4 | 81 | 76 | 20 | 16 | 16 | 16 | 8 | 4 | 16 |

- ❌ **storage/volumes/001-stale-pvc-detection**
  - Q1 — FAIL_NOT_DELIVERED

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 65 | 78 | 3 | 10 | 16 | 16 | 4 | 16 | 16 |

- ❌ **storage/volumes/002-pending-pvc-investigation**
  - Q1 — FAIL_NOT_DELIVERED
  - Q2 — UNDETERMINED
  - Q3 — PASS_ABSTENTION
  - Q4 — UNDETERMINED
  - Q5 — UNDETERMINED

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 75 | 79 | 12 | 16 | 16 | 16 | 3 | 12 | 16 |
| Q2 | 82 | 84 | 15 | 16 | 16 | 16 | 8 | 12 | 16 |
| Q3 | 85 | 81 | 20 | 16 | 16 | 16 | 13 | 4 | 16 |
| Q4 | 64 | 67 | ? | 10 | 16 | 16 | 9 | 0 | 16 |
| Q5 | 75 | 77 | 13 | 16 | 16 | 16 | 9 | 4 | 16 |


## ⚠️ Undetermined scenarios

- ⚠️ **storage/capacity/001-volume-capacity-forecast** — UNDETERMINED
