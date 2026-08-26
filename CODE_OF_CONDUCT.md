# Code of Conduct — hexawyn

## Our commitment

hexawyn is built on two pillars: **hexagonal architecture** and **strict TDD**.
The same discipline applies to how we treat each other. In the interest of
fostering an open and welcoming community, we as contributors and maintainers
pledge to make participation in our project and our community a harassment-free
experience for everyone, regardless of age, body size, disability, ethnicity,
sex characteristics, gender identity and expression, level of experience,
education, socio-economic status, nationality, personal appearance, race,
religion, or sexual identity and orientation.

We also commit to a standard of **engineering conduct**: the architecture and
the test suite are not negotiable, and no contribution is worth weakening them.

## Engineering conduct

These rules are as binding as the community standards. They exist because the
codebase is designed to be navigable, testable, and durable — and every
contribution must preserve that.

### Architecture

- **Hexagonal layers are sacred.** `domain/` stays pure (zero external
  dependencies), `application/` contains use cases and ports, `adapters/`
  implements the ports. A contribution that crosses a layer boundary in the
  wrong direction is rejected — no exceptions, no "temporary" shortcuts.
- **`hexa_guard.py` must pass.** The architectural rules are enforced by the
  guard, not by goodwill. If the guard flags your change, the change is wrong —
  do not silence or bypass the guard.
- **Prefer extending to duplicating.** Before adding a module, check whether
  an existing port, use case, or adapter already covers the need.
- **Small, focused changes.** One fix or one feature per PR. A PR that
  "accidentally" touches unrelated files will be sent back.

### Testing

- **TDD is mandatory: RED → GREEN → REFACTOR.** Tests are written before the
  code they validate. Code without tests is not done.
- **No green-washing.** A test that passes without asserting anything, a test
  that is skipped to make CI green, or a test that mocks the code under test
  into meaninglessness is worse than no test. Never delete or disable a failing
  test to pass CI — fix the root cause.
- **Tests document behavior.** The suite is the specification. Name tests by
  behavior (`test_rejects_query_shorter_than_2_chars`), not by implementation.
- **Coverage is a floor, not a ceiling.** CI enforces ≥ 80%; the domain and
  application layers are expected to stay well above it.
- **E2E is part of the job.** Adapter contributions run the real-cluster suite
  (`make test-e2e`). If you cannot run it, say so in the PR — do not claim it
  passed.

### Honesty

- **Report real status.** "It works on my machine" is not a result — include
  the output, the command, and the environment. Never fabricate test output,
  coverage numbers, or CI results.
- **Docs must match code.** A documentation file that references a wrong
  symbol, a flow that no longer exists, or a command that fails is a bug.
  Update the docs you touch — the anti-drift check is part of CI.

## Community standards

Examples of behavior that contributes to a positive environment:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Giving and gracefully accepting constructive feedback — **on the code and
  the architecture, with evidence, never ad hominem**
- Focusing on what is best for the community and the long-term health of the
  codebase
- Showing empathy towards other community members

Examples of unacceptable behavior:

- The use of sexualized language or imagery, and sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic
  address, without explicit permission
- Dismissing a report, a bug, or a contribution without a reason — "works on
  my machine" with no evidence is not a valid dismissal
- Any conduct that could reasonably be considered inappropriate in a
  professional setting

## Enforcement

Community leaders (maintainers) are responsible for clarifying and enforcing
our standards and will take appropriate and fair corrective action in response
to any behavior they deem inappropriate, threatening, offensive, or harmful.

Enforcement follows a graduated path, depending on severity:

1. **Correction** — a private, written warning explaining the violation
2. **Warning** — a warning with consequences for continued behavior
3. **Temporary ban** — a specified period of no interaction with the community
4. **Permanent ban** — for sustained harassment or severe violations

Maintainers may enforce the **engineering conduct** directly on contributions
(labeling a PR with the violated rule and closing it) without a community
warning — the architecture and the test suite are protected as strongly as the
community.

## Reporting

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the maintainers privately (private message or email —
never in a public issue). All complaints will be reviewed and investigated
promptly and fairly, with confidentiality respected for the reporter.

## Scope

This Code of Conduct applies within all project spaces — issues, pull
requests, discussions, documentation, the Discord server, and community events —
and also applies when an individual is officially representing the project in
public spaces.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, with the **Engineering conduct** section written specifically for
hexawyn's architecture-first, test-first culture.

[homepage]: https://www.contributor-covenant.org
