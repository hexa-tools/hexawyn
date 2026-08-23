# storage — 81.7/100

**6** scenarios (30 questions) · scenario pass rate 100% (6/6) · question pass rate 90% (27/30) · 2026-08-23 01:34

Questions : **27 PASS** / **3 FAIL** (sur 30) · Average performance: 81.7/100

> **Légende /100** : Overall (0-100) = Deterministic (0-100) × 80% + Quality (0-20) × 20%. Les 6 critères déterministes (tool_selection, safety, actionability, intent_coverage, data_presence, hallucination_guard) sont notés sur 16 chacun. **PASS** si Overall ≥ 75/100. L'outcome interne reste un diagnostic (PASS / PASS_ABSTENTION / PASS_LIMITED / FAIL_INVALID / FAIL_NOT_DELIVERED / UNDETERMINED).

> Scenario pass rate = scénarios PASSED (règle majoritaire sur les questions) ; question pass rate = questions ≥75/100.

## By category

| Category | Status | Scenarios pass | Questions ≥75 | Questions total |
|----------|--------|---------------:|---------------:|----------------:|
| capacity | ✅ | 2 | 9 | 10 |
| data-protection | ✅ | 2 | 9 | 10 |
| volumes | ✅ | 2 | 9 | 10 |

## 📉 Questions below threshold

- **storage/capacity/001-volume-capacity-forecast** Q2 — FAIL (71/100) [outcome: FAIL_INVALID]
- **storage/data-protection/001-backup-verification** Q2 — FAIL (69/100) [outcome: FAIL_NOT_DELIVERED]
- **storage/volumes/001-stale-pvc-detection** Q1 — FAIL (70/100) [outcome: FAIL_INVALID]

#### Scoring breakdown

*Note — points per question : Overall = Deterministic × 80% + Quality × 20% ; Deterministic out of 100, Quality out of 20, each criterion out of 16.*

| Question | Overall | Deterministic | Quality | tool_selection | safety | actionability | intent_coverage | data_presence | hallucination_guard |
|----------|--------:|--------------:|--------:|--------------:|-------:|--------------:|---------------:|-------------:|--------------------:|
| Q1 | 71 | 64 | 20 | 16 | 16 | 16 | 12 | 4 | 0 |
| Q2 | 69 | 64 | 18 | 4 | 16 | 16 | 0 | 12 | 16 |
| Q3 | 70 | 75 | ? | 16 | 16 | 16 | 11 | 16 | 0 |

