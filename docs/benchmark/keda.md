# keda — 81.3/100

**10** scenarios (55 questions) · scenario pass rate 100% (10/10) · question pass rate 87% (48/55) · 2026-08-25 06:30

Questions: **48 PASS** / **7 FAIL** (of 55) · Average performance: 81.3/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| audit | ✅ | 2 | 10 | 12 |
| scaledjobs | ✅ | 2 | 9 | 11 |
| scaledobjects | ✅ | 3 | 13 | 16 |
| triggers | ✅ | 3 | 16 | 16 |

## 📉 Questions below threshold

- ❌ **keda/audit/001-keda-installed**
  - Q6 — FAIL (69/100) [outcome: FAIL_INVALID]
- ❌ **keda/audit/002-full-keda-audit**
  - Q1 — FAIL (66/100) [outcome: UNDETERMINED]
- ❌ **keda/scaledjobs/001-scaledjob-execution-audit**
  - Q1 — FAIL (53/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (74/100) [outcome: PASS]
- ❌ **keda/scaledobjects/001-scaledobject-health-audit**
  - Q1 — FAIL (74/100) [outcome: PASS]
- ❌ **keda/scaledobjects/002-scale-to-zero-verification**
  - Q1 — FAIL (57/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — FAIL (72/100) [outcome: FAIL_NOT_DELIVERED]
