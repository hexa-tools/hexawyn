# networking — 79.0/100

**13** scenarios (70 questions) · scenario pass rate 85% (11/13) · question pass rate 67% (47/70) · 2026-08-27 03:04

Questions: **47 PASS** / **23 FAIL** (of 70) · Average performance: 79.0/100

> **Legend /100**: Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. The 6 deterministic criteria (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) are each scored /16. **PASS** if Overall ≥ 75/100. Internal outcome remains a diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scenarios PASSED (majority rule on questions); question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| exposure | ✅ | 3 | 12 | 16 |
| policies | ✅ | 6 | 27 | 33 |
| segmentation | ⚠️ | 2 | 8 | 21 |

## ❌ Failed scenarios

- ❌ **networking/segmentation/003-cross-namespace-traffic-map**
  - Q1 — FAIL (74/100) [outcome: PASS_ABSTENTION]
  - Q2 — PASS (78/100) [outcome: UNDETERMINED]
  - Q3 — FAIL (69/100) [outcome: UNDETERMINED]
  - Q4 — FAIL (70/100) [outcome: UNDETERMINED]
  - Q5 — FAIL (62/100) [outcome: UNDETERMINED]
- ❌ **networking/segmentation/004-cross-cluster-incident**
  - Q1 — FAIL (70/100) [outcome: PASS_LIMITED]
  - Q2 — FAIL (64/100) [outcome: FAIL_INVALID]
  - Q3 — FAIL (66/100) [outcome: FAIL_INVALID]
  - Q4 — FAIL (58/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (60/100) [outcome: FAIL_INVALID]
  - Q6 — FAIL (70/100) [outcome: UNDETERMINED]

## 📉 Questions below threshold

- ❌ **networking/exposure/001-external-exposure-audit**
  - Q4 — FAIL (69/100) [outcome: FAIL_INVALID]
- ❌ **networking/exposure/002-pending-public-services**
  - Q5 — FAIL (70/100) [outcome: UNDETERMINED]
- ❌ **networking/exposure/003-db-exposed-nodeport**
  - Q1 — FAIL (58/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (69/100) [outcome: FAIL_INVALID]
- ❌ **networking/policies/002-segment-namespaces**
  - Q1 — FAIL (66/100) [outcome: FAIL_INVALID]
- ❌ **networking/policies/003-egress-restrictions-audit**
  - Q2 — FAIL (71/100) [outcome: FAIL_INVALID]
- ❌ **networking/policies/004-no-network-policies**
  - Q2 — FAIL (69/100) [outcome: FAIL_INVALID]
  - Q4 — FAIL (72/100) [outcome: FAIL_INVALID]
- ❌ **networking/policies/005-network-security-audit**
  - Q2 — FAIL (70/100) [outcome: FAIL_INVALID]
- ❌ **networking/policies/006-verify-network-policies**
  - Q2 — FAIL (66/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **networking/segmentation/001-multi-cluster-segmentation**
  - Q2 — FAIL (71/100) [outcome: FAIL_INVALID]
  - Q5 — FAIL (70/100) [outcome: FAIL_NOT_DELIVERED]
- ❌ **networking/segmentation/002-calico-cilium-audit**
  - Q1 — FAIL (66/100) [outcome: FAIL_NOT_DELIVERED]
