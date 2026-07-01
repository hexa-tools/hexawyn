from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GitOpsAppStatusCommand:
    name: str
    namespace: str
