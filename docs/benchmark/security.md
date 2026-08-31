# security — 83.3/100

**26** scenarios (138 questions) · scenario pass rate 100% (26/26) · question pass rate 91% (125/138) · 2026-08-29 02:08

Questions: **125 PASS** / **13 FAIL** (of 138) · Average performance: 83.3/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| drift | ✅ | 4 | 18 | 21 |
| policy | ✅ | 4 | 18 | 21 |
| posture | ✅ | 6 | 32 | 33 |
| rbac | ✅ | 4 | 19 | 21 |
| secrets | ✅ | 4 | 21 | 21 |
| vulnerabilities | ✅ | 4 | 17 | 21 |

## 📉 Questions below threshold

- ❌ **security/drift/002-container-image-drift**
  - Q1 — FAIL (71/100) [outcome: PASS_ABSTENTION]
  - Q5 — FAIL (67/100) [outcome: UNDETERMINED]
- ❌ **security/drift/004-configuration-drift**
  - Q4 — FAIL (74/100) [outcome: UNDETERMINED]
- ❌ **security/policy/001-detect-policy-engine**
  - Q3 — FAIL (72/100) [outcome: UNDETERMINED]
- ❌ **security/policy/002-policy-violations-audit**
  - Q1 — FAIL (68/100) [outcome: FAIL_INVALID]
- ❌ **security/policy/004-policy-violations**
  - Q1 — FAIL (72/100) [outcome: UNDETERMINED]
- ❌ **security/posture/003-admin-access-audit**
  - Q5 — FAIL (65/100) [outcome: FAIL_INVALID]
- ❌ **security/rbac/002-unused-permissions**
  - Q4 — FAIL (70/100) [outcome: FAIL_INVALID]
- ❌ **security/rbac/004-rbac-audit**
  - Q5 — FAIL (74/100) [outcome: PASS_ABSTENTION]
- ❌ **security/vulnerabilities/001-cve-scan**
  - Q5 — FAIL (73/100) [outcome: PASS_ABSTENTION]
- ❌ **security/vulnerabilities/002-eol-base-images**
  - Q1 — FAIL (72/100) [outcome: PASS_ABSTENTION]
  - Q5 — FAIL (70/100) [outcome: UNDETERMINED]
- ❌ **security/vulnerabilities/004-image-vulnerability-scan**
  - Q1 — FAIL (73/100) [outcome: UNDETERMINED]
