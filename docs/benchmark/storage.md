# storage — 74.1/100

**2** scenarios passed, **3** failed, **0** undetermined (5 total) · 2026-08-22 00:13 · 40% pass rate

> Le verdict PASS/FAIL du test est déterminé par le score (>=75 → PASS). L'outcome interne reste un diagnostic disponible pour l'investigation.

Average performance: 74.1/100 · Questions above threshold: 5/13

## By category

| Category | ✅ Passed | ❌ Failed | ⚠️ Undetermined |
|----------|-------:|-------:|-------:|
| ⚠️ capacity | 1 | 1 | 0 |
| ✅ data-protection | 1 | 0 | 0 |
| ⚠️ volumes | 0 | 2 | 0 |

## ❌ Failed scenarios

- ❌ **storage/capacity/001-volume-capacity-forecast**
  - Q1 — FAIL (57/100) [outcome: UNDETERMINED]
  - Q2 — FAIL (65/100) [outcome: UNDETERMINED]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 57 | 59 | ? | 4 | 16 | 16 | 3 | 4 | 16 |
| Q2 | 65 | 56 | 20 | 4 | 16 | 16 | 0 | 4 | 16 |

- ❌ **storage/volumes/001-stale-pvc-detection**
  - Q1 — FAIL (71/100) [outcome: FAIL_INVALID]
  - Q2 — FAIL (61/100) [outcome: FAIL_NOT_DELIVERED]
  - Q3 — PASS (83/100) [outcome: PASS_LIMITED]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 71 | 67 | 17 | 10 | 16 | 16 | 9 | 16 | 0 |
| Q2 | 61 | 73 | 3 | 10 | 16 | 16 | 3 | 12 | 16 |
| Q3 | 83 | 80 | 19 | 10 | 16 | 16 | 10 | 12 | 16 |

- ❌ **storage/volumes/002-pending-pvc-investigation**
  - Q1 — FAIL (74/100) [outcome: UNDETERMINED]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 74 | 72 | 16 | 10 | 16 | 16 | 14 | 0 | 16 |

