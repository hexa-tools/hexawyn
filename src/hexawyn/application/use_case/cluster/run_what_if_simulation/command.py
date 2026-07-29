from dataclasses import dataclass


@dataclass(frozen=True)
class RunWhatIfSimulationCommand:
    target_service: str = ""
    namespace: str = ""
    current_replicas: int | None = None
    proposed_replicas: int = 1
    current_cpu_utilization: float | None = None
