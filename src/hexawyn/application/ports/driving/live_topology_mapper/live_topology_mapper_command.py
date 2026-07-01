from dataclasses import dataclass


@dataclass(frozen=True)
class LiveTopologyMapperCommand:
    namespace: str | None = None
