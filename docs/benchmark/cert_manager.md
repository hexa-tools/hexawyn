# cert_manager — 75.9/100

**8** scenarios (14 questions) · scenario pass rate 75% (6/8) · question pass rate 64% (9/14) · 2026-08-26 02:35

Questions: **9 PASS** / **5 FAIL** (of 14) · Average performance: 75.9/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| certificates | ⚠️ | 4 | 4 | 8 |
| challenges | ⚠️ | 2 | 5 | 6 |

## ❌ Failed scenarios

- ❌ **cert_manager/certificates/001-expiry-forecast**
  - Q1 — FAIL (70/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cert_manager/challenges/002-dns-challenge-propagation**
  - Q1 — FAIL (51/100) [outcome: FAIL_NOT_DELIVERED]

## 📉 Questions below threshold

- ❌ **cert_manager/certificates/002-certificate-readiness**
  - Q2 — FAIL (66/100) [outcome: PASS_LIMITED]
- ❌ **cert_manager/certificates/003-expiry-check**
  - Q1 — FAIL (73/100) [outcome: PASS_LIMITED]
- ❌ **cert_manager/certificates/005-renewal-failure**
  - Q1 — FAIL (60/100) [outcome: FAIL_INVALID]
