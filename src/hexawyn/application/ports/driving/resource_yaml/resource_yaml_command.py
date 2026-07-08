from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceYAMLCommand:
    resource_name: str
    namespace: str
    kind: str
