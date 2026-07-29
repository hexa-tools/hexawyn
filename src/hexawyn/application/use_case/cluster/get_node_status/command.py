from dataclasses import dataclass


@dataclass(frozen=True)
class GetNodeStatusCommand:
    node_name: str | None = None
