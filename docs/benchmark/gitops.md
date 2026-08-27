# gitops — 79.3/100

**15** scenarios (85 questions) · scenario pass rate 80% (12/15) · question pass rate 73% (62/85) · 2026-08-27 10:04

Questions: **62 PASS** / **23 FAIL** (of 85) · Average performance: 79.3/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| drift | ✅ | 2 | 10 | 11 |
| pipelines | ⚠️ | 3 | 18 | 30 |
| releases | ⚠️ | 4 | 20 | 28 |
| sync | ✅ | 3 | 14 | 16 |

## ❌ Failed scenarios

- ❌ **gitops/pipelines/003-ci-health-audit**
  - Q1 — FAIL (72/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — PASS (81/100) [outcome: FAIL_NOT_DELIVERED]
  - Q3 — FAIL (71/100) [outcome: FAIL_NOT_DELIVERED]
  - Q4 — FAIL (69/100) [outcome: UNDETERMINED]
  - Q5 — PASS (76/100) [outcome: FAIL_NOT_DELIVERED]
  - Q6 — FAIL (70/100) [outcome: UNDETERMINED]
- ❌ **gitops/pipelines/004-version-regression**
  - Q1 — FAIL (68/100) [outcome: PASS]
  - Q2 — FAIL (62/100) [outcome: PASS]
  - Q3 — FAIL (69/100) [outcome: PASS]
  - Q4 — FAIL (69/100) [outcome: PASS]
  - Q5 — FAIL (63/100) [outcome: FAIL_NOT_DELIVERED]
  - Q6 — PASS (100/100) [outcome: UNDETERMINED]
- ❌ **gitops/releases/002-gitops-engine-health**
  - Q1 — FAIL (73/100) [outcome: PASS]
  - Q2 — PASS (86/100) [outcome: PASS]
  - Q3 — PASS (81/100) [outcome: PASS]
  - Q4 — FAIL (70/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (74/100) [outcome: PASS]

## 📉 Questions below threshold

- ❌ **gitops/drift/001-full-drift-audit**
  - Q1 — FAIL (70/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **gitops/pipelines/002-canary-vs-stable**
  - Q1 — FAIL (73/100) [outcome: UNDETERMINED]
- ❌ **gitops/pipelines/005-pipeline-dag-trace**
  - Q1 — FAIL (66/100) [outcome: UNDETERMINED]
  - Q6 — FAIL (72/100) [outcome: PASS_LIMITED]
- ❌ **gitops/releases/001-helm-upgrade-planning**
  - Q2 — FAIL (66/100) [outcome: FAIL_INVALID]
  - Q4 — FAIL (66/100) [outcome: UNDETERMINED]
- ❌ **gitops/releases/003-gitops-health-check**
  - Q4 — FAIL (65/100) [outcome: FAIL_INVALID]
  - Q6 — FAIL (72/100) [outcome: UNDETERMINED]
- ❌ **gitops/releases/005-helm-values-diff**
  - Q3 — FAIL (62/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **gitops/sync/001-pre-release-sync-verification**
  - Q2 — FAIL (67/100) [outcome: FAIL_INVALID]
- ❌ **gitops/sync/002-git-source-connectivity**
  - Q4 — FAIL (70/100) [outcome: FAIL_INVALID]
