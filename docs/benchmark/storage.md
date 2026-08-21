# storage — 76.0/100

**3** scenarios passed, **3** failed, **0** undetermined (6 total) · 2026-08-21 23:18 · 50% pass rate

> Le verdict PASS/FAIL du test est déterminé par le score (>=75 → PASS). L'outcome interne reste un diagnostic disponible pour l'investigation.

Average performance: 76.0/100 · Questions above threshold: 17/30

## By category

| Category | ✅ Passed | ❌ Failed | ⚠️ Undetermined |
|----------|-------:|-------:|-------:|
| ⚠️ capacity | 1 | 1 | 0 |
| ⚠️ data-protection | 1 | 1 | 0 |
| ⚠️ volumes | 1 | 1 | 0 |

## ❌ Failed scenarios

- ❌ **storage/capacity/002-large-unused-volumes**
  - Q1 — FAIL (71/100) [outcome: UNDETERMINED]
  - Q2 — PASS (78/100) [outcome: UNDETERMINED]
  - Q3 — FAIL (74/100) [outcome: FAIL_INVALID]
  - Q4 — FAIL (68/100) [outcome: FAIL_INVALID]
  - Q5 — PASS (87/100) [outcome: UNDETERMINED]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 71 | 76 | ? | 16 | 16 | 16 | 8 | 4 | 16 |
| Q2 | 78 | 72 | 20 | 16 | 16 | 16 | 4 | 4 | 16 |
| Q3 | 74 | 68 | 20 | 16 | 16 | 16 | 16 | 4 | 0 |
| Q4 | 68 | 60 | 20 | 16 | 16 | 16 | 8 | 4 | 0 |
| Q5 | 87 | 84 | 20 | 16 | 16 | 16 | 16 | 4 | 16 |

- ❌ **storage/data-protection/001-backup-verification**
  - Q1 — FAIL (72/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (72/100) [outcome: PASS]
  - Q3 — FAIL (71/100) [outcome: FAIL_NOT_DELIVERED]
  - Q4 — FAIL (71/100) [outcome: PASS]
  - Q5 — PASS (76/100) [outcome: FAIL_INVALID]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 72 | 70 | 16 | 10 | 16 | 16 | 0 | 12 | 16 |
| Q2 | 72 | 77 | ? | 4 | 16 | 16 | 13 | 12 | 16 |
| Q3 | 71 | 73 | 13 | 10 | 16 | 16 | 3 | 12 | 16 |
| Q4 | 71 | 76 | ? | 10 | 16 | 16 | 6 | 12 | 16 |
| Q5 | 76 | 70 | 20 | 10 | 16 | 16 | 16 | 12 | 0 |

- ❌ **storage/volumes/001-stale-pvc-detection**
  - Q1 — FAIL (68/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (61/100) [outcome: FAIL_NOT_DELIVERED]
  - Q3 — PASS (76/100) [outcome: PASS_LIMITED]
  - Q4 — FAIL (61/100) [outcome: FAIL_NOT_DELIVERED]
  - Q5 — PASS (76/100) [outcome: PASS]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 68 | 78 | 6 | 10 | 16 | 16 | 4 | 16 | 16 |
| Q2 | 61 | 73 | 3 | 10 | 16 | 16 | 3 | 12 | 16 |
| Q3 | 76 | 70 | 20 | 4 | 16 | 16 | 14 | 4 | 16 |
| Q4 | 61 | 72 | 3 | 10 | 16 | 16 | 2 | 12 | 16 |
| Q5 | 76 | 70 | 20 | 10 | 16 | 16 | 0 | 12 | 16 |

