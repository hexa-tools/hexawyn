from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledJobsListCommand:
    namespace: str | None = None
