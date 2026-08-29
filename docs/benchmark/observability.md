# observability — 79.7/100

**18** scenarios (94 questions) · scenario pass rate 83% (15/18) · question pass rate 78% (73/94) · 2026-08-28 22:16

Questions: **73 PASS** / **21 FAIL** (of 94) · Average performance: 79.7/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| data | ⚠️ | 1 | 6 | 9 |
| dependencies | ⚠️ | 2 | 12 | 16 |
| latency | ⚠️ | 3 | 17 | 21 |
| metrics | ✅ | 5 | 21 | 27 |
| traces | ✅ | 4 | 17 | 21 |

## ❌ Failed scenarios

- ❌ **observability/data/001-query-kubearchive-history**
  - Q1 — FAIL (69/100) [outcome: UNDETERMINED]
  - Q2 — PASS (82/100) [outcome: UNDETERMINED]
  - Q3 — FAIL (64/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (74/100) [outcome: UNDETERMINED]
  - Q5 — PASS (84/100) [outcome: UNDETERMINED]
- ❌ **observability/dependencies/002-cross-namespace-deps**
  - Q1 — FAIL (66/100) [outcome: UNDETERMINED]
  - Q2 — PASS (84/100) [outcome: UNDETERMINED]
  - Q3 — PASS (78/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (73/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (74/100) [outcome: PASS_ABSTENTION]
- ❌ **observability/latency/003-slo-latency-budget**
  - Q1 — FAIL (68/100) [outcome: FAIL_INVALID]
  - Q2 — PASS (86/100) [outcome: UNDETERMINED]
  - Q3 — FAIL (74/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (71/100) [outcome: UNDETERMINED]
  - Q5 — PASS (75/100) [outcome: UNDETERMINED]

## 📉 Questions below threshold

- ❌ **observability/dependencies/003-dependency-mapping**
  - Q1 — FAIL (68/100) [outcome: UNDETERMINED]
- ❌ **observability/latency/002-multi-service-latency**
  - Q3 — FAIL (74/100) [outcome: FAIL_INVALID]
- ❌ **observability/metrics/002-cpu-memory-anomaly**
  - Q3 — FAIL (66/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (50/100) [outcome: FAIL_INVALID]
- ❌ **observability/metrics/003-slo-error-budget-burn**
  - Q5 — FAIL (68/100) [outcome: UNDETERMINED]
- ❌ **observability/metrics/004-metric-correlation**
  - Q1 — FAIL (64/100) [outcome: UNDETERMINED]
- ❌ **observability/metrics/005-etcd-instability**
  - Q3 — FAIL (69/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (59/100) [outcome: FAIL_INVALID]
- ❌ **observability/traces/001-slowest-traces-hour**
  - Q4 — FAIL (68/100) [outcome: UNDETERMINED]
- ❌ **observability/traces/003-redundant-calls**
  - Q1 — FAIL (74/100) [outcome: PASS]
  - Q4 — FAIL (74/100) [outcome: PASS]
- ❌ **observability/traces/004-slowest-traces**
  - Q1 — FAIL (74/100) [outcome: UNDETERMINED]
