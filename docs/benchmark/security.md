# security — 82.3/100

**26** scenarios (138 questions) · scenario pass rate 92% (24/26) · question pass rate 83% (115/138) · 2026-08-28 23:22

Questions: **115 PASS** / **23 FAIL** (of 138) · Average performance: 82.3/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| drift | ⚠️ | 3 | 17 | 21 |
| policy | ✅ | 4 | 16 | 21 |
| posture | ✅ | 6 | 28 | 33 |
| rbac | ✅ | 4 | 19 | 21 |
| secrets | ✅ | 4 | 20 | 21 |
| vulnerabilities | ⚠️ | 3 | 15 | 21 |

## ❌ Failed scenarios

- ❌ **security/drift/002-container-image-drift**
  - Q1 — FAIL (64/100) [outcome: PASS_ABSTENTION]
  - Q2 — FAIL (72/100) [outcome: PASS_ABSTENTION]
  - Q3 — PASS (78/100) [outcome: PASS_ABSTENTION]
  - Q4 — PASS (75/100) [outcome: FAIL_NOT_DELIVERED]
  - Q5 — FAIL (68/100) [outcome: UNDETERMINED]
- ❌ **security/vulnerabilities/002-eol-base-images**
  - Q1 — FAIL (74/100) [outcome: PASS_ABSTENTION]
  - Q2 — FAIL (67/100) [outcome: UNDETERMINED]
  - Q3 — PASS (77/100) [outcome: PASS_ABSTENTION]
  - Q4 — FAIL (73/100) [outcome: PASS_ABSTENTION]
  - Q5 — FAIL (72/100) [outcome: UNDETERMINED]

## 📉 Questions below threshold

- ❌ **security/drift/001-gitops-config-drift**
  - Q4 — FAIL (62/100) [outcome: FAIL_INVALID]
- ❌ **security/policy/001-detect-policy-engine**
  - Q1 — FAIL (72/100) [outcome: UNDETERMINED]
- ❌ **security/policy/002-policy-violations-audit**
  - Q1 — FAIL (72/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **security/policy/003-policy-review-enforce**
  - Q4 — FAIL (69/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **security/policy/004-policy-violations**
  - Q1 — FAIL (66/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (74/100) [outcome: UNDETERMINED]
- ❌ **security/posture/001-security-posture-board**
  - Q3 — FAIL (65/100) [outcome: FAIL_INVALID]
- ❌ **security/posture/004-security-posture-report**
  - Q4 — FAIL (72/100) [outcome: PASS_LIMITED]
- ❌ **security/posture/005-admin-endpoint-audit**
  - Q2 — FAIL (71/100) [outcome: FAIL_INVALID]
  - Q4 — FAIL (74/100) [outcome: FAIL_INVALID]
- ❌ **security/posture/006-full-compliance-audit**
  - Q1 — FAIL (73/100) [outcome: PASS_ABSTENTION]
- ❌ **security/rbac/001-cluster-admin-audit**
  - Q5 — FAIL (68/100) [outcome: UNDETERMINED]
- ❌ **security/rbac/003-least-privilege-review**
  - Q2 — FAIL (71/100) [outcome: UNDETERMINED]
- ❌ **security/secrets/001-expired-rotation**
  - Q3 — FAIL (73/100) [outcome: FAIL_INVALID]
- ❌ **security/vulnerabilities/004-image-vulnerability-scan**
  - Q1 — FAIL (74/100) [outcome: PASS_ABSTENTION]
  - Q4 — FAIL (70/100) [outcome: UNDETERMINED]
