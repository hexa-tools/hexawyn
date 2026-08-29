# gitops — 81.6/100

**15** scenarios (85 questions) · scenario pass rate 100% (15/15) · question pass rate 84% (71/85) · 2026-08-28 02:20

Questions: **71 PASS** / **14 FAIL** (of 85) · Average performance: 81.6/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| drift | ✅ | 2 | 10 | 11 |
| pipelines | ✅ | 5 | 25 | 30 |
| releases | ✅ | 5 | 23 | 28 |
| sync | ✅ | 3 | 13 | 16 |

## 📉 Questions below threshold

- ❌ **gitops/drift/001-full-drift-audit**
  - Q5 — FAIL (70/100) [outcome: PASS]
- ❌ **gitops/pipelines/001-pipeline-failed-rca**
  - Q2 — FAIL (65/100) [outcome: FAIL_INVALID]
- ❌ **gitops/pipelines/002-canary-vs-stable**
  - Q1 — FAIL (69/100) [outcome: PASS_ABSTENTION]
- ❌ **gitops/pipelines/003-ci-health-audit**
  - Q5 — FAIL (52/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **gitops/pipelines/005-pipeline-dag-trace**
  - Q1 — FAIL (69/100) [outcome: UNDETERMINED]
  - Q6 — FAIL (72/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **gitops/releases/001-helm-upgrade-planning**
  - Q1 — FAIL (62/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **gitops/releases/002-gitops-engine-health**
  - Q1 — FAIL (73/100) [outcome: PASS]
- ❌ **gitops/releases/004-outdated-helm-releases**
  - Q3 — FAIL (74/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (64/100) [outcome: UNDETERMINED]
- ❌ **gitops/releases/005-helm-values-diff**
  - Q1 — FAIL (71/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **gitops/sync/001-pre-release-sync-verification**
  - Q3 — FAIL (71/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (65/100) [outcome: PASS]
- ❌ **gitops/sync/003-app-out-of-sync**
  - Q5 — FAIL (74/100) [outcome: PASS]
