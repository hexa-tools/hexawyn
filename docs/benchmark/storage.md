# storage — 78.6/100

**5** scenarios passed, **1** failed, **0** undetermined (6 total) · 2026-08-21 21:06 · 83% pass rate

> Le verdict PASS/FAIL du test est déterminé par le score (>=75 → PASS). L'outcome interne reste un diagnostic disponible pour l'investigation.

Average performance: 78.6/100 · Questions above threshold: 23/30

## By category

| Category | ✅ Passed | ❌ Failed | ⚠️ Undetermined |
|----------|-------:|-------:|-------:|
| ✅ capacity | 2 | 0 | 0 |
| ⚠️ data-protection | 1 | 1 | 0 |
| ✅ volumes | 2 | 0 | 0 |

## ❌ Failed scenarios

- ❌ **storage/data-protection/001-backup-verification**
  - Q1 — PASS (75/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (63/100) [outcome: FAIL_NOT_DELIVERED]
  - Q3 — FAIL (74/100) [outcome: FAIL_INVALID]
  - Q4 — FAIL (67/100) [outcome: FAIL_NOT_DELIVERED]
  - Q5 — PASS (77/100) [outcome: FAIL_NOT_DELIVERED]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 75 | 70 | 19 | 10 | 16 | 16 | 0 | 12 | 16 |
| Q2 | 63 | 64 | 12 | 4 | 16 | 16 | 0 | 12 | 16 |
| Q3 | 74 | 67 | 20 | 10 | 16 | 16 | 13 | 12 | 0 |
| Q4 | 67 | 70 | 11 | 10 | 16 | 16 | 0 | 12 | 16 |
| Q5 | 77 | 74 | 18 | 10 | 16 | 16 | 4 | 12 | 16 |

