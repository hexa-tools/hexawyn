from dataclasses import dataclass


@dataclass(frozen=True)
class CalicoEncryptionStatusCommand:
    """Empty command — WireGuard status is cluster-scoped."""

    pass
