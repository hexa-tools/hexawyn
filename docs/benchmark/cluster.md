# cluster — 77.0/100

**8** scenarios (40 questions) · scenario pass rate 88% (7/8) · question pass rate 70% (28/40) · 2026-08-24 04:29

Questions: **28 PASS** / **12 FAIL** (of 40) · Average performance: 77.0/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| capacity | ✅ | 2 | 9 | 10 |
| health | ✅ | 2 | 7 | 10 |
| nodes | ⚠️ | 2 | 9 | 15 |
| upgrade | ✅ | 1 | 3 | 5 |

## ❌ Failed scenarios

- ❌ **cluster/nodes/001-node-drain-planning**
  - Q1 — FAIL (74/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (70/100) [outcome: FAIL_NOT_DELIVERED]
  - Q3 — PASS (84/100) [outcome: PASS]
  - Q4 — FAIL (66/100) [outcome: FAIL_NOT_DELIVERED]
  - Q5 — PASS (78/100) [outcome: FAIL_NOT_DELIVERED]

## 📉 Questions below threshold

- ❌ **cluster/capacity/002-node-pool-imbalance**
  - Q2 — FAIL (70/100) [outcome: UNDETERMINED]
- ❌ **cluster/health/001-global-health-audit**
  - Q3 — FAIL (68/100) [outcome: UNDETERMINED]
- ❌ **cluster/health/002-cross-region-comparison**
  - Q3 — FAIL (70/100) [outcome: PASS]
  - Q5 — FAIL (71/100) [outcome: PASS]
- ❌ **cluster/nodes/002-node-hardware-health**
  - Q3 — FAIL (68/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (61/100) [outcome: UNDETERMINED]
- ❌ **cluster/nodes/003-node-label-taint-inventory**
  - Q2 — FAIL (55/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cluster/upgrade/001-upgrade-blast-radius**
  - Q1 — FAIL (74/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (63/100) [outcome: FAIL_NOT_DELIVERED]
