from dataclasses import dataclass


@dataclass(frozen=True)
class GetCalicoStatusCommand:
    """Empty command — Calico status takes no user parameters."""

    pass
