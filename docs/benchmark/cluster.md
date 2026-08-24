# cluster — 80.2/100

**8** scenarios (40 questions) · scenario pass rate 88% (7/8) · question pass rate 75% (30/40) · 2026-08-24 21:04

Questions: **30 PASS** / **10 FAIL** (of 40) · Average performance: 80.2/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| capacity | ✅ | 2 | 9 | 10 |
| health | ✅ | 2 | 8 | 10 |
| nodes | ✅ | 3 | 11 | 15 |
| upgrade | ⚠️ | 0 | 2 | 5 |

## ❌ Failed scenarios

- ❌ **cluster/upgrade/001-upgrade-blast-radius**
  - Q1 — PASS (89/100) [outcome: PASS]
  - Q2 — FAIL (71/100) [outcome: PASS]
  - Q3 — PASS (76/100) [outcome: FAIL_INVALID]
  - Q4 — FAIL (66/100) [outcome: FAIL_NOT_DELIVERED]
  - Q5 — FAIL (70/100) [outcome: FAIL_INVALID]

## 📉 Questions below threshold

- ❌ **cluster/capacity/002-node-pool-imbalance**
  - Q2 — FAIL (70/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cluster/health/002-cross-region-comparison**
  - Q4 — FAIL (71/100) [outcome: PASS_ABSTENTION]
  - Q5 — FAIL (70/100) [outcome: PASS]
- ❌ **cluster/nodes/001-node-drain-planning**
  - Q4 — FAIL (67/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cluster/nodes/002-node-hardware-health**
  - Q3 — FAIL (68/100) [outcome: FAIL_INVALID]
- ❌ **cluster/nodes/003-node-label-taint-inventory**
  - Q1 — FAIL (60/100) [outcome: UNDETERMINED]
  - Q2 — FAIL (69/100) [outcome: UNDETERMINED]
