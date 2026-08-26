# cert_manager — 81.6/100

**11** scenarios (60 questions) · scenario pass rate 91% (10/11) · question pass rate 80% (48/60) · 2026-08-26 03:05

Questions: **48 PASS** / **12 FAIL** (of 60) · Average performance: 81.6/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| certificates | ⚠️ | 4 | 19 | 28 |
| challenges | ✅ | 3 | 14 | 16 |
| issuers | ✅ | 3 | 15 | 16 |

## ❌ Failed scenarios

- ❌ **cert_manager/certificates/001-expiry-forecast**
  - Q1 — PASS (80/100) [outcome: PASS_LIMITED]
  - Q2 — FAIL (69/100) [outcome: PASS_LIMITED]
  - Q3 — FAIL (74/100) [outcome: PASS_ABSTENTION]
  - Q4 — PASS (90/100) [outcome: PASS_LIMITED]
  - Q5 — FAIL (68/100) [outcome: FAIL_NOT_DELIVERED]

## 📉 Questions below threshold

- ❌ **cert_manager/certificates/002-certificate-readiness**
  - Q2 — FAIL (73/100) [outcome: PASS_LIMITED]
  - Q5 — FAIL (68/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cert_manager/certificates/003-expiry-check**
  - Q2 — FAIL (68/100) [outcome: PASS_LIMITED]
- ❌ **cert_manager/certificates/004-cert-health-audit**
  - Q1 — FAIL (74/100) [outcome: PASS]
  - Q3 — FAIL (70/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cert_manager/certificates/005-renewal-failure**
  - Q4 — FAIL (72/100) [outcome: PASS_ABSTENTION]
- ❌ **cert_manager/challenges/001-pending-challenges**
  - Q1 — FAIL (74/100) [outcome: PASS_LIMITED]
- ❌ **cert_manager/challenges/002-dns-challenge-propagation**
  - Q1 — FAIL (53/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cert_manager/issuers/003-issuer-health-check**
  - Q1 — FAIL (74/100) [outcome: FAIL_NOT_DELIVERED]
