from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CiliumEncryptionStatusResponse:
    installed: bool = False
    status: str = "not_installed"
    mode: str = "UNKNOWN"
    encrypted_nodes: int = 0
    total_nodes: int = 0
    coverage: str | None = None
    note: str | None = None
    error: str | None = None
