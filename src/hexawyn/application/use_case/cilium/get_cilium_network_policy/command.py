from dataclasses import dataclass


@dataclass(frozen=True)
class GetCiliumNetworkPolicyCommand:
    name: str
    namespace: str | None = None

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("network policy name is required")
