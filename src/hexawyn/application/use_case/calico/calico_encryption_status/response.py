from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CalicoEncryptionStatusResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    wireguard_enabled: bool | None = None
    mode: str | None = None
    per_node: list[object] = field(default_factory=list)
    summary: str | None = None
    error: str | None = None
