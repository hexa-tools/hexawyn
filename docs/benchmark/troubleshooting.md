# troubleshooting — 83.1/100

**27** scenarios (162 questions) · scenario pass rate 96% (26/27) · question pass rate 79% (128/162) · 2026-08-29 07:01

Questions: **128 PASS** / **34 FAIL** (of 162) · Average performance: 83.1/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| custom_tools | ✅ | 3 | 16 | 18 |
| diagnostics | ⚠️ | 5 | 22 | 36 |
| pods | ✅ | 7 | 35 | 42 |
| reliability | ✅ | 5 | 23 | 30 |
| resources | ✅ | 6 | 32 | 36 |

## ❌ Failed scenarios

- ❌ **troubleshooting/diagnostics/002-payment-worker-crashloop**
  - Q1 — FAIL (70/100) [outcome: FAIL_NOT_DELIVERED]
  - Q2 — PASS (86/100) [outcome: PASS]
  - Q3 — FAIL (72/100) [outcome: PASS_ABSTENTION]
  - Q4 — FAIL (73/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (71/100) [outcome: FAIL_NOT_DELIVERED]
  - Q6 — PASS (100/100) [outcome: UNDETERMINED]

## 📉 Questions below threshold

- ❌ **troubleshooting/custom_tools/001-list-registered-tools**
  - Q4 — FAIL (71/100) [outcome: PASS_LIMITED]
- ❌ **troubleshooting/custom_tools/003-run-all-security-scanners**
  - Q1 — FAIL (65/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **troubleshooting/diagnostics/001-staging-health-check**
  - Q4 — FAIL (72/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (73/100) [outcome: UNDETERMINED]
- ❌ **troubleshooting/diagnostics/003-data-pipeline-oom**
  - Q2 — FAIL (70/100) [outcome: FAIL_INVALID]
  - Q3 — FAIL (70/100) [outcome: PASS_ABSTENTION]
  - Q4 — FAIL (70/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **troubleshooting/diagnostics/004-checkout-multi-symptom**
  - Q1 — FAIL (59/100) [outcome: FAIL_INVALID]
  - Q3 — FAIL (70/100) [outcome: PASS]
- ❌ **troubleshooting/diagnostics/005-cross-cluster-comparison**
  - Q2 — FAIL (66/100) [outcome: PASS_ABSTENTION]
- ❌ **troubleshooting/diagnostics/006-blind-investigation**
  - Q1 — FAIL (70/100) [outcome: FAIL_NOT_DELIVERED]
  - Q3 — FAIL (67/100) [outcome: PASS]
- ❌ **troubleshooting/pods/002-pod-logs-errors**
  - Q1 — FAIL (63/100) [outcome: PASS_LIMITED]
- ❌ **troubleshooting/pods/003-missing-health-probes**
  - Q2 — FAIL (72/100) [outcome: PASS]
  - Q3 — FAIL (72/100) [outcome: PASS]
- ❌ **troubleshooting/pods/005-privileged-pods-audit**
  - Q1 — FAIL (69/100) [outcome: PASS]
  - Q3 — FAIL (69/100) [outcome: FAIL_INVALID]
- ❌ **troubleshooting/pods/006-log-correlation-multi-pod**
  - Q1 — FAIL (72/100) [outcome: PASS_LIMITED]
  - Q3 — FAIL (72/100) [outcome: PASS]
- ❌ **troubleshooting/reliability/001-weekly-reliability-report**
  - Q4 — FAIL (67/100) [outcome: FAIL_NOT_DELIVERED]
  - Q6 — FAIL (70/100) [outcome: FAIL_INVALID]
- ❌ **troubleshooting/reliability/003-quarterly-sla-board**
  - Q1 — FAIL (65/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (66/100) [outcome: PASS]
  - Q6 — FAIL (47/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **troubleshooting/reliability/005-incident-rca-report**
  - Q1 — FAIL (64/100) [outcome: PASS_ABSTENTION]
  - Q4 — FAIL (65/100) [outcome: PASS]
- ❌ **troubleshooting/resources/003-oomkilled-investigation**
  - Q1 — FAIL (69/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (72/100) [outcome: UNDETERMINED]
  - Q6 — FAIL (73/100) [outcome: FAIL_INVALID]
- ❌ **troubleshooting/resources/006-right-sizing-campaign**
  - Q1 — FAIL (73/100) [outcome: UNDETERMINED]
