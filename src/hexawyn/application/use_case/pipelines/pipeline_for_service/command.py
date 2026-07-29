from dataclasses import dataclass


@dataclass(frozen=True)
class PipelineForServiceCommand:
    service_name: str
