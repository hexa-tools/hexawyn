# networking — 81.2/100

**13** scenarios (70 questions) · scenario pass rate 85% (11/13) · question pass rate 77% (54/70) · 2026-08-27 08:32

Questions: **54 PASS** / **16 FAIL** (of 70) · Average performance: 81.2/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| exposure | ✅ | 3 | 12 | 16 |
| policies | ✅ | 6 | 31 | 33 |
| segmentation | ⚠️ | 2 | 11 | 21 |

## ❌ Failed scenarios

- ❌ **networking/segmentation/003-cross-namespace-traffic-map**
  - Q1 — FAIL (71/100) [outcome: UNDETERMINED]
  - Q2 — PASS (77/100) [outcome: PASS_ABSTENTION]
  - Q3 — FAIL (66/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (73/100) [outcome: PASS_ABSTENTION]
  - Q5 — PASS (78/100) [outcome: UNDETERMINED]
- ❌ **networking/segmentation/004-cross-cluster-incident**
  - Q1 — FAIL (72/100) [outcome: PASS_LIMITED]
  - Q2 — FAIL (68/100) [outcome: UNDETERMINED]
  - Q3 — FAIL (66/100) [outcome: FAIL_INVALID]
  - Q4 — FAIL (72/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (54/100) [outcome: FAIL_INVALID]
  - Q6 — FAIL (70/100) [outcome: UNDETERMINED]

## 📉 Questions below threshold

- ❌ **networking/exposure/001-external-exposure-audit**
  - Q1 — FAIL (74/100) [outcome: FAIL_INVALID]
  - Q2 — FAIL (66/100) [outcome: FAIL_INVALID]
- ❌ **networking/exposure/002-pending-public-services**
  - Q1 — FAIL (70/100) [outcome: FAIL_INVALID]
- ❌ **networking/exposure/003-db-exposed-nodeport**
  - Q1 — FAIL (70/100) [outcome: UNDETERMINED]
- ❌ **networking/policies/005-network-security-audit**
  - Q4 — FAIL (74/100) [outcome: UNDETERMINED]
- ❌ **networking/policies/006-verify-network-policies**
  - Q4 — FAIL (73/100) [outcome: PASS_ABSTENTION]
- ❌ **networking/segmentation/001-multi-cluster-segmentation**
  - Q5 — FAIL (67/100) [outcome: FAIL_NOT_DELIVERED]
