# cluster — 79.5/100

**8** scenarios (40 questions) · scenario pass rate 100% (8/8) · question pass rate 78% (31/40) · 2026-08-24 23:02

Questions: **31 PASS** / **9 FAIL** (of 40) · Average performance: 79.5/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| capacity | ✅ | 2 | 8 | 10 |
| health | ✅ | 2 | 10 | 10 |
| nodes | ✅ | 3 | 10 | 15 |
| upgrade | ✅ | 1 | 3 | 5 |

## 📉 Questions below threshold

- ❌ **cluster/capacity/002-node-pool-imbalance**
  - Q1 — FAIL (74/100) [outcome: UNDETERMINED]
  - Q3 — FAIL (72/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cluster/nodes/001-node-drain-planning**
  - Q3 — FAIL (71/100) [outcome: FAIL_NOT_DELIVERED]
  - Q4 — FAIL (71/100) [outcome: PASS]
- ❌ **cluster/nodes/002-node-hardware-health**
  - Q5 — FAIL (54/100) [outcome: FAIL_INVALID]
- ❌ **cluster/nodes/003-node-label-taint-inventory**
  - Q2 — FAIL (58/100) [outcome: PASS_ABSTENTION]
  - Q3 — FAIL (66/100) [outcome: UNDETERMINED]
- ❌ **cluster/upgrade/001-upgrade-blast-radius**
  - Q2 — FAIL (73/100) [outcome: FAIL_NOT_DELIVERED]
  - Q4 — FAIL (66/100) [outcome: FAIL_NOT_DELIVERED]
