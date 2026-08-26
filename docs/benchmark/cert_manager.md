# cert_manager — 80.9/100

**11** scenarios (60 questions) · scenario pass rate 100% (11/11) · question pass rate 77% (46/60) · 2026-08-25 22:46

Questions: **46 PASS** / **14 FAIL** (of 60) · Average performance: 80.9/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| certificates | ✅ | 5 | 20 | 28 |
| challenges | ✅ | 3 | 10 | 16 |
| issuers | ✅ | 3 | 16 | 16 |

## 📉 Questions below threshold

- ❌ **cert_manager/certificates/001-expiry-forecast**
  - Q2 — FAIL (71/100) [outcome: PASS_LIMITED]
- ❌ **cert_manager/certificates/002-certificate-readiness**
  - Q1 — FAIL (68/100) [outcome: PASS_ABSTENTION]
  - Q2 — FAIL (72/100) [outcome: PASS_LIMITED]
- ❌ **cert_manager/certificates/003-expiry-check**
  - Q2 — FAIL (66/100) [outcome: PASS_LIMITED]
  - Q5 — FAIL (68/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cert_manager/certificates/004-cert-health-audit**
  - Q5 — FAIL (68/100) [outcome: PASS]
- ❌ **cert_manager/certificates/005-renewal-failure**
  - Q4 — FAIL (62/100) [outcome: PASS_ABSTENTION]
  - Q5 — FAIL (68/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cert_manager/challenges/001-pending-challenges**
  - Q1 — FAIL (59/100) [outcome: FAIL_NOT_DELIVERED]
  - Q4 — FAIL (73/100) [outcome: FAIL_INVALID]
- ❌ **cert_manager/challenges/002-dns-challenge-propagation**
  - Q1 — FAIL (51/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **cert_manager/challenges/003-acme-challenge-stuck**
  - Q1 — FAIL (65/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (73/100) [outcome: FAIL_INVALID]
  - Q6 — FAIL (62/100) [outcome: FAIL_NOT_DELIVERED]
