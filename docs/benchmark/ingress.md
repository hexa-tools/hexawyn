# ingress — 81.0/100

**5** scenarios (25 questions) · scenario pass rate 80% (4/5) · question pass rate 80% (20/25) · 2026-08-24 02:59

Questions: **20 PASS** / **5 FAIL** (of 25) · Average performance: 81.0/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| controllers | ✅ | 2 | 8 | 10 |
| routing | ⚠️ | 1 | 7 | 10 |
| tls | ✅ | 1 | 5 | 5 |

## ❌ Failed scenarios

- ❌ **ingress/routing/002-ingress-500-investigation**
  - Q1 — PASS (79/100) [outcome: PASS_ABSTENTION]
  - Q2 — FAIL (68/100) [outcome: PASS]
  - Q3 — PASS (81/100) [outcome: PASS_LIMITED]
  - Q4 — FAIL (73/100) [outcome: PASS_ABSTENTION]
  - Q5 — FAIL (74/100) [outcome: PASS_LIMITED]

## 📉 Questions below threshold

- ❌ **ingress/controllers/001-ingress-controller-health**
  - Q2 — FAIL (69/100) [outcome: PASS]
  - Q4 — FAIL (70/100) [outcome: PASS_ABSTENTION]
