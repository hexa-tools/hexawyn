# finops — 79.1/100

**13** scenarios (70 questions) · scenario pass rate 85% (11/13) · question pass rate 74% (52/70) · 2026-08-26 21:34

Questions: **52 PASS** / **18 FAIL** (of 70) · Average performance: 79.1/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| forecasting | ✅ | 5 | 23 | 27 |
| optimization | ⚠️ | 4 | 18 | 27 |
| reporting | ⚠️ | 2 | 11 | 16 |

## ❌ Failed scenarios

- ❌ **finops/optimization/001-rightsizing-recommendations**
  - Q1 — FAIL (67/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (61/100) [outcome: FAIL_NOT_DELIVERED]
  - Q3 — FAIL (70/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (70/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (61/100) [outcome: UNDETERMINED]
- ❌ **finops/reporting/002-cost-anomaly-detection**
  - Q1 — PASS (75/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (74/100) [outcome: UNDETERMINED]
  - Q3 — PASS (75/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (74/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (68/100) [outcome: UNDETERMINED]

## 📉 Questions below threshold

- ❌ **finops/forecasting/001-monthly-cost-forecast**
  - Q3 — FAIL (74/100) [outcome: FAIL_INVALID]
- ❌ **finops/forecasting/002-cost-growth-trend**
  - Q1 — FAIL (73/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (65/100) [outcome: FAIL_INVALID]
- ❌ **finops/forecasting/005-budget-overrun**
  - Q1 — FAIL (72/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **finops/optimization/002-idle-resource-cleanup**
  - Q1 — FAIL (61/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **finops/optimization/003-optimization-roi-report**
  - Q3 — FAIL (74/100) [outcome: UNDETERMINED]
- ❌ **finops/optimization/004-optimization-roi**
  - Q1 — FAIL (71/100) [outcome: UNDETERMINED]
- ❌ **finops/optimization/005-incident-financial-cost**
  - Q1 — FAIL (73/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **finops/reporting/001-team-cost-chargeback**
  - Q1 — FAIL (69/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (61/100) [outcome: UNDETERMINED]
