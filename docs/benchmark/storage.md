# storage — 79.9/100

**6** scenarios (30 questions) · scenario pass rate 100% (6/6) · question pass rate 73% (22/30) · 2026-08-24 04:06

Questions: **22 PASS** / **8 FAIL** (of 30) · Average performance: 79.9/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| capacity | ✅ | 2 | 9 | 10 |
| data-protection | ✅ | 2 | 7 | 10 |
| volumes | ✅ | 2 | 6 | 10 |

## 📉 Questions below threshold

- ❌ **storage/capacity/002-large-unused-volumes**
  - Q3 — FAIL (74/100) [outcome: FAIL_INVALID]
- ❌ **storage/data-protection/001-backup-verification**
  - Q3 — FAIL (74/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **storage/data-protection/002-volume-snapshot-health**
  - Q1 — FAIL (71/100) [outcome: FAIL_INVALID]
  - Q4 — FAIL (73/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **storage/volumes/001-stale-pvc-detection**
  - Q2 — FAIL (66/100) [outcome: FAIL_NOT_DELIVERED]
  - Q3 — FAIL (74/100) [outcome: FAIL_INVALID]
- ❌ **storage/volumes/002-pending-pvc-investigation**
  - Q1 — FAIL (71/100) [outcome: FAIL_NOT_DELIVERED]
  - Q4 — FAIL (59/100) [outcome: FAIL_INVALID]
