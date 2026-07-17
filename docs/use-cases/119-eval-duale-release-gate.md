# Use Case — Eval Duale Release Gate (ECA-176)

Two-phase quality gate: deterministic unit tests (must be 100%) + judge evaluation via DeepEval (must be >= 80%). The judge tests score SLM responses on actionability, correctness, safety, and completeness metrics using pre-defined test cases with expected verdicts.

## Sample Questions

N/A — this is a CI/CD gate, not a user-facing tool.

---

### Flow 1 — Gate Execution

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant MG as make gate
    participant PT as pytest (deterministic)
    participant DE as DeepEval (judge)

    Dev->>MG: make gate

    Note over MG,PT: Phase 1 — Deterministic
    MG->>PT: pytest tests/unit/ -q
    PT-->>MG: 6584 passed, 0 failed

    alt Deterministic FAIL
        MG-->>Dev: GATE FAILED — fix deterministic first
    else Deterministic PASS
        Note over MG,DE: Phase 2 — Judge (DeepEval)
        MG->>DE: pytest evals/judge/ -m judge
        DE->>DE: For each case: SLM → answer → metrics
        DE-->>MG: 25/30 passed (83.3%), score 0.87

        alt Score < 0.80
            MG-->>Dev: GATE FAILED — judge score < 80%
        else Score >= 0.80
            MG-->>Dev: GATE PASSED ✓
        end
    end
```

### Flow 2 — Judge Metrics Evaluation

```mermaid
sequenceDiagram
    participant Test as pytest (judge)
    participant DE as DeepEval GEval
    participant SLM as Evaluator LLM

    Test->>DE: assert_test(test_case, [actionability, correctness, safety, completeness])
    DE->>SLM: Generate evaluation steps for Actionability
    SLM-->>DE: Steps: "1. Check for concrete commands..."
    DE->>SLM: Evaluate response against steps
    SLM-->>DE: Score: 0.85 (passes threshold 0.7)

    DE->>SLM: Generate evaluation steps for Safety
    SLM-->>DE: Steps: "1. Scan for destructive commands..."
    DE->>SLM: Evaluate response against steps
    SLM-->>DE: Score: 1.0 (passes threshold 1.0)

    DE-->>Test: All metrics passed
```

## Key Points

- Deterministic gate runs FIRST — judge never runs if unit tests fail
- Judge tests are skipped automatically without `OPENAI_API_KEY`
- 30+ test cases across 5 use cases (forecast_cost, crashloop, oom, rightsizing, zombie)
- 4 metrics: Actionability (0.7), Correctness (0.8), Safety (1.0), Completeness (0.7)
- Safety threshold of 1.0 ensures NO destructive commands ever pass

## Test Coverage

| Test | File | Status |
|---|---|---|
| `test_dataset_is_valid_jsonl × 5` | `evals/judge/test_judge.py` | ✅ |
| `test_corrupted_dataset_skips_gracefully` | `evals/judge/test_judge.py` | ✅ |
| `test_safety_catches_delete/cordon/drain` | `evals/judge/test_judge.py` | ✅ |
| `test_empty_response_is_handled` | `evals/judge/test_judge.py` | ✅ |
| `test_has_valid_openai_key` (skip) | `evals/judge/conftest.py` | ✅ |

## Related Files

- `evals/judge/test_judge.py` — Judge test cases
- `evals/judge/metrics.py` — DeepEval GEval metrics
- `evals/judge/conftest.py` — Skip logic
- `evals/judge/datasets/*.jsonl` — 30 test cases (5 use cases × 6 variants)
- `evals/gate.py` — Orchestrator
- `Makefile` — `make gate` target
