# storage — 78.6/100

**2** scenarios passed, **1** failed, **3** undetermined (6 total) · 2026-08-21 21:06 · 33% pass rate

> Le verdict PASS/FAIL est déterminé par l'outcome contractuel des questions. Le score 0–100 mesure la performance et ne détermine pas le verdict.

Average performance: 78.6/100 · Questions above threshold: 23/30

## By category

| Category | ✅ Passed | ❌ Failed | ⚠️ Undetermined |
|----------|-------:|-------:|-------:|
| ✅ capacity | 0 | 0 | 2 |
| ⚠️ data-protection | 1 | 1 | 0 |
| ✅ volumes | 1 | 0 | 1 |

## ❌ Failed scenarios

- ❌ **storage/data-protection/001-backup-verification**
  - Q1 — FAIL_NOT_DELIVERED
  - Q2 — FAIL_NOT_DELIVERED
  - Q3 — FAIL_INVALID
  - Q4 — FAIL_NOT_DELIVERED
  - Q5 — FAIL_NOT_DELIVERED

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 75 | 70 | 19 | 10 | 16 | 16 | 0 | 12 | 16 |
| Q2 | 63 | 64 | 12 | 4 | 16 | 16 | 0 | 12 | 16 |
| Q3 | 74 | 67 | 20 | 10 | 16 | 16 | 13 | 12 | 0 |
| Q4 | 67 | 70 | 11 | 10 | 16 | 16 | 0 | 12 | 16 |
| Q5 | 77 | 74 | 18 | 10 | 16 | 16 | 4 | 12 | 16 |


## ⚠️ Undetermined scenarios

- ⚠️ **storage/capacity/001-volume-capacity-forecast** — UNDETERMINED
- ⚠️ **storage/capacity/002-large-unused-volumes** — UNDETERMINED
- ⚠️ **storage/volumes/002-pending-pvc-investigation** — UNDETERMINED
