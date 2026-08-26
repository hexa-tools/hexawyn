# ADR-001 — Hexagonal Architecture (Ports & Adapters)

**Date** : 2026-08-25 · **Status** : `accepted`

## Context

hexawyn talks to many external systems: Kubernetes, clouds
(AWS/GCP/Azure/OpenShift), DuckDB, LLM providers, Slack, and telemetry
(Jaeger/Prometheus). Without a firm boundary, diagnostic logic mixes with
each provider's implementation details, becomes impossible to unit test, and
breaks on every backend change.

We need a **pure, testable** business core (no SDK, no I/O), and
**interchangeable** providers behind interfaces.

## Decision

Adopt **Hexagonal Architecture (Ports & Adapters)**: `domain/` stays pure
(zero external dependencies), `application/` holds the `use cases` + the
`ports` (`driving`/`driven` ABCs), `adapters/` implements the ports.

- `domain/` **never** imports infrastructure or application.
- `application/use_case/` knows **only** the ports (ABCs), never the adapters.
- Every external need is a **driven port** (~127 present); every business
  capability is a **driving port** (one folder per use case, ~138).
- Adapter selection happens at the **composition root**
  (`mcp/server.py` → `build_*_adapter()`, `adapter_factory.py`), never in
  application code.

## Alternatives considered

- **Module-structured monolith** (no layer boundary) — rejected: providers
  leak into business logic, unit tests impossible.
- **Classic layered architecture (MVC)** — rejected: downward dependency to
  infrastructure remains, domain never isolated.
- **Microservices** — rejected: overkill for a standalone CLI/agent.

## Consequences

- The domain is testable without a cluster or SDK (mock the ports).
- Any new adapter = implement an existing port (provider-aware).
- **Forbidden**: importing `kubernetes`/`boto3`/`httpx`/`fastapi` in
  `domain/` or `application/`. Enforced by `hexa_guard.py` (R1, R5, R6).
- Reversible: no (founding choice), but the per-layer boundary can be
  refined.
