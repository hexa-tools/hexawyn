from dataclasses import dataclass


@dataclass(frozen=True)
class CalicoFelixMetricsCommand:
    """Empty command — Felix counters are cluster-scoped."""

    pass
