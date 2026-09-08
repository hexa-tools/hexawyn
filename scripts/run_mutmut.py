#!/usr/bin/env python3
"""Run the mutmut CLI with beartype.claw neutralized.

hexawyn's dependency set pulls ``py-key-value-*``, which calls
``beartype_this_package()`` at import. That installs beartype.claw's import hook,
and mutmut's mutant generation (multiprocessing.Pool) then recurses inside it and
segfaults. hexa-sec doesn't ship that dependency, so it runs plain ``mutmut``;
hexawyn needs this shim for the same ``mutmut run`` calls.

Usage: python scripts/run_mutmut.py <mutmut-args...>
"""

from __future__ import annotations

import beartype.claw as _claw

for _name in ("beartype_this_package", "beartype_all", "beartype_package"):
    setattr(_claw, _name, lambda *args, **kwargs: None)

import multiprocessing.context  # noqa: E402, F401
import multiprocessing.pool  # noqa: E402, F401

from mutmut.__main__ import cli  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(cli())
