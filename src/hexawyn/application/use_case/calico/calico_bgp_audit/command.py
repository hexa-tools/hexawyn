from dataclasses import dataclass


@dataclass(frozen=True)
class CalicoBgpAuditCommand:
    """Empty command — Calico BGP config is cluster-scoped."""

    pass
