from dataclasses import dataclass


@dataclass(frozen=True)
class ClusterHeadroomSimulationCommand:
    namespace: str | None = None
