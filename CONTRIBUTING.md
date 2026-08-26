# Contributing to hexawyn

## Welcome & Quick Links

hexawyn is an open-source Kubernetes diagnosis and cost analysis tool. Before
you contribute:

- [README.md](README.md) — what hexawyn is and how to use it
- [AGENTS.md](AGENTS.md) — architecture rules enforced by `hexa_guard.py`
- [ARCHITECTURE.md](ARCHITECTURE.md) — the hexagonal layer map
- [docs/use-cases/](docs/use-cases/) — one documented flow per use case
- [Issues](https://github.com/hexa-tools/hexawyn/issues) — what needs help
- [SECURITY.md](SECURITY.md) — how to report vulnerabilities

## Contribution priorities

We accept contributions in this order of preference:

1. **Bug fixes** — a real reported symptom, fixed for the whole bug class
2. **Compatibility** — new providers, platforms, Python versions
3. **Security** — hardening, least privilege, secret handling
4. **Performance & robustness** — without changing behavior
5. **New features** — only after discussing on an issue first
6. **Documentation** — always welcome, including use-case diagrams

## Where to start

- Look for issues labeled `good first issue` or `help wanted`.
- **Search before you open**: issues, PRs, and the code — your problem may
  already be solved.
- **Comment on the issue first** before starting work: say what you plan to
  do, so we don't duplicate effort.
- Keep PRs **small and focused**. One fix or one feature per PR.

## Decision: Use case, MCP tool, Adapter, or Doc?

Before writing code, decide which layer your contribution belongs to:

| You want to… | Write a… | Where |
|---|---|---|
| Add business logic (a capability) | **Use case** | `application/` (driving port + ServicePort) |
| Expose a capability to an AI agent | **MCP tool** | one file in `mcp/tools/` |
| Support a new backend | **Adapter** | `adapters/` — implements a driven port, provider-aware |
| Explain a flow | **Doc** | `docs/use-cases/NN-<slug>.md` + `intent_examples.yaml` questions |

Wrong layer = rejected PR. If unsure, ask in the issue.

## GitHub workflow

### Issues

- Use the templates; add labels (`bug`, `enhancement`, `question`) when
  possible.
- A good bug report includes: expected vs actual, reproduction steps, hexawyn
  version, and the relevant log/output.
- The issue-management process (triage/deciding/rejected, stale, priority,
  issue-rating) is described in
  [docs/issue-management.md](docs/issue-management.md).

### Branches

- `main` is protected: no direct pushes, CI must pass.
- Work on short-lived branches: `feat/<slug>`, `fix/<slug>`, `docs/<slug>`.
- Rebase on `main` before opening the PR.

### Pull requests

- Open a **draft** PR early to get feedback; mark it ready when CI is green.
- Title follows conventional commits (`feat(scope): …`).
- Reference the issue: `Closes #123` in the description.
- CI gates must pass: `make check`, `make test`, `make test-integration`,
  `make docs-check`, coverage ≥ 80% (see [CI/CD Pipeline](#cicd-pipeline)).
- Review is **respectful and constructive**: explain, suggest, approve.

### Milestones & releases

- PRs merge to `main` (squash). Fixes are backported only when needed.
- Releases are cut from `main` via GitHub Release → `publish.yml` gates
  (TestPyPI → PyPI → Docker Hub).

## Security

- Do **not** open a public issue for a vulnerability.
- Report privately via [SECURITY.md](SECURITY.md) (private security advisory).
- Advisories are handled before public disclosure.

## Releasing

See [CI/CD Pipeline → Release (publish.yml)](#cicd-pipeline). Releases are
triggered from GitHub Releases, by maintainers only.

---

## Prerequisites

```bash
python 3.12+
poetry
git

# E2E tests only
docker + kubectl + k3d
```

## Quick start

```bash
git clone https://github.com/hexa-tools/hexawyn.git
cd hexawyn

make install       # poetry install --with dev
make test          # unit tests — no cluster needed
make test-integration  # integration tests — no cluster needed
make help          # all commands
```

That's it for most contributions. Unit + integration tests cover 95% of use
cases without any cluster.

## Test levels

| Level | Dir | Command | Requires |
|---|---|---|---|
| Unit | `tests/unit/` | `make test` | Nothing |
| Integration | `tests/integration/` | `make test-integration` | Nothing |
| E2E | `tests/e2e/` | `make test-e2e` | Docker + k3d |

Most contributors never need `make test-e2e`. E2E tests run nightly in CI.

## E2E tests (adapter contributions)

```bash
make cluster-up       # create k3d cluster with Jaeger + Prometheus (~120s)
make cluster-load     # deploy fixtures (pods, cert-manager, Tekton, KEDA)
make test-e2e         # run E2E tests against real cluster
make cluster-down     # cleanup free resources
```

**Cluster includes:** cert-manager, Tekton Pipelines, KEDA, Argo Rollouts, Jaeger, Prometheus.
**Fixtures:** crashloop pod, OOM pod, pending pod, high-CPU pod, healthy deployment,
cert-manager Issuer + Certificate, Tekton PipelineRun, KEDA ScaledObject.

## Architecture

```
domain/           pure business logic — zero external deps
application/      use cases, ports (ABC interfaces)
adapters/         primary (CLI, MCP) / secondary (k8s, cloud)
infrastructure/   DuckDB, config, encryption, telemetry
runtime/          agent tools & prompts
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full layer map, and
[AGENTS.md](AGENTS.md) for the rules enforced by `hexa_guard.py`.

## TDD workflow (mandatory)

1. Write test → RED
2. Implement source file
3. Run test → GREEN
4. Run `python hexa_guard.py` → approve

## Test file naming

```
tests/unit/test_{module}.py
tests/integration/test_{feature}_integration.py
tests/e2e/test_{scenario}_e2e.py
```

## Before opening a PR

```bash
make check               # ruff + format + mypy
make guard               # hexa_guard.py rules (R1–R15)
make test                # unit tests
make test-integration    # integration tests
make docs-check          # docs must not drift from code (anti-dérive)
make coverage            # coverage >= 80%

# Only if you touched src/hexawyn/adapters/
make cluster-up && make cluster-load && make test-e2e && make cluster-down
```

> **`make docs-check`** : toute modification de doc (ou d'API/use case) qui
> référence un symbole inexistant fait échouer la CI. Garde-toujours la doc
> alignée sur le code.

## Commit convention

```
feat(scope): new feature
fix(scope):  bug fix
test(scope): add or update tests
chore(scope): maintenance
docs(scope): documentation only
```

## CI/CD Pipeline

### What runs on every push/PR (ci.yml)

| Job | What it checks |
|---|---|
| **Code Quality** | `ruff check` + `ruff format --check` + `mypy` |
| **Unit Tests** | full unit suite + coverage ≥ 80% + Codecov report |
| **Integration Tests** | Real DuckDB + DemoAdapter, K8s mocked |
| **Docs Anti-Drift** | `tool/check_docs.py` — docs must not drift from code |
| **Docker Build** | Multi-arch (amd64, arm64) build validation |

### Nightly + on adapter changes

| Workflow | Trigger | What |
|---|---|---|
| `e2e-tests.yml` | Nightly 2am UTC + push on `dev` touching `adapters/**` | E2E suite against k3d cluster |

### Release (publish.yml)

Triggered by GitHub Release. Gates:

1. ✅ Unit tests pass (coverage ≥ 80%)
2. ✅ Integration tests pass
3. Prerelease → **TestPyPI**
4. Stable release → **PyPI** + **Docker Hub** (`hexatools/hexawyn:latest` + `:vX.Y.Z`)

## Pre-push checklist

Run before `git push`:

```bash
make check       # lint + format + mypy
make guard       # hexa_guard.py rules
make test        # unit tests
make docs-check  # docs anti-drift
```

CI enforces these automatically, but running locally saves time.

## Developer Certificate of Origin (DCO)

All contributors must sign-off each commit using `git commit -s`.
See [developercertificate.org](https://developercertificate.org/).
