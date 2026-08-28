# observability — 79.7/100

**18** scenarios (94 questions) · scenario pass rate 89% (16/18) · question pass rate 80% (75/94) · 2026-08-28 09:20

Questions: **75 PASS** / **19 FAIL** (of 94) · Average performance: 79.7/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| data | ⚠️ | 1 | 6 | 9 |
| dependencies | ⚠️ | 2 | 12 | 16 |
| latency | ✅ | 4 | 16 | 21 |
| metrics | ✅ | 5 | 25 | 27 |
| traces | ✅ | 4 | 16 | 21 |

## ❌ Failed scenarios

- ❌ **observability/data/001-query-kubearchive-history**
  - Q1 — FAIL (72/100) [outcome: UNDETERMINED]
  - Q2 — PASS (83/100) [outcome: FAIL_NOT_DELIVERED]
  - Q3 — FAIL (69/100) [outcome: FAIL_NOT_DELIVERED]
  - Q4 — FAIL (74/100) [outcome: UNDETERMINED]
  - Q5 — PASS (86/100) [outcome: UNDETERMINED]
- ❌ **observability/dependencies/002-cross-namespace-deps**
  - Q1 — FAIL (60/100) [outcome: FAIL_INVALID]
  - Q2 — PASS (75/100) [outcome: UNDETERMINED]
  - Q3 — PASS (78/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (73/100) [outcome: PASS_ABSTENTION]
  - Q5 — FAIL (72/100) [outcome: PASS_ABSTENTION]

## 📉 Questions below threshold

- ❌ **observability/dependencies/003-dependency-mapping**
  - Q1 — FAIL (74/100) [outcome: UNDETERMINED]
- ❌ **observability/latency/001-payment-p99-spike**
  - Q3 — FAIL (63/100) [outcome: UNDETERMINED]
- ❌ **observability/latency/003-slo-latency-budget**
  - Q4 — FAIL (71/100) [outcome: UNDETERMINED]
- ❌ **observability/latency/004-p99-latency**
  - Q1 — FAIL (72/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (71/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (74/100) [outcome: UNDETERMINED]
- ❌ **observability/metrics/001-gateway-error-correlation**
  - Q5 — FAIL (66/100) [outcome: UNDETERMINED]
- ❌ **observability/metrics/004-metric-correlation**
  - Q1 — FAIL (71/100) [outcome: UNDETERMINED]
- ❌ **observability/traces/002-span-bottleneck-chain**
  - Q4 — FAIL (73/100) [outcome: UNDETERMINED]
- ❌ **observability/traces/003-redundant-calls**
  - Q3 — FAIL (74/100) [outcome: PASS]
  - Q4 — FAIL (74/100) [outcome: PASS]
- ❌ **observability/traces/004-slowest-traces**
  - Q1 — FAIL (70/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (72/100) [outcome: UNDETERMINED]
