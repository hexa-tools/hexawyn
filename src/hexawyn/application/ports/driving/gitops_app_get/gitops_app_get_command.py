from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GitOpsAppGetCommand:
    name: str
    namespace: str
