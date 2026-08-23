<p align="center">

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-join-5865F2.svg?logo=discord&logoColor=white)](https://discord.gg/HH3WsrnNw)
[![Tests](https://img.shields.io/badge/tests-8490_passed-brightgreen.svg)]()
[![codecov](https://codecov.io/gh/hexa-tools/hexawyn/branch/main/graph/badge.svg?token=E6PJX17GA8)](https://codecov.io/gh/hexa-tools/hexawyn)
[![CI](https://github.com/hexa-tools/hexawyn/actions/workflows/ci.yml/badge.svg)](https://github.com/hexa-tools/hexawyn/actions/workflows/ci.yml)
[![Security](https://github.com/hexa-tools/hexawyn/actions/workflows/security.yml/badge.svg)](https://github.com/hexa-tools/hexawyn/actions/workflows/security.yml)
[![Docker Hub](https://img.shields.io/docker/pulls/hexatools/hexawyn.svg)](https://hub.docker.com/r/hexatools/hexawyn)




[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![Benchmark](https://img.shields.io/badge/benchmark-79.7%2F100-yellow.svg)](docs/benchmark/README.md)


</p>

<p align="center">
  <img
    src="https://raw.githubusercontent.com/hexa-tools/hexawyn/main/assets/hexawyn-logo-light.svg"
    alt="Hexawyn"
    width="900"
  />
</p>

# hexawyn

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
virtual environment instead:

```bash
# Option A — pipx (recommended for CLI apps)
pipx install hexawyn

# Option B — dedicated virtual environment
python3 -m venv ~/.hexawyn-venv
~/.hexawyn-venv/bin/pip install hexawyn
```

> Other Linux distributions (Fedora, Arch, Alpine...) allow plain
> `pip install hexawyn` when using the system Python, but a virtual
> environment or `pipx` is still best practice.

After installing, verify the CLI works:

```bash
hexa --help
```

## Connect Hexawyn to your coding agent

Hexawyn exposes an MCP server (`python -m hexawyn.mcp.stdio`) that coding agents
can consume as a tool backend. These commands configure your coding agent to
talk to that server — the Hexawyn CLI itself remains fully usable
independently.

```bash
hexa claude install        # Claude Code
hexa codex install         # Codex
hexa opencode install      # OpenCode
hexa cursor install        # Cursor
hexa gemini install        # Gemini CLI
```

Each client also supports `hexa <client> status` and `hexa <client> uninstall`.
Installation is idempotent, and uninstall removes only the `hexawyn` MCP server.

Requirements:

- The `hexa` CLI must be installed — see [Installation](#installation) above.
- The target coding agent must be installed where applicable.

The integration registers the server over stdio, so the coding agent spawns the
Hexawyn MCP server for each session — no separate server process to manage.

Inside Claude Code, this capability is also available as an agent skill
(`.claude/skills/hexawyn-mcp/`): install it by copying that folder to
`~/.claude/skills/`, then ask Claude Code to *"install the Hexawyn MCP
server"*.

Claude Code (and the other coding agents) are **optional** MCP clients. Hexawyn
does not require any of them.

## 📊 Benchmark

Hexawyn is continuously benchmarked against real-world Kubernetes troubleshooting scenarios.

→ [View latest benchmark results](docs/benchmark/README.md)

