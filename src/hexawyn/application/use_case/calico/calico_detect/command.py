from dataclasses import dataclass


@dataclass(frozen=True)
class CalicoDetectCommand:
    """Empty command — Calico detection takes no user parameters."""

    pass
