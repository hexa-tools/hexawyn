# workloads — 79.2/100

**8** scenarios (40 questions) · scenario pass rate 88% (7/8) · question pass rate 72% (29/40) · 2026-08-24 23:43

Questions: **29 PASS** / **11 FAIL** (of 40) · Average performance: 79.2/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| deployments | ✅ | 3 | 11 | 15 |
| health | ⚠️ | 2 | 10 | 15 |
| scaling | ✅ | 2 | 8 | 10 |

## ❌ Failed scenarios

- ❌ **workloads/health/002-readiness-liveness-gap**
  - Q1 — FAIL (64/100) [outcome: PASS_LIMITED]
  - Q2 — FAIL (70/100) [outcome: PASS]
  - Q3 — FAIL (68/100) [outcome: PASS]
  - Q4 — PASS (81/100) [outcome: PASS]
  - Q5 — PASS (77/100) [outcome: PASS_ABSTENTION]

## 📉 Questions below threshold

- ❌ **workloads/deployments/001-rolling-update-health**
  - Q1 — FAIL (53/100) [outcome: UNDETERMINED]
- ❌ **workloads/deployments/002-deployment-diff-staging-prod**
  - Q1 — FAIL (63/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (62/100) [outcome: FAIL_INVALID]
- ❌ **workloads/deployments/003-deployment-rollout-strategy**
  - Q1 — FAIL (53/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **workloads/health/001-pod-disruption-budget-audit**
  - Q1 — FAIL (65/100) [outcome: PASS]
- ❌ **workloads/health/003-zombie-deployment-cleanup**
  - Q3 — FAIL (73/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **workloads/scaling/001-hpa-health-check**
  - Q1 — FAIL (64/100) [outcome: PASS]
- ❌ **workloads/scaling/002-statefulset-daemonset-inventory**
  - Q1 — FAIL (67/100) [outcome: PASS_ABSTENTION]
