# ADR-004 — DuckDB memory + versioned SQL in `.sql` files

**Date** : 2026-08-25 · **Status** : `accepted`

## Context

hexawyn persists history, incident memory, and semantic search vectors
(VSS). Inline SQL in Python makes schemas/query evolution unreadable,
ungit-reviewable, and error-prone (hardcoded `SELECT *`, no migrations).

## Decision

Use **DuckDB** as the in-process store, with all SQL in dedicated `.sql`
files under `infrastructure/memory/sql/`:

- `schema.sql`, `indexes.sql`, `search_similar.sql`, `migrations/vNNN_*.sql`.
- Loaded at runtime via `_load_sql(filename)` — **no SQL string literals in
  Python**.
- **L1 cache** in memory (`cache_l1_repository.py`); **L2** DuckDB/VSS.
- Parameters use `?` placeholders; **no `SELECT *`** (explicit columns).

## Alternatives considered

- **PostgreSQL** — rejected: heavy for a local CLI/agent, no embedded mode.
- **SQLite** — rejected: weak vector search; DuckDB VSS is a better fit.
- **Inline SQL in Python** — rejected: unreadable, unversioned, hexa_guard R13.

## Consequences

- Schema + queries are reviewable in PRs and safely migratable.
- `DuckDBUnavailableError` → degraded mode, never a crash.
- **Forbidden**: `SELECT *`, f-string SQL, inline SQL (hexa_guard R8, R13).
- Reversible: the storage backend is behind driven ports (`memory_port`).
