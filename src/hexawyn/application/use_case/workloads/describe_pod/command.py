from dataclasses import dataclass


@dataclass(frozen=True)
class DescribePodCommand:
    namespace: str = ""
    pod_name: str = ""
