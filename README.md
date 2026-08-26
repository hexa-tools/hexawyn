<p align="center">

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2.svg?logo=discord&logoColor=white)](https://discord.gg/HH3WsrnNw)
[![Tests](https://img.shields.io/badge/tests-8500%2B_passed-brightgreen.svg)]()
[![codecov](https://codecov.io/gh/hexa-tools/hexawyn/branch/main/graph/badge.svg?token=E6PJX17GA8)](https://codecov.io/gh/hexa-tools/hexawyn)
[![CI](https://github.com/hexa-tools/hexawyn/actions/workflows/ci.yml/badge.svg)](https://github.com/hexa-tools/hexawyn/actions/workflows/ci.yml)
[![Security](https://github.com/hexa-tools/hexawyn/actions/workflows/security.yml/badge.svg)](https://github.com/hexa-tools/hexawyn/actions/workflows/security.yml)
[![Docker Hub](https://img.shields.io/docker/pulls/hexatools/hexawyn.svg)](https://hub.docker.com/r/hexatools/hexawyn)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![Benchmark](https://img.shields.io/badge/benchmark-80.7%2F100-yellow.svg)](docs/benchmark/README.md)

</p>

<p align="center">
  <img
    src="https://raw.githubusercontent.com/hexa-tools/hexawyn/main/assets/hexawyn-logo-light.svg"
    alt="Hexawyn"
    width="900"
  />
</p>

# hexawyn

🧠 **AI-powered Kubernetes diagnosis & cost analysis** — driven by coding agents
(Claude, Codex, OpenCode, Cursor, Gemini) over **MCP**.

Point your agent at your cluster and ask in plain language: diagnose a
crashloop, explain a costly namespace, audit RBAC, trace a slow pipeline.
Hexawyn answers from **~130 use cases**, exposed as **~150 MCP tools**, on a
strict hexagonal, TDD-locked codebase.

## Quick start

```bash
# 1. Install
pipx install hexawyn        # or: pip install hexawyn

# 2. Point your coding agent at the cluster
hexa claude install          # also: hexa codex|opencode|cursor|gemini install

# 3. Ask
# In Claude: "why is payments-api crashing?" → hexawyn routes to analyze_pod_logs
```

The MCP server runs over stdio — your agent spawns it per session, no separate
process to manage.

## What it does

- **Diagnostics** — pod/namespace/cluster health, crashloop & OOM analysis,
  log search, event correlation, K8s topology.
- **Cost & FinOps** — compute cost, namespace waste, budget projection,
  rightsizing, optimization ROI.
- **GitOps & Security** — drift detection, unauthorized access / stale
  credentials / secret rotation audits, posture score.
- **Platform** — certificate status, KEDA, Tekton pipelines, ingress, OpenShift,
  spans/traces.

Capabilities are documented one-by-one with example questions + diagrams in
[`docs/use-cases/`](docs/use-cases/) (138).

## Architecture

Hexawyn is **hexagonal (Ports & Adapters)**: a pure testable core, providers
behind driven ports, and tools wired at the composition root.

```
domain/          pure business logic — zero external deps
application/     use cases + ports (driving/driven ABCs)
adapters/        primary (CLI, MCP) / secondary (k8s, cloud, duckdb, mock)
infrastructure/  DuckDB, config, logging, cache L1/L2
mcp/             FastMCP server — composition root
```

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for the full map and
[`docs/adr/`](docs/adr/) for the decisions behind it. Architectural rules are
**enforced** by `hexa_guard.py` (`make guard`).

## Installation

### Requirements

- Python 3.12+
- `pip` (or `pipx` on Linux)

### macOS / Windows

```bash
pip install hexawyn
```

### Linux (Debian/Ubuntu and similar)

Debian/Ubuntu enforce [PEP 668](https://peps.python.org/pep-0668/) — the system
Python refuses global `pip` installs. Use `pipx` (recommended) or a dedicated
virtual environment:

```bash
# Option A — pipx (recommended for CLI apps)
pipx install hexawyn

# Option B — dedicated virtual environment
python3 -m venv ~/.hexawyn-venv
~/.hexawyn-venv/bin/pip install hexawyn
```

> Other Linux distributions allow plain `pip install hexawyn`, but a virtual
> environment or `pipx` is still best practice.

Verify:

```bash
hexa --help
```

## Connect Hexawyn to your coding agent

Hexawyn exposes an MCP server (`python -m hexawyn.mcp.stdio`). Configure your
coding agent — the CLI remains fully usable independently:

```bash
hexa claude install        # Claude Code
hexa codex install         # Codex
hexa opencode install      # OpenCode
hexa cursor install        # Cursor
hexa gemini install        # Gemini CLI
hexa deepseek install      # DeepSeek Harness
```

Each client supports `hexa <client> status` / `hexa <client> uninstall`.
Installation is idempotent; uninstall removes only the `hexawyn` MCP server.

Requirements: the `hexa` CLI installed (see above) and the target coding agent
installed. The integration registers the server over stdio — no separate
process to manage.

**Explore the tools in a browser** (`make mcp-inspector`, or `npx
@modelcontextprotocol/inspector -- poetry run python -m hexawyn.mcp.stdio`):
each tool shows its description plus example queries (→ **Tools** tab,
http://localhost:6274).

> The coding agents are **optional** MCP clients. Hexawyn does not require any
> of them.

## Documentation

- [`ARCHITECTURE.md`](ARCHITECTURE.md) — hexagonal layer map
- [`docs/use-cases/`](docs/use-cases/) — 138 use cases (questions + diagrams)
- [`docs/adr/`](docs/adr/) — architecture decision records
- [`docs/benchmark/README.md`](docs/benchmark/README.md) — benchmark results
- [`docs/issue-management.md`](docs/issue-management.md) — issue triage process
- [`AGENTS.md`](AGENTS.md) — conventions enforced by `hexa_guard.py`

Docs are guarded: `make docs-check` fails if a doc references a symbol that no
longer exists.

## Contributing

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to contribute
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — community & engineering conduct
- `make docs-check` and `make guard` must pass before opening a PR

## 📊 Benchmark

Hexawyn is continuously benchmarked against real-world Kubernetes
troubleshooting scenarios.

→ [View latest benchmark results](docs/benchmark/README.md)
