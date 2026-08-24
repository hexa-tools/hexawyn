# governance — 81.9/100

**6** scenarios (30 questions) · scenario pass rate 83% (5/6) · question pass rate 70% (21/30) · 2026-08-24 03:27

Questions: **21 PASS** / **9 FAIL** (of 30) · Average performance: 81.9/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| audit | ⚠️ | 1 | 5 | 10 |
| compliance | ✅ | 2 | 8 | 10 |
| policy | ✅ | 2 | 8 | 10 |

## ❌ Failed scenarios

- ❌ **governance/audit/001-cis-benchmark-audit**
  - Q1 — FAIL (61/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — PASS (87/100) [outcome: UNDETERMINED]
  - Q3 — FAIL (68/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (73/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (73/100) [outcome: UNDETERMINED]

## 📉 Questions below threshold

- ❌ **governance/audit/002-change-management-audit**
  - Q3 — FAIL (70/100) [outcome: FAIL_INVALID]
- ❌ **governance/compliance/001-full-compliance-audit**
  - Q1 — FAIL (72/100) [outcome: PASS_LIMITED]
- ❌ **governance/compliance/002-pci-dss-checklist**
  - Q1 — FAIL (73/100) [outcome: PASS_LIMITED]
- ❌ **governance/policy/001-policy-enforcement-gap**
  - Q1 — FAIL (74/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **governance/policy/002-policy-as-code-review**
  - Q5 — FAIL (67/100) [outcome: FAIL_INVALID]
