# Contributing to hexawyn

## Developer Certificate of Origin (DCO)

All contributors must sign-off each commit using `git commit -s`:

```
git commit -s -m "your message"
```

This adds a `Signed-off-by:` trailer certifying you wrote the code and have the right to contribute it under the project license. See [developercertificate.org](https://developercertificate.org/).

```
Developer Certificate of Origin
Version 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the LICENSE file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the LICENSE file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.
```

## PR Checklist

- [ ] Commits are signed (`git log --show-signature`)
- [ ] Unit tests pass (`poetry run pytest tests/unit/`)
- [ ] Coverage >= 80% (`poetry run pytest tests/unit/ --cov=src/hexawyn --cov-fail-under=80`)
- [ ] Lint passes (`poetry run ruff check src/ tests/`)
- [ ] Type check passes (`poetry run mypy src/hexawyn/`)
- [ ] No secrets in code (hexa_guard.py)

## Architecture

hexawyn follows **Ports & Adapters** (Hexagonal Architecture):

```
domain/           # pure business logic — zero external deps
application/      # use cases, ports (ABC interfaces)
adapters/         # primary (CLI, MCP) / secondary (k8s, cloud)
infrastructure/   # DuckDB, config, encryption, telemetry
lang_graph/       # LangGraph orchestration nodes
```

See [AGENTS.md](AGENTS.md) for detailed rules enforced by `hexa_guard.py`.
