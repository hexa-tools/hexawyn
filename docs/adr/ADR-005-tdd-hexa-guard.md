# ADR-005 — Strict TDD + enforced `hexa_guard.py`

**Date** : 2026-08-25 · **Status** : `accepted`

## Context

A Kubernetes diagnostic agent produces code whose correctness is hard to
assert by hand, and whose architectural rules (hexagonal imports, secrets,
cloud SDK usage) are easy to violate by accident. Relying on reviewer
goodwill is not sustainable.

## Decision

Make **TDD mandatory** and enforce architecture rules **deterministically**
with `hexa_guard.py`:

- **TDD**: RED → GREEN → REFACTOR; a source file has no value without its
  failing test (`tests/unit/test_{module}.py`).
- `hexa_guard.py` (R1–R15) runs on every Write/Edit and on `make guard`:
  hexagonal imports, no secrets, no `SELECT *`, no inline SQL, no direct LLM
  provider imports, no demo-adapter leakage.
- **Coverage is a floor**: full suite passes and `make coverage` ≥ 80%
  (domain/application expected well above).

## Alternatives considered

- **Code review only** — rejected: not deterministic, misses rule drifts.
- **Lint/type-check only** — rejected: covers style, not architecture.
- **No enforcement** — rejected: hexagonal rules erode over time.

## Consequences

- `hexa_guard.py` must pass for every change; if it flags you, the change is
  wrong — do not bypass it.
- Every new use case is generated with its port + test (see
  `scripts/generate_use_case_tests.py`).
- **Forbidden**: skipping a test, green-washing, silencing the guard.
- Reversible: rules are additive and versioned with the codebase.
