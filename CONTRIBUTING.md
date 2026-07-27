# Contributing to hexawyn

Thank you for contributing! hexawyn uses strict TDD, hexagonal architecture,
and `hexa_guard.py` to enforce architectural rules automatically.

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
make test-e2e         # run 51 E2E tests against real cluster
make cluster-down     # cleanup free resources
```

**Cluster includes:** cert-manager, Tekton Pipelines, KEDA, Argo Rollouts, Jaeger, Prometheus.
**Fixtures:** crashloop pod, OOM pod, pending pod, high-CPU pod, healthy deployment,
cert-manager Issuer + Certificate, Tekton PipelineRun, KEDA ScaledObject.

## Before opening a PR

```bash
make check               # ruff + mypy + hexa_guard
make test                # unit tests
make test-integration    # integration tests
make coverage            # coverage >= 80%

# Only if you touched src/hexawyn/adapters/
make cluster-up && make cluster-load && make test-e2e && make cluster-down
```

## Architecture

```
domain/           pure business logic — zero external deps
application/      use cases, ports (ABC interfaces)
adapters/         primary (CLI, MCP) / secondary (k8s, cloud)
infrastructure/   DuckDB, config, encryption, telemetry
lang_graph/       LangGraph orchestration nodes
```

See [AGENTS.md](AGENTS.md) for detailed architecture rules enforced by `hexa_guard.py`.

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
| **Unit Tests** | 5438 tests + coverage >= 80% + Codecov report |
| **Integration Tests** | Real DuckDB + DemoAdapter, K8s mocked |
| **Docker Build** | Multi-arch (amd64, arm64) build validation |

### Nightly + on adapter changes

| Workflow | Trigger | What |
|---|---|---|
| `e2e-tests.yml` | Nightly 2am UTC + push on `dev` touching `adapters/**` | E2E suite against k3d cluster |

### Release (publish.yml)

Triggered by GitHub Release. Gates:

1. ✅ Unit tests pass (coverage >= 80%)
2. ✅ Integration tests pass
3. Prerelease → **TestPyPI**
4. Stable release → **PyPI** + **Docker Hub** (`hexatools/hexawyn:latest` + `:vX.Y.Z`)

## Pre-push checklist

Run before `git push`:

```bash
make check       # lint + format + mypy + hexa_guard
make test        # unit tests
```

CI enforces these automatically, but running locally saves time.

## Developer Certificate of Origin (DCO)

All contributors must sign-off each commit using `git commit -s`.
See [developercertificate.org](https://developercertificate.org/).
