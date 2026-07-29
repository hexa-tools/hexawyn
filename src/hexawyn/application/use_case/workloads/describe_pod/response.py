from dataclasses import dataclass


@dataclass
class DescribePodResponse:
    pod_name: str = ""
    namespace: str = ""
    status: str = ""
    restarts: int = 0
    node: str = ""
    age: str = ""
    error: str | None = None
