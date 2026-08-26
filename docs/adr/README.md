# ADR — Architecture Decision Records

Hexawyn's structuring architecture decisions, dated and justified.
The code says *what*; the ADRs say *why*.

## Why ADRs?

- Avoid re-debating the same choices every six months.
- Onboard a newcomer (or an agent) on the *why*, not just the *what*.
- Make the non-negotiable architecture **defensible**: `hexa_guard.py`
  enforces the rules, the ADRs justify them.
- Track reversible decisions so you know how and when to roll back.

## Index

| ADR | Decision | Status |
|---|---|---|
| [ADR-001](ADR-001-hexagonal-architecture.md) | Hexagonal Architecture (Ports & Adapters) | accepted |
| [ADR-002](ADR-002-mcp-tool-surface.md) | MCP / FastMCP as the agent surface | accepted |
| [ADR-003](ADR-003-demo-adapter-selection.md) | DemoAdapter + `adapter_factory` selection | accepted |
| [ADR-004](ADR-004-duckdb-memory-sql.md) | DuckDB memory + versioned SQL in `.sql` files | accepted |
| [ADR-005](ADR-005-tdd-hexa-guard.md) | Strict TDD + enforced `hexa_guard.py` | accepted |

---

## ADR template

```markdown
# ADR-00N — Decision title

**Date** : YYYY-MM-DD · **Status** : `proposed` | `accepted` | `deprecated` | `superseded`

## Context

Why this decision is needed. The problem, the constraints, what triggered
the need to settle this.

## Decision

What was chosen, in one clear, verifiable sentence.
_« We choose X because … »_

## Alternatives considered

- **Option A** — why rejected.
- **Option B** — why rejected.

## Consequences

- Impact on code, tests, CI, docs.
- What becomes mandatory, what becomes forbidden.
- How to roll back (if reversible).
```
