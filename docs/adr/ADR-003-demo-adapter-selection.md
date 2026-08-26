# ADR-003 — DemoAdapter + `adapter_factory` selection

**Date** : 2026-08-25 · **Status** : `accepted`

## Context

hexawyn needs to run and be tested without a real cluster: CI (unit +
integration), demos, and rapid onboarding. But cloud detection
(`eks`/`aks`/`gke`) and direct adapter instantiation scattered around the
code would make the demo path non-testable and the providers non-ignorable.

## Decision

Provide a **DemoAdapter** and drive **all** adapter selection through
`adapters/secondary/adapter_factory.py`:

- `DEMO_MODE` → `DemoAdapter` (in `adapters/secondary/mock/`).
- Otherwise → detect the provider (`aws`/`gcp`/`azure`/`openshift`) or fall
  back to the `VanillaAdapter`.
- Adapters are **never instantiated** directly in application/use-case code.

## Alternatives considered

- **Hardcode the demo adapter in tests/CLI** — rejected: duplicates
  selection logic, leaks provider knowledge.
- **Detect + instantiate inline at each call site** — rejected: non-testable,
  violates ADR-001 (composition root owns wiring).
- **No demo mode** — rejected: CI/demos impossible without a cluster.

## Consequences

- Integration tests and demos run without Kubernetes.
- Adding a provider = extending `adapter_factory`, not touching use cases.
- **Forbidden**: `DemoAdapter` outside `adapters/secondary/mock/`; hardcoded
  adapter selection in application code (hexa_guard R10/R11).
- Reversible: the factory is a single point of truth.
